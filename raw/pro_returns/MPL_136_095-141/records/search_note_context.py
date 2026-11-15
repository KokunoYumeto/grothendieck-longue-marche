#!/usr/bin/env python3
"""Search every authored research-note query against the complete context.

Imports ITEMS from research_items.py without altering it. Ripgrep itself
validates every regex, and only a successful search with return code 1 is
classified as no_match. Exact matching lines and optional raw-byte fields are
preserved in JSON; Markdown contains only queries, statuses, counts, and paths.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def load_items(path: Path):
    before = path.read_bytes()
    spec = importlib.util.spec_from_file_location('authored_research_items', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot import research_items.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if path.read_bytes() != before:
        raise RuntimeError('research_items.py changed during import; rerun after the edit completes.')
    items = module.ITEMS
    if not isinstance(items, (list, tuple)):
        raise TypeError('ITEMS must be a list or tuple')
    return items, hashlib.sha256(before).hexdigest()


def context_files(root: Path):
    if not root.is_dir():
        raise FileNotFoundError('Context root does not exist: ' + str(root))
    paths = sorted(path for path in root.rglob('*') if path.is_file())
    if not paths:
        raise ValueError('Context root contains no files')
    files = []
    for path in paths:
        content = path.read_bytes()
        if b'\x00' in content:
            raise ValueError('Non-text context file requires explicit handling: ' + str(path))
        files.append({'path': path.relative_to(root).as_posix(),
                      'size_bytes': len(content),
                      'sha256': hashlib.sha256(content).hexdigest()})
    return files


def error_item(identifier, query, status, message, returncode=None):
    return {'id': identifier, 'query': query, 'status': status,
            'matching_lines': 0, 'match_spans': 0, 'matched_file_count': 0,
            'path_counts': {}, 'hits': [], 'rg_returncode': returncode,
            'error': message}


def run_searches(items, context_root: Path, *, rg_bin=None, timeout=30):
    """Return a report without writing files or modifying research material."""
    root = Path(context_root).resolve()
    files = context_files(root)
    paths = [item['path'] for item in files]
    executable = rg_bin or shutil.which('rg')
    results = []
    seen_ids = set()
    for position, item in enumerate(items, 1):
        if not isinstance(item, dict):
            results.append(error_item(f'item_{position}', None, 'input_error', 'Item is not a dictionary'))
            continue
        identifier = item.get('id')
        query = item.get('query')
        if not isinstance(identifier, str) or not identifier:
            results.append(error_item(f'item_{position}', query, 'input_error', 'Missing nonempty string id'))
            continue
        if identifier in seen_ids:
            results.append(error_item(identifier, query, 'input_error', 'Duplicate note id'))
            continue
        seen_ids.add(identifier)
        if not isinstance(query, str) or not query:
            results.append(error_item(identifier, query, 'input_error', 'Missing nonempty string query'))
            continue
        if not executable:
            results.append(error_item(identifier, query, 'tool_error', 'rg executable is unavailable'))
            continue
        common = [str(executable), '--no-config', '--json', '--ignore-case',
                  '--color', 'never', '--regexp', query, '--']
        try:
            # Validation uses the actual rg regex engine, rather than Python's.
            validation = subprocess.run(common + ['/dev/null'], cwd=root,
                                        capture_output=True, text=True, timeout=timeout)
            if validation.returncode not in (0, 1):
                message = validation.stderr.strip() or 'rg failed during regex validation'
                regex_messages = ('regex parse error', 'regex error', 'not allowed in a regex',
                                  'compiled regex exceeds', 'regex is too big')
                status = 'regex_error' if any(token in message.lower() for token in regex_messages) else 'tool_error'
                results.append(error_item(identifier, query, status, message, validation.returncode))
                continue
            process = subprocess.run(common + paths, cwd=root, capture_output=True,
                                     text=True, timeout=timeout)
        except subprocess.TimeoutExpired as error:
            results.append(error_item(identifier, query, 'tool_error', f'rg timed out after {timeout}s'))
            continue
        except OSError as error:
            results.append(error_item(identifier, query, 'tool_error', str(error)))
            continue
        if process.returncode not in (0, 1):
            results.append(error_item(identifier, query, 'tool_error',
                                      process.stderr.strip() or 'rg search failed', process.returncode))
            continue
        hits = []
        parse_error = None
        try:
            for record in process.stdout.splitlines():
                event = json.loads(record)
                if event.get('type') != 'match':
                    continue
                data = event['data']
                hit = {'path': data['path'].get('text'),
                       'line': data['line_number'],
                       'text': data['lines'].get('text'),
                       'absolute_byte_offset': data['absolute_offset'],
                       'submatches': data['submatches']}
                if 'bytes' in data['path']:
                    hit['path_base64'] = data['path']['bytes']
                if 'bytes' in data['lines']:
                    hit['text_base64'] = data['lines']['bytes']
                hits.append(hit)
        except (json.JSONDecodeError, KeyError, TypeError) as error:
            parse_error = 'Cannot parse rg JSON output: ' + str(error)
        if parse_error:
            results.append(error_item(identifier, query, 'tool_error', parse_error, process.returncode))
            continue
        if (process.returncode == 0 and not hits) or (process.returncode == 1 and hits):
            results.append(error_item(identifier, query, 'tool_error',
                                      'rg return code disagrees with parsed match events', process.returncode))
            continue
        counts = collections.Counter(hit['path'] or '[base64 path]' for hit in hits)
        results.append({'id': identifier, 'query': query,
                        'status': 'matched' if process.returncode == 0 else 'no_match',
                        'matching_lines': len(hits),
                        'match_spans': sum(len(hit['submatches']) for hit in hits),
                        'matched_file_count': len(counts),
                        'path_counts': dict(sorted(counts.items())),
                        'hits': hits, 'rg_returncode': process.returncode,
                        'stderr': process.stderr})
    # A source change during a batch could invalidate the file hashes/citations.
    after = context_files(root)
    if after != files:
        raise RuntimeError('Context files changed during the search batch; output was not written.')
    statuses = collections.Counter(item['status'] for item in results)
    summary = {'notes': len(results), 'context_files': len(files),
               **{name: statuses[name] for name in ('matched', 'no_match', 'regex_error', 'tool_error', 'input_error')},
               'matching_lines_total': sum(item['matching_lines'] for item in results)}
    return {'schema_version': 1,
            'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
            'context_root': str(root), 'context_files': files,
            'search_settings': {'tool': str(executable) if executable else None,
                                'case_insensitive': True,
                                'engine': 'ripgrep default Rust regex engine',
                                'regex_validation': 'rg against /dev/null before each full-context search',
                                'query_transformation': 'none',
                                'hit_unit': 'one matching source line; individual spans retained in submatches'},
            'summary': summary, 'notes': results}


def inline(value):
    value = str(value).replace('\r', '').replace('\n', ' ↵ ').replace('|', '\\|')
    fence = '`' * max(1, 1 + max((len(m.group()) for m in re.finditer(r'`+', value)), default=0))
    return fence + value + fence


def markdown(report):
    summary = report['summary']
    lines = ['# Per-note searches of the supplied context', '',
             'Every query is searched case-insensitively, without alteration, over every supplied context text file. '
             'The companion JSON preserves exact matching lines and paths. A `no_match` result means regex validation '
             'succeeded and ripgrep returned 1; regex errors and tool failures are separate statuses.', '',
             f'Generated: {report["generated_utc"]}. Notes: {summary["notes"]}; context files: {summary["context_files"]}; '
             f'matched: {summary["matched"]}; no match: {summary["no_match"]}; '
             f'errors: {summary["regex_error"] + summary["tool_error"] + summary["input_error"]}.', '',
             '## Context coverage', '']
    lines.extend('- ' + inline(item['path']) for item in report['context_files'])
    lines.extend(['', '## Queries and results', '',
                  '| Note | Query | Status | Matching lines | Files | Matching paths (line counts) |',
                  '|---|---|---|---:|---:|---|'])
    for item in report['notes']:
        coverage = '; '.join(inline(path) + f' ({count})' for path, count in item['path_counts'].items()) or '—'
        lines.append('| ' + inline(item['id']) + ' | ' + inline(item['query']) + ' | ' + item['status'] +
                     f' | {item["matching_lines"]} | {item["matched_file_count"]} | ' + coverage + ' |')
    failures = [item for item in report['notes'] if item['status'].endswith('_error')]
    if failures:
        lines.extend(['', '## Errors requiring attention', ''])
        for item in failures:
            lines.append('- ' + inline(item['id']) + ': ' + inline(item.get('error', 'Unspecified error')))
    lines.extend(['', 'Matching counts measure source lines, not independent propositions. '
                  'A search hit is a lead; a no-match is bounded to the supplied context and chosen regex.', ''])
    return '\n'.join(lines)


def main():
    records = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--items', type=Path, default=records / 'research_items.py')
    parser.add_argument('--context', type=Path, default=records.parent.parent / 'context')
    parser.add_argument('--json', type=Path, default=records / 'note_context_searches.json')
    parser.add_argument('--markdown', type=Path, default=records / 'note_context_searches.md')
    parser.add_argument('--timeout', type=float, default=30)
    args = parser.parse_args()
    try:
        items, source_hash = load_items(args.items.resolve())
        report = run_searches(items, args.context, timeout=args.timeout)
        report['query_source'] = str(args.items.resolve())
        report['query_source_sha256'] = source_hash
        # Never overwrite a good report with an incompletely captured batch.
        for destination, body in ((args.json, json.dumps(report, ensure_ascii=False, indent=2) + '\n'),
                                  (args.markdown, markdown(report))):
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_name(destination.name + '.tmp')
            temporary.write_text(body, encoding='utf-8')
            temporary.replace(destination)
    except Exception as error:
        print('FATAL: search reports not updated: ' + str(error), file=sys.stderr)
        return 2
    print(json.dumps({'summary': report['summary'], 'json': str(args.json.resolve()),
                      'markdown': str(args.markdown.resolve())}, ensure_ascii=False))
    for item in report['notes']:
        if item['status'].endswith('_error'):
            print(json.dumps({'id': item['id'], 'status': item['status'], 'error': item['error']}, ensure_ascii=False))
    return 1 if any(item['status'].endswith('_error') for item in report['notes']) else 0


if __name__ == '__main__':
    raise SystemExit(main())

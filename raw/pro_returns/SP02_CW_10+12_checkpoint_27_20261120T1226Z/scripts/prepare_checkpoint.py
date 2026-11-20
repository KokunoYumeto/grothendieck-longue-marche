#!/usr/bin/env python3
"""Prepare a bounded checkpoint snapshot; never package, upload or schedule it.

Default mode checks metadata/hashes and reports the plan without writes.
--write runs the existing script refresher, ordered assembler and lexical
checker, preserving pages, records, reports and event logs. Provisional files
must already be supplied by root; their contents are hashed, never interpreted.
Audit sessions, immutable history and image-first receipts are also protected
recursively, including their filename sets. Missing audit trees are permitted;
symlinks and special files in those trees are rejected before hashing.
Only page_map.tsv metadata is read from the witness directory.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True

import assemble_and_index as assembly_tool
import refresh_checkpoint_documentation as refresh_tool
from validate_tex import validate_text

DEFAULT_OUTPUT = Path(__file__).resolve().parents[1]
PREFIX = 'SP02_CW_10+12'
AUDIT_STATE_DIRS = ('documentation/audit_sessions',
                    'documentation/page_history',
                    'documentation/audit_image_first')


def digest(path: Path) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Refusing a symlink, missing file or non-file: {path}')
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def audit_state_files(output: Path) -> set[Path]:
    """Enumerate optional audit trees without following any symlink component."""
    files = set()
    for name in AUDIT_STATE_DIRS:
        root = output
        for part in Path(name).parts:
            root = root / part
            if root.is_symlink():
                raise ValueError(f'Audit-state paths may not contain symlinks: {root}')
            if root.exists() and not root.is_dir():
                raise ValueError(f'Audit-state directory is not a directory: {root}')
        if not root.exists():
            continue
        pending = [root]
        while pending:
            for path in pending.pop().iterdir():
                if path.is_symlink():
                    raise ValueError(f'Audit-state paths may not contain symlinks: {path}')
                if path.is_dir():
                    pending.append(path)
                elif path.is_file():
                    files.add(path)
                else:
                    raise ValueError(f'Audit-state path is not a regular file or directory: {path}')
    return files


def protected_snapshot(output: Path) -> dict:
    files = set((output / 'pages').rglob('*.tex'))
    files.update((output / 'documentation/page_records').rglob('*.json'))
    files.update(audit_state_files(output))
    for name in ['progress.log', 'CHECK_EVENTS.tsv',
                 *[f'{PREFIX}_{kind}' for kind in
                   ['changes.md', 'collation.tsv', 'inventory.csv', 'doubts.md']]]:
        files.add(output / name)
    for name in [f'{PREFIX}_audit.md', 'documentation/editorial_metadata.json']:
        if (output / name).exists():
            files.add(output / name)
    return {str(path.relative_to(output)): digest(path) for path in sorted(files)}


def source_snapshot(work: Path) -> dict:
    work = Path(work).resolve()
    return {str(source.relative_to(work)): digest(source)
            for source, _ in refresh_tool.scoped_sources(work)}


def provisional_snapshot(output: Path, relative_paths: list[str]) -> dict:
    result = {}
    for name in relative_paths:
        relative = Path(name)
        if (relative.is_absolute() or '..' in relative.parts or not relative.parts
                or relative.parts[0] != 'documentation'
                or relative.suffix.lower() not in {'.md', '.json', '.py', '.txt'}):
            raise ValueError('Provisional files must be explicit documentation paths inside output.')
        path = output
        for part in relative.parts:
            path = path / part
            if path.is_symlink():
                raise ValueError('Provisional paths may not contain symlinks.')
        result[str(relative)] = digest(path)
    return result


def prepare(checkpoint: int, expected_pages: int, last_page: str, *,
            output=DEFAULT_OUTPUT, work=None, witnesses=None,
            provisional=(), label=None, write=False) -> dict:
    output = Path(output).resolve()
    work = Path(work or output.parent / 'work').resolve()
    witnesses = Path(witnesses or output.parent / 'source' / f'{PREFIX}_witnesses').resolve()
    label = label or f'{expected_pages:03d}'
    if checkpoint < 1 or expected_pages < 1 or not re.fullmatch(r'[A-Za-z0-9_.-]+', label):
        raise ValueError('Positive checkpoint/page counts and a filename-safe label are required.')
    map_path = witnesses / 'page_map.tsv'
    map_before = digest(map_path)
    with map_path.open(encoding='utf-8', newline='') as stream:
        mapped = list(csv.DictReader(stream, delimiter='\t'))
    keys = [f"{row['folder']}_{row['cote']}_scan{int(row['our_scan']):03d}" for row in mapped]
    if len(keys) != len(set(keys)) or expected_pages > len(keys):
        raise ValueError('Mapped identities are duplicated or expected page count exceeds the map.')
    for row, key in zip(mapped, keys):
        if Path(row['codex_file']).name != key + '.tex':
            raise ValueError('Mapped page filename differs from its folder/cote/scan identity.')
    expected_keys = keys[:expected_pages]
    if expected_keys[-1] != last_page:
        raise ValueError('Expected last page differs from the mapped prefix.')
    page_names = {str(p.relative_to(output / 'pages')) for p in (output / 'pages').rglob('*.tex')}
    record_dir = output / 'documentation/page_records'
    record_names = {str(p.relative_to(record_dir)) for p in record_dir.rglob('*.json')}
    if page_names != {key + '.tex' for key in expected_keys} or record_names != {key + '.json' for key in expected_keys}:
        raise ValueError('Page/record filenames do not equal the requested finalized map prefix.')
    pages = [output / 'pages' / (key + '.tex') for key in expected_keys]
    before = protected_snapshot(output)
    sources_before = source_snapshot(work)
    provisional_before = provisional_snapshot(output, list(provisional))
    for key in expected_keys:
        record = json.loads((record_dir / (key + '.json')).read_bytes())
        if record.get('key') != key or record.get('page_sha256') != before['pages/' + key + '.tex']['sha256']:
            raise ValueError(f'Record identity/page hash differs for {key}.')
    evidence = output / 'evidence'
    names = {kind: f'checkpoint{checkpoint:02d}_{kind}_{label}.json'
             for kind in ['refresh', 'assembly', 'lexical', 'preparation']}
    result = {'checkpoint': checkpoint, 'label': label, 'finalized_pages': expected_pages,
              'last_page': last_page, 'snapshot_valid': True, 'written': False,
              'ready': False, 'protected_inputs': before,
              'root_script_sources': sources_before, 'provisional_files': provisional_before,
              'map_metadata': map_before, 'evidence': names,
              'scope': 'Mechanical staging only. No archive/upload/schedule, images, witness prose, context, source-edit replay, reading decisions, audit or freeze.'}
    if not write:
        result['note'] = 'Read-only snapshot check; refresh, assembly and lexical checks were not executed.'
        return result
    if any((evidence / name).exists() for name in names.values()):
        raise FileExistsError('Preparation evidence already exists; use a new explicit label or page count.')
    evidence.mkdir(parents=True, exist_ok=True)

    def save(kind: str, value: dict) -> None:
        with (evidence / names[kind]).open('x', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2); stream.write('\n')

    def unchanged() -> None:
        if protected_snapshot(output) != before:
            raise ValueError('Protected pages/records/reports/logs or their filename set changed during staging.')
        if source_snapshot(work) != sources_before:
            raise ValueError('Root script sources or their filename set changed during staging.')
        if provisional_snapshot(output, list(provisional)) != provisional_before:
            raise ValueError('Root provisional files changed during staging.')
        if digest(map_path) != map_before:
            raise ValueError('Page-map metadata changed during staging.')

    result['stage_writes_attempted'] = True
    try:
        refreshed = refresh_tool.refresh(work, output)
        save('refresh', refreshed); unchanged()
        assembled = assembly_tool.assemble(witnesses, output, write=True)
        save('assembly', assembled); unchanged()
        lexical = {'checker': 'validate_tex lexical balance only',
                   'results': [validate_text(path.read_text(encoding='utf-8'), str(path)) for path in pages]}
        lexical['files'] = len(pages)
        lexical['ok'] = all(item['ok'] for item in lexical['results'])
        save('lexical', lexical); unchanged()
        combined = output / f'{PREFIX}_transcription.tex'
        if combined.read_bytes() != b''.join(path.read_bytes() for path in pages):
            raise ValueError('Combined bytes differ from the captured ordered page set.')
        if not lexical['ok']:
            raise ValueError('Lexical checks failed; inspect the saved lexical evidence.')
        unchanged()
        result.update(ready=True, written=True, protected_hashes_verified=len(before),
                      protected_inputs_unchanged=True, exact_ordered_concatenation=True,
                      copied_files=refreshed['copied_files'], combined=digest(combined),
                      lexical={'ok': True, 'files': len(pages)})
    except Exception as exc:
        result.update(error=f'{type(exc).__name__}: {exc}', written=True)
        try:
            result['protected_inputs_unchanged'] = protected_snapshot(output) == before
        except (OSError, ValueError) as snapshot_error:
            result['protected_inputs_unchanged'] = None
            result['protected_readback_error'] = str(snapshot_error)
    result['completed_utc'] = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    save('preparation', result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=int, required=True)
    parser.add_argument('--expected-pages', type=int, required=True)
    parser.add_argument('--last-page', required=True)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--work', type=Path)
    parser.add_argument('--witness-root', type=Path)
    parser.add_argument('--provisional', action='append', default=[], metavar='DOCUMENTATION_PATH')
    parser.add_argument('--label', help='Distinct evidence suffix; default is the three-digit page count')
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = prepare(args.checkpoint, args.expected_pages, args.last_page, output=args.output,
                     work=args.work, witnesses=args.witness_root, provisional=args.provisional,
                     label=args.label, write=args.write)
    print(json.dumps({key: value for key, value in result.items()
                      if key not in {'protected_inputs', 'root_script_sources'}}, ensure_ascii=False, indent=2))
    if args.write and not result['ready']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

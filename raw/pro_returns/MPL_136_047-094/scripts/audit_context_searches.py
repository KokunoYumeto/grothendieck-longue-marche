#!/usr/bin/env python3
"""Reproduce the exact literal context queries recorded in research notes.

Usage:
    python scripts/audit_context_searches.py
    python scripts/audit_context_searches.py --context /path/to/context

Only the backtick-delimited queries before the first semicolon in each
**Context search:** clause are searched. Each is passed separately to rg with
--fixed-strings and --ignore-case across the five explicitly listed context
files. No TeX expansion, whitespace joining, stemming, synonym expansion or
semantic interpretation occurs. Therefore zero literal matches do not prove
the absence of a semantic match. The manual context comparisons in the notes
and context evidence memo remain authoritative.

match_count counts literal substring occurrences (rg JSON submatches);
matching_line_count counts matching source lines. Only the first twenty
matching file:line locations are retained, without copying source excerpts.
The run records actual UTC, a notes-source SHA-256, and a separate manifest of
the five context-source SHA-256 values. It writes only the requested audit and
manifest, and never changes the notes, transcription or supplied context.
"""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

CONTEXT_FILES = (
    'README.md',
    'notes/RESULTS_STATE.md',
    'PURSUING_STACKS_CONTENTS.md',
    'ps_chapters_VI_VII/ps6.tex',
    'ps_chapters_VI_VII/ps7.tex',
)
NOTE_HEADING = re.compile(r'^### (R\d{3})\s+—\s+', re.MULTILINE)
CLAUSE = re.compile(r'^\*\*Context search:\*\*\s*(.+)$', re.MULTILINE)
FIELDS = (
    'run_utc', 'note_id', 'query_index', 'query', 'search_mode',
    'match_count', 'matching_line_count', 'first_up_to20_file_line_locations',
    'notes_source_sha256', 'interpretation_limit',
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def query_prefix(clause: str) -> str:
    """Find the first semicolon outside the literal backtick spans."""
    in_code = False
    for i, char in enumerate(clause):
        if char == '`':
            in_code = not in_code
        elif char == ';' and not in_code:
            return clause[:i]
    raise ValueError('Context-search clause has no terminating semicolon')


def extract_queries(notes: str, expected_notes: int) -> list[tuple[str, int, str]]:
    headings = list(NOTE_HEADING.finditer(notes))
    expected = [f'R{i:03}' for i in range(1, expected_notes + 1)]
    actual = [m.group(1) for m in headings]
    if actual != expected:
        raise ValueError(f'Expected ordered notes {expected[0]}–{expected[-1]}; got {actual}')
    result = []
    for i, heading in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(notes)
        block = notes[heading.end():end]
        clauses = list(CLAUSE.finditer(block))
        if len(clauses) != 1:
            raise ValueError(f'{heading.group(1)} has {len(clauses)} context-search clauses')
        prefix = query_prefix(clauses[0].group(1))
        queries = re.findall(r'`([^`]+)`', prefix)
        if not queries or any(not q.strip() for q in queries):
            raise ValueError(f'{heading.group(1)} has no usable literal queries')
        for j, query in enumerate(queries, 1):
            result.append((heading.group(1), j, query))
    return result


def search(rg: str, context: Path, query: str) -> tuple[int, int, list[str]]:
    command = [rg, '--fixed-strings', '--ignore-case', '--json', '--color',
               'never', '--threads', '1', '--sort', 'path', '--', query, *CONTEXT_FILES]
    proc = subprocess.run(command, cwd=context, text=True, encoding='utf-8',
                          capture_output=True, check=False)
    if proc.returncode not in (0, 1):
        raise RuntimeError(f'rg failed for {query!r}: {proc.stderr.strip()}')
    occurrences = 0
    matching_lines = 0
    locations = []
    for line in proc.stdout.splitlines():
        event = json.loads(line)
        if event.get('type') != 'match':
            continue
        data = event['data']
        occurrences += len(data['submatches'])
        matching_lines += 1
        if len(locations) < 20:
            source = data['path'].get('text')
            if source is None:
                raise RuntimeError('Unexpected non-UTF-8 source path from rg')
            locations.append(f"{source}:{data['line_number']}")
    return occurrences, matching_lines, locations


def main() -> int:
    work = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--context', type=Path, default=work.parent/'context')
    parser.add_argument('--notes', type=Path, default=work/'MPL_136_047-094_notes.md')
    parser.add_argument('--output', type=Path, default=work/'research/context_search_audit.tsv')
    parser.add_argument('--manifest', type=Path,
                        default=work/'research/context_sources.sha256')
    parser.add_argument('--expected-notes', type=int, default=65)
    args = parser.parse_args()
    rg = shutil.which('rg')
    if not rg:
        raise RuntimeError('rg is required for this literal-search audit')
    context = args.context.resolve()
    sources = [context/name for name in CONTEXT_FILES]
    for path in sources:
        if not path.is_file():
            raise FileNotFoundError(path)
    context_hashes = [sha256(path) for path in sources]
    notes_bytes = args.notes.read_bytes()
    notes_hash = hashlib.sha256(notes_bytes).hexdigest()
    queries = extract_queries(notes_bytes.decode('utf-8'), args.expected_notes)
    run_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    rows = []
    # Queries are intentionally executed for every note, even when repeated.
    for note_id, query_index, query in queries:
        count, line_count, locations = search(rg, context, query)
        rows.append({
            'run_utc': run_utc, 'note_id': note_id, 'query_index': query_index,
            'query': query,
            'search_mode': 'exact literal; rg fixed-string, case-insensitive',
            'match_count': count, 'matching_line_count': line_count,
            'first_up_to20_file_line_locations': '; '.join(locations),
            'notes_source_sha256': notes_hash,
            'interpretation_limit': 'Literal hits only; zero does not exclude semantic matches; manual notes/memo comparisons remain authoritative.',
        })
    if [sha256(path) for path in sources] != context_hashes:
        raise RuntimeError('A context source changed during the audit')
    if sha256(args.notes) != notes_hash:
        raise RuntimeError('The notes changed during the audit; rerun on their final version')
    if {row['note_id'] for row in rows} != {f'R{i:03}' for i in range(1, args.expected_notes+1)}:
        raise RuntimeError('Not every expected research note is represented')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    args.manifest.write_text(''.join(f'{digest}  {name}\n'
                                   for digest, name in zip(context_hashes, CONTEXT_FILES)),
                             encoding='utf-8')
    print(f'Audited {args.expected_notes} notes and {len(rows)} literal queries at {run_utc}.')
    print(f'Zero-hit literal queries: {sum(row["match_count"] == 0 for row in rows)}.')
    print(f'Audit: {args.output}')
    print(f'Context-source manifest: {args.manifest}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

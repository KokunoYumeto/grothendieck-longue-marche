#!/usr/bin/env python3
"""Structural checks only; never OCR, interpret, or alter manuscript readings.

Run after assembling the package. --partial permits an unfinished page set and
an absent combined file/freeze marker. Freeze records should use sha256sum form:
<64 hexadecimal digits>  <path relative to package root>
The same lines must appear in progress.log, before the transcription-frozen line.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

PREFIX = 'MPL_136_095-141'
SCANS = [n for n in range(95, 142) if n != 122]
FIELDS = ['cote', 'scan', 'sheet_kind', 'element', 'kind', 'position',
          'first_words_or_objects', 'transcribed']
SHEET_KINDS = {'text', 'reused_typed', 'cancelled_draft', 'cover'}
ELEMENT_KINDS = {'text', 'display', 'diagram', 'drawing', 'margin note',
                 'insertion', 'deletion'}


def unescaped_source(source: str) -> str:
    """Blank comments and escaped control symbols, preserving line numbers."""
    result = []
    i = 0
    while i < len(source):
        c = source[i]
        if c == '%':
            j = source.find('\n', i)
            j = len(source) if j < 0 else j
            result.extend(' ' * (j - i))
            i = j
        elif c == '\\' and i + 1 < len(source):
            if source[i + 1].isalpha():
                result.append(c)
                i += 1
                while i < len(source) and source[i].isalpha():
                    result.append(source[i])
                    i += 1
            else:
                result.extend('  ' if source[i + 1] != '\n' else ' \n')
                i += 2
        else:
            result.append(c)
            i += 1
    return ''.join(result)


def brace_errors(source: str) -> list[str]:
    stack = []
    errors = []
    line = 1
    for c in unescaped_source(source):
        if c == '\n':
            line += 1
        elif c == '{':
            stack.append(line)
        elif c == '}':
            if stack:
                stack.pop()
            else:
                errors.append(f'unmatched closing brace at line {line}')
    errors.extend(f'unclosed opening brace at line {n}' for n in stack)
    return errors


def hash_records(log: str) -> dict[str, str]:
    records = {}
    patterns = [
        re.compile(r'^(?:(?:sha256|SHA256|SHA-256)\s+)?([a-fA-F0-9]{64})\s+\*?(.+?)\s*$'),
        re.compile(r'^(?:sha256|SHA256|SHA-256)\s+(.+?)\s+([a-fA-F0-9]{64})\s*$'),
    ]
    for line in log.splitlines():
        first = patterns[0].match(line)
        if first:
            digest, name = first.groups()
        else:
            second = patterns[1].match(line)
            if not second:
                continue
            name, digest = second.groups()
        records[name.removeprefix('./')] = digest.lower()
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--partial', action='store_true')
    args = parser.parse_args()
    root = args.root.resolve()
    problems = []
    warnings = []
    page_paths = {n: root / 'pages' / f'{PREFIX}_136_scan{n:03d}.tex' for n in SCANS}
    actual = set((root / 'pages').glob('*.tex'))
    expected = set(page_paths.values())
    missing = [n for n, p in page_paths.items() if not p.is_file()]
    if missing:
        (warnings if args.partial else problems).append('missing scans: ' + ', '.join(map(str, missing)))
    if extra := actual - expected:
        problems.append('unexpected page filenames: ' + ', '.join(p.name for p in sorted(extra)))
    present = {n: p for n, p in page_paths.items() if p.is_file()}
    sources = {}
    for n, p in present.items():
        try:
            source = p.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as error:
            problems.append(f'{p.name}: {error}')
            continue
        sources[n] = source
        problems.extend(f'{p.name}: {error}' for error in brace_errors(source))
        markers = re.findall(r'\\scanpage\s*\{\s*(\d+)\s*\}', unescaped_source(source))
        if [int(m) for m in markers] != [n]:
            problems.append(f'{p.name}: expected one scanpage marker for {n}, got {markers}')
    combined_path = root / f'{PREFIX}_transcription.tex'
    if combined_path.is_file():
        combined = combined_path.read_bytes()
        parts = [p.read_bytes() for p in present.values()]
        if not any(combined == separator.join(parts) for separator in (b'', b'\n', b'\n\n')):
            problems.append('combined transcription is not an exact ordered concatenation (zero, one, or two separator newlines)')
        text = combined.decode('utf-8')
        if not text.lstrip().startswith('\\cotefile{136}'):
            problems.append('combined transcription does not start with \\cotefile{136}')
        if re.search(r'\\(?:documentclass|begin\s*\{document\})', text):
            problems.append('combined transcription contains a document preamble or document environment')
    else:
        (warnings if args.partial else problems).append('combined transcription is absent')
    inventory_path = root / f'{PREFIX}_inventory.csv'
    if inventory_path.is_file():
        with inventory_path.open(encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != FIELDS:
                problems.append(f'inventory columns differ: {reader.fieldnames}')
            rows = list(reader)
        counts = Counter()
        identifiers = set()
        for index, row in enumerate(rows, 2):
            try:
                scan = int(row.get('scan', ''))
            except ValueError:
                problems.append(f'inventory row {index}: invalid scan')
                continue
            counts[scan] += 1
            if scan not in present:
                problems.append(f'inventory row {index}: scan {scan} has no page file')
            if row.get('cote') != '136':
                problems.append(f'inventory row {index}: cote is not 136')
            if row.get('sheet_kind') not in SHEET_KINDS:
                problems.append(f'inventory row {index}: invalid sheet_kind')
            if row.get('kind') not in ELEMENT_KINDS:
                problems.append(f'inventory row {index}: invalid kind')
            if row.get('transcribed') != 'yes':
                problems.append(f'inventory row {index}: transcribed is not yes')
            if not row.get('element'):
                problems.append(f'inventory row {index}: empty element identifier')
            key = (scan, row.get('element'))
            if key in identifiers:
                problems.append(f'inventory row {index}: duplicate scan/element identifier')
            identifiers.add(key)
        if absent := sorted(set(present) - set(counts)):
            problems.append('present scans without inventory rows: ' + ', '.join(map(str, absent)))
    else:
        problems.append('inventory is absent')
        rows = []
    log_path = root / 'progress.log'
    if log_path.is_file():
        log = log_path.read_text(encoding='utf-8')
        frozen = re.search(r'^transcription frozen .+$', log, re.M)
        records = hash_records(log[:frozen.start()] if frozen else log)
        if not frozen:
            (warnings if args.partial else problems).append('no transcription frozen line in progress.log')
        if frozen:
            hash_targets = [*present.values(), combined_path]
            for path in hash_targets:
                relative = path.relative_to(root).as_posix()
                expected_hash = records.get(relative) or records.get(str(path))
                if not expected_hash:
                    problems.append(f'no frozen SHA-256 for {relative}')
                elif not path.is_file():
                    problems.append(f'frozen target is absent: {relative}')
                elif hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
                    problems.append(f'frozen SHA-256 mismatch: {relative}')
            audited = {int(n) for n in re.findall(r'^scan (\d+) audited .+$', log[:frozen.start()], re.M)}
            if absent := sorted(set(present) - audited):
                problems.append('scans without pre-freeze audit log: ' + ', '.join(map(str, absent)))
    else:
        problems.append('progress.log is absent')
    for item in warnings:
        print('WARNING:', item)
    for item in problems:
        print('ERROR:', item)
    print(f'Structural check: {len(present)}/{len(SCANS)} page files; {len(rows)} inventory rows; '
          f'{len(problems)} errors; {len(warnings)} warnings.')
    print('This check cannot establish transcription accuracy or visual completeness.')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())

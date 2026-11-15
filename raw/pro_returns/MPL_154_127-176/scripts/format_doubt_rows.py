#!/usr/bin/env python3
"""Format the mechanical uncertainty extraction as a complete Markdown table.

This formatter does not inspect images, consult context, or interpret manuscript
content. Confidence is assigned exclusively by the root agent's explicit rules:
low for illegible markers, alternative readings, scans 141/153/162/166/168,
multiline arguments, or arguments longer than 100 characters; medium otherwise.
It never assigns high confidence to an uncertainty marker.

Run:
    python3 scripts/format_doubt_rows.py --root /absolute/package/path

Inputs are read only. Outputs are records/doubt_rows.md and
records/doubt_rows_generation.txt. Every input occurrence produces one table row.
"""

from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import html
import io
from pathlib import Path


LOW_SCANS = {141, 153, 162, 166, 168}
REQUIRED_FIELDS = [
    'scan', 'tex_line', 'macro', 'complete_argument', 'source_snippet',
]


def split_top_level(argument: str) -> list[str]:
    """Split literal top-level pipes while respecting braces and TeX escapes.

    Comments are retained, but braces/pipes inside a comment do not affect the
    split. A backslash consumes the following character for lexical purposes;
    this correctly protects escaped braces, pipes, percent signs, and \\.
    No whitespace or argument content is stripped or normalized.
    """
    depth = 0
    index = 0
    start = 0
    parts: list[str] = []
    while index < len(argument):
        ch = argument[index]
        if ch == '\\':
            index += 2
            continue
        if ch == '%':
            newline = argument.find('\n', index)
            if newline < 0:
                index = len(argument)
                break
            index = newline + 1
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth < 0:
                raise ValueError('unmatched closing brace')
        elif ch == '|' and depth == 0:
            parts.append(argument[start:index])
            start = index + 1
        index += 1
    if depth != 0:
        raise ValueError(f'unbalanced braces (final depth {depth})')
    parts.append(argument[start:])
    if '|'.join(parts) != argument:
        raise AssertionError('split failed exact reconstruction')
    return parts


def code_cell(value: str) -> str:
    """Preserve literal source, escaping HTML and table separators."""
    escaped = html.escape(value, quote=True).replace('|', '&#124;')
    escaped = escaped.replace('\r', '&#13;').replace('\n', '<br>')
    return '<code>' + escaped + '</code>'


def protected_hashes(root: Path) -> dict[str, str]:
    paths = sorted((root / 'pages').glob('MPL_154_127-176_154_scan*.tex'))
    paths += [root / 'MPL_154_127-176_doubts.md',
              root / 'MPL_154_127-176_transcription.tex']
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in paths if p.is_file()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True, type=Path)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    source = root / 'records/doubts_extracted.csv'
    data = source.read_bytes()
    before = protected_hashes(root)
    reader = csv.DictReader(io.StringIO(data.decode('utf-8'), newline=''))
    if reader.fieldnames != REQUIRED_FIELDS:
        parser.error(f'unexpected CSV fields: {reader.fieldnames!r}')
    rows = list(reader)
    totals = Counter((row['scan'], row['tex_line']) for row in rows)
    seen: Counter[tuple[str, str]] = Counter()
    confidences: Counter[str] = Counter()
    macros: Counter[str] = Counter()
    alternatives = 0
    multiple_alternatives = 0
    multiline = 0
    long_arguments = 0
    output = [
        '| ID | cote | scan | Approximate location | Reading | Alternatives | Confidence |',
        '|---|---|---|---|---|---|---|',
    ]
    for serial, row in enumerate(rows, 1):
        scan = int(row['scan'])
        line = int(row['tex_line'])
        marker = row['macro']
        argument = row['complete_argument']
        if marker not in {r'\unsure', r'\illegible'}:
            raise ValueError(f'row {serial}: unsupported marker {marker!r}')
        try:
            parts = split_top_level(argument)
        except ValueError as exc:
            raise ValueError(f'row {serial}, scan {scan}, line {line}: {exc}') from exc
        has_alternative = len(parts) > 1
        is_multiline = '\n' in argument or '\r' in argument
        alternatives += has_alternative
        multiple_alternatives += len(parts) > 2
        multiline += is_multiline
        long_arguments += len(argument) > 100
        confidence = 'low' if (
            marker == r'\illegible' or has_alternative or scan in LOW_SCANS
            or is_multiline or len(argument) > 100
        ) else 'medium'
        confidences[confidence] += 1
        macros[marker] += 1
        key = (row['scan'], row['tex_line'])
        seen[key] += 1
        location = f'page source line {line}'
        if totals[key] > 1:
            location += f'; occurrence {seen[key]}/{totals[key]}'
        if marker == r'\illegible':
            if not argument.isdigit():
                raise ValueError(f'row {serial}: nonnumeric illegible word estimate')
            reading = f'unreadable ink; estimated {argument} words'
            alternative = '—'
        else:
            reading = code_cell(parts[0])
            alternative = code_cell('|'.join(parts[1:])) if has_alternative else '—'
        output.append(
            f'| D{serial:04d} | 154 | {scan} | {location} | '
            f'{reading} | {alternative} | {confidence} |'
        )
    if source.read_bytes() != data:
        raise RuntimeError('input CSV changed during formatting; refusing to write')
    after = protected_hashes(root)
    if before != after:
        raise RuntimeError('protected source files changed concurrently; rerun against stable input')
    markdown = '\n'.join(output) + '\n'
    # Every content row has exactly seven cells; source pipes are HTML entities.
    if any(len(line.split('|')) != 9 for line in output):
        raise AssertionError('incorrect Markdown table column count')
    destination = root / 'records/doubt_rows.md'
    destination.write_text(markdown, encoding='utf-8')
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    report = '\n'.join([
        f'Generated {stamp}',
        'Operation: mechanical per-occurrence uncertainty table formatting only.',
        f'Input: {source.relative_to(root)}',
        f'Input SHA-256: {hashlib.sha256(data).hexdigest()}',
        f'Input rows: {len(rows)}',
        f'Output content rows: {len(output)-2}',
        f'Output: {destination.relative_to(root)}',
        f'Output SHA-256: {hashlib.sha256(markdown.encode("utf-8")).hexdigest()}',
        f'Uncertain markers: {macros[chr(92)+"unsure"]}',
        f'Illegible markers: {macros[chr(92)+"illegible"]}',
        f'Low confidence by root rule: {confidences["low"]}',
        f'Medium confidence by root rule: {confidences["medium"]}',
        'High confidence: 0',
        f'Arguments with top-level alternatives: {alternatives}',
        f'Arguments with more than two alternatives: {multiple_alternatives}',
        f'Multiline arguments: {multiline}',
        f'Arguments longer than 100 characters: {long_arguments}',
        'Parser issues: 0',
        'Argument split/rejoin exact reconstruction: PASS',
        'Markdown seven-column check: PASS',
        'Source CSV byte preservation: PASS',
        f'Protected page/doubts/combined files unchanged: PASS ({len(before)} files)',
        'No image, context archive, or semantic manuscript interpretation used.',
        '',
    ])
    (root / 'records/doubt_rows_generation.txt').write_text(report, encoding='utf-8')
    print(report, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

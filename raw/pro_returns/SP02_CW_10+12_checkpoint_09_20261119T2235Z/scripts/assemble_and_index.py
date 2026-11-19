#!/usr/bin/env python3
"""Concatenate completed pages exactly and create lexical review indices.

No reading is decided or changed. The output contains only existing page files
in page_map order. Missing pages remain missing and are listed in the report.
Indices are navigation aids, not evidence of visual or mathematical checking.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_OUT = Path(__file__).resolve().parents[1]
DEFAULT_WITNESSES = DEFAULT_OUT.parent / 'source' / 'SP02_CW_10+12_witnesses'
PREFIX = 'SP02_CW_10+12'
COMMAND = re.compile(r'\\(?:[A-Za-z]+|.)', re.DOTALL)


def mask_comments(s: str) -> str:
    out = list(s)
    for i, ch in enumerate(s):
        if ch != '%':
            continue
        n, j = 0, i - 1
        while j >= 0 and s[j] == '\\':
            n += 1; j -= 1
        if n % 2:
            continue
        end = s.find('\n', i)
        if end < 0:
            end = len(s)
        out[i:end] = ' ' * (end - i)
    return ''.join(out)


def group_at(s: str, i: int) -> tuple[str, int]:
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s):
        return '', i
    if s[i] != '{':
        m = COMMAND.match(s, i)
        return (m.group(), m.end()) if m else (s[i], i + 1)
    start, depth = i, 0
    while i < len(s):
        if s[i] == '\\':
            m = COMMAND.match(s, i)
            i = m.end() if m else i + 1
            continue
        if s[i] == '{':
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0:
                return s[start:i+1], i + 1
        i += 1
    return s[start:], len(s)


def loc(s: str, pos: int) -> tuple[int, int]:
    return s.count('\n', 0, pos) + 1, pos - s.rfind('\n', 0, pos)


def snippet(s: str, start: int, end: int) -> str:
    return s[max(0, start - 40):min(len(s), end + 60)].replace('\n', ' ')


def index_page(text: str, row: dict, filename: str) -> list[dict]:
    clean = mask_comments(text)
    out = []
    common = {'folder': row['folder'], 'cote': row['cote'], 'scan': row['our_scan'], 'page_file': filename}
    for m in COMMAND.finditer(clean):
        after = m.end()
        while after < len(clean) and clean[after].isspace():
            after += 1
        arg, stop = group_at(clean, after) if after < len(clean) and clean[after] == '{' else ('', m.end())
        line, column = loc(clean, m.start())
        out.append({**common, 'type': 'control sequence', 'token': m.group(), 'argument': arg,
                    'line': line, 'column': column, 'context': snippet(text, m.start(), stop)})
    for m in re.finditer(r'[_^]', clean):
        # Escaped punctuation belongs to the control-sequence index above.
        n, j = 0, m.start() - 1
        while j >= 0 and clean[j] == '\\':
            n += 1; j -= 1
        if n % 2:
            continue
        arg, stop = group_at(clean, m.end())
        line, column = loc(clean, m.start())
        out.append({**common, 'type': 'script marker (lexical)', 'token': m.group(), 'argument': arg,
                    'line': line, 'column': column, 'context': snippet(text, m.start(), stop)})
    for m in re.finditer(r"``|''", clean):
        line, column = loc(clean, m.start())
        out.append({**common, 'type': 'paired quote (lexical)', 'token': m.group(), 'argument': '',
                    'line': line, 'column': column, 'context': snippet(text, m.start(), m.end())})
    return sorted(out, key=lambda r: (r['line'], r['column'], r['type']))


def assemble(witness_root: Path, output_root: Path, write=False, require_complete=False) -> dict:
    with (witness_root / 'page_map.tsv').open(encoding='utf-8') as f:
        mapped = list(csv.DictReader(f, delimiter='\t'))
    present, missing, indices, chunks = [], [], [], []
    for r in mapped:
        filename = Path(r['codex_file']).name
        page = output_root / 'pages' / filename
        if not page.exists():
            missing.append({'cote': r['cote'], 'scan': r['our_scan'], 'page_file': filename})
            continue
        raw = page.read_bytes()
        if raw and not raw.endswith(b'\n'):
            raise ValueError(f'{filename} lacks a final newline; correct explicitly before concatenation.')
        chunks.append(raw)
        present.append({'cote': r['cote'], 'scan': r['our_scan'], 'page_file': filename,
                        'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
        indices.extend(index_page(raw.decode('utf-8'), r, filename))
    if require_complete and missing:
        raise ValueError(f'Require-complete failed: {len(missing)} page files are missing.')
    raw = b''.join(chunks)
    combined = output_root / f'{PREFIX}_transcription.tex'
    report = {'present_pages': len(present), 'missing_pages': len(missing), 'pages': present,
              'missing': missing, 'combined': str(combined), 'combined_bytes': len(raw),
              'combined_sha256': hashlib.sha256(raw).hexdigest(), 'index_occurrences': len(indices),
              'cotefile_occurrences': dict(Counter(m.decode() for m in re.findall(rb'\\cotefile\{([^}]+)\}', raw))),
              'note': 'Exact byte concatenation. Repeated cotefile markers are reported, never removed. Indices are lexical aids, not checks.',
              'written': False}
    if not write:
        return report
    log = output_root / 'progress.log'
    frozen = log.exists() and ('transcription frozen ' in log.read_text(encoding='utf-8') or 'context opened ' in log.read_text(encoding='utf-8'))
    if frozen and (not combined.exists() or combined.read_bytes() != raw):
        raise ValueError('Frozen transcription differs from proposed concatenation; no mutation permitted.')
    if not frozen:
        combined.write_bytes(raw)
    docs = output_root / 'documentation'
    docs.mkdir(exist_ok=True)
    fields = ['folder', 'cote', 'scan', 'page_file', 'type', 'token', 'argument', 'line', 'column', 'context']
    with (docs / 'notation_occurrences.tsv').open('w', encoding='utf-8', newline='') as f:
        wr = csv.DictWriter(f, fields, delimiter='\t'); wr.writeheader(); wr.writerows(indices)
    grouped = defaultdict(list)
    for r in indices:
        grouped[(r['type'], r['token'], r['argument'])].append(f"{r['cote']}:{int(r['scan']):03d}:{r['line']}")
    with (docs / 'notation_groups.tsv').open('w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter='\t'); wr.writerow(['type', 'token', 'argument', 'occurrences', 'cote_scan_line'])
        for (kind, token, arg), places in sorted(grouped.items()):
            wr.writerow([kind, token, arg, len(places), '; '.join(places)])
    report['written'] = True
    (docs / 'assembly_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return report


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--witness-root', type=Path, default=DEFAULT_WITNESSES)
    ap.add_argument('--output', type=Path, default=DEFAULT_OUT)
    ap.add_argument('--write', action='store_true')
    ap.add_argument('--require-complete', action='store_true')
    args = ap.parse_args()
    result = assemble(args.witness_root, args.output, args.write, args.require_complete)
    print(json.dumps({k: v for k, v in result.items() if k not in {'pages', 'missing'}}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

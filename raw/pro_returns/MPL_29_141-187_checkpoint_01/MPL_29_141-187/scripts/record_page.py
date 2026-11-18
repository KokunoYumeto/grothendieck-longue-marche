#!/usr/bin/env python3
"""Save a manually read page and its manually enumerated inventory, in order.

No image recognition is performed. Input is JSON on stdin, with scan, tex,
elements ([kind, position, first_words_or_objects]), optional sheet_kind,
and optional doubts ([approximate_line, reading, alternatives, confidence]).
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_29_141-187'
p = json.load(sys.stdin)
n = int(p['scan'])
page = ROOT / 'pages' / f'{PREFIX}_29_scan{n:03d}.tex'
if page.exists():
    raise SystemExit(f'Refusing to overwrite completed page: {page}')
if n > 141 and not (page.parent / f'{PREFIX}_29_scan{n-1:03d}.tex').exists():
    raise SystemExit('Previous page has not been saved')
tex = p['tex'].rstrip() + '\n'
page.write_text(tex, encoding='utf-8')
with (ROOT / f'{PREFIX}_inventory.csv').open('a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    for i, row in enumerate(p['elements'], 1):
        w.writerow(['29', n, p.get('sheet_kind', 'text'), f'{n}.{i:02d}', *row, 'yes'])
with (ROOT / 'doubts_rows.tsv').open('a', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter='\t')
    for row in p.get('doubts', []):
        w.writerow(['29', n, *row])
with (ROOT / 'progress.log').open('a', encoding='utf-8') as f:
    f.write(f'29 scan {n:03d} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print(f'Saved scan {n}; {len(p["elements"])} inventory elements')

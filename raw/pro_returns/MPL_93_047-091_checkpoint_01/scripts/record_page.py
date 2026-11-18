#!/usr/bin/env python3
"""Commit the root reader's page inventory/doubts after its visual rereading."""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PREFIX = 'MPL_93_047-091'
data = json.load(sys.stdin)
scan = int(data['scan'])
page = ROOT / 'pages' / f'{PREFIX}_93_scan{scan:03d}.tex'
assert page.is_file() and f'\\scanpage{{{scan}}}' in page.read_text()
inventory = ROOT / f'{PREFIX}_inventory.csv'
with inventory.open(newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = [row for row in reader if int(row['scan']) != scan]
for i, element in enumerate(data['elements'], 1):
    kind, position, beginning = element
    rows.append(dict(cote='93', scan=str(scan), sheet_kind=data['sheet_kind'],
                     element=f'{scan:03d}.{i:02d}', kind=kind, position=position,
                     first_words_or_objects=beginning, transcribed='yes'))
with inventory.open('w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sorted(rows, key=lambda r:(int(r['scan']),r['element'])))
with (ROOT / f'{PREFIX}_doubts.md').open('a', encoding='utf-8') as f:
    for place, reading, alternatives, confidence in data.get('doubts', []):
        cells = ['93', str(scan), place, reading, alternatives, confidence]
        f.write('| ' + ' | '.join(str(c).replace('|', '\\|') for c in cells) + ' |\n')
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT / 'progress.log').open('a', encoding='utf-8') as f:
    f.write(f'93 scan {scan:03d} done {now}\n')
pages = sorted((ROOT / 'pages').glob(f'{PREFIX}_93_scan*.tex'))
(ROOT / f'{PREFIX}_transcription.tex').write_bytes(b''.join(p.read_bytes() for p in pages))
print(f'Scan {scan:03d} saved; {len(data["elements"])} inventory elements; {now}')

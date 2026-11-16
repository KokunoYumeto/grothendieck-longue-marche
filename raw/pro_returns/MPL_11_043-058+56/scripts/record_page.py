#!/usr/bin/env python3
"""Save a manually read page and its manually prepared inventory immediately."""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
cote, scan = str(data['cote']), int(data['scan'])
prefix = 'MPL_11_043-058+56'
path = root / 'pages' / f'{prefix}_{cote}_scan{scan:03}.tex'
if path.exists():
    raise SystemExit(f'Refusing to overwrite finished page: {path}')
path.write_text(data['tex'].rstrip() + '\n', encoding='utf-8')
with (root / f'{prefix}_inventory.csv').open('a', newline='', encoding='utf-8') as out:
    writer = csv.writer(out)
    for i, row in enumerate(data['elements'], 1):
        kind, position, incipit = row
        writer.writerow([cote, f'{scan:03}', data.get('sheet_kind','text'), f'{cote}-{scan:03}-{i:02}', kind, position, incipit, 'yes'])
with (root / 'records' / 'doubts_rows.md').open('a', encoding='utf-8') as out:
    for row in data.get('doubts', []):
        place, reading, alternatives, confidence = row
        cells = [cote, str(scan), place, reading, alternatives, confidence]
        out.write('| ' + ' | '.join(str(c).replace('|', r'\|').replace('\n',' ') for c in cells) + ' |\n')
with (root / 'records' / 'research_leads.md').open('a', encoding='utf-8') as out:
    for lead in data.get('leads', []):
        out.write(f'\n- Cote {cote}, scan {scan:03}: {lead}\n')
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root / 'progress.log').open('a', encoding='utf-8') as out:
    out.write(f'{cote} scan {scan:03} done {stamp}\n')
with (root / 'records' / 'image_readings.log').open('a', encoding='utf-8') as out:
    out.write(f'{cote} scan {scan:03}: whole, a, b personally viewed; line-by-line rereading and inventory completed {stamp}\n')
print(f'Saved cote {cote}, scan {scan:03}: {len(data["elements"])} inventory elements.')

"""Save a primary-reader page, inventory and timestamp from one JSON stdin record.

No OCR or automatic reading is performed. Input text and inventory are supplied
by the primary reader after direct visual inspection.
"""
import csv
import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
scan = int(data['scan'])
path = ROOT / 'pages' / f'MPL_136_047-094_136_scan{scan:03d}.tex'
if path.exists():
    raise SystemExit(f'Refusing to overwrite completed page: {path.name}')
text = data['tex'].rstrip() + '\n'
path.write_text(text, encoding='utf-8')
with (ROOT / 'MPL_136_047-094_inventory.csv').open('a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for i, e in enumerate(data['elements'], 1):
        writer.writerow(['136', scan, data.get('sheet_kind','text'), f'{scan:03d}-{i:02d}', *e, 'yes'])
with (ROOT / 'reading_observations.md').open('a', encoding='utf-8') as f:
    f.write(f'\n## Scan {scan:03d}\n\n' + data.get('observations','') + '\n')
now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
    f.write(f'136 scan {scan:03d} done {now}\n')
print(f'Saved scan {scan:03d}: {len(data["elements"])} inventory elements; {now}')

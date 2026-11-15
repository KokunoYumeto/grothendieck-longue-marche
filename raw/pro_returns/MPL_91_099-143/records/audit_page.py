from pathlib import Path
from datetime import datetime, timezone
import csv, json, sys

root = Path(__file__).resolve().parents[1]
data = json.load(sys.stdin)
scan = int(data['scan'])
now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'scan {scan:03} audited {now}\n')
with (root/'records/audit.md').open('a') as f:
    f.write(f"\n## Scan {scan:03} — {now}\n\n{data['notes']}\n")
if data.get('extra_elements'):
    path = root/'MPL_91_099-143_inventory.csv'
    with path.open(newline='') as f:
        rows = list(csv.DictReader(f))
    original = [r for r in rows if int(r['scan']) == scan]
    idx = max(int(r['element']) for r in original)
    for kind, pos, first in data['extra_elements']:
        idx += 1
        rows.append(dict(cote='91',scan=f'{scan:03}',sheet_kind=original[0]['sheet_kind'],element=str(idx),kind=kind,position=pos,first_words_or_objects=first,transcribed='yes'))
    rows.sort(key=lambda r:(int(r['scan']),int(r['element'])))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed'])
        w.writeheader();w.writerows(rows)
print(f'Audited {scan:03} at {now}')

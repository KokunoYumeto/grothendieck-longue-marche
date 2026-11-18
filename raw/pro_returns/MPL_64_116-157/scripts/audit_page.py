from pathlib import Path
from datetime import datetime, timezone
import json, sys, csv

ROOT = Path(__file__).resolve().parents[1]
d = json.load(sys.stdin)
n = int(d['scan'])
p = ROOT / 'pages' / f'MPL_64_116-157_64_scan{n:03}.tex'
t = p.read_text()
for old, new in d.get('replacements', []):
    if old not in t:
        raise SystemExit(f'Expected text not found on scan {n}: {old!r}')
    t = t.replace(old, new)
p.write_text(t)
inv = ROOT / 'MPL_64_116-157_inventory.csv'
with inv.open(newline='') as f:
    rows = list(csv.DictReader(f))
present = [r for r in rows if int(r['scan']) == n]
if d.get('elements'):
    with inv.open('a', newline='') as f:
        w = csv.writer(f)
        for i, e in enumerate(d['elements'], len(present) + 1):
            w.writerow([64,n,present[0]['sheet_kind'],f'{n}.{i:02}',*e,'yes'])
with (ROOT/'MPL_64_116-157_doubts.md').open('a') as f:
    for e in d.get('doubts', []):
        f.write('| 64 | '+str(n)+' | '+' | '.join(str(x).replace('|',' / ') for x in e)+' |\n')
stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    if d.get('note'):
        f.write(f'scan {n:03} audit note {stamp}: '+d['note']+'\n')
    f.write(f'scan {n:03} audited {stamp}\n')
print(f'scan {n:03} audited; {len(d.get("replacements", []))} explicit replacements')

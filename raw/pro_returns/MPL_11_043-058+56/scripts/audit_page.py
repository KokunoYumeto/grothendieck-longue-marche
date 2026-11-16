#!/usr/bin/env python3
"""Record root's completed visual audit and explicit ink-based corrections."""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
d = json.load(sys.stdin)
c, n = str(d['cote']), int(d['scan'])
prefix = 'MPL_11_043-058+56'
p = root / 'pages' / f'{prefix}_{c}_scan{n:03}.tex'
t = p.read_text()
for old, new in d.get('replacements', []):
    if old not in t:
        raise SystemExit(f'Missing replacement target: {old!r}')
    t = t.replace(old, new)
p.write_text(t)
with (root/'records'/'doubts_rows.md').open('a') as f:
    for place, reading, alternatives, confidence in d.get('doubts', []):
        cells = [c, n, place, reading, alternatives, confidence]
        f.write('| ' + ' | '.join(str(x).replace('|', r'\|').replace('\n',' ') for x in cells) + ' |\n')
if d.get('elements'):
    inv = root / f'{prefix}_inventory.csv'
    with inv.open(newline='') as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0])
    indexes = [i for i,r in enumerate(rows) if r['cote']==c and int(r['scan'])==n]
    base = rows[indexes[0]]
    newrows=[]
    for j,(kind,pos,incipit) in enumerate(d['elements'],len(indexes)+1):
        newrows.append(dict(zip(fields,[c,f'{n:03}',base['sheet_kind'],f'{c}-{n:03}-{j:02}',kind,pos,incipit,'yes'])))
    rows[indexes[-1]+1:indexes[-1]+1]=newrows
    with inv.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'{c} scan {n:03} audited {stamp}\n')
with (root/'records'/'audit.log').open('a') as f:
    f.write(f'{c} scan {n:03}: {d.get("note","Second visual reading; no change.")} [{stamp}]\n')
print(f'Audited {c} scan {n:03}')

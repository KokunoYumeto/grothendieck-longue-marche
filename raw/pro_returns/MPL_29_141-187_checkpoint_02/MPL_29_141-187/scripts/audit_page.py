#!/usr/bin/env python3
"""Record the primary reader's completed visual audit; never reads images."""
import csv, json, sys
from pathlib import Path
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_29_141-187'
p = json.load(sys.stdin)
n = int(p['scan'])
log = ROOT / 'progress.log'
oldlog = log.read_text()
if 'transcription frozen' in oldlog or 'context opened' in oldlog:
    raise SystemExit('Transcription is frozen or context has opened')
if f'scan {n:03d} audited ' in oldlog:
    raise SystemExit('Audit already recorded')
if n > 141 and f'scan {n-1:03d} audited ' not in oldlog:
    raise SystemExit('Previous page not audited')
if len(list((ROOT/'pages').glob(PREFIX+'_29_scan*.tex'))) != 47:
    raise SystemExit('All 47 first-pass fragments must exist')
path = ROOT/'pages'/f'{PREFIX}_29_scan{n:03d}.tex'
text = path.read_text()
for a,b in p.get('replace', []):
    if a not in text: raise SystemExit('Replacement source not found: '+repr(a))
    text = text.replace(a,b)
path.write_text(text)
inv = ROOT/f'{PREFIX}_inventory.csv'
with inv.open(newline='') as f:
    rows = list(csv.DictReader(f)); fields = list(rows[0])
if p.get('sheet_kind'):
    for r in rows:
        if int(r['scan']) == n: r['sheet_kind'] = p['sheet_kind']
existing = [r for r in rows if int(r['scan']) == n]
for i,el in enumerate(p.get('elements',[]),len(existing)+1):
    rows.append(dict(zip(fields,['29',str(n),p.get('sheet_kind',existing[0]['sheet_kind']),f'{n}.{i:02d}',*el,'yes'])))
rows.sort(key=lambda r:(int(r['scan']),r['element']))
with inv.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
with (ROOT/'doubts_rows.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for row in p.get('doubts',[]): w.writerow(['29',n,*row])
with (ROOT/'audit_changes.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow([n,p.get('note','Compared with image; no change required.')])
with log.open('a') as f:
    f.write(f'scan {n:03d} audited '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print(f'Audited {n}; {len(p.get("replace",[]))} replacements')

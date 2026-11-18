from pathlib import Path
from datetime import datetime, timezone
import json,sys,csv,re
ROOT=Path(__file__).resolve().parents[1]
d=json.load(sys.stdin)
n=int(d['scan'])
f=ROOT/'pages'/f'MPL_64_116-157_64_scan{n:03}.tex'
if f.exists(): raise SystemExit('Refusing to replace completed page; use explicit audited edit')
text=d['text'].rstrip()+'\n'
f.write_text(text)
with (ROOT/'MPL_64_116-157_inventory.csv').open('a',newline='') as g:
    w=csv.writer(g)
    for i,e in enumerate(d['elements'],1):
        w.writerow([64,n,d.get('sheet_kind','text'),f'{n}.{i:02}',*e,'yes'])
with (ROOT/'MPL_64_116-157_doubts.md').open('a') as g:
    for e in d.get('doubts',[]):
        g.write('| 64 | '+str(n)+' | '+' | '.join(str(x).replace('|',' / ') for x in e)+' |\n')
with (ROOT/'progress.log').open('a') as g:
    g.write(f'64 scan {n:03} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print(f.name, len(text), 'characters;',len(d['elements']),'inventory elements')

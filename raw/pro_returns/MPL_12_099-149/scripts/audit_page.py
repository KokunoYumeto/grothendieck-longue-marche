"""Record root's visual audit; edits are explicitly supplied, never inferred."""
import csv, json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.load(sys.stdin); n=int(d['scan'])
p=root/'pages'/f'MPL_12_099-149_12_scan{n:03d}.tex'
s=p.read_text()
for old,new in d.get('replacements',[]):
    if old not in s: raise SystemExit('Replacement target not present: '+repr(old))
    s=s.replace(old,new)
if 'text' in d: s=d['text'].rstrip()+'\n'
p.write_text(s)
q=root/'MPL_12_099-149_doubts.md'; a=q.read_text()
for where,reading,alts,confidence in d.get('doubts',[]):
    vals=['12',f'{n:03d}',where,reading,alts,confidence]
    row='| '+' | '.join(str(v).replace('|','&#124;').replace('\n',' ') for v in vals)+' |'
    a=a.replace('\n## Abbreviations','\n'+row+'\n\n## Abbreviations')
q.write_text(a)
ip=root/'MPL_12_099-149_inventory.csv'
with ip.open(newline='') as f: rows=list(csv.DictReader(f))
for k,pos,opening in d.get('elements',[]):
    old=[r for r in rows if int(r['scan'])==n]
    i=max([int(r['element'].split('.')[1]) for r in old]+[0])+1
    rows.append(dict(cote='12',scan=f'{n:03d}',sheet_kind=old[0]['sheet_kind'],element=f'{n:03d}.{i:02d}',kind=k,position=pos,first_words_or_objects=opening,transcribed='yes'))
if d.get('elements'):
    with ip.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']);w.writeheader();w.writerows(rows)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (root/'progress.log').open('a') as f:
    f.write(f'scan {n:03d} audited {stamp}\n')
    if d.get('comment'): f.write(f'audit {n:03d}: '+d['comment']+'\n')
print(f'scan {n:03d} audited {stamp}; {len(d.get("replacements",[]))} supplied replacement(s)')

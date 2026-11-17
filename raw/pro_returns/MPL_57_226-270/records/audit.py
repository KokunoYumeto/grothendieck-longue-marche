from pathlib import Path
from workflow import BASE, now, log, combine
import difflib, csv

def audit(scan, replacements=(), doubts=(), note=''):
 p=BASE/'pages'/f'MPL_57_226-270_57_scan{scan:03d}.tex'
 old=p.read_text(); new=old
 for a,b in replacements:
  if new.count(a)!=1: raise ValueError((scan,'replacement match count',new.count(a),a))
  new=new.replace(a,b)
 if new!=old:
  p.write_text(new)
  with (BASE/'records/audit_corrections.diff').open('a') as out:
   out.write(f'\n# Scan {scan} visual audit {now()}\n')
   out.writelines(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=p.name+' before',tofile=p.name+' after'))
 with (BASE/'MPL_57_226-270_doubts.md').open('a') as f:
  for place,reading,alternative,confidence in doubts:
   vals=[str(v).replace('|',' / ').replace('\n',' ') for v in ('57',scan,place,reading,alternative,confidence)]
   f.write('| '+' | '.join(vals)+' |\n')
 if note: log(f'audit note scan {scan:03d}: {note}')
 log(f'scan {scan:03d} audited {now()}')
 combine()
 print(f'Audited {scan}; {len(replacements)} corrections; {now()}')

def inventory_add(scan, after_id, kind,position,incipit):
 p=BASE/'MPL_57_226-270_inventory.csv'
 with p.open(newline='') as f:
  rows=list(csv.DictReader(f)); fields=list(rows[0])
 i=next(i for i,r in enumerate(rows) if r['scan']==str(scan) and r['element']==after_id)
 row=rows[i].copy(); row.update(kind=kind,position=position,first_words_or_objects=incipit)
 rows.insert(i+1,row)
 count=0
 for r in rows:
  if r['scan']==str(scan):count+=1;r['element']=f'{scan}.{count:02d}'
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 log(f'inventory audit addition scan {scan}: {kind}, {position}, {incipit} {now()}')

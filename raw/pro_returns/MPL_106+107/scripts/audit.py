from pathlib import Path
from datetime import datetime, timezone
import csv,json,difflib,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import save_page
BASE='MPL_106+107'
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def rebuild():
 inv=ROOT/f'{BASE}_inventory.csv'
 rows=list(csv.DictReader(inv.open()))
 fields=['cote','scan','sheet_kind','element','kind','position','first_words_or_objects','transcribed']
 new=[]; doubts=[]
 for p in sorted((ROOT/'pages').glob('*.tex')):
  cote,scan=map(int,re.search(r'_(\d+)_scan(\d+)',p.name).groups());body=p.read_text()
  old=[r for r in rows if int(r['cote'])==cote and int(r['scan'])==scan]
  sheet=old[0]['sheet_kind']
  group=[r for r in old if not r['position'].startswith('tex line ')]
  for macro,typ in [('deleted','deletion'),('inserted','insertion'),('margin','margin note')]:
   for line,value in save_page.macro_values(body,macro):
    group.append(dict(cote=cote,scan=scan,sheet_kind=sheet,element='',kind=typ,position=f'tex line {line}',first_words_or_objects=value,transcribed='yes'))
  for i,r in enumerate(group,1):r['element']=f'{i:03}'
  new.extend(group)
  for macro in ['unsure','illegible']:
   for line,value in save_page.macro_values(body,macro):
    parts=value.split('|',1)
    low=(macro=='illegible' or len(value)>65 or (cote,scan) in [(106,14),(107,3),(107,8),(107,14),(107,16),(107,23),(107,25)] or '\\deleted' in body.splitlines()[line-1])
    doubts.append(dict(cote=cote,scan=scan,line=line,reading=parts[0],alternative=parts[1] if len(parts)>1 else '',confidence='low' if low else 'medium',macro=macro))
 with inv.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(new)
 (ROOT/'records/doubts.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in doubts))
 (ROOT/f'{BASE}_transcription.tex').write_text('\n'.join(p.read_text() for p in sorted((ROOT/'pages').glob('*.tex'))))
 save_page.update_doubts()
def revise(cote,scan,changes,note):
 p=ROOT/'pages'/f'{BASE}_{cote}_scan{scan:03}.tex';old=p.read_text();new=old
 for a,b in changes:
  if a not in new:raise ValueError(f'Not found: {a!r}')
  new=new.replace(a,b)
 p.write_text(new)
 with (ROOT/'records/audit_changes.diff').open('a') as f:
  f.write(f'\n# {cote} scan {scan:03} {now()} — {note}\n')
  f.writelines(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=p.name+' first pass',tofile=p.name+' audited'))
 rebuild()
def audited(cote,scan,note=''):
 with (ROOT/'progress.log').open('a') as f:f.write(f'{cote} scan {scan:03} audited {now()}\n')
 with (ROOT/'records/visual_audit.md').open('a') as f:f.write(f'\n- {cote}, scan {scan:03}: {note or "Image reread against the complete page fragment; no further change."}\n')
 print(f'{cote} {scan:03} audited {now()}')
if __name__=='__main__':rebuild()
def add_element(cote,scan,kind,position,first_words):
 p=ROOT/f'{BASE}_inventory.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
 sheet=next(r['sheet_kind'] for r in rows if int(r['cote'])==cote and int(r['scan'])==scan)
 rows.append(dict(cote=cote,scan=scan,sheet_kind=sheet,element='999',kind=kind,position=position,first_words_or_objects=first_words,transcribed='yes'))
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
 rebuild()

from pathlib import Path
from datetime import datetime, timezone
import json,sys,csv,re
ROOT=Path(__file__).resolve().parents[1]
def macros(s,name):
 start=0
 while True:
  m=re.search(r'\\'+name+r'\{',s[start:])
  if not m:return
  a=start+m.end(); i=a; d=1
  while i<len(s) and d:
   if s[i]=='{' and (i==0 or s[i-1]!='\\'):d+=1
   elif s[i]=='}' and (i==0 or s[i-1]!='\\'):d-=1
   i+=1
  yield s[a:i-1],s[:a].count('\n')+1
  start=i
x=json.load(sys.stdin); n=int(x['scan']); p=ROOT/'pages'/f'MPL_12_002-050_12_scan{n:03}.tex'
if p.exists() and not x.get('replace'): raise SystemExit(f'Already exists: {p}')
s=x['text'].rstrip()+'\n'; p.write_text(s,encoding='utf-8')
kind=x.get('sheet_kind','text')
from inventory_from_tex import inventory_rows,FIELDS
rows=inventory_rows(s,n,kind)
f=ROOT/'MPL_12_002-050_inventory.csv'
with f.open('a',newline='',encoding='utf-8') as h:csv.DictWriter(h,fieldnames=FIELDS).writerows(rows)
f=ROOT/'MPL_12_002-050_doubts.md';d=f.read_text(encoding='utf-8'); added=[]
for t,line in macros(s,'unsure'):
 parts=t.split('|',1); reading=parts[0];alt=parts[1] if len(parts)>1 else 'Unresolved ink; no secure alternative'
 added.append(f'| 12 | {n:03} | transcription line {line} | `{reading}` | `{alt}` | medium |')
for t,line in macros(s,'illegible'):added.append(f'| 12 | {n:03} | transcription line {line} | unreadable, estimated {t} word(s) | crossed or physically indistinct ink | low |')
if added:d=d.replace('\n# Abbreviations','\n'+'\n'.join(added)+'\n\n# Abbreviations')
for sign,latex,remark in x.get('notation',[]): d=d.replace('\n# Doubt register',f'| {sign} | `{latex}` | {remark} |\n\n# Doubt register')
if x.get('abbreviations'):d=d.replace('\n# Legibility','\n'+x['abbreviations']+'\n\n# Legibility')
f.write_text(d,encoding='utf-8')
if x.get('notes'):
 with (ROOT/'working_notes.md').open('a',encoding='utf-8') as h:h.write(f'\n## Scan {n:03}\n\n'+x['notes']+'\n')
with (ROOT/'progress.log').open('a',encoding='utf-8') as h:h.write(f'12 scan {n:03} done '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
print(f'Saved scan {n:03}: {len(rows)} inventory elements, {len(added)} doubt entries')

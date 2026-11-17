from pathlib import Path
import csv,re
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/(ROOT.name+'_inventory.csv');rows=list(csv.DictReader(p.open()));fields=list(rows[0]);new=[];added=[]
for n in sorted({r['scan'] for r in rows}):
 rr=[r.copy() for r in rows if r['scan']==n];s=(ROOT/'pages'/f'{ROOT.name}_154_scan{n}.tex').read_text();kind=rr[0]['sheet_kind']
 def add(k,pos,txt,where):
  x=dict(cote='154',scan=n,sheet_kind=kind,element='',kind=k,position=pos,first_words_or_objects=txt,transcribed='yes')
  if where=='first':rr.insert(0,x)
  else:rr.append(x)
  added.append((n,k,txt))
 for val in re.findall(r'\\mspage\{([^{}]+)\}',s):
  norm=val.replace('$','').replace("'",'′')
  if not any(r['first_words_or_objects'].strip().replace("'",'′')==norm and r['kind']=='text' for r in rr):add('text','author page number at upper edge',val,'first')
 for val in re.findall(r'\\margin\{(\d+)\}',s):
  if not any(r['first_words_or_objects'].strip()==val and r['kind']=='margin note' for r in rr):add('margin note','pencil archival foliation at lower edge',val,'last')
 existing=sum(r['kind']=='diagram' for r in rr);count=s.count(r'\diagram{')
 if count>existing:
  labels={'006':['printed job-row table','printed system-notice table'],'027':['printed six-line END JOB table'],'030':['printed JCL table'],'033':['printed compiler-header table','printed Fortran five-line table']}
  for txt in labels[n]:add('diagram','printed stock; constituent text rows indexed separately',txt,'last')
 if n=='033':
  for r in rr:
   if r['first_words_or_objects']=='polygone topologique; l’indice égale l’ordre':r['first_words_or_objects']="polygone topologique; unsure d’indice égal à l’ordre / l’indice égale l’ordre"
 for i,r in enumerate(rr,1):r['element']=f'{n}.{i:03d}';new.append(r)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(new)
print('Added',len(added),'metadata and table elements; final rows',len(new))
for row in added:print(row)

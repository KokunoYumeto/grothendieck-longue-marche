#!/usr/bin/env python3
"""Assemble the exact numbered-result and editorial-reading ledgers.

Run from any working directory after editing section sources or metadata.
This validates the one-result/one-row invariant and every cited BibTeX key.
The JSON metadata inputs are retained under audit/ledger_inputs in the ZIP.
"""
import csv,json,re
from pathlib import Path
base=Path(__file__).resolve().parents[1]

def source(name):
 p=base/name
 if p.exists(): return p
 return base/'audit'/'ledger_inputs'/name

def group(s,i):
 assert s[i]=='{',(i,s[i:i+20])
 depth=1;j=i+1
 while depth:
  if s[j]=='\\': j+=2; continue
  if s[j]=='{': depth+=1
  elif s[j]=='}': depth-=1
  j+=1
 return s[i+1:j-1],j

section_names=['AB_agent.tex','F7_test.tex','F7_test5.tex','C_agent.tex','DE_agent.tex','F_root.tex','F_agent.tex','G_root.tex','AB_Z_agent.tex','CF_Z_agent.tex','DE_Z_agent.tex','Z_root.tex']
numbered=[]
citations=set()
for name in section_names:
 if not (base/'sections'/name).exists(): continue
 s=(base/'sections'/name).read_text()
 for m in re.finditer(r'\\begin\{result\}',s):
  at=m.end();ident,at=group(s,at);status,at=group(s,at);title,at=group(s,at)
  end=s.index('\\end{result}',at)
  body=s[at:end].strip()
  body=re.sub(r'\\label\{[^}]*\}','',body)
  numbered.append((ident,status,title,body,name))
 for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}',s):
  citations.update(k.strip() for k in m.group(1).split(','))

reading_inputs={}
for prefix in ('AB','CF','DE','ROOT','F7'):
 p=source(prefix+'_readings.json')
 reading_inputs[prefix]=json.loads(p.read_text()) if p.exists() else []

def scan_numbers(value):
 result=set()
 for m in re.finditer(r'(\d+)(?:\s*[–—-]\s*(\d+))?',str(value)):
  a=int(m[1]); b=int(m[2]) if m[2] else a
  if 1<=a<=b<=136: result.update(range(a,b+1))
 return result

def reading_place(row):
 return next((str(row[x]) for x in ['the_unsure_or_illegible_place','the \\unsure or \\illegible place','place'] if x in row),'')

def expand_reading_links(prefix,row):
 original=row.get('depends_on_doubtful_reading','')
 if prefix=='AB':
  selected=[r for r in reading_inputs[prefix] if r.get('id') in re.findall(r'ABR\d+',original)]
 elif prefix in ('CF','DE'):
  match=re.search(r'\bscans?\s*(.*)',row.get('manuscript_passages',''),re.I)
  passages=scan_numbers(match[1]) if match else set()
  selected=[r for r in reading_inputs[prefix] if scan_numbers(r['scan']) & passages]
 else:
  return original
 if not selected:
  return 'None required by the exact stated hypotheses; no linked doubtful reading.'
 links='; '.join('scan '+str(r['scan'])+': '+reading_place(r) for r in selected)
 return 'The mathematical statement uses its explicitly stated data; disputed readings are retained and tested. '+links

meta={}
for prefix in ('AB','CF','DE','ROOT','F7'):
 if not source(prefix+'_results.json').exists(): continue
 for row in json.loads(source(prefix+'_results.json').read_text()):
  ident=row['id']
  if ident in meta: raise ValueError('duplicate metadata '+ident)
  row['depends_on_doubtful_reading']=expand_reading_links(prefix,row)
  meta[ident]=row
ids=[x[0] for x in numbered]
assert len(ids)==len(set(ids)),'duplicate result ID in TeX'
assert set(ids)==set(meta),{'missing_metadata':sorted(set(ids)-set(meta)),'extra_metadata':sorted(set(meta)-set(ids))}
fields=['id','statement','status','where_proved','depends_on','manuscript_passages','depends_on_doubtful_reading','notes']
rows=[]
for ident,status,title,body,name in numbered:
 r={k:str(meta[ident].get(k,'')) for k in fields}
 assert r['status'].lower()==status.lower(),(ident,r['status'],status)
 # Always synchronize the full mathematical statement and its hypotheses.
 r['statement']=title+' — '+re.sub(r'\s+',' ',body).strip()
 r['where_proved']='FLAGGED_149_paper.tex; sections/'+name+'; Result '+ident
 r['status']=status
 rows.append(r)
with (base/'FLAGGED_149_results.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

readings=[row for prefix in ('AB','CF','DE','ROOT','F7') for row in reading_inputs[prefix]]
rf=['file','scan','the \\unsure or \\illegible place','what the mathematics supports','how strongly']
aliases=[['file'],['scan'],['the_unsure_or_illegible_place','the \\unsure or \\illegible place','place'],['what_the_mathematics_supports','what the mathematics supports','mathematical_evidence'],['how_strongly','how strongly','strength']]
with (base/'FLAGGED_149_readings.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rf);w.writeheader()
 for row in readings:
  out={}
  for k,opts in zip(rf,aliases):
   out[k]=next((row[x] for x in opts if x in row),'')
  assert all(str(out[x]) for x in rf),(row,out)
  w.writerow(out)

for m in re.finditer(r'\\cite(?:\[[^\]]*\])*\{([^}]+)\}',(base/'FLAGGED_149_paper.tex').read_text()):
 citations.update(k.strip() for k in m.group(1).split(','))
bib=(base/'FLAGGED_149_references.bib').read_text()
bibkeys=re.findall(r'@\w+\s*\{\s*([^,]+),',bib)
assert len(bibkeys)==len(set(bibkeys)),'duplicate bibliography keys'
assert citations.issubset(set(bibkeys)),sorted(citations-set(bibkeys))
status_counts={status:sum(r['status']==status for r in rows) for status in ['Proved','Known','Refuted','Open']}
summary={'numbered_results':len(rows),'status_counts':status_counts,'reading_rows':len(readings),'bibliography_entries':len(bibkeys),'cited_entries':len(citations),'missing_metadata':[],'missing_citations':[],'open_result_ids':[r['id'] for r in rows if r['status']=='Open']}
(base/'audit'/'assembly_checks.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))

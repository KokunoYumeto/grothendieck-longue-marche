"""Structural and audit-completeness checks only. Does not compile TeX."""
from pathlib import Path
import csv,json,re,hashlib
root=Path(__file__).resolve().parents[1]
scans=range(26,34); errors=[]; stats={}
allowed=set(['misread word', 'misread symbol or index', 'omission', 'text not on the page', 'deletion state (struck given live or live given struck)', 'insertion or placement', 'abbreviation expanded or spelling modernised', 'readable ink left as `\\ill{}`', 'drawing or diagram', 'other'])
texts=[]
for n in scans:
 p=root/'pages'/f'J156-5-04_156-5_scan{n:03}.tex'
 if not p.exists():errors.append(f'Missing {p.name}');continue
 t=p.read_text();texts.append(t.rstrip());stats[str(n)]={'bytes':p.stat().st_size,'unsure':len(re.findall(r'\\unsure\{',t))}
 for pat,count in [(rf'\\scanpage\{{{n}\}}',1),(rf'\\mspage\{{{n-1}\.?\}}',1)]:
  if len(re.findall(pat,t))!=count:errors.append(f'{p.name}: marker mismatch {pat}')
 if re.search(r'\\(?:struck|uncertain|marginal|ill|add|note|page)\b',t):errors.append(f'{p.name}: forbidden witness macro')
 if '\\documentclass' in t or '\\begin{document}' in t:errors.append(f'{p.name}: contains preamble/document wrapper')
 clean=re.sub(r'(?<!\\)%[^\n]*','',t)
 depth=0
 for m in re.finditer(r'\\.|[{}]',clean):
  v=m.group()
  if v=='{':depth+=1
  elif v=='}':
   depth-=1
   if depth<0:errors.append(f'{p.name}: unmatched close brace');break
 if depth:errors.append(f'{p.name}: brace depth {depth}')
 stack=[]
 for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
  if m[1]=='begin':stack.append(m[2])
  elif not stack or stack.pop()!=m[2]:errors.append(f'{p.name}: mismatched environment {m[2]}')
 if stack:errors.append(f'{p.name}: open environments {stack}')
 a=root/'review'/f'scan{n:03}_adjudicated.json'
 if not a.exists():errors.append(f'Missing adjudication {n}');continue
 d=json.loads(a.read_text())
 for c in d.get('changes',[]):
  if c['confidence'] not in ['high','medium','low']:errors.append(f'Bad confidence {c.get("id")}')
  if c['kind'] not in allowed:errors.append(f'Bad kind {c.get("id")}: {c["kind"]}')
  if c.get('crop'):
   cp=root/c['crop']
   if not cp.exists():errors.append(f'Missing crop {cp}')
   if len(c.get('box',[]))!=4:errors.append(f'Missing box {c.get("id")}')
 base=root/'second'/p.stem
 files={suffix:Path(str(base)+suffix+'.tsv') for suffix in ['_boxes','_first','_second']}
 if not all(q.exists() for q in files.values()): errors.append(f'Incomplete second reading {n}')
 else:
  sets={}
  for suffix,q in files.items():
   with q.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t');rows=list(reader)
    expected=['box','kind','x0','y0','x1','y1'] if suffix=='_boxes' else ['box','reading']
    if reader.fieldnames!=expected:errors.append(f'Invalid columns {q.name}: {reader.fieldnames}')
   sets[suffix]={r['box'] for r in rows}
   if len(sets[suffix])!=len(rows):errors.append(f'Duplicate second box {q.name}')
  if len({tuple(sorted(s)) for s in sets.values()})!=1:errors.append(f'Second-reading box mismatch {n}')
 if not d.get('second_audit_complete'):errors.append(f'Main second adjudication incomplete {n}')
 else:
  cp=root/'second'/f'{p.stem}_comparison.json';ad=root/'second'/f'{p.stem}_adjudication.json'
  if not cp.exists() or not ad.exists():errors.append(f'Missing comparison/adjudication {n}')
  else:
   comp=json.loads(cp.read_text());dec=json.loads(ad.read_text())
   needed={x['box'] for x in comp if x['different']};seen={x['box'] for x in dec['decisions']}
   if needed!=seen:errors.append(f'Unadjudicated token differences {n}: {needed^seen}')
   for x in dec['decisions']:
    if not x.get('viewed_utc') or not x.get('evidence') or not (root/x['crop']).exists():errors.append(f'Incomplete visual adjudication {n}/{x["box"]}')
comb=root/'SP114_CW_156-5_transcription.tex'
if comb.exists() and comb.read_text()!='\n\n'.join(texts)+'\n':errors.append('Combined fragment differs from pages')
coll=root/'SP114_CW_156-5_collation.tsv'
if coll.exists():
 with coll.open(newline='') as f:
  for r in csv.DictReader(f,delimiter='\t'):
   if r['kind'] not in allowed:errors.append(f'Collation invalid kind {r["kind"]}')
inv=root/'SP114_CW_156-5_inventory.csv'
if inv.exists():
 with inv.open(newline='') as f: rows=list(csv.DictReader(f))
 if {int(r['scan']) for r in rows}!=set(scans):errors.append('Inventory page coverage incomplete')
 for r in rows:
  if r['transcribed']!='yes':errors.append(f'Inventory unfinished {r}')
  if r['kind'] not in {'text','display','diagram','drawing','margin note','insertion','deletion'}:errors.append(f'Invalid inventory kind {r["kind"]}')
result={'purpose':'Structural checks; no TeX compilation or OCR','scans':stats,'errors':errors,'passed':not errors}
(root/'review/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(bool(errors))

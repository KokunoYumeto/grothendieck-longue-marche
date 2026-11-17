"""Mechanical splitting of audited inventory groups, using the frozen-ready page macros.
No recognition of scan images is performed here. Human-reviewed grouping overrides below.
"""
from pathlib import Path
import csv,re
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/(ROOT.name+'_inventory.csv')
ORIG=ROOT/'records/inventory_before_reconciliation.csv'
if ORIG.exists():raise RuntimeError('Reconciliation already run; use the preserved original deliberately.')
ORIG.write_bytes(P.read_bytes())
rows=list(csv.DictReader(P.open()))
fields=list(rows[0])

def arguments(s,macro):
 out=[]
 for m in re.finditer(r'\\'+macro+r'\{',s):
  start=m.end();i=start;depth=1
  while depth:
   if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
   elif s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
   i+=1
  out.append((m.start(),re.sub(r'\s+',' ',s[start:i-1]).strip()))
 return out

# Each count refers to separate visible page-state elements, not semicolon clauses.
counts={'014.04':3,'017.28':2,'020.18':5,'024.19':2,'024.22':2,'024.20':2,'029.17':1,'032.24':2}
# Independent drawings originally entered as a cluster are individually indexed.
drawings={
 '013.02':['first orange concurrency pattern along yellow line','second orange concurrency pattern along yellow line','third orange concurrency pattern along yellow line','fourth orange concurrency pattern along yellow line','fifth orange concurrency pattern along yellow line'],
 '017.08':['first all-outgoing vertex star','second all-outgoing vertex star; adjacent equivalence sign'],
 '033.22':['small striped patch labelled s,t','circular boundary drawing'],
 '038.26':['first crossing-brin local configuration','second crossing-brin local configuration and connecting arrows'],
 '039.10':['first disk with u,v,s,t,D labels','second disk with D,D prime labels','result disk after the addition/result signs'],
 '039.13':['left disk of three-disk chain','middle disk of three-disk chain','right disk of three-disk chain','first separate disk with dashed boundary arcs','second separate disk with boundary arcs and curved arrow'],
 '039.18':['upper left disk with D1 labels and alpha,beta','upper right disk with D0,D prime0 labels and alpha,beta','lower left disk with D0,D prime0 labels','lower right disk with D1,D prime1 labels; central black quadrilateral']}
new=[]
for n in sorted({r['scan'] for r in rows}):
 s=(ROOT/'pages'/f'{ROOT.name}_154_scan{n}.tex').read_text()
 source={k:arguments(s,m) for k,m in [('deletion','deleted'),('insertion','inserted')]}
 indexes=defaultdict(int)
 page=[]
 for r in [r for r in rows if r['scan']==n]:
  r=r.copy();key=r['element'];kind=r['kind']
  if kind in source:
   c=counts.get(key,r['first_words_or_objects'].count(';')+1)
   for j in range(c):
    off,arg=source[kind][indexes[kind]];indexes[kind]+=1
    rr=r.copy();rr['first_words_or_objects']=arg[:260]
    if c>1:rr['position']+=f'; separate {kind} {j+1} of {c}'
    if n=='014' and 'mais?' in arg:rr['position']='diagonal correction beside the counterexample'
    if n=='014' and 'fausse!' in arg:rr['position']='diagonal correction beside the counterexample'
    if n=='032' and 'par le côté' in arg:rr['position']='margin beside repere description'
    page.append(rr)
  elif key in drawings:
   for j,incipit in enumerate(drawings[key],1):
    rr=r.copy();rr['first_words_or_objects']=incipit;rr['position']+=f'; constituent {j}';page.append(rr)
  else:
   # Pencil foliation was initially inventoried as text; the audited TeX uses margin.
   if r['first_words_or_objects'].strip().isdigit():
    value=r['first_words_or_objects'].strip()
    if ('pencil' in r['position'] or ('\\margin{'+value+'}') in s and ('\\mspage{'+value+'}') not in s):r['kind']='margin note'
   page.append(r)
 for kind,args in source.items():assert indexes[kind]==len(args),(n,kind,indexes[kind],len(args))
 for j,r in enumerate(page,1):r['element']=f'{n}.{j:03d}';new.append(r)
with P.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(new)
print(f'{len(rows)} original rows; {len(new)} reconciled rows. All insertion/deletion counts match actual page macros.')

"""Necessary cohomological indeterminacy span for the stored A64 action.
This computes coefficient vectors only, not a full UT4 quotient action.
"""
from pathlib import Path
import json,itertools
HERE=Path(__file__).resolve().parent
w=json.loads((HERE.parents[1]/'work_A/A63_zero_t_cross_cup_square.json').read_text())
def mul(a,b):
 out=0
 while b:
  if b&1:out^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return out
def power(a,n):
 out=1
 while n:
  if n&1:out=mul(out,a)
  a=mul(a,a);n>>=1
 return out
def rank(cols):
 piv={}
 for col in cols:
  v=list(col)
  for i in range(len(v)):
   if not v[i]:continue
   if i in piv:
    c=v[i];v=[a^mul(c,b)for a,b in zip(v,piv[i])]
   else:
    inv=power(v[i],6);piv[i]=[mul(inv,a)for a in v];break
 return len(piv)
pairs=list(itertools.combinations(range(4),2));triples=list(itertools.combinations(range(4),3))
P=w['positive_corrections'];C=w['canonical_c_corrections']
assert all(not any(row[4:8])for row in P+C)
def defect(rows,t):
 i,j,k=t;out=[0]*16
 for r,a in enumerate(rows[pairs.index((i,j))][:4]):out[4*r+k]^=a
 for r,a in enumerate(rows[pairs.index((j,k))][:4]):out[4*r+i]^=a
 return out
pc=[defect(P,t)for t in triples];cc=[defect(C,t)for t in triples]
assert rank(pc+cc)==7
print('Stored eta H1 parts involve only the four cusp classes: PASS')
print('Four UT4 triples:',triples)
print('Ordinary classes indexed e_r^[2] cup e_i, 0<=r,i<4.')
print('Positive defect coefficient columns:',pc)
print('Canonical-c defect coefficient columns:',cc)
print('Combined rank overF8:',rank(pc+cc))
print('The four cusp H1 classes are fixed, so this seven-dimensional span is stable.')
print('Scope: cohomological defining-system differences; no UT4 norm or realization claim.')
out=dict(scope='Cohomological upper bound for stable UT4 enlargement; not a quotient-action certificate',
         triples=triples,ordinary_cup_order=[[r,i]for r in range(4)for i in range(4)],
         positive_defects=pc,canonical_c_defects=cc,rank=7,
         all_eta_cohomology_in_cusp_span=True)
(HERE.parent/'UT4_stable_cup_span.json').write_text(json.dumps(out,indent=2)+'\n')

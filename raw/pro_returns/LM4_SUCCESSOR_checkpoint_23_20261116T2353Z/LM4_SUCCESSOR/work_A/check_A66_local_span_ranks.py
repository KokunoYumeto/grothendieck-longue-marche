"""Exact ranks of all radical-compatible local cusp-frame choices.
Reads the saved 29-of-841 compatibility certificate and the complete
local frame lists. No group witness is modified.
"""
from pathlib import Path
import json
from collections import Counter
ROOT=Path(__file__).resolve().parent.parent
A=ROOT/'work_A';CE=ROOT/'work_CE'
d=json.loads((A/'A66_W0_radical_local_gate.json').read_text())
l=json.loads((CE/'A66_W0_joint_local_frame_pairs.json').read_text())
def mul(a,b):
 c=0
 while b:
  if b&1:c^=a
  a<<=1
  if a&8:a^=11
  b>>=1
 return c
def pw(a,n):
 x=1
 while n:
  if n&1:x=mul(x,a)
  a=mul(a,a);n//=2
 return x
def rank(rows):
 rows=[r[:] for r in rows];r=0
 for j in range(4):
  k=next((k for k in range(r,len(rows)) if rows[k][j]),None)
  if k is None:continue
  rows[r],rows[k]=rows[k],rows[r]
  inv=pw(rows[r][j],6);rows[r]=[mul(inv,x) for x in rows[r]]
  for k in range(len(rows)):
   if k!=r and rows[k][j]:
    t=rows[k][j];rows[k]=[x^mul(t,y) for x,y in zip(rows[k],rows[r])]
  r+=1
 return r
out=[]
for s in d['solutions']:
 i,j=s['local_indices']
 # The list is closed under reversal; actual t reverses each right pair.
 v=l['records'][0]['right_corrections'][i][::-1]+l['records'][1]['right_corrections'][j][::-1]
 r=rank(v)
 rec={'local_indices':[i,j],'rank':r,'t_vectors':v,'full360_mask':s['full360_mask']}
 out.append(rec)
print('Exact F8 row ranks of all',len(out),'compatible choices:',dict(Counter(x['rank'] for x in out)))
print('Maximum rank:',max(x['rank'] for x in out))
print('First maximum-rank record:',next(x for x in out if x['rank']==max(z['rank'] for z in out)))
(A/'A66_local_span_ranks.json').write_text(json.dumps({'scope':'All 29 local pairs compatible with the saved old-norm core; not all possible norm cores','distribution':dict(Counter(x['rank'] for x in out)),'records':out},indent=2)+'\n')

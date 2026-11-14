#!/usr/bin/env python3
"""Exhaust every r-fixed detecting line in the actual12-dimensional block."""
from pathlib import Path
from itertools import product
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_correction_graph.json').read_text());S=D['mod3_s_columns'];R=D['mod3_r_columns'];n=97
B=json.loads((OUT/'d_arithmetic_detecting_block.json').read_text());basis=B['selected_quotient_covector_rows'];d=len(basis);assert d==12
bas={}
for j,rr in enumerate(basis):
 v=rr[:];wit=[0]*d;wit[j]=1
 while any(v):
  p=max(i for i,a in enumerate(v) if a)
  if p not in bas:
   inv=pow(v[p],-1,3);bas[p]=([a*inv%3 for a in v],[a*inv%3 for a in wit]);break
  a=v[p];x,y=bas[p];v=[(b-a*c)%3 for b,c in zip(v,x)];wit=[(b-a*c)%3 for b,c in zip(wit,y)]
def coords(v):
 v=v[:];out=[0]*d
 for p in sorted(bas,reverse=True):
  if v[p]:
   a=v[p];x,y=bas[p];v=[(b-a*c)%3 for b,c in zip(v,x)];out=[(b+a*c)%3 for b,c in zip(out,y)]
 assert not any(v)
 return out
def act97(v,M):return [sum(a*b for a,b in zip(v,c))%3 for c in M]
MS=[coords(act97(v,S)) for v in basis];MR=[coords(act97(v,R)) for v in basis]
def combo(v,cols):return [sum(a*c[j] for a,c in zip(v,cols))%3 for j in range(len(cols[0]))]
def null(rows,size):
 bas={}
 for rr in rows:
  v=rr[:]
  while any(v):
   p=max(i for i,a in enumerate(v) if a)
   if p not in bas:
    inv=pow(v[p],-1,3);bas[p]=[a*inv%3 for a in v];break
   a=v[p];v=[(x-a*y)%3 for x,y in zip(v,bas[p])]
 ans=[]
 for f in range(size):
  if f in bas:continue
  v=[0]*size;v[f]=1
  for p in sorted(bas):v[p]=-sum(a*b for i,(a,b) in enumerate(zip(bas[p],v)) if i!=p)%3
  assert all(sum(a*b for a,b in zip(v,row))%3==0 for row in rows);ans.append(v)
 return ans
fixed=null([[(MR[j][i]-int(i==j))%3 for j in range(d)] for i in range(d)],d)
assert len(fixed)==5
rec=next(x for x in D['complete_centralizer_lifting_equations']['r'] if x['q_matrix']==[5,0,0,5])
w=[sum(a*b for a,b in zip(phi,rec['defect']))%3 for phi in basis]
def orbit(v):
 bas={};todo=[]
 def add(v):
  v=v[:]
  while any(v):
   p=max(i for i,a in enumerate(v) if a)
   if p not in bas:
    inv=pow(v[p],-1,3);v=[a*inv%3 for a in v];bas[p]=v;todo.append(v);return
   a=v[p];v=[(x-a*y)%3 for x,y in zip(v,bas[p])]
 add(v);at=0
 while at<len(todo):
  v=todo[at];at+=1;add(combo(v,MS));add(combo(v,MR))
 return todo
records=[];best=None
for coeff in product(range(3),repeat=5):
 v=combo(coeff,fixed)
 if sum(a*b for a,b in zip(v,w))%3!=1:continue
 span=orbit(v);records.append({'fixed_coordinates':list(coeff),'dimension':len(span)})
 if best is None or len(span)<len(best[1]):best=(v,span)
assert len(records)==81
v,span=best
rows=[combo(a,basis) for a in span]
summary={'scope':'Actual Q-submodule, with all81 normalized detecting lines in the full r-fixed5-space exhausted.',
 'ambient_block_dimension':12,'r_fixed_dimension':5,'all_detecting_lines_tested':81,
 'smallest_detecting_submodule_dimension':len(span),
 'dimension_counts':{str(k):sum(r['dimension']==k for r in records) for k in sorted({r['dimension'] for r in records})},
 'quotient_group_order':str(576*3**len(span)),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all81_detecting_line_spans':records,'selected_detecting_fixed_vector':v,
 'actual_quotient_covector_rows':rows,'ambient_block_s_action':MS,'ambient_block_r_action':MR}
(OUT/'d_arithmetic_smallest_detecting.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

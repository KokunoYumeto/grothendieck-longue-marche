#!/usr/bin/env python3
"""Exact Q-module quotients detecting the actual5I r-centralizer obstruction."""
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_correction_graph.json').read_text());S=D['mod3_s_columns'];R=D['mod3_r_columns'];n=97
def row_action(v,M):return [sum(a*b for a,b in zip(v,c))%3 for c in M]
def echelon(rows):
 bas={}
 for vv in rows:
  v=vv[:]
  while any(v):
   p=max(i for i,a in enumerate(v) if a)
   if p not in bas:
    inv=pow(v[p],-1,3);bas[p]=[a*inv%3 for a in v];break
   a=v[p];v=[(x-a*y)%3 for x,y in zip(v,bas[p])]
 return bas
def nullspace(rows):
 bas=echelon(rows);free=[i for i in range(n) if i not in bas];ans=[]
 for f in free:
  v=[0]*n;v[f]=1
  for p in sorted(bas):v[p]=-sum(a*b for i,(a,b) in enumerate(zip(bas[p],v)) if i!=p)%3
  assert all(sum(a*b for a,b in zip(v,row))%3==0 for row in rows);ans.append(v)
 return ans
fixed=nullspace([[(a-int(i==j))%3 for i,a in enumerate(c)] for j,c in enumerate(R)])
assert len(fixed)==34
record=next(x for x in D['complete_centralizer_lifting_equations']['r'] if x['q_matrix']==[5,0,0,5])
defect=record['defect']
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
  v=todo[at];at+=1
  add(row_action(v,S));add(row_action(v,R))
 return todo
records=[];best=None
for j,phi in enumerate(fixed):
 value=sum(a*b for a,b in zip(phi,defect))%3
 if not value:continue
 basis=orbit(phi);records.append({'r_fixed_basis_index':j,'defect_value':value,'Q_span_dimension':len(basis)})
 if best is None or len(basis)<len(best[1]):best=(j,basis)
 assert row_action(phi,R)==phi
assert best is not None
j,basis=best;dim=len(basis)
# Exact coordinates in the chosen row basis.
bas={}
for j0,row in enumerate(basis):
 v=row[:];wit=[0]*dim;wit[j0]=1
 while any(v):
  p=max(i for i,a in enumerate(v) if a)
  if p not in bas:
   inv=pow(v[p],-1,3);bas[p]=([a*inv%3 for a in v],[a*inv%3 for a in wit]);break
  rr,ww=bas[p];a=v[p];v=[(x-a*y)%3 for x,y in zip(v,rr)];wit=[(x-a*y)%3 for x,y in zip(wit,ww)]
def coordinates(v):
 v=v[:];out=[0]*dim
 for p in sorted(bas,reverse=True):
  if v[p]:
   rr,ww=bas[p];a=v[p];v=[(x-a*y)%3 for x,y in zip(v,rr)];out=[(x+a*y)%3 for x,y in zip(out,ww)]
 assert not any(v)
 return out
smallS=[coordinates(row_action(v,S)) for v in basis]
smallR=[coordinates(row_action(v,R)) for v in basis]
projected_defect=[sum(a*b for a,b in zip(phi,defect))%3 for phi in basis]
# These are matrices on the covector rows; transpose to the actual quotient action.
qS=[[smallS[i][j] for i in range(dim)] for j in range(dim)]
qR=[[smallR[i][j] for i in range(dim)] for j in range(dim)]
summary={'scope':'Actual Q-invariant quotient of N_ab/3 detecting5I.',
 'r_fixed_dual_dimension':34,'tested_detecting_dual_basis_vectors':len(records),
 'smallest_detecting_Q_span_dimension_among_basis_vectors':dim,
 'selected_r_fixed_basis_index':j,
 'detected_5I_defect_nonzero':any(projected_defect),
 'quotient_group_order':str(576*3**dim),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all_detecting_basis_trials':records,
 'quotient_covector_rows':basis,'quotient_s_columns':qS,'quotient_r_columns':qR,
 'projected_5I_commutator_defect':projected_defect}
(OUT/'d_arithmetic_detecting_module.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

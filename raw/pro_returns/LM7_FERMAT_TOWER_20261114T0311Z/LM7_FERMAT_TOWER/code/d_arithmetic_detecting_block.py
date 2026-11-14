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

Q=[tuple(a) for a in D['Q_states']];ix={a:i for i,a in enumerate(Q)}
def qmul(a,b):
 x,y,z0,w=a;p0,q,r0,s0=b
 c=((x*p0+y*r0)%12,(x*q+y*s0)%12,(z0*p0+w*r0)%12,(z0*q+w*s0)%12)
 return min(c,tuple(-x%12 for x in c))
def qm(i,j):return ix[qmul(Q[i],Q[j])]
sidx=ix[(0,1,11,0)];ridx=ix[(0,1,11,1)] if (0,1,11,1) in ix else ix[min((0,11,1,11),(0,1,11,1))]
assert all(qm(i,sidx)==D['right_s'][i] and qm(i,ridx)==D['right_r'][i] for i in range(576))
qi=[ix[min((a[3],-a[1]%12,-a[2]%12,a[0]),tuple(-x%12 for x in (a[3],-a[1]%12,-a[2]%12,a[0])))] for a in Q]
words={0:[]};todo=[0]
for i in todo:
 for token,g in [(0,sidx),(1,ridx)]:
  j=qm(i,g)
  if j not in words:words[j]=words[i]+[token];todo.append(j)
assert len(words)==576
def ar(v,g):
 for token in words[g]:v=row_action(v,S if token==0 else R)
 return v
center=ix[(5,0,0,5)]
K4=[i for i,a in enumerate(Q) if tuple(x%2 for x in a)==(1,0,0,1) and (tuple(x%3 for x in a) in [(1,0,0,1),(2,0,0,2)])]
assert len(K4)==8 and center in K4 and all(qm(i,i)==0 for i in K4)
normal_v4=[]
for a in K4:
 for b in K4:
  H={0,a,b,qm(a,b)}
  if len(H)!=4 or center in H:continue
  if all({qm(qm(g,h),qi[g]) for h in H}==H for g in [sidx,ridx]):
   if H not in normal_v4:normal_v4.append(H)
assert len(normal_v4)==1
H=sorted(normal_v4[0])
def negative(v):return [(a-b)*2%3 for a,b in zip(v,ar(v,center))]
def avg(v):
 ans=[0]*n
 for g in H:ans=[(a+b)%3 for a,b in zip(ans,ar(v,g))]
 return ans
records=[];best=None;negative_fixed=[];parts=[[],[]]
for j,phi in enumerate(fixed):
 neg=negative(phi);negative_fixed.append(neg);inv=avg(neg);mov=[(a-b)%3 for a,b in zip(neg,inv)]
 for typ,v in [('V4_fixed',inv),('V4_moving',mov)]:
  parts[0 if typ=='V4_fixed' else 1].append(v)
  assert row_action(v,R)==v
  value=sum(a*b for a,b in zip(v,defect))%3
  if not value:continue
  basis=orbit(v);records.append({'r_fixed_basis_index':j,'type':typ,'defect_value':value,'Q_span_dimension':len(basis)})
  if best is None or len(basis)<len(best[2]):best=(j,typ,basis)
assert best is not None
j,typ,basis=best
summary={'scope':'Actual central-idempotent blocks of the Q-module N_ab/3.',
 'normal_V4_states':H,'negative_r_fixed_dimension':len(echelon(negative_fixed)),
 'negative_V4_fixed_r_fixed_dimension':len(echelon(parts[0])),
 'negative_V4_moving_r_fixed_dimension':len(echelon(parts[1])),
 'smallest_detecting_Q_span_dimension_among_block_basis_vectors':len(basis),
 'selected_r_fixed_basis_index':j,'selected_block':typ,
 'quotient_group_order':str(576*3**len(basis)),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'all_detecting_block_trials':records,'selected_quotient_covector_rows':basis,
 'normal_V4_matrices':[list(Q[h]) for h in H]}
(OUT/'d_arithmetic_detecting_block.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

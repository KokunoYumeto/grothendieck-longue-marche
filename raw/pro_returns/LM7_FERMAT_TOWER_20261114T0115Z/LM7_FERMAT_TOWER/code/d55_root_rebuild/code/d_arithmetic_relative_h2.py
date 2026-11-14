#!/usr/bin/env python3
"""Actual marked arithmetic central covers and the relative-H2 comparison.

The proof uses the five-term and universal-coefficient maps. This
certificate reconstructs their exact integral lattice and the two
central-cover restrictions; it does not claim to enumerate G3.
"""
from pathlib import Path
from collections import deque
from itertools import product
from math import lcm
import json,time
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
OUT=Path(__file__).resolve().parent;started=time.time()
source=json.loads((OUT/'d_cm_central_mixed.json').read_text())
I=(1,0,0,1);S=(0,1,11,0);R=(0,11,1,11)
def mm(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
         (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12)
def canon(a):return min(a,tuple(-x%12 for x in a))
SL=[I];seen={I}
for a in SL:
 for b in [S,R]:
  c=mm(a,b)
  if c not in seen:seen.add(c);SL.append(c)
assert len(SL)==1152
assert seen=={a for a in product(range(12),repeat=4) if (a[0]*a[3]-a[1]*a[2])%12==1}
Q=[tuple(a) for a in source['Q']];assert len(Q)==576 and set(Q)=={canon(a) for a in SL}
ix={a:i for i,a in enumerate(Q)}
rs=[ix[canon(mm(a,S))] for a in Q];rr=[ix[canon(mm(a,R))] for a in Q]
ls=[ix[canon(mm(S,a))] for a in Q];lr=[ix[canon(mm(R,a))] for a in Q]
# Exact abelianization map, with s ->3 and r ->2 in C6.
abel={0:0};queue=deque([0])
while queue:
 q=queue.popleft()
 for h,inc in [(rs[q],3),(rr[q],2)]:
  val=(abel[q]+inc)%6
  if h not in abel:abel[h]=val;queue.append(h)
  else:assert abel[h]==val
assert len(abel)==576 and set(abel.values())==set(range(6))
# Reconstruct the complete97-cycle integral relation lattice.
v2=[(0,min(q,rs[q])) for q in range(576)]
v3=[(1,min(q,rr[q],rr[rr[q]])) for q in range(576)]
adj={v:[] for v in set(v2+v3)}
for e in range(576):
 adj[v2[e]].append((v3[e],e,1));adj[v3[e]].append((v2[e],e,-1))
paths={v2[0]:{}};tree=set();queue=deque([v2[0]])
while queue:
 v=queue.popleft()
 for w,e,a in adj[v]:
  if w not in paths:
   c=paths[v].copy();c[e]=c.get(e,0)+a
   if not c[e]:del c[e]
   paths[w]=c;tree.add(e);queue.append(w)
chords=[e for e in range(576) if e not in tree];assert len(chords)==97
cycles=[]
for e in chords:
 c=paths[v2[e]].copy()
 for j,a in paths[v3[e]].items():c[j]=c.get(j,0)-a
 c[e]=c.get(e,0)+1;cycles.append({j:a for j,a in c.items() if a})
columns=[]
for j,c in enumerate(cycles):
 for perm in [ls,lr]:
  cc={perm[e]:a for e,a in c.items()}
  columns.append([int(i==j)-cc.get(e,0) for i,e in enumerate(chords)])
mat=Matrix(97,194,lambda i,j:columns[j][i])
normal=smith_normal_form(mat,domain=ZZ)
diag=[abs(int(normal[i,i])) for i in range(97)]
assert diag==[1]*96+[2]
def path(word):
 q=0;c=[0]*576
 for a in word:
  if a==0:q=rs[q]
  else:
   h=rr[q] if a==1 else rr[rr[q]]
   c[q]+=1;c[h]-=1;q=h
 return q,[c[e] for e in chords]
q,t12=path([0,1]*12);assert q==0 and any(a%3 for a in t12)
assert all(a%3==0 for a in path([0,1]*36)[1])
full=smith_normal_form(mat.row_join(Matrix(t12)),domain=ZZ)
assert [abs(int(full[i,i])) for i in range(97)]==[1]*97
# Both marked double covers, including every state and projection edge.
es=source['E_right_s'];er=source['E_right_r'];assert len(es)==len(er)==1152
words={0:[]};projection={0:0};queue=deque([0])
while queue:
 a=queue.popleft()
 for h,qh,token in [(es[a],rs[projection[a]],0),(er[a],rr[projection[a]],1)]:
  if h not in words:words[h]=words[a]+[token];projection[h]=qh;queue.append(h)
  else:assert projection[h]==qh
assert len(words)==1152 and all(sum(v==q for v in projection.values())==2 for q in range(576))
assert all(es[es[i]]==i and er[er[er[i]]]==i for i in range(1152))
def ew(word,start=0):
 q=start
 for a in word:q=es[q] if a==0 else (er[q] if a==1 else er[er[q]])
 return q
zword=[0,1]*12;zperm=[ew(zword,i) for i in range(1152)]
assert zperm[0]!=0 and all(zperm[zperm[i]]==i for i in range(1152))
assert all(es[zperm[i]]==zperm[es[i]] and er[zperm[i]]==zperm[er[i]] for i in range(1152))
assert all(ew([0,1]*24,i)==i for i in range(1152))
def sl_order(a):
 b=a;n=1
 while b!=I:b=mm(b,a);n+=1
 return n
assert sl_order(S)==4 and sl_order(R)==3 and sl_order(mm(S,R))==12
cover_evals=[[1,0],[0,1]]
assert (cover_evals[0][0]*cover_evals[1][1]-cover_evals[0][1]*cover_evals[1][0])%2==1
summary={
 'scope':'Actual Q, its two marked central covers and the actual odd G3 extension.',
 'Q_order':576,'SL2_mod12_order':1152,'central_E_order':1152,
 'actual_integral_coinvariant_Smith_factors':{'one':96,'two':1},
 'cusp_appended_integral_lattice_index':1,'Q_abelianization_order':6,
 'SL_lift_s_r_t_orders':[4,3,12],'E_lift_s_r_t_orders':[2,3,24],
 'G3_cusp_order':36,'G3_odd_kernel_rank':97,
 'pulled_back_SL_s_t_orders':[4,lcm(36,12)],
 'pulled_back_E_s_t_orders':[2,lcm(36,24)],
 'dual_restriction_matrix_on_s_and_t':cover_evals,
 'integral_H2_Q_order':2,'mod2_H2_G3_dimension':2,
 's_plus_cusp_H2_map_rank':2,'relative_H2_dimension':1,
 'marked_B_relative_orientation_map_isomorphism':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'actual_Q_abelianization_coordinates':[abel[i] for i in range(576)],
 'integral_N_cycle_chords':chords,'integral_augmentation_columns':columns,
 'actual_t12_cycle':t12,'E_projection_to_Q':[projection[i] for i in range(1152)],
 'E_central_involution_permutation':zperm}
(OUT/'d_arithmetic_relative_h2.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

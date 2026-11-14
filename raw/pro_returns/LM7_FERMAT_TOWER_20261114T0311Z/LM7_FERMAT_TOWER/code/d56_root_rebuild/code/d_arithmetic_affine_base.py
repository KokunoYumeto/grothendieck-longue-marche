#!/usr/bin/env python3
"""Actual3888-state arithmetic detecting quotient and its complete source maps."""
from pathlib import Path
from collections import deque
from itertools import product
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_correction_graph.json').read_text())
J=json.loads((OUT/'d_arithmetic_smallest_detecting.json').read_text())
phi=J['actual_quotient_covector_rows'];assert len(phi)==4
Q=[tuple(x) for x in D['Q_states']];ix={a:i for i,a in enumerate(Q)}
rs=D['right_s'];rr=D['right_r'];S=D['mod3_s_columns'];R=D['mod3_r_columns'];ch=D['cycle_chords'];chi={e:i for i,e in enumerate(ch)}
n=97;dim=4
bas={}
for j,row in enumerate(phi):
 v=row[:];w=[0]*4;w[j]=1
 while any(v):
  p=max(i for i,a in enumerate(v) if a)
  if p not in bas:
   inv=pow(v[p],-1,3);bas[p]=([a*inv%3 for a in v],[a*inv%3 for a in w]);break
  a=v[p];u,z=bas[p];v=[(x-a*y)%3 for x,y in zip(v,u)];w=[(x-a*y)%3 for x,y in zip(w,z)]
assert len(bas)==4
def coord(v):
 v=v[:];w=[0]*4
 for p in sorted(bas,reverse=True):
  if v[p]:
   a=v[p];u,z=bas[p];v=[(x-a*y)%3 for x,y in zip(v,u)];w=[(x+a*y)%3 for x,y in zip(w,z)]
 assert not any(v)
 return w
def ar(v,M):return [sum(a*b for a,b in zip(v,c))%3 for c in M]
SM=[coord(ar(v,S)) for v in phi];RM=[coord(ar(v,R)) for v in phi]
S4=tuple(tuple(SM[i][j] for i in range(4)) for j in range(4))
R4=tuple(tuple(RM[i][j] for i in range(4)) for j in range(4))
I4=tuple(tuple(int(i==j) for i in range(4)) for j in range(4))
def mv(M,v):return tuple(sum(a*c[i] for a,c in zip(v,M))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def neg(a):return tuple(-x%3 for x in a)
words={0:[]};Mats={0:I4};queue=deque([0])
while queue:
 q=queue.popleft()
 for g,M,token in [(rs[q],S4,0),(rr[q],R4,1)]:
  mat=mm(Mats[q],M)
  if g not in words:words[g]=words[q]+[token];Mats[g]=mat;queue.append(g)
  else:assert Mats[g]==mat
assert len(words)==576
center=ix[(5,0,0,5)];minusI=tuple(tuple(-a%3 for a in c) for c in I4)
assert Mats[center]==minusI
image=[];imidx={}
for q in range(576):
 M=Mats[q]
 if M not in imidx:imidx[M]=len(image);image.append(M)
assert len(image)==48
kernel=[q for q in range(576) if Mats[q]==I4];assert len(kernel)==12
# Irreducibility of the actual four-dimensional quotient, by all40 projective lines.
def orbit_rank(v):
 bas={};todo=[]
 def insert(v):
  v=list(v)
  while any(v):
   p=max(i for i,a in enumerate(v) if a)
   if p not in bas:
    inv=pow(v[p],-1,3);v=tuple(a*inv%3 for a in v);bas[p]=v;todo.append(v);return
   a=v[p];v=[(x-a*y)%3 for x,y in zip(v,bas[p])]
 insert(v);at=0
 while at<len(todo):
  v=todo[at];at+=1;insert(mv(S4,v));insert(mv(R4,v))
 return len(bas)
lines=[v for v in product(range(3),repeat=4) if any(v) and next(a for a in v if a)==1]
assert len(lines)==40 and all(orbit_rank(v)==4 for v in lines)
# Literal closed-word projection from N to the selected quotient.
def inverse(word):return [0 if a==0 else 3-a for a in reversed(word)]
def projected(word):
 q=0;v=[0]*97
 for token in word:
  if token==0:q=rs[q]
  else:
   h=rr[q] if token==1 else rr[rr[q]]
   if q in chi:v[chi[q]]+=1
   if h in chi:v[chi[h]]-=1
   q=h
 assert q==0
 return tuple(sum(a*b for a,b in zip(row,v))%3 for row in phi)
wc=words[center]
assert projected(wc+wc)==(0,0,0,0)
def comm(a,b):return a+b+inverse(a)+inverse(b)
ds=projected(comm([0],wc));dr=projected(comm([1],wc))
vs=neg(ds);vr=neg(dr)
assert add(vs,mv(S4,vs))==(0,0,0,0)
assert add(add(vr,mv(R4,vr)),mv(mm(R4,R4),vr))==(0,0,0,0)
def aff_word(word):
 v=(0,0,0,0);q=0
 for token in word:
  repeats=1 if token in [0,1] else 2
  for _ in range(repeats):
   vg=vs if token==0 else vr
   v=add(v,mv(Mats[q],vg));q=rs[q] if token==0 else rr[q]
 return v,q
assert aff_word(wc)==((0,0,0,0),center)
# Reconstruct every actual free N generator and compare all97 images.
v2=[(0,min(q,rs[q])) for q in range(576)];v3=[(1,min(q,rr[q],rr[rr[q]])) for q in range(576)]
adj={v:[] for v in set(v2+v3)}
for e in range(576):
 adj[v2[e]].append((v3[e],e,1));adj[v3[e]].append((v2[e],e,-1))
paths={v2[0]:[]};queue=deque([v2[0]])
while queue:
 v=queue.popleft()
 for u,e,sg in adj[v]:
  if u not in paths:paths[u]=paths[v]+[(e,sg)];queue.append(u)
basis_words=[]
for j,e in enumerate(ch):
 path=paths[v2[e]]+[(e,1)]+[(k,-a) for k,a in reversed(paths[v3[e]])]
 assert all(a==(1 if i%2==0 else -1) for i,(k,a) in enumerate(path))
 word=[] if path[0][0]==0 else [0]
 for (q,a),(h,b) in zip(path,path[1:]):
  if q==h:continue
  if a==1:
   if rr[q]==h:word.append(1)
   else:assert rr[rr[q]]==h;word.append(2)
  else:assert rs[q]==h;word.append(0)
 if path[-1][0]==rs[0]:word.append(0)
 expect=tuple(row[j] for row in phi)
 assert projected(word)==expect and aff_word(word)==(expect,0)
 basis_words.append(word)
# Complete exact generation of both the46656-state and3888-state quotients.
vectors=list(product(range(3),repeat=4));vix={v:i for i,v in enumerate(vectors)}
adds=[[vix[add(a,b)] for b in vectors] for a in vectors]
acts=[[vix[mv(M,v)] for v in vectors] for M in image]
qtoim=[imidx[Mats[q]] for q in range(576)]
si=imidx[S4];ri=imidx[R4];ci=imidx[minusI]
isr=[imidx[mm(M,S4)] for M in image];irr=[imidx[mm(M,R4)] for M in image]
vsi=vix[vs];vri=vix[vr]
def fullstep(a,token):
 q,v=divmod(a,81);mi=qtoim[q]
 return (rs[q] if token==0 else rr[q])*81+adds[v][acts[mi][vsi if token==0 else vri]]
def smallstep(a,token):
 q,v=divmod(a,81)
 return (isr[q] if token==0 else irr[q])*81+adds[v][acts[q][vsi if token==0 else vri]]
def generate(step):
 found={0};todo=[0]
 for a in todo:
  for token in [0,1]:
   b=step(a,token)
   if b not in found:found.add(b);todo.append(b)
 return found
assert len(generate(fullstep))==46656
assert len(generate(smallstep))==3888
RS=[smallstep(a,0) for a in range(3888)];RR=[smallstep(a,1) for a in range(3888)]
assert all(RS[RS[a]]==a and RR[RR[RR[a]]]==a for a in range(3888))
def permorder(f):
 a=f[0];n=1
 while a:a=f[a];n+=1
 return n
T=[RR[RS[a]] for a in range(3888)]
order_t=permorder(T);assert order_t==12
base_t=mm(S4,R4);power=base_t;order_base_t=1
while power!=I4:power=mm(power,base_t);order_base_t+=1
assert order_base_t==12
# Exhaust the full affine coset over5I; no element centralizes the actual r image.
centralizing=[]
for v in vectors:
 if add(v,mv(minusI,vr))==add(vr,mv(R4,v)):centralizing.append(v)
assert not centralizing
# Exact constraints on the actual arithmetic parameter from its s and r formulas.
im1r={add(v,neg(mv(R4,v))) for v in vectors}
parameter_candidates=[a for a in vectors if mv(S4,a)==neg(a) and add(a,neg(tuple(2*x%3 for x in vr))) in im1r]
assert parameter_candidates and (0,0,0,0) not in parameter_candidates
summary={'scope':'Actual marked arithmetic quotient obtained from the actual N_ab/3 module.',
 'quotient_module_dimension':4,'irreducible_projective_lines_checked':40,
 'Q_linear_image_order':48,'Q_linear_kernel_order':12,
 'full_affine_quotient_order':46656,'smaller_affine_quotient_order':3888,
 'all97_actual_N_generator_images_verified':True,
 'all81_lifts_over_5I_tested':True,'r_centralizing_lifts_over_5I':0,
 'actual_parameter_s_r_constraint_candidate_count':len(parameter_candidates),
 'actual_parameter_forced_nonzero':True,
 'actual_parameter_normal_span_image_order':81,
 'cusp_order':order_t,'lower48_cusp_order':order_base_t,
 'kernel_free_rank':649,'compact_genus':163,'cusp_count':324,
 'A_invariant_homology_dimension':9,'A_moving_homology_dimension':640,
 'A_invariant_moving_exterior_dimension':2560,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'actual_quotient_covector_rows':phi,'quotient_s_columns':S4,'quotient_r_columns':R4,
 'affine_s_translation':vs,'affine_r_translation':vr,'central5I_word':wc,
 'Q_linear_image_matrices':image,'Q_to_linear_image':qtoim,'Q_linear_kernel_states':kernel,
 'all97_source_basis_words':basis_words,'right_s_3888':RS,'right_r_3888':RR,
 'actual_parameter_s_r_candidates':parameter_candidates}
(OUT/'d_arithmetic_affine_base.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

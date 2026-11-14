#!/usr/bin/env python3
"""Exact rank-nine common-source matrices for the actual order3888 quotient.

This is a structural and arithmetic-seed experiment.  Its geometric
identification and arithmetic action are to be proved in the accompanying
research note before any theorem is asserted.
"""
from pathlib import Path
from itertools import product
from collections import deque
from fractions import Fraction
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
D=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
M=[tuple(map(tuple,x)) for x in D['Q_linear_image_matrices']];mi={x:i for i,x in enumerate(M)}
S=tuple(map(tuple,D['quotient_s_columns']));R=tuple(map(tuple,D['quotient_r_columns']))
def mv(A,v):return tuple(sum(v[j]*A[j][i] for j in range(4))%3 for i in range(4))
def mm(A,B):return tuple(mv(A,c) for c in B)
tab=[[mi[mm(a,b)] for b in M] for a in M]
si=mi[S];ri=mi[R];ti=tab[si][ri]
def gp(a,k):
 out=0
 while k:
  if k&1:out=tab[out][a]
  a=tab[a][a];k//=2
 return out
inv=[next(j for j in range(48) if tab[i][j]==0) for i in range(48)]
q8=sorted({tab[tab[tab[a][b]][inv[a]]][inv[b]] for a in range(48) for b in range(48)})
assert len(q8)==8 and all(tab[a][b] in q8 for a in q8 for b in q8)
z=gp(ti,6);assert z in q8 and z!=0
rs=[tab[g][si] for g in range(48)];rr=[tab[g][ri] for g in range(48)]
v2=[(0,min(g,rs[g])) for g in range(48)]
v3=[(1,min(g,rr[g],rr[rr[g]])) for g in range(48)]
adj={v:[] for v in set(v2+v3)}
for e in range(48):
 adj[v2[e]].append((v3[e],e,1));adj[v3[e]].append((v2[e],e,-1))
paths={v2[0]:[]};queue=deque([v2[0]]);tree=set()
while queue:
 v=queue.popleft()
 for u,e,sg in adj[v]:
  if u not in paths:paths[u]=paths[v]+[(e,sg)];tree.add(e);queue.append(u)
ch=[e for e in range(48) if e not in tree];assert len(ch)==9
IC=[];words=[]
for j,e in enumerate(ch):
 path=paths[v2[e]]+[(e,1)]+[(k,-a) for k,a in reversed(paths[v3[e]])]
 c={}
 for k,a in path:c[k]=c.get(k,0)+a
 c={k:a for k,a in c.items() if a}
 assert [c.get(k,0) for k in ch]==[int(i==j) for i in range(9)]
 word=[] if path[0][0]==0 else [0]
 for (g,a),(h,b) in zip(path,path[1:]):
  if g==h:continue
  if a==1:
   if rr[g]==h:word.append(1)
   else:assert rr[rr[g]]==h;word.append(2)
  else:assert rs[g]==h;word.append(0)
 if path[-1][0]==si:word.append(0)
 IC.append(c);words.append(word)
def action(g):
 cols=[]
 for c in IC:
  image={}
  for k,a in c.items():image[tab[g][k]]=image.get(tab[g][k],0)+a
  cols.append([image.get(k,0) for k in ch])
 return cols
HC={g:action(g) for g in range(48)}
def imul(A,B):return [[sum(B[j][k]*A[k][i] for k in range(9)) for i in range(9)] for j in range(9)]
ident=[[int(i==j) for i in range(9)] for j in range(9)]
N=[[sum(HC[g][j][i] for g in q8) for i in range(9)] for j in range(9)]
assert imul(N,N)==[[8*x for x in col] for col in N]
T2=HC[gp(ti,2)];ZN=HC[z]
TN=imul(T2,N)
numer=[[56*ZN[j][i]-10*N[j][i]-8*TN[j][i] for i in range(9)] for j in range(9)]
assert all(x%8==0 for col in numer for x in col)
T7=[[x//8 for x in col] for col in numer]
Tmod={str(m):[[(x*pow(7,-1,m))%m for x in col] for col in T7] for m in (2,4,8,16)}
for g in (si,ri):
 assert imul(HC[g],T7)==imul(T7,HC[g])
# The exact translation map K_Q -> A_* from the already marked affine source.
def affine(word):
 v=(0,0,0,0);q=0
 for token in word:
  for _ in range(1 if token in (0,1) else 2):
   vg=(0,0,0,0) if token==0 else tuple(D['affine_r_translation'])
   av=mv(M[q],vg);v=tuple((a+b)%3 for a,b in zip(v,av));q=rs[q] if token==0 else rr[q]
 return v,q
phi=[affine(w)[0] for w in words];assert all(affine(w)[1]==0 for w in words)
def rank_mod(cols,p):
 bas={}
 for col in cols:
  v=[x%p for x in col]
  while any(v):
   k=max(i for i,x in enumerate(v) if x)
   if k not in bas:
    iv=pow(v[k],-1,p);bas[k]=[x*iv%p for x in v];break
   a=v[k];v=[(x-a*y)%p for x,y in zip(v,bas[k])]
 return len(bas)
assert rank_mod(phi,3)==4
assert rank_mod([[(ZN[j][i]-int(i==j))%3 for i in range(9)] for j in range(9)],3)==4
assert all(tuple(sum(phi[k][i]*ZN[j][k] for k in range(9))%3 for i in range(4))
           ==tuple(-x%3 for x in phi[j]) for j in range(9))
assert rank_mod(Tmod['2'],2)==9
# Integral ribbon form and its three-dimensional cusp radical.
entries=[[] for g in range(48)]
for j,c in enumerate(IC):
 for g,a in c.items():entries[g].append((j,a))
twice=[[0]*9 for i in range(9)]
for g in sorted({min(g,rr[g],rr[rr[g]]) for g in range(48)}):
 for i,a in entries[g]:
  for j,b in entries[rr[g]]:
   twice[i][j]+=a*b;twice[j][i]-=a*b
assert all(x%2==0 for row in twice for x in row)
Omega=[[x//2 for x in row] for row in twice]
assert rank_mod(Omega,3)==6
TT_O_T=[[sum(T7[i][k]*Omega[k][l]*T7[j][l] for k in range(9) for l in range(9)) for j in range(9)] for i in range(9)]
assert TT_O_T==[[49*x for x in row] for row in Omega]
# Rank-nine integer normal form for the three rational constituents.
assert rank_mod(N,3)==2
summary={
 'scope':'Actual rank-nine common-source graph; the proposed arithmetic formula awaits the geometric proof.',
 'linear_base_order':48,'kernel_rank':9,'Q8_normal_kernel_order':8,
 'Q8_norm_rank':2,'central_involution_minus_rank':4,'cusp_radical_rank':3,
 'all9_marked_words_and_translation_columns_checked':True,
 'translation_map_rank_mod3':4,
 'minus_compact_translation_isomorphism_mod3':True,
 'proposed_seed_integral_over_Z2':True,
 'proposed_seed_commutes_with_actual_s_r':True,
 'proposed_seed_preserves_integral_pairing_over_Q2':True,
 'proposed_seed_rank_mod2':rank_mod(Tmod['2'],2),
 'proposed_seed_difference_rank_mod2':rank_mod([[(col[i]-int(i==j))%2 for i in range(9)] for j,col in enumerate(Tmod['2'])],2),
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'linear_Q8_states':q8,'central_involution_state':z,
 'rank9_cycle_chords':ch,'all9_marked_words':words,
 'all9_translation_columns_mod3':phi,
 'homology_s_columns':HC[si],'homology_r_columns':HC[ri],'homology_t_columns':HC[ti],
 'central_involution_columns':ZN,'Q8_norm_columns':N,'proposed_seed_seven_times_columns':T7,
 'proposed_seed_columns_moduli':Tmod,'intersection_form_integer':Omega}
(OUT/'d_arithmetic_rank9_seed.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)

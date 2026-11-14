#!/usr/bin/env python3
"""CM entanglement and a necessary GT0 lift test in a finite homology cover.

B=C2*C3 -> Q=SL2(Z/12)/global +/-1; N is free of rank97.
The quotient B/[N,N]N^2 is represented by Bass--Serre edge chains over F2.
No exhaustive enumeration of its 2^97-element kernel is needed.
"""
from collections import deque
from pathlib import Path
import json
import random
import sympy as sp
import numpy as np

OUT=Path(__file__).resolve().parent
n=12
I=(1,0,0,1)
def mul(a,b):
 return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
         (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)
def neg(a):return tuple(-x%n for x in a)
def inv(a):return (a[3],-a[1]%n,-a[2]%n,a[0])
def canon(a):return min(a,neg(a))
def qm(a,b):return canon(mul(a,b))
S=(0,1,11,0);R=(0,11,1,11)
qs,qr=canon(S),canon(R);qr2=qm(qr,qr)
one=canon(I)
Q={one};todo=[one]
while todo:
 a=todo.pop()
 for g in (qs,qr):
  b=qm(a,g)
  if b not in Q:Q.add(b);todo.append(b)
Q=sorted(Q);ix={a:i for i,a in enumerate(Q)};z=ix[one]
assert len(Q)==576
left={g:[ix[qm(g,a)] for a in Q] for g in (qs,qr)}
def act(bits,g):
 perm=left.get(g)
 if perm is None:perm=[ix[qm(g,a)] for a in Q]
 ans=0
 while bits:
  b=bits&-bits;ans^=1<<perm[b.bit_length()-1];bits^=b
 return ans

# A spanning tree of N\T gives a genuine integral cycle basis, reduced mod2.
v2={a:('s',min(a,qm(a,qs))) for a in Q}
v3={a:('r',min(a,qm(a,qr),qm(a,qr2))) for a in Q}
vertices=set(v2.values())|set(v3.values());adj={v:[] for v in vertices}
for i,a in enumerate(Q):
 adj[v2[a]].append((v3[a],i));adj[v3[a]].append((v2[a],i))
root=v2[one];paths={root:0};queue=deque([root]);tree=set()
while queue:
 v=queue.popleft()
 for w,e in adj[v]:
  if w not in paths:paths[w]=paths[v]^(1<<e);tree.add(e);queue.append(w)
assert len(paths)==480
cycles=[paths[v2[a]]^paths[v3[a]]^(1<<i) for i,a in enumerate(Q) if i not in tree]
assert len(cycles)==97
def echelon(vectors):
 basis={}
 for row in vectors:
  while row:
   p=row.bit_length()-1
   if p not in basis:basis[p]=row;break
   row^=basis[p]
 return basis
def remainder(row,basis):
 for p in sorted(basis,reverse=True):
  if (row>>p)&1:row^=basis[p]
 return row
assert len(echelon(cycles))==97
W=echelon([c^act(c,g) for c in cycles for g in (qs,qr)])
columns=[c^act(c,qs) for c in cycles]+[act(c^act(c,qr),qs) for c in cycles]
solvers={};nullspace=[]
for j,col in enumerate(columns):
 row=col;witness=1<<j
 while row:
  p=row.bit_length()-1
  if p not in solvers:solvers[p]=(row,witness);break
  v,w=solvers[p];row^=v;witness^=w
 if not row:nullspace.append(witness)
assert len(solvers)==len(W) and len(nullspace)==194-len(W)
def solve(row):
 witness=0
 for p in sorted(solvers,reverse=True):
  if (row>>p)&1:
   v,w=solvers[p];row^=v;witness^=w
 assert row==0
 return witness
def cycle_sum(mask):
 ans=0
 for j,c in enumerate(cycles):
  if (mask>>j)&1:ans^=c
 return ans
all_left=[[ix[qm(q,a)] for a in Q] for q in Q]
def module_rank(edge):
 indices=[];bits=edge
 while bits:
  b=bits&-bits;indices.append(b.bit_length()-1);bits^=b
 translates=[]
 for perm in all_left:
  val=0
  for j in indices:val^=1<<perm[j]
  translates.append(val)
 images=[]
 for c in cycles:
  val=0
  while c:
   b=c&-c;val^=translates[b.bit_length()-1];c^=b
  images.append(val)
 return len(echelon(images))

# The Bass--Serre path cocycle has P(s)=0, P(r)=edge1-edge_r.
Pr=(1<<z)^(1<<ix[qr]);P={one:0};queue=deque([one])
while queue:
 a=queue.popleft()
 for g,Pg in ((qs,0),(qr,Pr)):
  b=qm(a,g)
  if b not in P:P[b]=P[a]^act(Pg,a);queue.append(b)
assert len(P)==len(Q)
qt=qm(qs,qr);Pt=act(Pr,qs);ct=0;gt=one
for j in range(12):ct^=act(Pt,gt);gt=qm(gt,qt)
assert gt==one and ct!=0
H=[a for a in Q if tuple(x%2 for x in a)==I]
assert len(H)==96
CA=[a for a in H if qm(a,qr)==qm(qr,a)]
CB=[b for b in H if qm(b,qs)==qm(qs,b)]
S_centralizer_columns=echelon([c^act(c,qs) for c in cycles])
S_centralizer_images=[b for b in CB if remainder(P[b]^act(P[b],qs),S_centralizer_columns)==0]
V4={(1,0,0,1),(1,2,0,1),(1,0,2,1),(1,2,2,1)}
def flift(a):
 if tuple(x%4 for x in a) in V4:return a
 a=neg(a)
 assert tuple(x%4 for x in a) in V4
 return a
def red(a,k):return tuple(x%k for x in a)
def cm_bit(a,b):
 A=flift(a);B=flift(b)
 assert mul(A,R)==mul(R,A) and mul(B,S)==mul(S,B)
 T=inv(A);W=inv(B)
 assert red(T,4)==I
 # The rational point (0,1) of order3 spans ker(R-I) modulo3.
 tv=((T[0]+2*T[1])%3,(T[2]+2*T[3])%3)
 assert tv in [(1,2),(2,1)]
 sign3=int(tv==(2,1))
 wr=red(W,3)
 if wr in [I,red(neg(I),3)]:sign4=0
 else:
  assert wr in [red(S,3),red(neg(S),3)]
  sign4=1
 return sign3^sign4,sign3,sign4

def check_binary_hexagons(a,b,pa,pb):
 def mm(g,h):return qm(g[0],h[0]),g[1]^act(h[1],g[0])
 def ii(g):
  gi=canon(inv(g[0]));return gi,act(g[1],gi)
 def cc(g,h):return mm(mm(g,h),ii(g))
 s=(qs,0);r=(qr,Pr);A=(a,pa);B=(b,pb)
 ss=cc(B,s);rr=cc(A,r);t=mm(s,r)
 assert mm(ss,rr)==t
 u=ii(t);v=mm(mm(s,u),s);f=mm(s,ss)
 assert mm(mm(mm(u,ii(f)),v),f)==mm(ii(f),mm(u,v))
 assert mm(mm(mm(ii(f),v),f),u)==mm(mm(v,u),f)
 assert mm(f,cc(s,f))==(one,0)

records=[]
rng=random.Random(20261113)
for a in CA:
 for b in CB:
  # Error of beta*s*beta^-1*A*r*A^-1=(sr), modulo N^ab/2.
  dr=P[a]^act(P[a],qr)^act(Pr,a)^Pr
  ds=P[b]^act(P[b],qs)
  error=ds^act(dr,qs)
  assert remainder(error,echelon(cycles))==0
  rem=remainder(error,W)
  bit,j3,j4=cm_bit(a,b)
  row={'A':flift(a),'beta':flift(b),'CM3_bit':j3,'CM4_bit':j4,
                  'missing_coset':bool(bit),'homology_cover_lift':rem==0,
                  'obstruction_bits':hex(rem)}
  if rem==0:
   particular=solve(error);best=0
   for trial in range(64):
    witness=particular
    if trial:
     for v in nullspace:
      if rng.randrange(2):witness^=v
    bv=cycle_sum(witness&((1<<97)-1));av=cycle_sum(witness>>97)
    # The equivariant map on Bass--Serre edges sends edge1 to
    # the path from beta*S to A*R: -P(beta)+P(A)+edge_A.
    edge=P[a]^P[b]^(1<<ix[a])^av^bv
    rank=module_rank(edge);best=max(best,rank)
    if rank==97:
     check_binary_hexagons(a,b,P[a]^av,P[b]^bv)
     row.update({'finite_automorphism':True,'kernel_rank':rank,
                 'A_cycle_coefficients':hex(witness>>97),
                 'beta_cycle_coefficients':hex(witness&((1<<97)-1)),
                 'trials':trial+1})
     break
   else:row.update({'finite_automorphism':False,'best_kernel_rank':best,'trials':64})
  records.append(row)

def mod3_refinement():
 p=3;edge_count=len(Q);rankN=97
 def action(vec,g):
  ans=np.zeros(edge_count,dtype=np.int16)
  ans[np.array(all_left[ix[g]],dtype=int)]=vec
  return ans
 # Integral oriented spanning-tree paths and fundamental cycles.
 ipaths={root:np.zeros(edge_count,dtype=np.int16)};queue=deque([root]);itree=set()
 while queue:
  v=queue.popleft()
  for w,e in adj[v]:
   if w not in ipaths:
    t=ipaths[v].copy();t[e]+=1 if v[0]=='s' else -1
    ipaths[w]=t;itree.add(e);queue.append(w)
 C=[]
 for i,a in enumerate(Q):
  if i not in itree:
   c=ipaths[v2[a]]-ipaths[v3[a]];c[i]+=1
   assert sum(1<<int(j) for j in np.flatnonzero(c%2))==cycles[len(C)]
   C.append(c%p)
 assert len(C)==rankN
 cols=[(c-action(c,qs))%p for c in C]+[action((c-action(c,qr))%p,qs) for c in C]
 basis={};nulls=[]
 for j,col in enumerate(cols):
  row=col.copy();wit=np.zeros(194,dtype=np.int16);wit[j]=1
  while np.any(row):
   pos=int(np.flatnonzero(row)[-1]);factor=int(row[pos])
   if pos not in basis:
    row=(row*factor)%p;wit=(wit*factor)%p;basis[pos]=(row,wit);break
   v,w=basis[pos];row=(row-factor*v)%p;wit=(wit-factor*w)%p
  if not np.any(row):nulls.append(wit)
 def solution(row):
  row=row.copy();wit=np.zeros(194,dtype=np.int16)
  for pos in sorted(basis,reverse=True):
   factor=int(row[pos])
   if factor:
    v,w=basis[pos];row=(row-factor*v)%p;wit=(wit+factor*w)%p
  return not np.any(row),wit,row
 Pr3=np.zeros(edge_count,dtype=np.int16);Pr3[z]=1;Pr3[ix[qr]]=-1;Pr3%=p
 ct=np.zeros(edge_count,dtype=np.int16);gt=one;Pt3=action(Pr3,qs)
 for j in range(12):ct=(ct+action(Pt3,gt))%p;gt=qm(gt,qt)
 assert gt==one and np.any(ct)
 P3={one:np.zeros(edge_count,dtype=np.int16)};queue=deque([one])
 while queue:
  a=queue.popleft()
  for g,Pg in ((qs,np.zeros(edge_count,dtype=np.int16)),(qr,Pr3)):
   b=qm(a,g)
   if b not in P3:P3[b]=(P3[a]+action(Pg,a))%p;queue.append(b)
 def linrank(rows):
  bas={}
  for row in rows:
   row=row.copy()
   while np.any(row):
    pos=int(np.flatnonzero(row)[-1]);fac=int(row[pos])
    if pos not in bas:bas[pos]=(fac*row)%p;break
    row=(row-fac*bas[pos])%p
  return len(bas)
 def in_span(row,cols):
  bas={}
  for vector in cols:
   vector=vector.copy()
   while np.any(vector):
    pos=int(np.flatnonzero(vector)[-1]);fac=int(vector[pos])
    if pos not in bas:bas[pos]=(fac*vector)%p;break
    vector=(vector-fac*bas[pos])%p
  row=row.copy()
  for pos in sorted(bas,reverse=True):row=(row-int(row[pos])*bas[pos])%p
  return not np.any(row)
 R_centralizer_images=[]
 for a in CA:
  dr=(P3[a]-action(P3[a],qr)+action(Pr3,a)-Pr3)%p
  if in_span((-dr)%p,[(c-action(c,qr))%p for c in C]):R_centralizer_images.append(a)
 def mrank(edge):
  translates=np.stack([action(edge,q) for q in Q])
  images=[]
  for c in C:
   ids=np.flatnonzero(c);images.append(np.sum(translates[ids]*c[ids,None],axis=0)%p)
  return linrank(images)
 def check_hexagons(a,b,pa,pb):
  def mm(g,h):return qm(g[0],h[0]),(g[1]+action(h[1],g[0]))%p
  def ii(g):
   gi=canon(inv(g[0]));return gi,(-action(g[1],gi))%p
  def cc(g,h):return mm(mm(g,h),ii(g))
  def equal(g,h):return g[0]==h[0] and np.array_equal(g[1]%p,h[1]%p)
  s=(qs,np.zeros(edge_count,dtype=np.int16));r=(qr,Pr3);A=(a,pa);B=(b,pb)
  ss=cc(B,s);rr=cc(A,r);t=mm(s,r)
  assert equal(mm(ss,rr),t)
  u=ii(t);v=mm(mm(s,u),s);f=mm(s,ss)
  assert equal(mm(mm(mm(u,ii(f)),v),f),mm(ii(f),mm(u,v)))
  assert equal(mm(mm(mm(ii(f),v),f),u),mm(mm(v,u),f))
  assert equal(mm(f,cc(s,f)),(one,np.zeros(edge_count,dtype=np.int16)))
 for row in records:
  a=canon(tuple(row['A']));b=canon(tuple(row['beta']))
  dr=(P3[a]-action(P3[a],qr)+action(Pr3,a)-Pr3)%p
  ds=(P3[b]-action(P3[b],qs))%p
  error=(ds+action(dr,qs))%p
  good,wit,rem=solution((-error)%p)
  row['mod3_cusp_lift']=bool(good)
  if not good:row['mod3_obstruction']={str(i):int(rem[i]) for i in np.flatnonzero(rem)};continue
  for trial in range(64):
   candidate=wit.copy()
   if trial:
    for v in nulls:candidate=(candidate+rng.randrange(3)*v)%p
   bv=sum((candidate[j]*C[j] for j in range(97)),np.zeros(edge_count,dtype=np.int16))%p
   av=sum((candidate[97+j]*C[j] for j in range(97)),np.zeros(edge_count,dtype=np.int16))%p
   edge=(P3[a]+av-P3[b]-bv)%p;edge[ix[a]]=(edge[ix[a]]+1)%p
   rank=mrank(edge)
   if rank==97:
    check_hexagons(a,b,(P3[a]+av)%p,(P3[b]+bv)%p)
    row['mod3_automorphism']=True;row['mod3_kernel_rank']=rank
    row['mod3_A_cycles']={str(i):int(candidate[97+i]) for i in range(97) if candidate[97+i]}
    row['mod3_beta_cycles']={str(i):int(candidate[i]) for i in range(97) if candidate[i]}
    row['mod3_trials']=trial+1;break
  else:row['mod3_automorphism']=False;row['mod3_trials']=64
 return {'mod3_relation_rank':len(basis),'mod3_coinvariant_dimension':97-len(basis),
         'mod3_nullity':len(nulls),'mod3_lifts':sum(r['mod3_cusp_lift'] for r in records),
         'mod3_automorphisms':sum(r.get('mod3_automorphism',False) for r in records),
         'mod3_R_centralizer_images_in_H':[flift(a) for a in R_centralizer_images]}
mod3_summary=mod3_refinement()
for row in records:
 if row.get('finite_automorphism') and row.get('mod3_automorphism'):
  for name,bitkey,mod3key in [('A','A_cycle_coefficients','mod3_A_cycles'),('beta','beta_cycle_coefficients','mod3_beta_cycles')]:
   two=int(row[bitkey],16);three=row[mod3key];crt={}
   for j in range(97):
    a=(two>>j)&1;b=three.get(str(j),0)
    c=next(c for c in range(6) if c%2==a and c%3==b)
    if c:crt[str(j)]=c
   row[f'mod6_{name}_cycles']=crt

# Algebraic identities proving the exact common finite field.
r=sp.symbols('r');mod=r**4-sp.Rational(3,4)
def reduce(f):
 num,den=sp.fraction(sp.cancel(f));return sp.rem(num,mod,r),den
h=2*r**2 # sqrt3
y=h*(h-1)*r
assert reduce(y*y-(-9+6*h))[0]==0
w=1/r;a=(w+2/w)/2
# The other root b=(w-2/w)/(2i), so b^2 is a rational function of r.
b2=-(w-2/w)**2/4
assert reduce(3*a**4-6*a*a-1)[0]==0
assert reduce(3*b2*b2-6*b2-1)[0]==0
assert reduce(a*a-(1+2/h))[0]==0
summary={'Q_order':len(Q),'graph_vertices':len(vertices),'graph_edges':len(Q),
 'G2_order':576*2**97,'G3_order':576*3**97,'G6_order':576*6**97,
 'cusp_order_in_G2':24,'cusp_order_in_G3':36,'cusp_order_in_G6':72,'GT_shadow_Nord':36,
 'N_rank':len(cycles),'coinvariant_relation_rank_mod2':len(W),
 'coinvariant_dimension_mod2':len(cycles)-len(W),
 'A_choices':len(CA),'beta_choices':len(CB),'tested_pairs':len(records),
 'matrix_compatible_pairs':sum(not z['missing_coset'] for z in records),
 'matrix_missing_pairs':sum(z['missing_coset'] for z in records),
 'cover_lift_compatible':sum(z['homology_cover_lift'] and not z['missing_coset'] for z in records),
 'cover_lift_missing':sum(z['homology_cover_lift'] and z['missing_coset'] for z in records),
 'automorphism_compatible':sum(z.get('finite_automorphism',False) and not z['missing_coset'] for z in records),
 'automorphism_missing':sum(z.get('finite_automorphism',False) and z['missing_coset'] for z in records),
 'combined_automorphism_compatible':sum(z.get('finite_automorphism',False) and z.get('mod3_automorphism',False) and not z['missing_coset'] for z in records),
 'combined_automorphism_missing':sum(z.get('finite_automorphism',False) and z.get('mod3_automorphism',False) and z['missing_coset'] for z in records),
 'mod2_S_centralizer_images_in_H':[flift(a) for a in S_centralizer_images],
 'common_field':'Q(i,r), r^4=3/4; full E3[4] = projective E4[3]',
 'global_sign_rule':'T4 normalized by the scalar of T3 on ker(R-I); projective E3[12] recovers full E3[4]',
 'scope':'Exact cusp-relation and both m=0 hexagon tests in B/[N,N]N^2 and B/[N,N]N^3, plus explicit witnesses whose induced N^ab/p matrix has full rank97. CRT coordinates define single finite quotient automorphisms modulo6. A stated integral cusp gauge makes f a commutator word; no automatic profinite lifting asserted.',**mod3_summary}
out={'summary':summary,'pairs':records}
(OUT/'d_cm_shadow.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))
print('missing coset survivor matrix pairs:',[(r['A'],r['beta']) for r in records if r.get('finite_automorphism') and r.get('mod3_automorphism') and r['missing_coset']])
print('All exact cycle coefficients and CRT witnesses are retained in d_cm_shadow.json.')

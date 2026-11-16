#!/usr/bin/env python3
"""Necessary finite tests for psi(D_L), not actual profinite lifts.

Induce the S3 quotient x -> 3-cycle, y -> transposition from F to B.
Its faithful permutation image has order648. Then retain all six
orbifold evaluations, the original S3 value, the common-word constraint,
the six cycle equations, and the descendant r conjugacy constraint.
All three putative discrepancies survive; no full lift is asserted.
"""
from itertools import product
from collections import deque
from sympy.combinatorics import Permutation, PermutationGroup
from pathlib import Path
import json

# Free-product syllables: 1 denotes s, 2 and 3 denote r and r^2.
def mul(a,b):
    c=list(a)
    for x in b:
        if not c or (c[-1]==1)!=(x==1):c.append(x)
        elif x==1:c.pop()
        else:
            v=((c.pop()-1)+(x-1))%3
            if v:c.append(v+1)
    return tuple(c)
def inv(a):return tuple(1 if x==1 else 5-x for x in reversed(a))
def pw(a,n):
    if n<0:return pw(inv(a),-n)
    o=()
    for _ in range(n):o=mul(o,a)
    return o
s=(1,);r=(2,);tau=mul(s,r)
x=pw(tau,-2);y=mul(mul(s,x),s)

P=tuple(Permutation(v) for v in product(range(3),repeat=3)
        if len(set(v))==3)
idp=Permutation([0,1,2]);sp=Permutation([1,0,2]);rp=Permutation([1,2,0])
def ev(a):
    o=idp
    for v in a:o=o*(sp if v==1 else rp**(v-1))
    return o
trans=[(),s,r,pw(r,2),tau,mul(s,pw(r,2))]
tindex={ev(t):i for i,t in enumerate(trans)}
assert len(tindex)==6
needed={}
for i,t in enumerate(trans):
    for name,g in [('s',s),('r',r)]:
        j=tindex[ev(mul(t,g))]
        c=mul(mul(t,g),inv(trans[j]))
        needed[i,name]=(j,c)
xy={( ):()};queue=deque([()])
gens=[(1,x),(-1,inv(x)),(2,y),(-2,inv(y))]
while any(c not in xy for j,c in needed.values()):
    a=queue.popleft()
    for n,g in gens:
        b=mul(a,g)
        if b not in xy:xy[b]=xy[a]+(n,);queue.append(b)
assert len(xy)<10000

# Induce q:F -> S3, x -> 3-cycle, y -> transposition.
qx=rp;qy=sp
def qword(w):
    o=idp
    for a in w:o=o*((qx if abs(a)==1 else qy)**(1 if a>0 else -1))
    return o
pindex={p:i for i,p in enumerate(P)}
perms={}
for name in ('s','r'):
    arr=[]
    for i in range(6):
        j,c=needed[i,name];qc=qword(xy[c])
        for h in P:arr.append(6*j+pindex[h*qc])
    perms[name]=Permutation(arr)
S=perms['s'];R=perms['r'];T=S*R
X=T**-2;Y=S*X*S
G=PermutationGroup([S,R]);F=PermutationGroup([X,Y]);der=G.derived_subgroup()
print('orders',G.order(),F.order(),der.order(),flush=True)
assert (G.order(),F.order(),der.order())==(648,108,324)
def q(a):
    assert a(0)//6==0
    # image q(a) from regular action in the identity-coset block.
    return P[a(pindex[idp])%6]
assert q(X)==qx and q(Y)==qy
elements=list(G.generate_schreier_sims())
felements=set(F.generate_schreier_sims())
cs=[c for c in der.generate_schreier_sims() if c in felements]
print('C possible abstract',len(cs),flush=True)
def aD(C,a):
    ff=Y**a*S*C*S*C**-1*X**-a
    out=q(ff)
    return next((j for j in range(3)if qx**j==out),None)
records=[]
for C in cs:
    for af in range(3):
        aa=next(a for a in range(6) if a%3==(-af)%3 and aD(C,a) is not None)
        records.append((C,af,aa,aD(C,aa)))
from collections import Counter
print('raw discrepancy',Counter((ad+af)%3 for C,af,a,ad in records),flush=True)

# Actual common-word source, with original a_f retained.
def join(g,h):return Permutation(list(g.array_form)+[36+h(i) for i in range(3)])
K=PermutationGroup([join(S,qx),join(T,qy)]);KD=K.derived_subgroup()
print('joint',K.order(),KD.order(),flush=True)
sur=[]
for C,af,a,ad in records:
    if KD.contains(join(C,qx**af)):sur.append((C,af,a,ad))
print('common discrepancy',Counter((ad+af)%3 for C,af,a,ad in sur),flush=True)
gent=[]
for C,af,a,ad in sur:
    RR=S*C**-1*T*C
    # The r-image must be a conjugate of the same r, with conjugator
    # H in B' whose S3 residue is r^l, l=-a_f modulo three.
    if any(H*R*H**-1==RR and H*(R**af) in felements
           for H in der.generate_schreier_sims()):
        gent.append((C,af,a,ad))
print('descent boundary discrepancy',Counter((ad+af)%3 for C,af,a,ad in gent),flush=True)
print('descent boundary triples',sorted(set((af,a,ad)for C,af,a,ad in gent)),flush=True)

pairs=[(S,T),(T,R**-1),(R**-1,S),(T,S),(R**-1,T),(S,R**-1)]
def direct(coords,extra=None):
    ar=[]
    for j,g in enumerate(coords):ar += [36*j+g(i)for i in range(36)]
    if extra is not None:ar += [216+extra(i)for i in range(3)]
    return Permutation(ar)
K6=PermutationGroup([direct([a for a,b in pairs],qx),direct([b for a,b in pairs],qy)])
print('six plus original group computing',flush=True)
print('six plus original order',K6.order(),flush=True)
K6d=K6.derived_subgroup()
print('six plus original derived order',K6d.order(),flush=True)
look={}
for j,(A,B)in enumerate(pairs):
    for M in elements:look.setdefault((M*A*M**-1,M*B*M**-1),(j,M))
cycles=[]
for A,B in pairs:
    Z=(A*B)**-1
    cycles.append((look[(Z,A)],look[(B,Z)]))
allgent=[];allmem=[]
ders=list(der.generate_schreier_sims())
for C,af,a,ad in gent:
    RR=S*C**-1*T*C
    for H in ders:
        if H*R*H**-1!=RR or H*R**af not in felements:continue
        B=H**-1*C**-1
        co=[C,B,H,C**-1,B**-1,H**-1]
        if not K6d.contains(direct(co,qx**af)):continue
        allmem.append((C,H,af,a,ad))
        def cv(t):j,M=t;return M*co[j]*M**-1
        if not all(cv(c[0])*cv(c[1])*v==G.identity for c,v in zip(cycles,co)):continue
        allgent.append((C,H,af,a,ad))
print('full common word',Counter((ad+af)%3 for C,H,af,a,ad in allmem),flush=True)
print('all cycles',Counter((ad+af)%3 for C,H,af,a,ad in allgent),flush=True)
out=dict(scope='necessary finite conditions only; no lifting conclusion',
         induced_B_order=int(G.order()),induced_F_order=int(F.order()),
         induced_B_derived_order=int(der.order()),
         six_plus_original_order=int(K6.order()),
         six_plus_original_derived_order=int(K6d.order()),
         common_word_counts=dict(Counter((ad+af)%3 for C,H,af,a,ad in allmem)),
         all_cycle_counts=dict(Counter((ad+af)%3 for C,H,af,a,ad in allgent)))
assert out['all_cycle_counts']=={0:108,1:108,2:108}
(Path(__file__).resolve().parents[1]/'records'/'cubic_descent_shadow.json').write_text(
    json.dumps(out,indent=2)+'\n')

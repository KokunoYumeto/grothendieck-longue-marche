#!/usr/bin/env python3
"""Exact certificates for H^1(SL_2(Z), E[n]) and its nonzero class.

The amalgam presentation is <R,S | R^4=S^6=1, R^2=S^3>.
The integral matrices have zero norm sums for their orders.
A cocycle is determined by u=z(R),v=z(S), with
(1+R)u=(1+S+S^2)v.  Coboundaries are ((R-1)m,(S-1)m).
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

R=((0,-1),(1,0))
S=((0,-1),(1,1))
def act(A,x,n):
    return tuple(sum(A[i][j]*x[j] for j in range(2))%n for i in range(2))
def add(x,y,n):return tuple((a+b)%n for a,b in zip(x,y))
def sub(x,y,n):return tuple((a-b)%n for a,b in zip(x,y))
def a(x,n):return add(x,act(R,x,n),n)
def b(x,n):return add(add(x,act(S,x,n),n),act(S,act(S,x,n),n),n)

rows=[]
for n in list(range(1,17))+[24,32,64]:
    M=list(product(range(n),repeat=2))
    ca,cb=Counter(a(x,n) for x in M),Counter(b(x,n) for x in M)
    z1=sum(v*cb[k] for k,v in ca.items())
    boundaries={(sub(act(R,x,n),x,n),sub(act(S,x,n),x,n)) for x in M}
    size=z1//len(boundaries)
    assert z1%len(boundaries)==0 and size==(2 if n%2==0 else 1)
    row={'n':n,'cocycles':z1,'coboundaries':len(boundaries),'H1_order':size}
    if n%2==0:
        c=(n//2,0)
        z=((0,0),sub(act(S,c,n),c,n))
        assert a(z[0],n)==b(z[1],n)
        assert z not in boundaries
        assert tuple(add(t,t,n) for t in z)==((0,0),(0,0))
        scaled=tuple(tuple(2*k for k in t) for t in z)
        c2=(n,0)
        z2=((0,0),sub(act(S,c2,2*n),c2,2*n))
        assert scaled==z2
        row.update(nonzero_cocycle=z,inclusion_to_2n_preserves_generator=True)
    rows.append(row)

M=list(product(range(2),repeat=2))
index={x:i for i,x in enumerate(M)}
c=(1,0)
shift=sub(act(S,c,2),c,2)
pR=tuple(index[act(R,x,2)] for x in M)
pS=tuple(index[add(act(S,x,2),shift,2)] for x in M)
def comp(p,q):return tuple(p[q[i]] for i in range(4))
identity=tuple(range(4));group={identity};todo=[identity]
while todo:
    p=todo.pop()
    for q in [pR,pS]:
        t=comp(p,q)
        if t not in group:group.add(t);todo.append(t)
assert len(group)==24
assert {p[0] for p in group}==set(range(4))
assert all(pR[i]!=i or pS[i]!=i for i in range(4))
def order(p):
    q=identity
    for k in range(1,25):
        q=comp(q,p)
        if q==identity:return k
    raise AssertionError
assert order(pR)==2 and order(pS)==3 and order(comp(pR,pS))==4

result={'matrices':{'R':R,'S':S},'finite_cohomology':rows,
        'affine_two_torsion_cover':{'points':M,'R':pR,'S':pS,
        'group_order':len(group),'orbit_size':4,
        'orders_R_S_RS':[order(pR),order(pS),order(comp(pR,pS))]}}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

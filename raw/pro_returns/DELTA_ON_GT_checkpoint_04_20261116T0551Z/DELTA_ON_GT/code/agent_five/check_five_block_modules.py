#!/usr/bin/env python3
"""Exact small finite ingredients of FP.22.
No enumeration of pentagon shadows or claim of a global GT element.
"""
from itertools import product, combinations
import json

def mm(a,b,n):
 p,q,r,s=a;t,u,v,w=b
 return ((p*t+q*v)%n,(p*u+q*w)%n,(r*t+s*v)%n,(r*u+s*w)%n)
def inv(a,n):p,q,r,s=a;return(s%n,-q%n,-r%n,p%n)
def comm(a,b,n):return mm(mm(mm(a,b,n),inv(a,n),n),inv(b,n),n)
I=(1,0,0,1);minusI=(2,0,0,2)
G=[x for x in product(range(3),repeat=4) if (x[0]*x[3]-x[1]*x[2])%3==1]
Q=[x for x in G if x in (I,minusI) or (x[0]+x[3])%3==0]
assert len(G)==24 and len(Q)==8
for a in Q:
 for b in Q:assert mm(a,b,3) in Q
X=(1,2,0,1);S=(0,1,2,0)
eps={}
powx=I
for k in range(3):
 for g in Q:eps[mm(powx,g,3)]=k
 powx=mm(powx,X,3)
assert len(eps)==24
for a in G:
 for b in G:assert eps[mm(a,b,3)]==(eps[a]+eps[b])%3
C=[c for c in product(range(3),repeat=5) if sum(c)%3==0]
assert len(C)==81
cols=[tuple(int(i not in pair) for i in range(5)) for pair in combinations(range(5),2)]
span={(0,0,0,0,0)}
for v in cols:span={tuple((a[i]+k*v[i])%3 for i in range(5)) for a in span for k in range(3)}
assert span==set(C)
for i in range(5):
 for j in range(i+1,5):
  assert any(c[i]!=c[j] for c in C)
  assert any(c[i]!=(-c[j])%3 for c in C)
# Every nontrivial 2-dimensional F2 C3 module is irreducible; check explicit matrix.
M=((0,1),(1,1))
def act(v):return ((M[0][0]*v[0]+M[0][1]*v[1])%2,(M[1][0]*v[0]+M[1][1]*v[1])%2)
assert all(act(v)!=v for v in [(1,0),(0,1),(1,1)])
noncentral=[g for g in Q if g not in (I,minusI)]
assert any(comm(a,b,3)==minusI for a in noncentral for b in noncentral)
# CRT lifts that are identity mod4 and produce the desired parity changes mod3.
Stilde=(9,4,8,9);fiveI=(5,0,0,5);S12=(0,1,11,0)
assert tuple(a%4 for a in Stilde)==I and tuple(a%3 for a in Stilde)==S
assert mm(Stilde,S12,12)==mm(S12,Stilde,12)
assert mm(Stilde,Stilde,12)==fiveI
assert tuple(a%4 for a in fiveI)==I and tuple(a%3 for a in fiveI)==minusI
print(json.dumps({'SL2_F3_order':len(G),'Q8_order':len(Q),'abelian_image_order':len(C),'module_characters_distinct_up_to_inversion':True,'joint_pure_image_order_from_proof':8**5*3**4,'joint_commutator_image_order_from_proof':8**5,'W_parity_toggle_mod12':Stilde,'T_parity_toggle_mod12':fiveI,'all_small_finite_checks':'passed'},indent=2))

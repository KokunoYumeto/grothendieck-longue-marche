#!/usr/bin/env python3
"""Exact double-cover obstruction for the A6 passport in check_A28_s6_passport.py.
Permutations C,D are the ATLAS 2.S6 representation 2S6G1-p80B0.
Sources opened: https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/mtx/2S6G1-p80B0.m1
and .m2.  Their declared degree/order are verified below, not assumed.
"""
from collections import Counter

def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inv(a):return tuple(a.index(i) for i in range(len(a)))
def parity(a):return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
def cyc(n,*cs):
    a=list(range(n))
    for c in cs:
        for u,v in zip(c,c[1:]+c[:1]):a[u-1]=v-1
    return tuple(a)
def power(a,k):
    if k<0:return power(inv(a),-k)
    b=tuple(range(len(a)))
    while k:
        if k&1:b=mul(b,a)
        a=mul(a,a);k//=2
    return b

aC=[1,5,3,8,2,13,11,4,16,17,7,21,6,24,22,9,10,30,28,31,12,15,34,14,38,27,26,19,42,18,20,45,33,23,52,50,54,25,58,59,60,29,64,65,32,46,68,69,67,36,62,35,71,37,72,73,66,39,40,41,77,51,76,43,44,57,49,47,48,80,53,55,56,74,75,63,61,78,79,70]
aD=[2,6,7,1,10,9,14,3,4,18,19,5,23,15,8,20,27,22,26,11,32,12,35,36,13,16,40,30,17,44,45,47,21,49,39,53,24,56,25,43,28,62,29,61,66,31,48,33,68,69,34,70,55,51,37,50,38,71,75,73,41,65,42,79,78,67,46,54,57,64,80,52,59,58,76,60,74,63,72,77]
assert sorted(aC)==list(range(1,81)) and sorted(aD)==list(range(1,81))
C=tuple(v-1 for v in aC);D=tuple(v-1 for v in aD)
c=cyc(6,(1,2));d=cyc(6,(2,3,4,5,6))
one6=tuple(range(6));one80=tuple(range(80))
# Enumerate the joint group and retain its exact homomorphism to S6.
seen={(one6,one80)};queue=[(one6,one80)]
for q,p in queue:
    for qg,pg in ((c,C),(d,D)):
        b=(mul(q,qg),mul(p,pg))
        if b not in seen:seen.add(b);queue.append(b)
assert len(queue)==1440
assert len({p for q,p in queue})==1440
assert len({q for q,p in queue})==720
cover={p:q for q,p in queue}
K=[p for q,p in queue if q==one6]
assert len(K)==2
central=next(p for p in K if p!=one80)
assert all(mul(central,g)==mul(g,central) for g in (C,D))
A=[p for q,p in queue if not parity(q)]
assert len(A)==720
x=cyc(6,(1,2,3,4),(5,6));y=cyc(6,(1,2,4,6),(3,5));z=inv(mul(x,y));t=cyc(6,(2,4))
T=next(p for q,p in queue if q==t)
assert power(T,2)==one80
liftX=next(p for b,p in queue if b==x)
liftY=next(p for b,p in queue if b==y)
liftZ=inv(mul(liftX,liftY))
assert cover[liftZ]==z
for name,X in [('x',liftX),('y',liftY),('z',liftZ)]:
    thetaX=mul(mul(T,X),inv(T))
    orbit={mul(mul(g,inv(X)),inv(g)) for g in A}
    assert thetaX not in orbit
    assert mul(central,thetaX) in orbit
    allowed=[k for k in (1,3,5,7) if thetaX in {mul(mul(g,power(X,k)),inv(g)) for g in A}]
    assert allowed==[3,5]
    print(name,': lift order 8 =', power(X,8)==one80 and power(X,4)!=one80,
          '; theta(X) conjugate to X^-1 =',thetaX in orbit,
          '; theta(X) conjugate to central*X^-1 =',mul(central,thetaX) in orbit,
          '; allowed unit exponents mod8 =',allowed)
print('joint double-cover order =',len(queue),'even preimage order =',len(A),'central kernel order =',len(K))
print('The negative multiplier -1 mod8 is obstructed already in this central double cover.')

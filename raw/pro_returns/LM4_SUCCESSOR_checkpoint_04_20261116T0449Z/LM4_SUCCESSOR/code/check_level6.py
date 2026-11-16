#!/usr/bin/env python3
"""Exact finite certificates for B.37 (no numerical arithmetic)."""
from itertools import product
from fractions import Fraction

def raw_mul(a,b,n):
    return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,
            (a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)
def canon(a,n):
    return min(tuple(x%n for x in a),tuple(-x%n for x in a))
def matrices(n):
    return {canon(a,n) for a in product(range(n),repeat=4) if (a[0]*a[3]-a[1]*a[2])%n==1}
def mul(a,b,n): return canon(raw_mul(a,b,n),n)
def inv(a,n): return canon((a[3],-a[1],-a[2],a[0]),n)
def generated(gs,n):
    e=canon((1,0,0,1),n); seen={e}; stack=[e]
    while stack:
        a=stack.pop()
        for g in gs:
            b=mul(a,g,n)
            if b not in seen: seen.add(b);stack.append(b)
    return seen

def order(a,n):
    e=canon((1,0,0,1),n); b=e
    for k in range(1,2001):
        b=mul(b,a,n)
        if b==e:return k
    raise AssertionError('order bound')

def comm(a,b,n):return mul(mul(mul(a,b,n),inv(a,n),n),inv(b,n),n)
def derived(G,n):return generated({comm(a,b,n) for a in G for b in G},n)
def center(G,n):return {a for a in G if all(mul(a,b,n)==mul(b,a,n) for b in G)}

G=matrices(6); G2=matrices(2);G3=matrices(3)
e=canon((1,0,0,1),6)
s=canon((0,-1,1,0),6); r=canon((0,-1,1,1),6);tau=mul(s,r,6)
assert len(G)==72 and len(G2)==6 and len(G3)==12
pairs={(canon(a,2),canon(a,3)) for a in G}
assert pairs==set(product(G2,G3))
assert generated([s,r],6)==G
assert (order(s,6),order(r,6),order(tau,6))==(2,3,6)
assert len(center(G,6))==1
D1=derived(G,6);D2=derived(D1,6)
assert len(D1)==12 and D2=={e}
index=len(G);cusps=index//order(tau,6);chi=-Fraction(index,6)
genus=(2-cusps-chi)/2
assert (cusps,genus,1-chi)==(12,1,13)
print('PSL2(Z/6) order:',len(G))
print('CRT bijection with PSL2(F2) x PSL2(F3):',len(pairs),'pairs')
print('Orders of s,r,tau:',order(s,6),order(r,6),order(tau,6))
print('Derived series orders:',len(G),len(D1),len(D2))
print('Center order:',len(center(G,6)))
print('Y(6): cusps =',cusps,', genus =',genus,', free rank =',1-chi)
# A4 automorphisms: the presentation s^2=r^3=(sr)^3=1 has order12.
s3=canon((0,-1,1,0),3);r3=canon((0,-1,1,1),3)
presenting_pairs=[(a,b) for a in G3 for b in G3 if order(a,3)==2 and order(b,3)==3 and order(mul(a,b,3),3)==3 and generated([a,b],3)==G3]
class_r={mul(mul(g,r3,3),inv(g,3),3) for g in G3}
inner_class_pairs=[(a,b) for a,b in presenting_pairs if b in class_r]
assert len(presenting_pairs)==24 and len(inner_class_pairs)==12
inner_pairs={(mul(mul(g,s3,3),inv(g,3),3),mul(mul(g,r3,3),inv(g,3),3)) for g in G3}
assert set(inner_class_pairs)==inner_pairs
print('A4 generating (2,3,3) pairs:',len(presenting_pairs))
print('Pairs preserving the named 3-cycle class:',len(inner_class_pairs),'= inner automorphism pairs')
for p,expected in [(7,3),(11,26)]:
    index=p*(p*p-1)//2;cusps=index//p;genus=(Fraction(index,6)+2-cusps)/2
    assert genus==expected
    print('Y(%d): index = %d, cusps = %d, genus = %s'%(p,index,cusps,genus))
print('PASS: all assertions exact')

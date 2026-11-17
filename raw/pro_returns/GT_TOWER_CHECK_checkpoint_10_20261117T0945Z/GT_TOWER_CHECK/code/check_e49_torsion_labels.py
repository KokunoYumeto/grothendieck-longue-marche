#!/usr/bin/env python3
"""Finite check of the determinant and pair-label ambiguity in E.49."""
from itertools import product
from collections import Counter
p=3
vectors=list(product(range(3),repeat=2))
lines=[frozenset({v,tuple((-a)%3 for a in v)}) for v in [(1,0),(0,1),(1,1),(1,2)]]
def image(M,v): return ((M[0]*v[0]+M[1]*v[1])%3,(M[2]*v[0]+M[3]*v[1])%3)
def determinant(M):return (M[0]*M[3]-M[1]*M[2])%3
def sign(q):return (-1)**sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
counts=Counter()
for M in product(range(3),repeat=4):
 d=determinant(M)
 if not d:continue
 q=tuple(lines.index(frozenset(image(M,v) for v in L)) for L in lines)
 s=sign(q)
 assert (s%3)==d,(M,d,q,s)
 counts[(d,s)]+=1
 assert image(M,(0,0))==(0,0)
print('GL2(F3) matrices:',sum(counts.values()))
for k,v in sorted(counts.items()):print('determinant, pair permutation sign, count:',k[0],k[1],v)
print('Every determinant-minus-one relabelling permutes the four pair labels oddly.')
print('Every determinant-one relabelling permutes the four pair labels evenly.')
# Source free-group class-two calculation: [u^a v^c,u^b v^d]
# has determinant exponent ad-bc. Check every mod-3 matrix in UT3(F3).
def mul(g,h):
 a,b,c=g;d,e,f=h
 return ((a+d)%3,(b+e)%3,(c+f+a*e)%3)
def inv(g):
 a,b,c=g;return (-a%3,-b%3,(-c+a*b)%3)
def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
for a,b,c,d in product(range(3),repeat=4):
 assert comm((a,c,0),(b,d,0))==(0,0,(a*d-b*c)%3)
print('Class-two commutator exponent ad-bc: all 81 mod-3 matrices verified.')
print('ALL CHECKS PASSED')

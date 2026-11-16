#!/usr/bin/env python3
"""Centralizer of the order-five companion matrix at N=12.
This verifies a matrix target only; it constructs no GT action or frame map.
"""
from itertools import product
import json

def mul(a,b,n):
 p=[0]*7
 for i in range(4):
  for j in range(4):p[i+j]+=a[i]*b[j]
 # z^4=-1-z-z^2-z^3
 for k in range(6,3,-1):
  v=p[k]
  for j in range(4):p[k-4+j]-=v
 return tuple(x%n for x in p[:4])
def add(a,b,n):return tuple((x+y)%n for x,y in zip(a,b))
def scale(a,k,n):return tuple(k*x%n for x in a)
def pw(a,k,n):
 o=(1,0,0,0)
 for _ in range(k):o=mul(o,a,n)
 return o
def bar(a,n):
 zi=(n-1,n-1,n-1,n-1) # z^-1=z^4
 o=(0,0,0,0)
 for i,x in enumerate(a):o=add(o,scale(pw(zi,i,n),x,n),n)
 return o
def torus(n):return [a for a in product(range(n),repeat=4) if mul(a,bar(a,n),n)==(1,0,0,0)]
def neg(a,n):return tuple(-x%n for x in a)
def canon(a,n):return min(a,neg(a,n))
res={}
for n,expected in ((3,10),(4,20),(12,200)):
 T=torus(n);assert len(T)==expected
 two=[a for a in T if mul(a,a,n)==(1,0,0,0)]
 projective=set(canon(a,n) for a in T)
 ptwo=[a for a in projective if canon(mul(a,a,n),n)==canon((1,0,0,0),n)]
 res[n]={'order':len(T),'two_torsion_order':len(two),'quotient_by_global_sign_order':len(projective),'quotient_two_torsion_order':len(ptwo),'scalar_norm_one':[a[0] for a in T if a[1:]==(0,0,0)]}
assert res[12]['two_torsion_order']==8
assert res[12]['quotient_two_torsion_order']==4
print(json.dumps(res,indent=2))

#!/usr/bin/env python3
"""Complete computation in (Z/9)[a]/(a^3-3), the local quotient by a^6."""
from itertools import product
M=9;one=(1,0,0)
def add(a,b):return tuple((x+y)%M for x,y in zip(a,b))
def scale(a,s):return tuple((s*x)%M for x in a)
def mul(a,b):
 c=[0]*5
 for i in range(3):
  for j in range(3):c[i+j]+=a[i]*b[j]
 for d in [4,3]:c[d-3]+=3*c[d]
 return tuple(t%M for t in c[:3])
def power(a,n):
 b=one
 while n:
  if n&1:b=mul(b,a)
  a=mul(a,a);n//=2
 return b
R=list(product(range(M),repeat=3));U=(7,0,1);A=(0,pow(649,8,M),0);B=power(U,3)
assert add(U,scale(one,-1))==mul((0,0,1),(1,8,0))
assert add(B,scale(one,-1))==scale(mul((0,0,1),U),-6)
principal=[x for x in R if x[0]%3==1]
assert len(R)==729 and len(principal)==243
assert all(power(y,9)==one for y in principal)
assert U not in {power(y,3) for y in R}
assert B not in {power(y,9) for y in R}
left={mul(A,power(x,9)) for x in R};right={mul(B,power(y,9)) for y in R}
solutions=[(x,y) for x in left for y in right if add(x,y)==one]
assert not solutions
print('Ring elements:',len(R));print('Principal units:',len(principal))
print('A mod a^6:',A,'; B mod a^6:',B)
print('Distinct A-times ninth powers:',sorted(left));print('Distinct B-times ninth powers:',sorted(right))
print('Integral ordinary solutions modulo a^6:',len(solutions))
print('U is not a cube; B is not a ninth power: verified by complete ring enumeration.')
print('PASS: negative valuations and actual local mod3 existence are handled by the proof E.43.')

#!/usr/bin/env python3
"""Exact finite checks for E.40–E.42; these do not execute an infinite prime recursion."""
from math import gcd,factorial
from fractions import Fraction
from itertools import product
from sympy.ntheory.modular import crt
import sympy as sp

def mul(a,b,m):return ((a[0]+a[1]*b[0])%m,(a[1]*b[1])%m)
def inv(a,m):
 u=pow(a[1],-1,m);return ((-u*a[0])%m,u)
count=0
for m in range(4,65,4):
 c=(0,m-1)
 for u in range(m):
  if gcd(u,m)>1:continue
  for k in range(m):
   g=(k,u);v=mul(mul(mul(c,g,m),inv(c,m),m),inv(g,m),m)
   assert v==((-2*k)%m,1)
   count+=1
print('Kummer conjugation commutators checked:',count)
P=[5,7,11];C=[0,1,3]
R=int(crt([p*p for p in P],[c+p for c,p in zip(C,P)])[0]);A=[R-c for c in C]
def vp(n,p):
 n=abs(n);v=0
 while n and n%p==0:n//=p;v+=1
 return v
assert [[vp(a,p) for a in A] for p in P]==[[1,0,0],[0,1,0],[0,0,1]]
print('Private-prime CRT witness:',{'punctures':C,'primes':P,'R':R,'coefficients':A})
k,m=sp.symbols('k m',integer=True,positive=True)
g2=(k-1)*m**k-(k+1)*m**(k-1)+2
t0=(k+1)*m**k+3;b=(k+1)*m**(k-1)
assert sp.simplify(t0-g2-(2*m**k+(k+1)*m**(k-1)+1))==0
checks=0
for kk in range(2,12):
 for mm in range(2,31):
  gg=int(g2.subs({k:kk,m:mm}));tt=int(t0.subs({k:kk,m:mm}));bb=int(b.subs({k:kk,m:mm}))
  assert gg>=0 and gg%2==0
  assert tt*tt-gg*tt+1-bb>0 and 2*tt>gg
  checks+=1
print('Genus parity and strict large-prime bound cases:',checks)
checks=0
for j in range(15):
 for p in [2,3,5,7,11,13]:
  n=8*factorial(j+1);mm=8*factorial(j+2);nn=8*factorial(j+3)
  L=2*vp(2*nn,p)+j+4
  assert L>2*vp(mm,p)
  assert 2*vp(2*mm,p)+j+3-vp(n,p)>=vp(2*mm,p)
  checks+=1
print('Including two-primary root and next-precision inequalities:',checks)
# Associativity of the bilinear class-two multiplication and its pair projections.
N=3;rank=3;pairs=[(0,1),(0,2),(1,2)]
def law(a,b):
 av,ah=a;bv,bh=b
 return (tuple((av[i]+bv[i])%N for i in range(rank)),tuple((ah[t]+bh[t]+av[i]*bv[j])%N for t,(i,j) in enumerate(pairs)))
unit=((0,0,0),(0,0,0));gens=[(tuple(int(i==j) for i in range(rank)),(0,0,0)) for j in range(rank)]
count=0
for v in product(range(N),repeat=rank):
 for h in product(range(N),repeat=len(pairs)):
  a=(v,h)
  for b in gens:
   for c in gens:
    assert law(law(a,b),c)==law(a,law(b,c));count+=1
print('Class-two generator-edge associativity cases:',count)
print('PASS: exact finite identities; general claims are proved in E.40–E.42.')

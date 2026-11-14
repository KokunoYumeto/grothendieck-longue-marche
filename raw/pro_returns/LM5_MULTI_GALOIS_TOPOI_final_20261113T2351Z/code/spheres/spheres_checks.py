#!/usr/bin/env python3
"""Finite and symbolic checks accompanying LM5 Part D; standard library only.

These calculations check the stated algebra and finite counterexamples. They do
not claim to compute homotopy groups or substitute for the proofs in D.tex.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

print('LM5 Part D reproducible checks')
print('1. Central extensions of C2 by C2')
G=list(product(range(2),repeat=2))
for eps in range(2):
 def mul(x,y):
  a,e=x;b,f=y
  return ((a+b+eps*e*f)%2,(e+f)%2)
 assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(G,repeat=3))
 def order(x):
  a=(0,0)
  for n in range(1,5):
   a=mul(a,x)
   if a==(0,0):return n
 counts=Counter(order(x) for x in G)
 print(f'epsilon={eps}: orders={dict(sorted(counts.items()))}; reflection_lift_square={mul((0,1),(0,1))}')
 assert (order((0,1))==2 if eps==0 else order((0,1))==4)

print('2. SL2 and PGL2 over F2 and F3')
for p in (2,3):
 def det(m):a,b,c,d=m;return (a*d-b*c)%p
 mats=list(product(range(p),repeat=4))
 gl=[m for m in mats if det(m)]
 sl=[m for m in gl if det(m)==1]
 def proj(m):
  first=next(a for a in m if a)
  inv=pow(first,-1,p)
  return tuple((inv*a)%p for a in m)
 pgl={proj(m) for m in gl};psl={proj(m) for m in sl}
 squares={a*a%p for a in range(1,p)}
 U=(1,1,0,1);I=(1,0,0,1)
 assert proj(U)!=proj(I) and proj(U) in psl
 assert len(pgl)//len(psl)==(p-1)//len(squares)
 print(f'F{p}: |SL2|={len(sl)}, |PGL2|={len(pgl)}, |PSL2|={len(psl)}, surviving_automorphism_components={len(pgl)//len(psl)}; nonidentity_unipotent_is_killed=True')

print('3. Chern-root calculation')
roots_standard=(1,-1);roots_adjoint=(2,0,-2)
def c2_coefficient(rs):return sum(rs[i]*rs[j] for i in range(len(rs)) for j in range(i+1,len(rs)))
c2=c2_coefficient(roots_standard);adj=c2_coefficient(roots_adjoint);p1=-adj
assert p1==-4*c2
print(f'with roots measured in x: c2_standard={c2}*x^2, c2_adjoint={adj}*x^2, p1_adjoint={p1}*x^2=-4*c2_standard')

print('4. Moore-space cellular calculation')
# The cochain complex in degrees 3 and 4 is Z --4--> Z.
H4_representatives=list(range(4))
pontryagin=[(-4*c)%4 for c in H4_representatives]
assert pontryagin==[0,0,0,0]
print('M(Z/4,3): d^3=[4], H^4(Z)=Z/4; c2 representatives=',H4_representatives,'; p1 values=',pontryagin,sep='')

print('5. Mod-two polynomial normalization for the degree-six invariant')
# Polynomials in a,b are represented by finite sets of monomial exponents.
def add(p,q):return p^q
def multiply(p,q):
 out=set()
 for a,b in p:
  for c,d in q:
   m=(a+c,b+d)
   if m in out:out.remove(m)
   else:out.add(m)
 return out
def sq1(p):
 out=set()
 for a,b in p:
  if a%2:out=add(out,{(a+1,b)})
  if b%2:out=add(out,{(a,b+1)})
 return out
x={(2,0),(1,1),(0,2)}
y=sq1(x)
y2=multiply(y,y)
assert y=={(2,1),(1,2)}
assert y2=={(4,2),(2,4)}
print('x=a^2+ab+b^2; Sq1(x)=',sorted(y),'; (Sq1 x)^2=',sorted(y2),' (nonzero)',sep='')
print('x^3=',sorted(multiply(multiply(x,x),x)),sep='')

print('6. Quaternion tensor-product basis and valuation cosets')
B=list(product(range(2),repeat=4))
values={tuple(Fraction(i,2) for i in b) for b in B}
assert len(values)==16
# A monomial is (sign, exponent of each central t_i, basis bits).
def multiply_monomials(x,y):
 sx,tx,bx=x;sy,ty,by=y
 sign=sx*sy*(-1)**(bx[1]*by[0]+bx[3]*by[2])
 t=tuple(tx[i]+ty[i]+(bx[i]+by[i])//2 for i in range(4))
 b=tuple((bx[i]+by[i])%2 for i in range(4))
 return sign,t,b
basis=[(1,(0,0,0,0),b) for b in B]
for x,y,z in product(basis,repeat=3):
 assert multiply_monomials(multiply_monomials(x,y),z)==multiply_monomials(x,multiply_monomials(y,z))
for x,y in product(basis,repeat=2):
 z=multiply_monomials(x,y)
 valz=tuple(Fraction(z[1][i])+Fraction(z[2][i],2) for i in range(4))
 valxy=tuple(Fraction(x[2][i]+y[2][i],2) for i in range(4))
 assert valz==valxy
print('16 distinct valuation cosets; 4096 associativity checks passed; 256 multiplicative-valuation checks passed.')
print('ALL CHECKS PASSED')

#!/usr/bin/env python3
from math import isqrt
from fractions import Fraction
import sympy as S
u,a,W=S.symbols('u a W',nonzero=True)
x=u-1/u;z=W**2*(u*u+1)/(u*u)
f=(u**3-u)/(8*a)
assert S.simplify(x.subs(u,-1/u)-x)==0
assert S.simplify(z.subs({u:-1/u,W:W/u},simultaneous=True)-z)==0
assert S.simplify((z**2).subs(W**4,f)-x*(x*x+4)/(8*a))==0
av=Fraction(529,382)*Fraction(147,382)*Fraction((13*155564491)**2,191)
q=Fraction(325596479663,72962)
assert av==573*q*q
counts={}
for b in [8,32]:
 pts=[]
 for xx in range(-isqrt(573//4),isqrt(573//4)+1):
  for zz in range(-isqrt(573//b),isqrt(573//b)+1):
   rem=573-4*xx*xx-b*zz*zz
   if rem<0:continue
   yy=isqrt(rem)
   if yy*yy==rem:
    pts.append((xx,yy,zz))
    if yy:pts.append((xx,-yy,zz))
 counts[b]=len(pts)
print('Both invariant functions and elliptic equation: PASS')
print('Exact a=573*q^2 identity: PASS')
print('Exact ternary counts 573=4x²+y²+bz²:',counts)
print('No rank or Tate–Shafarevich assertion follows from this certificate alone.')

# Independent computation from Tunnell's q-product g*theta_4.
limit=573
coef=[0]*(limit+1);coef[1]=1
for step in [8,16]:
 for exp in range(step,limit+1,step):
  for j in range(limit,exp-1,-1):coef[j]-=coef[j-exp]
b573=coef[573]+2*sum(coef[573-4*j*j] for j in range(1,isqrt(573//4)+1))
assert b573==counts[32]-counts[8]//2==0
print('Independent coefficient b(573) from q-product:',b573)

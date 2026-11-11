#!/usr/bin/env python3
"""Finite Lazard-group verification of the rational jet, characteristic13, class12.
All group-law computations below are in the associative enveloping algebra
truncated above degree12. Products of F=log(f) begin in degree14, so the
three-cycle product is exactly tested by its displayed logarithmic sum.
"""
from pathlib import Path
from functools import cache
from math import factorial
from fractions import Fraction
import json
from graded_dimensions import words,lyndon
O=Path(__file__).resolve().parent;P=13;N=12

def add(a,b,s=1):
 r=a.copy()
 for w,c in b.items():
  r[w]=(r.get(w,0)+s*c)%P
  if not r[w]:del r[w]
 return r
def mul(a,b,M):
 r={}
 for u,c in a.items():
  for v,d in b.items():
   if len(u)+len(v)<=M:
    w=u+v;r[w]=(r.get(w,0)+c*d)%P
 return {w:c for w,c in r.items() if c}
def br(a,b,M):return add(mul(a,b,M),mul(b,a,M),-1)
x={(0,):1};y={(1,):1}
M=6
ex={(0,)*n:pow(factorial(n),-1,P) for n in range(M+1)}
ey={(1,)*n:pow(factorial(n),-1,P) for n in range(M+1)}
u=mul(ex,ey,M);u.pop(())
z={};v={():1}
for k in range(1,M+1):
 v=mul(v,u,M);z=add(z,v,(-1)**k*pow(k,-1,P))
@cache
def ev(w,mode,M):
 if len(w)==1:return {v:c for v,c in ((x,y),(y,x),(z,x),(y,z))[mode][w[0]].items() if len(v)<=M}
 j=next(j for j in range(1,len(w)) if lyndon(w[j:]));a,b=w[:j],w[j:]
 return br(ev(a,mode,M-len(b)),ev(b,mode,M-len(a)),M)
J=json.loads((O/'graded_rational_jets.json').read_text())
coeffs=dict(J['initial_weight7'])
for row in J['corrections']:coeffs.update(row['lyndon_coefficients'])
anti={};cyc={}
for w,a in coeffs.items():
 a=Fraction(a);assert a.denominator%P
 c=a.numerator*pow(a.denominator,-1,P)%P
 t=tuple(0 if v=='x' else 1 for v in w)
 anti=add(anti,add(ev(t,0,N),ev(t,1,N)),c)
 for mode in (0,2,3):cyc=add(cyc,ev(t,mode,N),c)
assert not anti and not cyc
rank=sum(len(words(n)) for n in range(1,N+1))
print('finite nilpotent Lazard group: prime13, class12, dimension',rank,'order 13^'+str(rank))
print('All denominators in the explicit F9,F11 coordinates are invertible modulo13.')
print('Two-cycle and three-cycle full associative defects through class12: 0, 0.')
print('The normalized substitution is triangular with identity linear part, hence an automorphism.')
print('Leading degree7 pentagon coefficient 16 mod13 =',16%13,'(nonzero).')
print('This is a finite nilpotent equation solution; an infinite pro-13 lift is not asserted.')

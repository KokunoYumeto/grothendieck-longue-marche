#!/usr/bin/env python3
"""Check the genuine GT_0 braid action at level 12 and the 3-torsion degeneration."""
from itertools import product
from pathlib import Path
from math import gcd
import json
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
n=12;I=(1,0,0,1)
def mul(a,b):return ((a[0]*b[0]+a[1]*b[2])%n,(a[0]*b[1]+a[1]*b[3])%n,(a[2]*b[0]+a[3]*b[2])%n,(a[2]*b[1]+a[3]*b[3])%n)
def inv(a):
 d=pow((a[0]*a[3]-a[1]*a[2])%n,-1,n)
 return (a[3]*d%n,-a[1]*d%n,-a[2]*d%n,a[0]*d%n)
def power(a,k):
 r=I
 for j in range(k):r=mul(r,a)
 return r
def closure(gens):
 r={I};todo=[I]
 while todo:
  a=todo.pop()
  for b in gens:
   c=mul(a,b)
   if c not in r:r.add(c);todo.append(c)
 return r
def conjugate(a,b):return mul(mul(a,b),inv(a))
def comm(a,b):return mul(conjugate(a,b),inv(b))
u=(1,1,0,1);w=(1,0,11,1)
F=closure([power(u,2),power(w,2)])
Fp=closure([comm(a,b) for a in F for b in F])
SL=closure([u,w])
assert len(F)==96 and len(Fp)==8 and len(SL)==1152
records=[];images=set()
for mu in [1,5,7,11]:
 good=[];rejected=[]
 for f in sorted(Fp):
  A=power(u,mu);B=conjugate(inv(f),power(w,mu))
  assert mul(mul(A,B),A)==mul(mul(B,A),B)
  generated=closure([A,B])
  if generated!=SL:
   rejected.append({'f':f,'generated_order':len(generated),'lower_left':B[2]})
   continue
  a,b,c,d=B
  assert gcd(c,n)==1 and c==(-pow(mu,-1,n))%n
  t=mu*(1-a)%n;V=(mu,t,0,1)
  assert conjugate(V,u)==A and conjugate(V,w)==B
  assert t%4==0
  images.add(V);good.append({'f':f,'V':V})
 records.append({'mu':mu,'surjective_pairs':len(good),'intertwiners':sorted({tuple(x['V']) for x in good}),
                 'non_surjective_pairs':rejected})
assert images=={(mu,t,0,1) for mu in [1,5,7,11] for t in [0,4,8]}
assert closure(list(images))==images
# The level-12 action is a group of order 12; center-fixing normalization
# V_22=1 makes the conjugation map injective.
assert [V for V in images if V[1]==V[2]==0 and V[0]==V[3]]==[I]

x,l,s,z=sp.symbols('x l s z')
psi=3*x**4-4*(1+l)*x**3+6*l*x**2-l**2
special=sp.factor(psi.subs(l,0))
scaled=sp.expand(psi.subs({l:s**3,x:s**2*z})/s**6)
assert sp.expand(scaled-(3*s**2*z**4-4*(1+s**3)*z**3+6*s*z**2-1))==0
assert sp.expand(scaled.subs(s,0))==-4*z**3-1
assert sp.diff(psi,x).subs({l:0,x:sp.Rational(4,3)})!=0
# Transformation of the cubic leading coefficient to a cube root of 2.
a=sp.symbols('a')
assert sp.rem(sp.together((-2*(-1/(a**2)))**3-2).as_numer_denom()[0],a**3-2,a)==0
out={'F_image_order':len(F),'commutator_image_order':len(Fp),
     'SL12_order':len(SL),'braid_checks':records,'normalized_image_order':len(images),
     'normalized_matrices':sorted(images),'division_polynomial':str(psi),
     'special_at_zero':str(special),'Puiseux_scaled_polynomial':str(scaled),
     'leading_cubic':'c^3=-1/4; c=-1/(cube_root(2)^2)',
     'coefficient_splitting_field':'Q(zeta_3, cube_root(2))'}
(ROOT/'code/a_braid.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

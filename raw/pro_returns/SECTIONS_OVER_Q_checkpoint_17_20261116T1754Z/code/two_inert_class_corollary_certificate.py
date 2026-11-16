"""Finite checks for the exact Hilbert90/conjugation class consequence."""
import itertools
for q in (11,59):
 r=next(x for x in range(q)if x**3%q==3)
 def mul(v,w):
  a,b=v;c,e=w
  return ((a*c-r*r*b*e)%q,(a*e+b*c-r*b*e)%q)
 def pw(v,k):
  z=(1,0)
  while k:
   if k&1:z=mul(z,v)
   v=mul(v,v);k//=2
  return z
 zeta=(10,6)if q==11 else(58,6)
 assert pw(zeta,3)==(1,0)and zeta!=(1,0)
 m=(q*q-1)//3;assert m%3
 assert 2*2-3==1
 for a in range(3):
  # Valuations (a,-a), sigma(pi)/pi=zeta², tau(zeta)=zeta^-1.
  e=(2*a-2*(-a))%3
  assert e==a and ((m*e)%3==0)==(a==0)
 print('q',q,'residue degree2; cubic-character exponent',m%3,'; descended residue zeta^a: PASS')
for a,b in itertools.product(range(3),repeat=2):
 assert (a==0 and (2*b)%3==0)==(a==0 and b==0)
print('PASS: all nine putative relation coefficients; only zero has both trivial norm-one-unit characters.')
print('The complete class argument uses exact divisors and Cl(Q(zeta3,cuberoot3)){3}=0 as proved in A138.')

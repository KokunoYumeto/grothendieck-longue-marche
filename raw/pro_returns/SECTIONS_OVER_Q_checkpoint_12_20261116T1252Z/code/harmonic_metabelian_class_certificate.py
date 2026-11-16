"""Exact integral module and curve-map checks for A.157.

No profinite section is simulated: the arithmetic conclusion is proved by
the finite-cover and Kummer maps in the source.  This certifies their
literal polynomial identities and the integral geometric presentation.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

T,W,a,t=s.symbols('T W a t',nonzero=True)
F=T*(T-1)*(T-s.Rational(1,2))
f=4*T*(1-T)
assert s.expand(64*F**2-f**2*(1-f))==0
assert s.factor(s.Rational(1,2)-4*F/f-T)==0
Tin=s.Rational(1,2)-4*a*W**4/t
assert s.factor(4*Tin*(1-Tin)-t+(64*a*a*W**8-t*t*(1-t))/t**2)==0
assert s.factor(F.subs(T,1-T)+F)==0
print('Both curve-map compositions, eighth-power identity, and deck sign: PASS')

# Integral H-ab coordinates u0,...,u7,z and the four inertia words.
z=s.Matrix([0]*8+[1])
even=s.Matrix([int(j%2==0) for j in range(8)]+[1])
odd=s.Matrix([int(j%2==1) for j in range(8)]+[1])
inf=s.Matrix([-1]*8+[-3])
assert z+even+odd+inf==s.zeros(9,1)
B=s.Matrix.hstack(z,even,odd)
assert B.rank()==3
assert abs(B.extract([8,6,7],[0,1,2]).det())==1
# Explicit quotient sends u6=-u0-u2-u4 and u7=-u1-u3-u5.
Q=s.zeros(6,9)
for j in range(6): Q[j,j]=1
for j in [0,2,4]: Q[j,6]=-1
for j in [1,3,5]: Q[j,7]=-1
assert Q*B==s.zeros(6,3)
assert Q[:,:6]==s.eye(6)
print('Four inertia vectors, primitive rank-three lattice, free rank-six quotient: PASS')

V=s.zeros(6)
for j in range(5):V[j+1,j]=1
for j in [0,2,4]:V[j,5]=-1
assert V**6+V**4+V**2+s.eye(6)==s.zeros(6)
assert V**8==s.eye(6)
assert V.det()==1
e=s.Matrix([1,0,0,0,0,0])
assert sum((V**(2*j)*e for j in range(4)),s.zeros(6,1))==s.zeros(6,1)
assert sum((V**(2*j+1)*e for j in range(4)),s.zeros(6,1))==s.zeros(6,1)
assert (V-s.eye(6))**6%2==s.zeros(6)
assert (V-s.eye(6))**5%2!=s.zeros(6)
rows=[]
for m in range(1,13):
    mod=2**m
    assert (V**8-s.eye(6))%mod==s.zeros(6)
    rows.append({'m':m,'module_rank':6,'cyclic_order':8,'group_order':2**(6*m+3)})
print('Companion action, order-eight splitting and reductions m=1..12: PASS')

M=325596479663
aa=573*Fraction(M,2*191**2)**2
assert aa==Fraction(318039202706815117780707,27871484)
print('Literal A145/A154 cover coefficient equality: PASS')
data={'inertia_vectors':[list(map(int,v)) for v in [z,even,odd,inf]],
      'quotient_matrix':[list(map(int,Q.row(i))) for i in range(6)],
      'action_matrix':[list(map(int,V.row(i))) for i in range(6)],
      'finite_orders':rows,'cover_coefficient':str(aa)}
Path(__file__).with_name('harmonic_metabelian_class_certificate_data.json').write_text(json.dumps(data,indent=2)+'\n')
print('A157 exact certificate: PASS')

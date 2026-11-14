#!/usr/bin/env python3
"""Independent exact checks of the F4 theta-fifteen certificate.

This uses SymPy Groebner reduction over F2, not the author's F4
polynomial/Hankel engine. Divisor, gonality and section implications
are proved separately in the mathematical audit.
"""
from pathlib import Path
import json
from math import gcd
import sympy as s

x,t,a,T=s.symbols('x t a T')
G=s.groebner([a*a+a+1,t*t+a*t+1],x,t,a,modulus=2)
def red(p):
    return G.reduce(s.expand(p))[1]

Acoef=[a*a+t,a*t,t,1+t,a*a+a*t,1+a*a*t,1+t]
Bcoef=[a,a+t,a+t,1+t,a*a*t,a*t,1]
A=sum(v*x**i for i,v in enumerate(Acoef))
B=sum(v*x**i for i,v in enumerate(Bcoef))
u=x*(x+1)
F=x**3+x**2+a
delta=a*t
norm=u*(A*A+A*B)+B*B*(F+delta*u)
assert red(norm+(x+t)**15)==0
assert red(A.subs(x,t))==0
assert red(B.subs(x,t)+t)==0
assert red(B.subs(x,0)+a)==0
assert red(B.subs(x,1)+a)==0
assert red(t**3+t*t+a+delta*t*(t+1))==0
assert red(t**4+t+a)==0
assert red(t**5+1)==0
assert red(t)!=0 and red(t+1)!=0

# A separate formal-jet calculation rules out all geometric theta-five
# points. Here T is independent of the selected order-fifteen coordinate t.
Ga=s.groebner([a*a+a+1],T,a,modulus=2)
def ra(p):
    return Ga.reduce(s.expand(p))[1]
D=T*(T+1)
P={}
for k in range(1,5):
    p=a*T**(k-1)*(T+1)**(2*k)+a*T**(2*k)*(T+1)**(k-1)
    if k==1:p+=D**2
    if k%2==0:p+=P[k//2]**2
    P[k]=ra(p)
f=T**4+T+a
m1=ra(P[2]**2+P[1]*P[3])
m2=ra(P[2]*P[3]+P[1]*P[4])
assert ra(m1+f**4)==0
Gf=s.groebner([a*a+a+1,f],T,a,modulus=2)
assert Gf.reduce(m2)[1]==a+1
assert Gf.reduce(P[1]+D)[1]==0
assert Gf.reduce(P[2]+D+1)[1]==0
assert Gf.reduce(P[3]+a*D+a*a)[1]==0
assert Gf.reduce(P[4]+a*D+1)[1]==0
assert ra((1+a+a)**3+a*a)==a

orbits=[]
remaining=set(range(1,15))
while remaining:
    j=min(remaining);orbit=[];z=j
    while z not in orbit:
        orbit.append(z);z=2*z%15
    remaining.difference_update(orbit);orbits.append(orbit)
primitive={i for i in range(1,15) if gcd(i,15)==1}
hit=set(next(o for o in orbits if 1 in o))|set(next(o for o in orbits if 14 in o))
assert hit==primitive and len(hit)==8
survivors=set(range(1,15))-primitive
assert len(survivors)==6
assert gcd(15,*survivors)==1

# The two-prime group-ring operator has exactly the primitive support.
support=[i for i in range(15) if (3*i)%15 and (5*i)%15]
assert set(support)==primitive
out={
  'status':'PASS',
  'method':'SymPy Groebner reduction over F2; independent of author polynomial engine',
  'field_relations':['alpha^2+alpha+1=0','t^2+alpha*t+1=0'],
  'norm_identity':'u*(A^2+A*B)+B^2*(x^3+x^2+alpha+alpha*t*u)=(x+t)^15',
  'point_value':'phi(t)=alpha*t',
  'A_at_t':'0','B_at_t':'t','B_at_zero_and_one':'alpha',
  'theta_five_exclusion':{'first_minor':'(T^4+T+alpha)^4','second_minor_mod_radical':'alpha^2, nonzero'},
  'cubic_obstruction':'alpha, nonzero',
  'doubling_orbits':orbits,
  'primitive_characters':sorted(primitive),
  'surviving_nontrivial_characters':sorted(survivors),
  'cover_genus':16,
  'two_rank_from_proved_character_argument':8,
  'deck_kernel_order_from_survivor_gcd':1,
  'primitive_operator':'(1-sigma^3)*(1-sigma^5)',
  'scope':'Exact algebra and character arithmetic only; geometry and A1 consequence are separate proofs.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

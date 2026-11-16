#!/usr/bin/env python3
"""Literal finite maps and prime valuations in A.136."""
from fractions import Fraction as F
from itertools import product
from sympy import symbols, expand, factorint
T,X0,X1,Xh,a0,a1,ah=symbols("T X0 X1 Xh a0 a1 ah")
f=4*T*(1-T)
assert expand(1-f-4*(T-F(1,2))**2)==0
assert expand(f+8+4*(T-2)*(T+1))==0
assert [f.subs(T,t) for t in (0,1,F(1,2),2,-1)]==[0,0,1,-8,-8]
assert f.subs(T,F(1,4))==F(3,4)
count=0
for N in (1,2,3,4,8,12,16,20):
    assert expand(-4*(a0*X0**N)*(a1*X1**N)-(-4*a0*a1)*(X0*X1)**N)==0
    assert expand(4*(ah*Xh**N)**2-(4*ah**2)*(Xh**2)**N)==0
    count+=2
def sc(a):
    a=F(a)
    return frozenset(([-1] if a<0 else [])+
        [int(p) for p,e in factorint(abs(a.numerator)).items() if e%2]+
        [int(p) for p,e in factorint(a.denominator).items() if e%2])
fields=0
for u0,u1,uh in product((F(1),F(2,3),F(-5,7),F(11,13)),repeat=3):
    A0=F(1,4)*u0**4
    A1=F(-3,4)*u1**4
    Ah=F(-1,4)*uh**4
    A=-4*A0*A1
    B=4*Ah**2
    assert A==F(3,4)*(u0*u1)**4
    assert B==F(1,4)*uh**8
    assert sc(-8/A)==frozenset({-1,2,3})
    assert sc(9/B)==frozenset()
    assert frozenset({-1}) not in {frozenset(),sc(-8/A)}
    fields+=1
primes=(577,601,937,1201,1801,2473,2593,2833,4057,4297)
vals=0
for p in primes:
    t=2+p
    x=4*t*(1-t)
    assert x+8==-4*p*(p+3)
    assert (x+8)%p==0 and (x+8)%(p*p)!=0
    assert x not in (0,1,-8)
    assert (t+1)%p
    vals+=1
print("A.136 tripod escaping-support certificate: PASS")
print("symbolic coordinate identities:",count+3)
print("actual four-power coefficient/common-field checks:",fields)
print("literal forced-prime valuation checks:",vals)
print("No full fundamental-group section or infinite prime execution is asserted.")


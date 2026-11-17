#!/usr/bin/env python3
"""Exact certificates for the two isogeny descents and support-prime tests."""
from fractions import Fraction as Q
from math import gcd
import sympy as s

x,y=s.symbols('x y')
relation=y*y-x**3+243
Y=y*(x**3+1944)/(27*x**3)
expr=s.cancel(Y-3-((y-27)/(3*x))**3)
assert s.rem(s.Poly(s.fraction(expr)[0],y,x),s.Poly(relation,y,x)).is_zero
print('PASS: (Y-3) composed with psi equals ((y-27)/(3x))^3')

classes={( (i+2*j)%3, (i+j)%3 ) for i in range(3) for j in range(3)}
assert len(classes)==9
print('PASS: the valuation vectors of 6 and 12 span all nine {2,3}-unit cube classes')

def add(P,R,p=None):
    if P is None: return R
    if R is None: return P
    x,y=P; u,v=R
    mod=(lambda z:z%p) if p else (lambda z:z)
    if x==u and mod(y+v)==0: return None
    numer,denom=(3*x*x,2*y) if P==R else (v-y,u-x)
    k=mod(numer*pow(denom,-1,p)) if p else Q(numer,denom)
    X=mod(k*k-x-u)
    return X,mod(-y+k*(x-X))

def mul(n,P,p):
    R=None
    while n:
        if n&1: R=add(R,P,p)
        P=add(P,P,p); n//=2
    return R

P0=(6,15); T=(0,3)
assert add(P0,T)==(-2,1)
assert add(P0,(0,-3))==(3,-6)
assert add(add(T,T),T) is None
print('PASS: P0+T=(-2,1), P0-T=(3,-6), and T has exact order three')

def cardinality(p):
    return 1+sum(1 if (z:=(a*a*a+9)%p)==0 else 2 if pow(z,(p-1)//2,p)==1 else 0 for a in range(p))

def order(P,p,N):
    P=(P[0]%p,P[1]%p)
    n=N
    assert mul(n,P,p) is None
    for ell in s.factorint(N):
        while n%ell==0 and mul(n//ell,P,p) is None:
            n//=ell
    return n

p=4177; N=cardinality(p)
assert N==4212
orders={str(P):order(P,p,N) for P in (P0,T,(-2,1),(3,-6))}
assert orders[str((-2,1))]==234 and orders[str((3,-6))]==234
print(f'PASS: at the small Heisenberg witness q={p}, #E\'(Fq)={N}, point orders={orders}')

assert all((u*u+u+1)%9!=0 for u in range(9))
print('PASS: X^2+X+1 has no root modulo nine')

def is_power(a,n,p):
    return pow(a%p,(p-1)//gcd(n,p-1),p)==1

def first_example(radical,power,noncube):
    for k in range(1,200000):
        p=120*k+1
        if s.isprime(p) and is_power(radical,power,p) and not is_power(noncube,3,p):
            return p
    raise AssertionError('No small auxiliary certificate found')

q=first_example(-2,24,3)
r=first_example(3,120,2)
for p,P in ((q,(-2,1)),(r,(3,-6))):
    N=cardinality(p)
    assert N%3==0 and N%9!=0
    n=order(P,p,N)
    assert n%3
    print(f'PASS: auxiliary passing support prime {p}, #E\'(Fp)={N}, ord({P})={n}')
print('These finite-field examples omit the enormous recursive CRT modulus and are not the actual A.44 primes.')

#!/usr/bin/env python3
"""Independent exact algebra for the R6 audit.

The computations certify identities and finite examples; the accompanying
paper proves Selmer completeness, continuous cohomology, and the Chebotarev
recursion. No finite search is used to claim those infinite assertions.
"""
from fractions import Fraction
from math import gcd
import sympy as S

u, v, x, y, z = S.symbols("u v x y z")
cubic = 3*u**3 - 2*v**3 - 1
d = 3*u*(u-1) - 2*v*(v-1)
iX = 18*(u*v-1)/d
iY = -27*(3*u*(u+1)+2*v*(v+1))/d

def reduce_zero(expression, relation, variables):
    numerator = S.fraction(S.cancel(expression))[0]
    return S.Poly(numerator, *variables).rem(S.Poly(relation, *variables)).is_zero

assert reduce_zero(iY**2-iX**3+243, cubic, (u, v))
assert S.factor(S.resultant(cubic, d, v)) == 12*(u-1)**3*(3*u**3+2)
vjet = S.series(((3*(1+z)**3-1)/2)**S.Rational(1,3), z, 0, 4).removeO()
assert S.series(d.subs({u:1+z, v:vjet}), z, 0, 4).removeO() == S.Rational(5,4)*z**3
assert S.series((u*v-1).subs({u:1+z, v:vjet}), z, 0, 2).removeO() == S.Rational(5,2)*z
print("PASS: cubic-to-E identity; denominator resultant = 12(u-1)^3(3u^3+2).")
print("PASS: at (1,1), denominator has order 3 and x numerator has order 1.")
print("      Together with cancellation at uv=1, u^3=-2/3, this proves degree one.")

phiX = (x**3+36)/x**2
phiY = y*(x**3-72)/x**3
psiX = (x**3-972)/(9*x**2)
psiY = y*(x**3+1944)/(27*x**3)
assert reduce_zero(phiY**2-phiX**3+243, y*y-x**3-9, (y, x))
assert reduce_zero(psiY**2-psiX**3-9, y*y-x**3+243, (y, x))
assert reduce_zero(psiY-3-((y-27)/(3*x))**3, y*y-x**3+243, (y, x))
print("PASS: both degree-three isogenies and the literal psi-Kummer identity.")

def add(P, Q, modulus=None):
    if P is None: return Q
    if Q is None: return P
    a,b = P; c,e = Q
    mod = (lambda t: t % modulus) if modulus else (lambda t:t)
    if a == c and mod(b+e) == 0: return None
    nn,dd = (3*a*a, 2*b) if P == Q else (e-b,c-a)
    slope = mod(nn*pow(dd, -1, modulus)) if modulus else Fraction(nn,dd)
    xx = mod(slope*slope-a-c)
    return xx, mod(slope*(a-xx)-b)

def times(n,P,p):
    answer = None
    while n:
        if n & 1: answer = add(answer,P,p)
        P=add(P,P,p); n >>= 1
    return answer

P0=(6,15); T=(0,3)
assert add(P0,T)==(-2,1)
assert add(P0,(0,-3))==(3,-6)
assert add(add(T,T),T) is None
assert len({((a+b)%3,(a+2*b)%3) for a in range(3) for b in range(3)}) == 9
assert {k**3 % 9 for k in range(9) if k%3} == {1,8}
print("PASS: P0+T=(-2,1), P0-T=(3,-6); T has order 3.")
print("PASS: 6,12 are independent cube classes globally and over Q_3.")

# Check phi o psi against the ordinary addition formula on E.
f=x**3-243
double_x=S.cancel((3*x*x)**2/(4*f)-2*x)
double_y_over_y=S.cancel(3*x*x*(x-double_x)/(2*f)-1)
triple_slope_over_y=S.cancel((double_y_over_y-1)/(double_x-x))
triple_x=S.cancel(f*triple_slope_over_y**2-x-double_x)
triple_y_over_y=S.cancel(triple_slope_over_y*(x-triple_x)-1)
assert S.cancel((psiX**3+36)/psiX**2-triple_x)==0
assert S.cancel((x**3+1944)/(27*x**3)*(psiX**3-72)/psiX**3-triple_y_over_y)==0
print("PASS: phi composed with psi is exactly [3] on E.")

# On the cubic, check g0=psi o iota + P0, using subtraction of P0.
gX=6*u*v; gY=3*(3*u**3+2*v**3)
slope=(gY+15)/(gX-6)
minus_X=slope**2-gX-6
minus_Y=slope*(gX-minus_X)-gY
assert reduce_zero(minus_X-(iX**3-972)/(9*iX**2),cubic,(u,v))
assert reduce_zero(minus_Y-iY*(iX**3+1944)/(27*iX**3),cubic,(u,v))
up=S.Rational(253,655); vp=S.Rational(-488,655)
assert 3*up**3-2*vp**3 == 1
assert iX.subs({u:up,v:vp}) == phiX.subs({x:6,y:15})
assert iY.subs({u:up,v:vp}) == phiY.subs({x:6,y:15})
print("PASS: boundary identity g0=[3]+P0; exact u(P0), v(P0) values.")

def cardinality(p):
    squares={a*a%p for a in range(p)}
    return 1+sum(1 if (a**3+9)%p==0 else 2 if (a**3+9)%p in squares else 0 for a in range(p))

def point_order(P,p,total):
    P=(P[0]%p,P[1]%p)
    assert times(total,P,p) is None
    n=total
    for ell in S.factorint(total):
        while n%ell==0 and times(n//ell,P,p) is None: n//=ell
    return n

assert all((a*a+a+1)%9 for a in range(9))
print("PASS: no automorphism of a cyclic group of order 9 satisfies rho^2+rho+1=0.")
for p,point,expected_n,expected_order in [(2281,(-2,1),2361,787),(19441,(3,-6),19200,40),(4177,(-2,1),4212,234)]:
    n=cardinality(p); order=point_order(point,p,n)
    assert (n,order)==(expected_n,expected_order)
    print(f"PASS: p={p}: #E'(F_p)={n}; order({point})={order}.")
print("Finite examples are auxiliary certificates, not the enormous recursive A.44 primes.")

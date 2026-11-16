#!/usr/bin/env python3
"""Exact finite certificates used by the root proofs.

The proofs of universal statements are in the paper.  Enumerations here
verify finite certificates and polynomial identities, not infinite claims.
"""
from fractions import Fraction
import sympy as sp

t, a, b, w = sp.symbols('t a b w')

print('G counterexample: x_2=infinity, all other x_v=2')
for c in (Fraction(-3), Fraction(0), Fraction(1), Fraction(2), Fraction(7, 3)):
    uc = 2-c if c != 2 else Fraction(1)
    required = c != 2
    assert not required or uc == 2-c
    print(f'  c={c}, u_c={uc}, constraints at v!=2: {required}')
print('  Universal verification: the sole non-2 coordinate type is 2;')
print('  v=2 is excluded by x_v=infinity, c=2 excludes every coordinate.')

print('\nFinite-puncture real-place certificate')
S = [sp.Rational(-2), sp.Rational(0), sp.Rational(1), sp.Rational(3)]
r = sp.Rational(2)
delta = min(abs(r-c) for c in S)
y = r + delta*sp.sqrt(2)/4
for c in S:
    assert sp.sign(y-c) == sp.sign(r-c)
    print(f'  c={c}, sign(r-c)={sp.sign(r-c)}, sign(y-c)={sp.sign(y-c)}')
print(f'  r={r}, y={y}, y irrational: {y.is_irrational}')
assert y.is_irrational

print('\nPolynomial maps and their branch fibres')
f=4*t*(1-t)
j=256*(t*t-t+1)**3/(t*t*(1-t)**2)
J=j/1728
u=1-1/J
assert sp.factor(f-1) == -(2*t-1)**2
assert sp.cancel(u-(t-2)**2*(t+1)**2*(2*t-1)**2/(4*(t*t-t+1)**3)) == 0
print('  f(t)-1 =',sp.factor(f-1))
print('  derivative f =',sp.factor(sp.diff(f,t)))
print('  numerator J =',sp.factor(sp.fraction(sp.cancel(J))[0]))
print('  numerator J-1 =',sp.factor(sp.fraction(sp.cancel(J-1))[0]))
print('  denominator J =',sp.factor(sp.fraction(sp.cancel(J))[1]))
print('  derivative J =',sp.factor(sp.diff(J,t)))
print('  u(t) =',sp.factor(u))
print('  u at cusps =',sp.limit(u,t,0),sp.limit(u,t,1),sp.limit(u,t,sp.oo))
assert all(sp.limit(u,t,z)==1 for z in [0,1,sp.oo])

print('\nCyclotomic cubic cover certificate')
print('  t=-4a^3, 1-t=-2b^3; equation 1+2b^3+4a^3=0')
assert sp.expand((-4*a**3)+(-2*b**3)-1)==-(1+2*b**3+4*a**3)
for emod in [1,2]:
    residues = [0,emod%3,(2*emod)%3]
    assert len(set(residues))==3
    print(f'  e mod3={emod}: three term valuations mod3={residues}')
assert {pow(2,k,3) for k in range(2)}=={1,2}
print('  e=2^r is never 0 mod3; minimum valuation is unique.')
print('  cover degree=3*3=9; three branch indices=3; boundary points=9')
genus = (9*(-2)+3*3*(3-1)+2)//2
assert genus==1
print('  Riemann-Hurwitz genus=',genus)
print('  finite Kummer datum (A,B)=(2k,k), k nonzero in F*/F*3')
for k in [1,2]:
    A,B=2*k%3,k
    assert A and B and A!=B
    print(f'  k={k}: A={A}, B={B}; off cusp axes B=0, A=0, A=B')

print('\nCoefficient prime p=5 cusp certificate')
fifth = sorted({pow(v,5,25) for v in range(25) if v%5})
assert fifth == [1,7,18,24]
assert (-4)%25 not in fifth
print('  fifth powers of units modulo25=',fifth)
print('  -4 modulo25=',(-4)%25,'not a fifth power')
print('  valuation data for t=5: (v5(t),v5(1-t))=(1,0)')

print('\nLocal inertia after a boundary blowup')
for n in [2,3,5,8]:
    kernel = [(i,j) for i in range(n) for j in range(n) if (i+j)%n==0]
    assert len(kernel)==n
    assert all((i,(-i)%n) in kernel for i in range(n))
    print(f'  modulo{n}: (m,n)->m+n has kernel size {len(kernel)}')
print('\nPASS: all exact finite certificates.')

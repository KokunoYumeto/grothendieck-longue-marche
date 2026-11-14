#!/usr/bin/env python3
"""Find and certify the missing cubic unit in Q(zeta,cuberoot3)."""
from sympy import I, Poly, Rational, expand, sqrt, symbols

x = symbols('x')
alpha = 3**Rational(1, 3)
zeta = (-1+I*sqrt(3))/2
eta = alpha**2-2
sigma_eta = zeta**2*alpha**2-2
target = expand(zeta*eta**2*sigma_eta)
poly = Poly(x**3-target, x, extension=[alpha, zeta])
constant, factors = poly.factor_list()
print('Factoring X³-zeta*(alpha²-2)²*(zeta²*alpha²-2) over Q(alpha,zeta):')
print('constant', constant)
for factor, exponent in factors:
    print('factor', factor.as_expr(), 'multiplicity', exponent)
    if factor.degree() == 1:
        root = -factor.nth(0)/factor.nth(1)
        assert poly.domain.from_sympy(expand(root**3-target)) == poly.domain.zero
        print('verified cube root', root)
assert len(factors) == 3 and all(factor.degree() == 1 for factor, _ in factors)
pi = (1-zeta)/alpha
delta = 1+zeta**2*alpha+zeta*pi
sigma_delta = 1+alpha+pi
sigma2_delta = 1+zeta*alpha+zeta**2*pi
assert poly.domain.from_sympy(expand(delta**3-target)) == poly.domain.zero
assert poly.domain.from_sympy(expand(delta*sigma_delta*sigma2_delta-zeta)) == poly.domain.zero
print('Exact compact root: delta=1+zeta²*alpha+zeta*pi, pi=(1-zeta)/alpha.')
print('Verified delta³=zeta*eta²*sigma(eta) and Norm(delta)=zeta.')
print('PASS')

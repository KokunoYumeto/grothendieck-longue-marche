#!/usr/bin/env python3
"""Exact symbolic identities for the integral negative-valuation primitive."""
from sympy import symbols, expand
a, b, x, y, u = symbols("a b x y u")
f = lambda z, c: -(z*z+c*z)/2
delta_f = x*x*f(b, y) - f(a+x*b, x*y) + f(a, x)
assert expand(delta_f - a*x*(b+(y-1)/2)) == 0
k = lambda z, c: -z*c*u
delta_k = x*x*k(b,y) - k(a+x*b,x*y) + k(a,x)
assert expand(delta_k - a*x*(y-1)*u) == 0
for z in range(-100, 101):
    for c in range(-99, 100, 2):
        assert (z*z+c*z) % 2 == 0
print("delta[-(a^2+chi*a)/2] = a cup (a+epsilon), epsilon=(chi-1)/2: PASS")
print("delta[-a*chi*u] = a cup delta(u): PASS")
print("Integral at 2: a(a+chi) is even when chi is odd; finite parity check: PASS")
print("These are polynomial identities; the global cohomological proof is separate.")

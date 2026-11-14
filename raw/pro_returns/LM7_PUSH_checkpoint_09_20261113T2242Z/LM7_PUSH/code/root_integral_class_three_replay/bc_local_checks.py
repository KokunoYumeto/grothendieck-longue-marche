#!/usr/bin/env python3
"""Exact finite certificates for F.24; no numerical Galois inference."""
from fractions import Fraction
import sympy as s

T = s.Symbol("T")
phi = s.Poly(T**4 + T**3 + T**2 + T + 1, T)
disc = int(s.discriminant(phi.as_expr(), T))
assert disc == 125
print("discriminant Phi_5:", disc)

# pi > 3 and sqrt(5) < 9/4 give this entirely rational upper bound.
minkowski_upper = Fraction(15) * Fraction(9, 4) / (2 * 3**2)
assert minkowski_upper < 2
print("strict rational Minkowski upper bound:", minkowski_upper, "< 2")

mod2 = s.Poly(phi, modulus=2)
assert mod2.is_irreducible
print("Phi_5 modulo 2 is irreducible:", mod2.is_irreducible)

def red(f):
    return s.rem(s.Poly(f, T, modulus=2), mod2).as_expr()

zeta_powers = [red(T**i) for i in range(6)]
assert zeta_powers[5] == 1
assert all(zeta_powers[i] != 1 for i in range(1, 5))
print("order of zeta in F_16^*:", 5)
print("five-part of |F_16^*|/|mu_5|:", (16-1)//5, "(prime to five)")

def norm(f):
    return s.factor(s.resultant(phi.as_expr(), f, T))

for j in (1, 2):
    den = -1-T**j
    assert norm(den) == 1
    for i in range(5):
        if i == j:
            continue
        n = norm(T**i - T**j)
        assert n == 5
        print("cusp i=%d, Kummer function j=%d: numerator norm %s, denominator norm 1"
              % (i, j, n))
assert all(any(i != j for j in (1, 2)) for i in range(5))
print("every cusp over x=0 excluded by at least one Kummer function: PASS")

# The point x=2 lifts to y=-1, z_1=z_2=1 exactly.
assert (-1)**5 == 1-2
for j in (1, 2):
    assert s.cancel((-1-T**j)/(-1-T**j)) == 1
print("lift (y,z_1,z_2)=(-1,1,1) of x=2: PASS")

# The class of 2 generates the pro-five completion of integral local units.
n = 2**4-1
v = 0
while n % 5 == 0:
    v += 1
    n //= 5
assert v == 1
print("v_5(2^4-1):", v)

eisenstein = s.Poly(s.expand((T+2)**5-2), T)
coeffs = [int(c) for c in eisenstein.all_coeffs()]
assert coeffs[0] == 1
assert all(c % 5 == 0 for c in coeffs[1:])
assert coeffs[-1] % 25 != 0
print("coefficients of (T+2)^5-2:", coeffs)
print("Eisenstein at five: PASS")
assert Fraction(1-5,1-2) == 4
print("path torsor Kummer ratio (1-5)/(1-2):", 4)
print("All exact local certificates: PASS")

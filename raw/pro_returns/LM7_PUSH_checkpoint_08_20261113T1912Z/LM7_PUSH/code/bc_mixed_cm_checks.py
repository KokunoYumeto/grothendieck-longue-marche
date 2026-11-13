#!/usr/bin/env python3
"""Exact finite certificates for F.26; no floating-point group assertions."""
from fractions import Fraction
from math import gcd
import json
import sympy as sp


def elliptic_count(p):
    return 1 + sum(
        sum((y * y - x * x * x + 2 * x) % p == 0 for y in range(p))
        for x in range(p)
    )


counts = {p: elliptic_count(p) for p in (3, 5)}
assert counts == {3: 4, 5: 10}
assert gcd(counts[3], counts[5]) == 2
assert 2**2 == 2**3 - 2 * 2
assert Fraction((2**2 + 2) ** 2, 4 * 2 * (2**2 - 2)) == Fraction(9, 4)

# Exact arithmetic in Q(sqrt(2)), represented by (a,b).
def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def inv(x):
    norm = x[0] ** 2 - 2 * x[1] ** 2
    return Fraction(x[0], norm), Fraction(-x[1], norm)


u = (-1, 1)
fplus = (2, -1)
fminus = (2, 1)
assert mul(fplus, fminus) == (2, 0)
assert mul(fplus, inv(fminus)) == mul(u, u) == (3, -2)
assert mul(u, (-1, -1)) == (-1, 0)

# The cover equation follows from Y^2 = X(X^2-2), t=X^2/2:
# (Y/2)^4 = X^2 (X^2-2)^2 / 16 = t(t-1)^2/2.
for x in range(-10, 11):
    t = Fraction(x * x, 2)
    left = Fraction(x * x * (x * x - 2) ** 2, 16)
    right = t * (t - 1) ** 2 / 2
    assert left == right
assert Fraction(2 * (2 - 1) ** 2, 2) == 1

# CM root algebra: i^2=-1, and the chosen embedding has i=2 modulo 5.
# (-2-i)+(-2+i)=-4; product=5; only -2-i is a 5-adic unit.
assert (-2 - 2) % 5 != 0 and (-2 + 2) % 5 == 0
assert (-2) ** 2 + 1 == 5

# Derive the actual [2-i] formula from the group law, in Q(i)(X,Y).
X, Y = sp.symbols("X Y")
slope_double = (3 * X**2 - 2) / (2 * Y)
X2 = slope_double**2 - 2 * X
Y2 = slope_double * (X - X2) - Y
slope_beta = (Y2 + sp.I * Y) / (X2 + X)
Xbeta = slope_beta**2 - X2 + X
Ybeta = slope_beta * (X2 - Xbeta) - Y2
Dbeta = 5 * X**2 - 2 + 4 * sp.I
Xformula = X * (3 + 4 * sp.I) * (X**2 - 2 - 4 * sp.I) ** 2 / Dbeta**2
Yformula = (
    Y * (2 + 11 * sp.I) * (X**2 - 2 - 4 * sp.I)
    * (X**4 + (4 + 16 * sp.I) * X**2 + 4) / Dbeta**3
)
curve_poly = sp.Poly(Y**2 - X**3 + 2 * X, Y, domain=sp.QQ_I.frac_field(X))
for actual, formula in ((Xbeta, Xformula), (Ybeta, Yformula)):
    num, den = sp.fraction(sp.together(actual - formula))
    reduced = sp.Poly(num, Y, domain=sp.QQ_I.frac_field(X)).rem(curve_poly)
    assert reduced.is_zero


def beta_mod25(x, y):
    modulus, i = 25, 7
    denominator = 5 * x * x - 2 + 4 * i
    xx = (
        x * (3 + 4 * i) * (x * x - 2 - 4 * i) ** 2
        * pow(denominator, -2, modulus)
    ) % modulus
    yy = (
        y * (2 + 11 * i) * (x * x - 2 - 4 * i)
        * (x**4 + (4 + 16 * i) * x * x + 4)
        * pow(denominator, -3, modulus)
    ) % modulus
    return xx, yy


preimage_lifts = [
    (x, y)
    for x in range(25)
    for y in range(25)
    if x % 5 == 2 and y % 5 == 3 and (y * y - x**3 + 2 * x) % 25 == 0
]
assert len(preimage_lifts) == 5
beta_images = [beta_mod25(x, y) for x, y in preimage_lifts]
assert set(beta_images) == {(7, 2)}
assert (2, 2) not in beta_images
for k in (1, 2, 3):
    assert (1 - 2**k) % 5 and (1 - 3**k) % 5
fixed_abelian_mod4 = [
    (a, b)
    for a in range(4)
    for b in range(4)
    if (a + 2 * b) % 4 == 0 and (a + b) % 4 == 0
]
assert fixed_abelian_mod4 == [(0, 0)]

# Character monomials chi^a epsilon^b psi^c, epsilon^2=1.
def char_mul(x, y):
    return x[0] + y[0], (x[1] + y[1]) % 2, x[2] + y[2]


def char_inv(x):
    return -x[0], x[1] % 2, -x[2]


chi = (1, 0, 0)
theta = (1, 1, 0)
psi = (0, 0, 1)
formal = (1, 0, -1)
offdiag_1 = char_mul(theta, char_mul(formal, char_inv(psi)))
offdiag_2 = char_mul(theta, char_mul(psi, char_inv(formal)))
assert offdiag_1 == (2, 1, -2)
assert offdiag_2 == (0, 1, 2)
assert theta not in {chi, psi, formal, offdiag_1, offdiag_2}


def mobius(n):
    primes = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            primes += 1
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        primes += 1
    return (-1) ** primes


def witt_rank(rank, degree):
    numerator = sum(
        mobius(d) * rank ** (degree // d)
        for d in range(1, degree + 1)
        if degree % d == 0
    )
    assert numerator % degree == 0
    return numerator // degree


witt = {d: witt_rank(5, d) for d in range(1, 7)}
assert witt[2] == 10 and witt[3] == 40

report = {
    "curve": "Y^2=X^3-2X",
    "point": [2, 2],
    "cover": "t=X^2/2; (Y/2)^4=t(t-1)^2/2",
    "point_counts": counts,
    "rational_torsion_order_bound": 2,
    "point_y_nonzero": True,
    "doubling_x": "9/4",
    "toric_ratio": "(2-sqrt(2))/(2+sqrt(2))=(sqrt(2)-1)^2",
    "unit_root": "-2-i, i=2 modulo 5",
    "beta_isogeny_group_law_identity": "both coordinates passed",
    "beta_preimage_residue_lifts_mod25": preimage_lifts,
    "beta_images_mod25": beta_images,
    "finite_quotient_order": 4 * 5**5,
    "two_C4_characters": [[1, 2], [1, 1]],
    "common_kernel_mod4": fixed_abelian_mod4,
    "johnson_characters": [chi, offdiag_1, offdiag_2],
    "separated_character": theta,
    "witt_ranks_rank_five": witt,
    "peripheral_C4_vector": [1, 2],
    "all_assertions": "passed",
}
print(json.dumps(report, indent=2))

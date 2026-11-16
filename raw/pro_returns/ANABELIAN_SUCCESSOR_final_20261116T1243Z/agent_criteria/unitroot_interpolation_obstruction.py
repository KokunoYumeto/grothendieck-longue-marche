#!/usr/bin/env python3
"""Exact number-field identities in AC.43; no interpolation is assumed."""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json


def mul(a, b):
    return (a[0]*b[0] + 13*a[1]*b[1], a[0]*b[1] + a[1]*b[0])


def norm(a):
    return a[0]*a[0] - 13*a[1]*a[1]


def is_rational_square(a):
    a = Q(a)
    return (a >= 0 and isqrt(a.numerator)**2 == a.numerator
            and isqrt(a.denominator)**2 == a.denominator)


def valuation(a, prime):
    count = 0
    while a % prime == 0:
        count += 1
        a //= prime
    return count


t = (Q(-139, 2), Q(13, 2))
d0, d1 = mul(t, t)
d = (d0-16384, d1)
assert d == (Q(-22009, 2), Q(-1807, 2))
nd = norm(d)
assert nd == 110486961 == 39**2*17*4273
assert valuation(nd.numerator, 17) == 1
assert not is_rational_square(nd)
assert not is_rational_square(nd/13)
assert d[0] + abs(d[1])*4 < 0

# Product of the two conjugate character quadratics, in descending order.
coefficients = [1, -2*t[0], norm(t)+8192, -8192*t[0], 4096**2]
assert coefficients == [1, 139, 12473, 569344, 16777216]
result = {
    "status": "exact supporting identities; the no-interpolation proof is in the LaTeX section",
    "characteristic_polynomial_descending": [int(a) for a in coefficients],
    "quadratic_discriminant": "(-22009 - 1807*sqrt(13))/2",
    "discriminant_norm": int(nd),
    "norm_factorization": "39^2 * 17 * 4273",
    "seventeen_valuation": 1,
    "norm_is_rational_square": False,
    "norm_is_thirteen_times_rational_square": False,
    "both_real_discriminants_negative": True,
    "positive_power_degree_of_alpha": "4 (proved using the unique quadratic subfield and valuations 0,12)",
    "cubic_parameter_degree": 2,
    "thirteen_parameter_degree": 3,
    "contradictory_finite_monodromy_relation": "alpha^(2N)=beta^(3N)",
    "scope": "No rank-one finite-geometric-monodromy interpolation containing both prescribed fibers; no existence of a character F-isocrystal asserted",
}
Path(__file__).with_name("unitroot_interpolation_obstruction_output.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

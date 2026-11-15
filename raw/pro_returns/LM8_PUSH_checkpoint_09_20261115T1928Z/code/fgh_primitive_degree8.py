#!/usr/bin/env python3
"""Exact arithmetic and integral-filter data for the actual degree-eight image.

The all-group Johnson filtering argument is proved in G.9.  This file checks
its finite residue input, lower special-character list, and every mod-five
choice of the two CM characters.  It does not evaluate the unknown nu value.
"""
from fractions import Fraction
from math import comb, gcd, factorial, pi, sqrt
from pathlib import Path
import json
from sympy import symbols, cyclotomic_poly, resultant


def mobius(n):
    ans, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            ans = -ans
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    return -ans if n > 1 else ans


def lie_rank(a, b):
    if min(a, b) < 0 or a + b == 0:
        return 0
    n = a + b
    ans = Fraction(0)
    for d in range(1, gcd(a, b) + 1):
        if a % d == b % d == 0:
            ans += Fraction(mobius(d) * comb(n // d, a // d), n)
    assert ans.denominator == 1
    return int(ans)


weights = {}
for m in range(1, 9):
    row = {}
    for a in range(m + 1):
        b = m - a
        rank = lie_rank(a + 1, b) + lie_rank(a, b + 1) - lie_rank(a + 1, b + 1)
        assert rank >= 0
        if rank and (a - b) % 4 == 0:
            row[f"{a},{b}"] = rank
    weights[str(m)] = row
assert weights["2"] == {"1,1": 1}
assert weights["4"] == {"2,2": 1}
assert weights["6"] == {"1,5": 1, "3,3": 2, "5,1": 1}
assert all(weights[str(m)] == {} for m in (1, 3, 5, 7))
assert weights["8"] == {"2,6": 1, "4,4": 3, "6,2": 1}

q, primitive = 101, 2
assert all(q % n for n in range(2, 11))
assert pow(primitive, 100, q) == 1
assert pow(primitive, 50, q) != 1 and pow(primitive, 20, q) != 1
i, zeta = pow(primitive, 25, q), pow(primitive, 20, q)
assert i == 10 and zeta == 95 and pow(i, 2, q) == q - 1
factors, unit = [], 1
for a in range(1, 5):
    factor = (1 - i * pow(zeta, 4 * a, q)) % q
    value = pow(factor, a**3, q)
    factors.append([a, factor, a**3, value])
    unit = unit * value % q
assert unit == 97 and pow(unit, 20, q) == 36
assert pow(zeta, 20, q) == 1

filters = []
for psi in range(1, 5):
    psibar = 2 * pow(psi, -1, 5) % 5
    roots = [
        psi * psibar % 5,
        psi**2 * psibar**2 % 5,
        psi**5 * psibar % 5,
        psi**3 * psibar**3 % 5,
        psi * psibar**5 % 5,
    ]
    eta = (psi * psibar) ** 4 % 5
    multiplier = 1
    for root in roots:
        assert root != eta
        multiplier = multiplier * (eta - root) % 5
    assert roots == [2, 4, 2, 3, 2] and multiplier == 4
    filters.append({"psi": psi, "psibar": psibar, "roots": roots,
                    "eta": eta, "multiplier": multiplier})

commutator_factor = 6**4 - 1
assert commutator_factor == 1295
assert commutator_factor % 5 == 0 and commutator_factor % 25 != 0
assert 267840 // 5 == 53568 and 53568 % 5 != 0
assert 31 * pow(4, -1, 5) % 5 == 4
elliptic_factor = -Fraction(6 * 4, 4) * Fraction(-1, 30) * Fraction(1 - 5**6, 1 - 5**3)
assert elliptic_factor == Fraction(126, 5)
actual_alpha_factor = -elliptic_factor / (12 * (1 - 5**6) * 6**2)
assert actual_alpha_factor == Fraction(1, 267840)

z = symbols("z")
principal_norm = int(resultant(cyclotomic_poly(20, z), z**3 - z + 1, z))
assert principal_norm == 5
minkowski_bound = (4 / pi)**4 * factorial(8) / 8**8 * sqrt(4_000_000)
assert 12 < minkowski_bound < 13
mu4_mod25 = {1, 7, 18, 24}
frobenius_coset_order = next(n for n in range(1, 21) if pow(9, n, 25) in mu4_mod25)
assert frobenius_coset_order == 5 and (7 * 7 + 1) % 25 == 0

out = {
    "CM_fixed_special_character_multiplicities": weights,
    "residue_certificate": {
        "prime": q, "primitive_root": primitive, "i": i, "zeta5": zeta,
        "factor_rows_a_factor_exponent_value": factors,
        "u1": unit, "u1_to_20": pow(unit, 20, q),
        "zeta5_to_20": pow(zeta, 20, q),
    },
    "lower_Johnson_filter_residues": filters,
    "commutator_factor": commutator_factor,
    "commutator_factor_divided_by_5": commutator_factor // 5,
    "arithmetic_denominator_divided_by_5": 267840 // 5,
    "elliptic_character_factor": str(elliptic_factor),
    "alpha_factor_after_removing_d_cubed": str(actual_alpha_factor),
    "rational_generation_hypothesis_certificate": {
        "cyclotomic_field_conductor": 20,
        "discriminant": 4_000_000,
        "minkowski_bound": minkowski_bound,
        "norm_zeta20_cubed_minus_zeta20_plus_1": principal_norm,
        "ray_group_mod25_order": 100,
        "inertia_order": 20,
        "conjugate_i_mod25": 7,
        "frobenius_representative": 9,
        "frobenius_coset_order_mod_mu4": frobenius_coset_order,
    },
    "conclusions_from_the_proved_filter_lemma": {
        "chi4_on_Delta": "5 Z_5",
        "chi4_on_Delta_intersect_J8": "5 Z_5",
        "alpha_image": "Z_5",
        "lambda_minus_31_over_20": "belongs to Z_5; value unknown",
        "v5_lambda": -1,
        "5_lambda_mod_5": 4,
        "index_in_saturated_arithmetic_line": 1,
    },
    "not_computed": ["nu on an actual normalized Galois element",
                     "the actual scalar lambda"],
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))

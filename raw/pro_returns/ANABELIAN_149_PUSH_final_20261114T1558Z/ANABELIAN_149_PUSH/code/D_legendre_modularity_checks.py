#!/usr/bin/env python3
"""Finite certificates for the separately stated cuspidal warning in D.30.

The program checks exact leading-coefficient, CRT and tame matrix identities.
It does not test finite ramification or construct a noncuspidal section.
"""
from fractions import Fraction
from pathlib import Path
import json


def multiply(a, b, modulus):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) % modulus
             for j in range(2)] for i in range(2)]


def power(a, n, modulus):
    out = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            out = multiply(out, a, modulus)
        a = multiply(a, a, modulus)
        n >>= 1
    return out


def inverse(a, modulus):
    det = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % modulus
    dinv = pow(det, -1, modulus)
    return [[a[1][1] * dinv % modulus, -a[0][1] * dinv % modulus],
            [-a[1][0] * dinv % modulus, a[0][0] * dinv % modulus]]


# j(t)^(-1)=t^2(1-t)^2/[256(1-t+t^2)^3].
# Its denominator has constant coefficient 256 and its numerator starts t^2.
leading_order = 2
leading_coefficient = Fraction(1, 256)
assert leading_coefficient.denominator % 13 != 0
assert (5 * 5 + 1) % 13 == 0 and (2 * 5) % 13 != 0

crt_rows = []
previous_e = None
previous_modulus = None
for level in range(1, 7):
    m5, m7 = 5 ** level, 7 ** level
    e = (m7 * pow(m7, -1, m5)) % (m5 * m7)
    assert e % m5 == 1 and e % m7 == 0
    if previous_e is not None:
        assert e % previous_modulus == previous_e
    crt_rows.append({"level": level, "modulus": m5 * m7,
                     "e": e, "five_component": e % m5,
                     "seven_component": e % m7})
    previous_e, previous_modulus = e, m5 * m7

matrix_rows = []
for ell, n_coefficient in [(5, 2), (7, 0)]:
    modulus = ell ** 2
    frobenius = [[13 % modulus, 0], [0, 1]]
    inertia = [[1, n_coefficient], [0, 1]]
    conjugate = multiply(multiply(frobenius, inertia, modulus),
                         inverse(frobenius, modulus), modulus)
    assert conjugate == power(inertia, 13, modulus)
    rank_mod_ell = int(n_coefficient % ell != 0)
    matrix_rows.append({
        "coefficient_prime": ell, "modulus": modulus,
        "frobenius": frobenius, "inertia": inertia,
        "tame_relation_holds": True, "monodromy_rank": rank_mod_ell,
        "semisimple_characteristic_polynomial_over_Z": [1, -14, 13]
    })
assert [row["monodromy_rank"] for row in matrix_rows] == [1, 0]

out = {
    "status": "PASS",
    "scope": "Exact finite checks for the cuspidal monodromy warning only; "
             "no assertion of a noncuspidal counterexample or a test of modularity.",
    "j_inverse_leading_order": leading_order,
    "j_inverse_leading_coefficient": str(leading_coefficient),
    "sqrt_minus_one_mod_13": 5,
    "crt_compatibility": crt_rows,
    "local_matrix_checks": matrix_rows
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"status": out["status"],
                  "crt_levels": len(crt_rows),
                  "monodromy_ranks": [x["monodromy_rank"] for x in matrix_rows],
                  "frobenius_polynomial": [1, -14, 13]}, indent=2))

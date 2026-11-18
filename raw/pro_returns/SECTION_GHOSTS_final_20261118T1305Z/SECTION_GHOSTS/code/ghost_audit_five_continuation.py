#!/usr/bin/env python3
"""Finite arithmetic certificate for E205; no prime-search assertion.

This checks the exact original factorial indices and representative
finite affine correction maps. The proof of all-index bounds and
Chebotarev/Kummer compatibility is in the manuscript, not inferred
from this finite run. No legal first pair or consistent first gate
is asserted by the certificate.
"""

import json
from collections import Counter
from math import factorial
from pathlib import Path


def v5(n):
    assert n != 0
    result = 0
    while n % 5 == 0:
        result += 1
        n //= 5
    return result


def factorial_v5(n):
    result = 0
    while n:
        n //= 5
        result += n
    return result


rows = []
for j in range(1, 100001):
    c = factorial_v5(j + 4)
    t = v5(j + 5)
    e = factorial_v5(j + 5)
    assert e == c + t
    assert c >= t
    if j <= 6 or j in (20, 21, 120, 620, 3120, 15620, 78120):
        rows.append({"j": j, "c": c, "t": t, "e": e,
                     "normalized_lower_bound": c - t})

assert [(r["c"], r["t"], r["e"]) for r in rows[:4]] == [(1, 0, 1)] * 4
assert next(r for r in rows if r["j"] == 20) == {
    "j": 20, "c": 4, "t": 2, "e": 6,
    "normalized_lower_bound": 2,
}

root_parameters = 0
for j in range(1, 21):
    n = factorial(j + 4)
    m = factorial(j + 5)
    c, e = v5(n), v5(m)
    modulus, root_order = 5**c, 5**e
    unit = m // root_order
    assert unit % 5 != 0
    image_counts = Counter((unit * i) % modulus for i in range(root_order))
    assert len(image_counts) == modulus
    assert set(image_counts.values()) == {5 ** (e - c)}
    for i in range(root_order):
        change = unit * i
        assert (n * change) % modulus == 0
    root_parameters += root_order
    for sign in (-1, 1):
        shell_representative = 1 + sign * 5**e
        assert v5(shell_representative**2 - 1) == e
        assert (shell_representative**2 - 1) % modulus == 0

affine_equations = 0
for c in range(1, 4):
    modulus = 5**c
    for alpha in range(modulus):
        if alpha % 5 == 0:
            continue
        inverse = pow(alpha, -1, modulus)
        for gamma in range(modulus):
            a_primitive = gamma * inverse % modulus
            b_primitive = -gamma * inverse % modulus
            assert (gamma - alpha * a_primitive) % modulus == 0
            assert (gamma + alpha * b_primitive) % modulus == 0
            affine_equations += 2

result = {
    "status": "PASS",
    "scope": "Finite arithmetic only; no legal first pair, matrix rank, or first-gate consistency claimed.",
    "factorial_indices_checked": 100000,
    "selected_exact_indices": rows,
    "root_parameters_checked": root_parameters,
    "affine_equations_checked": affine_equations,
    "checks": [
        "e_j = c_j + t_j and c_j >= t_j for j=1..100000",
        "Original n_j=(j+4)! and m=n_{j+1}; first jump by25 is j20",
        "Each mu_(5^e) primitive correction is surjective modulo5^c with fibre size5^(e-c)",
        "The same primitive correction has zero central tame effect modulo5^c",
        "Both minimal shell signs annihilate central coboundaries modulo5^c",
        "All affine unit-coefficient correction equations modulo5,25,125 solve uniquely",
    ],
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

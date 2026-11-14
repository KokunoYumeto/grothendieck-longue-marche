"""Finite exact certificates for the infinite-residue valuation construction.

The infinitude and transcendence arguments are proved in the paper. This
program checks the norm-polynomial and leading-coefficient identities for
the first four stages, using exact multiquadratic arithmetic throughout.
No floating point arithmetic or pre-existing archived program is used.
"""
from collections import defaultdict
from itertools import product
import json
from pathlib import Path

PRIMES = (2, 3, 5, 7, 11)


def radical_product(a, b):
    coefficient = 1
    overlap = a & b
    for i, p in enumerate(PRIMES):
        if overlap & (1 << i):
            coefficient *= p
    return a ^ b, coefficient


def multiply(left, right):
    # Keys are (X-degree, Y-degree, radical-mask).
    out = defaultdict(int)
    for (x, y, a), c in left.items():
        for (u, v, b), d in right.items():
            mask, scalar = radical_product(a, b)
            out[(x + u, y + v, mask)] += c * d * scalar
    return {key: value for key, value in out.items() if value}


def add_term(poly, key, coefficient):
    poly[key] = poly.get(key, 0) + coefficient
    if poly[key] == 0:
        del poly[key]


def norm_polynomial(m):
    result = {(0, 0, 0): 1}
    for signs in product((-1, 1), repeat=m):
        factor = {(0, 1, 0): 1}
        for i, sign in enumerate(signs):
            factor[(i + 1, 0, 1 << i)] = -sign
        result = multiply(result, factor)
    assert all(mask == 0 for _, _, mask in result)
    assert result.get((0, 2**m, 0)) == 1
    return result


def substituted_product(m):
    # y = sum_{i=1}^{m+1} sqrt(p_i) X^i. Later terms cannot
    # change the leading coefficient being tested.
    result = {(0, 0, 0): 1}
    for signs in product((-1, 1), repeat=m):
        factor = {}
        for i in range(m + 1):
            coefficient = 1 - signs[i] if i < m else 1
            if coefficient:
                add_term(factor, (i + 1, 0, 1 << i), coefficient)
        result = multiply(result, factor)
    degree = min(x for x, _, _ in result)
    leading = {mask: c for (x, _, mask), c in result.items()
               if x == degree}
    expected_scalar = 2**(2**m - 1)
    for i in range(m - 1):
        expected_scalar *= PRIMES[i]**(2**(m - i - 2))
    expected_mask = (1 << (m - 1)) | (1 << m)
    assert degree == 2**(m + 1) - 1
    assert leading == {expected_mask: expected_scalar}
    return degree, leading


rows = []
for m in range(1, 5):
    poly = norm_polynomial(m)
    degree, leading = substituted_product(m)
    rows.append({
        "m": m,
        "norm_degree_Y": 2**m,
        "norm_coefficients_rational": True,
        "norm_nonzero_terms": len(poly),
        "valuation": degree,
        "leading_coefficient": {
            "rational_factor": list(leading.values())[0],
            "radicands": [PRIMES[m - 1], PRIMES[m]],
        },
    })
output = {
    "status": "all exact checks passed",
    "scope": "four finite stages; the proof of infinite algebraic residue is in F.26",
    "rows": rows,
}
path = Path(__file__).with_name("infinite_residue_checks_output.json")
path.write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))

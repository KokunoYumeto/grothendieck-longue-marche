#!/usr/bin/env python3
"""Exact finite tests for E_a:y^2+xy=x^3+a at primitive 3-power parameters.

The tests do not assert an asymptotic pattern.  In particular, the trace-one
pattern at orders 3 and 9 fails at order 27.  The complete halving chains
certify the two-primary exponents without enumerating the full fields.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "code"))
from big_binary_field import BigBinaryField


DATA = [
    (1, 7, 2),
    (2, 67, 6),
    (3, 262153, 66562),
    (4, 18014398509482497, 8813306445824),
    (5, 5846006549323611672814739330865132078623864389633,
     2854495385411919920572896967427674255946481664),
]


def double(field, point):
    if point is None or point[0] == 0:
        return None
    x, y = point
    slope = x ^ field.div(y, x)
    xx = field.sq(slope) ^ slope
    yy = field.sq(x) ^ field.mul(slope ^ 1, xx)
    return xx, yy


rows = []
for n, modulus, parameter in DATA:
    degree = 2 * 3 ** (n - 1)
    field = BigBinaryField(modulus)
    assert field.m == degree
    assert field.power(parameter, 3 ** n) == 1
    assert field.power(parameter, 3 ** (n - 1)) != 1
    assert field.frob(parameter, degree // 2) != parameter
    if n > 1:
        assert field.frob(parameter, degree // 3) != parameter

    point = (0, field.sqrt(parameter))
    chain = [point]
    assert double(field, point) is None
    while True:
        slope = field.as_root(point[0])
        if slope is None:
            break
        u = field.sqrt(point[1] ^ field.mul(slope ^ 1, point[0]))
        v = field.mul(u, slope ^ u)
        half = (u, v)
        assert field.sq(v) ^ field.mul(u, v) == field.mul(field.sq(u), u) ^ parameter
        assert double(field, half) == point
        chain.append(half)
        point = half
    assert field.trace(point[0]) == 1
    exponent_valuation = len(chain)
    rows.append({
        "n": n,
        "parameter_order": 3 ** n,
        "degree_over_F2": degree,
        "degree_over_F4": degree // 2,
        "field_modulus": str(modulus),
        "parameter": str(parameter),
        "v2_two_primary_exponent": exponent_valuation,
        "two_primary_group": "Z/2^" + str(exponent_valuation),
        "halving_chain_starting_at_order_two": [[str(x), str(y)] for x, y in chain],
        "terminal_x_absolute_trace": 1,
        "all_curve_and_doubling_checks_passed": True,
    })

assert [row["v2_two_primary_exponent"] for row in rows] == [2, 6, 8, 14, 14]
result = {
    "status": "exact finite tests; no asymptotic assertion",
    "family": "E_a: y^2+xy=x^3+a",
    "fixed_parameter_prime": 3,
    "field_engine": "../code/big_binary_field.py with its exact C++ helper",
    "halving_formula": "lambda^2+lambda=x_R; u^2=y_R+(lambda+1)x_R; v=u(lambda+u)",
    "scope": "The order27 test refutes the trace-one pattern; this is not the Abel tower of AR20",
    "rows": rows,
}
(HERE / "primitive_three_unitroot_halving_output.json").write_text(
    json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"],
                  "valuations": [row["v2_two_primary_exponent"] for row in rows]}, indent=2))

#!/usr/bin/env python3
"""Exact tiny-field certificate for the example in AC.45.

No external packages.  GF(4) = GF(2)[a]/(a^2+a+1), integers 0..3.
The affine Artin--Schreier model has simple poles at 0,1,infinity.
"""
import json


def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return z


def inv(a):
    assert a != 0
    return next(b for b in range(1, 4) if mul(a, b) == 1)


def count(field):
    finite = []
    trace = {}
    for x in field:
        if x in (0, 1):
            continue
        rhs = x ^ inv(x) ^ inv(x ^ 1)
        trace[str(x)] = rhs ^ mul(rhs, rhs)
        for y in field:
            if mul(y, y) ^ y == rhs:
                finite.append([x, y])
    return {
        "finite_nonpole_points": finite,
        "three_rational_ramification_points": ["0", "1", "infinity"],
        "nonpole_rhs_absolute_trace_in_F4": trace,
        "total": 3 + len(finite),
    }


f2 = count([0, 1])
f4 = count([0, 1, 2, 3])
q = 2
s1 = q + 1 - f2["total"]
s2 = q * q + 1 - f4["total"]
assert (s1 * s1 - s2) % 2 == 0
a1 = -s1
a2 = (s1 * s1 - s2) // 2
poly = [1, a1, a2, q * a1, q * q]
assert f2["total"] == f4["total"] == 3
assert poly == [1, 0, -1, 0, 4]
assert sum(poly) == 4
result = {
    "curve": "y^2+y=x+1/x+1/(x+1) over F2",
    "GF4_modulus": "a^2+a+1",
    "simple_pole_orders": [1, 1, 1],
    "genus": (sum(1 + 1 for _ in range(3)) - 2) // 2,
    "two_rank_by_Deuring_Shafarevich": 3 - 1,
    "F2": f2,
    "F4": f4,
    "zeta_numerator_coefficients_low_to_high": poly,
    "Jacobian_F2_order": sum(poly),
    "all_assertions_passed": True,
}
print(json.dumps(result, indent=2, sort_keys=True))

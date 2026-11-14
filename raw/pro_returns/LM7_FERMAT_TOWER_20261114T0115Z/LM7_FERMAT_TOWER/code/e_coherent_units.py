#!/usr/bin/env python3
"""E.69 exact residue certificate; it does not calculate universal norm indices."""
from itertools import product
from pathlib import Path
import json


def mul(a, b):
    return ((a[0] * b[0] - a[1] * b[1]) % 17,
            (a[0] * b[1] + a[1] * b[0] - a[1] * b[1]) % 17)


def power(a, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


one, zeta, lam, c = (1, 0), (0, 1), (1, 16), (1, 3)


def zmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0] - a[1] * b[1])


# Literal characteristic-zero norm in K(beta1), beta1^3=17*zeta.
c_constant_cube = zmul(zmul((1, 3), (1, 3)), (1, 3))
first_norm = (c_constant_cube[0], c_constant_cube[1] + 17)
assert first_norm == (1, -1)
second_total_norm = zmul(zmul(first_norm, first_norm), first_norm)
assert second_total_norm == (-3, -6)
assert power(zeta, 3) == one and zeta != one
assert power(lam, 32) == zeta
assert power(lam, 64) == power(zeta, 2)
assert power(c, 3) == lam
all_units = [u for u in product(range(17), repeat=2) if u != (0, 0)]
mu9 = {power(u, 64) for u in all_units}
assert len(mu9) == 9
assert all(power(u, 9) == one for u in mu9)
image9 = {power(u, 9) for u in all_units}
assert len(image9) == 32
assert image9.intersection({one, zeta, power(zeta, 2)}) == {one}
lambda_tests = []
for a in range(27):
    residue = power(power(lam, a), 64)
    assert (residue == one) == (a % 3 == 0)
    lambda_tests.append({"exponent_mod27": a,
                         "three_primary_residue": list(residue)})

out = {
    "status": "PASS",
    "residue_field_size": 289,
    "nonzero_elements_checked": len(all_units),
    "three_primary_unit_order": len(mu9),
    "depth_two_unit_norm_image_order": len(image9),
    "mu3_intersection_with_depth_two_image": 1,
    "lambda_power32": list(power(lam, 32)),
    "lambda_three_primary_residue": list(power(lam, 64)),
    "c_first_residue_norm": list(power(c, 3)),
    "c_exact_first_norm": list(first_norm),
    "included_c_exact_total_norm_from_L2": list(second_total_norm),
    "exact_finite_projection_index_at_L2": 9,
    "finite_projection_exponents_a1_a2": [0, 1],
    "lambda_exponent_checks": len(lambda_tests),
    "universal_norm_index_h": "finite and at least1 by proof; not numerically evaluated",
    "lambda_tests": lambda_tests,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))

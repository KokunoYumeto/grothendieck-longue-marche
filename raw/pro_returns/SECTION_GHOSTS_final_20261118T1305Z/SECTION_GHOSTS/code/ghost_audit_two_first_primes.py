#!/usr/bin/env python3
"""Finite algebra certificate for E.213.

This checks the common-diagonal argument and the finite radical-group
calculation. It does not construct rational primes satisfying the very
large original CRT conditions. Their existence uses the field proof.
"""

from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json


P = 5
matrix_checks = 0
for a1, a2, d, chi in product(range(1, P), range(1, P),
                            range(P), range(1, P)):
    # Before conjugation the two products are a1 and 2*a2.
    x1 = x2 = pow(chi, 2, P)
    y1 = pow(chi, 3, P) * a1 % P
    y2 = pow(chi, 3, P) * 2 * a2 % P
    ratio1 = x1 * y1 * pow(a1, -1, P) % P
    ratio2 = x2 * y2 * pow(a2, -1, P) % P
    assert ratio1 == chi
    assert ratio2 == 2 * chi % P
    assert ratio1 != ratio2
    det1 = (a1 * d - x1 * y1) % P
    det2 = (a2 * d - x2 * y2) % P
    assert det1 or det2
    matrix_checks += 1

zero_diagonal_checks = 0
for d, chi in product(range(P), range(1, P)):
    assert (-pow(chi, 2, P) * pow(chi, 3, P)) % P
    zero_diagonal_checks += 1

# Generator chi=2 acts as 4 on weight two and 3 on weight three.
# A map to the weight-one character (eigenvalue 2) must be zero.
source_eigenvalues = (4, 4, 3, 3)
intertwiners = []
for row in product(range(P), repeat=4):
    if all((a * ev - 2 * a) % P == 0
           for a, ev in zip(row, source_eigenvalues)):
        intertwiners.append(row)
assert intertwiners == [(0, 0, 0, 0)]

# An explicit automorphism model of the joint radical splitting field.
# chi acts on mu_120; u=3^(1/24) maps to zeta_24^b*u.
# Its parity records the actual cyclotomic action on sqrt(3)=u^12.
# The c_i are the two independent fifth-root translations.
units = tuple(a for a in range(120) if gcd(a, 120) == 1)


def sqrt_three_sign(chi):
    return 1 if chi % 12 in (1, 11) else -1


def valid(g):
    chi, b, c1, c2 = g
    return (chi in units and 0 <= b < 24 and 0 <= c1 < 5
            and 0 <= c2 < 5
            and (-1 if b % 2 else 1) == sqrt_three_sign(chi))


def mul(g, h):
    chi, b, c1, c2 = g
    psi, d, e1, e2 = h
    return (chi * psi % 120, (b + chi * d) % 24,
            (c1 + chi * e1) % 5, (c2 + chi * e2) % 5)


def inv(g):
    chi, b, c1, c2 = g
    u = pow(chi, -1, 120)
    return (u, -u * b % 24, -u * c1 % 5, -u * c2 % 5)


def comm(g, h):
    return mul(mul(mul(g, h), inv(g)), inv(h))


identity = (1, 0, 0, 0)
group = {(chi, b, c1, c2)
         for chi, b, c1, c2 in product(units, range(24),
                                     range(5), range(5))
         if valid((chi, b, c1, c2))}
assert len(group) == 9600
kernel = {g for g in group if g[0] == 1}
assert len(kernel) == 300
twice_kernel = {mul(g, g) for g in kernel}
assert len(twice_kernel) == 150
assert twice_kernel == {g for g in kernel if g[1] % 4 == 0}

conjugation = (119, 0, 0, 0)
sqrt_three_flipper = (7, 1, 0, 0)
t1, t2 = (1, 0, 1, 0), (1, 0, 0, 1)
generators = [conjugation, sqrt_three_flipper,
              (1, 2, 0, 0), t1, t2]
operation_checks = 0
for g in group:
    assert valid(inv(g))
    assert mul(g, inv(g)) == identity
    for h in generators:
        assert mul(g, h) in group
        assert mul(h, g) in group
        operation_checks += 2

derived_generators = [comm(conjugation, h)
                      for h in (sqrt_three_flipper, t1, t2)]
assert derived_generators == [(1, 22, 0, 0),
                              (1, 0, 3, 0), (1, 0, 0, 3)]
derived = {identity}
frontier = [identity]
while frontier:
    g = frontier.pop()
    for h in derived_generators:
        new = mul(g, h)
        if new not in derived:
            derived.add(new)
            frontier.append(new)
assert derived == kernel

payload = {
    "statement": "E.213",
    "status": "PASS",
    "nonzero_diagonal_matrix_cases": matrix_checks,
    "zero_diagonal_cases": zero_diagonal_checks,
    "character_rows_checked": 5 ** 4,
    "weight_one_intertwiners": intertwiners,
    "joint_radical_group_order": len(group),
    "radical_kernel_order": len(kernel),
    "twice_kernel_order": len(twice_kernel),
    "derived_generators": derived_generators,
    "derived_subgroup_order": len(derived),
    "group_operation_checks": operation_checks,
    "scope": (
        "Finite algebra only. No numerical legal original prime, "
        "prime distribution, or all-depth section is certified."
    ),
}
encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["payload_sha256"] = sha256(encoded.encode()).hexdigest()
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps(payload, indent=2))

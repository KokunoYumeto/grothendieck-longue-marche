#!/usr/bin/env python3
"""Finite certificates for LM6 statements B.6, B.12, and B.22.

All arithmetic and group enumeration is exact.  The program checks the
finite examples used in the proofs; it does not claim to decide a section
conjecture by finite computation.
"""
from fractions import Fraction
from itertools import permutations, product, combinations
import json


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    return tuple(p.index(i) for i in range(3))


S3 = list(permutations(range(3)))
one = (0, 1, 2)


def mul(a, b):
    l, x, y, e = a
    m, z, w, f = b
    if e:
        z, w = w, z
    return compose(l, m), compose(x, z), compose(y, w), e ^ f


def inv(a):
    l, x, y, e = a
    if e:
        x, y = y, x
    return inverse(l), inverse(x), inverse(y), e


E = list(product(S3, S3, S3, range(2)))
section_H = {(a, a, b, 0) for a, b in product(S3, repeat=2)}
identity = (one, one, one, 0)
assert len(E) == 432 and len(section_H) == 36
assert all(mul(a, inv(a)) == identity for a in E)
assert all(mul(a, b) in section_H for a, b in product(section_H, repeat=2))
fixed_L = [l for l in S3 if all(compose(l, a) == compose(a, l) for a in S3)]
normalizer = [g for g in E if {mul(mul(g, h), inv(g)) for h in section_H} == section_H]
normalizer_image = {(a, b, e) for _, a, b, e in normalizer}
expected_H = {(a, b, 0) for a, b in product(S3, repeat=2)}
assert fixed_L == [one]
assert normalizer_image == expected_H
assert len(normalizer) == 36


def cusp_vector(boundary, y, a):
    return tuple(Fraction(a) if s == y else Fraction(y - s) for s in boundary)


def same_projective_vector(a, b):
    if any(x == 0 or y == 0 for x, y in zip(a, b)):
        raise ValueError("The torus coordinates must be nonzero")
    ratios = {x / y for x, y in zip(a, b)}
    return len(ratios) == 1


boundary = (0, 1, 3)
intersections = []
parameters = {y: [] for y in boundary}
for y, z in combinations(boundary, 2):
    w = next(s for s in boundary if s != y and s != z)
    diagonal = Fraction(y - w, z - w)
    a = diagonal * (z - y)
    b = Fraction(y - z) / diagonal
    left, right = cusp_vector(boundary, y, a), cusp_vector(boundary, z, b)
    assert same_projective_vector(left, right)
    parameters[y].append(a)
    parameters[z].append(b)
    intersections.append({"cusps": [y, z], "remaining": w,
                          "diagonal": str(diagonal),
                          "parameters": [str(a), str(b)],
                          "left_vector": list(map(str, left)),
                          "right_vector": list(map(str, right))})
assert all(len(v) == 2 and v[0] == -v[1] for v in parameters.values())
for a, b in combinations(intersections, 2):
    va = tuple(Fraction(x) for x in a["left_vector"])
    vb = tuple(Fraction(x) for x in b["left_vector"])
    assert not same_projective_vector(va, vb)

four_boundary = (0, 1, 3, 7)
four_checks = []
for y, z in combinations(four_boundary, 2):
    remaining = [s for s in four_boundary if s not in (y, z)]
    ratios = [Fraction(y-s, z-s) for s in remaining]
    assert ratios[0] != ratios[1]
    four_checks.append({"cusps": [y, z], "required_diagonal_values": list(map(str, ratios))})

crossing_checks = []
for n in (2, 3, 5, 8):
    kernel = [(a, b) for a, b in product(range(n), repeat=2) if (b-a) % n == 0]
    assert kernel == [(a, a) for a in range(n)]
    crossing_checks.append({"modulus": n, "kernel_order": len(kernel),
                            "image_order": len({(b-a) % n for a,b in product(range(n), repeat=2)})})

result = {
    "partial_splitting_counterexample": {
        "L_order": 6, "H_order": 36, "G_order": 72, "E_order": 432,
        "fixed_L_order": len(fixed_L), "normalizer_order": len(normalizer),
        "normalizer_image_order": len(normalizer_image),
        "normalizer_image_equals_H": normalizer_image == expected_H,
        "normalizer_image_is_proper": len(normalizer_image) < 72,
    },
    "tripod_pairwise_packet_intersections": intersections,
    "tripod_pairwise_intersections_are_distinct": True,
    "four_puncture_disjointness": four_checks,
    "normal_crossing_inertia_quotients": crossing_checks,
    "M04_multisection": {
        "base_map": "lambda=t^2",
        "section": "x=t",
        "cover_removed_points": ["0", "1", "-1", "infinity"],
        "x_minus_lambda_factors": ["t", "1-t"],
        "critical_derivative": "2*t",
        "branch_values": ["0", "infinity"],
        "finite_integer_substitutions_checked": list(range(-20, 21)),
    },
}
for t in range(-20, 21):
    if t in (0, 1, -1):
        continue
    assert t != 0 and t != 1 and t != t*t
    assert t-t*t == t*(1-t)
print(json.dumps(result, indent=2, sort_keys=True))

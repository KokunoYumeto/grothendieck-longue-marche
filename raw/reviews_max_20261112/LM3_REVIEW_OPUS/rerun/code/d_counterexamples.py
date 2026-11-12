#!/usr/bin/env python3
"""Finite checks for D.2 and D.20; the accompanying text proves the profinite claims.
No network access or nonstandard packages are required.
"""
from itertools import permutations, product
import json
from pathlib import Path


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def inverse(a):
    return tuple(a.index(i) for i in range(len(a)))


def generated(gens, degree):
    identity = tuple(range(degree))
    out = {identity}
    frontier = [identity]
    steps = set(gens) | {inverse(g) for g in gens}
    while frontier:
        a = frontier.pop()
        for b in steps:
            c = compose(a, b)
            if c not in out:
                out.add(c)
                frontier.append(c)
    return out


def commutator(a, b):
    return compose(compose(compose(a, b), inverse(a)), inverse(b))


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a))) % 2


def matrix_mul(a, b, modulus):
    return ((a[0]*b[0]+a[1]*b[2]) % modulus,
            (a[0]*b[1]+a[1]*b[3]) % modulus,
            (a[2]*b[0]+a[3]*b[2]) % modulus,
            (a[2]*b[1]+a[3]*b[3]) % modulus)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Quotient of the actual geometric free profinite group used in D.2.
a5 = {a for a in permutations(range(5)) if parity(a) == 0}
gens5 = ((1, 2, 3, 4, 0), (1, 2, 0, 3, 4))  # (12345), (123)
a5_generated = generated(gens5, 5)
a5_derived = generated({commutator(a, b) for a in a5 for b in a5}, 5)
assert a5_generated == a5 and a5_derived == a5

# Elementary finite model of normal geometric kernel with surjective normalizer.
ambient = set(range(8))       # (C2)^3 with XOR operation
geometric = set(range(4))     # (C2)^2 x {0}
normalizer = {a for a in ambient if {a ^ x ^ a for x in geometric} == geometric}
projection = {a >> 2 for a in normalizer}
assert normalizer == ambient and projection == {0, 1}
assert all(x ^ x == 0 for x in geometric) and len(geometric) == 4

s3 = set(permutations(range(3)))
s3_derived = generated({commutator(a, b) for a in s3 for b in s3}, 3)
assert len(s3_derived) == 3
cubic_discriminant = -27 * (-2)**2
assert cubic_discriminant == -108

matrix_checks = []
for modulus in (2, 3, 4, 5, 8, 9):
    J = (0, (-1) % modulus, 1, 0)
    centralizer = [A for A in product(range(modulus), repeat=4)
                   if gcd(A[0]*A[3]-A[1]*A[2], modulus) == 1
                   and matrix_mul(A, J, modulus) == matrix_mul(J, A, modulus)]
    expected = {(a, (-b) % modulus, b, a)
                for a, b in product(range(modulus), repeat=2)
                if gcd(a*a+b*b, modulus) == 1}
    assert set(centralizer) == expected
    abelian = all(matrix_mul(A, B, modulus) == matrix_mul(B, A, modulus)
                  for A in centralizer for B in centralizer)
    assert abelian
    matrix_checks.append({"modulus": modulus, "centralizer_order": len(centralizer),
                          "abelian": abelian})

report = {
    "D.2": {"A5_order": len(a5), "generated_by_12345_and_123": len(a5_generated),
            "A5_derived_order": len(a5_derived),
            "finite_normalizer_model": {"ambient_order": len(ambient),
                                        "geometric_order": len(geometric),
                                        "normalizer_order": len(normalizer),
                                        "normalizer_projection": sorted(projection),
                                        "geometric_cyclic": False}},
    "D.20": {"x3_minus_2_discriminant": cubic_discriminant,
             "S3_derived_order": len(s3_derived),
             "CM_matrix_centralizers": matrix_checks},
    "scope": "Finite checks only. Profinite and arithmetic conclusions are proved in D.tex."
}
path = Path(__file__).with_name("d_counterexamples_output.json")
path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, indent=2))

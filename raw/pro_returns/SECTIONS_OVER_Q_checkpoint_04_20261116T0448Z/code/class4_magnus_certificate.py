#!/usr/bin/env python3
"""Exact truncated Magnus arithmetic for the integral fourth-layer argument.

All coefficients are integers. No Galois-action coefficients are simulated:
the manuscript proves that every actual integral substitution preserves
the displayed two-sided coefficient ideals.
"""
from pathlib import Path
from math import comb
import json

DEGREE = 4
ONE = {"": 1}


def add(a, b):
    out = dict(a)
    for word, coefficient in b.items():
        out[word] = out.get(word, 0) + coefficient
    return {word: c for word, c in out.items() if c}


def scale(a, c):
    return {word: coefficient * c for word, coefficient in a.items()
            if coefficient * c}


def multiply(a, b):
    out = {}
    for left, c in a.items():
        for right, d in b.items():
            word = left + right
            if len(word) <= DEGREE:
                out[word] = out.get(word, 0) + c * d
    return {word: c for word, c in out.items() if c}


def inverse(a):
    assert a.get("") == 1
    difference = add(a, scale(ONE, -1))
    out, term = dict(ONE), dict(ONE)
    for degree in range(1, DEGREE + 1):
        term = multiply(term, difference)
        out = add(out, scale(term, (-1)**degree))
    assert multiply(a, out) == ONE == multiply(out, a)
    return out


def power(a, n):
    if n < 0:
        return power(inverse(a), -n)
    out = dict(ONE)
    while n:
        if n & 1:
            out = multiply(out, a)
        a = multiply(a, a)
        n //= 2
    return out


def commutator(a, b):
    # [a,b] = a b a^{-1} b^{-1}; matches C,D,F in A.43.
    return multiply(multiply(multiply(a, b), inverse(a)), inverse(b))


def homogeneous(a, degree):
    return {word: c for word, c in a.items() if len(word) == degree}


x, y = {"": 1, "X": 1}, {"": 1, "Y": 1}
C = commutator(x, y)
D, F = commutator(C, x), commutator(C, y)
P, Q, R = commutator(D, x), commutator(D, y), commutator(F, y)
assert Q == commutator(F, x)
third = [[homogeneous(g, 3).get(word, 0) for g in (D, F)]
         for word in ("XXY", "XYY")]
fourth = [[homogeneous(g, 4).get(word, 0) for g in (P, Q, R)]
          for word in ("XXXY", "XXYY", "XYYY")]
assert third == [[-1, 0], [0, 1]]
assert fourth == [[1, 0, 0], [0, -1, 0], [0, 0, 1]]

# Verify central extraction, including negative Hall exponents.
central_cases = 0
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-3, 4):
            g = multiply(multiply(power(P, a), power(Q, b)), power(R, c))
            assert g.get("XXXY", 0) == a
            assert g.get("XXYY", 0) == -b
            assert g.get("XYYY", 0) == c
            assert all(len(word) == 4 for word in g if word)
            central_cases += 1

# These finite checks supplement the manuscript's integer-valued
# polynomial proof of the ideal bounds; they do not replace that proof.
ideal_cases = 0
for e in (24, 48, 72, 120, 240, 720):
    for sign in (-1, 1):
        for multiplier in (0, 1, 2, 3):
            m = sign * e * multiplier
            for n in (0, m):
                for k in (-3, -1, 0, 1, 4):
                    t = (e // 2) * k
                    v0 = multiply(multiply(power(y, n), power(x, m)), power(C, t))
                    assert all(c % (e // 6) == 0 for word, c in v0.items()
                               if 1 <= len(word) <= 3)
                    assert all(c % (e // 12) == 0 for word, c in v0.items()
                               if word)
                    ideal_cases += 1

result = {
    "commutator_convention": "[a,b]=a b a^{-1} b^{-1}",
    "third_layer_words": ["XXY", "XYY"],
    "third_layer_matrix": third,
    "fourth_layer_words": ["XXXY", "XXYY", "XYYY"],
    "fourth_layer_matrix": fourth,
    "hall_jacobi_identity_Q_equals_F_x": True,
    "central_coordinate_extractions": central_cases,
    "integer_ideal_cases": ideal_cases,
    "fourth_layer_homogeneous_expansions": {
        name: homogeneous(g, 4) for name, g in (("P", P), ("Q", Q), ("R", R))
    },
    "status": "All exact integer assertions passed."
}
out = json.dumps(result, indent=2) + "\n"
Path(__file__).with_name("class4_magnus_certificate_output.txt").write_text(out)
print(out, end="")

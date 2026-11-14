#!/usr/bin/env python3
"""Exact free-word and finite-matrix certificates for D.67."""

from itertools import product
from pathlib import Path
import json


COUNTS = {"word_generator_equalities": 0,
          "word_multiplication_pairs": 0,
          "outer_matrix_multiplication_pairs": 0,
          "mod_two_conjugation_pairs": 0,
          "cubic_inverting_pairs": 0}


def reduce_word(w):
    stack = []
    for letter in w:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(w):
    return tuple(-letter for letter in reversed(w))


def multiply(*words):
    return reduce_word(letter for word in words for letter in word)


def apply(a, w):
    return multiply(*(a[abs(letter) - 1] if letter > 0
                      else inverse(a[abs(letter) - 1]) for letter in w))


def compose(a, b):
    return tuple(apply(a, word) for word in b)


def power(a, n):
    result = ID
    for _ in range(n):
        result = compose(result, a)
    return result


def inner(w):
    return tuple(multiply(w, (letter,), inverse(w)) for letter in (1, 2))


def check_aut(a, b):
    for left, right in zip(a, b):
        assert left == right, (left, right)
        COUNTS["word_generator_equalities"] += 1


def matrix(a):
    columns = []
    for word in a:
        columns.append(tuple(sum(1 if letter == j else -1 if letter == -j else 0
                                 for letter in word) for j in (1, 2)))
    return ((columns[0][0], columns[1][0]),
            (columns[0][1], columns[1][1]))


def mm(a, b, modulus=None):
    out = tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                      for j in range(2)) for i in range(2))
    if modulus is not None:
        out = tuple(tuple(value % modulus for value in row) for row in out)
    return out


def determinant(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def mpower(a, n, modulus=None):
    out = IM
    for _ in range(n):
        out = mm(out, a, modulus)
    return out


def minverse2(a):
    assert determinant(a) % 2 == 1
    return ((a[1][1] % 2, -a[0][1] % 2),
            (-a[1][0] % 2, a[0][0] % 2))


ID = ((1,), (2,))
IM = ((1, 0), (0, 1))
R = ((2,), (-1,))
RINV = ((-2,), (1,))
B = ((1,), (-2,))
ALPHA0 = ((2, 1, -2), (-2,))
ALPHA1 = ((2,), (1,))
ZETA0 = ((-1,), (2,))
ZETA1 = ((-1,), (-2,))
CUSP = (1, 2, -1, -2)


def main():
    check_aut(compose(R, RINV), ID)
    check_aut(compose(RINV, R), ID)
    check_aut(power(R, 4), ID)
    check_aut(power(R, 2), ZETA1)
    check_aut(compose(B, compose(R, B)), RINV)
    check_aut(compose(inner((2,)), B), ALPHA0)
    check_aut(compose(R, B), ALPHA1)
    check_aut(compose(R, ALPHA0), compose(inner((-1,)), ALPHA1))
    check_aut(compose(R, compose(ALPHA0, RINV)), compose(inner((-1,)), ZETA0))
    check_aut(compose(R, compose(ZETA0, RINV)), compose(inner((-2,)), ALPHA0))
    check_aut(compose(R, compose(ALPHA1, RINV)), compose(ZETA1, ALPHA1))
    check_aut(compose(ALPHA0, ZETA0), compose(inner((2,)), ZETA1))
    check_aut(power(ALPHA0, 2), ID)
    check_aut(power(ALPHA1, 2), ID)
    assert apply(R, CUSP) == multiply((-1,), CUSP, (1,))
    assert apply(B, CUSP) == multiply((-2,), inverse(CUSP), (2,))

    elements = {(k, e): compose(power(R, k), power(B, e))
                for k in range(4) for e in range(2)}
    matrices = {label: matrix(a) for label, a in elements.items()}
    assert len(set(elements.values())) == len(set(matrices.values())) == 8
    assert matrices[(1, 0)] == ((0, -1), (1, 0))
    assert matrices[(0, 1)] == ((1, 0), (0, -1))

    def label_product(x, y):
        return ((x[0] + (-1 if x[1] else 1) * y[0]) % 4,
                (x[1] + y[1]) % 2)

    def label_inverse(x):
        return next(y for y in elements if label_product(x, y) == (0, 0))

    def conjugate(x, y):
        return label_product(label_product(x, y), label_inverse(x))

    for left, right in product(elements, repeat=2):
        target = label_product(left, right)
        check_aut(compose(elements[left], elements[right]), elements[target])
        COUNTS["word_multiplication_pairs"] += 1
        assert mm(matrices[left], matrices[right]) == matrices[target]
        COUNTS["outer_matrix_multiplication_pairs"] += 1

    v0 = {(0, 0), (2, 0), (0, 1), (2, 1)}
    v1 = {(0, 0), (2, 0), (1, 1), (3, 1)}
    center = {(0, 0), (2, 0)}
    assert v0 & v1 == center
    assert elements[(1, 1)] == ALPHA1
    for v in (v0, v1):
        assert all({conjugate(x, y) for y in v} == v for x in elements)
    assert {x for x in elements
            if all(label_product(x, y) == label_product(y, x)
                   for y in elements)} == center
    reduction_kernel = {label for label, m in matrices.items()
                        if tuple(tuple(v % 2 for v in row) for row in m) == IM}
    assert reduction_kernel == v0

    gl2 = []
    for values in product(range(2), repeat=4):
        m = (values[:2], values[2:])
        if determinant(m) % 2:
            gl2.append(m)
    assert len(gl2) == 6
    cubic = [m for m in gl2 if m != IM and mpower(m, 3, 2) == IM]
    assert len(cubic) == 2
    inverters = []
    for a, b in product(cubic, gl2):
        conjugated = mm(mm(b, a, 2), minverse2(b), 2)
        COUNTS["mod_two_conjugation_pairs"] += 1
        if conjugated == minverse2(a):
            assert b != IM and mpower(b, 2, 2) == IM
            inverters.append({"cubic": a, "inverter": b})
            COUNTS["cubic_inverting_pairs"] += 1
    assert len(inverters) == 6
    assert all(a != minverse2(a) for a in cubic)

    result = {
        "claim": "D.67", "status": "PASS", "counts": COUNTS,
        "actual_generators": {"R": R, "B": B, "alpha0": ALPHA0,
                              "alpha1": ALPHA1, "zeta0": ZETA0,
                              "zeta1": ZETA1},
        "dihedral_elements": [{"label": label, "automorphism": elements[label],
                               "homology_matrix": matrices[label]}
                              for label in elements],
        "V0_labels": sorted(v0), "V1_labels": sorted(v1),
        "center_labels": sorted(center),
        "mod_two_kernel_labels": sorted(reduction_kernel),
        "GL2_F2_cubic_inversion_pairs": inverters,
        "scope": "Exact specified word and finite-module maps; the full ambient bounds are supplied by D64-D65 and the proved nine-type theorem.",
    }
    output = Path(__file__).with_name("standard_negative_overgroups_d67_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"claim": "D.67", "status": "PASS", "counts": COUNTS,
                      "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()

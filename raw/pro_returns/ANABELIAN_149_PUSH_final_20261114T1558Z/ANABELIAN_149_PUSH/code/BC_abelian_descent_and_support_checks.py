#!/usr/bin/env python3
"""Exact finite character checks and an abstract Heisenberg support profile.

This does not assert geometric realization of the Heisenberg Frobenius module.
It checks the group-algebra obstruction to inferring a sparse annihilator from
nonordinariness alone.
"""
from fractions import Fraction
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json


def character_value(t, a, moduli):
    return sum((Fraction(x * y, m) for x, y, m in zip(t, a, moduli)),
               Fraction()) % 1


def order(t, moduli):
    return lcm(*(m // gcd(x, m) for x, m in zip(t, moduli)))


def abelian_checks():
    families = [(3,), (5,), (9,), (15,), (3, 3), (9, 3),
                (3, 5), (9, 5), (3, 3, 5), (3, 9, 5)]
    rows = []
    total = 0
    for moduli in families:
        elements = list(product(*(range(m) for m in moduli)))
        subgroup_checks = 0
        unit_checks = 0
        for h in elements:
            n = order(h, moduli)
            if n == 1:
                continue
            faithful_value = Fraction(1, n)
            extensions = [t for t in elements
                          if character_value(t, h, moduli) == faithful_value]
            assert extensions
            for t in extensions:
                N = order(t, moduli)
                assert N % n == 0
                primitive = []
                for u in range(1, N):
                    if gcd(u, N) != 1:
                        continue
                    tu = tuple(u * x % m for x, m in zip(t, moduli))
                    assert order(tu, moduli) == N
                    assert character_value(tu, h, moduli).denominator == n
                    primitive.append(tu)
                    unit_checks += 1
                assert len(set(primitive)) == len(primitive)
            subgroup_checks += 1
        total += subgroup_checks + unit_checks
        rows.append({"moduli": moduli, "cyclic_generators": subgroup_checks,
                     "primitive_restrictions": unit_checks})
    return rows, total


def f4mul(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return ans


def omega_power(n):
    return (1, 2, 3)[n % 3]


def f4_matrix_to_f2(M):
    r, c = len(M), len(M[0])
    out = [[0] * (2 * c) for _ in range(2 * r)]
    for i in range(r):
        for j in range(c):
            for b, basis in enumerate((1, 2)):
                value = f4mul(M[i][j], basis)
                out[2 * i][2 * j + b] = value & 1
                out[2 * i + 1][2 * j + b] = (value >> 1) & 1
    return out


def diagonal_blocks(blocks):
    n = sum(len(B) for B in blocks)
    out = [[0] * n for _ in range(n)]
    offset = 0
    for B in blocks:
        for i, row in enumerate(B):
            out[offset + i][offset:offset + len(B)] = row
        offset += len(B)
    return out


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) % 2
             for j in range(n)] for i in range(n)]


def matvec_bits(M):
    value = 0
    for row in M:
        for x in row:
            value = (value << 1) | x
    return value


def binary_rank(vectors):
    pivots = {}
    for v in vectors:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def heisenberg_matrix(g, copies=2):
    a, b, c = g
    blocks = [[[1]], [[1]]]
    for u, v in ((1, 0), (0, 1), (1, 1), (1, 2)):
        blocks.append(f4_matrix_to_f2([[omega_power(u * a + v * b)]]))
    W = [[0] * 3 for _ in range(3)]
    for j in range(3):
        W[(j + a) % 3][j] = omega_power(b * j + c)
    blocks.extend(f4_matrix_to_f2(W) for _ in range(copies))
    return diagonal_blocks(blocks)


def heisenberg_checks():
    elements = list(product(range(3), repeat=3))
    matrices = {g: heisenberg_matrix(g) for g in elements}
    for g in elements:
        for h in elements:
            a, b, c = g
            x, y, z = h
            gh = ((a + x) % 3, (b + y) % 3,
                  (c + z + b * x) % 3)
            assert matmul(matrices[g], matrices[h]) == matrices[gh]
    algebra_rank = binary_rank([matvec_bits(M) for M in matrices.values()])
    assert algebra_rank == 27

    # The coherent Chevalley-Weil module for genus-two base has dimension 28:
    # two trivial lines, four F4-lines, three copies of the F4 3-space.
    coherent_dim = len(heisenberg_matrix((0, 0, 0), copies=3))
    P = [[int(i == j and i < 22) for j in range(28)] for i in range(28)]
    assert coherent_dim == 28
    assert matmul(P, P) == P
    for g in elements:
        U = heisenberg_matrix(g, copies=3)
        assert matmul(P, U) == matmul(U, P)
    stable_rank = binary_rank([sum(x << j for j, x in enumerate(row))
                               for row in P])
    assert stable_rank == 22
    return {
        "group": "Heisenberg group of order 27",
        "multiplication_checks": 27 * 27,
        "coherent_dimension": coherent_dim,
        "stable_dimension": stable_rank,
        "nonordinary_defect": coherent_dim - stable_rank,
        "dimension_of_image_of_F2_group_algebra": algebra_rank,
        "dimension_of_group_algebra_annihilator": 27 - algebra_rank,
        "geometric_realization_claimed": False,
        "meaning": "A nonordinary semilinear profile can retain every irreducible."
    }


def main():
    abelian, total = abelian_checks()
    heisenberg = heisenberg_checks()
    result = {"status": "PASS",
              "abelian_character_checks": total,
              "abelian_families": abelian,
              "heisenberg_profile": heisenberg,
              "scope": "Finite algebra checks; no curve existence theorem."}
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

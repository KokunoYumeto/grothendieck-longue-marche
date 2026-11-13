#!/usr/bin/env python3
"""Finite matrix, character and Bockstein certificates for D.48."""
from itertools import product
from pathlib import Path
import json

BASE = Path(__file__).resolve().with_suffix("")


def mv(v, e, modulus=9):
    x, y = v
    for _ in range(e % 3):
        x, y = -y, x - y
    return x % modulus, y % modulus


def mul(g, h):
    x, y, e = g
    z, w, f = h
    zz, ww = mv((z, w), e)
    return ((x + zz) % 9, (y + ww) % 9, (e + f) % 3)


def finite_model():
    group = list(product(range(9), range(9), range(3)))
    # These are all possible homomorphisms, by images of x,y,s and the
    # semidirect relations. Values in Z/9 use arbitrary coefficients
    # satisfying invariance, plus a section value killed by three.
    chars_9 = [(a, b, c) for a, b, c in product(range(9), repeat=3)
               if b == a and (-a - b) % 9 == b and 3 * c % 9 == 0]
    chars_3 = [(a, b, c) for a, b, c in product(range(3), repeat=3)
               if b == a and (-a - b) % 3 == b]
    assert len(chars_9) == len(chars_3) == 9
    assert all(a % 3 == b % 3 == c % 3 == 0 for a, b, c in chars_9)
    comparisons = 0
    for g, h in product(group, repeat=2):
        gh = mul(g, h)
        # The quotient character u and the invariant kernel character chi.
        ug, uh, ugh = g[2], h[2], gh[2]
        phig = (g[0] + g[1]) % 9
        phih = (h[0] + h[1]) % 9
        phigh = (gh[0] + gh[1]) % 9
        delta_u = (ug + uh - ugh) % 9
        delta_chi = (phig + phih - phigh) % 9
        assert delta_u % 3 == delta_chi % 3 == 0
        assert (delta_u // 3) % 3 == ((ug + uh) // 3) % 3
        az, aw = mv((h[0], h[1]), g[2])
        assert delta_chi == (h[0] + h[1] - az - aw) % 9
        # Both chosen lifts restrict to zero on the opposite input factor.
        if g[0] == g[1] == h[0] == h[1] == 0:
            assert delta_chi == 0
        comparisons += 1
    return {
        "finite_group": "(Z/9)^2 semidirect C3 with matrix [[0,-1],[1,-1]]",
        "order": len(group),
        "characters_to_Z9": chars_9,
        "characters_to_F3": chars_3,
        "all_Z9_characters_reduce_to_zero": True,
        "cochain_pair_comparisons": comparisons,
        "quotient_bockstein_is_the_carry_cocycle": True,
        "kernel_character_bockstein_vanishes_on_chosen_section": True,
    }


def mm(A, B, modulus=None):
    C = [[sum(A[i][k] * B[k][j] for k in range(2))
          for j in range(2)] for i in range(2)]
    return [[c % modulus for c in row] for row in C] if modulus else C


def matrix_checks():
    A = [[0, -1], [1, -1]]
    I = [[1, 0], [0, 1]]
    A2 = mm(A, A)
    assert mm(A2, A) == I
    assert [[A2[i][j] + A[i][j] + I[i][j] for j in range(2)]
            for i in range(2)] == [[0, 0], [0, 0]]
    AmI = [[A[i][j] - I[i][j] for j in range(2)] for i in range(2)]
    determinant = AmI[0][0] * AmI[1][1] - AmI[0][1] * AmI[1][0]
    assert determinant == 3
    D = [[A[j][i] % 3 for j in range(2)] for i in range(2)]
    D2 = mm(D, D, 3)
    norm = [[(I[i][j] + D[i][j] + D2[i][j]) % 3
             for j in range(2)] for i in range(2)]
    differential = [[(D[i][j] - I[i][j]) % 3 for j in range(2)]
                    for i in range(2)]
    assert norm == [[0, 0], [0, 0]]
    vectors = list(product(range(3), repeat=2))
    image = {tuple(sum(differential[i][j] * v[j] for j in range(2)) % 3
                   for i in range(2)) for v in vectors}
    kernel = [v for v in vectors if all(
        sum(differential[i][j] * v[j] for j in range(2)) % 3 == 0
        for i in range(2))]
    assert len(image) == len(kernel) == 3
    return {
        "integral_matrix": A,
        "cube_is_identity": True,
        "cyclotomic_relation": True,
        "determinant_A_minus_I": determinant,
        "dual_mod_three_matrix": D,
        "cyclic_resolution_alternating_matrices": [differential, norm],
        "kernel_dimension": 1,
        "image_dimension": 1,
        "cohomology_dimensions_degrees_zero_through_eight": [1] * 9,
        "period_two_resolution_map": "identity on the displayed coefficient module",
    }


def main():
    result = {
        "claim": "D.48",
        "scope": "Finite inputs for the Bockstein and cyclic spectral-sequence proof; full Brown and boundary-cover arguments are in d48.tex.",
        "matrix": matrix_checks(),
        "finite_model": finite_model(),
        "all_checks_passed": True,
    }
    output = BASE.with_name(BASE.name + "_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

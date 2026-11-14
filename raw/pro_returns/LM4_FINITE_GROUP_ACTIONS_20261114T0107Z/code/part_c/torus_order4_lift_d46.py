#!/usr/bin/env python3
"""Exact finite certificates for the cohomology identities in D.46.

The finite model checks cochains, not the number of section classes of the
full profinite extension. The latter is proved by Brown restriction and
the rank-two cohomology calculation in d46.tex.
"""
from itertools import product, combinations
from pathlib import Path
import json

BASE = Path(__file__).resolve().with_suffix("")


def mul(g, h):
    a, b, e = g
    c, d, f = h
    sign = -1 if e else 1
    return ((a + sign * c) % 4, (b + sign * d) % 4, (e + f) % 2)


def character(g, coefficients):
    a, b, _ = g
    c, d = coefficients
    return (c * a + d * b) % 4


def finite_cochains():
    group = list(product(range(4), range(4), range(2)))
    comparisons = 0
    for coefficients in product(range(4), repeat=2):
        for g, h in product(group, repeat=2):
            gh = mul(g, h)
            vg, vh, vgh = [character(k, coefficients) for k in (g, h, gh)]
            coboundary = (vg + vh - vgh) % 4
            assert coboundary == (2 * g[2] * vh) % 4
            bockstein = (coboundary // 2) % 2
            cup_u_chi = (g[2] * (vh % 2)) % 2
            assert bockstein == cup_u_chi
            bool_coboundary = ((vg % 2) + (vh % 2) - (vgh % 2)) % 4
            cup_square = ((vg % 2) * (vh % 2)) % 2
            assert (bool_coboundary // 2) % 2 == cup_square
            # phi minus its {0,1}-valued lift is twice this 1-cochain.
            k_values = [((v - (v % 2)) // 2) % 2 for v in (vg, vh, vgh)]
            delta_k = (k_values[0] + k_values[1] - k_values[2]) % 2
            assert (bockstein - cup_square) % 2 == delta_k
            comparisons += 1
    return {
        "finite_group": "(Z/4)^2 semidirect C2, with C2 acting by -I",
        "group_order": len(group),
        "mod_four_characters": 16,
        "cochain_pair_comparisons": comparisons,
        "coboundary_equals_2_u_chi": True,
        "bockstein_compared_to_cup_square_by_exact_coboundary": True,
    }


def boolean_algebra():
    points = list(product(range(2), repeat=2))
    monomials = ((0, 0), (1, 0), (0, 1), (1, 1))
    evaluation_matrix = [
        [((a ** i) * (b ** j)) % 2 for i, j in monomials]
        for a, b in points
    ]
    # Enumerate every reduced bilinear polynomial and check evaluation is bijective.
    evaluations = set()
    for coeffs in product(range(2), repeat=4):
        values = tuple(sum(c * m for c, m in zip(coeffs, row)) % 2
                       for row in evaluation_matrix)
        evaluations.add(values)
    assert len(evaluations) == 16
    quotient_certificates = []
    for kept in combinations(range(4), 3):
        values = set(tuple(e[i] for i in kept) for e in evaluations)
        assert len(values) == 8
        assert all(tuple(x * x % 2 for x in v) == v for v in values)
        quotient_certificates.append({
            "retained_evaluation_points": [points[i] for i in kept],
            "dimension": 3,
            "all_elements_idempotent": True,
            "nonzero_nilpotents": 0,
        })
    return {
        "evaluation_matrix_over_F2": evaluation_matrix,
        "evaluation_is_bijective": True,
        "three_dimensional_quotients": quotient_certificates,
    }


def odd_class_set():
    permutations = list(__import__("itertools").permutations(range(3)))
    involutive = [p for p in permutations if all(p[p[i]] == i for i in range(3))]
    fixed_counts = [sum(p[i] == i for i in range(3)) for p in involutive]
    assert sorted(fixed_counts) == [1, 1, 1, 3]
    return {"C2_actions_on_three_classes": 4, "fixed_class_counts": fixed_counts}


def main():
    result = {
        "claim": "D.46",
        "scope": "Finite cochain and algebra identities only; the full section and lift theorem is proved in d46.tex.",
        "cochains": finite_cochains(),
        "localized_boolean_algebra": boolean_algebra(),
        "class_set": odd_class_set(),
        "all_checks_passed": True,
    }
    output = BASE.with_name(BASE.name + "_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

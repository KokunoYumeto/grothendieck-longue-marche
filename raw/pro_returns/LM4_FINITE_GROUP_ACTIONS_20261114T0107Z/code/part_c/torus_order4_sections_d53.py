#!/usr/bin/env python3
"""Finite affine and mod-four checks for the exact D.53 proof."""
import itertools
import json
from pathlib import Path


def matrix(entries):
    return (tuple(entries[:2]), tuple(entries[2:]))


def multiply(a, b, modulus):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) % modulus
                       for j in range(2)) for i in range(2))


def apply(a, v, modulus=2):
    return tuple(sum(a[i][k]*v[k] for k in range(2)) % modulus
                 for i in range(2))


def main():
    identity = ((1, 0), (0, 1))
    minus_identity4 = ((3, 0), (0, 3))
    roots = []
    for entries in itertools.product(range(4), repeat=4):
        r = matrix(entries)
        if multiply(r, r, 4) == minus_identity4:
            reduced = tuple(tuple(value % 2 for value in row) for row in r)
            assert reduced != identity
            assert multiply(reduced, reduced, 2) == identity
            roots.append(r)
    assert roots

    order_two_matrices = [
        matrix(e) for e in itertools.product(range(2), repeat=4)
        if matrix(e) != identity and multiply(matrix(e), matrix(e), 2) == identity
    ]
    assert len(order_two_matrices) == 3
    points = list(itertools.product(range(2), repeat=2))
    configurations = []
    for r in order_two_matrices:
        for shift in points:
            def f(v):
                rv = apply(r, v)
                return tuple((rv[i]+shift[i]) % 2 for i in range(2))
            if any(f(f(v)) != v for v in points):
                continue
            for missing in points:
                selected = [v for v in points if v != missing]
                if set(map(f, selected)) != set(selected):
                    continue
                fixed = [v for v in selected if f(v) == v]
                assert len(fixed) == 1
                moving = [v for v in selected if f(v) != v]
                assert len(moving) == 2
                assert f(moving[0]) == moving[1]
                assert f(moving[1]) == moving[0]
                configurations.append({
                    "linear": r, "shift": shift, "missing": missing,
                    "fixed_section_point": fixed[0], "interchanged_points": moving
                })
    assert len(configurations) == 12

    # The inverse image of the nonidentity C2 element under C4 -> C2
    # consists of the two odd labels. Its full subgroup inverse image
    # is exactly C4, with kernel {0,2}; label 1 selects one generator.
    c4 = list(range(4))
    kernel = [a for a in c4 if a % 2 == 0]
    odd_lifts = [a for a in c4 if a % 2 == 1]
    assert kernel == [0, 2] and odd_lifts == [1, 3]
    assert all((2*a) % 4 == 2 for a in odd_lifts)
    assert [a for a in odd_lifts if a == 1] == [1]

    result = {
        "claim": "D.53",
        "matrices_R_mod4_with_square_minus_I": len(roots),
        "all_have_nonidentity_reduction_mod2": True,
        "nonidentity_order_two_matrices_GL2_F2": len(order_two_matrices),
        "invariant_three_point_affine_configurations": configurations,
        "configuration_count": len(configurations),
        "all_configurations_have_exactly_one_fixed_point": True,
        "exact_C4_quotient_labels": {"kernel": kernel, "odd_lifts": odd_lifts},
        "scope": (
            "Checks the finite matrix obstruction, affine permutation, and quotient labels. "
            "The full uniqueness and centralizer cohomology follow from the specified "
            "normalizer quotient and Brown restriction, as proved in d53.tex."
        )
    }
    Path(__file__).with_name("torus_order4_sections_d53_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

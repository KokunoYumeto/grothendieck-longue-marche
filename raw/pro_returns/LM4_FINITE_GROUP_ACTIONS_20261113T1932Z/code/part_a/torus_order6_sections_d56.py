#!/usr/bin/env python3
"""Exact finite section-coordinate checks for D.56; no recognition inference."""
import itertools
import json
from pathlib import Path


def matmul(a, b, p):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % p
                       for j in range(2)) for i in range(2))


def matvec(a, x, p):
    return tuple(sum(a[i][j] * x[j] for j in range(2)) % p for i in range(2))


def determinant(a, p):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % p


def main():
    identity = ((1, 0), (0, 1))
    points = list(itertools.product(range(2), repeat=2))
    matrices = []
    for values in itertools.product(range(2), repeat=4):
        a = (values[:2], values[2:])
        if determinant(a, 2) and a != identity and matmul(matmul(a, a, 2), a, 2) == identity:
            matrices.append(a)
    assert len(matrices) == 2
    affine_cases = []
    for a in matrices:
        a_minus_i = tuple(tuple((a[i][j] - identity[i][j]) % 2
                               for j in range(2)) for i in range(2))
        assert determinant(a_minus_i, 2) == 1
        for translation in points:
            def action(x):
                y = matvec(a, x, 2)
                return tuple((y[i] + translation[i]) % 2 for i in range(2))
            fixed = [x for x in points if action(x) == x]
            assert len(fixed) == 1
            assert all(action(action(action(x))) == x for x in points)
            invariant_sets = []
            for missing in points:
                subset = set(points) - {missing}
                if {action(x) for x in subset} == subset:
                    invariant_sets.append(subset)
            assert len(invariant_sets) == 1
            subset = invariant_sets[0]
            assert subset == set(points) - set(fixed)
            start = min(subset)
            cycle = [start, action(start), action(action(start))]
            assert len(set(cycle)) == 3 and set(cycle) == subset
            affine_cases.append({"linear_part": a, "translation": translation,
                                 "unique_fixed_point": fixed[0],
                                 "section_class_cycle": cycle})

    cubic_cases = []
    for b in (1, 2):
        subset = {0, b}
        permissible = [d for d in range(3)
                       if {(-x + d) % 3 for x in subset} == subset]
        assert permissible == [b]
        assert (-0 + b) % 3 == b and (-b + b) % 3 == 0
        cubic_cases.append({"nonzero_separation": b, "forced_translation": b,
                            "section_class_action": [[0, b], [b, 0]]})

    # A generator of the quotient C6 acts by a 3-cycle on the three
    # involution classes and a transposition on the two cubic classes.
    quotient = list(range(6))
    two_stabilizers = [[g for g in quotient if (r + g) % 3 == r] for r in range(3)]
    three_stabilizers = [[g for g in quotient if (r + g) % 2 == r] for r in range(2)]
    assert two_stabilizers == [[0, 3]] * 3
    assert three_stabilizers == [[0, 2, 4]] * 2
    assert all((r + 2) % 3 != r for r in range(3))
    assert all((r + 3) % 2 != r for r in range(2))
    assert [g for g in quotient if g % 3 == 0 and g % 2 == 0] == [0]

    result = {
        "claim": "D.56",
        "cubic_linear_matrices_over_F2": len(matrices),
        "affine_involution_section_cases": affine_cases,
        "affine_involution_section_case_count": len(affine_cases),
        "cubic_section_separation_cases": cubic_cases,
        "quotient_C6_stabilizers_of_involution_classes": two_stabilizers,
        "quotient_C6_stabilizers_of_cubic_classes": three_stabilizers,
        "all_assertions_passed": True,
        "scope": "Exact finite affine actions forced by the full section-coordinate maps. "
                 "The proof supplies those maps and the nonlifting conclusion; this "
                 "certificate does not identify the extension with a free profinite product."
    }
    Path(__file__).with_name("torus_order6_sections_d56_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

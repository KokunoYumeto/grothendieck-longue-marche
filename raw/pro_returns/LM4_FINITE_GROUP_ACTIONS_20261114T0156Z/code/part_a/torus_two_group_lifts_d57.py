#!/usr/bin/env python3
"""All finite affine class actions used in the full lifting proof D.57."""
import itertools
import json
from pathlib import Path


def matvec(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) % 2 for i in range(2))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 2
                       for j in range(2)) for i in range(2))


def main():
    points = list(itertools.product(range(2), repeat=2))
    identity = ((1, 0), (0, 1))
    matrices = []
    for entries in itertools.product(range(2), repeat=4):
        a = (entries[:2], entries[2:])
        if matmul(a, a) == identity:
            matrices.append(a)
    assert len(matrices) == 4
    cases = []
    excluded_nonzero_translations = 0
    affine_involutions = 0
    for a in matrices:
        for d in points:
            def action(v):
                av = matvec(a, v)
                return tuple((av[i] + d[i]) % 2 for i in range(2))
            if not all(action(action(v)) == v for v in points):
                continue
            affine_involutions += 1
            invariant_subsets = []
            for omitted in points:
                subset = set(points) - {omitted}
                if {action(v) for v in subset} == subset:
                    invariant_subsets.append(subset)
            if a == identity and d != (0, 0):
                assert not invariant_subsets
                excluded_nonzero_translations += 1
            for subset in invariant_subsets:
                fixed = [v for v in sorted(subset) if action(v) == v]
                expected = 3 if a == identity else 1
                assert len(fixed) == expected
                if a == identity:
                    assert d == (0, 0)
                else:
                    assert len([v for v in points if action(v) == v]) == 2
                    moved = subset - set(fixed)
                    assert len(moved) == 2
                    assert {action(v) for v in moved} == moved
                cases.append({"linear_part": a, "translation": d,
                              "three_section_points": sorted(subset),
                              "invariant_section_points": fixed,
                              "number_of_full_V4_section_classes": expected})
    assert affine_involutions == 10
    assert excluded_nonzero_translations == 3
    assert len(cases) == 16
    assert sum(c["number_of_full_V4_section_classes"] == 3 for c in cases) == 4
    assert sum(c["number_of_full_V4_section_classes"] == 1 for c in cases) == 12
    result = {
        "claim": "D.57",
        "involutive_linear_matrices_over_F2": len(matrices),
        "affine_involutions_checked": affine_involutions,
        "nonzero_translations_excluded_by_three_point_invariance": excluded_nonzero_translations,
        "invariant_three_point_configurations": len(cases),
        "three_section_class_configurations": 4,
        "one_section_class_configurations": 12,
        "cases": cases,
        "all_assertions_passed": True,
        "scope": "Exact affine permutation calculation for the section-class maps. "
                 "The proof uses projectivity, full Brown restriction, and exact finite "
                 "preimages to establish actual labelled V4 and D8 lifts and their counts."
    }
    Path(__file__).with_name("torus_two_group_lifts_d57_output.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

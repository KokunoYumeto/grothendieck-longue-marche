#!/usr/bin/env python3
"""Exhaustive verification of a quadratic tensor-product obstruction over F_2.

H = F_2^2, q(x,y) = xy, and s(x,y) = (y,x).
The ordered basis of H tensor H is (e⊗e, e⊗f, f⊗e, f⊗f).
Enumerate ALL homogeneous degree-two polynomials in its four coordinates:
four square coefficients and six cross coefficients, each in F_2.
No nondegeneracy requirement is imposed on a candidate Q.

Run: python verify_f2_tensor_quadratic.py
The JSON output defaults to f2_tensor_quadratic_results.json beside this file.
Only Python's standard library is required. Assertion failures abort the run.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


VECTORS_2 = tuple(itertools.product((0, 1), repeat=2))
VECTORS_4 = tuple(itertools.product((0, 1), repeat=4))
MONOMIALS = ((0, 0), (1, 1), (2, 2), (3, 3),
             (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
NAMES = tuple(f"z{i}^2" if i == j else f"z{i}*z{j}"
              for i, j in MONOMIALS)
BASIS_4 = tuple(tuple(int(i == j) for i in range(4)) for j in range(4))


def add(u, v):
    return tuple(x ^ y for x, y in zip(u, v))


def q0(v):
    x, y = v
    return x * y


def q1(v):
    x, y = v
    return (x * x + x * y + y * y) % 2


def swap_factor(v):
    return (v[1], v[0])


def tensor(v, w):
    return (v[0] * w[0], v[0] * w[1],
            v[1] * w[0], v[1] * w[1])


def swap_first_tensor_factor(z):
    return (z[2], z[3], z[0], z[1])


def value(coefficients, z):
    return sum(c * z[i] * z[j]
               for c, (i, j) in zip(coefficients, MONOMIALS)) % 2


def polar(function, u, v):
    return function(add(u, v)) ^ function(u) ^ function(v)


def polynomial(coefficients):
    return " + ".join(n for c, n in zip(coefficients, NAMES) if c) or "0"


def expected_linear_conditions(c):
    # Pure basis tensors kill the four square coefficients; the four
    # rank-one row/column sums kill b01,b02,b13,b23.  The all-ones tensor
    # then requires b03+b12=1.  This is checked against evaluation below.
    return (not any(c[:4])
            and c[4] == c[5] == c[8] == c[9] == 0
            and (c[6] ^ c[7]) == 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name(
                            "f2_tensor_quadratic_results.json"))
    args = parser.parse_args()

    # Check that the stated linear symmetry is an isometry of the factor.
    assert all(q0(swap_factor(v)) == q0(v) for v in VECTORS_2)
    assert all(swap_first_tensor_factor(tensor(v, w))
               == tensor(swap_factor(v), w)
               for v in VECTORS_2 for w in VECTORS_2)

    all_coefficients = tuple(itertools.product((0, 1), repeat=10))
    pure_pairs = tuple((v, w, tensor(v, w), q0(v) * q0(w))
                       for v in VECTORS_2 for w in VECTORS_2)
    pure_solutions = []
    invariant_pure_solutions = []
    invariant_all_candidates = 0
    evaluation_condition_agreements = 0

    for c in all_coefficients:
        pure_condition = all(value(c, z) == required
                             for _, _, z, required in pure_pairs)
        invariant = all(value(c, swap_first_tensor_factor(z)) == value(c, z)
                        for z in VECTORS_4)
        invariant_all_candidates += int(invariant)
        assert pure_condition == expected_linear_conditions(c)
        evaluation_condition_agreements += 1
        if pure_condition:
            pure_solutions.append(c)
            if invariant:
                invariant_pure_solutions.append(c)

    assert len(all_coefficients) == 1024
    assert len({z for _, _, z, _ in pure_pairs}) == 10
    assert {polynomial(c) for c in pure_solutions} == {"z0*z3", "z1*z2"}
    assert len(pure_solutions) == 2
    assert not invariant_pure_solutions

    e, f = (1, 0), (0, 1)
    t00, t01, t10, t11 = BASIS_4
    x, y = tensor(add(e, f), e), tensor(add(e, f), f)
    solution_records = []

    for c in pure_solutions:
        Q = lambda z: value(c, z)
        transformed = [d for d in pure_solutions
                       if all(value(d, z) == Q(swap_first_tensor_factor(z))
                              for z in VECTORS_4)]
        assert len(transformed) == 1 and transformed[0] != c
        within_row = [polar(Q, t00, t01), polar(Q, t10, t11)]
        cross = [polar(Q, t00, t11), polar(Q, t10, t01)]
        assert [Q(x), Q(y), Q(add(x, y))] == [0, 0, 1]
        assert polar(Q, x, y) == 1
        assert within_row == [0, 0]
        assert (cross[0] ^ cross[1]) == 1
        # Invariance would identify the two cross pairings by symmetry
        # of the polar form. Both actual solutions violate that equality.
        assert cross[0] != cross[1]
        counterexamples = [list(z) for z in VECTORS_4
                           if Q(swap_first_tensor_factor(z)) != Q(z)]
        assert counterexamples
        solution_records.append({
            "polynomial": polynomial(c),
            "coefficients": dict(zip(NAMES, c)),
            "swap_pullback_polynomial": polynomial(transformed[0]),
            "invariant": False,
            "invariance_counterexamples": counterexamples,
            "polar_expansion": {
                "x": list(x), "y": list(y),
                "Q_x_Q_y_Q_x_plus_y": [Q(x), Q(y), Q(add(x, y))],
                "B_x_y": polar(Q, x, y),
                "B_t00_t01_and_B_t10_t11": within_row,
                "B_t00_t11_and_B_t10_t01": cross,
            },
        })

    # Independently compare both binary forms on every pair of vectors.
    assert all(polar(q0, u, v) == polar(q1, u, v)
               == ((u[0] * v[1] + u[1] * v[0]) % 2)
               for u in VECTORS_2 for v in VECTORS_2)
    zeros0 = [list(v) for v in VECTORS_2 if q0(v) == 0]
    zeros1 = [list(v) for v in VECTORS_2 if q1(v) == 0]
    assert zeros0 == [[0, 0], [0, 1], [1, 0]]
    assert zeros1 == [[0, 0]]
    radical = [list(u) for u in VECTORS_2
               if all(polar(q0, u, v) == 0 for v in VECTORS_2)]
    assert radical == [[0, 0]]

    results = {
        "status": "verified",
        "kind": "own calculation; exhaustive finite-field verification",
        "hypotheses": {
            "field": "F_2",
            "factor_space": "H = F_2^2 with ordered basis (e,f)",
            "factor_quadratic_form": "q(x,y)=xy",
            "factor_isometry": "s(e)=f; s(f)=e",
            "tensor_basis": ["e⊗e", "e⊗f", "f⊗e", "f⊗f"],
            "candidate_Q": "Every homogeneous degree-two polynomial on H⊗H over F_2",
            "nondegeneracy_of_Q_required": False,
            "pure_tensor_condition": "Q(v⊗w)=q(v)q(w) for every v,w in H",
            "invariance_condition": "Q((s⊗id)z)=Q(z) for every z in H⊗H",
        },
        "enumeration": {
            "coefficient_order": list(NAMES),
            "candidate_count": len(all_coefficients),
            "pairs_v_w_tested_per_candidate": len(pure_pairs),
            "distinct_pure_tensors_including_zero": 10,
            "ambient_vectors_tested_for_invariance_per_candidate": len(VECTORS_4),
            "linear_conditions_agree_with_evaluation_for_all_candidates":
                evaluation_condition_agreements == len(all_coefficients),
            "invariant_candidates_before_pure_tensor_condition": invariant_all_candidates,
            "pure_tensor_solution_count": len(pure_solutions),
            "invariant_pure_tensor_solution_count": len(invariant_pure_solutions),
        },
        "solutions": sorted(solution_records, key=lambda record: record["polynomial"]),
        "binary_form_comparison": {
            "q0": "x*y", "q1": "x^2+x*y+y^2",
            "same_polar_form": True,
            "polar_formula": "B((x,y),(u,v))=x*v+y*u",
            "polar_matrix": [[0, 1], [1, 0]],
            "polar_radical": radical,
            "q0_zero_vectors": zeros0,
            "q1_zero_vectors": zeros1,
            "q0_nonzero_isotropic_vector_count": len(zeros0) - 1,
            "q1_nonzero_isotropic_vector_count": len(zeros1) - 1,
        },
        "conclusion": "No candidate Q satisfies both conditions; q0 and q1 have the same nonsingular polar form but different isotropy.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
    print(json.dumps({"status": results["status"],
                      "candidates": len(all_coefficients),
                      "pure_tensor_solutions": len(pure_solutions),
                      "invariant_pure_tensor_solutions": len(invariant_pure_solutions),
                      "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

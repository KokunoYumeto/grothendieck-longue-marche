#!/usr/bin/env python3
"""Exact original Möbius and stabilizer labels for the branch-lift comparison."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import json
from c5_centralizer_labels_f11 import (
    C, THETA, ZETA, cinverse, canonical, mm, mi, IDENTITY, maps_point
)

counts = Counter()


def check(name, value):
    assert value, name
    counts[name] += 1


def main():
    s0 = C(0, THETA**2-2)*ZETA
    t0 = s0*s0
    a_plus = (ZETA-s0)*cinverse(ZETA+s0)
    a_minus = -a_plus
    geometric_parameter = C(1-THETA**2)
    A = canonical((-geometric_parameter, geometric_parameter,
                   C(-1), geometric_parameter))
    D = canonical((ZETA, C(0), C(0), C(1)))
    B = mm(A, D)
    letters = {1: A, 2: B, -2: mi(B)}
    beta = IDENTITY
    beta_word = [-2, 1, 2, 1, -2, 1, 2]
    for letter in beta_word:
        beta = mm(beta, letters[letter])
    tau = canonical((C(0), t0, C(1), C(0)))
    coordinate = canonical((C(1), -s0, C(1), s0))
    tau_W = mm(mm(coordinate, tau), mi(coordinate))
    beta_W = mm(mm(coordinate, beta), mi(coordinate))
    product_W = mm(tau_W, beta_W)
    check("actual_tau_coordinate",
          tau_W == canonical((C(-1), C(0), C(0), C(1))))
    check("actual_beta_coordinate",
          beta_W == canonical((C(0), a_plus, C(1), C(0))))
    check("actual_product_coordinate",
          product_W == canonical((C(0), a_minus, C(1), C(0))))
    for matrix in (tau_W, beta_W, product_W):
        check("actual_involution", mm(matrix, matrix) == IDENTITY)
    check("commuting_actual_lifts", mm(tau_W, beta_W) == mm(beta_W, tau_W))
    check("literal_branch_coefficient",
          a_plus == C(1-2*THETA**2/5)*(C(1)+C(0, 2)))
    check("literal_quotient_coefficient",
          a_plus*a_plus == C(Fraction(-3, 5), Fraction(4, 5)))
    check("branch_values_distinct", a_plus != a_minus)

    # Exact V=W^2 quotient. W^2=a_plus is the fixed equation for beta;
    # W^2=a_minus is the fixed equation for tau beta.
    r = canonical((C(0), a_plus*a_plus, C(1), C(0)))
    for point in (a_plus, a_minus):
        check("actual_fixed_branch_values", maps_point(r, point, point))
    values = [C(1)] + [
        ((ZETA**j-s0)*cinverse(ZETA**j+s0))**2 for j in range(5)
    ]
    paired = (2, 3, 0, 1, 5, 4)
    for i, point in enumerate(values):
        check("actual_free_orbit_pairs", maps_point(r, point, values[paired[i]]))
        check("no_marked_fixed_point", point not in (a_plus, a_minus))
    check("pole_pair", maps_point(r, C(0), None) and maps_point(r, None, C(0)))

    # Automorphisms of the actual V4 label group, with tau, beta,
    # tau beta as the three nonzero elements.
    elements = ((0, 0), (1, 0), (0, 1), (1, 1))
    nonzero = elements[1:]
    def add(x, y):
        return (x[0]^y[0], x[1]^y[1])
    automorphisms = []
    for ordering in permutations(nonzero):
        image = dict(zip(elements, ((0, 0),)+ordering))
        preserves = all(image[add(x, y)] == add(image[x], image[y])
                        for x, y in product(elements, repeat=2))
        check("V4_automorphism_relations", preserves)
        automorphisms.append(image)
    fixes_tau = [image for image in automorphisms if image[(1, 0)] == (1, 0)]
    check("two_tau_preserving_type_maps", len(fixes_tau) == 2)
    check("only_identity_preserves_both_types",
          sum(image[(0, 1)] == (0, 1) and image[(1, 1)] == (1, 1)
              for image in fixes_tau) == 1)
    check("other_map_exchanges_types",
          sum(image[(0, 1)] == (1, 1) and image[(1, 1)] == (0, 1)
              for image in fixes_tau) == 1)

    result = {
        "claim": "F.18", "status": "PASS",
        "beta_word": beta_word,
        "basepoint": s0.encoded(),
        "a_plus": a_plus.encoded(), "a_minus": a_minus.encoded(),
        "branch_stabilizers": {"a_plus": "beta", "a_minus": "tau beta"},
        "tau_W": [x.encoded() for x in tau_W],
        "beta_W": [x.encoded() for x in beta_W],
        "tau_beta_W": [x.encoded() for x in product_W],
        "checks": dict(counts), "total_checks": sum(counts.values()),
        "scope": "The literal original Möbius coordinate and the finite V4 stabilizer labels. Completion, unique branch lifting, the two section classes, and the coset membership map are proved in the text."
    }
    target = Path(__file__).with_name("common_reflection_branch_lift_f18_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in
                     ("claim", "status", "branch_stabilizers", "checks",
                      "total_checks", "scope")}, indent=2))


if __name__ == "__main__":
    main()

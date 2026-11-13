#!/usr/bin/env python3
"""Exact finite checks accompanying Part 1 of EXIT_ONE_TYPE.

These computations check specified matrices, finite cell complexes, and fans.
They do not prove the geometric models, the exit-category reconstruction, or
the topological assertions from which those finite inputs are obtained.
Run from any directory with Python 3 and SymPy. Outputs are written beside
this script as criterion_checks_output.json and criterion_checks_output.txt.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


HERE = Path(__file__).resolve().parent


def ints(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def primitive_rank_one_kernel(rows):
    """Compute a primitive integral generator when nullity is exactly one."""
    matrix = sp.Matrix(rows)
    basis = matrix.nullspace()
    assert len(basis) == 1
    rational = basis[0]
    denominator = sp.ilcm(*[int(x.q) for x in rational])
    vector = [int(denominator * x) for x in rational]
    divisor = math.gcd(*vector)
    vector = [x // divisor for x in vector]
    if next(x for x in vector if x) < 0:
        vector = [-x for x in vector]
    assert math.gcd(*vector) == 1
    assert matrix * sp.Matrix(vector) == sp.zeros(matrix.rows, 1)
    return {"matrix": rows, "rank": int(matrix.rank()),
            "primitive_kernel_generator": vector,
            "opposite_generator": [-x for x in vector]}


def homology_of_free_cell_complex(dimensions, differentials):
    """Integral cellular ranks and torsion, checking d*d=0 exactly.

    For these examples every differential is zero except the primitive
    interval boundary. Thus the displayed Smith factors determine all the
    integral homology groups, with no nontrivial change-of-basis interaction.
    """
    top = len(dimensions) - 1
    d = {0: sp.zeros(0, dimensions[0])}
    for degree in range(1, top + 1):
        d[degree] = differentials.get(
            degree, sp.zeros(dimensions[degree - 1], dimensions[degree]))
        assert d[degree].shape == (dimensions[degree - 1], dimensions[degree])
    d[top + 1] = sp.zeros(dimensions[top], 0)
    for degree in range(2, top + 1):
        assert d[degree - 1] * d[degree] == sp.zeros(
            dimensions[degree - 2], dimensions[degree])
    ranks = {degree: int(matrix.rank()) for degree, matrix in d.items()}
    betti = [dimensions[q] - ranks[q] - ranks[q + 1]
             for q in range(top + 1)]
    factors = {}
    for degree in range(1, top + 1):
        matrix = d[degree]
        if matrix.rows and matrix.cols:
            smith = smith_normal_form(matrix, domain=sp.ZZ)
            nonzero = [abs(int(smith[i, i]))
                       for i in range(min(smith.shape)) if smith[i, i]]
        else:
            nonzero = []
        assert all(value == 1 for value in nonzero)
        factors[str(degree)] = nonzero
    return {"cell_counts_by_degree": dimensions,
            "boundary_ranks_by_degree": [ranks[q] for q in range(1, top + 1)],
            "nonzero_boundary_smith_factors": factors,
            "integral_betti_by_degree": betti,
            "integral_homology_torsion": [],
            "euler_characteristic": sum((-1)**q * b for q, b in enumerate(betti))}


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def fan_check(rays):
    count = len(rays)
    adjacent = [det(rays[i], rays[(i + 1) % count]) for i in range(count)]
    assert adjacent == [1] * count
    self_intersections = [-det(rays[(i - 1) % count], rays[(i + 1) % count])
                          for i in range(count)]
    for i, square in enumerate(self_intersections):
        assert [rays[(i - 1) % count][j] + square * rays[i][j]
                + rays[(i + 1) % count][j] for j in range(2)] == [0, 0]
    return {"rays_counterclockwise": rays, "adjacent_determinants": adjacent,
            "boundary_self_intersections_in_ray_order": self_intersections,
            "cones_by_dimension": [1, count, count],
            "torus_orbit_object_count": 1 + 2 * count}


def compute():
    kernels = {
        "adjacent_counterexample_full_lattice": primitive_rank_one_kernel(
            [[1, 1], [0, 0]]),
        "affine_cusp_b_h_with_h_equal_b_cubed": primitive_rank_one_kernel([[1, 3]]),
        "affine_cusp_a_h_with_h_equal_a_squared": primitive_rank_one_kernel([[1, 2]]),
        "proper_cusp_m_h_in_Z2_semidirect_Z": primitive_rank_one_kernel([[1, 6]]),
    }
    assert kernels["adjacent_counterexample_full_lattice"]["primitive_kernel_generator"] == [1, -1]
    for name, coefficient in [("affine_cusp_b_h_with_h_equal_b_cubed", 3),
                              ("affine_cusp_a_h_with_h_equal_a_squared", 2),
                              ("proper_cusp_m_h_in_Z2_semidirect_Z", 6)]:
        assert kernels[name]["primitive_kernel_generator"] == [coefficient, -1]
    action = sp.Matrix([[0, -1], [1, 1]])
    action_powers = [ints(action**j) for j in range(1, 7)]
    assert action**6 == sp.eye(2)
    assert all(action**j != sp.eye(2) for j in range(1, 6))
    proper = {
        "specified_target": "Z^2 semidirect_A Z; (v,k)(w,l)=(v+A^k w,k+l)",
        "A": ints(action), "powers_A_1_through_A_6": action_powers,
        "order_A": 6, "m": [[0, 0], 1], "h": [[0, 0], 6],
        "node_map": "(u,v) -> ((0,0),u+6v)",
        "primitive_kernel_words": ["m^6 h^-1", "m^-6 h"],
        "scope": "Checks this specified proper target. The affine cusp peripheral pair (m,h) is not assigned this cyclic relation."
    }

    transgressions = {}
    for name, coefficient in [("Hopf", 1), ("trivial", 0), ("conic", 4)]:
        matrix = sp.Matrix([[coefficient]])
        smith = smith_normal_form(matrix, domain=sp.ZZ)
        rank = int(matrix.rank())
        torsion = [] if abs(coefficient) <= 1 else [abs(coefficient)]
        transgressions[name] = {
            "transgression_matrix": ints(matrix), "smith_matrix": ints(smith),
            "kernel_free_rank": 1 - rank,
            "cokernel_free_rank": 1 - rank,
            "cokernel_torsion_invariant_factors": torsion}

    cellular = {
        "S2": homology_of_free_cell_complex([1, 0, 1], {}),
        "interval": homology_of_free_cell_complex([2, 1], {1: sp.Matrix([[-1], [1]])}),
        "S2_times_S2": homology_of_free_cell_complex([1, 0, 2, 0, 1], {}),
    }
    for n in range(1, 7):
        cellular[f"CP{n}"] = homology_of_free_cell_complex(
            [int(q % 2 == 0) for q in range(2 * n + 1)], {})
    assert cellular["S2"]["integral_betti_by_degree"] == [1, 0, 1]
    assert cellular["interval"]["integral_betti_by_degree"] == [1, 0]
    assert cellular["S2_times_S2"]["integral_betti_by_degree"] == [1, 0, 2, 0, 1]

    divisors = list(itertools.combinations(range(1, 6), 2))
    nodes = [(a, b) for a, b in itertools.combinations(divisors, 2)
             if set(a).isdisjoint(b)]
    incidences = [(node_index, list(pair)) for node_index, node in enumerate(nodes)
                  for pair in node]
    incidence_counts = [sum(pair in node for node in nodes) for pair in divisors]
    moduli = {"divisors": divisors, "unordered_disjoint_pairs": nodes,
              "node_divisor_incidences": incidences,
              "counts": {"divisors": len(divisors), "nodes": len(nodes),
                         "incidences": len(incidences),
                         "objects_including_open_stratum": 1 + len(divisors) + len(nodes)},
              "nodes_per_divisor": incidence_counts,
              "scope": "Finite stable-partition incidence calculation; not a verification of the infinite curve complex or exit mapping spaces."}
    assert moduli["counts"] == {"divisors": 10, "nodes": 15, "incidences": 30,
                                "objects_including_open_stratum": 26}
    assert incidence_counts == [3] * 10

    toric = {
        "P2": fan_check([[1, 0], [0, 1], [-1, -1]]),
        "P1_times_P1": fan_check([[1, 0], [0, 1], [-1, 0], [0, -1]]),
        "F2": fan_check([[1, 0], [0, 1], [-1, 2], [0, -1]])}
    assert [toric[name]["torus_orbit_object_count"]
            for name in ["P2", "P1_times_P1", "F2"]] == [7, 9, 9]
    assert toric["P2"]["boundary_self_intersections_in_ray_order"] == [1, 1, 1]
    assert toric["P1_times_P1"]["boundary_self_intersections_in_ray_order"] == [0, 0, 0, 0]
    assert toric["F2"]["boundary_self_intersections_in_ray_order"] == [0, -2, 0, 2]

    return {"status": "PASS", "arithmetic": "Exact integers and rational linear algebra; SymPy Smith normal forms",
            "sympy_version": sp.__version__,
            "scope": "Finite verification of supplied algebraic and cellular models. Geometric identifications and general theorems require the proofs in the paper.",
            "primitive_kernels": kernels, "proper_cusp_target": proper,
            "transgression_smith_forms": transgressions, "cellular_homology": cellular,
            "Mbar_0_5": moduli, "toric_surfaces": toric}


def human_summary(data):
    lines = ["criterion_checks.py: PASS", data["scope"], "", "Primitive integral kernels:"]
    for name, row in data["primitive_kernels"].items():
        lines.append(f"  {name}: {row['matrix']} -> {row['primitive_kernel_generator']} (up to sign)")
    lines.extend(["  Proper cusp target: A has exact order 6; m=(0,1), h=(0,6).",
                  "  This does not impose h=m^6 on the affine cusp peripheral subgroup.",
                  "", "Transgression Smith forms:"])
    for name, row in data["transgression_smith_forms"].items():
        lines.append(f"  {name}: SNF={row['smith_matrix']}; kernel rank={row['kernel_free_rank']}; cokernel free rank={row['cokernel_free_rank']}, torsion={row['cokernel_torsion_invariant_factors']}")
    lines.append("\nIntegral cellular Betti numbers (torsion zero in these models):")
    for name, row in data["cellular_homology"].items():
        lines.append(f"  {name}: {row['integral_betti_by_degree']}; Euler={row['euler_characteristic']}")
    lines.extend(["", f"Mbar_0_5 counts: {data['Mbar_0_5']['counts']}", "", "Smooth toric fans:"])
    for name, row in data["toric_surfaces"].items():
        lines.append(f"  {name}: adjacent determinants={row['adjacent_determinants']}; boundary squares={row['boundary_self_intersections_in_ray_order']}; objects={row['torus_orbit_object_count']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    result = compute()
    summary = human_summary(result)
    (HERE / "criterion_checks_output.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (HERE / "criterion_checks_output.txt").write_text(summary, encoding="utf-8")
    print(summary, end="")

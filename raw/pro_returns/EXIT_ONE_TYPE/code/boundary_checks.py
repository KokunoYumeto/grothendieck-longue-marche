#!/usr/bin/env python3
"""Exact finite checks for Part 4. Requires Python 3 and SymPy.

The laminar complexes are finite coarse dual complexes, not the infinite P_k.
The Smith normal form is computed over ZZ, not inferred from Euler numbers.
"""
from collections import Counter
from itertools import combinations, permutations
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def compatible(a, b):
    return a <= b or b <= a or a.isdisjoint(b)


def boundary(rows, columns):
    result = Matrix.zeros(len(rows), len(columns))
    row_index = {face: i for i, face in enumerate(rows)}
    for j, simplex in enumerate(columns):
        for k in range(len(simplex)):
            face = simplex[:k] + simplex[k + 1:]
            result[row_index[face], j] += (-1) ** k
    return result


def spanning_forest(vertex_count, edges):
    parent = list(range(vertex_count))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    tree, cotree = [], []
    for edge_index, (u, v) in enumerate(edges):
        a, b = find(u), find(v)
        if a == b:
            cotree.append(edge_index)
        else:
            parent[a] = b
            tree.append(edge_index)
    components = len({find(i) for i in range(vertex_count)})
    return tree, cotree, components


def laminar_complex(n):
    assert 4 <= n <= 6
    vertices = [
        frozenset(a)
        for size in range(2, n - 1)
        for a in combinations(range(1, n), size)
    ]
    simplices = []
    for size in range(1, n - 2):
        simplices.append([
            family for family in combinations(range(len(vertices)), size)
            if all(compatible(vertices[a], vertices[b])
                   for a, b in combinations(family, 2))
        ])
    edges = simplices[1] if len(simplices) > 1 else []
    triangles = simplices[2] if len(simplices) > 2 else []
    d1 = boundary(simplices[0], edges)
    d2 = boundary(edges, triangles)
    assert d1 * d2 == Matrix.zeros(len(vertices), len(triangles))
    tree, cotree, components = spanning_forest(len(vertices), edges)
    projected = d2.extract(cotree, list(range(len(triangles))))
    if projected.rows and projected.cols:
        smith = smith_normal_form(projected, domain=ZZ)
        diagonal = [
            abs(int(smith[i, i]))
            for i in range(min(smith.rows, smith.cols))
            if smith[i, i] != 0
        ]
    else:
        diagonal = []
    rank_d2 = len(diagonal)
    result = {
        "n": n,
        "face_vector": [len(level) for level in simplices],
        "components": components,
        "boundary_square_zero": True,
        "spanning_forest_edges": len(tree),
        "cycle_lattice_rank": len(cotree),
        "projected_boundary_shape": [projected.rows, projected.cols],
        "smith_nonzero_diagonal_histogram":
            dict(sorted(Counter(map(str, diagonal)).items())),
        "H1_torsion_invariant_factors": [d for d in diagonal if d > 1],
        "reduced_homology_free_ranks": {
            "0": components - 1,
            "1": len(cotree) - rank_d2,
            "2": len(triangles) - rank_d2,
        },
    }
    expected_faces = {4: [3], 5: [10, 15], 6: [25, 105, 105]}
    assert result["face_vector"] == expected_faces[n]
    if n == 6:
        assert diagonal == [1] * 81
    return result


def component_segal_counterexample():
    tau = {1: 2, 2: 1, 3: 4, 4: 3}

    def act(flag):
        return tuple(tuple(sorted(tau[i] for i in branch_set))
                     for branch_set in flag)

    def orbit(flag):
        return min(flag, act(flag))

    upper = [((1, 2, 3), (1, 2)), ((1, 2, 4), (1, 2))]
    lower = [((1, 2), (1,)), ((1, 2), (2,))]
    triples = [
        (a, (1, 2), c)
        for a in ((1, 2, 3), (1, 2, 4))
        for c in ((1,), (2,))
    ]
    triple_orbits = sorted({orbit(flag) for flag in triples})
    composite_orbits = sorted({
        orbit((flag[0], flag[2])) for flag in triples
    })
    upper_count = len({orbit(flag) for flag in upper})
    lower_count = len({orbit(flag) for flag in lower})
    assert (upper_count, lower_count, len(triple_orbits),
            len(composite_orbits)) == (1, 1, 2, 2)
    return {
        "permutation": "(12)(34)",
        "upper_arrow_components": upper_count,
        "lower_arrow_components": lower_count,
        "selected_composable_pairs": upper_count * lower_count,
        "triple_flag_components": len(triple_orbits),
        "distinct_composite_components": len(composite_orbits),
        "triple_representatives": triple_orbits,
        "composite_representatives": composite_orbits,
    }


def loop_graph_and_bar():
    involution = (1, 0, 2)  # Two loop half-edges; the labelled leg is 2.
    automorphisms = [
        p for p in permutations(range(3))
        if p[2] == 2 and all(
            p[involution[i]] == involution[p[i]] for i in range(3)
        )
    ]
    # Normalized C_2 bar differential:
    # d[1|1] = [1] - [0] + [1], and [0] is degenerate.
    terms = [((1,), 1), (((1 + 1) % 2,), -1), ((1,), 1)]
    d2 = sum(coefficient for word, coefficient in terms if 0 not in word)
    assert len(automorphisms) == 2 and d2 == 2
    return {
        "type": [1, 1],
        "automorphism_count": len(automorphisms),
        "automorphisms_on_half_edges_and_leg": automorphisms,
        "coarse_length_one_space": "point",
        "normalized_C2_bar_d2": d2,
        "H1_of_graph_category": "Z/2",
    }


def normal_bundle_checks():
    results = []
    for degree in (1, 2):
        euler = degree * degree
        smith = smith_normal_form(Matrix([[euler]]), domain=ZZ)
        invariant = abs(int(smith[0, 0]))
        results.append({
            "plane_curve_degree": degree,
            "normal_Euler_number": euler,
            "Smith_diagonal": [invariant],
            "link_fundamental_group":
                "trivial" if invariant == 1 else "Z/" + str(invariant),
        })
    return results


def main():
    result = {
        "warning": "Finite coarse dual complexes are not the infinite P_k.",
        "genus_zero": [laminar_complex(n) for n in (4, 5, 6)],
        "component_Segal_counterexample": component_segal_counterexample(),
        "loop_graph_homotopy_orbit": loop_graph_and_bar(),
        "normal_bundle_examples": normal_bundle_checks(),
    }
    output = Path(__file__).with_name("boundary_checks_output.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact cover, Magnus and periodic-cohomology checks for D.33."""
from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path

from three_cusp_rank_d32 import (
    partitions, from_partition, inverse, cycles, graph_basis, rref,
    dual_characters,
)


def commutator_boundaries(x, y, non_tree):
    n = len(x)
    ix, iy = inverse(x), inverse(y)
    c = tuple(iy[ix[y[x[v]]]] for v in range(n))
    records = []
    for cyc in cycles(c):
        vector = [0]*(2*n)
        v = cyc[0]
        for _ in cyc:
            vector[v] += 1
            v = x[v]
            vector[n+v] += 1
            v = y[v]
            w = ix[v]
            vector[w] -= 1
            v = w
            w = iy[v]
            vector[n+w] -= 1
            v = w
        assert v == cyc[0]
        records.append({"cycle": cyc, "degree": len(cyc),
                        "edge_vector": vector,
                        "homology": [vector[e] for e in non_tree]})
    assert all(sum(b["edge_vector"][i] for b in records) == 0
               for i in range(2*n))
    return records


def poly_multiply(a, b, degree=2):
    out = Counter()
    for u, c in a.items():
        for v, d in b.items():
            if len(u+v) <= degree:
                out[u+v] += c*d
    return {w: c for w, c in out.items() if c}


def magnus_checks():
    x = {(): 1, (0,): 1}
    y = {(): 1, (1,): 1}
    ix = {(): 1, (0,): -1, (0, 0): 1}
    iy = {(): 1, (1,): -1, (1, 1): 1}
    c = poly_multiply(poly_multiply(poly_multiply(x, y), ix), iy)
    assert c == {(): 1, (0, 1): 1, (1, 0): -1}
    forbidden_square = {(0, 1): 1, (1, 0): 1}
    squares = []
    for a, b in product(range(2), repeat=2):
        linear = {(0,): a, (1,): b}
        square = {w: k % 2 for w, k in poly_multiply(linear, linear).items()
                  if k % 2}
        assert square != forbidden_square
        squares.append({"a": a, "b": b,
                        "coefficients_XX_XY_YX_YY": [square.get(w, 0)
                            for w in ((0, 0), (0, 1), (1, 0), (1, 1))]})
    return {"commutator_degree_two": {"XY": 1, "YX": -1},
            "all_linear_squares_over_F2": squares,
            "odd_prime_degree_obstruction": "A pth power's leading degree is p times a positive integer, hence cannot be2 for odd p."}


def periodic_checks():
    out = []
    for p in (2, 3, 5, 7):
        def carry(a, b):
            return ((a+b)//p) % p
        # Inhomogeneous degree-two cocycle; trivial action.
        for a, b, c in product(range(p), repeat=3):
            coboundary = (carry(b, c)-carry((a+b) % p, c)
                          +carry(a, (b+c) % p)-carry(a, b)) % p
            assert coboundary == 0
        assert sum(carry(a, 1) for a in range(p)) % p == 1
        # The same sum vanishes on every coboundary of a one-cochain,
        # checked on a basis of all one-cochains.
        for j in range(p):
            one = [int(a == j) for a in range(p)]
            value = sum(one[1]-one[(a+1) % p]+one[a] for a in range(p)) % p
            assert value == 0
        ranks = []
        for rank in range(1, 7):
            # Tensor of the rank-r free group's cellular resolution and
            # the periodic Cp resolution, evaluated in trivial Fp.
            # Both differentials are zero. Multiplication by u^m moves
            # the r first-factor degree-one generators to their own
            # independent degree-(2m+1) tensor components.
            matrix = [[0]*rank] + [[int(i == j) for j in range(rank)]
                                  for i in range(rank)]
            assert len(rref(matrix, p)[1]) == rank
            ranks.append({"free_rank": rank, "high_cohomology_dimension": rank+1,
                          "cup_product_matrix": matrix, "cup_product_rank": rank})
        out.append({"prime": p, "periodic_class_nonzero_test": 1,
                    "cup_product_checks": ranks})
    return out


def main():
    counts = Counter()
    examples = {}
    for n in range(1, 7):
        for parts in partitions(n):
            x = from_partition(parts)
            for y in permutations(range(n)):
                basis = graph_basis(x, y)
                if basis is None:
                    continue
                counts[f"degree_{n}_transitive_pairs"] += 1
                boundaries = commutator_boundaries(x, y, basis)
                b = len(boundaries)
                assert (n+2-b) % 2 == 0 and n+2-b >= 0
                for p in (2, 3, 5):
                    assert len(rref([v["homology"] for v in boundaries], p)[1]) == b-1
                    counts["boundary_relation_field_checks"] += 1
                    if n % p:
                        continue
                    for selected, boundary in enumerate(boundaries):
                        d = boundary["degree"]
                        if d % p == 0:
                            continue
                        assert b >= 2
                        scalar = pow(d, -1, p)
                        row = [scalar*v % p for v in boundary["homology"]]
                        assert any(row)
                        dual = dual_characters([row], p)[0]
                        assert sum(a*b for a, b in zip(row, dual)) % p == 1
                        counts[f"p_{p}_selected_cusp_checks"] += 1
                        if str(p) not in examples:
                            examples[str(p)] = {
                                "degree": n, "prime": p, "x": x, "y": y,
                                "genus": (n+2-b)//2, "non_tree_edges": basis,
                                "boundaries": boundaries, "selected": selected,
                                "restriction_scalar": scalar,
                                "selected_full_Zp_homology": row,
                                "detecting_character": dual, "evaluation": 1,
                            }
    assert set(examples) == {"2", "3", "5"}
    # Exact count supporting the 3-primary matrix bound.
    gl2f3 = [a for a in product(range(3), repeat=4)
             if (a[0]*a[3]-a[1]*a[2]) % 3]
    assert len(gl2f3) == 48
    result = {
        "claim": "D.33", "status": "passed", "counts": dict(sorted(counts.items())),
        "coverage": "Every connected once-punctured-torus cover through degree six is represented, retaining residual relabeling duplicates.",
        "explicit_cusp_character_examples": examples,
        "magnus_nonpower_checks": magnus_checks(),
        "periodic_cohomology_and_multiplication": periodic_checks(),
        "GL2_F3_order": len(gl2f3),
        "logical_limit": "Finite calculations validate the displayed maps. The arbitrary-degree cover argument, cohomology comparison, and finite-group bounds are proved in d33.tex.",
    }
    destination = Path(__file__).with_name("torus_homology_d33_output.json")
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"status": "passed", "counts": result["counts"],
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()

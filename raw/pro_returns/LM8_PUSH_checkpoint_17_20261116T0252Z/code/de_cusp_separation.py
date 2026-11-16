#!/usr/bin/env python3
"""Exact finite graph certificate for the quotient in Statement D.50.

This verifies the cellular ranks for K_{ell,ell}.  The arithmetic comparison
and the all-prime proof are in D.50, rather than inferred from these examples.
"""
import json
from fractions import Fraction
from pathlib import Path


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][c]
        a[r] = [x / v for x in a[r]]
        for i in range(r + 1, len(a)):
            if a[i][c]:
                v = a[i][c]
                a[i] = [x - v*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def certificate(ell):
    # Edge (i,j) joins major vertex j and minor vertex i.
    edges = [(i, j) for i in range(ell) for j in range(ell)]
    boundary = [[0] * len(edges) for _ in range(2 * ell)]
    for e, (i, j) in enumerate(edges):
        boundary[j][e] = -1
        boundary[ell+i][e] = 1
    boundary_rank = rank(boundary)
    cycle_rank = len(edges) - boundary_rank
    assert boundary_rank == 2*ell-1
    assert cycle_rank == (ell-1)**2
    # The ell^2 deck labels give ell cosets for each vertex factor.
    major = {j for _, j in edges}
    minor = {i for i, _ in edges}
    assert len(major) == len(minor) == ell
    return {
        "ell": ell,
        "vertices": 2*ell,
        "edges": ell**2,
        "boundary_rank_over_Q": boundary_rank,
        "trivial_Galois_quotient_rank": cycle_rank,
        "expected": (ell-1)**2,
        "passed": True,
    }


if __name__ == "__main__":
    data = {
        "statement": "D.50",
        "scope": "finite graph and integral free-rank calculation only",
        "checks": [certificate(ell) for ell in (2, 3, 5, 7, 11)],
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))

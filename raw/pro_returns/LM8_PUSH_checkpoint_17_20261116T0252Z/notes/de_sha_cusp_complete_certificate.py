#!/usr/bin/env python3
"""Exact actual scalar boundary matrices for the new middle cusp range.

The arithmetic, compact topology, and infinite endpoint require the proof.
"""
from pathlib import Path
import hashlib
import json
import time

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def valuation5(x):
    x = abs(int(x))
    if not x:
        return None
    n = 0
    while x % 5 == 0:
        x //= 5
        n += 1
    return n


def report(matrix):
    diagonal = smith_normal_form(matrix, domain=ZZ)
    entries = [int(diagonal[i, i]) for i in range(min(diagonal.shape))]
    return {"free_rank": sum(x == 0 for x in entries),
            "positive_five_valuations": sorted(valuation5(x) for x in entries if x and valuation5(x))}


def cyclic_shift(n, amount):
    out = sp.zeros(n)
    for j in range(n):
        out[(j + amount) % n, j] = 1
    return out


def run():
    rows = []
    targets = []
    for m in [1, 2]:
        n = 5**m
        identity = sp.eye(n)
        translation = cyclic_shift(n, 1)
        substitution = sp.zeros(n)
        for j in range(n):
            substitution[(2*j) % n, j] = 1
        target = (identity + translation) * substitution
        target_report = report(target - identity)
        assert target_report == {"free_rank": m, "positive_five_valuations": []}
        targets.append({"m": m, "dimension": n, "actual_target": target_report})
        half_gauge = cyclic_shift(n, -pow(2, -1, n))
        for r in range(m):
            h = m-r
            deep_shift = cyclic_shift(n, 5**r)
            actual_map = deep_shift - identity
            norm = sp.zeros(n)
            for i in range(5**h):
                norm += cyclic_shift(n, i*5**r)
            source = (identity+translation) * (identity+deep_shift) * substitution
            diagonal_source = half_gauge * source
            diagonal_target = half_gauge * target
            assert actual_map * norm == sp.zeros(n)
            assert target * actual_map == actual_map * source
            assert diagonal_target * actual_map == actual_map * diagonal_source
            assert half_gauge * diagonal_source == source * half_gauge
            assert source * norm == 2*(identity+translation)*norm*substitution
            # The natural map has rank h on the rational orbit quotient.
            target_left_kernel = (target-identity).T.nullspace()
            projection = sp.Matrix.vstack(*(x.T for x in target_left_kernel))
            assert (projection*actual_map).rank() == h
            for b in [1, 2, 3, 4]:
                relation = 5**b * norm
                first = report((source-identity).row_join(relation))
                diagonal = report((diagonal_source-identity).row_join(relation))
                expected = {"free_rank": h,
                            "positive_five_valuations": [h+min(b, k) for k in range(1, r+1)]}
                assert first == diagonal == expected
                rows.append({"r": r, "m": m, "N": m+b,
                             "h": h, "b": b, "dimension": n,
                             "actual_source": first,
                             "actual_diagonal_source": diagonal,
                             "natural_map_free_rank": h,
                             "norm_relation_and_natural_map_exact": True})
    # The first strict-middle example with a retained smaller exponent.
    r, m, e = 1, 2, 3
    base = 1+5**(e+1)
    tangent = 5**(5**m) * base**(5**r)
    assert base == 626 and base % 4 == 2
    assert valuation5(base-1)-1+r == 4
    assert valuation5(5**m) == m and valuation5(5**r) == r
    example = {"r": r, "m": m, "N": 4, "e": e,
               "rational_tangent": str(tangent), "expression": "5^25 * 626^5",
               "infinite_torsion_exponent": 3,
               "retained_finite_exponents": [2, 2],
               "separate_free_boundary_rank": 2}
    return {"status": "PASS", "candidate": "D.91, unregistered",
            "scope": "Literal actual scalar actions, norm relations, diagonal gauge, natural-map ranks and integral Smith factors in the strict middle range. The full theorem and infinite topology are proved separately.",
            "target_rows": targets, "middle_rows": rows, "actual_rational_example": example}


if __name__ == "__main__":
    start = time.monotonic()
    result = run()
    result["elapsed_seconds"] = time.monotonic()-start
    result["source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))

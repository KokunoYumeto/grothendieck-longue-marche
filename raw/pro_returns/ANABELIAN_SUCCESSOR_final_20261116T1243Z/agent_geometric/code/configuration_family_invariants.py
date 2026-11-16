#!/usr/bin/env python3
"""Exact integer/rational consistency checks for the AG.39 cyclic family.

These computations do not enumerate a finite monodromy witness.  The theorem
uses the separate geometric and group-theoretic proof in the LaTeX draft.
"""
from fractions import Fraction
import json
from pathlib import Path


def invariants(g):
    assert g >= 2
    m = 3 ** (2*g)
    gc = 3*g - 2
    gb = m*(g-1) + 1
    h = (3*(2*gc-2) + 3*2 + 2)//2
    graph_degree = m//3
    graph_square = graph_degree*(2-2*gc)
    d2 = 3*graph_square
    kd = 3*((2*gb-2) + graph_degree*(2*gc-2))
    ey = (2-2*gc)*(2-2*gb)
    ky2 = 2*ey
    ed = 3*(2-2*gb)
    es = 3*ey - 2*ed
    ks2 = 3*(Fraction(ky2) + Fraction(4, 3)*kd + Fraction(4, 9)*d2)
    signature = (ks2 - 2*es)/3
    assert h == 9*g-5
    assert es == (2-2*h)*(2-2*gb)
    assert ks2.denominator == signature.denominator == 1
    assert signature == Fraction(16, 3)*m*(g-1) > 0
    return {
        "base_genus": g,
        "homology_cover_degree": m,
        "unramified_cubic_genus": gc,
        "base_cover_genus": gb,
        "branch_graphs": 3,
        "degree_of_each_graph_to_Cprime": graph_degree,
        "branched_fiber_genus": h,
        "fiber_cover_degree": 9,
        "punctures_on_branched_fiber": 3,
        "affine_fiber_H1_rank": 2*h+2,
        "compact_fiber_H1_rank": 2*h,
        "cuspidally_pro3_compactified_H1_rank_at_other_odd_primes": 2*gc,
        "lost_H1_dimensions_at_other_odd_primes": 2*(h-gc),
        "D_square": d2,
        "K_Y_dot_D": kd,
        "K_Y_square": ky2,
        "euler_S": es,
        "K_S_square": int(ks2),
        "signature_S": int(signature),
    }


if __name__ == "__main__":
    result = {
        "status": "All exact arithmetic assertions passed",
        "scope": "Numerical family invariants; no finite monodromy matrix is claimed",
        "cases": [invariants(g) for g in (2, 3, 4)],
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))

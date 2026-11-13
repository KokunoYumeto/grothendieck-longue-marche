#!/usr/bin/env python3
"""Exact finite endpoint certificate for C.35; no numerical exponentials."""
from fractions import Fraction as F
import json
from pathlib import Path


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def as_ints(values):
    assert all(x.denominator == 1 for x in values)
    return [int(x) for x in values]


def main():
    restriction = [
        [F(1), F(0)],
        [F(0), F(1)],
        [F(1), F(-1)],
    ]
    loop_vertices = [
        [F(0), F(0)],
        [F(1), F(1)],
        [F(1), F(0)],
        [F(0), F(0)],
    ]
    prefix_vertices = loop_vertices[:2]
    current = loop_vertices[2]
    prefix_min = [
        min(dot(row, v) for v in prefix_vertices) for row in restriction
    ]
    prefix_max = [
        max(dot(row, v) for v in prefix_vertices) for row in restriction
    ]
    current_edges = [dot(row, current) for row in restriction]
    median_edges = [
        sorted([lo, now, hi])[1]
        for lo, now, hi in zip(prefix_min, current_edges, prefix_max)
    ]
    annihilator = [F(1), F(-1), F(-1)]
    annihilator_product = [
        sum((annihilator[i] * restriction[i][k] for i in range(3)), F(0))
        for k in range(2)
    ]
    residual = dot(annihilator, median_edges)
    assert annihilator_product == [0, 0]
    assert median_edges == [1, 0, 0]
    assert residual == 1
    assert dot(annihilator, current_edges) == 0
    result = {
        "claim": "C.35",
        "arithmetic": "exact rational",
        "loop_parameter_vertices": [as_ints(v) for v in loop_vertices],
        "vertex_times": ["0", "1/3", "2/3", "1"],
        "homotopy_parameter_s": "2/3",
        "prefix_endpoint_r": "1/3",
        "current_loop_parameter_t": "2/3",
        "edge_order": ["y=0", "x=0", "z=0"],
        "restriction_matrix": [as_ints(row) for row in restriction],
        "prefix_min": as_ints(prefix_min),
        "prefix_max": as_ints(prefix_max),
        "current_edge_translations": as_ints(current_edges),
        "median_edge_translations": as_ints(median_edges),
        "image_annihilator": as_ints(annihilator),
        "annihilator_times_restriction": as_ints(annihilator_product),
        "median_obstruction_residual": int(residual),
        "fixed_median_extends_equivariantly": False,
        "original_loop_contraction": "(a(t),b(t)) maps to ((1-s)a(t),(1-s)b(t))",
        "all_assertions_passed": True,
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(
        "C.35 passed: median edge translations [1, 0, 0]; "
        "restriction-image residual 1."
    )
    print(out)


if __name__ == "__main__":
    main()

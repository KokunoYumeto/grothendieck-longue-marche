#!/usr/bin/env python3
"""Exact rational checks for the separate Teh preprint source audit."""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

COUNTS = Counter()


def determinant(a, b):
    return a[0]*b[1]-a[1]*b[0]


def on_segment(p, a, b):
    ap = (p[0]-a[0], p[1]-a[1])
    ab = (b[0]-a[0], b[1]-a[1])
    return (determinant(ap, ab) == 0
            and min(a[0], b[0]) <= p[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]))


def winding(polygon, p):
    total = 0
    for a, b in zip(polygon, polygon[1:]):
        assert not on_segment(p, a, b), (p, a, b)
        ay, by = a[1]-p[1], b[1]-p[1]
        cross = determinant((b[0]-a[0], b[1]-a[1]),
                            (p[0]-a[0], p[1]-a[1]))
        if ay <= 0 < by and cross > 0:
            total += 1
        elif by <= 0 < ay and cross < 0:
            total -= 1
    return total


def lasso(m):
    tail = [(F(m), F(0)), (F(m), F(1)),
            (F(5, 4), F(1)), (F(5, 4), F(1, 4))]
    square = [(F(5, 4), F(1, 4)), (F(3, 4), F(1, 4)),
              (F(3, 4), F(-1, 4)), (F(5, 4), F(-1, 4)),
              (F(5, 4), F(1, 4))]
    return tail + square[1:] + list(reversed(tail))[1:]


def main():
    radius, epsilon = F(2), F(1, 4)
    assert radius/2+epsilon < radius
    assert 2*radius < 3*radius-epsilon
    COUNTS["two_collar_hypotheses"] += 2
    assert radius/2-epsilon == F(3, 4)
    COUNTS["inner_collar_endpoints"] += 1

    empty_value = F(3, 4)
    for k in range(3, 17):
        time = F(1, 2**k)
        moving_radius = 1-time
        relevant_radii = [moving_radius] + [F(j) for j in range(10, 20)]
        inside = [r for r in relevant_radii if F(3, 4) <= r < 1]
        assert inside == [moving_radius]
        assert max(inside, default=empty_value) == 1-time
        COUNTS["positive_time_exact_collar_supremum"] += 2
    zero_radii = [F(1)] + [F(j) for j in range(10, 20)]
    assert max((r for r in zero_radii if F(3, 4) <= r < 1),
               default=empty_value) == empty_value
    COUNTS["zero_time_empty_collar_supremum"] += 1

    for m in range(3, 13):
        polygon = lasso(m)
        assert polygon[0] == polygon[-1] == (F(m), F(0))
        COUNTS["based_rational_lasso"] += 1
        for stationary_label in range(1, 15):
            if stationary_label == m:
                continue
            point = (F(stationary_label), F(0))
            assert all(not on_segment(point, a, b)
                       for a, b in zip(polygon, polygon[1:]))
            COUNTS["stationary_label_avoidance"] += 1
        assert winding(polygon, (F(1), F(0))) == 1
        assert winding(polygon, (F(2), F(0))) == 0
        COUNTS["exact_pair_windings"] += 2
        assert winding(polygon, (F(0), F(0))) == 0
        COUNTS["zero_avoidance_winding"] += 1

    result = {
        "status": "PASS",
        "purpose": "Separate source-audit counterexample calculations",
        "checks": dict(COUNTS),
        "total_checks": sum(COUNTS.values()),
        "collar_supremum": "u(0)=3/4; u(t)=1-t for 0<t<=1/8",
        "fixed_label_lasso": "strand 4 only; w_(1,4)=1 and w_(2,4)=0",
        "scope": (
            "Rational collar and polygon calculations. Infinite continuity, "
            "nonexistence of a continuous separator, invariance of winding, "
            "and the impossible common finite-truncation realization are "
            "proved in teh_preprints_source_audit.txt without numerical input."
        ),
    }
    output = Path(__file__).with_name("teh_configuration_audit_output.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

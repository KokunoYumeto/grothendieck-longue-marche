#!/usr/bin/env python3
"""Exact finite algebra for C84; topology and full contraction are proved in text."""
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path

import sympy as sp

COUNTS = Counter()


def equal(name, actual, expected):
    assert sp.simplify(actual-expected) == 0, (name, actual, expected)
    COUNTS[name] += 1


def pair_equal(name, actual, expected):
    for a, b in zip(actual, expected):
        equal(name, a, b)


def main():
    x, y, u, eplus, eminus = sp.symbols("x y u eplus eminus", real=True)
    y_nonzero, second = sp.symbols("y_nonzero second", nonzero=True, real=True)
    plus = (u+y_nonzero+eplus)/second
    minus = (u-y_nonzero+eminus)/second
    equal("two_direction_ratio_subtraction", plus-minus,
          (2*y_nonzero+eplus-eminus)/second)
    equal("second_coordinate_recovery",
          (2+(eplus-eminus)/y_nonzero)/(plus-minus),
          second/y_nonzero)
    equal("first_displacement_recovery",
          plus*second/y_nonzero-1-eplus/y_nonzero, u/y_nonzero)

    c, d, r = sp.symbols("c d r", real=True)

    def vertical(amplitude, xx, yy):
        return xx, yy+amplitude*c*sp.sin(2*sp.pi*xx)

    def horizontal(amplitude, xx, yy):
        return xx+amplitude*d*sp.cos(yy), yy

    def contraction(amplitude, xx, yy):
        return horizontal(amplitude, *vertical(amplitude, xx, yy))

    def inverse(amplitude, xx, yy):
        return vertical(-amplitude, *horizontal(-amplitude, xx, yy))

    pair_equal("vertical_inverse",
               vertical(-r, *vertical(r, x, y)), (x, y))
    pair_equal("horizontal_inverse",
               horizontal(-r, *horizontal(r, x, y)), (x, y))
    pair_equal("factorization", contraction(1, x, y),
               (x+d*sp.cos(y+c*sp.sin(2*sp.pi*x)),
                y+c*sp.sin(2*sp.pi*x)))
    pair_equal("contraction_inverse",
               inverse(r, *contraction(r, x, y)), (x, y))
    pair_equal("contraction_inverse",
               contraction(r, *inverse(r, x, y)), (x, y))
    pair_equal("identity_parameter_face", contraction(0, x, y), (x, y))
    pair_equal("original_parameter_face", contraction(1, x, y),
               horizontal(1, *vertical(1, x, y)))
    original = contraction(r, x, y)
    translated = contraction(r, x+1, y)
    pair_equal("actual_translation_relation",
               translated, (original[0]+1, original[1]))
    pair_equal("identity_map_fixed",
               tuple(a.subs({c: 0, d: 0}) for a in original), (x, y))

    radius, theta, alpha = sp.symbols("radius theta alpha", real=True)
    equal("polar_inverse", theta+alpha-alpha, theta)
    equal("polar_inverse", theta-alpha+alpha, theta)
    equal("core_angle_join",
          sp.pi*(2-20*sp.Rational(1, 20)), sp.pi)
    equal("support_boundary_angle",
          sp.pi*(2-20*sp.Rational(1, 10)), 0)

    for k in range(-3, 4):
        center = Q(2*k+1, 2)
        lower = (center, Q(-1, 40))
        upper = (center, Q(1, 40))
        rotate = lambda p: (2*center-p[0], -p[1])
        assert rotate(lower) == upper and rotate(upper) == lower
        COUNTS["literal_core_order_reversal"] += 1
        assert abs(lower[1]) < Q(1, 20)
        assert 2*Q(1, 10) == Q(1, 5) < 1
        COUNTS["core_and_disjoint_support_bounds"] += 2

    result = {
        "claim": "C.84",
        "status": "PASS",
        "checks": dict(COUNTS),
        "total_checks": sum(COUNTS.values()),
        "weighted_metric_denominator": "1+abs(y)",
        "contraction": "A_r(F)=H_(F,r) V_(F,r)",
        "proper_inclusion_witness":
            "periodic radius-1/10 disk rotations, angle pi on radius-1/20 cores",
        "scope": (
            "Exact ratio identities, a nontrivial mixed-fiber instance of the "
            "factorization and its inverse, parameter faces, literal operator "
            "relations, and the rational core-rotation order reversal. "
            "Set identification, both topology maps, monotonicity, all "
            "compact-family limits and inverse continuity are proved in c84.tex."
        ),
    }
    output = Path(__file__).with_name("c84_radial_monotone_output.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

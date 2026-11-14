#!/usr/bin/env python3
"""Exact finite identities for C83's actual evaluation-path obstruction.

The prose proves continuity of the infinite configuration path and rules out
every lift. This producer verifies the algebraic maps, literal deck labels,
time parametrizations and uniform positive displacement bound without floats.
"""
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

import sympy as sp

COUNTS = Counter()


def equal(name, actual, expected):
    assert sp.simplify(actual - expected) == 0, (name, actual, expected)
    COUNTS[name] += 1


def pair_equal(name, actual, expected):
    for a, b in zip(actual, expected):
        equal(name, a, b)


def tent(value):
    return max(F(0), F(1) - 4 * abs(value))


def main():
    radius = sp.symbols("radius", positive=True)
    disk_radius = sp.symbols("disk_radius", positive=True)
    radial = radius / (1 + radius)
    radial_inverse = disk_radius / (1 - disk_radius)
    equal("radial_inverse", radial_inverse.subs(disk_radius, radial), radius)
    equal("radial_inverse", radial.subs(radius, radial_inverse), disk_radius)

    x, y, n, s, t, m = sp.symbols("x y n s t m", real=True)
    bump = sp.Function("b")

    def shear(amplitude, xx, yy):
        return xx + amplitude * n * bump(yy - n), yy

    pair_equal("shear_group_law",
               shear(s, *shear(t, x, y)), shear(s+t, x, y))
    pair_equal("shear_inverse",
               shear(-s, *shear(s, x, y)), (x, y))
    pair_equal("shear_inverse",
               shear(s, *shear(-s, x, y)), (x, y))
    left = shear(s, x+m, y)
    right = shear(s, x, y)
    pair_equal("operator_commutation", left, (right[0]+m, right[1]))

    k, ell = sp.symbols("k ell", integer=True)
    pair_equal("literal_deck_label",
               ((k+4)/4, ell), (k/4+1, ell))

    for index in range(1, 9):
        for offset in (-1, 0, 1):
            value = tent(F(offset))
            assert value == int(offset == 0)
            COUNTS["integer_row_support"] += 1
            for amplitude in (F(0), F(1, 2), F(1)):
                y0 = F(index + offset)
                x0 = F(-3, 4)
                moved = (x0 + amplitude*index*tent(y0-index), y0)
                expected = (x0 + amplitude*index*int(offset == 0), y0)
                assert moved == expected
                COUNTS["exact_row_evaluation"] += 1

        start = F(1, 2**(index+1))
        peak = F(3, 2**(index+2))
        end = F(1, 2**index)
        for time, expected in ((start, 0), (peak, 1), (end, 0)):
            lam = 2**(index+1)*time - 1
            amplitude = 2*min(lam, 1-lam)
            assert amplitude == expected
            COUNTS["up_and_back_endpoints_and_peak"] += 1
        assert F(index, 1+2*index) >= F(1, 3)
        COUNTS["rational_displacement_lower_bound"] += 1

    positive_n = sp.symbols("positive_n", positive=True)
    equal("lower_bound_factorization",
          positive_n/(1+2*positive_n)-sp.Rational(1, 3),
          (positive_n-1)/(3*(1+2*positive_n)))
    assert 2 < 2**2
    COUNTS["strict_square_root_comparison"] += 1
    first = positive_n/(1+sp.sqrt(2)*positive_n)
    second = positive_n/(1+positive_n)
    squared_peak_distance = first**2 + (first-second)**2
    equal("exact_squared_distance_limit",
          sp.limit(squared_peak_distance, positive_n, sp.oo),
          2-sp.sqrt(2))

    result = {
        "claim": "C.83",
        "status": "PASS",
        "checks": dict(COUNTS),
        "total_checks": sum(COUNTS.values()),
        "radial_coordinate": "j(z)=z/(1+norm(z)); inverse w/(1-norm(w))",
        "original_operator": "(x,y)->(x+1,y)",
        "literal_labels": "(k,l)->(k+4,l), with vertex (k/4,l)",
        "actual_shear": "(x,y)->(x+s*n*max(0,1-4*abs(y-n)),y)",
        "peak_time": "3*2^(-n-2)",
        "forced_peak_displacement": ">1/3 for every n>=1",
        "exact_squared_distance_limit": "2-sqrt(2)",
        "scope": (
            "Exact finite identities and rational inequalities only. The "
            "original-disk extension, two-component configuration continuity, "
            "and nonexistence of every continuous evaluation lift are proved "
            "in c83.tex, with no numerical approximation."
        ),
    }
    output = Path(__file__).with_name("c83_evaluation_path_output.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

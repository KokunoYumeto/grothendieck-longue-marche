#!/usr/bin/env python3
"""Exact coordinate checks accompanying C.71.

The source proves properness, all topological comparisons, and the full
contractions. This certificate checks the explicit computable cyclic
model using rational arithmetic and symbolic affine-fiber formulas.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp


CHECKS = Counter()


def check(name, condition):
    assert condition, name
    CHECKS[name] += 1


def kappa(x):
    return x / (1 + abs(x))


def inverse_kappa(s):
    assert -1 < s < 1
    return s / (1 - abs(s))


def tau(s, translation):
    if s in (-1, 1):
        return s
    return kappa(inverse_kappa(s) + translation)


def vertical(point, translation=F(1)):
    x, y = point
    return x, tau(y, translation)


def horizontal(point, translation=F(1)):
    x, y = point
    return tau(x, translation), y


def fiber(beta, y):
    """An increasing integer-equivariant PL lift, 0 <= beta <= 1."""
    assert 0 <= beta <= 1
    integer = y.numerator // y.denominator
    t = y - integer
    if t <= F(1, 2):
        return integer + (1 + beta/2) * t
    return integer + beta/2 + (1 - beta/2) * t


def inverse_fiber(beta, y):
    integer = y.numerator // y.denominator
    t = y - integer
    if t <= F(1, 2) + beta/4:
        return integer + t/(1 + beta/2)
    return integer + (t-beta/2)/(1-beta/2)


def bump(x):
    return max(F(0), 1-abs(x))


def main():
    reals = sorted({F(n, d) for d in range(1, 6)
                    for n in range(-2*d, 2*d+1)})
    compact = sorted({kappa(x) for x in reals} | {F(-1), F(1)})
    shifts = [F(-2), F(-1), F(-1, 2), F(0), F(1, 3), F(1), F(2)]
    for x in reals:
        check("rational_compactification_inverse",
              inverse_kappa(kappa(x)) == x)
    for s in compact:
        if abs(s) < 1:
            check("rational_compactification_inverse",
                  kappa(inverse_kappa(s)) == s)
        for a in shifts:
            check("translation_inverse", tau(tau(s, a), -a) == s)
            for b in shifts:
                check("translation_group_law",
                      tau(tau(s, a), b) == tau(s, a+b))
        check("fixed_set_of_generator",
              (tau(s, F(1)) == s) == (abs(s) == 1))
        if abs(s) < 1:
            check("positive_boundary_motion", tau(s, F(1)) > s)

    # Exact fixed arcs and the partial-compactification counterexample.
    for s in compact:
        for sign in (F(-1), F(1)):
            check("horizontal_edges_fixed",
                  vertical((s, sign)) == (s, sign))
            if abs(s) < 1:
                check("partial_boundary_fixed_by_horizontal_map",
                      horizontal((sign, s)) == (sign, s))
        for t in compact:
            point = (s, t)
            check("horizontal_vertical_commutation",
                  horizontal(vertical(point)) == vertical(horizontal(point)))
    check("partial_restriction_has_no_relative_extension",
          horizontal((F(0), F(1))) == (F(1, 2), F(1)))

    # The actual strip quotient is (s,y) -> (s,[y]); its deck label is 1.
    for s in compact:
        for y in reals:
            for integer in (-2, -1, 0, 1, 2):
                check("strip_quotient_deck_label",
                      (y+integer) % 1 == y % 1)
                check("strip_covering_coordinate",
                      vertical((s, kappa(y)), F(integer))
                      == (s, kappa(y+integer)))

    betas = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    parameters = [F(0), F(1, 5), F(1, 2), F(4, 5), F(1)]
    for beta in betas:
        for y in reals:
            check("nonlinear_fiber_inverse",
                  inverse_fiber(beta, fiber(beta, y)) == y)
            check("nonlinear_fiber_inverse",
                  fiber(beta, inverse_fiber(beta, y)) == y)
            for integer in (-2, -1, 0, 1, 2):
                check("nonlinear_fiber_deck_commutation",
                      fiber(beta, y+integer) == fiber(beta, y)+integer)
            for r in parameters:
                check("actual_fiber_interpolation",
                      (1-r)*fiber(beta, y)+r*y
                      == fiber((1-r)*beta, y))
        for a, b in zip(reals, reals[1:]):
            check("nonlinear_fiber_strict_monotonicity",
                  fiber(beta, a) < fiber(beta, b))
    for x in reals:
        for y in reals:
            beta = bump(x)
            if abs(x) >= 1:
                check("exact_compact_support_in_base",
                      fiber(beta, y) == y)
            for r in parameters:
                check("contraction_preserves_actual_model",
                      (1-r)*fiber(beta, y)+r*y
                      == fiber((1-r)*beta, y))

    # Universal algebraic identities on each affine branch.
    beta, r, t = sp.symbols("beta r t", real=True)
    left = (1+beta/2)*t
    right = beta/2+(1-beta/2)*t
    for branch in (left, right):
        check("symbolic_interpolation_identity",
              sp.simplify((1-r)*branch+r*t
                          - branch.subs(beta, (1-r)*beta)) == 0)
    check("symbolic_left_inverse",
          sp.simplify(left/(1+beta/2)-t) == 0)
    check("symbolic_right_inverse",
          sp.simplify((right-beta/2)/(1-beta/2)-t) == 0)
    check("symbolic_breakpoint_agreement",
          sp.simplify(left.subs(t, sp.Rational(1, 2))
                      - right.subs(t, sp.Rational(1, 2))) == 0)

    result = {
        "claim": "C.71",
        "status": "PASS",
        "total_checks": sum(CHECKS.values()),
        "checks": dict(CHECKS),
        "actual_counterexample": {
            "real_generator": "(x,y) -> (x,y+1)",
            "compactification": "kappa(x)=x/(1+abs(x)), separately in each coordinate",
            "boundary_fixed_set": "the two closed horizontal square edges",
            "partial_space": "[-1,1] x (-1,1)",
            "partial_quotient": "[-1,1] x (R/Z)",
            "nonextendable_relative_map": "(x,y) -> (x+1,y)",
            "witness_on_missing_edge": [[0, 1], ["1/2", 1]]
        },
        "scope": "Exact rational and symbolic checks of the displayed cyclic model. Properness, the actual Lie and compact-word argument, the boundary obstruction, and all full topological group comparisons and contractions are proved in the text."
    }
    target = Path(__file__).with_name("c71_disk_compactification_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

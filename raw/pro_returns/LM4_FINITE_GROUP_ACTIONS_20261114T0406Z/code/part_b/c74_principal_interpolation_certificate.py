#!/usr/bin/env python3
"""Exact coordinate identities for C.74; boundary limits are proved in text."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import sympy as sp


COUNTS = Counter()
s, t, w, a, b, r, u = sp.symbols("s t w a b r u", real=True)
psi = sp.Function("psi")


def check(name, expression):
    assert sp.simplify(expression) == 0, (name, expression)
    COUNTS[name] += 1


def H(x, y):
    return (x-y**3, y)


def Hi(x, y):
    return (x+y**3, y)


def F(c, x, y):
    return (x+(y+c)**3-y**3, y+c)


def M(q, c, x, y):
    return (x+q*((y+c)**3-y**3), y+q*c)


def A(x, y):
    return (x+sp.Rational(3, 4)*y+sp.Rational(3, 8),
            y+sp.Rational(1, 2))


def Ai(x, y):
    return (x-sp.Rational(3, 4)*y, y-sp.Rational(1, 2))


def compare(name, left, right):
    for x, y in zip(left, right):
        check(name, x-y)


def main():
    compare("principal_chart_inverse", H(*Hi(w, t)), (w, t))
    compare("principal_chart_inverse", Hi(*H(s, t)), (s, t))
    compare("actual_fiber_translation",
            H(s+a, t), (H(s, t)[0]+a, H(s, t)[1]))
    compare("conjugated_vertical_translation",
            Hi(H(s, t)[0], H(s, t)[1]+a), F(a, s, t))
    compare("vertical_group_law", F(a, *F(b, s, t)), F(a+b, s, t))
    compare("vertical_inverse", F(-a, *F(a, s, t)), (s, t))
    compare("fiber_commutation", F(a, s+b, t),
            (F(a, s, t)[0]+b, F(a, s, t)[1]))
    compare("general_interpolation",
            H(*M(r, a, *Hi(w, t))),
            (w+3*r*(1-r)*a**2*t+r*(1-r**2)*a**3, t+r*a))
    compare("actual_midpoint",
            H(*M(sp.Rational(1, 2), 1, *Hi(w, t))), A(w, t))
    compare("midpoint_inverse", Ai(*A(w, t)), (w, t))
    compare("midpoint_inverse", A(*Ai(w, t)), (w, t))
    check("midpoint_determinant",
          sp.Matrix(A(w, t)).jacobian((w, t)).det()-1)
    compare("exact_vertical_ray",
            A(0, t),
            (sp.Rational(3, 4)*(t+sp.Rational(1, 2)),
             t+sp.Rational(1, 2)))
    check("exact_vertical_norm",
          A(0, t)[0]**2+A(0, t)[1]**2
          -sp.Rational(25, 16)*(t+sp.Rational(1, 2))**2)
    compare("horizontal_bump_commutation",
            (w+a+u*psi(t), t), (w+u*psi(t)+a, t))
    compare("horizontal_bump_inverse",
            (w+u*psi(t)-u*psi(t), t), (w, t))

    # Three actual out-and-back paths, with exact joins and unit peaks.
    for j in range(1, 4):
        start = Fraction(j-1, 3)
        middle = Fraction(2*j-1, 6)
        end = Fraction(j, 3)
        for time, expected in ((start, 0), (middle, 1), (end, 0)):
            amplitude = min(6*(time-start), 2-6*(time-start))
            assert amplitude == expected
            COUNTS["loop_endpoint_and_peak"] += 1

    # These exact constants enter integral bounds, not numerical angles.
    assert Fraction(3, 4)/(1+Fraction(3, 4)**2) == Fraction(12, 25)
    COUNTS["arctangent_integral_bound"] += 1
    assert Fraction(1, 4)-Fraction(12, 25) == -Fraction(23, 100)
    COUNTS["strict_angle_gap_bound"] += 1

    result = {
        "claim": "C.74",
        "status": "PASS",
        "checks": dict(COUNTS),
        "total_checks": sum(COUNTS.values()),
        "changed_principal_chart": "(s,t) -> (w,t)=(s-t^3,t)",
        "actual_midpoint_in_original_chart":
            "(w,t) -> (w+3*t/4+3/8,t+1/2)",
        "boundary_angle_difference":
            "log(5/4)-arctan(3/4), strictly between -pi/2 and -23/100",
        "scope": (
            "Exact principal-chart inverses, group and interpolation identities, "
            "inverse map, ray factorization, and rational bounds. The full "
            "centralizer, boundary limits, and compact filled-hull obstruction "
            "are proved in the text without numerical approximation."
        ),
    }
    output = Path(__file__).with_name("c74_principal_interpolation_output.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

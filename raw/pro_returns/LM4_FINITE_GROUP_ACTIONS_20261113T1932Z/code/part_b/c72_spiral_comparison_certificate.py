#!/usr/bin/env python3
"""Exact symbolic/rational coordinate certificate for C.72."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as sp


CHECKS = Counter()


def check(name, condition):
    assert condition, name
    CHECKS[name] += 1


def periodic_triangle(y):
    integer = y.numerator // y.denominator
    fraction = y-integer
    return min(fraction, 1-fraction)


def bump(x):
    return max(F(0), 1-abs(x))


def path(j, u, point):
    x, y = point
    if j == 1:
        return x+u, y
    if j == 2:
        return x, y+u
    if j == 3:
        return x+u*periodic_triangle(y), y
    if j == 4:
        return x, y+u*bump(x)
    raise ValueError(j)


def translate(point, integer):
    return point[0], point[1]+integer


def amplitude(t):
    j = min(int(4*t), 3)+1
    local = t-F(j-1, 4)
    return j, min(8*local, 2-8*local)


def main():
    r, rho = sp.symbols("r rho", positive=True)
    theta, u = sp.symbols("theta u", real=True)
    radius = r/(1+r)
    radial_inverse = rho/(1-rho)
    check("symbolic_radial_inverse",
          sp.simplify(radial_inverse.subs(rho, radius)-r) == 0)
    check("symbolic_radial_inverse",
          sp.simplify(radius.subs(r, radial_inverse)-rho) == 0)
    check("symbolic_phase_inverse",
          sp.simplify(sp.log(1+r)
                      +sp.log(1-radius).expand(log=True, force=True)) == 0)

    big = sp.symbols("big", positive=True)
    horizontal_radius = 2*(sp.exp(big)-1)/(2*sp.exp(big)-1)
    horizontal_extra_phase = sp.log(2-sp.exp(-big))
    check("horizontal_image_radius",
          sp.limit(horizontal_radius, big, sp.oo) == 1)
    check("horizontal_image_phase",
          sp.limit(horizontal_extra_phase, big, sp.oo) == sp.log(2))
    check("vertical_input_radius",
          sp.limit(1-sp.exp(-big), big, sp.oo) == 1)
    check("distinct_symbolic_boundary_phases",
          sp.log(2) != 0)

    # Exact B, B^-1, T and A equations in upper-half-plane coordinates.
    x, y = sp.symbols("x y", real=True)
    v = sp.symbols("v", positive=True)
    bx, by = y, sp.exp(x)
    check("upper_half_plane_inverse",
          sp.simplify(sp.log(by)-x) == 0 and bx == y)
    check("upper_half_plane_inverse",
          sp.exp(sp.log(v)) == v)
    check("actual_parabolic_conjugacy",
          bx.subs(y, y+1) == bx+1 and by.subs(y, y+1) == by)
    check("actual_obstructed_map_conjugacy",
          bx.subs(x, 2*x) == bx and
          sp.simplify(by.subs(x, 2*x)-by**2) == 0)
    check("half_plane_map_inverse",
          sp.sqrt(v**2) == v and sp.sqrt(v)**2 == v)
    z = sp.symbols("z")
    cayley = (z-sp.I)/(z+sp.I)
    w = sp.symbols("w")
    cayley_inverse = sp.I*(1+w)/(1-w)
    check("cayley_inverse",
          sp.simplify(cayley.subs(z, cayley_inverse)-w) == 0)
    check("cayley_inverse",
          sp.simplify(cayley_inverse.subs(w, cayley)-z) == 0)

    reals = sorted({F(n, d) for d in range(1, 5)
                    for n in range(-2*d, 2*d+1)})
    parameters = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
    for q in reals:
        for integer in (-2, -1, 0, 1, 2):
            check("primitive_periodic_shear",
                  periodic_triangle(q+integer) == periodic_triangle(q))
        check("periodic_zero_set",
              (periodic_triangle(q) == 0) == (q.denominator == 1))
        check("compact_bump_support",
              abs(q) < 1 or bump(q) == 0)
    for point in [(x, y) for x in reals for y in reals]:
        for j in range(1, 5):
            for parameter in parameters:
                moved = path(j, parameter, point)
                check("path_inverse",
                      path(j, -parameter, moved) == point)
                check("uniform_displacement_bound",
                      max(abs(moved[0]-point[0]), abs(moved[1]-point[1])) <= 1)
                check("actual_cyclic_commutation",
                      path(j, parameter, translate(point, 1))
                      == translate(moved, 1))
    for numerator in range(65):
        t = F(numerator, 64)
        j, a = amplitude(t)
        check("loop_amplitude_range", 0 <= a <= 1)
        if 4*t == int(4*t):
            check("loop_joining_labels", a == 0)
        for r0 in parameters:
            scaled = (1-r0)*a
            check("contraction_amplitude_range", 0 <= scaled <= 1)
            if r0 == 1:
                check("contraction_endpoint", scaled == 0)
            if r0 == 0:
                check("original_loop_retained", scaled == a)

    # Translation centralization equations at exact rational samples.
    for b in reals:
        check("vertical_centralizer_constraint",
              (periodic_triangle(b) == periodic_triangle(F(0)))
              == (b.denominator == 1))
    for a in reals:
        if a:
            integer = int(2/abs(a))+1
            check("horizontal_centralizer_constraint",
                  bump(integer*a) != bump(F(0)))

    result = {
        "claim": "C.72",
        "status": "PASS",
        "total_checks": sum(CHECKS.values()),
        "checks": dict(CHECKS),
        "exact_limits": {
            "first_input": "zeta",
            "second_input": "zeta",
            "horizontal_image": "exp(i log(2)) zeta",
            "vertical_image": "zeta",
            "actual_parabolic_map": "(u,v) -> (u+1,v)",
            "comparison_of_obstructed_map": "(u,v) -> (u,v^2)"
        },
        "scope": "Symbolic and rational coordinate identities. The uniform boundary estimate, full-circle forward orbit limit set, full local centralizer, actual topology and failure of extension are proved in c72.tex. The original loop has its displayed explicit contraction; no nonzero loop class is claimed."
    }
    target = Path(__file__).with_name("c72_spiral_comparison_output.json")
    target.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Exact checks for the H2 node-permutation example and local Kummer maps."""
from pathlib import Path
import json
import sympy as sp

x, t, w, u = sp.symbols("x t w u")
f = (x**2 + 1)**2 * (x**2 - 2) + t
discriminant = sp.factor(sp.discriminant(f, x))
assert discriminant == -46656 * t**2 * (t - 4)**2 * (t - 2)
f0 = f.subs(t, 0)
assert sp.rem(f0, x**2 + 1, x) == 0
assert sp.rem(sp.diff(f0, x), x**2 + 1, x) == 0
assert sp.rem(sp.diff(f0, x, 2), x**2 + 1, x) == 24
assert sp.expand((x**2 + 1)**2 * (w**2 - x**2 + 2)) == sp.expand(
    ((x**2 + 1) * w)**2 - f0)
infinity_rhs = sp.expand(u**6 * f.subs(x, 1/u))
assert sp.expand(infinity_rhs - (1 - 3*u**4 + (t - 2)*u**6)) == 0

# Thickness m: every finite level has surjective base projection and
# precisely the antidiagonal geometric kernel. These finite checks
# accompany the direct all-moduli proof in F17.6.
levels = []
for n in range(2, 19):
    for m in range(1, 10):
        points = [(a,b,c) for a in range(n) for b in range(n)
                  for c in range(n) if (a+b-m*c) % n == 0]
        assert len(points) == n*n
        assert {c for a,b,c in points} == set(range(n))
        kernel = {(a,b,c) for a,b,c in points if c == 0}
        assert kernel == {(a,(-a)%n,0) for a in range(n)}
        for c in range(n):
            assert ((m*c)%n, 0, c) in points
        levels.append({"modulus":n,"thickness":m,"order":n*n,
                       "kernel_order":n,"projection_surjective":True})

# F17.2 is literally the CM-equal-component test. Inverting x identifies
# the outer quartic with the inner cubic, and both remain smooth mod 5.
inner = 1 - x**3
outer = x*(x**3-1)
assert sp.expand(u**4 * outer.subs(x, 1/u)) == 1-u**3
inner_disc = int(sp.discriminant(inner,x))
outer_disc = int(sp.discriminant(outer,x))
assert inner_disc % 5 != 0 and outer_disc % 5 != 0

out = {
    "node_permutation_family": {
        "sextic":str(sp.expand(f)),
        "discriminant":str(discriminant),
        "node_x_minimal_polynomial":"x**2 + 1",
        "second_derivative_at_both_nodes":24,
        "quadratic_coefficient_at_both_nodes":12,
        "normalization":"w**2 = x**2 - 2",
        "chart_at_infinity_rhs":str(infinity_rhs),
        "generic_genus":2,
        "normalization_genus":0,
        "geometric_nodes":2,
        "stable_special_genus":2,
    },
    "thickness_map_finite_checks":levels,
    "compact_type_components": {
        "outer_to_inner":"X = 1/x; Y = V/x**2",
        "common_equation":"Y**2 = 1 - X**3",
        "inner_discriminant":inner_disc,
        "outer_discriminant":outer_disc,
        "both_smooth_modulo_5":True,
    },
}
path = Path(__file__).with_name("CF_h2_checks_output.json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"all_checks_passed":True,
                  "thickness_pairs_checked":len(levels),
                  "node_example_discriminant":str(discriminant),
                  "output":str(path)},indent=2))

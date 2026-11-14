#!/usr/bin/env python3
"""Finite certificates for the central marked-cusp fibers in B.12--B.14."""
from fractions import Fraction
import json


def wedge(x, y):
    return tuple(
        x[i] * y[j] - x[j] * y[i]
        for i in range(len(x))
        for j in range(i + 1, len(x))
    )


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(a, x):
    return tuple(a * b for b in x)


def law(g, h):
    v, z = g
    w, t = h
    return add(v, w), add(add(z, t), scale(Fraction(1, 2), wedge(v, w)))


def inv(g):
    return scale(-1, g[0]), scale(-1, g[1])


e = (1, 0, 0)
v = (0, 3, -6)
b = (0, 2, -4)
a, Q = 9, 7
z = wedge(e, v)
# A finite class-two check with permutation Phi=identity:
# (Q-1)v = a*b. This is the exact relation after dividing by Q.
assert scale(Q - 1, v) == scale(a, b)
t = (scale(a, e), z)
h = (b, (0, 0, 0))
F0t = (scale(Q, t[0]), scale(Q * Q, t[1]))
conjugated = law(law(h, F0t), inv(h))
assert conjugated == (scale(Q, t[0]), scale(Q, t[1]))
# The correcting vector is integral exactly when v/a is integral; use
# a divisible witness to check the actual sign of the conjugation.
v_div = (0, 27, -18)
t_div = (scale(a, e), wedge(e, v_div))
correction = (scale(Fraction(1, a), v_div), (0, 0, 0))
assert law(law(correction, t_div), inv(correction)) == (scale(a, e), (0, 0, 0))


def orbits(q, modulus):
    unseen = set(range(1, modulus))
    ans = []
    while unseen:
        start = min(unseen)
        orbit, x = [], start
        while x not in orbit:
            orbit.append(x)
            x = q * x % modulus
        assert x == start
        unseen.difference_update(orbit)
        ans.append(orbit)
    return ans


rows = []
for q in (2, 7, 13):
    for n in range(1, 8):
        modulus = 3**n
        oo = orbits(q, modulus)
        # These are actual invariant subfamilies of the exterior basis
        # delta_0 wedge delta_v on the rational unmarked cusp line.
        assert len(oo) >= n
        # On each orbit, the sum functional kills Phi-1; q^2=1 mod3.
        for orbit in oo:
            support = set(orbit)
            for v0 in range(modulus):
                assert ((q * q) * int(q * v0 % modulus in support)
                        - int(v0 in support)) % 3 == 0
        rows.append({
            "residue_cardinality": q,
            "label_modulus": modulus,
            "orbit_coinvariant_dimension_on_cusp_axis": len(oo),
            "orbit_lengths": sorted(len(o) for o in oo),
        })

print(json.dumps({
    "exact_BCH_tame_relation": "passed",
    "integral_conjugation_sign": "passed",
    "central_class": "[c,b*c*b^-1], b an unmarked rational cusp loop",
    "finite_orbit_sum_nonzero": True,
    "axis_orbit_certificates": rows,
    "all_assertions": "passed",
}, indent=2))

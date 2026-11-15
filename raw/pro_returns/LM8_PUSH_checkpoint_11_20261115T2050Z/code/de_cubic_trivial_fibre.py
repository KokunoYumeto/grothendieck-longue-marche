#!/usr/bin/env python3
"""Exact identities and finite reductions for the trivial cubic fibre in D.53.

The full-section assertion uses the independently checked Stoll input and
the local section theorem in D.23, not numerical point searching.
"""
import json
from pathlib import Path
import sympy as s

t, z, x, y = s.symbols("t z x y")
X = -4*z
Y = 4*(2*t-1)
cubic = s.expand(Y**2-X**3-16)
assert s.expand(cubic-64*(z**3-t*(1-t))) == 0

Xp = (x**3+64)/x**2
Yp = y*(x**3-128)/x**3
raw = s.factor(Yp**2-Xp**3+432)
factor = s.factor(raw/(y**2-x**3-16))
assert s.cancel(raw-factor*(y**2-x**3-16)) == 0
assert factor == (x**3-128)**2/x**6

counts = {}
for p in (5,7):
    pts = [(a,b) for a in range(p) for b in range(p)
           if (b*b-a**3-16)%p == 0]
    counts[str(p)] = {"affine_points":pts,"projective_count":len(pts)+1}
assert counts["5"]["projective_count"] == 6
assert counts["7"]["projective_count"] == 9

out = {
    "statement":"D.53",
    "cubic_model_identity":str(cubic),
    "degree_three_map": {"X":str(Xp),"Y":str(Yp)},
    "isogeny_identity_multiplier":str(factor),
    "reduction_counts":counts,
    "rational_cusps_on_model":["O","(0,4)","(0,-4)"],
    "scope":"Exact identities and finite counts; finiteness and all full-section claims are proved in D.53."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

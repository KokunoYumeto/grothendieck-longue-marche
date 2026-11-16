#!/usr/bin/env python3
"""Independent exact check of the first A145 binary node."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

w = json.loads((Path(__file__).parent.parent / "notes/uniform_detector_branch_witness.json").read_text())
q = w["q"]
a = (F(529, 382), F(147, 382), F(4089852535355054689, 191))
old = (F(0), F(1), F(1, 2))


def residue(x):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, q) % q


assert all(q % d for d in range(2, isqrt(q) + 1))
for i, aa, root in zip(old, a, w["bit0_roots"]):
    assert pow(root, 4, q) == residue((F(w["bit0_T"]) - i) / aa)
for i, aa, root in zip(old[1:], a[1:], w["bit1_other_residue_roots"]):
    assert pow(root, 4, q) == residue(-i / aa)
for d in w["all_boundary_quadratics_split"]:
    assert pow(d % q, (q - 1) // 2, q) == 1
assert q > (8 * 128 + 8) ** 2
print("PASS: first binary prime primality, both literal residue-root tuples, all five boundary characters, and the strict bound.")
print("The proof, not this finite node check, supplies all later cofinal refinements.")

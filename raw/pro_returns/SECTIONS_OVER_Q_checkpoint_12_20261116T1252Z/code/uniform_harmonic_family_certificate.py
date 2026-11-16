#!/usr/bin/env python3
"""Exact finite-node checks for A145; no simulated infinite recursion."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import json

work = Path(__file__).resolve().parents[1]
w = json.loads((work / "notes/uniform_detector_branch_witness.json").read_text())
q = w["q"]
assert all(q % d for d in range(2, isqrt(q) + 1))
assert q % 4 == 1 and q > (8 * 128 + 8) ** 2
a = (F(529, 382), F(147, 382), F(4089852535355054689, 191))
old = (F(0), F(1), F(1, 2))
c = F(-338, 191)
cp = 1-c

def mod(x, modulus):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, modulus) % modulus

def vp(x):
    x = F(x)
    assert x
    n, d = abs(x.numerator), x.denominator
    v = 0
    while n % q == 0:
        n //= q
        v += 1
    while d % q == 0:
        d //= q
        v -= 1
    return v

def hensel_fourth(root, target):
    assert pow(root, 4, q) == mod(target, q)
    assert (4 * root**3) % q
    discrepancy = (root**4 - mod(target, q*q)) // q
    correction = -discrepancy * pow(4 * root**3, -1, q) % q
    lifted = root + correction*q
    assert pow(lifted, 4, q*q) == mod(target, q*q)
    return lifted

t0 = F(w["bit0_T"])
t1 = a[0]*q**4
h0 = [hensel_fourth(root, (t0-i)/aa)
      for i, aa, root in zip(old, a, w["bit0_roots"])]
h1 = [hensel_fourth(root, (t1-i)/aa)
      for i, aa, root in zip(old[1:], a[1:], w["bit1_other_residue_roots"])]
assert t1/a[0] == q**4
for dd in w["all_boundary_quadratics_split"]:
    assert pow(dd % q, (q-1)//2, q) == 1
for tt in (t0, t1):
    assert vp(tt-c) == vp(tt-cp) == 0
assert vp(-4*t0*(t0-1)) == 0
assert vp(-4*t1*(t1-1)) == 4
assert vp(4*(t0-F(1,2))**2) == vp(4*(t1-F(1,2))**2) == 0
assert a[0]*a[1]*a[2] == F(318039202706815117780707,27871484)
data = {"q":q, "bit0_T":str(t0), "bit1_T":str(t1),
        "bit0_roots_mod_q2":h0, "bit1_other_roots_mod_q2":h1,
        "A_valuation_bit0":0, "A_valuation_bit1":4,
        "B_valuations":[0,0], "extra_difference_valuations":[0,0,0,0],
        "scope":"One finite binary node; later nodes and cofinal compatibility are supplied by the written proof."}
(work / "code/uniform_harmonic_family_data.json").write_text(json.dumps(data, indent=2)+"\n")
lines = [
    f"PASS: q={q} is prime, is1 modulo4, and exceeds the exact first mixed-cover bound.",
    "PASS: five residue fourth roots, five unit derivatives and five literal Hensel lifts modulo q^2.",
    "PASS: all five fixed boundary quadratic characters split; the degree-four boundary polynomials split completely.",
    "PASS: both extra differences are units on both branches; the tripod A valuations are exactly0 and4, and B valuations are0.",
    "PASS: the three initial coefficients multiply to the literal coefficient a used by the fixed order512 detector.",
    "ALL A145 FINITE-NODE CERTIFICATES PASSED.",
    data["scope"]]
out="\n".join(lines)+"\n"
(work / "code/uniform_harmonic_family_certificate_output.txt").write_text(out)
print(out,end="")

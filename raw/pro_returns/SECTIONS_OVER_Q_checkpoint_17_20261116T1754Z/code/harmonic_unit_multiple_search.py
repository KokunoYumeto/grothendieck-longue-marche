#!/usr/bin/env python3
"""Finite good-prime tests for unit multiples on the actual cyclic-four cover.

This is a search certificate only.  A missing finite image is a local
obstruction; nonempty images are not a proof of simultaneous local solubility.
"""
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
from harmonic_elliptic_rank_certificate import add_mod

K, N = 573, 1146
Q0 = Fraction(325596479663, 72962)
A = K * Q0 * Q0
RATIONAL_E_POINTS = {"P": (2028, 75348), "Q": (5202, 365976)}


def prime(p):
    return p > 1 and all(p % d for d in range(2, isqrt(p) + 1))


def residue(f, p):
    f = Fraction(f)
    return f.numerator * pow(f.denominator, -1, p) % p


def phi(P, p):
    if P is None or P[0] == 0:
        return None
    x, y = P
    invx = pow(x, -1, p)
    return ((x - N*N*invx) * pow(4, -1, p) % p,
            y * (1 + N*N*invx*invx) * pow(8, -1, p) % p)


rows = []
failed = {name: [] for name in RATIONAL_E_POINTS}
for p in range(3, 3001):
    if not prime(p) or K % p == 0 or Q0.numerator % p == 0 or Q0.denominator % p == 0:
        continue
    aa, qq, h = residue(A, p), residue(Q0, p), pow(2, -1, p)
    fourths = {}
    for w in range(p):
        fourths.setdefault(aa * pow(w, 4, p) % p, []).append(w)
    image = {None}
    for t in range(p):
        for w in fourths.get(t * (t-1) * (t-h) % p, []):
            image.add(phi((N * (2*t-1) % p, 8*K*K*qq*w*w % p), p))
    for name, integral in RATIONAL_E_POINTS.items():
        R = phi(tuple(v % p for v in integral), p)
        orbit = [None]
        current = R
        while current is not None:
            orbit.append(current)
            current = add_mod(current, R, p, K*K)
            assert len(orbit) <= p + 1 + 2 * isqrt(p) + 2
        order = len(orbit)
        all_allowed = [m for m in range(order) if orbit[m] in image]
        allowed = [m for m in all_allowed if gcd(m, order) == 1]
        forced_divisor = order
        for m in all_allowed:
            forced_divisor = gcd(forced_divisor, m)
        row = {"point": name, "p": p, "order": order,
               "generator_residues_in_D_image": allowed,
               "all_residues_in_D_image": all_allowed,
               "forced_scalar_divisor": forced_divisor,
               "D_image_size": len(image)}
        rows.append(row)
        if not allowed:
            failed[name].append(p)

out = {"scope": "Good-prime finite image test only; surviving residues need not be compatible.",
       "failures": failed, "rows": rows}
Path(__file__).with_name("harmonic_unit_multiple_search_data.json").write_text(
    json.dumps(out, indent=2) + "\n")
print("Actual Dbar(F_p)->F(F_p) unit-generator tests through 3000:", len(rows))
for name in RATIONAL_E_POINTS:
    print(name, "empty unit-generator image primes:", failed[name])
    print(name, "forced scalar divisors:",
          [(r["p"],r["forced_scalar_divisor"]) for r in rows
           if r["point"]==name and r["forced_scalar_divisor"]>1])
print("First exact constraints:")
for row in rows[:20]:
    print(row)
print("No conclusion about surviving compatible profinite units is drawn.")

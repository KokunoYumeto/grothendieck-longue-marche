#!/usr/bin/env python3
"""Exact elementary certificate for the three Fermat-quartic quotient targets.

No rank/BSD oracle is used.  Counts enumerate every F_p point.  The
mathematical proof uses good-reduction injectivity on prime-to-p torsion.
"""
from fractions import Fraction
from math import gcd
import json
from pathlib import Path


def point_count(a, p):
    points = [(x, y) for x in range(p) for y in range(p)
              if (y*y-x*x*x-a*x) % p == 0]
    return {"p": p, "affine_points": points, "count_including_infinity": len(points)+1,
            "good_reduction": (-64*a**3) % p != 0}


def double(a, point):
    x, y = map(Fraction, point)
    slope = (3*x*x+a)/(2*y)
    x2 = slope*slope-2*x
    y2 = slope*(x-x2)-y
    assert y2*y2 == x2*x2*x2+a*x2
    return [str(x2), str(y2)]


rows = []
for name, a, point, primes in [
    ("E_x", -6, (-2, -2), (5, 13)),
    ("E_y", -12, (-2, -4), (5, 7)),
    ("E_z", 18, (3, 9), (5, 7)),
]:
    x, y = point
    assert y*y == x*x*x+a*x and y != 0
    counts = [point_count(a, p) for p in primes]
    assert all(c["good_reduction"] for c in counts)
    bound = gcd(*(c["count_including_infinity"] for c in counts))
    assert bound == 2
    assert counts[0]["count_including_infinity"] % primes[1] != 0
    assert counts[1]["count_including_infinity"] % primes[0] != 0
    rows.append({"name": name, "coefficient_A": a, "point": point,
                 "double": double(a, point), "counts": counts,
                 "rational_torsion_exponent_divides": bound,
                 "point_has_infinite_order": True})

result = {"curve": "x^4+2*y^4=3*z^4", "base_point": [1, 1, 1],
          "base_t": "1/3", "status": "exact finite certificate; no exact rank asserted",
          "elliptic_targets": rows}
dest = Path(__file__).resolve().parents[1] / "audit" / "D_Fermat_quartic_certificate.json"
dest.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

#!/usr/bin/env python3
"""Independent torsion-polynomial check by the elementary Kummer-line law.

No division-polynomial recurrence is used to construct r_n=X([n]P).
The final reduced denominator is compared with the separately constructed
psi_n squared.  All computations are in F2[X].
"""
from functools import cache
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "native"))
from flint import nmod_poly
from primitive_parameter_gcd import psi

X = nmod_poly([0, 1], 2)
one = nmod_poly([1], 2)


@cache
def rational_x(n):
    if n == 1:
        return X, one
    if n % 2 == 0:
        numerator, denominator = rational_x(n//2)
        return numerator**4, denominator**4
    m = n//2
    a, b = rational_x(m)
    c, d = rational_x(m+1)
    denominator = (a*d+c*b)**2
    numerator = X*denominator+(b*d)**2
    common = numerator.gcd(denominator)
    numerator, rem1 = divmod(numerator, common)
    denominator, rem2 = divmod(denominator, common)
    assert rem1 == 0 and rem2 == 0
    assert numerator.gcd(denominator) == one
    return numerator, denominator


if __name__ == "__main__":
    rows = []
    for n in (3, 5, 7, 13, 191, 229):
        numerator, denominator = rational_x(n)
        p = psi(n)
        assert denominator == p*p
        assert numerator.degree() == n*n
        assert denominator.degree() == n*n-1
        raw = bytes(int(c) for c in denominator.coeffs())
        rows.append({"n": n, "numerator_degree": numerator.degree(),
                     "denominator_degree": denominator.degree(),
                     "denominator_equals_psi_squared": True,
                     "denominator_binary_coefficient_sha256": hashlib.sha256(raw).hexdigest()})
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(rows, indent=2)+"\n")
    print(json.dumps(rows, indent=2))

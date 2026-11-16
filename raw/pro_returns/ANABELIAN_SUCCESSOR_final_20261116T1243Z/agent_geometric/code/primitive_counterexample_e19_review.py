#!/usr/bin/env python3
"""Independent finite arithmetic review of the refined e=19 certificate.

Every odd n below the proved cutoff is factored by trial division.  This
does not reuse the root computation's sieve, order cache, or output.
The mathematics is AG.32--AG.34; no pencil parameter is enumerated.
"""
from math import gcd
from pathlib import Path
import json


def factor(n):
    answer = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            answer.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if n > 1:
        answer.append((n, 1))
    return answer


e = 19
q = 4 ** e
cutoff = 10 * e ** 3
rows = []
for n in range(3, cutoff, 2):
    factors = factor(n)
    phi = n
    for prime, exponent in factors:
        phi = phi // prime * (prime - 1)
    if phi ** 2 > 2 * e ** 2 * (n - 1):
        continue
    order = phi
    for prime, exponent in factor(phi):
        while order % prime == 0 and pow(2, order // prime, n) == 1:
            order //= prime
    assert pow(2, order, n) == 1
    assert all(pow(2, order // prime, n) != 1 for prime, _ in factor(order))
    d = gcd(order, e)
    M = phi // d
    if M * (M + 1) > 2 * (n - 1):
        continue
    jordan = 1
    for prime, exponent in factors:
        jordan *= prime ** (4 * (exponent - 1)) * (prime ** 4 - 1)
    rows.append({
        "n": n, "factorization": factors, "phi": phi,
        "order_2": order, "gcd_order_exponent": d, "M": M,
        "exact_order_n_points_J4": jordan,
        "bad_parameter_incidence_bound": jordan // M,
    })

expected = [191, 229, 361, 419, 457, 571, 573, 647, 687,
            955, 1083, 1257, 1371]
assert [row["n"] for row in rows] == expected
bound = sum(row["bad_parameter_incidence_bound"] for row in rows)
assert bound == 214950173608
good = q - 4 - bound
assert good == 59927733332 > 0
root_path = Path(__file__).resolve().parents[2] / "code/A6_scalar_conductor_bounds.json"
root = json.loads(root_path.read_text())
root_row = next(row for row in root["rows"] if row["e"] == e)
for row, reference in zip(rows, root_row["admissible_conductors"], strict=True):
    assert all(row[key] == value for key, value in reference.items())
assert root_row["refined_good_parameter_lower_bound"] == good
result = {
    "status": "all complete cutoff and independent factorization checks passed",
    "e": e, "q": q, "cutoff_exclusive": cutoff,
    "odd_conductors_examined": len(range(3, cutoff, 2)),
    "admissible_conductors": rows,
    "exact_order_multiplicity_union_bound": bound,
    "inadmissible_finite_family_parameters": 4,
    "good_parameter_lower_bound": good,
    "scope": "No nontrivial primitive-zero cover; the identity cover remains a witness.",
    "individual_parameter_enumerated": False,
    "root_certificate_comparison": "all e=19 records agree exactly",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

#!/usr/bin/env python3
"""Exact tame-symbol criterion for the inherited cubic class-two quotient.

The proof is E.29.  This program computes the criterion on all ordered pairs
of positive integers <=200, and all ordered pairs of nonzero reduced
rationals of numerator/denominator height <=16.  It also checks Steinberg
identities, selected ramified examples, and the three explicit central
cohomology classes modulo 3-powers.  No floating point arithmetic is used.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import json


@lru_cache(None)
def factor(n):
    n = abs(n)
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out


@lru_cache(None)
def rational_factors(a):
    out = dict(factor(a.numerator))
    for p, e in factor(a.denominator).items():
        out[p] = out.get(p, 0)-e
    return out


@lru_cache(None)
def valuation_and_unit(a, p):
    n, d = a.numerator, a.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v, (n*pow(d, -1, p)) % p


@lru_cache(None)
def multiplicative_order(u, p):
    assert u % p != 0
    order = p-1
    for prime in factor(p-1):
        while order % prime == 0 and pow(u, order//prime, p) == 1:
            order //= prime
    return order


def three_part(n):
    out = 1
    while n % 3 == 0:
        out *= 3
        n //= 3
    return out


def residues(a, b):
    answer = []
    for p in sorted(set(rational_factors(a)) | set(rational_factors(b))):
        va, ua = valuation_and_unit(a, p)
        vb, ub = valuation_and_unit(b, p)
        # theta_p = (-1)^(va*vb) a^vb/b^va after cancelling valuations.
        theta = ((-1 if va*vb % 2 else 1)*pow(ua, vb, p)
                 *pow(ub, -va, p)) % p
        order = multiplicative_order(theta, p)
        answer.append({"prime": p, "valuation_a": va, "valuation_b": vb,
                       "residue": theta, "order": order,
                       "three_primary_order": three_part(order)})
    return answer


def inspect_pair(a, b):
    rs = residues(a, b)
    bad = [r for r in rs if r["three_primary_order"] > 9]
    return {"a": str(a), "b": str(b), "admits_inherited_class_two_lift": not bad,
            "maximum_three_primary_order": max([1]+[r["three_primary_order"] for r in rs]),
            "obstructing_residues": bad}


integer_histogram = Counter()
obstructed_integer_pairs = []
for a, b in product(range(1, 201), repeat=2):
    record = inspect_pair(Fraction(a), Fraction(b))
    integer_histogram[record["maximum_three_primary_order"]] += 1
    if not record["admits_inherited_class_two_lift"]:
        obstructed_integer_pairs.append(record)

rationals = sorted({Fraction(s*a, b) for a in range(1, 17)
                    for b in range(1, 17) for s in (-1, 1)})
rational_histogram = Counter()
for a, b in product(rationals, repeat=2):
    record = inspect_pair(a, b)
    rational_histogram[record["maximum_three_primary_order"]] += 1
    assert record["admits_inherited_class_two_lift"]

steinberg_count = 0
for a in rationals:
    if a == 1:
        continue
    assert all(r["residue"] == 1 for r in residues(a, 1-a))
    steinberg_count += 1

selected_pairs = [
    (6, 109), (6**3, 109), (6**9, 109), (6, 109**3),
    (Fraction(1, 6), 109), (-6, 109),
    (Fraction(6, 109), Fraction(109, 6)),
    (2, 163), (2**3, 163), (2**9, 163), (2, 163**9),
    (-1, 109), (109, -108), (163, -162),
]
selected = []
for a, b in selected_pairs:
    a, b = Fraction(a), Fraction(b)
    r = inspect_pair(a, b)
    r["all_residues"] = residues(a, b)
    selected.append(r)
assert not selected[0]["admits_inherited_class_two_lift"]
assert selected[1]["admits_inherited_class_two_lift"]
assert selected[2]["admits_inherited_class_two_lift"]
assert selected[3]["admits_inherited_class_two_lift"]

cohomology_checks = []
for n in range(1, 5):
    m = 3**n
    big = 3*m
    units = [u for u in range(big) if u % 3]
    def boundary(u, k):
        return k*((u*u-1)//3) % m
    checked = 0
    for u, v, k in product(units, units, range(3)):
        assert boundary(u*v % big, k) == (boundary(u, k)+u*u*boundary(v, k)) % m
        checked += 1
    # At chi=2 a coboundary is 3z; the three differences have residues0,1,2.
    assert {boundary(2, k) % 3 for k in range(3)} == {0, 1, 2}
    small_units = [u for u in range(m) if u % 3]
    inv_twist2 = [a for a in range(m)
                  if all((u*u-1)*a % m == 0 for u in small_units)]
    inv_twist1 = [a for a in range(m)
                  if all((u-1)*a % m == 0 for u in small_units)]
    assert len(inv_twist2) == 3
    assert inv_twist1 == [0]
    cohomology_checks.append({"modulus": m, "units_represented_modulo": big,
                              "cocycle_triples_checked": checked,
                              "twist_two_invariant_count": len(inv_twist2),
                              "twist_one_invariant_count": len(inv_twist1)})

summary = {
    "criterion": "Every theta_q(a,b) has 3-primary order at most9.",
    "toric_coordinate_domain": "rational pairs Q* x Q*, mapped by pro3 Kummer",
    "quotient": "inherited cubic class2; central bracket9; not intrinsic rank10 classification",
    "positive_integer_range": [1, 200],
    "integer_pairs_checked": 200**2,
    "integer_pairs_admitting_lifts": 200**2-len(obstructed_integer_pairs),
    "integer_pairs_obstructed": len(obstructed_integer_pairs),
    "integer_histogram_by_maximum_three_primary_order": dict(sorted(integer_histogram.items())),
    "rational_height_bound": 16,
    "nonzero_signed_rationals_in_grid": len(rationals),
    "rational_pairs_checked": len(rationals)**2,
    "rational_pairs_admitting_lifts": len(rationals)**2,
    "rational_histogram_by_maximum_three_primary_order": dict(sorted(rational_histogram.items())),
    "steinberg_pairs_checked": steinberg_count,
    "central_cohomology_checks": cohomology_checks,
    "selected_pairs": selected,
    "all_obstructed_integer_pairs": obstructed_integer_pairs,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(summary, indent=2)+"\n")
printed = dict(summary)
printed.pop("all_obstructed_integer_pairs")
print(json.dumps(printed, indent=2))

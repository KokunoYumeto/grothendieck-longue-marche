#!/usr/bin/env python3
"""Exact finite certificates for A.96.

This enumerates genuine finite Galois-group data from A.57, including the
cyclotomic/quadratic compatibility at the prime 2.  It proves only its stated
finite checks; the arbitrary-radicand and initialization arguments are in
quartic_tripod_initialization_agent.tex.  It performs no prime recursion.
"""

from itertools import product
from random import Random
from math import prod

import sympy as sp


def parity(x):
    return x.bit_count() & 1


def span(generators):
    result = {0}
    for g in generators:
        result |= {x ^ g for x in tuple(result)}
    return result


def char_vector(primes, delta, weights):
    """Coordinate 0 is chi_-1, coordinate 1 is chi_2."""
    result = delta & 1
    odd = [p for p in primes if p != 2]
    for p, w in zip(primes, weights):
        if w & 1:
            result ^= 1 << (1 if p == 2 else 2 + odd.index(p))
    return result


counts = {
    "cases": 0,
    "actual_group_elements": 0,
    "literal_congruences": 0,
    "fixed_root_tuples_counted": 0,
    "negative_relation_generators": 0,
    "extra_common_field_cases": 0,
    "minus_one_cases": 0,
    "negative_relation_reductions": 0,
}


def check_case(primes, rows, label=None):
    odd = [p for p in primes if p != 2]
    rank = 2 + len(odd)
    gamma = range(1 << rank)
    wrows = [w for _, w in rows]
    deltas = [d for d, _ in rows]
    kindividual = [char_vector(primes, d, w) for d, w in rows]
    kspan = span(kindividual)
    minus_one = 1 in kspan
    negative = []
    all_relations = []
    for t in range(1 << len(rows)):
        wsum = [
            sum(wrows[i][j] for i in range(len(rows)) if (t >> i) & 1)
            for j in range(len(primes))
        ]
        if any(w & 1 for w in wsum):
            continue
        ds = sum(deltas[i] for i in range(len(rows)) if (t >> i) & 1) & 1
        rchar = char_vector(primes, 0, [w // 2 for w in wsum])
        beta = rchar ^ (2 if ds else 0)
        all_relations.append((t, ds, rchar, beta))
        if ds:
            negative.append(beta)
    predicted_chars = span(kindividual + negative)
    predicted_kernel = {
        g for g in gamma if all(parity(g & c) == 0 for c in predicted_chars)
    }
    admissible = set()
    fixed_counts = 0
    for g in gamma:
        counts["actual_group_elements"] += 1
        minus = g & 1
        two = (g >> 1) & 1
        u = {(0, 0): 1, (1, 0): 7, (0, 1): 5, (1, 1): 3}[(minus, two)]
        eps = [
            (g >> (1 if p == 2 else 2 + odd.index(p))) & 1 for p in primes
        ]
        for h in product(range(2), repeat=len(primes)):
            k = [e + 2 * hh for e, hh in zip(eps, h)]
            e_lists = []
            for delta, weights in rows:
                es = []
                for e in range(4):
                    counts["literal_congruences"] += 1
                    lhs = (u - 1) * (delta + 2 * e) + 2 * sum(
                        w * kk for w, kk in zip(weights, k)
                    )
                    if lhs % 8 == 0:
                        es.append(e)
                e_lists.append(es)
            if all(e_lists):
                admissible.add(g)
                fixed_counts += prod(map(len, e_lists))
                # Retain an actual tuple and recheck every literal equation.
                chosen = [es[0] for es in e_lists]
                for (delta, weights), e in zip(rows, chosen):
                    assert (
                        (u - 1) * (delta + 2 * e)
                        + 2 * sum(w * kk for w, kk in zip(weights, k))
                    ) % 8 == 0
    actual_h = span(admissible)
    assert actual_h == predicted_kernel, (primes, rows, actual_h, predicted_kernel)
    if minus_one:
        assert admissible == predicted_kernel
        allchars = span(kindividual + [b for _, _, _, b in all_relations])
        assert allchars == predicted_chars
        counts["minus_one_cases"] += 1
        neg_t0 = next(t for t, ds, _, _ in all_relations if ds)
        relations = {t: (ds, rc, be) for t, ds, rc, be in all_relations}
        for t, ds, rchar, beta in all_relations:
            if ds:
                continue
            tprime = t ^ neg_t0
            overlap = t & neg_t0
            abs_overlap = 0
            for i, (delta, weights) in enumerate(rows):
                if (overlap >> i) & 1:
                    abs_overlap ^= char_vector(primes, 0, weights)
            assert rchar == (
                relations[neg_t0][2] ^ relations[tprime][2] ^ abs_overlap
            )
            assert abs_overlap in kspan
            counts["negative_relation_reductions"] += 1
    else:
        assert not negative
        assert actual_h == {
            g for g in gamma if all(parity(g & c) == 0 for c in kindividual)
        }
    counts["cases"] += 1
    counts["fixed_root_tuples_counted"] += fixed_counts
    counts["negative_relation_generators"] += len(negative)
    counts["extra_common_field_cases"] += len(predicted_chars) > len(kspan)
    if label:
        print(
            f"{label}: degree K={len(kspan)}, degree B4={len(predicted_chars)}, "
            f"|Gamma|={1 << rank}, |H|={len(actual_h)}."
        )


all_two_prime_rows = [(d, w) for d in range(2) for w in product(range(4), repeat=2)]
for row in all_two_prime_rows:
    check_case((2, 3), [row])
for rows in product(all_two_prime_rows, repeat=2):
    check_case((2, 3), list(rows))

rng = Random(960416)
for primes, total, maxrows in [
    ((2, 3), 240, 4),
    ((3, 5), 160, 4),
    ((2, 3, 5), 160, 5),
    ((3, 5, 7), 80, 4),
]:
    for _ in range(total):
        rows = [
            (
                rng.randrange(2),
                tuple(rng.randrange(-5, 6) for _ in primes),
            )
            for _ in range(rng.randrange(1, maxrows + 1))
        ]
        check_case(primes, rows)

check_case((5,), [(0, (-1,)), (1, (-1,))], "A.57 +/-1/5 example")
check_case(
    (2, 11, 79),
    [(1, (-2, 1, 0)), (0, (-6, 0, 1)), (0, (0, -1, -1))],
    "A.69 three-coordinate example",
)
check_case((3, 5), [(1, (2, 0)), (0, (0, 2))], "Negative/positive square pair")

X, Y, r, k, a, b, c, z = sp.symbols("X Y r k a b c z")
identities = []
identities.append((X**2 + r) ** 2 - 2 * r * X**2 - (X**4 + r**2))
identities.append(
    (X**2 + k * Y**2) ** 2 - 2 * k * (X * Y) ** 2 - (X**4 + k**2 * Y**4)
)
# Exact cleared-denominator identity for the two-coordinate comparison.
actual = (
    (1 - c) * (a * X**4 - c)
    - a * (1 - c) ** 2 * X**4
    - a * b**2 * r**2 * Y**4
)
claimed = (
    c * (1 - c) * (a * X**4 - b * Y**4 - 1)
    + b * Y**4 * (c * (1 - c) - a * b * r**2)
)
identities.append(actual - claimed)
# The actual root-field element ((1-z^2/r)z)^2 is 2r modulo z^4+r^2.
root_identity = sp.rem(
    sp.together(((1 - z**2 / r) * z) ** 2 - 2 * r) * r**2,
    z**4 + r**2,
    z,
)
identities.append(root_identity)
for identity in identities:
    assert sp.expand(identity) == 0

squareclass_checks = 0
affine_checks = 0
from fractions import Fraction

for cc, aa, rr in product(
    [Fraction(-3, 2), Fraction(-1, 3), Fraction(2, 5), Fraction(3, 2)],
    [Fraction(-5, 3), Fraction(2, 7), Fraction(3)],
    [Fraction(1, 3), Fraction(2), Fraction(7, 5)],
):
    bb = cc * (1 - cc) / (aa * rr**2)
    kk = bb * rr / (1 - cc)
    d0, d1 = cc / aa, (cc - 1) / bb
    assert d0 * d1 == -(rr**2)
    assert (2 * kk) / (2 * rr) == d0 / rr**2
    assert aa * (1 - cc) * kk**2 == bb * cc
    squareclass_checks += 3
    for c1, c2 in [(Fraction(0), Fraction(1)), (Fraction(4, 15), Fraction(-64, 15))]:
        dd = c2 - c1
        anew, bnew, cnew = aa * dd, bb * dd, c1 + dd * cc
        assert (cnew - c1) / anew == d0
        assert (cnew - c2) / bnew == d1
        affine_checks += 2

print("All exact finite checks passed.")
for key, value in counts.items():
    print(f"{key}: {value}.")
print(f"Symbolic norm/root/cover identities: {len(identities)}.")
print(f"Exact rational squareclass/cover identities: {squareclass_checks}.")
print(f"Exact affine fibre comparisons: {affine_checks}.")
print(
    "These are finite certificates for the displayed maps and identities; "
    "the general proof and all-place initialization are in A.96."
)

#!/usr/bin/env python3
"""Exact finite audit of A120 on the actual cubic Belyi source.

Old points are recognized by their full Q2 fourth-power classes, not by
requiring the local fourth roots to be small rational numbers.  Every
pair in each sampled fibre is checked against the valuation proof.
Literal Hilbert evaluations are then checked on a deterministic spread
of pairs, all fifteen nonempty old subsets, and the printed new centres.
"""

from collections import defaultdict, Counter
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random

import sympy as sp

PUNCTURES = (Q(0), Q(1), Q(2, 3), Q(-1, 3))
SUBSETS = tuple(J for k in range(1, 5) for J in combinations(range(4), k))


def vu(x, modulus=32):
    x = Q(x)
    assert x
    a, b = x.numerator, x.denominator
    v = 0
    while a % 2 == 0:
        a //= 2
        v += 1
    while b % 2 == 0:
        b //= 2
        v -= 1
    return v, (a % modulus)*pow(b % modulus, -1, modulus) % modulus


def fourth_class(x):
    v, u = vu(x, 16)
    return v % 4, u


def hilbert(a, b):
    va, ua = vu(a, 8)
    vb, ub = vu(b, 8)
    bit = (((ua-1)//2)*((ub-1)//2)
           + va*((ub*ub-1)//8) + vb*((ua*ua-1)//8)) % 2
    return bit


def square_root_classes(x):
    v, u = vu(x)
    if v % 2 or u % 8 != 1:
        return ()
    r = Q(2)**(v//2)*{1: 1, 9: 3, 17: 7, 25: 5}[u]
    return (r, -r)


def profile(z):
    vals = tuple(vu(z-a)[0] for a in PUNCTURES)
    if vals[0] < 0:
        assert len(set(vals)) == 1
        return "infinity", vals
    if vals[0] >= 2:
        assert vals == (vals[0], 0, 1, 0)
        return "zero", vals
    if vals[2] >= 2:
        assert vals == (1, 0, vals[2], 0)
        return "two_thirds", vals
    if vals == (0, 1, 0, 1):
        return "odd_middle", vals
    if vals[1] >= 3:
        assert vals == (0, vals[1], 0, 2)
        return "one", vals
    assert vals[3] >= 3 and vals == (0, 2, 0, vals[3])
    return "minus_third", vals


def symbolic_checks():
    R, T, c, a, b, d, X = sp.symbols("R T c a b d X")
    assert sp.factor(((1/T-1/b)/(1/R-1/b))
                     - (R/T)*(T-b)/(R-b)) == 0
    assert sp.factor(((1/T-1/c)/(1/R-1/c))
                     - ((T-c)/(R-c))*R/T) == 0
    assert sp.factor((((T-a)/d-(b-a)/d)/((R-a)/d-(b-a)/d))
                     - (T-b)/(R-b)) == 0
    assert sp.expand((X*X+a)**2-2*a*X*X-(X**4+a*a)) == 0
    assert sp.expand((1+a)**2-2*a-(1+a*a)) == 0
    D = sp.symbols("D0:4")
    new = (1/D[0], *(D[j]/D[0] for j in range(1, 4)))
    for J in SUBSETS:
        jp = [i for i in J if i]
        if len(J) % 2:
            jp.append(0)
        old_product = sp.prod(D[i] for i in J)
        new_product = sp.prod(new[i] for i in jp)
        assert sp.factor(new_product-old_product*D[0]**(-2*((len(J)+1)//2))) == 0
        assert jp
    assert pow(3, -1, 16) == 11
    assert -pow(3, -1, 16) % 16 == 5
    print("PASS: five exact cover/norm identities, all15 subset transports, and both mod16 cross-disc exclusions.")


def main():
    symbolic_checks()
    offsets = {sign*Q(2)**e*u for sign, e, u in
               product((-1, 1), range(-8, 12), (1, 3, 5, 7, 9, 11, 13, 15))}
    centres = sorted({a+t for a, t in product(PUNCTURES, offsets)}
                     - set(PUNCTURES))
    fibres = defaultdict(list)
    for z in centres:
        profile(z)
        fibres[tuple(fourth_class(z-a) for a in PUNCTURES)].append(z)
    grouped_pairs = defaultdict(list)
    pairs_checked = 0
    for fibre in fibres.values():
        for R, T in combinations(fibre, 2):
            pairs_checked += 1
            row_R, vals_R = profile(R)
            row_T, vals_T = profile(T)
            assert row_R == row_T
            s = vu(T-R)[0]
            if vals_R == vals_T:
                assert s >= max(vals_R)+4
                grouped_pairs["equal"].append((R, T))
            elif row_R == "infinity":
                assert min(-vals_R[0], -vals_T[0]) >= 4
                grouped_pairs["infinity"].append((R, T))
            else:
                index, delta = {"zero": (0, 1), "two_thirds": (2, 1),
                                "one": (1, 2), "minus_third": (3, 2)}[row_R]
                assert s == min(vals_R[index], vals_T[index])
                assert s >= delta+4
                grouped_pairs[row_R].append((R, T))
    print(f"Old-point classes: {len(centres)} actual rational centres, "
          f"{len(fibres)} quartic fibres, {pairs_checked} literal local-point pairs.")
    print("Every pair satisfies the exact valuation partition and depth bounds:",
          dict(sorted((k, len(v)) for k, v in grouped_pairs.items())))

    rng = Random(118120)
    chosen = []
    for kind, pairs in sorted(grouped_pairs.items()):
        rng.shuffle(pairs)
        chosen.extend((kind, *pair) for pair in pairs[:32])
    c_offsets = {sign*Q(2)**e*u for sign, e, u in
                 product((-1, 1), range(-5, 10), (1, 3, 5))}
    new_centres = sorted({a+t for a, t in product(PUNCTURES, c_offsets)}
                         - set(PUNCTURES))
    evaluations = local_relations = 0
    case_checks = Counter()
    for kind, R, T in chosen:
        for c in new_centres:
            if c in (R, T):
                continue
            D = tuple((c-a)/(R-a) for a in PUNCTURES)
            f = (T-c)/(R-c)
            for J in SUBSETS:
                product_D = Q(1)
                for j in J:
                    product_D *= D[j]
                roots = square_root_classes(-product_D)
                if roots:
                    local_relations += 1
                for r in roots:
                    evaluations += 1
                    case_checks[kind] += 1
                    assert hilbert(f, 2*r) == 0, (R, T, c, J, r)
    print(f"Subset evaluation audit: {len(chosen)} spread pairs, "
          f"{len(new_centres)} new centres, all15 nonempty subsets, "
          f"{local_relations} actual local negative-square relations, "
          f"{evaluations} Hilbert evaluations including both root signs.")
    print("Evaluation counts by proof case:", dict(sorted(case_checks.items())))
    print("PASS: all exact finite checks. The complete all-point and finite-initialization claims are proved in A120.")


if __name__ == "__main__":
    main()

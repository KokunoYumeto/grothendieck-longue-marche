#!/usr/bin/env python3
"""Exact local quartic search on A.114's actual five-punctured source.

A local negative-subset relation is tested before any claim that its root
is rational globally.  A local witness is printed with that distinction.
No negative finite search is treated as a general constancy theorem.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import gcd, isqrt
from tripod_eighth_search import valuation_unit, hilbert

PUNCTURES = (Q(0), Q(1), Q(2, 3), Q(-1, 3))
SUBSETS = list(combinations(PUNCTURES, 3)) + [PUNCTURES]


def fourth(x, p):
    if not x:
        return False
    v, u = valuation_unit(x, p, 32 if p == 2 else p)
    if v % 4:
        return False
    return u % 16 == 1 if p == 2 else pow(u, (p-1)//gcd(4, p-1), p) == 1


def local_square_root_class(x, p):
    if not x:
        return None
    v, u = valuation_unit(x, p, 32 if p == 2 else p)
    if v % 2:
        return None
    if p == 2:
        if u % 8 != 1:
            return None
        root = {1: 1, 9: 3, 17: 7, 25: 5}[u]
    else:
        roots = [z for z in range(1, p) if z*z % p == u]
        if not roots:
            return None
        root = roots[0]
    return Q(p)**(v//2)*root


def rational_square(x):
    return x > 0 and isqrt(x.numerator)**2 == x.numerator and isqrt(x.denominator)**2 == x.denominator


def subset_product(x, subset):
    out = Q(1)
    for c in subset:
        out *= x-c
    return out


def search(p):
    units = (1, 3, 5, 7, 11, 15) if p == 2 else tuple(a for a in range(1, min(2*p, 18)) if a % p)
    depth = range(-3, 9) if p == 2 else range(-2, 5)
    offsets = {sign*Q(p)**e*u for sign, e, u in product((-1, 1), depth, units)}
    centres = sorted(({c+x for c, x in product(PUNCTURES, offsets)} | offsets) - set(PUNCTURES))
    roots = [Q(p)**e*u for e, u in product(range(-2, 3), units[:4])]
    c_values = centres
    f_values = {c: tuple(subset_product(c, S) for S in SUBSETS) for c in c_values}
    covers = old_points = local_sources = evaluations = rational_relations = 0
    for R in centres:
        Ts = []
        for X in roots:
            T = R*X**4
            if T == R or T in PUNCTURES:
                continue
            if all(fourth((T-c)/(R-c), p) for c in PUNCTURES):
                Ts.append((T, X))
        if not Ts:
            continue
        covers += 1
        old_points += len(Ts)
        FR = tuple(subset_product(R, S) for S in SUBSETS)
        for c in c_values:
            if c == R:
                continue
            for index, subset in enumerate(SUBSETS):
                D = -f_values[c][index]/FR[index]
                # A global negative-square subset relation requires D>0.
                # The local root itself is certified independently below.
                if D <= 0:
                    continue
                r = local_square_root_class(D, p)
                if r is None:
                    continue
                local_sources += 1
                global_relation = rational_square(D)
                rational_relations += global_relation
                for T, X in Ts:
                    if T == c:
                        continue
                    f = (T-c)/(R-c)
                    for sign in (-1, 1):
                        evaluations += 1
                        if hilbert(f, 2*sign*r, p):
                            print("LOCAL WITNESS on the exact A114 source", flush=True)
                            for name, value in [("p",p),("R",R),("T",T),("new c",c),
                                                ("subset",subset),("negative product r²",D),
                                                ("r local squareclass",sign*r),("normalized f",f),
                                                ("global rational relation",global_relation)]:
                                print(f"{name}: {value}", flush=True)
                            print("All four old ratios:",[(T-a)/(R-a) for a in PUNCTURES],flush=True)
                            print(f"covers={covers},old_points={old_points},local_sources={local_sources},evaluations={evaluations},rational_relations={rational_relations}",flush=True)
                            return True
    print(f"p={p}: covers={covers},actual_old_points={old_points},local_sources={local_sources},evaluations={evaluations},global_rational_relations={rational_relations}; no witness in this finite search.",flush=True)
    return False


if __name__ == "__main__":
    for p in (2, 3, 5, 7, 11, 13):
        if search(p):
            break
    print("The executed search establishes only the printed exact local results.",flush=True)

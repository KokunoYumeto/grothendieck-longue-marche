#!/usr/bin/env python3
"""Complementary exact search for A128's global constant.

Only one pointed coefficient is multiplied by q^2.  The quadratic old
cover retains its rational point, via U_j=q X_j^2.  The quartic twist
is identified with the pointed cover over Q(sqrt(q)) by X'_j=sqrt(q)X_j.
Missing searched points are not reported as local impossibility.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import sympy as sp

from arbitrary_harmonic_twist_search import (
    BOUNDARIES, actual, fourth, hilbert, local, pset, stringify
)


DATA = [
    (138, (150, 720), (162, 1080)),
    (154, (-98, 1176), (350, 5880)),
    (210, (-150, 1800), (-90, 1800)),
    (330, (-275, 3025), (-150, 3600)),
    (426, (588, 9828), (726, 15840)),
    (434, (448, 2352), (722, 15504)),
    (546, (-507, 4563), (-468, 6084)),
    (651, (-525, 8820), (-363, 10296)),
    (658, (1458, 49680), (1792, 70560)),
    (1146, (2028, 75348), (5202, 365976)),
    (1155, (-605, 24200), (-539, 23716)),
    (1254, (-912, 25992), (-1058, 21896)),
]


def source_data():
    result = set()
    for d, P, Q in DATA:
        for x, y in (P, Q):
            assert y*y == x*x*x-d*d*x
        R = (1+F(P[0], d))/2
        c = (1-F(Q[0], d))/2
        rho = abs(F(Q[1], P[1]))
        result.add((R, c, rho))
    for R in (F(1,3), F(1,7), F(2,11), F(3,10), F(3,22),
              F(5,12), F(2), F(3), F(4), F(32,81)):
        result.add((R, 1-R, F(1)))
    for R, c, rho in result:
        def polynomial(z):
            return z*(z-1)*(z-F(1,2))
        assert polynomial(c)/polynomial(R) == -rho*rho
    return sorted(result)


def witness(R, a, p, c):
    if actual(R, a, p, c):
        return R
    return local(a, p, c)


def main():
    counts = dict(covers=0, dyadic=0, support_local=0,
                  small_local=0, nonzero=0, certified=0)
    results = []
    qs = [q for q in range(2, 401)
          if all(e == 1 for e in sp.factorint(q).values())]
    small = list(sp.primerange(3, 151))
    allgood = list(sp.primerange(3, 4501))
    for (R, c, rho), j, q in product(source_data(), range(3), qs):
        a = [R-b for b in BOUNDARIES]
        a[j] *= q*q
        a = tuple(a)
        r, character = rho/q, 2*rho/q
        D = tuple((c-b)/aa for b, aa in zip(BOUNDARIES, a))
        assert D[0]*D[1]*D[2] == -r*r
        counts["covers"] += 1
        if counts["covers"] % 1000 == 0:
            print("progress", counts, flush=True)
        T2 = witness(R, a, 2, c)
        if T2 is None:
            continue
        counts["dyadic"] += 1
        witnesses = {2: T2}
        S = {2}
        for z in (*a, *(c-b for b in BOUNDARIES), character):
            S.update(pset(z))
        for p in sorted(S-{2}):
            T = witness(R, a, p, c)
            if T is None:
                break
            witnesses[p] = T
        else:
            counts["support_local"] += 1
            for p in small:
                if p in witnesses:
                    continue
                T = witness(R, a, p, c)
                if T is None:
                    break
                witnesses[p] = T
            else:
                counts["small_local"] += 1
                inv = {p: hilbert(witnesses[p]-c, character, p)
                       for p in sorted(S)}
                # rho,q>0, so the character is split over R.
                if sum(inv.values()) % 2:
                    counts["nonzero"] += 1
                    row = dict(R=R, c=c, rho=rho, j=j, q=q, a=a,
                               D=D, character=character, invariants=inv)
                    print("NONZERO SUPPORT SUM", stringify(row), flush=True)
                    for p in allgood:
                        if p in witnesses:
                            continue
                        T = witness(R, a, p, c)
                        if T is None:
                            print("NO SEARCHED WITNESS", p, flush=True)
                            break
                        witnesses[p] = T
                    else:
                        counts["certified"] += 1
                        row["local_T"] = witnesses
                        results.append(stringify(row))
                        print("ALL-PLACE WITNESS", stringify(
                            {k:v for k,v in row.items() if k!="local_T"}), flush=True)
                        Path(__file__).with_name(
                            "harmonic_square_twist_search_data.json").write_text(
                                json.dumps(dict(counts=counts, candidates=results),
                                           indent=2)+"\n")
                        return
    print("SEARCH COMPLETE", counts, flush=True)
    print("Zero retained sums are a finite search result; no absence theorem is inferred.",
          flush=True)
    Path(__file__).with_name("harmonic_square_twist_search_data.json").write_text(
        json.dumps(dict(counts=counts, candidates=results), indent=2)+"\n")


if __name__ == "__main__":
    main()

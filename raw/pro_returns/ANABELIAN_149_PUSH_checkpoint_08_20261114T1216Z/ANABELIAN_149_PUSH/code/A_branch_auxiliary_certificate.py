#!/usr/bin/env python3
"""Exact matrix/permutation certificate for the A.29m candidate.

Only Python's standard library is used. All fields are prime fields and all
group elements are determinant-one matrices modulo {I,-I}. This is a finite
certificate for the displayed branch triples and quotient genera, not a
substitute for the geometric proof in the accompanying audit note.
"""
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path
import json


PRIMES = (7, 11, 13, 17, 19, 23, 29, 31, 37)
EXPECTED = {
    7: (168, 3, 21, 0), 11: (660, 26, 55, 1),
    13: (1092, 50, 78, 0), 17: (2448, 133, 136, 1),
    19: (3420, 196, 171, 1), 23: (6072, 375, 253, 2),
    29: (12180, 806, 406, 2), 31: (14880, 1001, 465, 2),
    37: (25308, 1768, 666, 2),
}


def certificate(r):
    def canon(m):
        m = tuple(v % r for v in m)
        assert (m[0] * m[3] - m[1] * m[2]) % r == 1
        return min(m, tuple(-v % r for v in m))

    def mul(a, b):
        return canon((a[0]*b[0] + a[1]*b[2],
                      a[0]*b[1] + a[1]*b[3],
                      a[2]*b[0] + a[3]*b[2],
                      a[2]*b[1] + a[3]*b[3]))

    def inv(a):
        return canon((a[3], -a[1], -a[2], a[0]))

    identity = canon((1, 0, 0, 1))
    s = canon((0, -1, 1, 0))
    t = canon((1, 1, 0, 1))
    x, y, z = s, mul(s, t), inv(t)

    def order(a):
        b, n = identity, 0
        while True:
            b, n = mul(b, a), n + 1
            if b == identity:
                return n

    assert (order(x), order(y), order(z)) == (2, 3, r)
    assert mul(mul(x, y), z) == identity

    # Exhaustive generation is independent of the formula for |PSL_2(F_r)|.
    group = {identity}
    queue = deque((identity,))
    while queue:
        a = queue.popleft()
        for b in (s, t):
            c = mul(a, b)
            if c not in group:
                group.add(c)
                queue.append(c)
    assert len(group) == r * (r*r - 1) // 2

    # Represent infinity by r. The action is exact on P^1(F_r).
    def act(a, u):
        if u == r:
            numerator, denominator = a[0], a[2]
        else:
            numerator = (a[0]*u + a[1]) % r
            denominator = (a[2]*u + a[3]) % r
        return r if denominator == 0 else numerator * pow(denominator, -1, r) % r

    def cycle_lengths(a):
        unseen, lengths = set(range(r+1)), []
        while unseen:
            start = min(unseen)
            u, n = start, 0
            while True:
                assert u in unseen
                unseen.remove(u)
                n += 1
                u = act(a, u)
                if u == start:
                    break
            lengths.append(n)
        return sorted(lengths)

    borel = {a for a in group if act(a, r) == r}
    assert len(borel) == r * (r-1) // 2
    assert all(a[2] == 0 for a in borel)
    assert {act(a, r) for a in group} == set(range(r+1))
    assert [a for a in group if all(act(a, u) == u for u in (0, 1, r))] == [identity]

    cycles = [cycle_lengths(a) for a in (x, y, z)]
    f2 = 2 if r % 4 == 1 else 0
    f3 = 2 if r % 3 == 1 else 0
    assert Counter(cycles[0]) == Counter({1: f2, 2: (r+1-f2)//2})
    assert Counter(cycles[1]) == Counter({1: f3, 3: (r+1-f3)//3})
    assert cycles[2] == [1, r]
    genus_h = 1 + Fraction(len(group), 2) * (
        -2 + (1-Fraction(1, 2)) + (1-Fraction(1, 3)) + (1-Fraction(1, r)))
    genus_x = 1 + Fraction(-2*(r+1) + sum(r+1-len(c) for c in cycles), 2)
    assert genus_h.denominator == genus_x.denominator == 1
    assert genus_x == 1 + Fraction(r-11-3*f2-4*f3, 12)
    actual = (len(group), int(genus_h), len(borel), int(genus_x))
    assert actual == EXPECTED[r]

    # A direct commutator giving a nontrivial unipotent establishes perfectness
    # together with the elementary-matrix generation proved in the note.
    a = next(a for a in range(1, r) if a*a % r != 1)
    diagonal = canon((a, 0, 0, pow(a, -1, r)))
    comm = mul(mul(mul(diagonal, t), inv(diagonal)), inv(t))
    assert comm == canon((1, a*a-1, 0, 1))
    assert order(comm) == r

    extra = None
    if r == 7:
        subgroup = {identity}
        a = identity
        for _ in range(1, r):
            a = mul(a, t)
            subgroup.add(a)
        normalizer = {a for a in group if mul(mul(a, t), inv(a)) in subgroup}
        assert normalizer == borel
        fixed_points = len(normalizer) // r
        cyclic_quotient_genus = 1 + Fraction(2*genus_h-2-fixed_points*(r-1), 2*r)
        assert fixed_points == 3 and cyclic_quotient_genus == 0
        extra = {"order_seven_normalizer": len(normalizer),
                 "geometric_fixed_points": fixed_points,
                 "cyclic_quotient_genus": int(cyclic_quotient_genus)}

    return {"r": r, "group_order": len(group), "source_genus": int(genus_h),
            "borel_order": len(borel), "borel_quotient_genus": int(genus_x),
            "inertia_orders": [2, 3, r],
            "cycle_lengths": dict(zip(("order_2", "order_3", "order_r"), cycles)),
            "fixed_counts": {"order_2": f2, "order_3": f3},
            "klein_cyclic_check": extra}


def main():
    results = [certificate(r) for r in PRIMES]
    output = {"status": "PASS", "method": "exhaustive projective matrix groups and exact inertia permutations",
              "all_group_orders_verified": True, "all_generating_triples_verified": True,
              "all_quotient_genera_verified": True, "results": results}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

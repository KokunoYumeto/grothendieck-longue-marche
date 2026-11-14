#!/usr/bin/env python3
"""Independent direct-permutation check of the A.29m genus table."""
import json
from fractions import Fraction
from pathlib import Path

rows = []
for r in (7, 11, 13, 17, 19, 23, 29, 31, 37):
    points = list(range(r)) + [None]

    def inverse(a):
        return None if a == 0 else (0 if a is None else pow(a, -1, r))

    def x(a):
        z = inverse(a)
        return None if z is None else -z % r

    def y(a):
        return x(None if a is None else (a + 1) % r)

    def z(a):
        return None if a is None else (a - 1) % r

    assert all(x(y(z(a))) == a for a in points)
    cycles = []
    for action in (x, y, z):
        unseen, lengths = set(points), []
        while unseen:
            a, n = next(iter(unseen)), 0
            while a in unseen:
                unseen.remove(a)
                a, n = action(a), n + 1
            lengths.append(n)
        cycles.append(sorted(lengths))
    source_genus = 1 + Fraction((r * r - 1) * (r - 6), 24)
    quotient_genus = 1 + Fraction(r + 1 - sum(map(len, cycles)), 2)
    assert source_genus.denominator == quotient_genus.denominator == 1
    assert 0 <= quotient_genus <= 2
    rows.append(dict(r=r, source_genus=int(source_genus),
                     borel_quotient_genus=int(quotient_genus), cycles=cycles))
result = dict(status="PASS", method="direct permutations, independent of matrix enumeration", results=rows)
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

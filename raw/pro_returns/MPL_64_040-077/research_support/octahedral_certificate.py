#!/usr/bin/env python3
"""Exhaustive finite-field checks for the frozen cote64 octahedral assertions.

Uses no external packages.  F_9 is F_3[t]/(t^2+1), encoded a+3*b.
Run from any directory; JSON is written to stdout.  This checks concrete
fibres, not the relative descent theorem.  The characteristic-five objection
and witness were already given by Hua, modernised reading of cote64, §II.
"""

from datetime import datetime, timezone
from itertools import product
import json


class Field:
    def __init__(self, p, degree=1):
        assert degree == 1 or (p, degree) == (3, 2)
        self.p, self.degree, self.q = p, degree, p**degree
        self.elements = tuple(range(self.q))

    def add(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x + y) % p
        return (x % p + y % p) % p + p * ((x // p + y // p) % p)

    def neg(self, x):
        return self.add_inverse[x]

    def mul(self, x, y):
        p = self.p
        if self.degree == 1:
            return (x * y) % p
        a, b, c, d = x % p, x // p, y % p, y // p
        return (a * c - b * d) % p + p * ((a * d + b * c) % p)

    def prepare(self):
        self.add_inverse = {
            x: next(y for y in self.elements if self.add(x, y) == 0)
            for x in self.elements
        }
        self.inverse = {
            x: next(y for y in self.elements if self.mul(x, y) == 1)
            for x in self.elements if x
        }
        # Check the field axioms used by the computation, including F_9.
        for x, y, z in product(self.elements, repeat=3):
            assert self.add(self.add(x, y), z) == self.add(x, self.add(y, z))
            assert self.mul(self.mul(x, y), z) == self.mul(x, self.mul(y, z))
            assert self.mul(x, self.add(y, z)) == self.add(self.mul(x, y), self.mul(x, z))
            assert self.add(x, y) == self.add(y, x)
            assert self.mul(x, y) == self.mul(y, x)

    def sub(self, x, y):
        return self.add(x, self.neg(y))

    def norm(self, m):
        first = next(x for x in m if x)
        scale = self.inverse[first]
        return tuple(self.mul(scale, x) for x in m)

    def det(self, m):
        a, b, c, d = m
        return self.sub(self.mul(a, d), self.mul(b, c))

    def mmul(self, m, n):
        a, b, c, d = m
        e, f, g, h = n
        return self.norm((
            self.add(self.mul(a, e), self.mul(b, g)),
            self.add(self.mul(a, f), self.mul(b, h)),
            self.add(self.mul(c, e), self.mul(d, g)),
            self.add(self.mul(c, f), self.mul(d, h)),
        ))

    def minv(self, m):
        a, b, c, d = m
        return self.norm((d, self.neg(b), self.neg(c), a))

    def action(self, m, x):
        a, b, c, d = m
        if x == self.q:  # infinity
            return self.q if c == 0 else self.mul(a, self.inverse[c])
        top = self.add(self.mul(a, x), b)
        bottom = self.add(self.mul(c, x), d)
        return self.q if bottom == 0 else self.mul(top, self.inverse[bottom])


def partition_key(pairs):
    return tuple(sorted(tuple(sorted(pair)) for pair in pairs))


def matchings(points):
    if not points:
        yield ()
        return
    first, rest = points[0], points[1:]
    for j, second in enumerate(rest):
        for tail in matchings(rest[:j] + rest[j + 1:]):
            yield partition_key(((first, second),) + tail)


def check(p, degree=1):
    f = Field(p, degree)
    f.prepare()
    q = f.q
    one, minus_one = 1, f.neg(1)
    i = next(x for x in f.elements if f.mul(x, x) == minus_one)
    identity = f.norm((1, 0, 0, 1))
    klein = frozenset((
        identity,
        f.norm((minus_one, 0, 0, 1)),
        f.norm((0, 1, 1, 0)),
        f.norm((0, minus_one, 1, 0)),
    ))
    delta = frozenset((0, q, one, minus_one, i, f.neg(i)))
    assert len(delta) == 6
    standard_pairs = partition_key(((0, q), (one, minus_one), (i, f.neg(i))))
    projective_group = {
        f.norm(m) for m in product(f.elements, repeat=4) if f.det(m)
    }
    assert len(projective_group) == q * (q * q - 1)
    assert all(f.mmul(m, f.minv(m)) == identity for m in projective_group)
    actions = {
        m: tuple(f.action(m, x) for x in range(q + 1)) for m in projective_group
    }
    assert all(len(set(a)) == q + 1 for a in actions.values())
    full = {
        m for m in projective_group
        if frozenset(actions[m][x] for x in delta) == delta
    }
    normalizer = {
        m for m in projective_group
        if frozenset(f.mmul(f.mmul(m, h), f.minv(m)) for h in klein) == klein
    }
    centralizer = {
        m for m in projective_group
        if all(f.mmul(m, h) == f.mmul(h, m) for h in klein)
    }
    assert centralizer == set(klein)
    assert normalizer <= full
    assert len(normalizer) == 24
    pair_action = lambda m, pairs: partition_key(
        (actions[m][x] for x in pair) for pair in pairs
    )
    pair_stabilizer = {m for m in full if pair_action(m, standard_pairs) == standard_pairs}
    assert pair_stabilizer == normalizer
    normalizer_generators = set(klein) | {
        f.norm((i, 0, 0, 1)),
        f.norm((1, 1, 1, minus_one)),
    }
    closure = {identity}
    while True:
        larger = closure | {f.mmul(m, n) for m in closure for n in normalizer_generators}
        if larger == closure:
            break
        closure = larger
    assert closure == normalizer
    # The four antipodal pairs of triangular faces give the faithful S_4 action.
    faces = [frozenset(face) for face in product(*standard_pairs)]
    face_pairs = {
        frozenset((face, delta - face)) for face in faces
    }
    assert len(face_pairs) == 4
    ordered_face_pairs = sorted(face_pairs, key=lambda fp: sorted(sorted(t) for t in fp))
    face_pair_index = {fp: j for j, fp in enumerate(ordered_face_pairs)}
    induced = set()
    for m in normalizer:
        induced.add(tuple(face_pair_index[frozenset(
            frozenset(actions[m][x] for x in face) for face in fp
        )] for fp in ordered_face_pairs))
    assert len(induced) == 24
    all_matchings = sorted(set(matchings(tuple(sorted(delta)))))
    assert len(all_matchings) == 15
    matching_stabilizers = [
        len([m for m in full if pair_action(m, pairs) == pairs])
        for pairs in all_matchings
    ]
    regular_matchings = [pairs for pairs, n in zip(all_matchings, matching_stabilizers) if n == 24]
    regular_orbit = {pair_action(m, standard_pairs) for m in full}
    assert set(regular_matchings) == regular_orbit
    point_pair_fixer = {
        m for m in full if actions[m][q] == q and actions[m][minus_one] == minus_one
    }
    axis_pointwise_fixer = {
        m for m in full if actions[m][q] == q and actions[m][0] == 0
    }
    axis_setwise_fixer = {
        m for m in full if {actions[m][q], actions[m][0]} == {q, 0}
    }
    result = {
        "field": f"F_{q}",
        "characteristic": p,
        "encoding": "integers mod p" if degree == 1 else "a+3*b means a+b*t; t^2=-1",
        "infinity_encoding": q,
        "chosen_i": i,
        "pgl2_order": len(projective_group),
        "six_point_stabilizer_order": len(full),
        "klein_normalizer_order": len(normalizer),
        "klein_centralizer_order": len(centralizer),
        "opposition_preserving_stabilizer_order": len(pair_stabilizer),
        "faithful_action_on_four_opposite_face_pairs_order": len(induced),
        "fixer_of_infinity_and_minus_one_order": len(point_pair_fixer),
        "vertex_stabilizer_in_full_group_order": len([m for m in full if actions[m][q] == q]),
        "axis_pointwise_fixer_in_full_group_order": len(axis_pointwise_fixer),
        "axis_setwise_fixer_in_full_group_order": len(axis_setwise_fixer),
        "matching_stabilizer_order_histogram": {
            str(n): matching_stabilizers.count(n) for n in sorted(set(matching_stabilizers))
        },
        "regular_opposition_partitions": regular_matchings,
        "regular_opposition_orbit_size": len(regular_orbit),
    }
    if p == 5:
        witness = f.norm((2, 1, 0, 1))
        assert witness in point_pair_fixer and witness not in normalizer
        result["Hua_char5_witness"] = {
            "formula": "z -> 2*z + 1",
            "action_on_0_1_2_3_4_infinity": actions[witness],
            "image_of_standard_opposition": pair_action(witness, standard_pairs),
            "matrix": witness,
        }
        matching_index = {pairs: j for j, pairs in enumerate(regular_matchings)}
        action_on_five = {
            tuple(matching_index[pair_action(m, pairs)] for pairs in regular_matchings)
            for m in full
        }
        assert len(action_on_five) == 120
        result["faithful_action_on_five_regular_structures_order"] = len(action_on_five)
    if degree == 2:
        rational_normalizer = [m for m in normalizer if all(x < p for x in m)]
        assert len(rational_normalizer) == 8
        result["normalizer_F3_rational_points_order"] = len(rational_normalizer)
    return result


if __name__ == "__main__":
    checks = [check(3, 2), check(5), check(13)]
    assert [x["six_point_stabilizer_order"] for x in checks] == [24, 120, 24]
    assert [x["regular_opposition_orbit_size"] for x in checks] == [1, 5, 1]
    print(json.dumps({
        "statement_ids": ["OCT-S02", "OCT-S03", "OCT-S03R", "OCT-S04", "OCT-S04R", "OCT-S05", "OCT-S09"],
        "run_utc": datetime.now(timezone.utc).isoformat(),
        "checked_by": "GPT-6 Astra Pro /root/octahedral_checks, Python exhaustive enumeration",
        "cases": checks,
        "result": "all assertions passed",
    }, indent=2))

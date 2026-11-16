#!/usr/bin/env python3
"""Exact permutation check for the concrete SL4 tori in the companion record."""
from functools import reduce
from itertools import permutations
from math import gcd
import json

r = (3, 1, -1, -3)
a = (1, 2, -7, 4)

def quotient_coordinates(v):
    """Z^4 / Z(1,1,1,1) -> Z^3, in an explicit integral basis."""
    return tuple(v[i] - v[3] for i in range(3))

def negate(v):
    return tuple(-x for x in v)

qa = quotient_coordinates(a)
primitive_gcd = reduce(gcd, (abs(x) for x in qa))
assert sum(r) == 0 and sum(a) == 0
assert sum(x * y for x, y in zip(a, r)) == 0
assert primitive_gcd == 1

rows = []
stab_r = []
stab_a = []
intersection = []
for p in permutations(range(4)):
    pr = tuple(r[i] for i in p)
    pa = tuple(a[i] for i in p)
    r_sign = 1 if pr == r else -1 if pr == negate(r) else 0
    qpa = quotient_coordinates(pa)
    a_sign = 1 if qpa == qa else -1 if qpa == negate(qa) else 0
    sum_zero_sign = 1 if pa == a else -1 if pa == negate(a) else 0
    assert a_sign == sum_zero_sign
    label = tuple(i + 1 for i in p)
    if r_sign:
        stab_r.append(label)
    if a_sign:
        stab_a.append(label)
    if r_sign and a_sign:
        intersection.append(label)
    rows.append({
        "permutation_coordinate_list": label,
        "permuted_r": pr,
        "r_line_sign": r_sign,
        "permuted_a": pa,
        "a_quotient_coordinates": qpa,
        "a_character_line_sign": a_sign,
    })

assert len(rows) == 24
assert stab_r == [(1, 2, 3, 4), (4, 3, 2, 1)]
assert stab_a == [(1, 2, 3, 4)]
assert intersection == [(1, 2, 3, 4)]

result = {
    "r": r,
    "a": a,
    "sum_r": sum(r),
    "sum_a": sum(a),
    "a_dot_r": sum(x * y for x, y in zip(a, r)),
    "a_quotient_coordinates": qa,
    "primitive_character_gcd": primitive_gcd,
    "permutations_checked": len(rows),
    "r_line_stabilizer": stab_r,
    "a_character_line_stabilizer": stab_a,
    "intersection": intersection,
    "all_checks_passed": True,
    "rows": rows,
}
print(json.dumps(result, indent=2))

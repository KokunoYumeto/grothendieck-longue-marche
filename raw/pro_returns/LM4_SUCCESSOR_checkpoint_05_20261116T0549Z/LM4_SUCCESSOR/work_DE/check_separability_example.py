#!/usr/bin/env python3
"""Exact finite witness for the Minasyan product/intersection counterexample.

No external dependencies.  Elements of F_8 are bit vectors modulo
u^3+u+1.  Matrices are row-major 4-tuples.  The finite quotient
SL_2(Z) -> PSL_2(F_8) kills the central involution and factors through
PSL_2(Z) = C_2 * C_3.
"""
from collections import deque
from itertools import product
from pathlib import Path
import json


def field_mul(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011
    return value


def matrix_mul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (field_mul(a, e) ^ field_mul(b, g),
            field_mul(a, f) ^ field_mul(b, h),
            field_mul(c, e) ^ field_mul(d, g),
            field_mul(c, f) ^ field_mul(d, h))


IDENTITY = (1, 0, 0, 1)


def determinant(x):
    a, b, c, d = x
    return field_mul(a, d) ^ field_mul(b, c)


def inverse(x):
    assert determinant(x) == 1
    a, b, c, d = x
    return (d, b, c, a)


def generated(generators):
    generators = tuple(sorted(set(generators)))
    result = {IDENTITY}
    queue = deque([IDENTITY])
    while queue:
        x = queue.popleft()
        for y in generators:
            z = matrix_mul(x, y)
            if z not in result:
                result.add(z)
                queue.append(z)
    return result


def order(x):
    y = IDENTITY
    for n in range(1, 505):
        y = matrix_mul(y, x)
        if y == IDENTITY:
            return n
    raise AssertionError("Order exceeds the enumerated group order")


def main():
    for a in range(1, 8):
        assert sum(field_mul(a, b) == 1 for b in range(1, 8)) == 1
    assert field_mul(2, 5) == 1
    group = {x for x in product(range(8), repeat=4) if determinant(x) == 1}
    assert len(group) == 504
    a = (1, 1, 0, 1)
    b = (0, 5, 2, 1)
    assert (order(a), order(b), order(matrix_mul(a, b))) == (2, 3, 7)
    assert generated([a, b]) == group
    print("Field: F_2[u]/(u^3+u+1), u=2, u^{-1}=5")
    print("a =", a, "b =", b)
    print("orders (a,b,ab) = (2,3,7)")
    print("SL_2(F_8) = PSL_2(F_8): enumerated order =", len(group))
    print("<a,b> equals the entire enumerated group: PASS")

    unclassified = set(group)
    classes = []
    while unclassified:
        representative = min(unclassified)
        conjugacy_class = {
            matrix_mul(g, matrix_mul(representative, inverse(g))) for g in group
        }
        assert conjugacy_class <= unclassified
        unclassified -= conjugacy_class
        normal_closure_size = len(generated(conjugacy_class))
        classes.append({"representative": representative,
                        "order": order(representative),
                        "class_size": len(conjugacy_class),
                        "normal_closure_size": normal_closure_size})
        if representative != IDENTITY:
            assert normal_closure_size == 504
    print("Conjugacy class sizes =", sorted(x["class_size"] for x in classes))
    print("Normal closure of every nonidentity conjugacy class has order504: PASS")
    print("Thus the finite quotient is nonabelian simple: PASS")

    # A nonabelian simple congruence quotient of SL_2(Z) is PSL_2(F_p)
    # for a prime p>=5.  For p>=11 its order exceeds504, so only5,7
    # need comparison.  The proof of this reduction is in B.47.
    congruence_candidates = {p: p * (p * p - 1) // 2 for p in (5, 7, 11)}
    assert congruence_candidates == {5: 60, 7: 168, 11: 660}
    assert all(n != 504 for n in congruence_candidates.values())
    print("PSL_2(F_p) orders at p=5,7,11 =", congruence_candidates)
    print("No nonabelian simple congruence quotient has order504: PASS")
    output = {"field_polynomial": "u^3+u+1", "a": a, "b": b,
              "orders": [2, 3, 7], "group_order": len(group),
              "conjugacy_classes": classes,
              "congruence_candidate_orders": congruence_candidates,
              "all_checks_passed": True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2) + '\n')
    print("ALL CHECKS PASS")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Finite certificates for ALG-01, ALG-09 and ALG-10; no manuscript input.

The weak Boolean model tests distributivity as an order identity. It deliberately
does NOT satisfy the stronger partial-operation-domain interpretation or the
manuscript's marginal compatible-Boolean-generation assumption.
"""
from itertools import combinations, product
import json


def powerset(values):
    for n in range(len(values) + 1):
        yield from combinations(values, n)


def check_core(elements, zero, one, leq, meet, join, comp, closed, close, compatible):
    for x in elements:
        assert leq(zero, x) and leq(x, one)
        assert compatible(x, x)
        assert comp(comp(x)) == x
        assert compatible(x, comp(x))
        assert meet(x, comp(x)) == zero and join(x, comp(x)) == one
        candidates = [y for y in elements if compatible(x, y) and meet(x, y) == zero]
        assert comp(x) in candidates and all(leq(y, comp(x)) for y in candidates)
        complements = [y for y in candidates if join(x, y) == one]
        assert complements == [comp(x)]
        assert close(x) in closed and leq(x, close(x))
        assert all(leq(close(x), y) for y in closed if leq(x, y))
    assert zero in closed and one in closed
    for x, y in product(elements, repeat=2):
        assert compatible(x, y) == compatible(y, x)
        assert compatible(x, y) == compatible(x, comp(y))
        if leq(x, y):
            assert compatible(x, y) and leq(comp(y), comp(x))
        if compatible(x, y):
            m, j = meet(x, y), join(x, y)
            assert leq(m, x) and leq(m, y) and leq(x, j) and leq(y, j)
            assert all(leq(z, m) for z in elements if leq(z, x) and leq(z, y))
            assert all(leq(j, z) for z in elements if leq(x, z) and leq(y, z))
            assert comp(m) == join(comp(x), comp(y))
            assert comp(j) == meet(comp(x), comp(y))
            assert close(j) == join(close(x), close(y))
            assert compatible(close(x), y)
    for x, y, z in product(elements, repeat=3):
        if all(compatible(a, b) for a, b in ((x, y), (x, z), (y, z))):
            assert meet(x, join(y, z)) == join(meet(x, y), meet(x, z))


def generated(initial, zero, one, meet, join, comp, close=None):
    out = set(initial) | {zero, one}
    while True:
        old = set(out)
        out.update(comp(x) for x in old)
        out.update(meet(x, y) for x, y in product(old, repeat=2))
        out.update(join(x, y) for x, y in product(old, repeat=2))
        if close is not None:
            out.update(close(x) for x in old)
        if out == old:
            return out


def horizontal_sum():
    E = (0, 1, "a", "ac", "b", "bc")
    blocks = ({0, 1, "a", "ac"}, {0, 1, "b", "bc"})
    leq = lambda x, y: x == 0 or y == 1 or x == y
    meet = lambda x, y: x if leq(x, y) else y if leq(y, x) else 0
    join = lambda x, y: y if leq(x, y) else x if leq(y, x) else 1
    complements = {0: 1, 1: 0, "a": "ac", "ac": "a", "b": "bc", "bc": "b"}
    comp = complements.__getitem__
    compatible = lambda x, y: any(x in B and y in B for B in blocks)
    check_core(E, 0, 1, leq, meet, join, comp, set(E), lambda x: x, compatible)
    count = 0
    for family in powerset(E):
        if all(compatible(x, y) for x, y in product(family, repeat=2)):
            count += 1
            B = generated(family, 0, 1, meet, join, comp)
            assert all(compatible(x, y) for x, y in product(B, repeat=2))
            assert all(meet(x, join(y, z)) == join(meet(x, y), meet(x, z))
                       for x, y, z in product(B, repeat=3))
    assert not compatible("a", "b")
    return {"core_axioms": "passed", "all_compatible_families_checked": count,
            "marginal_boolean_generation": "passed", "all_six_elements_clopen": True,
            "a_compatible_b": False}


def weak_relation_model():
    U, X, Y, A = 31, 3, 5, 15
    E = tuple(range(U + 1))
    comp = lambda x: U ^ x
    leq = lambda x, y: x & y == x
    meet = lambda x, y: x & y
    join = lambda x, y: x | y
    orbit = {(x, y) for x in (X, comp(X)) for y in (Y, comp(Y))}
    orbit |= {(y, x) for x, y in tuple(orbit)}
    def compatible(x, y):
        cells = (x & y, x & comp(y), comp(x) & y, comp(x) & comp(y))
        return 0 in cells or (x, y) in orbit
    check_core(E, 0, U, leq, meet, join, comp, set(E), lambda x: x, compatible)
    z = meet(join(X, Y), comp(meet(X, Y)))
    assert compatible(X, Y)
    assert compatible(join(X, Y), comp(meet(X, Y)))
    assert not compatible(X, z)
    rel_Xc, rel_Yc = A & comp(X), A & comp(Y)
    assert not compatible(rel_Xc, rel_Yc)
    # Explicitly report the limitation: distributive expressions have a value
    # as lattice operations, but not all their input pairs are compatible.
    assert compatible(A, comp(X)) and compatible(A, comp(Y)) and compatible(comp(X), comp(Y))
    return {"weak_order_identity_axioms": "passed", "underlying_boolean_elements": len(E),
            "X": X, "Y": Y, "A": A, "xor_X_Y": z, "X_compatible_xor": False,
            "relative_complements": [rel_Xc, rel_Yc], "relative_complements_compatible": False,
            "strong_partial_domain_distributivity": "fails; not a counterexample to strengthened axiom 4"}


def closure_generator_model():
    U, X = 7, 1
    E = tuple(range(8))
    comp = lambda x: U ^ x
    meet = lambda x, y: x & y
    join = lambda x, y: x | y
    close = lambda x: 0 if x == 0 else U if x & 4 else 3
    check_core(E, 0, U, lambda x, y: x & y == x, meet, join, comp,
               {0, 3, 7}, close, lambda x, y: True)
    B = generated({X}, 0, U, meet, join, comp)
    BC = generated({X}, 0, U, meet, join, comp, close)
    assert len(B) == 4 and len(BC) == 8 and close(X) not in B
    interior = comp(close(comp(X)))
    frontier = close(X) & close(comp(X))
    assert interior == 0 and frontier != X
    return {"strengthened_axioms": "passed; underlying full Boolean algebra",
            "boolean_generated_size": len(B), "closure_generated_size": len(BC),
            "X": X, "closure_X": close(X), "interior_X": interior, "frontier_X": frontier}


if __name__ == "__main__":
    print(json.dumps({"ALG-01": weak_relation_model(), "ALG-09": horizontal_sum(),
                      "ALG-10": closure_generator_model()}, indent=2))

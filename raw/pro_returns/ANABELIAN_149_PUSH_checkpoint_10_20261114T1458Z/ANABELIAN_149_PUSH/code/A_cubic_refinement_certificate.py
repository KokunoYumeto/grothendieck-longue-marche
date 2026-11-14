#!/usr/bin/env python3
"""Exact group and integral group-ring certificate for Claim A.29b."""

from collections import defaultdict
from itertools import product
from pathlib import Path
import json


ZERO = (0, 0, 0)
A = tuple(a for a in product(range(3), repeat=3) if sum(a) % 3 == 0)


def add(a, b):
    return tuple((x + y) % 3 for x, y in zip(a, b))


def neg(a):
    return tuple(-x % 3 for x in a)


def scalar(n, a):
    return tuple(n * x % 3 for x in a)


def rotate(a, times=1):
    for _ in range(times % 3):
        a = (a[2], a[0], a[1])
    return a


def mul_g(g, h):
    a, j = g
    b, k = h
    return add(a, rotate(b, j)), (j + k) % 3


def inverse_g(g):
    a, j = g
    return rotate(neg(a), -j), -j % 3


def clean(x):
    return {a: coefficient for a, coefficient in x.items() if coefficient}


def ring_add(*items):
    out = defaultdict(int)
    for item in items:
        for a, coefficient in item.items():
            out[a] += coefficient
    return clean(out)


def ring_scale(n, item):
    return clean({a: n * coefficient for a, coefficient in item.items()})


def ring_mul(left, right):
    out = defaultdict(int)
    for a, x in left.items():
        for b, y in right.items():
            out[add(a, b)] += x * y
    return clean(out)


def subgroup(a):
    return {scalar(i, a) for i in range(3)}


def norm(group):
    return {a: 1 for a in group}


def main():
    identity = (ZERO, 0)
    G = tuple((a, j) for a in A for j in range(3))
    assert len(A) == 9 and len(G) == 27
    assert all(mul_g(g, inverse_g(g)) == identity for g in G)
    assert all(mul_g(mul_g(g, g), g) == identity for g in G)
    # Exhaustive associativity, centre, and commutator subgroup checks.
    for g, h, k in product(G, repeat=3):
        assert mul_g(mul_g(g, h), k) == mul_g(g, mul_g(h, k))
    centre = {g for g in G if all(mul_g(g, h) == mul_g(h, g) for h in G)}
    z = (1, 1, 1)
    Z = subgroup(z)
    assert centre == {(a, 0) for a in Z}
    commutators = {
        mul_g(mul_g(mul_g(g, h), inverse_g(g)), inverse_g(h))
        for g, h in product(G, repeat=2)
    }
    assert commutators == centre

    b = (0, 1, 2)
    subgroups = [subgroup(add(b, scalar(i, z))) for i in range(3)]
    coordinate_kernels = [{a for a in A if a[j] == 0} for j in range(3)]
    assert {frozenset(H) for H in subgroups} == {frozenset(H) for H in coordinate_kernels}
    assert {frozenset(rotate(a) for a in H) for H in subgroups} == {frozenset(H) for H in subgroups}
    assert all(H & Z == {ZERO} for H in subgroups)

    one = {ZERO: 1}
    nz = norm(Z)
    total = ring_add(*(norm(H) for H in subgroups))
    b_plus_b2 = {b: 1, scalar(2, b): 1}
    assert total == ring_add(ring_scale(3, one), ring_mul(b_plus_b2, nz))
    assert ring_mul(nz, nz) == ring_scale(3, nz)
    # On the Jacobian, b acts by translation on the elliptic quotient V/Z,
    # hence (b-1)N_Z=0.  This geometric input is proved in the manuscript.
    reduced = ring_add(ring_scale(3, one), ring_scale(2, nz))
    difference = ring_add(total, ring_scale(-1, reduced))
    assert difference == ring_mul(ring_add(b_plus_b2, ring_scale(-2, one)), nz)
    complement = ring_add(ring_scale(9, one), ring_scale(-2, nz))
    assert ring_mul(reduced, complement) == ring_scale(27, one)

    divisors = [(-2, 1, 1), (1, 1, -2), (1, -2, 1)]
    assert tuple(sum(v[i] for v in divisors) for i in range(3)) == ZERO
    assert tuple(divisors[1][i] - divisors[0][i] for i in range(3)) == (3, 0, -3)
    assert all(tuple(x % 3 for x in v) == z for v in divisors)
    # Degree-nine cover of E, three branch fibres of index three.
    assert 2 * 10 - 2 == 9 * 3 * (3 - 1) // 3
    assert 10 - 1 == 3 * (4 - 1)

    result = {
        "claim": "A.29b",
        "deck_group_over_E_order": len(A),
        "heisenberg_group_order": len(G),
        "exponent": 3,
        "centre_equals_commutator": True,
        "centre": [list(a) for a in sorted(Z)],
        "three_conjugate_coordinate_quotients": True,
        "divisor_vectors": divisors,
        "nontrivial_unramified_ratio_divisor_divided_by_3": [1, 0, -1],
        "genus_V": 10,
        "degree_V_over_B": 3,
        "etale_RH_identity": "10-1=3(4-1)",
        "integral_norm_identity": "sum N_Hi = 3*Id + (b+b^2)*N_Z",
        "geometric_translation_relation": "(b-1)*N_Z=0 on J_V because V/Z is an elliptic etale quotient",
        "reduced_norm_identity": "(3*Id+2*N_Z)(9*Id-2*N_Z)=27*Id",
        "geometric_nontriviality_input": "O-2d is a nonprincipal divisor of exact order3 on E; see flex in A.29a",
        "conclusion": "The three translated genus-four pullback Jacobians generate J_V; hence the absence of p-rank-zero abelian targets in A.29a persists on V.",
        "all_passed": True,
    }
    output = json.dumps(result, indent=2, sort_keys=True)
    Path(__file__).with_suffix(".json").write_text(output + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()

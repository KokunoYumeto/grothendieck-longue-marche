#!/usr/bin/env python3
"""Finite checks accompanying A and F; none replaces the infinite proofs.

Run with Python >=3.10, standard library only.  Output is deterministic.
"""
from itertools import permutations, combinations, product
from collections import Counter
import json

def mul(g, h):
    return tuple(g[h[i]] for i in range(len(g)))

G = tuple(permutations(range(3)))
one = (0, 1, 2)
a, b = (1, 0, 2), (0, 2, 1)

def inv(g):
    return tuple(g.index(i) for i in range(len(g)))

def subgroup(g):
    ans, h = set(), one
    while h not in ans:
        ans.add(h)
        h = mul(h, g)
    return frozenset(ans)

c = inv(mul(a, b))
Hs = [subgroup(a), subgroup(b), subgroup(c)]

def cosets(H):
    return tuple(sorted({frozenset(mul(g, h) for h in H) for g in G},
                        key=lambda q: sorted(q)))

# An arrow is (source, target, value); values at a boundary-to-open Hom
# are actual right-subgroup cosets. Empty Hom sets stay empty.
objects = ("u", "p0", "p1", "pi")
arrows = [("u", "u", g) for g in G]
for i, s in enumerate(objects[1:]):
    arrows.append((s, s, None))
    arrows.extend((s, "u", q) for q in cosets(Hs[i]))

def compose(f, g):
    """f after g."""
    assert g[1] == f[0]
    if f[0] == f[1] and f[2] is None:
        return g
    if g[0] == g[1] and g[2] is None:
        return f
    if g[0] == "u":
        return ("u", "u", mul(f[2], g[2]))
    return (g[0], "u", frozenset(mul(f[2], h) for h in g[2]))

triple_count = 0
for f, g, h in product(arrows, repeat=3):
    if h[1] == g[0] and g[1] == f[0]:
        assert compose(f, compose(g, h)) == compose(compose(f, g), h)
        triple_count += 1

def parity(g):
    return sum(g[i] > g[j] for i in range(3) for j in range(i+1, 3)) % 2

def quotient_arrow(f):
    s, t, v = f
    if v is None:
        return f
    if s == t == "u":
        return (s, t, parity(v))
    return (s, t, frozenset(parity(h) for h in v))

def compose_q(f, g):
    assert g[1] == f[0]
    if f[2] is None:
        return g
    if g[2] is None:
        return f
    if g[0] == "u":
        return ("u", "u", (f[2]+g[2]) % 2)
    return (g[0], "u", frozenset((f[2]+h) % 2 for h in g[2]))

pair_count = 0
for f, g in product(arrows, repeat=2):
    if g[1] == f[0]:
        assert quotient_arrow(compose(f, g)) == compose_q(
            quotient_arrow(f), quotient_arrow(g))
        pair_count += 1

# The natural transformation id_[1] => constant_1 exists.
# A subterminal covariant functor is bits (s0,s1) with s0 <= s1.
subterminal_arrow = [(x, y) for x, y in product((0, 1), repeat=2) if x <= y]
subterminal_point = [(x,) for x in (0, 1)]
assert len(subterminal_arrow) == 3 and len(subterminal_point) == 2

def norm_split(A, labels):
    A, B = frozenset(A), frozenset(labels)-frozenset(A)
    return min((A, B), key=lambda X: (len(X), tuple(sorted(X))))

def splits(n):
    L = frozenset(range(1, n+1))
    return tuple(sorted({norm_split(A, L)
                         for k in range(2, n-1) for A in combinations(L, k)},
                        key=lambda A: (len(A), tuple(sorted(A)))))

def compatible(A, B, L):
    return any(not z for z in (A&B, A&(L-B), (L-A)&B, (L-A)&(L-B)))

def trees(n):
    L, S = frozenset(range(1, n+1)), splits(n)
    return [frozenset(T) for k in range(n-2) for T in combinations(S, k)
            if all(compatible(A, B, L) for A, B in combinations(T, 2))]

def forget(T, n):
    L = frozenset(range(1, n))
    ans = set()
    for A in T:
        U = A & L
        if 2 <= len(U) <= len(L)-2:
            ans.add(norm_split(U, L))
    return frozenset(ans)

T4, T5 = trees(4), trees(5)
assert len(T4) == 4 and len(T5) == 26
assert Counter(map(len, T5)) == {0: 1, 1: 10, 2: 15}
assert all(forget(T, 5) in T4 for T in T5)
q = frozenset((frozenset((1, 2)), frozenset((3, 4))))
assert len(q) == 2 and len(forget(q, 5)) == 1
forget_rows = [{"source": [sorted(s) for s in sorted(T, key=lambda x: tuple(sorted(x)))],
                "target": [sorted(s) for s in forget(T, 5)]}
               for T in T5]

# Difference of the two node twists: exact kernel at every checked modulus.
modulus_checks = []
for m in range(2, 25):
    kernel = {(x, y) for x in range(m) for y in range(m) if (x+y) % m == 0}
    diagonal = {(x, -x % m) for x in range(m)}
    assert kernel == diagonal and len(kernel) == m
    units = [u for u in range(m) if __import__("math").gcd(u, m) == 1]
    for u in units:
        assert {((u*x) % m, (u*y) % m) for x, y in kernel} == kernel
    modulus_checks.append({"m": m, "kernel_size": len(kernel),
                           "units_checked": len(units)})

# Hom(C_m,F_l) is nonzero whenever l divides m.
for ell in (2, 3, 5, 7, 11):
    for m in (ell, 2*ell, 3*ell):
        hom_values = [v for v in range(ell) if (m*v) % ell == 0]
        assert len(hom_values) == ell

def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

I, negI = ((1, 0), (0, 1)), ((-1, 0), (0, -1))
S, T = ((0, -1), (1, 0)), ((1, 1), (0, 1))
assert mm(S, S) == negI
assert mm(mm(mm(S, T), mm(S, T)), mm(S, T)) == negI
assert mm(negI, negI) == I
assert tuple(tuple(v % 4 for v in row) for row in negI) != I

result = {
    "description": "Supplementary finite checks only; see A and F for proofs.",
    "subterminal_counts": {"arrow_category": 3, "point_category": 2},
    "finite_C4_model": {
        "group": "S3",
        "inertia_orders": [len(H) for H in Hs],
        "objects": len(objects), "arrows": len(arrows),
        "associative_composable_triples": triple_count,
        "sign_transition_composable_pairs": pair_count,
        "sign_quotient_arrows": len({quotient_arrow(f) for f in arrows})},
    "tree_counts": {"n4": len(T4), "n5": len(T5),
                   "n5_by_nodes": dict(sorted(Counter(map(len, T5)).items()))},
    "forget_5": forget_rows,
    "node_difference_moduli": modulus_checks,
    "torus_relations": "S^2=(ST)^3=-I, (-I)^2=I; -I detected modulo 4",
    "status": "PASS"
}
print(json.dumps(result, indent=2, sort_keys=True))


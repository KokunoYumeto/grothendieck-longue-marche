#!/usr/bin/env python3
"""Exact finite graph and discrete-word checks for A.4.39.

The theorem is proved for every finite quotient by its graph-chain argument.
This independent certificate exhausts all 216 maps with a nontrivial cone
involution into S4 and verifies the literal free-product changes of marking.
It is not a census of gentle images or pentagon shadows.
"""
from itertools import permutations
from pathlib import Path
import json

ID = tuple(range(4))
PERMS = tuple(permutations(range(4)))

def mul(x, y):
    return tuple(x[y[i]] for i in range(4))

def inv(x):
    return tuple(x.index(i) for i in range(4))

def subgroup(gens):
    seen = {ID}
    todo = [ID]
    for x in todo:
        for g in gens:
            z = mul(x, g)
            if z not in seen:
                seen.add(z)
                todo.append(z)
    return tuple(sorted(seen))

def cyclic(x):
    ans = [ID]
    while (z := mul(ans[-1], x)) != ID:
        ans.append(z)
    return tuple(ans)

def rank2(rows):
    piv = {}
    for x in rows:
        while x:
            i = x.bit_length() - 1
            if i in piv:
                x ^= piv[i]
            else:
                piv[i] = x
                break
    return len(piv)

def graph_case(a, d, group):
    # Right cosets x<a>; left translation is the deck action.
    vertices = sorted({min(x, mul(x, a)) for x in group})
    vi = {x: i for i, x in enumerate(vertices)}
    edge = []
    boundary_columns = []
    for x in group:
        source = vi[min(x, mul(x, a))]
        xd = mul(x, d)
        target = vi[min(xd, mul(xd, a))]
        edge.append((source, target))
        boundary_columns.append((1 << source) ^ (1 << target))
    gi = {x: i for i, x in enumerate(group)}
    cycle = cyclic(d)
    chain = [gi[x] for x in cycle]
    boundary = 0
    for i in chain:
        boundary ^= boundary_columns[i]
    assert boundary == 0 and len(chain) == len(set(chain))
    stabilizer = tuple(x for x in group
                       if {mul(x, y) for y in cycle} == set(cycle))
    assert set(stabilizer) == set(cycle)
    incidence_rank = rank2(boundary_columns)
    homology_rank = len(group) - incidence_rank
    assert incidence_rank == len(vertices) - 1
    assert homology_rank == 1 + len(group) // 2
    return {'vertices': vertices, 'edges': edge, 'cycle_edge_indices': chain,
            'deck_stabilizer': stabilizer, 'homology_rank': homology_rank,
            'homology_extension_order': len(group) * 2**homology_rank}

records = []
for a in PERMS:
    if a == ID or mul(a, a) != ID:
        continue
    for d in PERMS:
        v = mul(a, inv(d))
        group = subgroup((a, d))
        assert subgroup((a, v)) == group
        records.append({'a': a, 'd': d, 'v': v, 'Q_elements': group,
                        'd_graph': graph_case(a, d, group),
                        'v_graph': graph_case(a, v, group)})
assert len(records) == 216
print('PASS all 216 actual R0 -> S4 quotients with a nontrivial cone involution')
print('PASS both cusp cycles, all deck stabilizers, graph ranks and exact cover orders')

def normal(word, orders):
    out = []
    for factor, exponent in word:
        n = orders.get(factor, 0)
        if n:
            exponent %= n
        if not exponent:
            continue
        if out and out[-1][0] == factor:
            exponent += out.pop()[1]
            if n:
                exponent %= n
        if exponent:
            out.append((factor, exponent))
    return tuple(out)

def wi(word):
    return tuple((a, -n) for a, n in reversed(word))

R_ORDERS = {'a': 2}
A = (('a', 1),)
D = (('d', 1),)
V = normal(A + wi(D), R_ORDERS)
assert normal(D + V + wi(D), R_ORDERS) == normal(wi(V) + wi(D) * 2, R_ORDERS)
assert normal(D + V * 2 + wi(D), R_ORDERS) == normal((wi(V) + wi(D) * 2) * 2, R_ORDERS)
assert normal((V + D) * 2, R_ORDERS) == ()
print('PASS the exact K_std Schreier images Y, X^2, (X^-1 Y^-1)^2')

B_ORDERS = {'s': 2, 'r': 3}
U = (('r', 2), ('s', 1))
W = (('s', 1), ('r', 2))
assert normal(U + W + U, B_ORDERS) == (('s', 1),)
assert normal((U + W) * 3, B_ORDERS) == ()
assert normal(W + U * 2 + W, B_ORDERS) == normal(wi(U) * 2, B_ORDERS)
print('PASS the four-point folding identity w u^2 w = u^-2 in C2*C3')

report = {'scope': __doc__, 'maps_checked': len(records),
          'records': records,
          'literal_words': {'R_a': A, 'R_d': D, 'R_v': V,
                            'B_u': U, 'B_w': W},
          'all_assertions_passed': True}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')

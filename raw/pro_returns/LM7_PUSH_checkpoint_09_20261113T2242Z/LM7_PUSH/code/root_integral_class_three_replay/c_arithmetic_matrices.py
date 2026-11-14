#!/usr/bin/env python3
"""Exact finite cocycle matrices used in C.14.

The arithmetic check is at n=1 for the two Tate coefficient modules
F_3 and mu_3 over Q with S={3,infinity}.  The actual splitting field
Q(zeta_9,cuberoot(3)) has group (C_3 x C_3) semidirect C_2, and its
decomposition group at 3 is the entire group.  This quotient captures
all one-cocycles for both modules, by the S-unit calculation over
Q(zeta_3).  No enumeration of the vastly larger rank-44 fields in
C.14 is claimed here.

The duplicated local subgroup check is a separate finite-matrix
fixture; it is not asserted to describe a specified number field.
"""
from itertools import product
from pathlib import Path
import json


def rank(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return 0
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                t = a[i][col]
                a[i] = [(x - t*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


G = list(product(range(3), range(3), range(2)))
index = {g: i for i, g in enumerate(G)}


def multiply(g, h):
    a, b, c = g
    aa, bb, cc = h
    return ((a+aa) % 3, (b+(-1)**c*bb) % 3, (c+cc) % 2)


table = [[index[multiply(g, h)] for h in G] for g in G]
assert all(multiply(multiply(g, h), k) == multiply(g, multiply(h, k))
           for g in G for h in G for k in G)
assert all(any(multiply(g, h) == (0, 0, 0) for h in G) for g in G)


def one_dimensional_matrices(character, local_subgroups):
    """Return exact mod-three H1 and compact H1 dimensions and ranks."""
    n = len(G)
    assert len(character) == n
    assert all(character[table[i][j]] % 3 == character[i]*character[j] % 3
               for i in range(n) for j in range(n))
    coboundary = [[(character[i]-1) % 3] for i in range(n)]
    cocycle = []
    for i in range(n):
        for j in range(n):
            row = [0]*n
            row[j] += character[i]
            row[table[i][j]] -= 1
            row[i] += 1
            cocycle.append(row)
    rank_d0 = rank(coboundary, 3)
    rank_d1 = rank(cocycle, 3)
    compact = [row + [0]*len(local_subgroups) for row in cocycle]
    for v, subgroup in enumerate(local_subgroups):
        for g in subgroup:
            row = [0]*(n+len(local_subgroups))
            row[g] = 1
            row[n+v] = 1-character[g]
            compact.append(row)
    rank_compact = rank(compact, 3)
    # The compact coboundary sends b to (delta b,b,...,b).
    # At least one local subgroup occurs, so its rank is exactly one.
    assert local_subgroups
    return {
        'one_cochain_dimension': n,
        'coboundary_rank': rank_d0,
        'cocycle_equation_rank': rank_d1,
        'H1_dimension': n-rank_d1-rank_d0,
        'compact_variable_dimension': n+len(local_subgroups),
        'compact_equation_rank': rank_compact,
        'compact_H1_dimension': n+len(local_subgroups)-rank_compact-1,
    }


trivial = [1]*len(G)
cyclotomic = [(-1)**g[2] % 3 for g in G]
whole = list(range(len(G)))
results = {
    'field': 'Q(zeta_9,cuberoot(3))',
    'group_order': len(G),
    'local_decomposition_order_at_3': len(G),
    'constant_F3': one_dimensional_matrices(trivial, [whole]),
    'mu3': one_dimensional_matrices(cyclotomic, [whole]),
    'duplicate_local_matrix_fixture_constant':
        one_dimensional_matrices(trivial, [whole, whole]),
    'duplicate_local_matrix_fixture_cyclotomic':
        one_dimensional_matrices(cyclotomic, [whole, whole]),
}
assert results['constant_F3']['H1_dimension'] == 1
assert results['mu3']['H1_dimension'] == 1
assert results['constant_F3']['compact_H1_dimension'] == 0
assert results['mu3']['compact_H1_dimension'] == 0
assert results['duplicate_local_matrix_fixture_constant']['compact_H1_dimension'] == 1
assert results['duplicate_local_matrix_fixture_cyclotomic']['compact_H1_dimension'] == 0
results['all_assertions_passed'] = True
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(results, indent=2)+'\n')
print(json.dumps(results, indent=2))

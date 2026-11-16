#!/usr/bin/env python3
"""Exact rank-97 graph lattice behind the level-12 homology detector.

This computes an integral Bass--Serre graph basis, not a GT-shadow census.
The cohomology calculation and character descent are proved in RH.1--RH.3.
"""
from collections import Counter, deque
from itertools import product
from math import gcd
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
MOD = 12

def canonical(a):
    a = tuple(x % MOD for x in a)
    return min(a, tuple(-x % MOD for x in a))

def multiply(a, b):
    p, q, r, s = a
    t, u, v, w = b
    return canonical((p*t+q*v, p*u+q*w, r*t+s*v, r*u+s*w))

def power(a, k):
    z = (1, 0, 0, 1)
    for _ in range(k):
        z = multiply(z, a)
    return z

def main():
    one = (1, 0, 0, 1)
    s = canonical((0, 1, -1, 0))
    r = canonical((0, -1, 1, -1))
    qelts = sorted({canonical(a) for a in product(range(12), repeat=4)
                   if (a[0]*a[3]-a[1]*a[2]) % 12 == 1})
    qi = {q: i for i, q in enumerate(qelts)}
    assert len(qelts) == 576
    h2, h3 = [one, s], [one, r, power(r, 2)]
    def coset(a, h):
        return tuple(sorted(multiply(a, b) for b in h))
    cs2 = sorted({coset(a, h2) for a in qelts})
    cs3 = sorted({coset(a, h3) for a in qelts})
    v2 = {a: i for i, a in enumerate(cs2)}
    v3 = {a: i+len(cs2) for i, a in enumerate(cs3)}
    edges = [(v2[coset(a, h2)], v3[coset(a, h3)]) for a in qelts]
    vertices = len(cs2)+len(cs3)
    adjacency = [[] for _ in range(vertices)]
    for e, (u, v) in enumerate(edges):
        adjacency[u].append((v, e, 1))
        adjacency[v].append((u, e, -1))
    parent = [None]*vertices
    parent[0] = (-1, -1, 0)
    queue = deque([0])
    tree = set()
    while queue:
        u = queue.popleft()
        for v, e, sign in adjacency[u]:
            if parent[v] is None:
                # Parent-to-child traversal has the indicated edge sign.
                parent[v] = (u, e, sign)
                tree.add(e)
                queue.append(v)
    assert all(p is not None for p in parent)
    chords = sorted(set(range(len(edges)))-tree)
    assert (len(cs2), len(cs3), len(tree), len(chords)) == (288, 192, 479, 97)
    def path_to_root(v):
        out = np.zeros(len(edges), dtype=np.int64)
        while v:
            u, e, sign = parent[v]
            out[e] -= sign
            v = u
        return out
    cycles = []
    for e in chords:
        u, v = edges[e]
        c = path_to_root(v)-path_to_root(u)
        c[e] += 1
        cycles.append(c)
    cycles = np.stack(cycles, axis=1)
    assert np.array_equal(cycles[chords, :], np.eye(97, dtype=np.int64))
    boundary = np.zeros((vertices, len(edges)), dtype=np.int64)
    for e, (u, v) in enumerate(edges):
        boundary[u, e] = -1
        boundary[v, e] = 1
    assert not np.any(boundary @ cycles)
    def deck_matrix(q):
        perm = [qi[multiply(q, a)] for a in qelts]
        translated = np.empty_like(cycles)
        translated[perm, :] = cycles
        mat = translated[chords, :]
        assert np.array_equal(cycles @ mat, translated)
        return mat
    ms, mr = deck_matrix(s), deck_matrix(r)
    eye = np.eye(97, dtype=np.int64)
    assert np.array_equal(ms @ ms, eye)
    assert np.array_equal(mr @ mr @ mr, eye)
    # All traces and the finite deck faithfulness bound, without relying on
    # floating point eigenvalues or approximations to matrix orders.
    trace_data = []
    max_difference = 0
    for q in qelts:
        fixed2 = sum(coset(multiply(q, c[0]), h2) == c for c in cs2)
        fixed3 = sum(coset(multiply(q, c[0]), h3) == c for c in cs3)
        expected = 1 + (576 if q == one else 0)-fixed2-fixed3
        # Diagonal entries can be read directly from translated cycle columns.
        inverse_perm = [0]*576
        for a in qelts:
            inverse_perm[qi[multiply(q, a)]] = qi[a]
        actual = sum(int(cycles[inverse_perm[e], j])
                     for j, e in enumerate(chords))
        assert actual == expected
        if q != one:
            assert not (fixed2 and fixed3)
            difference = 97-actual
            assert 96 <= difference <= 384 < 576
            max_difference = max(max_difference, difference)
        trace_data.append(actual)
    # Doubled edge chains represent paths between edge midpoints.  A factor
    # s passes through a type-2 vertex, and r through a type-3 vertex.
    position = one
    doubled = np.zeros(576, dtype=np.int64)
    cusp_edges = []
    for letter in [s, r]*12:
        following = multiply(position, letter)
        if letter == s:
            doubled[qi[position]] -= 1
            doubled[qi[following]] += 1
        else:
            doubled[qi[position]] += 1
            doubled[qi[following]] -= 1
        position = following
    assert position == one and all(x % 2 == 0 for x in doubled)
    cusp = doubled//2
    assert not np.any(boundary @ cusp)
    coords = cusp[chords]
    assert np.array_equal(cycles @ coords, cusp)
    content = 0
    for x in coords:
        content = gcd(content, abs(int(x)))
    assert content == 1
    support = [e for e, c in enumerate(cusp) if c]
    assert len(support) == 24 and set(cusp[support]) == {-1, 1}
    degree = Counter(v for e in support for v in edges[e])
    assert len(degree) == 24 and set(degree.values()) == {2}
    data = {
        'Q12_order': 576, 'vertices_order2': 288, 'vertices_order3': 192,
        'tree_edges': 479, 'homology_rank': 97,
        'invariant_boundary_column': [2, -3],
        'invariant_augmentation_row': [288, 192],
        'cohomological_modulus': gcd(288, 192),
        'homology_detector_modulus_on_H': 576,
        'all_deck_characters_checked': 576,
        'trace_histogram': dict(sorted(Counter(trace_data).items())),
        'largest_nonidentity_trace_difference': max_difference,
        'primitive_cusp_cycle_content': content,
        'cusp_cycle_edge_count': len(support),
        'quotient_order': '576^98',
        'scope': 'H explicit; full GT0 integral homology factorization and some finite modulus only',
        'Q_ordered_matrices': qelts, 'edge_vertices': edges, 'tree_edge_indices': sorted(tree),
        'cycle_chord_indices': chords, 'cycle_basis_columns': cycles.T.tolist(),
        'deck_matrix_s': ms.tolist(), 'deck_matrix_r': mr.tolist(),
        'cusp_coordinates': coords.tolist(),
    }
    out = ROOT/'records'/'congruence_homology.json'
    out.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    concise = {k: v for k, v in data.items() if k not in {
        'Q_ordered_matrices','edge_vertices','tree_edge_indices','cycle_chord_indices',
        'cycle_basis_columns','deck_matrix_s','deck_matrix_r','cusp_coordinates'}}
    print(json.dumps(concise, indent=2))
    print('PASS: exact graph, cycle basis, deck matrices, all traces and primitive cusp.')

if __name__ == '__main__':
    main()

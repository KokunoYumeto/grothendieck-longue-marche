#!/usr/bin/env python3
"""Exact F9-character decomposition of the C4^5 five-point cover.

This verifies a concrete limitation of its first homology and records
the actual character rows of the 15 colored-quartet maps.  The next
class-two cover, rather than this abelian layer alone, is the candidate
for detecting the Brunnian pentagon.
"""
from itertools import product, combinations
from pathlib import Path
import json
import numpy as np
from fivepoint_relative_tools import relations

HERE = Path(__file__).resolve().parent
add = np.array([[(a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3)
                 for b in range(9)] for a in range(9)], dtype=np.int8)
neg = np.array([(-a % 3) + 3 * (-(a // 3) % 3) for a in range(9)], dtype=np.int8)
mul = np.array([[(a % 3 * (b % 3) + 2 * (a // 3) * (b // 3)) % 3 +
                 3 * ((a % 3 * (b // 3) + a // 3 * (b % 3)) % 3)
                 for b in range(9)] for a in range(9)], dtype=np.int8)
inv = np.zeros(9, dtype=np.int8)
for i in range(1, 9):
    inv[i] = int(np.flatnonzero(mul[i] == 1)[0])
units = (1, 3, 2, 6)
assert mul[3, 3] == 2


def rank(a):
    a = np.array(a, dtype=np.int8).copy()
    r = 0
    for col in range(a.shape[1]):
        nz = np.flatnonzero(a[r:, col])
        if not len(nz):
            continue
        i = r + int(nz[0])
        a[[r, i]] = a[[i, r]]
        a[r] = mul[inv[a[r, col]], a[r]]
        for j in range(a.shape[0]):
            if j != r and a[j, col]:
                a[j] = add[a[j], neg[mul[a[j, col], a[r]]]]
        r += 1
        if r == a.shape[0]:
            break
    return r


def fox_row(word, chi):
    value = 1
    row = np.zeros(5, dtype=np.int8)
    for letter in word:
        j = abs(letter) - 1
        if letter > 0:
            row[j] = add[row[j], value]
            value = int(mul[value, chi[j]])
        else:
            value = int(mul[value, inv[chi[j]]])
            row[j] = add[row[j], neg[value]]
    assert value == 1
    return row


edges = ((0, 2), (1, 2), (0, 3), (1, 3), (2, 3))
pairings = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
quartet_rows = []
supports = []
for S in combinations(range(5), 4):
    rows = []
    for pairing in pairings:
        paired = {tuple(sorted((S[i], S[j]))) for i, j in pairing}
        rows.append(tuple(0 if not set(e).issubset(S) else
                          2 if e in paired else 1 for e in edges))
    span = {tuple(sum(c * row[j] for c, row in zip(coeffs, rows)) % 4
                  for j in range(5)) for coeffs in product(range(4), repeat=3)}
    assert len(span) == 16
    quartet_rows.append({'quartet': list(S), 'rows': rows, 'characters': sorted(span)})
    supports.append(span)
zero = (0,) * 5
for i in range(5):
    for j in range(i):
        assert supports[i] & supports[j] == {zero}
expected = set.union(*supports)
assert len(expected) == 76

records = []
found = set()
dim_total = 0
for exponents in product(range(4), repeat=5):
    chi = tuple(units[i] for i in exponents)
    matrix = np.array([fox_row(w, chi) for w in relations], dtype=np.int8)
    boundary = np.array([add[c, neg[1]] for c in chi], dtype=np.int8)
    for row in matrix:
        val = 0
        for x, y in zip(row, boundary):
            val = int(add[val, mul[x, y]])
        assert val == 0
    dimension = (5 if exponents == zero else 4) - rank(matrix)
    assert dimension == (5 if exponents == zero else 1 if exponents in expected else 0)
    if dimension:
        found.add(exponents)
        records.append({'character': exponents, 'dimension': dimension,
                        'fox_matrix': matrix.tolist()})
    dim_total += dimension
assert found == expected and dim_total == 80
order_two = sum(all(x % 2 == 0 for x in r['character']) and r['character'] != zero
                for r in records)
order_four = len(records) - 1 - order_two
assert (order_two, order_four) == (15, 60)
print('PASS actual six-relator Fox matrices for all 1024 C4^5 characters', flush=True)
print('PASS nonzero support: trivial dimension5 plus 75 characters of dimension1', flush=True)
print('PASS five actual quartet character planes meet only at zero and give the entire support', flush=True)
print('PASS H1 dimension80 over F3: 5 trivial + 15 sign + 30 conjugate F9 pairs', flush=True)

output = {'source': 'Gamma_0,5=P4/center, generators A13,A23,A14,A24,A34',
          'source_relations': relations, 'base_order': 4 ** 5,
          'character_field': 'F3[i]/(i^2+1)', 'homology_dimension': 80,
          'nontrivial_order_two_characters': order_two,
          'nontrivial_order_four_characters': order_four,
          'quartet_character_planes': quartet_rows, 'nonzero_character_records': records,
          'scope': 'Exact first homology and actual four-point character support. No pentagon exclusion is inferred.'}
(HERE / 'check_fivepoint_relative_h1.json').write_text(json.dumps(output, indent=2) + '\n')

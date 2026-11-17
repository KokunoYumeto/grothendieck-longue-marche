#!/usr/bin/env python3
"""Exhaust all 36*3^4 affine possibilities for the homology parity detector."""
from pathlib import Path
import itertools
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'notes/reproduced/quaternion_homology/work/tower_code'
certificate = json.loads((DATA / 'modular_quaternion_homology_compressed.json').read_text())
archive = np.load(DATA / 'modular_quaternion_homology_compressed.npz')

def multiply(a, b, modulus):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % modulus
                 for i in range(2) for j in range(2))

cm = (0, 1, -1, 1)
residue_powers = {}
for modulus in (3, 4):
    a = (1, 0, 0, 1)
    powers = {}
    for exponent in range(6):
        assert a not in powers
        powers[a] = exponent
        a = multiply(a, cm, modulus)
    commuting = {a for a in itertools.product(range(modulus), repeat=4)
                 if (a[0]*a[3]-a[1]*a[2]) % modulus == 1
                 and multiply(a, cm, modulus) == multiply(cm, a, modulus)}
    assert set(powers) == commuting
    residue_powers[modulus] = powers
vectors = np.array(list(itertools.product(range(3), repeat=4)), dtype=np.int64)
records = certificate['records']
assert len(records) == 36
seen = set()
total = 0
for row in records:
    matrix = tuple(sum(row['mod12_matrix'], []))
    assert matrix not in seen
    seen.add(matrix)
    i = residue_powers[4][tuple(x % 4 for x in matrix)]
    j = residue_powers[3][tuple(x % 3 for x in matrix)]
    equations = np.array(row['actual_kernel_equation'], dtype=np.int64)
    rhs = np.array(row['actual_kernel_rhs'], dtype=np.int64)
    count = int(np.sum(np.all(vectors @ equations % 3 == rhs, axis=1)))
    assert count == (9 if i % 2 == j % 2 else 0)
    assert bool(count) == row['lifts_to_CM_centralizer']
    total += count
    print('MATRIX', matrix, 'EXPONENTS_MOD4_MOD3', (i, j),
          'EXACT_AFFINE_SOLUTIONS', count)
assert total == 162
w = archive['actual_IA'].astype(np.int64)
pivots = archive['actual_IA_pivots']
schreier = archive['source_Schreier_rows'].astype(np.int64)
assert w.shape == (4, 126) and schreier.shape == (36864, 126)
assert np.array_equal(w[:, pivots], np.eye(4, dtype=np.int64))
assert np.array_equal(schreier[:, pivots] @ w % 3, schreier)
coefficients = schreier[certificate['independent_Schreier_rows']][:, pivots]
assert len({tuple(v) for v in vectors @ coefficients % 3}) == 81
assert ((5, 0, 0, 5) in seen)
print('PASS all2916 affine vectors: exactly18 parity-compatible fibres of9.')
print('PASS separate exhaustive mod3/mod4 centralizers and all36864 source rows.')

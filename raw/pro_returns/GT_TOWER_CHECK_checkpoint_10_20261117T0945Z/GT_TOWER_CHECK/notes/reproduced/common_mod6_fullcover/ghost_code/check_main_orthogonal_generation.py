#!/usr/bin/env python3
"""Independent audit of the actual 18-dimensional tower matrices.

Checks the supplied words and reflection lists directly, then constructs
an actual determinant-minus-one element of the orthogonal centralizer
of the displayed C3^2. The infinite family of radical elements is
handled by the proved additive formula and the checked parameter rank.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

D = Path(__file__).resolve().parents[1] / 'tower_code'
Z = np.load(D / 'translation_quaternion_homology.npz')
generators = Z['quaternion_kernel_generators'].astype(np.int64) % 3
translations = Z['H18'].astype(np.int64) % 3
F = np.load(D / 'translation_quaternion_image.npz')['form'].astype(np.int64) % 3
certificate = json.loads((D / 'translation_quaternion_radical_certificate.json').read_text())
I = np.eye(18, dtype=np.int64)


def reduce_rows(matrix):
    a = np.array(matrix, dtype=np.int64) % 3
    pivots, row = [], 0
    for col in range(a.shape[1]):
        indices = np.flatnonzero(a[row:, col])
        if len(indices) == 0:
            continue
        pivot = row + int(indices[0])
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = (int(a[row, col]) * a[row]) % 3
        for k in range(a.shape[0]):
            if k != row:
                a[k] = (a[k] - a[k, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def rank(a):
    return len(reduce_rows(a)[1])


def inverse(a):
    n = a.shape[0]
    reduced, pivots = reduce_rows(np.concatenate((a, np.eye(n, dtype=np.int64)), axis=1))
    assert pivots[:n] == list(range(n))
    return reduced[:, n:]


def determinant(a):
    a = np.array(a, dtype=np.int64) % 3
    n, det = len(a), 1
    for col in range(n):
        rows = np.flatnonzero(a[col:, col])
        if len(rows) == 0:
            return 0
        pivot = col + int(rows[0])
        if pivot != col:
            det = -det
            a[[col, pivot]] = a[[pivot, col]]
        entry = int(a[col, col])
        det = det * entry % 3
        a[col] = entry * a[col] % 3
        for k in range(col + 1, n):
            a[k] = (a[k] - a[k, col] * a[col]) % 3
    return det % 3


def quadratic(v):
    return int(2 * (v @ F @ v) % 3)


def radical(e, v):
    assert e @ F @ e % 3 == 0 and e @ F @ v % 3 == 0
    return (I + np.outer(v, e @ F) - np.outer(e, v @ F)
            - quadratic(v) * np.outer(e, e @ F)) % 3


assert F.shape == (18, 18) and np.array_equal(F, F.T)
assert determinant(F) == 1
assert ((-1) ** 9 * determinant(F)) % 3 == 2
for g in generators:
    assert determinant(g) == 1 and np.array_equal(g.T @ F @ g % 3, F)
print('PASS: all 360 matrices are determinant-one isometries of a nondegenerate minus form')

e = np.array(certificate['root_vector'], dtype=np.int64)
parameters = np.array(certificate['radical_parameter_vectors'], dtype=np.int64)
source = generators[certificate['root_generator_index']]
assert rank(np.vstack((e, parameters))) == 17
assert np.all(parameters @ F @ e % 3 == 0)
for v, word in zip(parameters, certificate['conjugating_words_in_360_generators']):
    h = I.copy()
    for j in word:
        h = h @ generators[j - 1] % 3
    assert np.array_equal(h @ source @ inverse(h) % 3, radical(e, v))
for v in parameters:
    for w in parameters:
        assert np.array_equal(radical(e, v) @ radical(e, w) % 3,
                              radical(e, (v + w) % 3))
opposite = generators[certificate['opposite_generator_index']]
f_raw = opposite @ e % 3
pairing = int(e @ F @ f_raw % 3)
assert pairing != 0
f = pairing * f_raw % 3
assert e @ F @ f % 3 == 1 and quadratic(f) == 0
print('PASS: all 16 actual conjugating words and the complete 16-dimensional radical parameter space')
print(f'PASS: opposite radical from zero-based generator {certificate["opposite_generator_index"]}; B(e,f_raw)={pairing}')

# Construct the short orbit bridge from the two radicals.
W = []
for a in I:
    W.append((a - (a @ F @ f) * e - (a @ F @ e) * f) % 3)
anisotropic = next((w for w in W if quadratic(w)), None)
if anisotropic is None:
    anisotropic = next((u + v) % 3 for u in W for v in W if quadratic((u + v) % 3))
assert anisotropic @ F @ e % 3 == 0 and anisotropic @ F @ f % 3 == 0
rf = radical(f, anisotropic)
image = rf @ e % 3
normalizer = int(e @ F @ image % 3)
assert normalizer != 0
z = normalizer * image % 3
parameter = (z - f - (f @ F @ z) * e) % 3
bridge = radical(e, -parameter % 3) @ rf % 3
assert np.array_equal(bridge @ e % 3, normalizer * f % 3)
assert np.array_equal(bridge.T @ F @ bridge % 3, F)
print('PASS: explicit two-radical matrix sends the line of e to the opposite line')

# Directly multiply the recorded ordinary reflections, without importing
# the program that constructed the factorization.
spinors = []
for g, factors in zip(generators, certificate['all_reflection_factorizations']):
    remaining = g.copy()
    spinor = 1
    for vector in factors:
        v = np.array(vector, dtype=np.int64)
        norm = int(v @ F @ v % 3)
        assert norm != 0
        reflection = (I - 2 * norm * np.outer(v, v @ F)) % 3
        assert determinant(reflection) == 2
        remaining = reflection @ remaining % 3
        spinor = spinor * quadratic(v) % 3
    assert np.array_equal(remaining, I) and len(factors) % 2 == 0
    spinors.append(spinor)
assert spinors == certificate['all_generator_spinor_norms']
print('PASS: all direct reflection products; spinor counts', {x: spinors.count(x) for x in (1, 2)})

# Actual A=F3[C3^2]-freeness and determinant correction.
H1, H2 = translations
for h in translations:
    assert np.array_equal(h @ h @ h % 3, I)
    assert np.array_equal(h.T @ F @ h % 3, F)
assert np.array_equal(H1 @ H2 % 3, H2 @ H1 % 3)
group = [np.linalg.matrix_power(H1, a) @ np.linalg.matrix_power(H2, b) % 3
         for a in range(3) for b in range(3)]
assert len({g.tobytes() for g in group}) == 9
norm = sum(group) % 3
assert rank(norm) == 2
columns = []
for i in range(18):
    candidate = columns + [i]
    if rank(norm[:, candidate]) > len(columns):
        columns.append(i)
    if len(columns) == 2:
        break
free_basis = np.stack([g @ I[:, i] % 3 for i in columns for g in group], axis=1)
assert rank(free_basis) == 18
print(f'PASS: norm rank2 and explicit free A^2 basis from standard columns {columns}')

BN = F @ norm % 3
assert np.array_equal(BN, BN.T)
v = next((a for a in I if a @ BN @ a % 3), None)
if v is None:
    v = next((a + b) % 3 for a in I for b in I if (a + b) @ BN @ (a + b) % 3)
hvv = np.array([v @ F @ g @ v % 3 for g in group], dtype=np.int64)
assert sum(hvv) % 3 != 0

def algebra_product(a, b):
    result = np.zeros(9, dtype=np.int64)
    for i in range(9):
        for j in range(9):
            k = ((i // 3 + j // 3) % 3) * 3 + (i % 3 + j % 3) % 3
            result[k] += a[i] * b[j]
    return result % 3

convolution = np.stack([algebra_product(hvv, x) for x in np.eye(9, dtype=np.int64)], axis=1)
hvv_inverse = inverse(convolution)[:, 0]
assert np.array_equal(algebra_product(hvv, hvv_inverse), np.eye(9, dtype=np.int64)[:, 0])
w = sum(int(a) * g @ v for a, g in zip(hvv_inverse, group)) % 3
coefficient_map = np.stack([F @ g @ v % 3 for g in group])
action_map = np.stack([g @ w % 3 for g in group], axis=1)
correction = (I - 2 * action_map @ coefficient_map) % 3
assert np.array_equal(correction @ correction % 3, I)
assert np.array_equal(correction.T @ F @ correction % 3, F)
assert determinant(correction) == 2
assert rank(correction - I) == 9 and rank(correction + I) == 9
for h in translations:
    assert np.array_equal(correction @ h % 3, h @ correction % 3)
print('PASS: explicit hermitian reflection centralizes C3^2, preserves F, and has determinant -1')
print('Eigenspace dimensions: +1=9, -1=9')

record = {
    'scope': 'Independent actual-matrix verification, two-radical orbit bridge, and determinant correction',
    'input_sha256': {name: hashlib.sha256((D / name).read_bytes()).hexdigest()
                     for name in ('translation_quaternion_homology.npz',
                                  'translation_quaternion_image.npz',
                                  'translation_quaternion_radical_certificate.json')},
    'form_determinant': determinant(F),
    'spinor_counts': {str(x): spinors.count(x) for x in (1, 2)},
    'first_nonsquare_spinor_index': spinors.index(2),
    'anisotropic_bridge_vector': anisotropic.tolist(),
    'bridge_matrix': bridge.tolist(),
    'free_basis_standard_columns': columns,
    'hermitian_vector': v.tolist(),
    'hermitian_norm': hvv.tolist(),
    'hermitian_norm_inverse': hvv_inverse.tolist(),
    'determinant_correction_matrix': correction.tolist(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2) + '\n')
print('PASS. The group equality follows from the written two-radical proof and Taylor11.46/11.51.')

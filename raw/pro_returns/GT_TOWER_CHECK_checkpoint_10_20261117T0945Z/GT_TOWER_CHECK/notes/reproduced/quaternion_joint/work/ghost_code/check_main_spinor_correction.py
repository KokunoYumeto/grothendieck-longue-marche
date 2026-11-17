#!/usr/bin/env python3
"""Explicit SO centralizer element with nonsquare spinor norm."""
from pathlib import Path
import json
import runpy
import numpy as np

base = runpy.run_path(str(Path(__file__).with_name('check_main_orthogonal_generation.py')))
F, I, group = base['F'], base['I'], base['group']
norm = base['norm']
rank, determinant, inverse = base['rank'], base['determinant'], base['inverse']
quadratic, algebra_product = base['quadratic'], base['algebra_product']
H1, H2 = base['translations']


def hermitian_reflection(v):
    h = np.array([v @ F @ g @ v % 3 for g in group], dtype=np.int64)
    alpha = int(sum(h) % 3)
    assert alpha != 0
    multiplication = np.stack([algebra_product(h, a) for a in np.eye(9, dtype=np.int64)], axis=1)
    hinverse = inverse(multiplication)[:, 0]
    w = sum(int(a) * g @ v for a, g in zip(hinverse, group)) % 3
    coefficient_map = np.stack([F @ g @ v % 3 for g in group])
    action_map = np.stack([g @ w % 3 for g in group], axis=1)
    r = (I - 2 * action_map @ coefficient_map) % 3
    orbit = np.stack([g @ v % 3 for g in group], axis=1)
    assert rank(orbit) == 9 and np.array_equal(r @ orbit % 3, -orbit % 3)
    gram = orbit.T @ F @ orbit % 3
    assert determinant(gram) == alpha
    predicted_spinor = 2 * determinant(gram) % 3
    assert determinant(r) == 2 and np.array_equal(r.T @ F @ r % 3, F)
    assert np.array_equal(r @ r % 3, I)
    for h0 in (H1, H2):
        assert np.array_equal(r @ h0 % 3, h0 @ r % 3)
    return r, alpha, predicted_spinor


candidates = list(I) + [(a + b) % 3 for a in I for b in I]
vectors = [next(v for v in candidates if v @ F @ norm @ v % 3 == alpha)
           for alpha in (1, 2)]
reflections = [hermitian_reflection(v) for v in vectors]
correction = reflections[0][0] @ reflections[1][0] % 3
assert determinant(correction) == 1
assert np.array_equal(correction.T @ F @ correction % 3, F)
assert all(np.array_equal(correction @ h % 3, h @ correction % 3) for h in (H1, H2))
assert reflections[0][2] * reflections[1][2] % 3 == 2

# Independent ordinary-reflection factorization of the final product.
orthogonal_basis = np.array(base['certificate']['orthogonal_basis'], dtype=np.int64)
remaining, spinor, ordinary_factors = correction.copy(), 1, []
for b in orthogonal_basis.T:
    u = remaining @ b % 3
    if np.array_equal(u, b):
        continue
    difference = (u - b) % 3
    choices = [difference] if quadratic(difference) else [(u + b) % 3, b]
    for v in choices:
        bilinear_norm = int(v @ F @ v % 3)
        assert bilinear_norm != 0
        r = (I - 2 * bilinear_norm * np.outer(v, v @ F)) % 3
        remaining = r @ remaining % 3
        spinor = spinor * quadratic(v) % 3
        ordinary_factors.append(v.tolist())
    assert np.array_equal(remaining @ b % 3, b)
assert np.array_equal(remaining, I)
assert len(ordinary_factors) % 2 == 0 and spinor == 2
print('NEW PASS: augmentation norms1,2 give hermitian-reflection spinors2,1')
print('NEW PASS: their product centralizes the actual H=C3^2, has determinant1 and spinor2')
print(f'NEW PASS: independent ordinary-reflection factorization has {len(ordinary_factors)} factors and spinor2')

Path(__file__).with_suffix('.json').write_text(json.dumps({
    'scope':'Actual nonsquare-spinor element of the special orthogonal centralizer',
    'vectors':[v.tolist() for v in vectors],
    'augmentation_norms':[r[1] for r in reflections],
    'individual_spinor_norms':[r[2] for r in reflections],
    'hermitian_reflection_matrices':[r[0].tolist() for r in reflections],
    'special_orthogonal_correction':correction.tolist(),
    'ordinary_reflection_factorization':ordinary_factors,
    'determinant':1,'spinor_norm':2,
},indent=2)+'\n')

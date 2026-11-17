#!/usr/bin/env python3
"""Exact matrix certificate for a finite CM descent/forgetting discrepancy.

Source membership with trivial solvable forgetting coordinates is proved
by the actual perfect-image map of A.4.23, with those coordinates joined.
This script checks the named centralizer element and its non-inner output.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent / 'work'
inputs = {
    'homology': WORK / 'tower_code/translation_quaternion_homology.npz',
    'form': WORK / 'tower_code/translation_quaternion_image.npz',
    'reflection': WORK / 'ghost_code/check_main_spinor_correction.json',
    'quotient': WORK / 'ghost_code/check_main_normalizer_joint.npz',
}
H = np.load(inputs['homology'])['H18'].astype(np.int64) % 3
F = np.load(inputs['form'])['form'].astype(np.int64) % 3
R = np.array(json.loads(inputs['reflection'].read_text())[
    'hermitian_reflection_matrices'][0], dtype=np.int64) % 3
qdata = np.load(inputs['quotient'])
phi = qdata['quotient_map'].astype(np.int64) % 3
T = qdata['quotient_free_basis'].astype(np.int64) % 3
I = np.eye(18, dtype=np.int64)
I6 = np.eye(6, dtype=np.int64)

def rref(matrix):
    a = np.array(matrix, dtype=np.int64).copy() % 3
    row, pivots = 0, []
    for col in range(a.shape[1]):
        choices = np.flatnonzero(a[row:, col])
        if not len(choices):
            continue
        pivot = row + int(choices[0])
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = int(a[row, col]) * a[row] % 3
        for k in range(len(a)):
            if k != row:
                a[k] = (a[k] - a[k, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a, pivots

def inverse(a):
    n = len(a)
    reduced, pivots = rref(np.hstack((a, np.eye(n, dtype=np.int64))))
    assert pivots[:n] == list(range(n))
    return reduced[:, n:]

assert np.array_equal(R @ R % 3, I)
assert np.array_equal(R.T @ F @ R % 3, F)
assert all(np.array_equal(R @ h % 3, h @ R % 3) for h in H)
P = 2 * (I - R) % 3
assert np.array_equal(P @ P % 3, P)
assert len(rref(P)[1]) == 9
assert np.array_equal(P.T @ F % 3, F @ P % 3)
assert all(np.array_equal(P @ h % 3, h @ P % 3) for h in H)
K = (H[0] @ P + H[0] @ H[0] @ (I - P)) % 3
assert not np.array_equal(K, I)
assert np.array_equal(K @ K @ K % 3, I)
assert np.array_equal(K.T @ F @ K % 3, F)
assert all(np.array_equal(K @ h % 3, h @ K % 3) for h in H)
# Odd order makes both determinant and the order-two spinor character one.
assert len(rref(K)[1]) == 18

_, columns = rref(phi)
right_inverse = np.zeros((18, 6), dtype=np.int64)
right_inverse[columns] = inverse(phi[:, columns])
assert np.array_equal(phi @ right_inverse % 3, I6)

def quotient(a):
    answer = phi @ a @ right_inverse % 3
    assert np.array_equal(answer @ phi % 3, phi @ a % 3)
    return answer

K6 = quotient(K)
H6 = [quotient(h) for h in H]
deck = []
for i in range(3):
    for j in range(3):
        value = I6.copy()
        for _ in range(i):
            value = value @ H6[0] % 3
        for _ in range(j):
            value = value @ H6[1] % 3
        deck.append(value)
inner = [sign * h % 3 for sign in (1, 2) for h in deck]
assert len({a.tobytes() for a in inner}) == 18
assert all(not np.array_equal(K6, a) for a in inner)
adapted = inverse(T) @ K6 @ T % 3
assert np.array_equal(adapted[:2], I6[:2])
assert np.array_equal(adapted[2:, 2:], I6[2:, 2:])
coefficients = adapted[2:, :2].reshape(2, 2, 2)
assert any(not any(np.array_equal(a, scalar * np.eye(2, dtype=np.int64) % 3)
                   for scalar in range(3)) for a in coefficients)
record = {
    'scope': __doc__,
    'input_sha256': {key: hashlib.sha256(path.read_bytes()).hexdigest()
                     for key, path in inputs.items()},
    'reflection': R.tolist(), 'orthogonal_projector': P.tolist(),
    'centralizer_element18': K.tolist(), 'element_order': 3,
    'determinant': 1, 'spinor_norm': 1,
    'quotient_map': phi.tolist(), 'quotient_element6': K6.tolist(),
    'quotient_H_generators': [h.tolist() for h in H6],
    'all18_inner_module_values': [a.tolist() for a in inner],
    'adapted_element6': adapted.tolist(),
    'first_order_coefficients': coefficients.tolist(),
    'outside_full_inner_module_kernel': True,
    'all_assertions_passed': True,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2) + '\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'), projector=P,
                    centralizer_element=K, quotient_element=K6,
                    quotient_map=phi, adapted_element=adapted)
print('PASS rank9 orthogonal H-linear projector and exact order3 centralizer element')
print('PASS induced six-dimensional quotient map and all18 inner-kernel comparisons')
print('PASS first-order coefficients:', coefficients.tolist())
print('PASS this Omega centralizer element has nontrivial outer image in Pc')

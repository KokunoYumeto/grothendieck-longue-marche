#!/usr/bin/env python3
"""Independent literal-source audit of the faithful joint normalizer image.

Reconstructs the 73-dimensional source maps from free words, forms all 96
Schreier generators, restricts the actual 18-dimensional multiplicity
space, and independently enumerates the six-dimensional quotient image
together with its signed period modulo twelve.
"""
from pathlib import Path
import hashlib
import itertools
import json
import runpy
import numpy as np

here = Path(__file__).resolve().parent
source = runpy.run_path(str(here / 'check_main_faithful_detector.py'))
orth = runpy.run_path(str(here / 'check_main_orthogonal_generation.py'))
D = source['D']
rank, inverse, determinant = orth['rank'], orth['inverse'], orth['determinant']
rref = orth['reduce_rows']
F, H18, I18 = orth['F'], orth['translations'], orth['I']
CB = source['CB']
I73 = np.eye(73, dtype=np.int64)
cover = source['cover']
basis73 = source['basis73']
rewrite73, substitute = source['rewrite73'], source['substitute']
qmul, qinv, qword = source['multiply'], source['inverses'], source['quotient_word']


def power(a, n):
    result = np.eye(len(a), dtype=np.int64)
    for _ in range(n):
        result = result @ a % 3
    return result


def restrict(a, basis):
    _, rows = rref(basis.T)
    answer = inverse(basis[rows]) @ (a @ basis % 3)[rows] % 3
    assert np.array_equal(basis @ answer % 3, a @ basis % 3)
    return answer


def homology(word):
    result = np.zeros(73, dtype=np.int64)
    for letter in rewrite73(word):
        result[abs(letter)-1] += 1 if letter > 0 else -1
    return result % 3


source4 = cover['normalizer_automorphisms'] + cover['deck_automorphisms']
G73 = [np.stack([homology(substitute(w, g)) for w in basis73], axis=1)
       for g in source4]
G73i = [inverse(g) for g in G73]
Sigma4 = [((1,), (2, 1)), ((1, -2), (2,)),
          ((1,), (1, 2, -1)), ((2, 1, -2), (2,))]
quaternion_sections = [(), (1,), (2,), (1, 2),
                      (1, 1), (1, 1, 1), (1, 1, 2), (1, 1, 1, 2)]
qa = [tuple(qword(substitute(w, g), [1, 2]) for w in quaternion_sections)
      for g in Sigma4]
assert all(sorted(a) == list(range(8)) for a in qa)
I2 = np.eye(2, dtype=np.int64)
period4 = [np.array([[1, 1], [0, 1]], dtype=np.int64),
           np.array([[1, 0], [-1, 1]], dtype=np.int64), I2, I2]


def inverse12(a):
    assert determinant(a % 3) == 1
    return np.array([[a[1, 1], -a[0, 1]], [-a[1, 0], a[0, 0]]]) % 12


aut = [tuple(range(8))]
aut_index = {aut[0]: 0}
paths = [()]
representatives73 = [I73]
period_reps = [I2]
for k, alpha in enumerate(aut):
    for j, beta in enumerate(qa):
        gamma = tuple(alpha[beta[i]] for i in range(8))
        if gamma not in aut_index:
            aut_index[gamma] = len(aut)
            aut.append(gamma)
            paths.append(paths[k] + (j + 1,))
            representatives73.append(representatives73[k] @ G73[j] % 3)
            period_reps.append(period_reps[k] @ period4[j] % 12)
assert len(aut) == 24
representatives73i = [inverse(g) for g in representatives73]

# Our source-to-target homomorphism, independently rebuilt from free words.
raw_phi = source['multiplicity_map']
_, phi_rows = rref(raw_phi.T)
phi = raw_phi[phi_rows]
assert phi.shape == (6, 18) and rank(phi) == 6
_, phi_cols = rref(phi)
phi_right_inverse = np.zeros((18, 6), dtype=np.int64)
phi_right_inverse[phi_cols] = inverse(phi[:, phi_cols])
assert np.array_equal(phi @ phi_right_inverse % 3, np.eye(6, dtype=np.int64))


def quotient(a):
    b = phi @ a % 3 @ phi_right_inverse % 3
    assert np.array_equal(b @ phi % 3, phi @ a % 3)
    return b


H6 = [quotient(h) for h in H18]
I6 = np.eye(6, dtype=np.int64)
N1, N2 = [(h - I6) % 3 for h in H6]
free_columns = orth['columns']
vectors18 = I18[:, free_columns]
V = phi @ vectors18 % 3
T = np.hstack((V, N1 @ V % 3, N2 @ V % 3))
assert rank(T) == 6
Ti = inverse(T)
reduced_form = vectors18.T @ F @ orth['norm'] @ vectors18 % 3
assert determinant(reduced_form) == 1
assert all(v @ reduced_form @ v % 3 != 0
           for v in (np.array(a, dtype=np.int64)
                     for a in itertools.product(range(3), repeat=2)) if np.any(v))

orthogonal_basis = np.array(orth['certificate']['orthogonal_basis'], dtype=np.int64)
assert rank(orthogonal_basis) == 18
diagonal = orthogonal_basis.T @ F @ orthogonal_basis % 3
assert np.array_equal(diagonal, np.diag(np.diag(diagonal)))


def spinor(a):
    remaining, value = a.copy(), 1
    for v in orthogonal_basis.T:
        u = remaining @ v % 3
        if np.array_equal(u, v):
            continue
        difference = (u-v) % 3
        choices = [difference] if orth['quadratic'](difference) else [(u+v) % 3, v]
        for w in choices:
            norm = int(w @ F @ w % 3)
            assert norm
            reflection = (I18 - 2*norm*np.outer(w, w @ F)) % 3
            remaining = reflection @ remaining % 3
            value = value * orth['quadratic'](w) % 3
        assert np.array_equal(remaining @ v % 3, v)
    assert np.array_equal(remaining, I18)
    return value


def eta(q):
    a = q % 4
    assert np.array_equal(a % 2, I2)
    alpha, beta, gamma = ((int(a[0, 0])-1) % 4)//2, int(a[0, 1])//2, int(a[1, 0])//2
    assert a[1, 1] == a[0, 0]
    return pow(2, alpha+beta+gamma, 3)


words, actual18, matrices6, periods, spinors = [], [], [], [], []
for k, alpha in enumerate(aut):
    for j, beta in enumerate(qa):
        z = aut_index[tuple(alpha[beta[i]] for i in range(8))]
        a = representatives73[k] @ G73[j] % 3 @ representatives73i[z] % 3
        g = restrict(a, CB)
        q = period_reps[k] @ period4[j] % 12 @ inverse12(period_reps[z]) % 12
        word = paths[k] + (j+1,) + tuple(-x for x in paths[z][::-1])
        assert np.array_equal(g.T @ F @ g % 3, F) and determinant(g) == 1
        assert np.array_equal(q % 2, I2)
        for h, translation in enumerate(H18):
            rhs = power(H18[0], int(q[0, h] % 3)) @ power(H18[1], int(q[1, h] % 3)) % 3
            assert np.array_equal(g @ translation % 3 @ inverse(g) % 3, rhs)
        theta = spinor(g)
        assert theta == eta(q)
        words.append(word)
        actual18.append(g)
        matrices6.append(Ti @ quotient(g) % 3 @ T % 3)
        periods.append(q)
        spinors.append(theta)
assert len(words) == 96
retained = json.loads((D/'quaternion_compact_normalizer_joint.json').read_text())
assert [list(w) for w in words] == retained['quaternion_automorphism_kernel_words']
bridge = np.load(D/'quaternion_compact_normalizer_bridge.npz')
assert np.array_equal(np.array(actual18), bridge['source_kernel_matrices18'] % 3)
retained_joint = np.load(D/'quaternion_compact_normalizer_joint.npz')
change = bridge['multiplicity_quotient_map'] @ phi_right_inverse % 3 @ T % 3
assert rank(change) == 6
for g, recorded in zip(matrices6, retained_joint['actual_generators']):
    assert np.array_equal(change @ g % 3 @ inverse(change) % 3, recorded % 3)
assert np.array_equal(np.array(periods), retained_joint['periods'])
print('NEW PASS all 96 source words independently rebuilt on rank73, with exact 18-to-6 intertwiners')
print('NEW PASS all 96 determinant-one isometries: H-label equals signed period mod3; spinor equals eta(mod4)')


def split(a, q):
    result = np.zeros((6, 6), dtype=np.int64)
    result[:2, :2] = a
    for i in range(2):
        for j in range(2):
            result[2+2*i:4+2*i, 2+2*j:4+2*j] = q[i, j]*a % 3
    return result


def get_coordinates(g, q):
    a = g[:2, :2]
    assert determinant(a) == 1 and np.array_equal(a.T @ reduced_form @ a % 3, reduced_form)
    c = g @ inverse(split(a, q % 3)) % 3
    assert np.array_equal(c[:2], I6[:2]) and np.array_equal(c[2:, 2:], I6[2:, 2:])
    return c[2:, :2].reshape(-1), a, q


def action(a, q, v):
    return (split(a, q)[2:, 2:] @ np.array(v).reshape(4, 2) % 3 @ inverse(a) % 3).reshape(-1)


def multiply(g, h):
    c, a, q = g
    e, b, r = h
    return (c+action(a, q % 3, e)) % 3, a @ b % 3, q @ r % 12


generators = [get_coordinates(g, q) for g, q in zip(matrices6, periods)]
identity = (np.zeros(8, dtype=np.int64), I2, I2)
base, reps = [(I2, I2)], [identity]
index = {(I2.tobytes(), I2.tobytes()): 0}
for k, _ in enumerate(base):
    for g in generators:
        c, a, q = multiply(reps[k], g)
        key = a.tobytes(), q.tobytes()
        if key not in index:
            index[key] = len(base)
            base.append((a, q))
            reps.append((c, a, q))
assert len(base) == 384
assert len({q.tobytes() for a, q in base}) == 192
assert len({a.tobytes() for a, q in base}) == 4
assert all(sum(np.array_equal(q, r) for a, q in base) == 2
           for r in periods)
rows = []
for representative in reps:
    for generator in generators:
        c, a, q = multiply(representative, generator)
        z = index[a.tobytes(), q.tobytes()]
        rows.append((c-reps[z][0]) % 3)
reduced, pivots = rref(rows)
kernel = reduced[:len(pivots)]
assert len(rows) == 36864 and len(pivots) == 6
for v in kernel:
    for coefficient in v.reshape(2, 2, 2):
        assert np.array_equal(coefficient.T @ reduced_form % 3,
                              reduced_form @ coefficient % 3)
for c, a, q in generators:
    assert rank(np.vstack((kernel, [action(a, q % 3, v) for v in kernel]))) == 6
print('NEW PASS independent joint census: base384, 36864 complete Schreier rows, first-order rank6')
print('NEW PASS binary form anisotropic; all six first-order directions satisfy the exact self-adjoint equations')
print('NEW PASS exact joint order384*3^6 =', 384*3**6)

record = {
    'scope': 'Independent original-source/orthogonal/first-order joint normalizer audit',
    'source_words': [list(w) for w in words],
    'word_count': len(words), 'period_order': 192, 'base_order': 384,
    'complete_Schreier_rows': len(rows), 'first_order_kernel_rank': 6,
    'exact_order': 384*3**6, 'constant_group_order': 4,
    'reduced_binary_form': reduced_form.tolist(),
    'spinor_counts': {str(i): spinors.count(i) for i in (1, 2)},
    'input_sha256': {name: hashlib.sha256((D/name).read_bytes()).hexdigest()
                     for name in ('translation_cover_basis.json',
                                  'translation_quaternion_homology.npz',
                                  'modular_quaternion_compact_setup.npz',
                                  'quaternion_compact_normalizer_joint.npz')},
}
Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
                    source_matrices73=np.array(G73), source_kernel_matrices18=np.array(actual18),
                    quotient_map=phi, quotient_free_basis=T, source_kernel_matrices6=np.array(matrices6),
                    periods=np.array(periods), first_order_kernel=kernel,
                    base_constant=np.array([a for a,q in base]), base_period=np.array([q for a,q in base]))

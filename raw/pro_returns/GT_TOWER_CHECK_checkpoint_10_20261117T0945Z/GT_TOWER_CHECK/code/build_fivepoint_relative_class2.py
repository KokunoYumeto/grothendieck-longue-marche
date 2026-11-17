#!/usr/bin/env python3
"""Actual class-two exponent-three quotient of the C4^5 five-point kernel.

The source kernel is F129 semidirect F17.  All 2193 defining actions
are rewritten literally in the 129-generator free fibre, and then
collected through class two over F3.  This is a finite quotient of the
actual five-point group, not a replacement of its Brunnian kernel by
an arbitrary vector space.
"""
from pathlib import Path
import json
import hashlib
import numpy as np
from fivepoint_relative_tools import (abelian_schreier, fibre_action,
                                     subst, inverse, relations)

HERE = Path(__file__).resolve().parent
fs, ft, floops, rewrite_f = abelian_schreier(3)
bs, bt, bloops, rewrite_b = abelian_schreier(2)
assert len(floops) == 129 and len(bloops) == 17
actions = [fibre_action(w) for w in bloops]
print('PASS actual kernel presentation F129 semidirect F17', flush=True)
print('Base generator word lengths:', [len(w) for w in bloops], flush=True)
print('Maximum original-fibre action-word length:', max(len(w) for a in actions for w in a), flush=True)
rewritten = []
linear = []
for i, action in enumerate(actions):
    for j, loop in enumerate(floops):
        image = subst(loop, action)
        endpoint, word = rewrite_f(image)
        assert endpoint == 0
        rewritten.append(word)
        row = np.zeros(129, dtype=np.int16)
        row[j] = 1
        for letter in word:
            row[abs(letter) - 1] -= 1 if letter > 0 else -1
        linear.append(row % 3)
linear = np.array(linear, dtype=np.int16)
assert linear.shape == (2193, 129)
print('PASS all 2193 literal action relators; rewritten length sum/max:',
      sum(map(len, rewritten)), max(map(len, rewritten)), flush=True)

# Row reduction retains coefficients expressing every original linear row
# in an explicitly selected original-row basis.
basis = []
pivots = []
basis_source_rows = []
coefficients = np.zeros((2193, 129), dtype=np.int16)
for i, row0 in enumerate(linear):
    row = row0.copy()
    coeff = np.zeros(129, dtype=np.int16)
    for k, (pivot, b) in enumerate(zip(pivots, basis)):
        factor = int(row[pivot])
        if factor:
            row = (row - factor * b) % 3
            coeff = (coeff + factor * coefficients[basis_source_rows[k]]) % 3
    nz = np.flatnonzero(row)
    if len(nz):
        pivot = int(nz[0])
        factor = pow(int(row[pivot]), -1, 3)
        row = row * factor % 3
        k = len(basis)
        # The normalized row is factor*(original - accumulated originals).
        own_coeff = -factor * coeff % 3
        own_coeff[k] = (own_coeff[k] + factor) % 3
        basis.append(row)
        pivots.append(pivot)
        basis_source_rows.append(i)
        coefficients[i] = own_coeff
    else:
        coefficients[i] = coeff

# Recompute coefficients in the selected ORIGINAL basis using its pivot
# submatrix, avoiding confusion with the normalized echelon basis.
rank_linear = len(basis)
assert rank_linear == 66
original_basis = linear[basis_source_rows]
square = original_basis[:, pivots].copy()
aug = np.concatenate([square, np.eye(rank_linear, dtype=np.int16)], axis=1)
for k in range(rank_linear):
    nz = np.flatnonzero(aug[k:, k]); assert len(nz)
    j = k + int(nz[0]); aug[[k, j]] = aug[[j, k]]
    aug[k] = aug[k] * pow(int(aug[k, k]), -1, 3) % 3
    for j in range(rank_linear):
        if j != k and aug[j, k]:
            aug[j] = (aug[j] - int(aug[j, k]) * aug[k]) % 3
square_inverse = aug[:, rank_linear:]
coordinates = linear[:, pivots] @ square_inverse % 3
assert np.array_equal(coordinates @ original_basis % 3, linear)

free = [j for j in range(129) if j not in pivots]
P = np.zeros((129, len(free)), dtype=np.int16)
P[free] = np.eye(len(free), dtype=np.int16)
P[pivots] = -square_inverse @ original_basis[:, free] % 3
assert len(free) == 63 and not np.any(linear @ P % 3)
print('PASS exact H1 projection: 129 fibre generators ->63, joined to17 base generators', flush=True)

# BCH logarithms in class two, where 1/2=2 in F3.
upper_f = np.triu_indices(63, 1)
upper_h = np.triu_indices(80, 1)
relator_central = []
for r, word in enumerate(rewritten):
    v = np.zeros(129, dtype=np.int64)
    z = np.zeros((129, 129), dtype=np.int64)
    for letter in word:
        j = abs(letter) - 1
        sign = 1 if letter > 0 else -1
        z[:, j] += 2 * sign * v
        z[j, :] -= 2 * sign * v
        v[j] += sign
    v %= 3
    z %= 3
    projected_v = v @ P % 3
    projected_z = P.T @ z @ P % 3
    base, fibre = divmod(r, 129)
    ej = P[fibre]
    # log(b_i f_j b_i^-1 phi(f_j)^-1).
    central = np.zeros((80, 80), dtype=np.int16)
    central[:63, :63] = (-projected_z -
                          2 * (np.outer(ej, projected_v) - np.outer(projected_v, ej))) % 3
    central[63 + base, :63] = ej
    central[:63, 63 + base] = -ej % 3
    relator_central.append(central[upper_h])
    if (r + 1) % 256 == 0:
        print('Collected relators', r + 1, flush=True)
relator_central = np.array(relator_central, dtype=np.int16)
assert relator_central.shape == (2193, 3160)
# A linear-zero combination is the actual remaining central relation.
central_relations = (relator_central - coordinates @ relator_central[basis_source_rows]) % 3
assert not np.any(central_relations[basis_source_rows])
print('PASS exact linear elimination with all central correction terms retained', flush=True)

central_basis = []
central_pivots = []
central_source_rows = []
for i, original in enumerate(central_relations):
    row = original.copy()
    for pivot, b in zip(central_pivots, central_basis):
        factor = int(row[pivot])
        if factor:
            row = (row - factor * b) % 3
    nz = np.flatnonzero(row)
    if len(nz):
        pivot = int(nz[0])
        row = row * pow(int(row[pivot]), -1, 3) % 3
        central_basis.append(row)
        central_pivots.append(pivot)
        central_source_rows.append(i)
central_rank = len(central_basis)
central_dimension = 3160 - central_rank
print('RESULT relative class-two Lie dimensions:', 80, central_dimension,
      'central relation rank', central_rank, flush=True)

offsets = np.cumsum([0] + [len(w) for w in rewritten])
flat_words = np.array([i for w in rewritten for i in w], dtype=np.int16)
np.savez_compressed(HERE / 'build_fivepoint_relative_class2.npz',
                    linear=linear, projection=P,
                    linear_basis_sources=np.array(basis_source_rows),
                    linear_coordinates=coordinates,
                    relator_central=relator_central,
                    central_relations=central_relations,
                    central_basis=np.array(central_basis, dtype=np.int16),
                    central_pivots=np.array(central_pivots),
                    central_basis_sources=np.array(central_source_rows),
                    rewritten_offsets=offsets, rewritten_letters=flat_words)
output = {'source_relations': relations, 'abelian_base_order': 1024,
          'fibre_schreier_words': floops, 'base_schreier_words': bloops,
          'base_fibre_actions': actions, 'relator_count': 2193,
          'rewritten_length_sum': int(len(flat_words)),
          'rewritten_length_max': max(map(len, rewritten)),
          'linear_relation_rank': rank_linear, 'first_homology_dimension': 80,
          'central_relation_rank': central_rank, 'central_dimension': central_dimension,
          'relative_kernel_order': '3^%d' % (80 + central_dimension),
          'scope': 'Actual Gamma_0,5/(gamma3(J) J^3), J=kernel of abelianization modulo4. No shadow census or CM exclusion is inferred.'}
(HERE / 'build_fivepoint_relative_class2.json').write_text(json.dumps(output, indent=2) + '\n')

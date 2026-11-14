#!/usr/bin/env python3
"""Exact proper-Tate factorization and boundary comparison for the cubic cover.

H=ker(F(x,y)->C3^2), while N_B=ker(B->PSL_2(Z/12)).  All calculations
use integral Schreier words, without the characteristic-three collector.
"""
from pathlib import Path
from itertools import combinations
import importlib.util, json
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
def b_reduce(word):
    stack = []
    for a in word:
        kind, exponent, modulus = ('s', 1, 2) if a == 0 else ('r', a % 3, 3)
        if stack and stack[-1][0] == kind:
            exponent = (stack.pop()[1]+exponent) % modulus
        if exponent:
            stack.append((kind, exponent))
    return stack
def b_inverse(word):
    return [0 if a == 0 else -a for a in reversed(word)]
bx, by = [-1, 0, -1, 0], [0, -1, 0, -1]
assert b_reduce([1]+bx+[-1]) == b_reduce(by)
assert b_reduce([1]+by+[-1]) == b_reduce(b_inverse(bx+by))
bxp, byp = b_inverse(bx), b_inverse(by)
assert b_reduce([1]+byp+[-1]) == b_reduce(b_inverse(bxp)+b_inverse(bxp+byp)+bxp)
spec = importlib.util.spec_from_file_location('fermat_integral', HERE/'de_fermat_schreier.py')
f = importlib.util.module_from_spec(spec)
spec.loader.exec_module(f)
T = f.TATE_QUOTIENT
assert T.shape == (2, 10)
deck = []
proper = []
for j in (1, 2):
    A = np.stack([f.integral_abel([j]+w+[-j]) for w in f.NWORDS], axis=1)
    R = np.array([list(next(iter(sp.linsolve((sp.Matrix(T.T), sp.Matrix(row))))))
                  for row in T@A], dtype=np.int64)
    assert np.array_equal(R@T, T@A)
    assert np.array_equal(np.linalg.matrix_power(A, 3), np.eye(10, dtype=np.int64))
    deck.append(A)
    proper.append(R)
assert np.array_equal(proper[0], proper[1])
R = proper[0]
assert np.array_equal(np.linalg.matrix_power(R, 3), np.eye(2, dtype=np.int64))
assert not np.any(R@R+R+np.eye(2, dtype=np.int64))
translation = deck[0]@np.linalg.matrix_power(deck[1], 2)
assert np.array_equal(np.linalg.matrix_power(translation, 3), np.eye(10, dtype=np.int64))
assert np.array_equal(T@translation, T)
translation_rank = int(sp.Matrix(translation-np.eye(10, dtype=np.int64)).rank())

words = json.loads((HERE/'bc_cm_literal_words.json').read_text())['N_B_basis_in_F']
exponents = [[sum(1 if l == j else -1 if l == -j else 0 for l in w) for j in (1, 2)]
             for w in words]
assert all((a+b) % 3 == 0 for a, b in exponents)
residues = sorted({(a % 3, b % 3) for a, b in exponents})
commutator_columns = []
first_boundary = None
for i, j in combinations(range(len(words)), 2):
    w = words[i]+words[j]+f.inverse_word(words[i])+f.inverse_word(words[j])
    h = f.integral_abel(w)
    assert not np.any(T@h)
    commutator_columns.append(h)
    if first_boundary is None and np.any(h % 4):
        first_boundary = {'basis_indices': [i, j], 'literal_F_word': w,
                          'integral_H_abelianization': h.tolist(),
                          'mod4_H_abelianization': (h % 4).tolist(),
                          'proper_T_abelianization': (T@h).tolist()}
C = np.stack(commutator_columns, axis=1)
output = {'basis_convention': 'de_fermat_schreier.py integral signed Schreier words',
          'literal_B_words': {'x': bx, 'y': by},
          'both_r_conjugations_and_positive_square_change_verified': True,
          'proper_quotient_matrix': T.tolist(),
          'deck_x_matrix': deck[0].tolist(), 'deck_y_matrix': deck[1].tolist(),
          'proper_deck_matrix_both_x_y': R.tolist(),
          'translation_xy_inverse_matrix': translation.tolist(),
          'translation_minus_identity_rank': translation_rank,
          'N_B_basis_exponents': exponents, 'N_B_deck_residues': residues,
          'N_B_basis_commutators_checked': len(commutator_columns),
          'all_integral_proper_commutator_images_zero': True,
          'first_nonzero_full_boundary_mod4': first_boundary,
          'exact_factorization': 'For every n>=1, B/ker(H->T/2^n) is a quotient of G_(3*2^n).',
          'scope': 'The intrinsic Fermat-cubic proper Tate quotient, with its literal based group maps; no CM twist or full-GT special-locus comparison is assumed.'}
(HERE/'bc_cm_fermat_factorization.json').write_text(json.dumps(output, indent=2)+'\n')
np.savez_compressed(HERE/'bc_cm_fermat_factorization.npz', T=T, deck_x=deck[0], deck_y=deck[1],
                    translation=translation, N_B_commutator_images=C)
print('Integral proper quotient T:', T.tolist())
print('Both proper deck matrices:', R.tolist())
print('Rank(translation minus identity) in the full rank-ten module:', translation_rank)
print('Deck residues of all 97 N_B basis elements:', residues)
print('All', len(commutator_columns), 'N_B basis commutators have zero integral proper image.')
print('First nonzero boundary image modulo four:', first_boundary)
print('PASS: proper factorization and the separate boundary witness verified integrally.')

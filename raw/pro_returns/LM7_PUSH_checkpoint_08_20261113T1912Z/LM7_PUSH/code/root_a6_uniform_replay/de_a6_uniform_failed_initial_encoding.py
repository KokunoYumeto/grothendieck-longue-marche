#!/usr/bin/env python3
"""Literal E57 joint-source relation and full H-commutator images.

Every source power is tested in both full finite models. The ternary and
binary commutator matrices are freshly extracted from the accepted exact
solvable collector. The polynomial modular identity retains the actual
source convention and the first five-adic layer.
"""
from pathlib import Path
from hashlib import sha256
from math import lcm
import json, time
import numpy as np
import sympy as sp
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_solvable import SolvableF, word_interfaces
from de_ferrari_a6_metabelian import rank
from de_ferrari_two_core import rref2
from de_ferrari_a6_common import BITS
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_degree4_lift import InducedCombined
from e_symplectic_five_integral_residual_root import IntegralModel, enc

HERE = Path(__file__).resolve().parent
STEM = 'de_a6_uniform_comparison'


def permutation_order(p):
    seen = np.zeros(len(p), dtype=bool); result = 1
    for i in range(len(p)):
        if seen[i]:
            continue
        j = i; length = 0
        while not seen[j]:
            seen[j] = True; length += 1; j = int(p[j])
        assert j == i
        result = lcm(result, length)
    return result


def selected_columns(matrix, prime):
    selected = []; old = 0
    for j in range(matrix.shape[1]):
        trial = matrix[:, selected + [j]]
        new = rank(trial) if prime == 3 else len(rref2(trial)[1])
        if new > old:
            selected.append(j); old = new
    return selected


def rank_p(a, prime):
    a = np.array(a, dtype=np.int64) % prime; r = 0
    for col in range(a.shape[1]):
        pivot = next((i for i in range(r, len(a)) if a[i, col]), None)
        if pivot is None:
            continue
        a[[r, pivot]] = a[[pivot, r]]
        a[r] = a[r] * pow(int(a[r, col]), -1, prime) % prime
        for i in range(len(a)):
            if i != r:
                a[i] = (a[i] - a[i, col] * a[r]) % prime
        r += 1
    return r


def main():
    started = time.time()
    names = ['de_a6_schreier_full_ordered.npz', 'de_ferrari_a6_common.json',
             'de_ferrari_a6_common.npz', 'de_a6_module.json', 'de_a6_binary_module.json',
             'de_ferrari_sl2_5_model.py', 'de_ferrari_sl2_5_model.npz',
             'de_a6_gl_common_quotient.json', 'de_a6_gl_central_replay.json',
             'de_a6_gl_boundary.json', 'e_symplectic_five_integral_residual_root.json']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    d = load_data(); full = np.load(HERE / names[0])
    letters = {0: full['s'], 1: full['r'], -1: np.argsort(full['r'])}
    signed = FerrariSL2Five(); W = InducedCombined(signed, d)
    power_records = []; arrays = {}
    for name in ('x', 'y'):
        word = d[name + 'word']; p = np.arange(len(full['s']))
        for letter in word:
            p = letters[letter][p]
        assert permutation_order(p) == 120
        value = W.word(word)
        assert W.equal(W.power(value, 30), W.one)
        assert all(not W.equal(W.power(value, 30 // prime), W.one) for prime in (2, 3, 5))
        assert W.equal(W.power(value, 120), W.one)
        q = np.arange(len(p))
        for _ in range(120):
            q = p[q]
        assert np.array_equal(q, np.arange(len(p)))
        arrays[name + '_full_A6_value'] = p
        power_records.append({'source_generator': name, 'B_word': word,
                              'exact_full_A6_order': 120, 'exact_full_signed_order': 30,
                              'joint_exact_order': 120, 'common_power_relation': word * 120})

    F = SolvableF(); enodes, etargets, _, _ = word_interfaces()
    ebasis = [np.r_[0, 0, e] for e in F.E.original]
    hs = [F.power(F.x, 3), F.power(F.y, 3)]
    ternary = []; ternary_records = []
    for j, h in enumerate(hs):
        for i, e in enumerate(ebasis):
            c = F.comm(h, e)
            assert not np.any(c[:2])
            ternary.append(c[2:11])
            ternary_records.append({'H_source_word_B': d[('xword', 'yword')[j]] * 3,
                                    'E_basis_index': i, 'E_literal_word_node': int(etargets[i]),
                                    'full_solvable_value': c.tolist()})
    ternary = np.column_stack(ternary)
    assert rank(ternary) == 9
    mod = np.array(json.loads((HERE / 'de_a6_module.json').read_text())['conjugation_matrices'])
    X3 = mod[2] @ mod[2] @ mod[2] % 3
    Y3 = mod[3] @ mod[3] @ mod[3] % 3
    expected = np.c_[X3 - np.eye(9, dtype=np.int64), Y3 - np.eye(9, dtype=np.int64)] % 3
    assert np.array_equal(ternary, expected)

    raw = json.loads((HERE / 'de_ferrari_a6_common.json').read_text())
    words = raw['literal_gamma5_words_B']
    binary_basis = [F.word(d['fword'](w)) for w in words]
    assert all(not np.any(e[:-1]) for e in binary_basis)
    binary = []; binary_records = []
    for i, e in enumerate(ebasis):
        for j, w in enumerate(binary_basis):
            c = F.comm(e, w); assert not np.any(c[:-1])
            binary.append(BITS[int(c[-1])])
            binary_records.append({'H_Fprime_word_node': int(etargets[i]),
                                   'gamma5_binary_word_index': j,
                                   'binary_value': int(c[-1])})
    binary = np.column_stack(binary)
    assert len(rref2(binary)[1]) == 6
    selected3 = selected_columns(ternary, 3); selected2 = selected_columns(binary, 2)
    assert len(selected3) == 9 and len(selected2) == 6
    arrays.update(full_ternary_H_commutators=ternary,
                  full_binary_H_commutators=binary,
                  selected_ternary_columns=np.array(selected3),
                  selected_binary_columns=np.array(selected2))

    # The actual canonical signed modular matrix retains the specified pure
    # coordinates, and the integral eight-pair source has the same theta.
    model = IntegralModel(); S = sp.Matrix([[0, 1], [-1, 0]])
    R = sp.Matrix([[0, -1], [1, -1]]); P = sp.Matrix([[0, 1], [1, 0]])
    matrices = {0: S, 1: R, -1: R.inv()}
    pure_modular = []
    for name in ('x', 'y'):
        q = sp.eye(2)
        for letter in d[name + 'word']:
            q *= matrices[letter]
        if int(q[0, 0]) % 4 == 3:
            q = -q
        assert int(q[0, 0]) % 4 == int(q[1, 1]) % 4 == 1
        theta, _, _ = model.factor(d[name + 'word'] * 120)
        assert q**120 == P * theta * P
        pure_modular.append({'generator': name, 'canonical_signed_matrix': enc(q),
                             'actual_theta_of_power120': enc(theta)})
    assert pure_modular[0]['canonical_signed_matrix'] == [[1, 2], [0, 1]]
    assert pure_modular[1]['canonical_signed_matrix'] == [[1, 0], [-2, 1]]

    t = sp.Symbol('t'); lower = sp.Matrix([[1, 0], [t, 1]])
    upper = sp.Matrix([[1, 1], [0, 1]])
    polynomial = lower * upper * lower.inv() * upper.inv()
    assert polynomial == sp.Matrix([[1 - t, t], [-t*t, 1 + t + t*t]])
    comm = polynomial.subs(t, 240)
    mod25 = comm.applyfunc(lambda v: int(v) % 25)
    assert mod25 == sp.Matrix([[11, 15], [0, 16]])
    first = ((comm - sp.eye(2)) / 5).applyfunc(lambda v: int(v) % 5)
    assert first == sp.Matrix([[2, 3], [0, 3]])
    conjugators = [sp.eye(2), sp.Matrix([[1, 0], [2, 1]]), sp.Matrix([[1, -2], [0, 1]])]
    lie = [g * first * g.inv() for g in conjugators]
    vectors = [[int(v[0, 0]) % 5, int(v[0, 1]) % 5, int(v[1, 0]) % 5] for v in lie]
    assert rank_p(vectors, 5) == 3
    assert set(sp.factorint(240)) == {2, 3, 5}
    nonfactor = []
    for p in (7, 11, 13):
        matrix = sp.Matrix([[1, 240], [0, 1]]).applyfunc(lambda z: int(z) % p)
        assert matrix != sp.eye(2) and matrix != -sp.eye(2)
        nonfactor.append({'prime': p, 'source_identity_word': d['xword'] * 120,
                          'ordinary_projective_matrix_value': enc(matrix),
                          'not_central': True})
    result = {
        'status': 'PASS_LITERAL_UNIFORM_A6_COMPARISON',
        'scope': 'Exact source relations and quotient matrices; the closed-group image and full fibre arguments are proved separately in E57.',
        'complete_joint_power_relations': power_records,
        'full_ternary_H_commutator_rank': 9,
        'full_binary_H_commutator_rank': 6,
        'ternary_selected_literal_columns': [ternary_records[i] for i in selected3],
        'binary_selected_literal_columns': [binary_records[i] for i in selected2],
        'accepted_Fprime_word_DAG_size': len(enodes),
        'canonical_signed_modular_comparisons': pure_modular,
        'commutator_polynomial': [[str(v) for v in polynomial.row(i)] for i in range(2)],
        'parameter': 240, 'parameter_prime_divisors': [2, 3, 5],
        'actual_level25_matrix': enc(mod25), 'first_five_adic_Lie_vector': enc(first),
        'three_conjugate_Lie_vectors': vectors, 'five_adic_conjugate_rank': 3,
        'literal_projective_nonfactorization_controls': nonfactor,
        'input_sha256': hashes, 'all_protected_inputs_unchanged': True,
        'seconds': round(time.time() - started, 3),
    }
    arrays['five_adic_conjugate_vectors'] = np.array(vectors)
    np.savez_compressed(HERE / (STEM + '.npz'), **arrays)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k not in
                     ('input_sha256', 'complete_joint_power_relations',
                      'literal_projective_nonfactorization_controls')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

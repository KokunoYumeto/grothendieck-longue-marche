#!/usr/bin/env python3
"""Independent full-coordinate replay of binary C-preimage queries."""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from e_a6_double_model_root import FerrariA6Double
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_ferrari_two_core import rref2, solve2

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_commutator_replay_root'


def main():
    started = time.monotonic()
    names = ['e_a6_double_commutator_queries_root.json',
             'e_a6_double_commutator_prepare_root.npz',
             'e_a6_double_commutator_prepare_root.json',
             'e_a6_double_kernel_replay_root.npz',
             'e_a6_double_central_replay_root.npz',
             'de_a6_gl_central_prepare.npz',
             'e_a6_double_query_core_root.hpp', 'e_a6_double_central_root.cpp']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    central_source = (HERE / names[-1]).read_text()
    assert (HERE / names[-2]).read_text() == central_source[:central_source.index('int main(int argc')]
    raw = json.loads((HERE / names[0]).read_text())
    prep = np.load(HERE / names[1])
    labels = json.loads((HERE / names[2]).read_text())['query_labels']
    assert raw['status'] == 'PASS_EXACT_C_PREIMAGE_NORMAL_FORM_QUERIES'
    assert raw['query_count'] == len(labels) == len(raw['records']) == 21
    kernel, central, old = (np.load(HERE / names[i]) for i in (3, 4, 5))
    H = FerrariA6Double()
    d = load_data()
    W = InducedCombined(H, d)
    originals = [W.word(d['xword']), W.word(d['yword'])]
    queries, qcount = selected_group(prep['literal_F_word_DAG'], prep['query_word_nodes'], W, originals)
    qp = evaluate(prep['literal_F_word_DAG'], old['original_F_source_permutations'], prep['query_word_nodes'])
    targets = sorted({j for rec in raw['records'] for j in rec['normal_form_nodes']})
    c = [(W.id, v) for v in kernel['C_source_values']]
    values, ccount = selected_group(raw['normal_form_word_DAG'], targets, W, c)
    cp = evaluate(raw['normal_form_word_DAG'], old['C_original_source_permutations'], targets)
    exponents = []
    for op, a, b in raw['normal_form_word_DAG']:
        if op == 0:
            v = np.zeros(10, dtype=np.int64)
        elif op == 1:
            v = np.eye(10, dtype=np.int64)[a]
        elif op == 2:
            v = (exponents[a]+exponents[b]) % 2
        elif op == 3:
            v = -exponents[a] % 2
        elif op == 4:
            v = np.zeros(10, dtype=np.int64)
        elif op == 5:
            v = exponents[b]
        else:
            raise AssertionError(op)
        exponents.append(v)
    B = kernel['kernel_basis']
    piv = np.array(rref2(B.T)[1])
    inverse = np.column_stack([solve2(B[piv], np.eye(128, dtype=np.int64)[:, i])[0]
                               for i in range(128)])
    L = central['kernel_to_preimage_abelianization']
    hom = central['C_lift_abelianization_values']
    coords = []
    for i, (qn, rec) in enumerate(zip(prep['query_word_nodes'], raw['records'])):
        qn = int(qn)
        v, p, e = queries[qn], qp[qn], np.zeros(10, dtype=np.int64)
        assert np.array_equal(v[0], W.id)
        assert np.array_equal(v[1], prep['query_source_values'][i])
        assert np.array_equal(p, prep['query_A6_permutations'][i])
        for j in rec['normal_form_nodes']:
            v = W.mul(v, W.inv(values[j]))
            p = np.argsort(cp[j])[p]
            e = (e+exponents[j]) % 2
        assert np.array_equal(p, np.arange(9462)) and np.array_equal(v[0], W.id)
        actual = H.relative_kernel_vector(v[1]).ravel()
        expected = np.zeros(5724, dtype=np.int64)
        for at, x in rec['kernel_residue']:
            assert not expected[at] and x == 1
            expected[at] = x
        assert np.array_equal(actual, expected)
        k = inverse @ actual[piv] % 2
        assert np.array_equal(B @ k % 2, actual)
        assert np.array_equal(e, rec['C_generator_exponents'])
        value = (L @ k+hom @ e) % 2
        assert np.array_equal(value, rec['coordinate'])
        coords.append(value)
    coords = np.array(coords, dtype=np.int64).T
    pairing = np.zeros((3, 6, 6), dtype=np.int64)
    squares = np.zeros((3, 6), dtype=np.int64)
    for value, label in zip(coords.T, labels):
        if label[0] == 'module_square':
            squares[:, label[1]] = value
        else:
            _, i, j = label
            pairing[:, i, j] = value
            pairing[:, j, i] = value
    commutators = np.array([v for v, label in zip(coords.T, labels)
                           if label[0] == 'module_commutator']).T
    actions = central['B_quotient_actions']
    letters = {0: actions[0], 1: actions[1], -1: actions[1] @ actions[1] % 2}
    for word in (d['xword'], d['yword']):
        a = np.eye(3, dtype=np.int64)
        for letter in word:
            a = a @ letters[letter] % 2
        assert np.array_equal(a, np.eye(3, dtype=np.int64))
    rank = lambda a: len(rref2(a)[1])
    independent = rref2(commutators)[1]
    pair_labels = [label[1:] for label in labels if label[0] == 'module_commutator']
    out = {'status': 'PASS_INDEPENDENT_BINARY_C_PREIMAGE_QUERY_REPLAY',
           'query_count': 21, 'query_literal_F_ancestors_replayed': qcount,
           'C_normal_form_ancestors_replayed': ccount,
           'all_normal_forms_replayed_in_full_model_and_actual_base': True,
           'all_kernel_residues_and_abelian_coordinates_replayed': True,
           'pure_F_action_on_three_dimensional_quotient_is_identity': True,
           'square_image_rank': rank(squares),
           'commutator_image_rank': rank(commutators),
           'square_columns': squares.tolist(),
           'independent_commutator_pairs': [pair_labels[i] for i in independent],
           'independent_commutator_columns': commutators[:, independent].tolist(),
           'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)}
    np.savez_compressed(HERE / (STEM+'.npz'), query_coordinates=coords,
                        alternating_pairing=pairing, square_columns=squares,
                        commutator_columns=commutators)
    (HERE / (STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == v for n, v in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()

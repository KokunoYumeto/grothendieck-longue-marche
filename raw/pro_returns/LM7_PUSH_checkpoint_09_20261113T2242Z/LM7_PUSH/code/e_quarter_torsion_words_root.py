#!/usr/bin/env python3
"""Independent literal checks of all order-four witnesses and original inputs.

No conjugacy solver is imported.  Braid words are evaluated in the actual
binary and ternary targets, and all source parameters are reconstructed.
"""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product, groupby
from unittest.mock import patch
import io
import json
import runpy
import time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo
from de_ferrari_degree6_kernel import CombinedSix, InducedSix

HERE = Path(__file__).resolve().parent


def check_witnesses(H, data, word_key):
    delta = H.mul(H.mul(H.a, H.b), H.c)
    z4 = H.power(delta, 4)
    letters = {1: H.a, 2: H.b, 3: H.c}
    letters.update({-i: H.inv(g) for i, g in list(letters.items())})
    values, lengths = [], []
    for entry in data['literal_witnesses']:
        word = entry[word_key]
        value = H.one.copy()
        for letter, block in groupby(word):
            value = H.mul(value, H.power(letters[letter], sum(1 for _ in block)))
        assert np.array_equal(value, H.decode(entry['conjugator']))
        values.append(value)
        lengths.append(len(word))
    positives = 0
    targets = []
    for entry in data['distinct_targets']:
        y = H.decode(entry['delta_image'])
        targets.append(y)
        for translate in entry['translates']:
            if translate['conjugate']:
                j, wi = translate['central_exponent'], translate['witness_index']
                assert np.array_equal(H.conj(values[wi], delta), H.mul(y, H.power(z4, j)))
                positives += 1
    return delta, targets, values, {'literal_conjugators': len(values),
                                  'word_length_range': [min(lengths), max(lengths)],
                                  'positive_translates': positives,
                                  'distinct_targets': len(targets),
                                  'passing_translate_patterns': sorted({
                                      tuple(r['central_exponent'] for r in t['translates'] if r['conjugate'])
                                      for t in data['distinct_targets']})}


def main():
    started = time.time()
    with redirect_stdout(io.StringIO()), patch.object(Path, 'write_text', return_value=0):
        d = runpy.run_path(str(HERE/'de_distribution_test.py'))
    origins = json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    H2 = FerrariTwo(6)
    binary = json.loads((HERE/'e_quarter_torsion_binary.json').read_text())
    delta2, targets2, conjugators2, stats2 = check_witnesses(H2, binary, 'literal_B4_word')
    W2 = InducedTwo(H2, d, 4)
    X2 = W2.word(d['xword'])
    CM2 = np.load(HERE/'de_ferrari_two_degree6_module.npz')['F_prime_basis']
    rows2 = json.loads((HERE/'de_ferrari_two_lift.json').read_text())['records']
    original_index = 0
    for row, origin in zip(rows2, origins):
        chosen = row['chosen_witness']
        old_coeff = np.array(chosen['correction_coefficients'], dtype=np.int64)
        original = [H2.decode(g) for g in chosen['actual_binary_braid_images']]
        xg = W2.power(X2, origin['integral_cusp_gauge'])
        for branch in row['branches']:
            lam = branch['lambda_residue']
            part = np.array(branch['particular_correction'], dtype=np.int64)
            homogeneous = np.array(branch['homogeneous_correction_basis'], dtype=np.int64)
            for epsilon in range(2):
                rec = binary['records'][original_index]
                assert (rec['certificate_index'], rec['lambda_residue'], rec['binary_parameter']) == (
                    row['certificate_index'], lam, epsilon)
                coefficient = (part+epsilon*homogeneous[:, 0]-old_coeff)%2
                correction = W2.conj(xg, W2.element(CM2@coefficient%2))[1][W2.root]
                triple = [original[0], H2.conj(H2.inv(correction[4]), original[1]),
                          H2.conj(H2.inv(correction[5]), original[2])]
                H2.check_braids(triple)
                y = H2.mul(H2.mul(triple[0], triple[1]), triple[2])
                ti = rec['target_index']
                assert np.array_equal(y, targets2[ti])
                assert rec['passes_full_periodic_test']
                positive = next(t for t in binary['distinct_targets'][ti]['translates']
                                if t['central_exponent'] == rec['required_exponent_for_full_conjugacy'])
                assert positive['conjugate']
                g = conjugators2[positive['witness_index']]
                assert np.array_equal(H2.conj(g, H2.power(delta2, lam)), y)
                original_index += 1
    assert original_index == 96
    stats2['all_original_inputs_reconstructed'] = original_index
    stats2['all_actual_multiplier_conjugacies_checked'] = True

    H3 = CombinedSix()
    ternary = json.loads((HERE/'e_quarter_torsion_ternary.json').read_text())
    delta3, targets3, conjugators3, stats3 = check_witnesses(H3, ternary, 'literal_B4_conjugator')
    W3 = InducedSix(H3, d)
    X3 = W3.word(d['xword'])
    CM3 = np.load(HERE/'de_ferrari_degree6_lift_certificate.npz')['top_kernel_basis']
    rows3 = json.loads((HERE/'de_ferrari_degree6_lift.json').read_text())['records']
    checked = 0
    for row, origin, record in zip(rows3, origins, ternary['records']):
        chosen = row['chosen_witness']
        original = [H3.decode(g) for g in chosen['actual_braid_images']]
        K = np.array(chosen['homogeneous_top_correction'], dtype=np.int64)
        xg = W3.power(X3, origin['integral_cusp_gauge'])
        for pair, rec in zip(product(range(3), repeat=2), record['plane']):
            assert rec['ternary_parameters'] == list(pair)
            correction = W3.conj(xg, W3.element(CM3@(K@np.array(pair, dtype=np.int64)%3)%3))[1][W3.root]
            a, b, c = original[0], H3.conj(H3.inv(correction[4]), original[1]), H3.conj(H3.inv(correction[5]), original[2])
            H3.check_braids((a, b, c))
            y = H3.mul(H3.mul(a, b), c)
            ti = rec['target_index']
            assert np.array_equal(y, targets3[ti]) and rec['passes_full_periodic_test']
            positive = next(t for t in ternary['distinct_targets'][ti]['translates'] if t['central_exponent'] == 0)
            assert positive['conjugate']
            g = conjugators3[positive['witness_index']]
            for lam in (1, 73):
                assert np.array_equal(H3.conj(g, H3.power(delta3, lam)), y)
            checked += 1
    assert checked == 216
    stats3['all_original_inputs_reconstructed'] = checked
    stats3['both_actual_multiplier_conjugacies_checked'] = True
    out = {'binary': stats2, 'ternary': stats3,
           'all864_joint_points_covered_by_the_actual_product_comparison': True,
           'imports_no_conjugacy_solver': True, 'seconds': round(time.time()-started, 3)}
    (HERE/'e_quarter_torsion_words_root.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2), flush=True)
    print('PASS_ALL_PERIODIC_FERRARI_LITERAL_WORDS', flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Literal A5 Wajnryb evaluations before solving the whole correction fibre.

This records representative equations and complete N-generator images.
Failed representatives are not exclusions of their fixed-G6 fibres.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_a6_source_data import load_data
from de_wajnryb_free_model import build
from de_wajnryb_s4_fibres import bword, fword, reconstruct, multiply, power
from de_wajnryb_s3_model import perm_word

HERE = Path(__file__).resolve().parent


def main():
    started = time.monotonic()
    stem = 'de_wajnryb_a5_g2'
    names = [stem+'.npz', stem+'_source.npz', stem+'_source.json',
             'de_ferrari_fibres.json', 'de_ferrari_two_lift.json',
             'de_ferrari_degree6_kernel.json', 'de_ferrari_two_degree6_module.json',
             'de_ferrari_a6_source_data.py', 'de_ferrari_sl2_5_N.json',
             'de_wajnryb_free_model.py', 'de_wajnryb_s4_fibres.py',
             'de_wajnryb_s3_model.py']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    target = np.load(HERE/names[0])
    source = np.load(HERE/names[1])
    metadata = json.loads((HERE/names[2]).read_text())
    d = load_data()
    s, r = source['s'], source['r']
    sx, sy = bword(d['xword'], s, r), bword(d['yword'], s, r)
    identity_source = np.arange(len(s))
    N = np.array([bword(w, s, r) for w in d['Nwords']])
    assert len(N) == 97
    with (HERE/(stem+'_N.input')).open('w') as out:
        out.write(f'{len(s)} {len(N)}\n')
        for p in N:
            out.write(' '.join(map(str, p))+'\n')
    old = target['sigma']
    degree = old.shape[1]
    root = sorted(d['Q2']).index(d['unit'])
    offset = root*3*degree
    for p, expected in [(sx, target['x']), (sy, target['y'])]:
        raw = reconstruct(p, metadata)
        pairs = np.array([raw[offset+i*degree:offset+(i+1)*degree]-(offset+i*degree)
                          for i in range(3)])
        assert np.array_equal(pairs, expected)
    origins = json.loads((HERE/names[3]).read_text())['records']
    lifts = json.loads((HERE/names[4]).read_text())['records']
    bases = [json.loads((HERE/name).read_text())['F_prime_basis_words'] for name in names[5:7]]
    correction_words = [row['chosen_witness']['literal_B_old_correction_word'] for row in lifts]
    correction_words += bases[0]+bases[1]
    corrections = np.array([bword(w, s, r) for w in correction_words])
    model = build(2)
    assert all(np.array_equal(perm_word(rel['left_word'], old), perm_word(rel['right_word'], old))
               for rel in model['relations'])
    assert all(np.array_equal(power(g, 30), np.arange(degree)) for g in old)
    rows, f_values, corrected = [], [], []
    for index, origin in enumerate(origins):
        word = origin['actual_commutator_word_f']
        assert all(sum(1 if t == j else -1 if t == -j else 0 for t in word) == 0 for j in (1, 2))
        p = fword(word, sx, sy)
        raw = reconstruct(p, metadata)
        f = np.array([raw[offset+i*degree:offset+(i+1)*degree]-(offset+i*degree)
                      for i in range(3)])
        new = np.array([old[0]]+[multiply(multiply(np.argsort(f[i-1]), old[i]), f[i-1])
                               for i in range(1, 4)]+[old[4]])
        failures = [rel['name'] for rel in model['relations']
                    if not np.array_equal(perm_word(rel['left_word'], new),
                                          perm_word(rel['right_word'], new))]
        rows.append({'certificate_index': index, 'missing_coset': origin['missing_coset'],
                     'literal_F_word_length': len(word), 'failed_relations_at_multiplier_one': failures,
                     'all_relations_pass_for_this_representative': not failures})
        f_values.append(f)
        corrected.append(new)
        print(json.dumps(rows[-1]), flush=True)
    report = {'status': 'PASS_LITERAL_A5_WAJNRYB_PROBE',
              'source_degree': len(s), 'target_degree': degree,
              'N_basis_count': 97, 'N_basis_orders': [int(Permutation(p.tolist()).order()) for p in N],
              'N_sixth_power_identity_count': sum(np.array_equal(power(p, 6), identity_source) for p in N),
              'old_correction_words_count': len(correction_words),
              'old_correction_identity_indices': [i for i, p in enumerate(corrections) if np.array_equal(p, identity_source)],
              'old_correction_orders': [int(Permutation(p.tolist()).order()) for p in corrections],
              'identity_control_passes': True, 'finite_generator_period_divides': 30,
              'records': rows,
              'scope': 'Literal representative and correction images only. The complete fixed-G6 fibre is not yet solved; no representative failure is an exclusion.',
              'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 6)}
    np.savez_compressed(HERE/(stem+'_probe.npz'), N_basis_images=N,
                        old_correction_images=corrections, actual_f_values=np.array(f_values),
                        corrected_generators=np.array(corrected))
    (HERE/(stem+'_probe.json')).write_text(json.dumps(report, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in report.items() if k not in {'records', 'input_sha256'}}, indent=2), flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Actual six-coset induced source for the nonlinear Wajnryb evaluations."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from e_hurwitz_five_source_root import Evaluations, Source
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernel_source import compress

HERE = Path(__file__).resolve().parent


class WajnrybEvaluations(Evaluations):
    def __init__(self, genus):
        data = np.load(HERE/('de_wajnryb_s4_g'+str(genus)+'.npz'))
        self.sigma, self.x, self.y = data['sigma'], data['x'], data['y']
        self.degree, self.count = self.sigma.shape[1], len(self.x)
        self.one = np.arange(self.degree, dtype=np.int64)


def main(g):
    start = time.time()
    tag = 'de_wajnryb_s4_g'+str(g)+'_source'
    names = ['de_wajnryb_s4_g'+str(g)+'.npz', 'e_hurwitz_five_source_root.py',
             'de_ferrari_a6_source_data.py', 'de_ferrari_a6_kernel_source.py',
             'de_ferrari_sl2_5_N.json', 'de_ferrari_mod9_lift.py']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    H, data = WajnrybEvaluations(g), load_data()
    W = Source(H, data)
    s, r = [W.permutation(W.letters[t]) for t in (0, 1)]
    assert np.array_equal(s[s], np.arange(len(s)))
    assert np.array_equal(r[r[r]], np.arange(len(r)))
    for a in W.letters.values():
        for b in W.letters.values():
            assert np.array_equal(W.permutation(W.mul(a, b)),
                                  W.permutation(b)[W.permutation(a)])
    np.savez_compressed(HERE/(tag+'_raw.npz'), s=s, r=r)
    new, metadata = compress(s, r)
    np.savez_compressed(HERE/(tag+'.npz'), s=new[0], r=new[1])
    with (HERE/(tag+'.input')).open('w') as out:
        out.write(f'{len(new[0])} 2\n')
        for p in new:
            out.write(' '.join(map(str, p))+'\n')
    report = {**metadata, 'status': 'PASS_COMPLETE_LITERAL_WAJNRYB_S3_SOURCE',
              'genus': g, 'evaluation_count': H.count, 'coset_count': 6,
              'source_C2_C3_and_all_generator_products_verified': True,
              'input_sha256': hashes, 'seconds': round(time.time()-start, 6)}
    (HERE/(tag+'.json')).write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k not in
                     ('retained_original_canonical_orders', 'orbit_correspondences')}, indent=2), flush=True)
    # The full N image is retained, before drawing any factorization conclusion.
    N = [W.word(w) for w in data['Nwords']]
    order6 = [W.equal(W.power(a, 6), W.one) for a in N]
    noncommuting = []
    for i in range(len(N)):
        for j in range(i):
            if not W.equal(W.mul(N[i], N[j]), W.mul(N[j], N[i])):
                noncommuting.append([i, j])
                break
        if len(noncommuting) >= 4:
            break
    probe = {'all_97_N_sixth_powers_trivial': all(order6),
             'N_sixth_power_nonidentity_indices': [i for i, ok in enumerate(order6) if not ok],
             'first_literal_noncommuting_N_pairs': noncommuting,
             'noncommutation_search_complete': not noncommuting,
             'source_factor_through_G6_proved_by_these_checks': all(order6) and not noncommuting}
    report.update(probe)
    report['seconds'] = round(time.time()-start, 6)
    (HERE/(tag+'.json')).write_text(json.dumps(report, indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(probe, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--genus', type=int, choices=(2,), default=2)
    main(parser.parse_args().genus)

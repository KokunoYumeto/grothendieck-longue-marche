#!/usr/bin/env python3
"""Complete six-coset B source for the eight symplectic evaluations."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import time
import numpy as np
from sympy import factorint
from sympy.combinatorics import Permutation, PermutationGroup
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernel_source import compress
from e_hurwitz_five_source_root import Evaluations, Source

HERE = Path(__file__).resolve().parent


class SymplecticEvaluations(Evaluations):
    def __init__(self, prime):
        a = np.load(HERE / ('e_symplectic_five_p' + str(prime) + '_model_root.npz'))
        self.sigma, self.x, self.y = a['sigma'], a['x'], a['y']
        self.degree, self.count = self.sigma.shape[1], len(self.x)
        self.one = np.arange(self.degree, dtype=np.int64)


def main(prime):
    start = time.time()
    tag = 'e_symplectic_five_p' + str(prime)
    names = [tag + '_model_root.npz', 'e_hurwitz_five_source_root.py',
             'de_ferrari_a6_source_data.py', 'de_ferrari_a6_kernel_source.py',
             'de_ferrari_mod9_lift.py']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    H, d = SymplecticEvaluations(prime), load_data()
    W = Source(H, d)
    s, r = W.permutation(W.letters[0]), W.permutation(W.letters[1])
    one = np.arange(len(s))
    assert np.array_equal(s[s], one)
    assert np.array_equal(r[r[r]], one)
    for a in W.letters.values():
        for b in W.letters.values():
            assert np.array_equal(W.permutation(W.mul(a, b)),
                                  W.permutation(b)[W.permutation(a)])
    new, metadata = compress(s, r)
    np.savez_compressed(HERE / (tag + '_source_root_generators.npz'), s=s, r=r)
    np.savez_compressed(HERE / (tag + '_source_root_compressed.npz'), s=new[0], r=new[1])
    print('Faithfully compressed source degree', len(new[0]), flush=True)
    G = PermutationGroup([Permutation(p.tolist()) for p in new])
    order = int(G.order())
    out = {**metadata, 'prime': prime, 'evaluation_count': H.count, 'coset_count': 6,
           'source_C2_C3_relations_verified': True, 'source_multiplication_verified': True,
           'all_evaluation_and_coset_coordinates_retained': True,
           'source_image_order': order, 'factorization': factorint(order),
           'input_sha256': hashes, 'seconds': round(time.time() - start, 3)}
    (HERE / (tag + '_source_root.json')).write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in
                     ('retained_original_canonical_orders', 'orbit_correspondences',
                      'input_sha256')}, indent=2), flush=True)
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print('PASS_COMPLETE_SYMPLECTIC_FIVE_STRAND_SOURCE', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime', type=int, default=3)
    main(parser.parse_args().prime)

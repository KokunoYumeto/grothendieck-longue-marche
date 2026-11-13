#!/usr/bin/env python3
"""Prime-seven literal five-strand model; adapted from the audited root model.

The alternating form and every permutation are reconstructed from integer
matrices. No action of a shadow on a fixed kernel is assumed. This supplies
actual finite B5 maps for the full-source tests of E39 and the NS formulas.
"""
from itertools import product
from pathlib import Path
import argparse
import json
import time
import numpy as np
from sympy import factorint
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent


def build(p):
    start = time.time()
    assert p == 7
    J = np.zeros((4, 4), dtype=np.int64)
    for i in range(3):
        J[i, i+1], J[i+1, i] = 1, -1
    matrices = []
    for i in range(4):
        a = np.eye(4, dtype=np.int64)
        a[i, :] += J[i, :]
        a %= p
        assert np.array_equal(a.T @ J @ a % p, J % p)
        matrices.append(a)
    points = [v for v in product(range(p), repeat=4) if any(v)]
    index = {v: i for i, v in enumerate(points)}
    vectors = np.array(points, dtype=np.int64)
    arrays = []
    for a in matrices:
        image = vectors @ a.T % p
        row = [index[tuple(v)] for v in image]
        assert sorted(row) == list(range(len(points)))
        arrays.append(row)
    sig = [Permutation(row) for row in arrays]
    one = Permutation(list(range(len(points))))
    assert all(g.order() == p for g in sig)
    for i in range(3):
        assert sig[i] * sig[i+1] * sig[i] == sig[i+1] * sig[i] * sig[i+1]
    for i in range(4):
        for j in range(i+2, 4):
            assert sig[i] * sig[j] == sig[j] * sig[i]
    G = PermutationGroup(sig)
    order = int(G.order())
    expected = p**4 * (p**2 - 1) * (p**4 - 1)
    assert order == expected
    delta = sig[0] * sig[1] * sig[2] * sig[3]
    minus = Permutation([index[tuple((-np.array(v)) % p)] for v in points])
    assert delta**5 == minus
    assert delta.order() == 10
    epsilon = sig[0] * delta
    assert epsilon**4 == minus and epsilon.order() == 8
    pure = {}
    for i in range(1, 5):
        for j in range(i+1, 6):
            h = one
            for k in range(j-1, i, -1):
                h = h * sig[k-1]
            pure[(i, j)] = h * sig[i-1]**2 * ~h
    A12, A13, A23, A24, A34 = [pure[t] for t in
                               ((1, 2), (1, 3), (2, 3), (2, 4), (3, 4))]
    pairs = [(A12, A23*A24), (A13*A23, A34), (A23, A34),
             (A12*A13, A24*A34), (A12, A23)]
    for i in range(2, 5):
        y = one
        for j in range(i-1, 0, -1):
            y = y * sig[j-1]
        for j in range(1, i):
            y = y * sig[j-1]
        pairs.append((y, sig[i-1]**2))
    first_four = PermutationGroup(sig[:3])
    pair_orders = [int(PermutationGroup([a, b]).order()) for a, b in pairs]
    out = {
        'status': 'PASS_LITERAL_SYMPLECTIC_FIVE_STRAND_MODEL',
        'prime': p,
        'alternating_form': J.tolist(),
        'transvection_matrices': [a.tolist() for a in matrices],
        'permutation_degree': len(points),
        'all_Artin_relations_verified': True,
        'all_four_transvections_have_order': p,
        'full_image_order': order,
        'full_image_factorization': factorint(order),
        'symplectic_group_order_formula': expected,
        'first_four_strand_image_order': int(first_four.order()),
        'rotation_order': int(delta.order()),
        'second_periodic_order': int(epsilon.order()),
        'both_periodic_powers_equal_minus_identity': True,
        'evaluation_pair_count': len(pairs),
        'evaluation_pair_image_orders': pair_orders,
        'seconds': round(time.time() - start, 3),
    }
    stem = 'bc_symplectic_five_p7_model'
    (HERE / (stem + '.json')).write_text(json.dumps(out, indent=2) + '\n')
    np.savez_compressed(HERE / (stem + '.npz'),
                        sigma=np.array(arrays, dtype=np.int64),
                        matrices=np.array(matrices, dtype=np.int64),
                        J=J, points=vectors,
                        x=np.array([a.array_form for a, b in pairs], dtype=np.int64),
                        y=np.array([b.array_form for a, b in pairs], dtype=np.int64),
                        delta=np.array(delta.array_form, dtype=np.int64),
                        epsilon=np.array(epsilon.array_form, dtype=np.int64),
                        minus=np.array(minus.array_form, dtype=np.int64))
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime', type=int, default=7)
    build(parser.parse_args().prime)

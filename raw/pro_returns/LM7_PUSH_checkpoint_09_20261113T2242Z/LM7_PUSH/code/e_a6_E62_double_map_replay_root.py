#!/usr/bin/env python3
"""Full-model replay of the E62-to-double-cover quotient and its I kernel."""
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
from de_a6_schreier_certificate import read_certificate
from de_ferrari_two_core import rref2, solve2
from e_a6_E62_deep_collect_root import BinaryAmbient

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_E62_double_map_replay_root'


class BinaryDoubleQuotient:
    def __init__(self, squares, brackets):
        self.beta = np.zeros((64, 64), dtype=np.int64)
        for u in range(64):
            for v in range(64):
                out = 0
                for j in range(6):
                    if not (u >> j & 1):
                        continue
                    if v >> j & 1:
                        out ^= int(squares[j])
                    for i in range(j):
                        if v >> i & 1:
                            out ^= int(brackets[j, i])
                self.beta[u, v] = out

    def mul(self, a, b):
        return (a ^ b) ^ (int(self.beta[a & 63, b & 63]) << 6)

    def inv(self, a):
        return a ^ (int(self.beta[a & 63, a & 63]) << 6)

    def comm(self, a, b):
        return self.mul(self.mul(self.mul(a, b), self.inv(a)), self.inv(b))


def main():
    started = time.monotonic()
    names = ['e_a6_E62_double_map_queries_root.json',
             'e_a6_E62_double_map_prepare_root.npz',
             'e_a6_E62_double_map_prepare_root.json',
             'e_a6_double_kernel_replay_root.npz',
             'e_a6_double_central_replay_root.npz',
             'de_a6_gl_central_prepare.npz',
             'de_a6_schreier_full_ordered.bin',
             'e_a6_double_commutator_replay_root.npz',
             'e_a6_E62_deep_prepare_root.npz',
             'e_a6_E62_deep_collect_root.json',
             'e_a6_double_query_core_root.hpp', 'e_a6_double_central_root.cpp',
             'e_a6_double_query_root.cpp']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    raw = json.loads((HERE / names[0]).read_text())
    prep = np.load(HERE / names[1])
    assert raw['status'] == 'PASS_EXACT_C_PREIMAGE_NORMAL_FORM_QUERIES'
    assert raw['query_count'] == len(raw['records']) == 39
    central_source = (HERE / names[-2]).read_text()
    assert (HERE / names[-3]).read_text() == central_source[:central_source.index('int main(int argc')]
    kernel, central, old = (np.load(HERE / names[i]) for i in (3, 4, 5))
    H = FerrariA6Double()
    d = load_data()
    W = InducedCombined(H, d)
    queries, qcount = selected_group(prep['literal_B_word_DAG'], prep['query_word_nodes'],
                                     W, [W.letters[0], W.letters[1]])
    full = read_certificate(HERE / names[6])
    qp = evaluate(prep['literal_B_word_DAG'], full['original'], prep['query_word_nodes'])
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
            v = (exponents[a] + exponents[b]) % 2
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
            e = (e + exponents[j]) % 2
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
        value = (L @ k + hom @ e) % 2
        assert np.array_equal(value, rec['coordinate'])
        coords.append(value)
    coords = np.array(coords, dtype=np.int64)
    retained = np.load(HERE / names[7])
    squares = (1 << np.arange(3)) @ retained['square_columns']
    brackets = np.einsum('a,aij->ij', 1 << np.arange(3), retained['alternating_pairing'])
    Q = BinaryDoubleQuotient(squares, brackets)
    A = BinaryAmbient(np.load(HERE / names[8]))
    actual_images = prep['source_old_W_coordinates'].astype(np.int64) | ((coords @ (1 << np.arange(3))) << 6)
    generator_images = list(map(int, actual_images[:24]))

    def image(c):
        out = 0
        for i, g in enumerate(generator_images):
            if c >> i & 1:
                out = Q.mul(out, g)
        return out

    # These are all defining PC squares and commutators, with the exact
    # ordered carries. They establish a homomorphism on the entire C62.
    for i in range(24):
        for j in range(24):
            assert image(A.mul(1 << i, 1 << j)) == Q.mul(generator_images[i], generator_images[j])
            assert image(A.comm(1 << i, 1 << j)) == Q.comm(generator_images[i], generator_images[j])
    assert all(image(A.mul(1 << i, 1 << i)) == Q.mul(g, g)
               for i, g in enumerate(generator_images))
    assert all(image(int(c)) == int(v) for c, v in zip(prep['source_E62_coordinates'], actual_images))
    # Explicit identity, inverse and every cocycle identity in the
    # six-dimensional quotient validate the 512-element collected group.
    assert all(Q.mul(a, Q.inv(a)) == Q.mul(Q.inv(a), a) == 0 for a in range(512))
    for u in range(64):
        for v in range(64):
            for w in range(64):
                assert Q.beta[u, v] ^ Q.beta[u ^ v, w] == Q.beta[v, w] ^ Q.beta[u, v ^ w]
    raw_deep = json.loads((HERE / names[9]).read_text())
    rgens = [int(v) & ((1 << 24)-1) for v in raw_deep['binary_stages'][-1]['basis_values']]
    reached = [0]
    for g in rgens:
        values = [A.mul(a, g) for a in reached]
        assert not set(reached).intersection(values)
        reached += values
    assert len(reached) == len(set(reached)) == 32768
    images = [image(c) for c in reached]
    assert set(images) == set(range(512))
    counts = np.bincount(images, minlength=512)
    assert np.all(counts == 64)
    ker = sorted(c for c, q in zip(reached, images) if q == 0)
    index = {c: i for i, c in enumerate(ker)}
    assert len(index) == 64
    table = np.array([[index[A.mul(a, b)] for b in ker] for a in ker], dtype=np.uint8)
    assert np.array_equal(table[0], np.arange(64)) and np.array_equal(table[:, 0], np.arange(64))
    commutators = {A.comm(a, b) for a in ker for b in ker}
    derived = {0}
    for c in sorted(commutators):
        derived |= {A.mul(d, c) for d in list(derived)}
    orders = []
    for c in ker:
        value = 0
        for n in range(1, 5):
            value = A.mul(value, c)
            if value == 0:
                orders.append(n)
                break
        else:
            raise AssertionError('kernel exponent')
    result = {'status': 'PASS_EXACT_E62_TO_BINARY_DOUBLE_QUOTIENT_AND_64_KERNEL',
              'full_model_C_preimage_queries_replayed': 39,
              'query_B_word_ancestors_replayed': qcount,
              'C_normal_form_ancestors_replayed': ccount,
              'all_full_model_normal_forms_residues_and_coordinates_checked': True,
              'actual_E62_PC_generator_images_in_nine_bits': generator_images,
              'all_576_PC_products_and_commutators_checked': True,
              'all_262144_binary_cocycle_identities_checked': True,
              'entire_binary_double_quotient_order': 512,
              'actual_residual_order': len(reached),
              'actual_residual_quotient_surjective': True,
              'every_residual_quotient_fibre_size': 64,
              'exact_kernel_coordinates': ker,
              'kernel_derived_order': len(derived),
              'kernel_element_order_counts': {str(n): orders.count(n) for n in sorted(set(orders))},
              'scope': 'Actual N-prime quotient through E73; individual finite-depth source words are not asserted to belong to I.',
              'input_sha256': hashes, 'seconds': round(time.monotonic()-started, 6)}
    np.savez_compressed(HERE / (STEM + '.npz'),
        C_preimage_query_coordinates=coords,
        E62_PC_generator_images=np.array(generator_images, dtype=np.int64),
        binary_double_cocycle=Q.beta,
        residual_E62_coordinates=np.array(reached, dtype=np.int64),
        residual_double_coordinates=np.array(images, dtype=np.int64),
        exact_kernel_coordinates=np.array(ker, dtype=np.int64),
        exact_kernel_multiplication_table=table)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2)+'\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps({k: v for k, v in result.items() if k not in
        ['input_sha256', 'exact_kernel_coordinates']}, indent=2), flush=True)


if __name__ == '__main__':
    main()

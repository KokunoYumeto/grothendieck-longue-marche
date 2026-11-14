#!/usr/bin/env python3
"""Universal Ferrari model for the literal central double cover of A6.

The actual free quotient is U^53 times C2^2, for the enumerated perfect
720-element U. Four central lifts over each A6 epikernel are retained.
The maps to the retained A6 model and the binary affine model are exact.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np
from de_ferrari_a6_model import FerrariA6
from de_ferrari_two_model import FerrariTwo

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_model_root'


class FerrariA6Double(FerrariTwo):
    def __init__(self):
        raw = np.load(HERE / 'e_a6_double_cover_root.npz')
        old = np.load(HERE / 'de_ferrari_a6_kernels.npz')
        self.old = FerrariA6()
        self.n = 53
        self.um = raw['cover_multiplication']
        self.ui = raw['cover_inverse']
        self.uid = int(raw['cover_one'])
        self.z = int(raw['cover_central_generator'])
        self.zpowers = np.array([self.uid, self.z], dtype=np.int64)
        self.zlog = np.full(720, -1, dtype=np.int64)
        self.zlog[self.zpowers] = np.arange(2)
        self.quotient = raw['A6_quotient']
        self.section = raw['A6_section']
        self.auto = raw['all_lifted_automorphisms']
        self.character = raw['automorphism_central_character'].astype(np.int64)
        assert np.all(self.character == 1)
        self.am = old['Aut_multiplication']
        self.ai = old['Aut_inverse']
        self.autone = int(old['Aut_one'])
        self.lifts = self.section[old['kernel_representatives']]
        n = self.n
        self.ps, self.cs = slice(0, n), slice(n, 2*n)
        self.es, self.ms = slice(2*n, 4*n), slice(4*n, 4*n+4)
        self.ks, self.ts = slice(4*n+4, 5*n+4), slice(5*n+4, 5*n+6)
        self.width = 5*n+6
        self.one = np.r_[np.arange(n), np.full(n, self.autone),
                         np.zeros(2*n, dtype=np.int64), [1, 0, 0, 1],
                         np.full(n, self.uid), [0, 0]].astype(np.int64)
        assert self.one.shape == (271,)

        def nielsen(p, alpha, desired, matrix):
            value = self.one.copy()
            value[self.ps], value[self.cs] = p, alpha
            value[self.ms] = np.asarray(matrix).ravel()
            reference = self.auto[alpha[:, None], self.lifts[p]]
            cross = self.zlog[self.um[desired, self.ui[reference]]]
            assert np.all(cross >= 0)
            value[self.es] = cross.ravel()
            return value

        g, h = self.lifts.T
        self.a = nielsen(old['a_permutation'], old['a_automorphisms'],
                         np.column_stack((g, self.um[h, g])), [[1, 1], [0, 1]])
        self.b = nielsen(old['b_permutation'], old['b_automorphisms'],
                         np.column_stack((self.um[g, self.ui[h]], h)), [[1, 0], [1, 1]])
        self.xi1 = self.one.copy()
        self.xi1[self.ks], self.xi1[self.ts] = g, [1, 0]
        self.xi2 = self.one.copy()
        self.xi2[self.ks], self.xi2[self.ts] = h, [0, 1]
        self.c = self.mul(self.xi1, self.a)
        self.check_braids((self.a, self.b, self.c))
        sig = {1: self.a, 2: self.b, 3: self.c}

        def pure(i, j):
            value = self.one.copy()
            for k in range(j-1, i, -1):
                value = self.mul(value, sig[k])
            return self.conj(value, self.power(sig[i], 2))

        A12, A13, A23, A24, A34 = (pure(i, j) for i, j in
                                    ((1, 2), (1, 3), (2, 3), (2, 4), (3, 4)))
        omega = self.power(self.mul(self.a, self.b), 3)
        self.pairs = ((A12, self.mul(A23, A24)), (self.mul(A13, A23), A34),
                      (A23, A34), (self.mul(A12, A13), self.mul(A24, A34)),
                      (A12, A23), (omega, A34))
        self.x = np.array([x for x, y in self.pairs])
        self.y = np.array([y for x, y in self.pairs])
        assert np.array_equal(self.mul(self.c, self.inv(self.a)), self.xi1)
        xi2 = self.mul(self.mul(self.mul(self.mul(self.mul(
            self.a, self.b), self.a), self.inv(self.c)), self.inv(self.b)), self.inv(self.a))
        assert np.array_equal(xi2, self.xi2)
        assert np.array_equal(self.conj(self.a, self.xi1), self.xi1)
        assert np.array_equal(self.conj(self.a, self.xi2), self.mul(self.xi2, self.xi1))
        assert np.array_equal(self.conj(self.b, self.xi1), self.mul(self.xi1, self.inv(self.xi2)))
        assert np.array_equal(self.conj(self.b, self.xi2), self.xi2)

    def mul(self, x, y):
        x, y = np.broadcast_arrays(x, y)
        n = self.n
        p, q = x[..., self.ps], y[..., self.ps]
        alpha, beta = x[..., self.cs], y[..., self.cs]
        E = x[..., self.es].reshape(x.shape[:-1] + (n, 2))
        D = y[..., self.es].reshape(y.shape[:-1] + (n, 2))
        M = x[..., self.ms].reshape(x.shape[:-1] + (2, 2))
        N = y[..., self.ms].reshape(y.shape[:-1] + (2, 2))
        pp = np.take_along_axis(q, p, axis=-1)
        cc = self.am[alpha, np.take_along_axis(beta, p, axis=-1)]
        EE = (np.einsum('...ji,...ik->...jk', E, N)
              + np.take_along_axis(D, p[..., None], axis=-2)) % 2
        MM = np.einsum('...ij,...jk->...ik', M, N) % 2
        acted = self.auto[alpha, np.take_along_axis(y[..., self.ks], p, axis=-1)]
        shift = np.einsum('...ji,...i->...j', E, y[..., self.ts]) % 2
        kk = self.um[x[..., self.ks], self.um[self.zpowers[shift], acted]]
        tt = (x[..., self.ts] + np.einsum('...ij,...j->...i', M, y[..., self.ts])) % 2
        return np.concatenate((pp, cc, EE.reshape(x.shape[:-1] + (2*n,)),
                               MM.reshape(x.shape[:-1] + (4,)), kk, tt), axis=-1)

    def inv(self, x):
        n = self.n
        q = np.argsort(x[..., self.ps], axis=-1)
        beta = self.ai[np.take_along_axis(x[..., self.cs], q, axis=-1)]
        M = x[..., self.ms].reshape(x.shape[:-1] + (2, 2))
        det = (M[..., 0, 0]*M[..., 1, 1] - M[..., 0, 1]*M[..., 1, 0]) % 2
        assert np.all(det == 1)
        Mi = np.stack((M[..., 1, 1], -M[..., 0, 1], -M[..., 1, 0], M[..., 0, 0]),
                      axis=-1).reshape(M.shape) % 2
        E = np.take_along_axis(x[..., self.es].reshape(x.shape[:-1] + (n, 2)),
                              q[..., None], axis=-2)
        EE = -np.einsum('...ji,...ik->...jk', E, Mi) % 2
        t = x[..., self.ts]
        kk = self.auto[beta, self.ui[np.take_along_axis(x[..., self.ks], q, axis=-1)]]
        shift = -np.einsum('...ji,...i->...j', EE, t) % 2
        kk = self.um[self.zpowers[shift], kk]
        tt = -np.einsum('...ij,...j->...i', Mi, t) % 2
        return np.concatenate((q, beta, EE.reshape(x.shape[:-1] + (2*n,)),
                               Mi.reshape(x.shape[:-1] + (4,)), kk, tt), axis=-1)

    def project_a6(self, x):
        alpha = x[..., self.cs]
        left = self.am[self.old.inner[self.quotient[x[..., self.ks]]], alpha]
        return np.concatenate((x[..., self.ps], left, alpha), axis=-1)

    def project_affine2(self, x):
        return np.concatenate((x[..., self.ms], x[..., self.ts]), axis=-1)

    def relative_kernel_vector(self, x):
        assert np.array_equal(self.project_a6(x), np.broadcast_to(
            self.old.one, x.shape[:-1] + (3*self.n,)))
        assert np.array_equal(self.project_affine2(x), np.broadcast_to(
            [1, 0, 0, 1, 0, 0], x.shape[:-1] + (6,)))
        central = self.zlog[x[..., self.ks]]
        assert np.all(central >= 0)
        return np.concatenate((central, x[..., self.es]), axis=-1)

    def relative_kernel_element(self, v):
        value = np.broadcast_to(self.one, v.shape[:-1] + (self.width,)).copy()
        value[..., self.ks] = self.zpowers[v[..., :self.n] % 2]
        value[..., self.es] = v[..., self.n:] % 2
        return value

    def encode(self, x):
        return {'exact_coordinates': x.tolist()}


def main():
    started = time.monotonic()
    names = ['e_a6_double_cover_root.npz', 'de_ferrari_a6_kernels.npz',
             'de_ferrari_a6_model.npz']
    hashes = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}
    H, J = FerrariA6Double(), FerrariTwo(1)
    rng = np.random.default_rng(26111362)

    def generated(pair):
        seen, queue = {H.uid}, [H.uid]
        for value in queue:
            for g in pair:
                nxt = int(H.um[value, g])
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return len(queue)

    assert all(generated(pair) == 720 for pair in H.lifts)
    # Explicitly check all four central lift pairs for every old epikernel.
    lifted_pair_orders = []
    for g, h in H.lifts:
        for e1, e2 in product(range(2), repeat=2):
            count = generated([H.um[H.zpowers[e1], g], H.um[H.zpowers[e2], h]])
            assert count == 720
            lifted_pair_orders.append(count)
    gs = [H.a, H.b, H.c, H.inv(H.a), H.inv(H.b), H.inv(H.c)]
    olds = [H.old.a, H.old.b, H.old.c, H.old.inv(H.old.a), H.old.inv(H.old.b), H.old.inv(H.old.c)]
    affs = [J.a, J.b, J.c, J.inv(J.a), J.inv(J.b), J.inv(J.c)]
    for g, old, aff in zip(gs, olds, affs):
        assert np.array_equal(H.project_a6(g), old)
        assert np.array_equal(H.project_affine2(g), J.project(aff))
        assert np.array_equal(H.mul(g, H.inv(g)), H.one)
        for h in gs:
            assert np.array_equal(H.project_a6(H.mul(g, h)),
                                  H.old.mul(H.project_a6(g), H.project_a6(h)))
    value, ov, av = H.one.copy(), H.old.one.copy(), J.one.copy()
    for _ in range(1000):
        i = int(rng.integers(6))
        value, ov, av = H.mul(value, gs[i]), H.old.mul(ov, olds[i]), J.mul(av, affs[i])
        assert np.array_equal(H.project_a6(value), ov)
        assert np.array_equal(H.project_affine2(value), J.project(av))
        assert np.array_equal(H.mul(value, H.inv(value)), H.one)
    GL = np.array([np.array(v).reshape(2, 2) for v in product(range(2), repeat=4)
                   if (v[0]*v[3] - v[1]*v[2]) % 2], dtype=np.int64)
    assert len(GL) == 6

    def random_element():
        value = H.one.copy()
        value[H.ps] = rng.permutation(H.n)
        value[H.cs] = rng.integers(1440, size=H.n)
        value[H.es] = rng.integers(2, size=2*H.n)
        value[H.ms] = GL[int(rng.integers(6))].ravel()
        value[H.ks] = rng.integers(720, size=H.n)
        value[H.ts] = rng.integers(2, size=2)
        return value

    for _ in range(100):
        u, v, w = (random_element() for _ in range(3))
        assert np.array_equal(H.mul(H.mul(u, v), w), H.mul(u, H.mul(v, w)))
        assert np.array_equal(H.mul(u, H.inv(u)), H.one)
        assert np.array_equal(H.mul(H.inv(u), u), H.one)
    I = np.eye(159, dtype=np.int64)
    kernel = H.relative_kernel_element(I)
    for i, k in enumerate(kernel):
        assert np.array_equal(H.power(k, 2), H.one)
        assert np.array_equal(H.relative_kernel_vector(H.mul(k, kernel)), (I[i] + I) % 2)
    actions = np.array([H.relative_kernel_vector(H.conj(g, kernel)) for g in gs])
    for i, g in enumerate(gs):
        for j, h in enumerate(gs):
            actual = H.relative_kernel_vector(H.conj(H.mul(g, h), kernel))
            assert np.array_equal(actual, actions[j] @ actions[i] % 2)
    for _ in range(50):
        word = [int(v) for v in rng.choice([1, 2, -1, -2], size=31)]
        value = H.word(word, (H.xi1, H.xi2))
        chars = value[H.ts]
        for j, (g, h) in enumerate(H.lifts):
            for e1, e2 in product(range(2), repeat=2):
                pair = [H.um[H.zpowers[e1], g], H.um[H.zpowers[e2], h]]
                actual = H.uid
                for letter in word:
                    actual = int(H.um[actual, pair[letter-1] if letter > 0 else H.ui[pair[-letter-1]]])
                expected = H.um[H.zpowers[(e1*chars[0] + e2*chars[1]) % 2], value[H.ks][j]]
                assert actual == expected
    braid_orders = []
    for g in gs[:3]:
        value = H.one.copy()
        for k in range(1, 241):
            value = H.mul(value, g)
            if np.array_equal(value, H.one):
                braid_orders.append(k)
                break
        else:
            raise AssertionError('Braid order exceeds the tested bound 240.')
    assert np.array_equal(H.project_a6(H.x), H.old.x)
    assert np.array_equal(H.project_a6(H.y), H.old.y)
    assert np.array_equal(H.project_affine2(H.x), J.project(J.x))
    assert np.array_equal(H.project_affine2(H.y), J.project(J.y))
    result = {
        'status': 'PASS_EXACT_CENTRAL_DOUBLE_A6_FERRARI_MODEL',
        'cover_order': 720, 'chosen_A6_epikernels': 53,
        'lifts_per_epikernel': 4, 'all_cover_epimorphism_kernel_count': 212,
        'free_image_order_from_actual_central_perfect_comparison': 4 * 720**53,
        'global_abelian_character_rank': 2,
        'central_cross_term_ambient_dimension': 106,
        'relative_kernel_over_A6_and_affine2_ambient_dimension': 159,
        'all_212_lift_pairs_generate_cover': len(lifted_pair_orders) == 212,
        'all_literal_Ferrari_and_braid_relations_checked': True,
        'all_six_pure_evaluation_projection_pairs_checked': True,
        'successive_braid_word_projection_checks': 1000,
        'independent_ambient_associativity_and_inverse_checks': 100,
        'all_159_squared_kernel_basis_products_and_conjugation_laws_checked': True,
        'all_212_evaluations_on_literal_free_words_checked': 50,
        'braid_generator_orders': braid_orders,
        'input_sha256': hashes,
        'source_kernel_or_whole_CM_fibre_conclusion': False,
        'seconds': round(time.monotonic() - started, 3),
    }
    np.savez_compressed(HERE / (STEM + '.npz'), a=H.a, b=H.b, c=H.c,
                        x=H.x, y=H.y, xi1=H.xi1, xi2=H.xi2,
                        chosen_lift_pairs=H.lifts, relative_kernel_conjugation=actions)
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / name).read_bytes()).hexdigest() == digest for name, digest in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()

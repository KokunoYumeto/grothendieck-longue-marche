#!/usr/bin/env python3
"""Actual compact cup forms and equivariant p-adic similitude corrections.

The cup form is computed from every oriented Schreier boundary word by
the integer Heisenberg multiplication rule. No arbitrary symplectic form
is substituted for the cover form. The lifting step averages an actual
solution of H^t J+J H=Delta, including at p=2.
"""
from itertools import product
from pathlib import Path
import json
import random
import numpy as np
from a_peripheral_count import Group
from a_coprime_frattini import Cover, pivots, inverse

HERE = Path(__file__).resolve().parent


def unit_inverse(A, modulus, p):
    A = np.array(A, dtype=np.int64) % modulus
    n = len(A)
    B = np.concatenate((A, np.eye(n, dtype=np.int64)), axis=1)
    for col in range(n):
        candidates = [j for j in range(col, n) if B[j, col] % p]
        assert candidates
        row = candidates[0]
        B[[col, row]] = B[[row, col]]
        B[col] = B[col]*pow(int(B[col, col]), -1, modulus) % modulus
        for j in range(n):
            if j != col and B[j, col]:
                B[j] = (B[j]-B[j, col]*B[col]) % modulus
    assert np.array_equal(B[:, :n], np.eye(n, dtype=np.int64))
    return B[:, n:]


class IntegralCover:
    def __init__(self, D, dx, dy, p):
        self.base = C = Cover(D, dx, dy, p)
        self.D, self.p, self.n, self.m, self.b = D, p, D.size, C.m, C.b
        self.c = C.m-C.b
        self.paths, self.generators = C.paths, C.generators
        self.M = np.column_stack([self.chain(w)[1] for w in C.schreier_words])
        rows = []
        for j in range(self.m):
            target = np.eye(self.m, dtype=np.int64)[j]
            rows.append(next(i for i in range(2*self.n)
                             if np.array_equal(self.M[i], target)))
        self.Mleft = np.eye(2*self.n, dtype=np.int64)[rows]
        assert np.array_equal(self.Mleft @ self.M, np.eye(self.m, dtype=np.int64))
        self.A = [self.Mleft @ self.left_matrix(d) @ self.M for d in range(self.n)]
        self.edge_chord = {}
        for d in range(self.n):
            for letter in (1, 2):
                e = D.mul[d][self.generators[letter]]
                word = self.paths[d]+[letter]+[-a for a in self.paths[e][::-1]]
                v = self.Mleft @ self.chain(word)[1]
                nonzero = np.flatnonzero(v)
                assert len(nonzero) <= 1
                if len(nonzero):
                    j = int(nonzero[0])
                    assert v[j] == 1
                    self.edge_chord[d, letter] = j+1
                else:
                    self.edge_chord[d, letter] = 0
        self.boundary_words, boundary_vectors = [], []
        peripheral_words = ([1], [2], [-2, -1])
        for rec in C.boundary_records:
            i, d, e = rec['peripheral'], rec['coset'], rec['order']
            word = self.paths[d]+list(peripheral_words[i])*e+[-a for a in self.paths[d][::-1]]
            rewritten = self.rewrite(word)
            exponents = np.zeros(self.m, dtype=np.int64)
            for a in rewritten:
                exponents[abs(a)-1] += 1 if a > 0 else -1
            assert np.array_equal(exponents, self.Mleft @ self.chain(word)[1])
            self.boundary_words.append(rewritten)
            boundary_vectors.append(exponents)
        self.Bfull = np.column_stack(boundary_vectors)
        assert not np.any(np.sum(self.Bfull, axis=1))
        self.B = self.Bfull[:, C.basis_boundary_indices]
        basis = self.B.copy()
        for j in range(self.m):
            proposed = np.column_stack((basis, np.eye(self.m, dtype=np.int64)[:, j]))
            if len(pivots(proposed, p)) > basis.shape[1]:
                basis = proposed
            if basis.shape[1] == self.m:
                break
        self.basis = basis
        self.Craw = basis[:, self.b:]

    def chain(self, word):
        vertex = self.D.one
        vector = np.zeros(2*self.n, dtype=np.int64)
        for a in word:
            if a > 0:
                vector[(a-1)*self.n+vertex] += 1
                vertex = self.D.mul[vertex][self.generators[a]]
            else:
                vertex = self.D.mul[vertex][self.generators[a]]
                vector[(-a-1)*self.n+vertex] -= 1
        return vertex, vector

    def left(self, d, v):
        out = np.zeros_like(v)
        for j in range(2):
            for a in range(self.n):
                out[j*self.n+self.D.mul[d][a]] = v[j*self.n+a]
        return out

    def left_matrix(self, d):
        return np.column_stack([self.left(d, e)
                                for e in np.eye(2*self.n, dtype=np.int64)])

    def rewrite(self, word):
        vertex, out = self.D.one, []
        for a in word:
            if a > 0:
                chord = self.edge_chord[vertex, a]
                vertex = self.D.mul[vertex][self.generators[a]]
            else:
                vertex = self.D.mul[vertex][self.generators[a]]
                chord = -self.edge_chord[vertex, -a]
            if chord:
                out.append(chord)
        assert vertex == self.D.one
        return out

    def coordinates(self, modulus):
        p, D = self.p, self.D
        bi = unit_inverse(self.basis, modulus, p)
        E = bi[self.b:, :]
        actions = [E @ a @ self.Craw % modulus for a in self.A]
        # Exact Heisenberg evaluation on all oriented boundary relators.
        cup = np.zeros((self.c, self.c), dtype=np.int64)
        for word in self.boundary_words:
            prefix = np.zeros(self.c, dtype=np.int64)
            for a in word:
                v = E[:, abs(a)-1]
                if a > 0:
                    cup = (cup+np.outer(prefix, v)) % modulus
                    prefix = (prefix+v) % modulus
                else:
                    cup = (cup-np.outer(prefix, v)+np.outer(v, v)) % modulus
                    prefix = (prefix-v) % modulus
            assert not np.any(prefix)
        assert not np.any(np.diag(cup) % modulus)
        assert not np.any((cup+cup.T) % modulus)
        J = unit_inverse(cup, modulus, p)
        for a in actions:
            assert np.array_equal(a @ cup @ a.T % modulus, cup)
            assert np.array_equal(a.T @ J @ a % modulus, J)
        raw_projector = self.B @ bi[:self.b, :] % modulus
        PB = sum((self.A[d] @ raw_projector @ self.A[D.inv[d]]
                  for d in range(self.n)),
                 np.zeros((self.m, self.m), dtype=np.int64))
        PB = PB*pow(self.n, -1, modulus) % modulus
        Csection = (np.eye(self.m, dtype=np.int64)-PB) @ self.Craw % modulus
        assert np.array_equal(E @ Csection % modulus, np.eye(self.c, dtype=np.int64))
        assert not np.any(E @ self.B % modulus)
        return {'quotient': E, 'actions': actions, 'cup': cup, 'J': J,
                'PB': PB, 'Csection': Csection, 'basis_inverse': bi}

    def power_source_matrix(self, alpha, lam):
        columns = []
        for letter in (1, 2):
            word_chain = self.chain([letter]*lam)[1]
            for d in range(self.n):
                columns.append(self.left(alpha[d], word_chain))
        return self.Mleft @ np.column_stack(columns) @ self.M


def commutant_basis(actions, D, p):
    c = len(actions[0])
    candidates = []
    for i in range(c):
        for j in range(c):
            h = np.zeros((c, c), dtype=np.int64)
            h[i, j] = 1
            h = sum((actions[d] @ h @ actions[D.inv[d]] for d in range(D.size)),
                    np.zeros((c, c), dtype=np.int64))
            h = h*pow(D.size, -1, p) % p
            candidates.append(h)
    flat = np.column_stack([a.reshape(-1) for a in candidates])
    return [candidates[j] for j in pivots(flat, p)]


def find_isometry(initial, J, lam, basis, p, seed):
    c = len(J)
    target, old = lam*J % p, initial.T @ J @ initial % p
    identity = np.eye(c, dtype=np.int64)
    if np.array_equal(old, target):
        return identity, 0, []
    rng = random.Random(seed)
    seen = set()
    for attempt in range(1, 200001):
        coefficients = tuple(rng.randrange(p) for _ in basis)
        if coefficients in seen:
            continue
        seen.add(coefficients)
        R = sum((a*b for a, b in zip(coefficients, basis)),
                np.zeros((c, c), dtype=np.int64)) % p
        if np.array_equal(R.T @ old @ R % p, target):
            inverse(R, p)
            return R, attempt, list(coefficients)
    # Guaranteed finite fallback; the theorem proves a solution exists.
    for coefficients in product(range(p), repeat=len(basis)):
        if coefficients in seen:
            continue
        R = sum((a*b for a, b in zip(coefficients, basis)),
                np.zeros((c, c), dtype=np.int64)) % p
        if np.array_equal(R.T @ old @ R % p, target):
            inverse(R, p)
            return R, 200000+len(seen), list(coefficients)
    raise AssertionError('The complete finite isometry space was empty')


def main():
    records = []
    for dim in (1, 2):
        elements = list(product(range(5), repeat=dim))
        D = Group('C5' if dim == 1 else 'C5^2', elements,
                  lambda a, b: tuple((x+y) % 5 for x, y in zip(a, b)),
                  (0,)*dim)
        dx = D.index[(1,) if dim == 1 else (1, 0)]
        dy = D.index[(2,) if dim == 1 else (0, 1)]
        for p in (2, 3):
            C = IntegralCover(D, dx, dy, p)
            precision, modulus = 6, p**6
            data = C.coordinates(modulus)
            E, J, actions = data['quotient'], data['J'], data['actions']
            small_actions = [a % p for a in actions]
            centralizer = commutant_basis(small_actions, D, p)
            assert len(centralizer) == C.c
            cases = []
            for k in (1, 2, 3, 4):
                lam = next(a for a in range(k, k+5*p, 5) if a % p)
                alpha = [D.index[tuple(k*a % 5 for a in d)] for d in D.elements]
                phi = C.power_source_matrix(alpha, lam)
                assert not np.any(E @ phi @ C.B % modulus)
                initial = E @ phi @ C.Craw % p
                inverse(initial, p)
                assert all(np.array_equal(initial @ small_actions[d] % p,
                                          small_actions[alpha[d]] @ initial % p)
                           for d in range(D.size))
                R, attempts, coeffs = find_isometry(
                    initial, J % p, lam % p, centralizer, p,
                    17000+1000*dim+100*p+k)
                T0 = initial @ R % p
                assert np.array_equal(T0.T @ J @ T0 % p, lam*J % p)
                # Average an arbitrary lift of T0 to an exact intertwiner.
                T = sum((actions[alpha[d]] @ T0 @ actions[D.inv[d]]
                         for d in range(D.size)),
                        np.zeros((C.c, C.c), dtype=np.int64))
                T = T*pow(D.size, -1, modulus) % modulus
                assert np.array_equal(T % p, T0)
                steps = []
                for a in range(1, precision):
                    level = p**a
                    discrepancy = (lam*J-T.T @ J @ T) % modulus
                    assert not np.any(discrepancy % level)
                    delta = discrepancy//level % p
                    assert not np.any((delta+delta.T) % p)
                    assert not np.any(np.diag(delta))
                    upper = np.triu(delta, 1)
                    Hraw = inverse(lam*J % p, p) @ upper % p
                    H = sum((actions[d] @ Hraw @ actions[D.inv[d]]
                             for d in range(D.size)),
                            np.zeros((C.c, C.c), dtype=np.int64))
                    H = H*pow(D.size, -1, modulus) % modulus
                    B0 = lam*J % p
                    assert np.array_equal((H.T @ B0+B0 @ H) % p, delta)
                    T = T @ (np.eye(C.c, dtype=np.int64)+level*H) % modulus
                    assert not np.any((T.T @ J @ T-lam*J) % (p**(a+1)))
                    assert all(np.array_equal(T @ actions[d] % modulus,
                                              actions[alpha[d]] @ T % modulus)
                               for d in range(D.size))
                    steps.append({'precision': a+1, 'delta': delta.tolist(),
                                  'averaged_correction_mod_p': (H % p).tolist(),
                                  'compact_similitude': (T % (p**(a+1))).tolist()})
                unit_inverse(T, modulus, p)
                assert np.array_equal(T.T @ J @ T % modulus, lam*J % modulus)
                # Extend the exact boundary prescription to the same full
                # homology module, rather than replacing its boundary frames.
                hs = [D.index[tuple((i+1)*(j+2) % 5 for j in range(dim))]
                      for i in range(3)]
                target_columns = []
                for rec in C.base.boundary_records:
                    i, d = rec['peripheral'], rec['coset']
                    Xi_word = ([1], [2], [-2, -1])[i]
                    base_boundary = C.chain(list(Xi_word)*rec['order'])[1]
                    vector = lam*C.left(D.mul[alpha[d]][hs[i]], base_boundary)
                    target_columns.append(C.Mleft @ vector % modulus)
                target_full = np.column_stack(target_columns)
                target_basis = target_full[:, C.base.basis_boundary_indices]
                raw = target_basis @ data['basis_inverse'][:C.b, :] % modulus
                partial = sum((C.A[alpha[d]] @ raw @ C.A[D.inv[d]]
                               for d in range(D.size)),
                              np.zeros((C.m, C.m), dtype=np.int64))
                partial = partial*pow(D.size, -1, modulus) % modulus
                TM = (partial @ data['PB']+data['Csection'] @ T @ E) % modulus
                unit_inverse(TM, modulus, p)
                assert np.array_equal(TM @ C.Bfull % modulus, target_full)
                JM = E.T @ J @ E % modulus
                assert np.array_equal(TM.T @ JM @ TM % modulus, lam*JM % modulus)
                assert all(np.array_equal(TM @ C.A[d] % modulus,
                                          C.A[alpha[d]] @ TM % modulus)
                           for d in range(D.size))
                cases.append({'base_scalar': k, 'lambda': lam,
                              'base_automorphism': alpha, 'base_conjugators': hs,
                              'finite_field_search_attempts': attempts,
                              'finite_field_commutant_coefficients': coeffs,
                              'finite_field_correction': R.tolist(),
                              'initial_compact_similitude': T0.tolist(),
                              'hensel_steps': steps,
                              'full_homology_similitude_mod_p6': TM.tolist(),
                              'compact_similitude_mod_p6': T.tolist()})
            records.append({'base': D.name, 'order': D.size, 'p': p,
                            'precision': precision, 'modulus': modulus,
                            'homology_rank': C.m, 'boundary_rank': C.b,
                            'compact_rank': C.c,
                            'boundary_words_in_actual_schreier_basis': C.boundary_words,
                            'integral_schreier_chain_basis': C.M.tolist(),
                            'integral_boundary_vectors': C.Bfull.tolist(),
                            'quotient_coordinates_mod_p6': E.tolist(),
                            'compact_cup_matrix_mod_p6': data['cup'].tolist(),
                            'compact_intersection_matrix_mod_p6': J.tolist(),
                            'compact_action_matrices_mod_p6': [a.tolist() for a in actions],
                            'commutant_dimension': len(centralizer), 'cases': cases})
            print('PASS', D.name, 'p=', p, 'compact rank=', C.c,
                  'exact oriented cup form; four equivariant similitudes through modulus',
                  modulus, flush=True)
            print('  finite-field attempts:',
                  [r['finite_field_search_attempts'] for r in cases],
                  '; nonzero Hensel steps:',
                  [sum(any(any(v for v in row) for row in s['delta'])
                       for s in r['hensel_steps']) for r in cases], flush=True)
    payload = {'status': 'PASS_ACTUAL_COVER_INTERSECTION_AND_COPRIME_HENSEL',
               'source_comparison': 'All boundary relators are rewritten from their literal based Cayley words; the sum of their Heisenberg central values is the compact cup pairing.',
               'hensel_rule': 'Hraw=(lambda J)^-1 upper(delta); average conjugates over D; T <- T*(1+p^a H). No division by2.',
               'executed_covers': records,
               'scope': 'Actual finite and p-adic pairing corrections for coprime odd bases. No full profinite peripheral automorphism is inferred.'}
    HERE.joinpath('a_coprime_intersection.json').write_text(
        json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()

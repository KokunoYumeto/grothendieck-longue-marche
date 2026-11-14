#!/usr/bin/env python3
"""Actual universal coprime Frattini covers and all prescribed boundaries.

The source is the graph Magnus image (d,v), v in the two Cayley edge
modules. All Schreier words, the boundary sum, the averaging splitting,
the semilinear matrix, and the three kernel conjugators are retained.
The proof applies to every finite coprime base; executed examples have
base C5, C5^2, and S3, in coefficient characteristics 2, 3, and 5.
"""
from collections import deque
from itertools import product, permutations
from math import gcd
from pathlib import Path
import json
import numpy as np
from a_peripheral_count import Group, perm_mul

HERE = Path(__file__).resolve().parent


def pivots(matrix, p):
    A = np.array(matrix, dtype=np.int64) % p
    row, chosen = 0, []
    for col in range(A.shape[1]):
        nz = np.flatnonzero(A[row:, col])
        if not len(nz):
            continue
        target = row + int(nz[0])
        A[[row, target]] = A[[target, row]]
        A[row] = A[row]*pow(int(A[row, col]), -1, p) % p
        for j in range(A.shape[0]):
            if j != row and A[j, col]:
                A[j] = (A[j]-A[j, col]*A[row]) % p
        chosen.append(col)
        row += 1
        if row == A.shape[0]:
            break
    return chosen


def inverse(A, p):
    A = np.array(A, dtype=np.int64) % p
    n = len(A)
    assert A.shape == (n, n)
    B = np.concatenate((A, np.eye(n, dtype=np.int64)), axis=1)
    for col in range(n):
        nz = np.flatnonzero(B[col:, col])
        assert len(nz)
        row = col+int(nz[0])
        B[[col, row]] = B[[row, col]]
        B[col] = B[col]*pow(int(B[col, col]), -1, p) % p
        for j in range(n):
            if j != col and B[j, col]:
                B[j] = (B[j]-B[j, col]*B[col]) % p
    assert np.array_equal(B[:, :n], np.eye(n, dtype=np.int64))
    return B[:, n:]


def left_inverse(A, p):
    rows = pivots(A.T, p)
    assert len(rows) == A.shape[1]
    selection = np.eye(A.shape[0], dtype=np.int64)[rows]
    return inverse(A[rows, :], p) @ selection % p


class Cover:
    def __init__(self, D, dx, dy, p):
        self.D, self.p, self.n = D, p, D.size
        assert self.n % p
        self.m = self.n+1
        self.generators = {1: dx, 2: dy, -1: D.inv[dx], -2: D.inv[dy]}
        self.edges = 2*self.n
        self.zero = np.zeros(self.edges, dtype=np.int64)
        self.identity = D.one, self.zero.copy()
        self.x = dx, np.eye(self.edges, dtype=np.int64)[D.one]
        self.y = dy, np.eye(self.edges, dtype=np.int64)[self.n+D.one]
        self.paths = {D.one: []}
        todo = deque([D.one])
        while todo:
            d = todo.popleft()
            for letter in (1, 2, -1, -2):
                e = D.mul[d][self.generators[letter]]
                if e not in self.paths:
                    self.paths[e] = self.paths[d]+[letter]
                    todo.append(e)
        assert len(self.paths) == self.n
        self.path_chains = [self.word(self.paths[d])[1] for d in range(self.n)]
        cycles, words = [], []
        for d in range(self.n):
            for j in (1, 2):
                e = D.mul[d][self.generators[j]]
                word = self.paths[d]+[j]+[-a for a in self.paths[e][::-1]]
                value = self.word(word)
                assert value[0] == D.one
                cycles.append(value[1])
                words.append(word)
        all_cycles = np.column_stack(cycles)
        chosen = pivots(all_cycles, p)
        assert len(chosen) == self.m
        self.M = all_cycles[:, chosen]
        self.Mleft = left_inverse(self.M, p)
        self.schreier_words = [words[i] for i in chosen]
        self.actions = [self.Mleft @ self.left_matrix(d) @ self.M % p
                        for d in range(self.n)]
        assert all(np.array_equal(self.left_matrix(d) @ self.M % p,
                                  self.M @ self.actions[d] % p)
                   for d in range(self.n))
        self.kappa = sum(self.path_chains, self.zero.copy())*pow(self.n, -1, p) % p
        self.boundary_records, boundary_columns = [], []
        self.peripherals = [self.x, self.y, self.gi(self.gm(self.x, self.y))]
        for i, Xi in enumerate(self.peripherals):
            di = Xi[0]
            ei = D.orders[di]
            bi = self.gp(Xi, ei)
            assert bi[0] == D.one
            seen = set()
            for d in range(self.n):
                if d in seen:
                    continue
                orbit, e = [], d
                for _ in range(ei):
                    orbit.append(e)
                    seen.add(e)
                    e = D.mul[e][di]
                assert e == d and len(set(orbit)) == ei
                chain = self.left(d, bi[1])
                coordinates = self.Mleft @ chain % p
                assert np.array_equal(self.M @ coordinates % p, chain)
                boundary_columns.append(coordinates)
                self.boundary_records.append({'peripheral': i, 'coset': d,
                                              'orbit': orbit, 'order': ei})
        self.Bfull = np.column_stack(boundary_columns)
        assert not np.any(np.sum(self.Bfull, axis=1) % p)
        self.basis_boundary_indices = pivots(self.Bfull, p)
        self.b = len(self.basis_boundary_indices)
        assert self.b == len(self.boundary_records)-1
        self.B = self.Bfull[:, self.basis_boundary_indices]
        basis = self.B.copy()
        for col in range(self.m):
            extra = np.eye(self.m, dtype=np.int64)[:, [col]]
            proposed = np.concatenate((basis, extra), axis=1)
            if len(pivots(proposed, p)) > basis.shape[1]:
                basis = proposed
            if basis.shape[1] == self.m:
                break
        basis_inv = inverse(basis, p)
        raw_projector = self.B @ basis_inv[:self.b, :] % p
        self.PB = sum((self.actions[d] @ raw_projector @
                       self.actions[D.inv[d]] for d in range(self.n)),
                      np.zeros((self.m, self.m), dtype=np.int64))
        self.PB = self.PB*pow(self.n, -1, p) % p
        assert np.array_equal(self.PB @ self.PB % p, self.PB)
        assert np.array_equal(self.PB @ self.B % p, self.B)
        assert len(pivots(self.PB, p)) == self.b
        self.boundary_coordinate_rows = basis_inv[:self.b, :]
        assert all(np.array_equal(self.PB @ a % p, a @ self.PB % p)
                   for a in self.actions)
        # The splitting is verified on every literal pair of base elements.
        for d in range(self.n):
            for e in range(self.n):
                assert self.equal(self.gm(self.split(d), self.split(e)),
                                  self.split(D.mul[d][e]))

    def left(self, d, v):
        out = np.zeros_like(v)
        for j in range(2):
            for a in range(self.n):
                out[j*self.n+self.D.mul[d][a]] = v[j*self.n+a]
        return out % self.p

    def left_matrix(self, d):
        return np.column_stack([self.left(d, row)
                                for row in np.eye(self.edges, dtype=np.int64)])

    def gm(self, x, y):
        return self.D.mul[x[0]][y[0]], (x[1]+self.left(x[0], y[1])) % self.p

    def gi(self, x):
        di = self.D.inv[x[0]]
        return di, -self.left(di, x[1]) % self.p

    def gp(self, x, k):
        if k < 0:
            return self.gp(self.gi(x), -k)
        out = self.identity
        while k:
            if k & 1:
                out = self.gm(out, x)
            x = self.gm(x, x)
            k >>= 1
        return out

    def conjugate(self, a, b):
        return self.gm(self.gm(a, b), self.gi(a))

    def equal(self, a, b):
        return a[0] == b[0] and np.array_equal(a[1] % self.p, b[1] % self.p)

    def word(self, word):
        out = self.identity
        for letter in word:
            value = self.x if abs(letter) == 1 else self.y
            out = self.gm(out, value if letter > 0 else self.gi(value))
        return out

    def split(self, d):
        return d, (self.kappa-self.left(d, self.kappa)) % self.p

    def source_chain(self, alpha, lam):
        columns = []
        for Xi in (self.x, self.y):
            w = self.gp(Xi, lam)[1]
            for d in range(self.n):
                columns.append(self.left(alpha[d], w))
        chain_map = np.column_stack(columns)
        result = self.Mleft @ chain_map @ self.M % self.p
        assert np.array_equal(self.M @ result % self.p, chain_map @ self.M % self.p)
        return result

    def lift(self, alpha, lam, hs, initial):
        p, D = self.p, self.D
        assert sorted(alpha) == list(range(self.n))
        assert all(alpha[D.mul[d][e]] == D.mul[alpha[d]][alpha[e]]
                   for d in range(self.n) for e in range(self.n))
        assert gcd(lam, p) == 1
        target_columns = []
        for rec in self.boundary_records:
            i, d = rec['peripheral'], rec['coset']
            Xi = self.peripherals[i]
            assert alpha[Xi[0]] == D.conjugate(hs[i], D.power(Xi[0], lam))
            bi = self.gp(Xi, rec['order'])[1]
            target = lam*self.left(D.mul[alpha[d]][hs[i]], bi) % p
            target_columns.append(self.Mleft @ target % p)
        target_full = np.column_stack(target_columns)
        target_basis = target_full[:, self.basis_boundary_indices]
        raw = target_basis @ self.boundary_coordinate_rows % p
        partial = sum((self.actions[alpha[d]] @ raw @ self.actions[D.inv[d]]
                       for d in range(self.n)),
                      np.zeros((self.m, self.m), dtype=np.int64))
        partial = partial*pow(self.n, -1, p) % p
        assert np.array_equal(partial @ self.Bfull % p, target_full)
        assert np.array_equal(self.PB @ initial @ self.B % p, initial @ self.B % p)
        inverse(initial, p)
        T = (partial @ self.PB + initial @
             (np.eye(self.m, dtype=np.int64)-self.PB)) % p
        Ti = inverse(T, p)
        assert np.array_equal(T @ self.Bfull % p, target_full)
        assert all(np.array_equal(T @ self.actions[d] % p,
                                  self.actions[alpha[d]] @ T % p)
                   for d in range(self.n))

        def actual_automorphism(value):
            d, v = value
            module_chain = (v-self.split(d)[1]) % p
            module = self.Mleft @ module_chain % p
            assert np.array_equal(self.M @ module % p, module_chain)
            return alpha[d], (self.M @ T @ module+self.split(alpha[d])[1]) % p

        conjugators = []
        for i, Xi in enumerate(self.peripherals):
            # Include an arbitrary kernel part in the chosen lift H_i.
            vector = np.array([(i+1)*(j+2)+lam for j in range(self.m)],
                              dtype=np.int64) % p
            H = self.gm((D.one, self.M @ vector % p), self.split(hs[i]))
            U = self.conjugate(H, self.gp(Xi, lam))
            image = actual_automorphism(Xi)
            e = D.orders[Xi[0]]
            assert self.equal(self.gp(image, e), self.gp(U, e))
            difference = self.gm(image, self.gi(U))
            assert difference[0] == D.one
            v = self.Mleft @ difference[1] % p
            action = self.actions[alpha[Xi[0]]]
            norm, weighted, term = np.zeros(self.m, dtype=np.int64), np.zeros(self.m, dtype=np.int64), v
            for j in range(e):
                norm = (norm+term) % p
                weighted = (weighted+j*term) % p
                term = action @ term % p
            assert not np.any(norm)
            a = -pow(e, -1, p)*weighted % p
            kernel_element = D.one, self.M @ a % p
            assert self.equal(self.conjugate(kernel_element, U), image)
            conjugators.append({'base_h': hs[i], 'chosen_H_kernel_part': vector.tolist(),
                                'correcting_kernel_conjugator': a.tolist(),
                                'peripheral_order_in_D': e,
                                'image_chain': image[1].tolist()})
        # Verify the semidirect multiplication on a spanning collection.
        samples = [self.x, self.y]+[self.split(d) for d in range(self.n)]
        samples += [(D.one, self.M[:, j]) for j in range(self.m)]
        for a in samples:
            for b in samples[:self.n+2]:
                assert self.equal(actual_automorphism(self.gm(a, b)),
                                  self.gm(actual_automorphism(a), actual_automorphism(b)))
        return {'lambda': lam, 'base_automorphism': alpha, 'base_conjugators': hs,
                'module_automorphism': T.tolist(), 'module_inverse': Ti.tolist(),
                'peripheral_conjugators': conjugators}

    def metadata(self):
        return {'base': self.D.name, 'base_order': self.n, 'prime': self.p,
                'cover_order': self.n*self.p**self.m, 'kernel_rank': self.m,
                'boundary_count': self.b+1, 'boundary_rank': self.b,
                'compact_rank': self.m-self.b,
                'paths': [self.paths[d] for d in range(self.n)],
                'schreier_basis_words': self.schreier_words,
                'schreier_chain_basis': self.M.tolist(),
                'boundary_records': self.boundary_records,
                'all_boundary_vectors': self.Bfull.tolist(),
                'boundary_projector': self.PB.tolist(),
                'averaging_chain': self.kappa.tolist()}


def main():
    records, total = [], 0
    for dim in (1, 2):
        elems = list(product(range(5), repeat=dim))
        D = Group('C5' if dim == 1 else 'C5^2', elems,
                  lambda a, b: tuple((x+y) % 5 for x, y in zip(a, b)),
                  (0,)*dim)
        dx = D.index[(1,) if dim == 1 else (1, 0)]
        dy = D.index[(2,) if dim == 1 else (0, 1)]
        for p in (2, 3):
            C = Cover(D, dx, dy, p)
            rows = []
            for k in (1, 2, 3, 4):
                lam = next(a for a in range(k, k+5*p, 5) if a % p)
                alpha = [D.index[tuple(k*a % 5 for a in d)] for d in D.elements]
                hs = [D.index[tuple((i+1)*(j+2) % 5 for j in range(dim))]
                      for i in range(3)]
                initial = C.source_chain(alpha, lam)
                rows.append(C.lift(alpha, lam, hs, initial))
            data = C.metadata()
            data['cases'] = rows
            records.append(data)
            total += len(rows)
            print('PASS', D.name, 'p=', p, 'kernel', C.m, 'boundary', C.b,
                  'compact', C.m-C.b, 'four scalar base automorphisms', flush=True)
    D = Group('S3', list(permutations(range(3))), perm_mul, tuple(range(3)))
    dx, dy = D.index[(1, 0, 2)], D.index[(1, 2, 0)]
    C = Cover(D, dx, dy, 5)
    h = dy
    alpha = [D.conjugate(h, d) for d in range(D.size)]
    centralizers = [sorted(D.centralizer(Xi[0])) for Xi in C.peripherals]
    rows = []
    for cs in product(*centralizers):
        hs = [D.mul[h][c] for c in cs]
        rows.append(C.lift(alpha, 1, hs, C.actions[h]))
    assert len(rows) == 12
    data = C.metadata()
    data['cases'] = rows
    records.append(data)
    total += len(rows)
    print('PASS S3 p=5, all12 base-centralizer triples, compact rank0', flush=True)
    payload = {'status': 'PASS_ACTUAL_COPRIME_FRATTINI_PERIPHERAL_AUTOMORPHISMS',
               'total_cases': total,
               'source_model': '(d,v)(e,w)=(de,v+d*w), actual two Cayley edge modules',
               'splitting': 's(d)=(d,kappa-d*kappa), kappa=|D|^-1 sum of based Cayley paths',
               'boundary_sum': 'The sum of all oriented peripheral-cycle vectors is zero, and this is their only relation',
               'kernel_conjugator': '-e^-1 sum_(j=0)^(e-1) j*alpha(d)^j*v',
               'executed_covers': records,
               'scope': 'Actual universal elementary-p covers for coprime p and base, with complete prescribed conjugators. Further same-prime cover layers are not inferred.'}
    HERE.joinpath('a_coprime_frattini.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'], 'cases=', total)


if __name__ == '__main__':
    main()

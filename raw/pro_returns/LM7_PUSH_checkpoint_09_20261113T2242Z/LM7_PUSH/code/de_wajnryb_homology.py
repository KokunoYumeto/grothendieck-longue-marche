#!/usr/bin/env python3
"""Integral Wajnryb homology and its exact earlier-source factorization.

All presentation and block identities are checked over Z.  The final
finite comparison uses the retained right-permutation conventions and
every actual six-coset transition, without changing any older artifact.
"""
from hashlib import sha256
from pathlib import Path
from itertools import product
import json
import time
import numpy as np
import sympy as sp
from e_hurwitz_five_source_root import Evaluations, Source
from de_ferrari_a6_source_data import load_data

HERE = Path(__file__).resolve().parent
STEM = 'de_wajnryb_homology'


def product_matrix(xs, n):
    out = sp.eye(n)
    for x in xs:
        out = out * x
    return out


def model(g, transpose=False):
    n = 2*g
    J = sp.zeros(n)
    for i in range(n-1):
        J[i, i+1], J[i+1, i] = 1, -1
    I = sp.eye(n)
    e = [I[:, i] for i in range(n)]
    def T(v):
        a = I+v*v.T*J
        return a.T if transpose else a
    a = [T(v) for v in e]
    d = T(e[0]+e[2])
    return J, e, a, d, T


def yword(a, k):
    return product_matrix(list(reversed(a[:k-1]))+a[:k-1], a[0].rows)


def presentation(g, transpose=False):
    J, e, a, d, T = model(g, transpose)
    n = 2*g
    equations = []
    for i in range(n-1):
        assert a[i]*a[i+1]*a[i] == a[i+1]*a[i]*a[i+1]
        equations.append(['chain_braid', i+1, i+2])
    for i in range(n):
        for j in range(i+2, n):
            assert a[i]*a[j] == a[j]*a[i]
            equations.append(['chain_commutation', i+1, j+1])
    for i in range(n):
        if i == 3:
            assert d*a[i]*d == a[i]*d*a[i]
            equations.append(['d_braid', i+1])
        else:
            assert d*a[i] == a[i]*d
            equations.append(['d_commutation', i+1])
    Y5 = yword(a, 5)
    assert d*Y5*d*Y5.inv() == product_matrix(a[:3], n)**4
    equations.append(['B'])
    if g >= 3:
        t = [a[2*k-1]*a[2*k-2]*a[2*k]*a[2*k-1]
             for k in range(1, g)]
        d3 = ((t[0].inv()*t[1].inv()*d*t[1]*t[0]) *
              (t[1].inv()*d*t[1])*d*a[0].inv()*a[2].inv()*a[4].inv())
        assert d3 == T(e[0]+e[2]+e[4])
        assert d3*a[5]*d3 == a[5]*d3*a[5]
        equations.append(['C_and_literal_d3'])
        if g >= 4:
            h = t[1]*t[0]*t[2]*t[1]
            dp = Y5*d*Y5.inv()
            assert dp*h*d*h.inv() == h*d*h.inv()*dp
            equations.append(['Cprime'])
    return equations


class MatrixEvaluations(Evaluations):
    def __init__(self, rows, pairs, prime):
        self.prime = prime
        self.points = np.array([v for v in product(range(prime), repeat=rows[0].rows)
                                if any(v)], dtype=np.int64)
        self.index = {tuple(v): i for i, v in enumerate(self.points)}
        self.degree = len(self.points)
        self.one = np.arange(self.degree, dtype=np.int64)
        self.sigma = np.array([self.permutation(a) for a in rows])
        self.x = np.array([self.permutation(a) for a, b in pairs])
        self.y = np.array([self.permutation(b) for a, b in pairs])
        self.count = len(pairs)

    def permutation(self, row_matrix):
        a = np.array(row_matrix, dtype=np.int64) % self.prime
        image = self.points @ a % self.prime
        p = np.array([self.index[tuple(v)] for v in image], dtype=np.int64)
        assert np.array_equal(np.sort(p), self.one)
        return p


class OldEvaluations(Evaluations):
    def __init__(self, data):
        self.sigma, self.x, self.y = data['sigma'], data['x'], data['y']
        self.points = data['points']
        self.degree, self.count = self.sigma.shape[1], len(self.x)
        self.one = np.arange(self.degree, dtype=np.int64)
        self.index = {tuple(v): i for i, v in enumerate(self.points)}

    def row_matrix(self, p):
        return np.array([self.points[p[self.index[tuple(v)]]]
                         for v in np.eye(4, dtype=np.int64)], dtype=np.int64)


def main():
    start = time.time()
    names = ['e_symplectic_five_p3_model_root.npz',
             'e_hurwitz_five_source_root.py', 'de_ferrari_a6_source_data.py',
             'de_ferrari_mod9_lift.py', 'de_ferrari_sl2_5_N.json']
    hashes = {n: sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    checks = {f'g{g}_transpose{int(t)}': presentation(g, t)
              for g in (2, 3, 4) for t in (False, True)}
    J, e, a, d, T = model(3)
    _, _, b, _, _ = model(2)
    P0 = sp.Matrix.hstack(e[0], e[1], e[2], e[3], e[0]+e[2]+e[4], e[5])
    P1 = sp.Matrix.hstack(e[0]+e[2], e[3], e[4], e[5], e[0], e[1])
    assert abs(P0.det()) == abs(P1.det()) == 1
    assert P0.T*J*P0 == sp.diag(model(2)[0], sp.Matrix([[0, 1], [-1, 0]]))
    assert P1.T*J*P1 == sp.diag(model(2)[0], sp.Matrix([[0, 1], [-1, 0]]))
    rows = []
    for k in range(2, 7):
        old_k = k if k <= 4 else k-2
        P = P0 if k <= 4 else P1
        sign = 1 if k <= 4 else -1
        Y, Z = yword(a, k), a[k-1]**2
        U, V = yword(b, old_k), b[old_k-1]**2
        assert P.inv()*Y*P == sp.diag(U, sign*sp.eye(2))
        assert P.inv()*Z*P == sp.diag(V, sp.eye(2))
        if k >= 5:
            assert U[:, 0] == -sp.eye(4)[:, 0]
            assert V[:, 0] == sp.eye(4)[:, 0]
        rows.append({'new_index': k, 'old_index': old_k,
                     'old_eight_evaluation_index_zero_based': old_k+3,
                     'column_basis': 'P0' if k <= 4 else 'P1',
                     'scalar_x': sign, 'scalar_y': 1,
                     'extra_scalar_is_same_old_e1_character': k >= 5})

    # Independent orientation check against the saved right permutations.
    old_data = np.load(HERE/names[0])
    O = OldEvaluations(old_data)
    _, _, ar, dr, _ = model(3, True)
    _, _, br, _, _ = model(2, True)
    for i in range(4):
        assert np.array_equal(O.row_matrix(O.sigma[i]), np.array(br[i], dtype=np.int64) % 3)
    for k in range(2, 5):
        j = k+3
        assert np.array_equal(O.row_matrix(O.x[j]), np.array(yword(br, k), dtype=np.int64) % 3)
        assert np.array_equal(O.row_matrix(O.y[j]), np.array(br[k-1]**2, dtype=np.int64) % 3)
    pairs = [(yword(ar, k), ar[k-1]**2) for k in range(2, 7)]
    H = MatrixEvaluations(ar+[dr], pairs, 3)
    data = load_data()
    old_source, new_source = Source(O, data), Source(H, data)
    assert old_source.Q == new_source.Q and old_source.section == new_source.section
    finite_checks = 0
    reconstructed = []
    for letter in (0, 1, -1):
        old, new = old_source.letters[letter], new_source.letters[letter]
        assert np.array_equal(old[0], new[0])
        values = []
        for q in range(6):
            qvalues = []
            for k in range(2, 7):
                old_k = k if k <= 4 else k-2
                M = O.row_matrix(old[1][q, old_k+3])
                scalar = 1
                if k >= 5:
                    scalar = int(M[0, 0])
                    assert np.array_equal(M[0] % 3, np.array([scalar, 0, 0, 0]) % 3)
                    assert scalar in (1, 2)
                P = P0 if k <= 4 else P1
                new_row = P.T.inv()*sp.diag(sp.Matrix(M), scalar*sp.eye(2))*P.T
                p = H.permutation(new_row)
                assert np.array_equal(p, new[1][q, k-2])
                qvalues.append(p)
                finite_checks += 1
            values.append(qvalues)
        reconstructed.append(np.array(values, dtype=np.int64))
    s, r = [new_source.permutation(new_source.letters[t]) for t in (0, 1)]
    assert np.array_equal(s[s], np.arange(len(s)))
    assert np.array_equal(r[r[r]], np.arange(len(r)))
    out = {'status': 'PASS_INTEGRAL_WAJNRYB_HOMOLOGY_AND_EXACT_OLD_SOURCE_FACTORIZATION',
           'integral_presentation_checks': checks,
           'alternating_form': np.array(J, dtype=int).tolist(),
           'column_chain_matrices': [np.array(x, dtype=int).tolist() for x in a],
           'column_d_matrix': np.array(d, dtype=int).tolist(),
           'P0': np.array(P0, dtype=int).tolist(), 'P1': np.array(P1, dtype=int).tolist(),
           'P0_determinant': int(P0.det()), 'P1_determinant': int(P1.det()),
           'five_exact_block_maps': rows,
           'old_right_permutation_generators_and_pairs_compared': 10,
           'all_six_coset_transition_comparisons': finite_checks,
           'finite_prime': 3, 'finite_full_vector_degree': H.degree,
           'finite_induced_source_degree': len(s),
           'factorization_scope': 'Every integer modulus: the five new evaluation kernels equal the intersection of the three old NS evaluation kernels; this remains exact after B/F induction.',
           'fprime_values': 'The two appended scalar blocks are identity on every f in the closed commutator subgroup.',
           'no_new_homology_source_coordinate': True,
           'input_sha256': hashes, 'seconds': round(time.time()-start, 6)}
    (HERE/(STEM+'.json')).write_text(json.dumps(out, indent=2)+'\n')
    np.savez_compressed(HERE/(STEM+'.npz'), s=s, r=r,
                        sigma=H.sigma, x=H.x, y=H.y,
                        P0=np.array(P0, dtype=np.int64), P1=np.array(P1, dtype=np.int64),
                        reconstructed_source_letter_coordinates=np.array(reconstructed))
    assert all(sha256((HERE/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(out, indent=2), flush=True)


if __name__ == '__main__':
    main()

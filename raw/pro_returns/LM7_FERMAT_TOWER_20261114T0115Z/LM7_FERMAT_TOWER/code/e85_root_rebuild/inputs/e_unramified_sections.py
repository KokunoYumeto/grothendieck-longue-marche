#!/usr/bin/env python3
"""E.41: integral graded coordinates for every unramified section.

The proof evaluates the entire section space as a product of finite-rank
lattice cokernels.  This program constructs their exact integer matrices
in Hall, Chen, and retained-Hall bases, without a rational exponential.
The default degree-four run verifies all three first differing layers.
All sparse arithmetic uses Python integers, so there is no overflow.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import argparse
import json


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    ans, d = 1, 2
    while d * d <= n:
        if n % d == 0:
            n //= d
            ans = -ans
            if n % d == 0:
                return 0
            while n % d == 0:
                n //= d
        d += 1
    return -ans if n > 1 else ans


def vp3(n):
    ans = 0
    while n % 3 == 0:
        n //= 3
        ans += 1
    return ans


def witt_rank(n, r):
    numerator = sum(mobius(d) * n ** (r // d) for d in divisors(r))
    assert numerator % r == 0
    return numerator // r


def witt_trace(plus, minus, r):
    numerator = sum(mobius(d) *
                    (plus + (-1) ** d * minus) ** (r // d)
                    for d in divisors(r))
    assert numerator % r == 0
    return numerator // r


def sym_trace(r):
    # [t^r](1-t)^(-4)(1+t)^(-6).
    return sum(comb(3 + a, a) * (-1) ** (r - a) *
               comb(5 + r - a, r - a) for a in range(r + 1))


def layer_data(kind, r):
    if r == 1:
        rank, trace = 10, -2
    elif kind == 'full':
        rank, trace = witt_rank(10, r), witt_trace(4, 6, r)
    elif kind == 'metabelian':
        rank = (r - 1) * comb(r + 8, r)
        trace = -2 * sym_trace(r - 1) - sym_trace(r)
    elif kind == 'marked':
        diagonal = 9 ** (r // 2 - 1) if r % 2 == 0 else 0
        rank = (witt_rank(9, r) + 9 ** (r - 1) +
                ((r - 1) * 9 ** (r - 2) - diagonal) // 2)
        trace = (witt_trace(4, 5, r) + (-1) ** r +
                 ((r - 1) * (-1) ** r - diagonal) // 2)
    else:
        raise ValueError(kind)
    assert (rank - trace) % 2 == 0
    b = max(1 + vp3(j) for j in range(r, 2 * r + 1))
    return {'degree': r, 'rank': rank, 'c_trace': trace,
            'c_plus': (rank + trace) // 2,
            'coordinate_free_rank': (rank - trace) // 2,
            'torsion_bound_exponent': r + b,
            'sufficient_Smith_modulus': 3 ** (r + b + 1)}


def add_scaled(out, vector, scalar):
    for i, a in vector.items():
        out[i] = out.get(i, 0) + scalar * a
        if out[i] == 0:
            del out[i]


def negate(v):
    return {i: -a for i, a in v.items()}


class Hall:
    def __init__(self, degree):
        self.degree = [1] * 10
        self.children = [None] * 10
        self.letters = [tuple(int(i == j) for j in range(10))
                        for i in range(10)]
        self.pair = {}
        for r in range(2, degree + 1):
            old = len(self.degree)
            for i in range(old):
                for j in range(i):
                    if self.degree[i] + self.degree[j] != r:
                        continue
                    if self.children[i] is not None and self.children[i][1] > j:
                        continue
                    self.pair[i, j] = len(self.degree)
                    self.degree.append(r)
                    self.children.append((i, j))
                    self.letters.append(tuple(a + b for a, b in
                                              zip(self.letters[i], self.letters[j])))

    @lru_cache(None)
    def bracket(self, i, j):
        if i == j:
            return {}
        if i < j:
            return negate(self.bracket(j, i))
        if (i, j) in self.pair:
            return {self.pair[i, j]: 1}
        a, b = self.children[i]
        assert b > j
        # [[a,b],j]=[a,[b,j]]-[b,[a,j]].
        ans = {}
        for k, s in self.bracket(b, j).items():
            add_scaled(ans, self.bracket(a, k), s)
        for k, s in self.bracket(a, j).items():
            add_scaled(ans, self.bracket(b, k), -s)
        return ans

    def action(self, base, r, marked=False):
        selected = [i for i, d in enumerate(self.degree) if d == r and
                    (not marked or self.letters[i][5] <= 2)]
        rows = {i: j for j, i in enumerate(selected)}

        @lru_cache(None)
        def image(i):
            if i < 10:
                return base[i]
            a, b = self.children[i]
            ans = {}
            for u, x in image(a).items():
                for v, y in image(b).items():
                    add_scaled(ans, self.bracket(u, v), x * y)
            return ans

        return [{rows[i]: a for i, a in image(j).items() if i in rows}
                for j in selected], selected


class Chen:
    def __init__(self, degree):
        self.words = [(i,) for i in range(10)]
        for r in range(2, degree + 1):
            for i in range(10):
                for j in range(i):
                    for tail in combinations_with_replacement(range(j, 10), r - 2):
                        self.words.append((i, j) + tail)
        self.index = {word: i for i, word in enumerate(self.words)}

    @lru_cache(None)
    def bracket(self, i, j):
        a, b = self.words[i], self.words[j]
        if len(a) > 1 and len(b) > 1:
            return {}
        if len(b) > 1:
            return negate(self.bracket(j, i))
        k = b[0]
        if len(a) == 1:
            h = a[0]
            if h == k:
                return {}
            return {self.index[max(h, k), min(h, k)]: 1 if h > k else -1}
        h, l, *tail = a
        if k >= l:
            word = (h, l) + tuple(sorted(tail + [k]))
            return {self.index[word]: 1}
        w1 = (h, k) + tuple(sorted(tail + [l]))
        w2 = (l, k) + tuple(sorted(tail + [h]))
        return {self.index[w1]: 1, self.index[w2]: -1}

    def action(self, base, r):
        selected = [i for i, w in enumerate(self.words) if len(w) == r]
        rows = {i: j for j, i in enumerate(selected)}

        @lru_cache(None)
        def image_word(word):
            if len(word) == 1:
                return base[word[0]]
            ans = {}
            for a, x in image_word(word[:-1]).items():
                for b, y in base[word[-1]].items():
                    add_scaled(ans, self.bracket(a, b), x * y)
            return ans

        return [{rows[i]: a for i, a in image_word(self.words[j]).items()}
                for j in selected], selected


def identity(n, scalar=1):
    return [{i: scalar} for i in range(n)]


def plus(A, B, scalar=1):
    ans = [dict(c) for c in A]
    for c, b in zip(ans, B):
        add_scaled(c, b, scalar)
    return ans


def compose(A, B):
    ans = []
    for column in B:
        out = {}
        for k, b in column.items():
            add_scaled(out, A[k], b)
        ans.append(out)
    return ans


def dense_to_columns(A):
    return [{i: A[i][j] for i in range(len(A)) if A[i][j]}
            for j in range(len(A[0]))]


def trace(A):
    return sum(column.get(j, 0) for j, column in enumerate(A))


def coo(A):
    return [[i, j, a] for j, column in enumerate(A)
            for i, a in sorted(column.items())]


def arithmetic_inputs():
    cusps = [(1, 0), (2, 2), (0, 1), (2, 0), (1, 1), (0, 2), (2, 1), (1, 2)]
    U = [(v, -u) for u, v in cusps]
    CE = [[1, -1], [0, -1]]
    CT = [[0] * 8 for _ in range(8)]
    for j, i in enumerate([0, 2, 1, 3, 5, 4, 7, 6]):
        CT[i][j] = -1

    def vmat(E, T):
        A = [[0] * 10 for _ in range(10)]
        for i in range(2):
            A[i][:2] = E[i]
        for i in range(8):
            A[2 + i][2:] = T[i]
            for j in range(2):
                numerator = (sum(U[i][k] * E[k][j] for k in range(2)) -
                             sum(T[i][k] * U[k][j] for k in range(8)))
                assert numerator % 3 == 0
                A[2 + i][j] = numerator // 3
        return dense_to_columns(A)

    def diagonal(values):
        return [{i: value} for i, value in enumerate(values)]

    At = vmat([[1, -3], [3, -2]],
              [[7 * int(i == j) for j in range(8)] for i in range(8)])
    Ac = vmat(CE, CT)
    F2 = vmat([[-2, 0], [0, -2]],
              [[4 * int(i == j) for j in range(8)] for i in range(8)])
    B = diagonal([3, 3] + [1] * 8)
    C = diagonal([1, 1] + [3] * 8)
    for i, (a, b) in enumerate(U):
        if a:
            B[0][i + 2] = a
            C[0][i + 2] = -a
        if b:
            B[1][i + 2] = b
            C[1][i + 2] = -b
    assert compose(B, C) == identity(10, 3)
    assert compose(Ac, Ac) == identity(10)
    return {'tau': At, 'c': Ac, 'Frob_K2': F2,
            'B': B, 'C': C, 'split_Frob_K2': diagonal([-2, -2] + [4] * 8)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degree', type=int, default=4)
    parser.add_argument('--ranks-through', type=int, default=10)
    args = parser.parse_args()
    assert args.degree >= 1
    r = args.degree
    kinds = ['full', 'marked', 'metabelian']
    tables = {kind: [layer_data(kind, i) for i in range(1, args.ranks_through + 1)]
              for kind in kinds}
    for kind in kinds:
        print(kind, 'degree/rank/c-trace/free-rank:')
        for row in tables[kind]:
            print(row['degree'], row['rank'], row['c_trace'], row['coordinate_free_rank'])
    inputs = arithmetic_inputs()
    hall, chen = Hall(r), Chen(r)
    output = {'rank_tables': tables, 'computed_degree': r,
              'base_input_coo': {key: coo(value) for key, value in inputs.items()},
              'layers': {}}
    for kind in kinds:
        print('Constructing exact degree', r, kind, 'matrices.', flush=True)
        action = (lambda a: chen.action(a, r)) if kind == 'metabelian' else \
                 (lambda a: hall.action(a, r, marked=kind == 'marked'))
        matrices = {key: action(value)[0] for key, value in inputs.items()}
        basis = action(identity(10))[1]
        n = len(basis)
        assert n == layer_data(kind, r)['rank']
        assert compose(matrices['c'], matrices['c']) == identity(n)
        assert trace(matrices['c']) == layer_data(kind, r)['c_trace']
        assert compose(matrices['B'], matrices['C']) == identity(n, 3 ** r)
        assert compose(matrices['Frob_K2'], matrices['B']) == \
               compose(matrices['B'], matrices['split_Frob_K2'])
        split = matrices['split_Frob_K2']
        assert all(set(column) == {j} for j, column in enumerate(split))
        eigenvalues = sorted({column[j] for j, column in enumerate(split)})
        b = max(1 + vp3(j) for j in range(r, 2 * r + 1))
        assert max(vp3(abs(eigenvalue - 1)) for eigenvalue in eigenvalues) <= b
        cocycle = compose(plus(matrices['tau'], identity(n), -1),
                          plus(identity(n), matrices['c']))
        if kind == 'metabelian':
            words = [chen.words[i] for i in basis]
        else:
            words = [{'Hall_index': i, 'letters': hall.letters[i],
                      'children': hall.children[i]} for i in basis]
        output['layers'][kind] = {
            **layer_data(kind, r), 'basis': words,
            'matrices_coo': {key: coo(value) for key, value in matrices.items()},
            'cocycle_matrix_coo': coo(cocycle),
            'split_Frobenius_eigenvalues': eigenvalues,
            'verified': ['C_squared_identity', 'exact_conjugation_trace',
                         'B_times_C_equals_3_power_degree',
                         'Frobenius_split_conjugacy', 'torsion_exponent_bound']}
        print('Verified', kind, ': rank', n, ', trace', trace(matrices['c']),
              ', free rank', layer_data(kind, r)['coordinate_free_rank'],
              ', torsion killed by 3^', r + b, sep='', flush=True)
    # Independent combinatorial counts in a conjugation eigenbasis.
    # The marked letter is one of the six minus letters.
    h = Hall(min(args.degree, 4))
    for d in range(1, min(args.degree, 4) + 1):
        selected = [i for i, weight in enumerate(h.degree) if weight == d]
        for kind in ['full', 'marked']:
            retained = [i for i in selected if kind == 'full' or h.letters[i][5] <= 2]
            tr = sum((-1) ** sum(h.letters[i][4:]) for i in retained)
            assert len(retained) == layer_data(kind, d)['rank']
            assert tr == layer_data(kind, d)['c_trace']
        words = [w for w in chen.words if len(w) == d]
        assert len(words) == layer_data('metabelian', d)['rank']
        assert sum((-1) ** sum(i >= 4 for i in w) for w in words) == \
               layer_data('metabelian', d)['c_trace']
    output['status'] = 'PASS'
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, separators=(',', ':')) + '\n')
    print('PASS: exact Hall/Chen/marked matrices, traces, split-lattice certificates and rank formulas.')


if __name__ == '__main__':
    main()

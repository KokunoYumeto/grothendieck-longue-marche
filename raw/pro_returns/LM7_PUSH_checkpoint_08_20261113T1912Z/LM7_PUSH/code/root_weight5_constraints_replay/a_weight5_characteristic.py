#!/usr/bin/env python3
"""Characteristic finite Magnus targets and exact weight-five special maps.

No full profinite lift is inferred.  The finite target is the actual
two-generator Magnus image; its fully invariant kernel is proved by the
displayed Fox substitution map.  Arithmetic uses only integer polynomials.
"""

from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


class Magnus:
    def __init__(self, n):
        self.n, self.mod = n, 5**n
        self.one = {(0, 0): 1}
        self.X, self.Y = {(1, 0): 1}, {(0, 1): 1}
        self.a, self.b = self.add(self.one, self.X), self.add(self.one, self.Y)
        self.id = (self.one, {}, {})
        self.x, self.y = (self.a, self.one, {}), (self.b, {}, self.one)
        self.c = self.comm(self.x, self.y)
        assert self.c == self.module(self.one)

    def add(self, p, q, scalar=1, degree=6):
        out = dict(p)
        for mon, value in q.items():
            out[mon] = (out.get(mon, 0)+scalar*value) % self.mod
        return {mon: value % self.mod for mon, value in out.items()
                if value % self.mod and sum(mon) <= degree}

    def mul(self, p, q, degree=6):
        out = {}
        for (i, j), a in p.items():
            for (k, l), b in q.items():
                mon = i+k, j+l
                if sum(mon) <= degree:
                    out[mon] = (out.get(mon, 0)+a*b) % self.mod
        return {mon: value for mon, value in out.items() if value}

    def pow(self, p, exponent, degree=6):
        out = self.one
        while exponent:
            if exponent & 1:
                out = self.mul(out, p, degree)
            p = self.mul(p, p, degree)
            exponent >>= 1
        return out

    def unit_inv(self, a):
        tail = self.add(self.one, a, -1)
        out, term = self.one, self.one
        for _ in range(6):
            term = self.mul(term, tail)
            out = self.add(out, term)
        assert self.mul(a, out) == self.one
        return out

    def gm(self, g, h):
        a, u, v = g
        b, w, z = h
        return (self.mul(a, b), self.add(u, self.mul(a, w, 5), degree=5),
                self.add(v, self.mul(a, z, 5), degree=5))

    def gi(self, g):
        a, u, v = g
        ai = self.unit_inv(a)
        return ai, self.mul(ai, self.add({}, u, -1), 5), self.mul(ai, self.add({}, v, -1), 5)

    def gp(self, g, exponent):
        if exponent < 0:
            return self.gp(self.gi(g), -exponent)
        out = self.id
        while exponent:
            if exponent & 1:
                out = self.gm(out, g)
            g = self.gm(g, g)
            exponent >>= 1
        return out

    def conj(self, g, h):
        return self.gm(self.gm(g, h), self.gi(g))

    def comm(self, g, h):
        return self.gm(self.conj(g, h), self.gi(h))

    def module(self, p):
        return self.one, self.mul(self.add({}, self.Y, -1), p, 5), self.mul(self.X, p, 5)

    def module_coefficient(self, g):
        assert g[0] == self.one
        assert all(i >= 1 for i, j in g[2])
        p = {(i-1, j): value for (i, j), value in g[2].items()}
        assert self.module(p) == g
        return p

    def substitute(self, p, A, B, degree=6):
        out = {}
        for (i, j), value in p.items():
            term = self.mul(self.pow(A, i, degree), self.pow(B, j, degree), degree)
            out = self.add(out, term, value, degree)
        return out

    def source_map(self, gx, gy):
        A, B = self.add(gx[0], self.one, -1), self.add(gy[0], self.one, -1)
        def morphism(g):
            a, u, v = g
            su, sv = self.substitute(u, A, B, 5), self.substitute(v, A, B, 5)
            return (self.substitute(a, A, B),
                    self.add(self.mul(su, gx[1], 5), self.mul(sv, gy[1], 5), degree=5),
                    self.add(self.mul(su, gx[2], 5), self.mul(sv, gy[2], 5), degree=5))
        assert morphism(self.x) == gx and morphism(self.y) == gy
        return morphism

    def beta(self, Q):
        p = self.mul(self.add(self.X, self.Y), Q)
        h = self.mul(self.Y, Q)
        delta = self.mul(self.add({}, self.Y, -1), p)
        def morphism(g):
            s = g[0].get((0, 1), 0)
            return self.gm(g, self.module({mon: s*value % self.mod for mon, value in delta.items()
                                           if s*value % self.mod}))
        return morphism, self.module(p), self.module(h), delta

    def serialize(self, p):
        return [[i, j, value] for (i, j), value in sorted(p.items())]


def main():
    outputs = []
    for n in (1, 2):
        A = Magnus(n)
        q = A.mod
        N = 5**(n+1)
        assert A.gp(A.x, N) == A.gp(A.y, N) == A.id
        assert A.gp(A.x, N//5) != A.id and A.gp(A.y, N//5) != A.id
        diag = {tuple(sorted(A.mul(A.pow(A.a, r), A.pow(A.b, s)).items()))
                for r in range(N) for s in range(N)}
        assert len(diag) == N*N
        basis = [(i, j) for total in range(5) for i in range(total+1) for j in [total-i]]
        assert len(basis) == 15
        monomial_records = []
        for i, j in basis:
            g = A.c
            for _ in range(i):
                g = A.comm(A.x, g)
            for _ in range(j):
                g = A.comm(A.y, g)
            assert g == A.module({(i, j): 1})
            monomial_records.append({'monomial': [i, j], 'module_vector': [A.serialize(g[1]), A.serialize(g[2])]})
        z = A.gi(A.gm(A.x, A.y))
        Qbasis = [{(2, 0): 1}, {(1, 1): 1}, {(0, 2): 1}]
        beta_records = []
        for Q in Qbasis:
            beta, f, h, delta = A.beta(Q)
            assert beta(A.x) == A.x
            assert beta(A.y) == A.conj(f, A.y)
            assert beta(z) == A.conj(h, z)
            assert beta(A.c) == A.c
            assert A.gp(A.module(delta), q) == A.id
            assert A.gp(A.module(delta), q//5) != A.id
            # Exact agreement of the central formula and its actual Fox
            # source substitution on a generating normal-form sample.
            fox = A.source_map(A.x, A.conj(f, A.y))
            samples = [A.gm(A.gm(A.gp(A.x, r), A.gp(A.y, s)), A.module({mon: 1}))
                       for r, s, mon in [(0, 1, (0, 0)), (5, 3, (2, 1)), (N-1, N-2, (4, 0)), (2, 7, (0, 4))]]
            assert all(beta(g) == fox(g) for g in samples)
            assert all(beta(A.gm(g, k)) == A.gm(beta(g), beta(k)) for g in samples for k in samples)
            beta_records.append({'Q': A.serialize(Q), 'f_coefficient': A.serialize(A.module_coefficient(f)),
                                 'h_coefficient': A.serialize(A.module_coefficient(h)),
                                 'central_y_change': A.serialize(delta)})
        if n == 1:
            changes = set()
            for a, b, c in product(range(5), repeat=3):
                Q = {mon: value for mon, value in zip(((2, 0), (1, 1), (0, 2)), (a, b, c)) if value}
                beta, f, h, delta = A.beta(Q)
                changes.add(tuple(sorted(delta.items())))
                assert beta(A.y) == A.conj(f, A.y) and beta(z) == A.conj(h, z)
            assert len(changes) == 125

        # Actual finite centralizer restrictions on the diagonal exponent.
        sums = []
        value = {}
        for s in range(N):
            sums.append(A.add({}, value, degree=4))
            value = A.add(value, A.pow(A.b, s))
        assert [s for s, p in enumerate(sums) if not p] == [0]
        short_zero = [s for s, p in enumerate(sums) if not A.add({}, p, degree=3)]
        assert short_zero == list(range(0, N, q))
        assert all(sums[q*t] == ({(0, 4): (5**(n-1))*t} if t else {}) for t in range(5))

        # Exact geometric S3 actions, retaining the inner normalization.
        swap = A.source_map(A.y, A.x)
        cycle = A.source_map(A.y, z)
        cycle_inv = lambda g: cycle(cycle(g))
        assert all(swap(swap(g)) == g and cycle(cycle(cycle(g))) == g for g in (A.x, A.y))
        symmetry_records = []
        for label, s, si, linX, linY in (
                ('swap', swap, swap, A.Y, A.X),
                ('cycle', cycle, cycle_inv, A.Y, A.add({}, A.add(A.X, A.Y), -1))):
            for Q in Qbasis:
                beta, f, h, delta = A.beta(Q)
                transformed = lambda g: s(beta(si(g)))
                dx = A.module_coefficient(A.gm(transformed(A.x), A.gi(A.x)))
                assert all(i >= 1 for i, j in dx)
                inner_polynomial = {(i-1, j): coefficient for (i, j), coefficient in dx.items()}
                correction = A.module(inner_polynomial)
                normalized = lambda g: A.conj(correction, transformed(g))
                new_Q = A.substitute(Q, linX, linY)
                expected = A.beta(new_Q)[0]
                assert normalized(A.x) == expected(A.x) and normalized(A.y) == expected(A.y)
                symmetry_records.append({'symmetry': label, 'Q': A.serialize(Q),
                                         'actual_inner_correction': A.serialize(inner_polynomial),
                                         'new_Q': A.serialize(new_Q)})
        outputs.append({'n': n, 'coefficient_modulus': q, 'diagonal_generator_order': N,
                        'diagonal_order': len(diag), 'derived_rank': 15,
                        'actual_group_order': 5**(17*n+2),
                        'module_monomial_words': monomial_records,
                        'special_basis_maps': beta_records,
                        'centralizer_diagonal_exponents': {'y_exponent': [0],
                                                          'depth5_x_exponents': short_zero},
                        'geometric_symmetry_with_inner_corrections': symmetry_records})
        print('PASS n=', n, 'group order=', 5**(17*n+2), 'diagonal order=', len(diag),
              'derived module rank15; three exact special maps and actual S3 inner corrections', flush=True)
    payload = {'status': 'PASS_CHARACTERISTIC_WEIGHT_FIVE_MAGNUS_TARGETS',
               'ring': '(Z/5^n)[X,Y]/(X,Y)^7',
               'module': '((Z/5^n)[X,Y]/(X,Y)^6)^2',
               'multiplication': '(a,u)(b,v)=(ab,u+a v)',
               'source': 'x=(1+X,(1,0)); y=(1+Y,(0,1))',
               'target_order_formula': '5^(17n+2)',
               'central_special_parameter': 'Q=A X^2+B X Y+C Y^2',
               'f_coefficient': '(X+Y)Q', 'h_coefficient': 'YQ',
               'central_y_change': '-Y(X+Y)Q',
               'executed_precisions': outputs,
               'scope': 'Actual characteristic finite five-group targets and their special outer maps. No full profinite source lift or obstruction is claimed.'}
    HERE.joinpath('a_weight5_characteristic.json').write_text(json.dumps(payload, indent=2)+'\n')
    print(payload['status'])


if __name__ == '__main__':
    main()

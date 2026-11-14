#!/usr/bin/env python3
"""Exact finite local norm characters for the pure-seventeen tower."""
from math import comb
from pathlib import Path
import json
from sympy import Matrix, eye
from sympy.matrices.normalforms import hermite_normal_form


def nullspace3(rows, n):
    a = [[int(x) % 3 for x in row] for row in rows]
    pivots = []
    k = 0
    for j in range(n):
        r = next((r for r in range(k, len(a)) if a[r][j]), None)
        if r is None:
            continue
        a[k], a[r] = a[r], a[k]
        inv = pow(a[k][j], -1, 3)
        a[k] = [x * inv % 3 for x in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                q = a[i][j]
                a[i] = [(x - q * y) % 3 for x, y in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
    free = [i for i in range(n) if i not in pivots]
    out = []
    for j in free:
        v = [0] * n
        v[j] = 1
        for i, p in enumerate(pivots):
            v[p] = -a[i][j] % 3
        out.append(v)
    return out


class DVR:
    def __init__(self, d):
        self.d = d
        self.m = 3 ** (d - 1)
        self.e = 2 * self.m
        self.n = 2 * self.e + 1
        self.rho = 23  # the unique Q3 cube root of17, modulo27
        m, e, rho = self.m, self.e, self.rho
        self.q = [(comb(e, j) * (-1) ** (e - j)
                   + (rho * comb(m, j) * (-1) ** (m - j) if j <= m else 0)
                   + (rho * rho if j == 0 else 0)) % 27
                  for j in range(e + 1)]
        assert self.q[-1] == 1 and self.q[0] % 9 == 3
        assert all(x % 3 == 0 for x in self.q[:-1])
        self.zero = (0,) * e
        self.one = (1,) + (0,) * (e - 1)
        self.x = (0, 1) + (0,) * (e - 2)
        self.hs = {}
        power = list(self.one)
        for k in range(self.n + 1):
            cols = []
            for j in range(e):
                cols.append(Matrix(self.polyred([0] * j + power)))
            h = hermite_normal_form(Matrix.hstack(*cols, 27 * eye(e)))
            assert h.shape == (e, e)
            assert abs(int(h.det())) == 3 ** k
            self.hs[k] = [[int(h[i, j]) for j in range(e)] for i in range(e)]
            power = self.polyred([0] + power)
        self.powers = [self.one]
        for i in range(self.n):
            self.powers.append(self.mul(self.powers[-1], self.x))
        assert self.powers[-1] == self.zero
        self.gens = [self.add(self.one, self.powers[i]) for i in range(1, self.n)]
        self.inverses = [self.power(g, 2 * 3 ** (self.n - 1) - 1) for g in self.gens]
        assert all(self.mul(g, inv) == self.one for g, inv in zip(self.gens, self.inverses))

    def polyred(self, a):
        a = list(a) + [0] * max(0, self.e - len(a))
        for i in range(len(a) - 1, self.e - 1, -1):
            q = a[i] % 27
            for j in range(self.e):
                a[i - self.e + j] -= q * self.q[j]
        return [x % 27 for x in a[:self.e]]

    def canonical(self, a, k=None):
        if k is None:
            k = self.n
        a = self.polyred(a)
        h = self.hs[k]
        for i in range(self.e - 1, -1, -1):
            q = a[i] // h[i][i]
            for j in range(i + 1):
                a[j] -= q * h[j][i]
        return tuple(a)

    def add(self, a, b):
        return self.canonical([x + y for x, y in zip(a, b)])

    def scale(self, a, c):
        return self.canonical([x * c for x in a])

    def mul(self, a, b):
        q = [0] * (2 * self.e - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        q[i + j] += x * y
        return self.canonical(q)

    def power(self, a, n):
        r = self.one
        while n:
            if n & 1:
                r = self.mul(r, a)
            a = self.mul(a, a)
            n >>= 1
        return r

    def coords(self, a):
        residue = self.canonical(a, 1)[0]
        assert residue in (1, 2)
        if residue == 2:
            a = self.scale(a, -1)
        out = []
        for i in range(1, self.n):
            candidates = [c for c in range(3)
                          if self.canonical(a, i + 1)
                          == self.canonical(self.add(self.one, self.scale(self.powers[i], c)), i + 1)]
            assert len(candidates) == 1
            c = candidates[0]
            out.append(c)
            a = self.mul(a, self.power(self.inverses[i - 1], c))
        assert a == self.one
        return out

    def smul(self, a, b):
        q = [self.zero] * 5
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                q[i + j] = self.add(q[i + j], self.mul(x, y))
        # T^3 = pi -3T +3T^2.
        for k in (4, 3):
            v = q[k]
            q[k - 3] = self.add(q[k - 3], self.mul(v, self.x))
            q[k - 2] = self.add(q[k - 2], self.scale(v, -3))
            q[k - 1] = self.add(q[k - 1], self.scale(v, 3))
        return q[:3]

    def snorm(self, a):
        basis = [[self.one, self.zero, self.zero],
                 [self.zero, self.one, self.zero],
                 [self.zero, self.zero, self.one]]
        cols = [self.smul(a, b) for b in basis]
        out = self.zero
        for perm, sign in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                           ((2, 1, 0), -1), ((1, 0, 2), -1), ((0, 2, 1), -1)]:
            term = self.one
            for j, i in enumerate(perm):
                term = self.mul(term, cols[j][i])
            out = self.add(out, self.scale(term, sign))
        return out


def run():
    records = []
    for d in (1, 2, 3):
        r = DVR(d)
        cubes = [r.coords(r.power(g, 3)) for g in r.gens]
        chars_before = nullspace3(cubes, r.n - 1)
        assert len(chars_before) == r.e + 1
        t = [r.zero, r.one, r.zero]
        tp = [r.one, r.zero, r.zero]
        norms, normcoords = [], []
        for i in range(1, 3 * r.n):
            tp = r.smul(tp, t)
            u = [r.add(r.one, tp[0]), tp[1], tp[2]]
            nu = r.snorm(u)
            norms.append(nu)
            normcoords.append(r.coords(nu))
        assert r.smul(tp, t) == [r.zero] * 3
        assert r.snorm(t) == r.canonical(r.x)
        weights = nullspace3(cubes + normcoords, r.n - 1)
        assert len(weights) == 1
        weight = weights[0]
        first = next(c for c in weight if c)
        weight = [c * pow(first, -1, 3) % 3 for c in weight]
        def char(a):
            return sum(c * w for c, w in zip(r.coords(a), weight)) % 3
        assert all(char(nu) == 0 for nu in norms)
        # Distinct mixed units test character additivity through the real ring law.
        units = []
        for i in range(1, r.n):
            units.append(r.mul(r.gens[i - 1], r.gens[(2 * i) % (r.n - 1)]))
        for a in units:
            for b in units:
                assert char(r.mul(a, b)) == (char(a) + char(b)) % 3
        rec = {
            "d": d, "e": r.e, "truncation": r.n, "rho_mod27": r.rho,
            "eisenstein_polynomial_mod27": r.q,
            "hnf": r.hs[r.n], "unit_cube_relations": cubes,
            "norm_unit_coordinates": normcoords, "norm_character_weights": weight,
            "unit_cube_character_dimension": len(chars_before),
            "norm_cokernel_dimension": len(weights),
            "additivity_checks": len(units) ** 2,
        }
        records.append(rec)
        print(json.dumps({k: rec[k] for k in ("d", "e", "truncation", "norm_character_weights", "additivity_checks")}), flush=True)

    out = {"status": "PASS", "records": records}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2) + "\n")
    print("PASS")


if __name__ == "__main__":
    run()

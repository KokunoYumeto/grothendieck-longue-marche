#!/usr/bin/env python3
"""Independent finite checks of the complete abelian peripheral count.

Finite groups are constructed as permutations or explicit products.  We
enumerate actual allowed triples, their generated subgroups, and every
complement.  These results are compared with the relative coinvariant /
base-centralizer formula, computed directly from group operations.
No cohomology package, group database, or numerical linear algebra is used.
"""

from collections import deque
from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm
from pathlib import Path
import json


class Group:
    def __init__(self, name, elements, multiplication, identity):
        self.name = name
        self.elements = list(elements)
        self.size = len(self.elements)
        self.index = {a: i for i, a in enumerate(self.elements)}
        self.one = self.index[identity]
        self.mul = [[self.index[multiplication(a, b)] for b in self.elements]
                    for a in self.elements]
        self.inv = [next(b for b in range(self.size)
                         if self.mul[a][b] == self.one)
                    for a in range(self.size)]
        self.orders = [self.order(a) for a in range(self.size)]
        self.exponent = lcm(*self.orders)

    def order(self, a):
        b = self.one
        for k in range(1, self.size + 1):
            b = self.mul[b][a]
            if b == self.one:
                return k
        raise AssertionError('finite order')

    def power(self, a, k):
        b = self.one
        for _ in range(k % self.orders[a]):
            b = self.mul[b][a]
        return b

    def conjugate(self, h, a):
        return self.mul[self.mul[h][a]][self.inv[h]]

    def commutator(self, a, b):
        return self.mul[self.conjugate(a, b)][self.inv[b]]

    def generated(self, gens):
        seen = {self.one}
        queue = deque([self.one])
        while queue:
            a = queue.popleft()
            for g in gens:
                b = self.mul[a][g]
                if b not in seen:
                    seen.add(b)
                    queue.append(b)
        return frozenset(seen)

    def conjugacy_class(self, a):
        return {self.conjugate(h, a) for h in range(self.size)}

    def centralizer(self, a):
        return {h for h in range(self.size)
                if self.mul[h][a] == self.mul[a][h]}

    def quotient(self, normal, name):
        normal = frozenset(normal)
        assert all(self.conjugate(g, a) in normal
                   for g in range(self.size) for a in normal)
        cosets = []
        projection = {}
        for g in range(self.size):
            if g not in projection:
                c = frozenset(self.mul[g][a] for a in normal)
                idx = len(cosets)
                cosets.append(c)
                projection.update({a: idx for a in c})
        reps = [min(c) for c in cosets]
        q = Group(name, range(len(cosets)),
                  lambda a, b: projection[self.mul[reps[a]][reps[b]]],
                  projection[self.one])
        return q, projection, reps

    def automorphisms(self):
        others = [a for a in range(self.size) if a != self.one]
        for perm in permutations(others):
            alpha = {self.one: self.one, **dict(zip(others, perm))}
            if all(alpha[self.mul[a][b]] == self.mul[alpha[a]][alpha[b]]
                   for a in range(self.size) for b in range(self.size)):
                yield alpha


def perm_mul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def parity(a):
    return sum(a[i] > a[j] for i in range(len(a))
               for j in range(i + 1, len(a))) % 2


def make_examples():
    s3 = Group('S3', permutations(range(3)), perm_mul, tuple(range(3)))
    a = {i for i, p in enumerate(s3.elements) if parity(p) == 0}
    x = s3.index[(1, 0, 2)]
    y = s3.index[(0, 2, 1)]
    yield s3, a, x, y

    a4 = Group('A4', [p for p in permutations(range(4)) if parity(p) == 0],
               perm_mul, tuple(range(4)))
    a = {i for i in range(a4.size) if a4.orders[i] in (1, 2)}
    x, y = next((x, y) for x, y in product(range(a4.size), repeat=2)
                if a4.orders[x] == a4.orders[y] == 3
                and a4.orders[a4.mul[x][y]] == 3
                and len(a4.generated([x, y])) == a4.size)
    yield a4, a, x, y

    d8 = Group('D8', product(range(4), range(2)),
               lambda a, b: ((a[0] + (-1)**a[1]*b[0]) % 4,
                             (a[1] + b[1]) % 2), (0, 0))
    yield d8, {d8.index[(0, 0)], d8.index[(2, 0)]}, \
        d8.index[(1, 0)], d8.index[(0, 1)]

    for modulus in (6, 9):
        e = Group(f'C{modulus}', range(modulus),
                  lambda a, b, m=modulus: (a+b) % m, 0)
        a = {i for i in range(modulus) if i % (modulus // 3) == 0}
        yield e, a, e.index[1], e.index[0]

    e = Group('C3xC3', product(range(3), repeat=2),
              lambda a, b: ((a[0]+b[0]) % 3, (a[1]+b[1]) % 3), (0, 0))
    a = {i for i, v in enumerate(e.elements) if v[0] == 0}
    yield e, a, e.index[(1, 0)], e.index[(0, 1)]


def check(e, a, x, y):
    assert len(e.generated([x, y])) == e.size
    assert all(e.mul[u][v] == e.mul[v][u] for u in a for v in a)
    g, pi, reps = e.quotient(a, e.name + '/A')
    xs = [x, y, e.inv[e.mul[x][y]]]
    gs = [pi[u] for u in xs]
    ia = e.generated([e.commutator(h, u) for h in range(e.size) for u in a])
    assert ia <= a
    q, aq, _ = e.quotient(ia, e.name + '/[E,A]')
    abar = {aq[u] for u in a}
    centralizers = [g.centralizer(v) for v in gs]
    kappas = [
        {c: aq[e.commutator(reps[c], xs[i])] for c in centralizers[i]}
        for i in range(3)
    ]
    for i in range(3):
        assert all(kappas[i][g.mul[b][c]] == q.mul[kappas[i][b]][kappas[i][c]]
                   for b in centralizers[i] for c in centralizers[i])
        for c in centralizers[i]:
            assert all(aq[e.commutator(e.mul[u][reps[c]], xs[i])] == kappas[i][c]
                       for u in a)
    hspace = q.generated([v for k in kappas for v in k.values()])
    assert hspace <= abar

    subgroups = {e.generated([u, v]) for u, v in product(range(e.size), repeat=2)}
    complements = [c for c in subgroups if c & a == {e.one}
                   and {pi[u] for u in c} == set(range(g.size))]
    admissible = []
    for comp in complements:
        section = {pi[u]: u for u in comp}
        if all(section[gs[i]] in e.conjugacy_class(xs[i]) for i in range(3)):
            admissible.append(comp)
    rows = []
    for alpha in g.automorphisms():
        for lam in range(1, e.exponent + 1):
            if gcd(lam, e.exponent) != 1:
                continue
            powers = [e.power(u, lam) for u in xs]
            targets = [alpha[v] for v in gs]
            base_h = []
            for i in range(3):
                possible = [v for v in range(g.size)
                            if g.conjugate(v, g.power(gs[i], lam)) == targets[i]]
                if not possible:
                    break
                base_h.append(possible[0])
            if len(base_h) != 3:
                continue
            initial = [e.conjugate(reps[base_h[i]], powers[i]) for i in range(3)]
            r = e.mul[e.mul[initial[0]][initial[1]]][initial[2]]
            assert r in a
            obstruction_zero = aq[r] in hspace
            allowed = [{u for u in e.conjugacy_class(powers[i]) if pi[u] == targets[i]}
                       for i in range(3)]
            weak, good, bad = [], [], []
            for u, v in product(allowed[0], allowed[1]):
                w = e.inv[e.mul[u][v]]
                if w not in allowed[2]:
                    continue
                triple = [u, v, w]
                weak.append(triple)
                image = e.generated([u, v])
                (good if len(image) == e.size else bad).append(triple)
            numerator = len(a)**2 * len(abar)
            denominator = len(hspace)
            for i in range(3):
                numerator *= len(centralizers[i])
                denominator *= len(e.centralizer(xs[i]))
            formula = Fraction(numerator, denominator)
            assert formula.denominator == 1
            predicted = int(formula) if obstruction_zero else 0
            assert len(weak) == predicted
            assert len(bad) == len(admissible)
            assert bool(good) == obstruction_zero
            # Check the affine A^3 kernel, without the closed count formula.
            zero_lifts = 0
            for aa in product(a, repeat=3):
                vv = [e.conjugate(aa[i], initial[i]) for i in range(3)]
                rr = e.mul[e.mul[vv[0]][vv[1]]][vv[2]]
                if rr == r:
                    zero_lifts += 1
            assert zero_lifts == len(a)**2 * len(abar)
            rows.append({'alpha': [alpha[i] for i in range(g.size)], 'lambda': lam,
                         'obstruction_zero': obstruction_zero, 'weak': len(weak),
                         'generating': len(good), 'nongenerating': len(bad),
                         'formula': int(formula)})
    result = {'group': e.name, 'group_order': e.size, 'kernel_order': len(a),
              'quotient_order': g.size, 'coinvariant_order': len(abar),
              'centralizer_image_order': len(hspace),
              'source_triple': [e.elements[u] for u in xs],
              'complements': len(complements), 'admissible_complements': len(admissible),
              'cases': rows}
    print(e.name, 'A=', len(a), 'A_G=', len(abar), 'H=', len(hspace),
          'admissible_complements=', len(admissible), 'cases=', len(rows))
    print('  weak/generating/nongenerating:',
          sorted({(r['weak'], r['generating'], r['nongenerating']) for r in rows}))
    return result


def main():
    results = [check(*example) for example in make_examples()]
    output = {'status': 'PASS', 'commutator': '[a,b]=aba^-1b^-1',
              'total_cases': sum(len(r['cases']) for r in results), 'examples': results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
    print('PASS: exact relative obstruction, complete count, complements, generation')


if __name__ == '__main__':
    main()

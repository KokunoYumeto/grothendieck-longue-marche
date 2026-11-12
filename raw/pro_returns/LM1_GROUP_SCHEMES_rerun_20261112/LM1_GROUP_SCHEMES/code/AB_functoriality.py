#!/usr/bin/env python3
"""Exact functoriality and reconstruction computations for LM C3:570--572 and 691--696.

The numerical group in this computation is U(12), not the infinite group
Zhat*.  All defining powers and both signs factor through U(12) in these
examples.  Automorphisms are found from generator images by checking the
complete Cayley graph, without using an automorphism classification.
"""
from itertools import permutations, product
from collections import deque, Counter, defaultdict
from math import gcd, lcm
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


class FiniteGroup:
    def __init__(self, name, elements, one, mul, inv):
        self.name = name
        self.elements = sorted(elements)
        self.index = {a: i for i, a in enumerate(self.elements)}
        self.n = len(self.elements)
        self.one = self.index[one]
        self.m = [[self.index[mul(a, b)] for b in self.elements]
                  for a in self.elements]
        self.inv = [self.index[inv(a)] for a in self.elements]
        self.orders = [self.order(a) for a in range(self.n)]

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv[a], -n)
        b = self.one
        while n:
            if n & 1:
                b = self.m[b][a]
            a = self.m[a][a]
            n //= 2
        return b

    def order(self, a):
        b = self.one
        for n in range(1, self.n + 1):
            b = self.m[b][a]
            if b == self.one:
                return n
        raise AssertionError("finite order not found")

    def conj(self, a, b):
        return self.m[self.m[a][b]][self.inv[a]]

    def as_list(self, a):
        return list(self.elements[a])


def symmetric(n, rcycle, scycle):
    one = tuple(range(n))

    def mul(a, b):
        return tuple(a[b[i]] for i in range(n))

    def inv(a):
        b = [0] * n
        for i, j in enumerate(a):
            b[j] = i
        return tuple(b)

    def cycle(c):
        a = list(one)
        for i, j in zip(c, c[1:] + c[:1]):
            a[i - 1] = j - 1
        return tuple(a)

    C = FiniteGroup(f"S{n}", permutations(range(n)), one, mul, inv)
    return C, C.index[cycle(rcycle)], C.index[cycle(scycle)]


def matmul(a, b, n):
    x, y, z, w = a
    X, Y, Z, W = b
    return ((x*X+y*Z) % n, (x*Y+y*W) % n,
            (z*X+w*Z) % n, (z*Y+w*W) % n)


def sl2(n):
    elements = [a for a in product(range(n), repeat=4)
                if (a[0]*a[3]-a[1]*a[2]) % n == 1]
    C = FiniteGroup(f"SL2(Z/{n})", elements, (1, 0, 0, 1),
                    lambda a, b: matmul(a, b, n),
                    lambda a: (a[3], -a[1] % n, -a[2] % n, a[0]))
    return C, C.index[(0, 1, n-1, 1)], C.index[(0, n-1, 1, 0)]


def cayley_map(C, r, s, rp, sp):
    """Propagate a proposed homomorphism and test every right Cayley edge."""
    steps = (r, s, C.inv[r], C.inv[s])
    targets = (rp, sp, C.inv[rp], C.inv[sp])
    images = {C.one: C.one}
    todo = deque([C.one])
    while todo:
        a = todo.popleft()
        for g, h in zip(steps, targets):
            b, y = C.m[a][g], C.m[images[a]][h]
            if b in images:
                if images[b] != y:
                    return None
            else:
                images[b] = y
                todo.append(b)
    assert len(images) == C.n, "source generators do not generate"
    if len(set(images.values())) != C.n:
        return None
    return tuple(images[i] for i in range(C.n))


def automorphisms(C, r, s):
    result = set()
    for rp in range(C.n):
        if C.orders[rp] != C.orders[r]:
            continue
        for sp in range(C.n):
            if C.orders[sp] != C.orders[s]:
                continue
            a = cayley_map(C, r, s, rp, sp)
            if a is not None:
                result.add(a)
    autos = sorted(result)
    index = {a: i for i, a in enumerate(autos)}
    one = index[tuple(range(C.n))]
    mul = [[index[tuple(a[b[x]] for x in range(C.n))]
            for b in autos] for a in autos]
    inv = [next(j for j in range(len(autos)) if mul[i][j] == one)
           for i in range(len(autos))]
    return autos, index, one, mul, inv


def quotient_data(elements, one, mul, normal):
    """Canonical right cosets of an explicitly checked normal subgroup."""
    canon = {a: min(mul(a, k) for k in normal) for a in elements}
    reps = sorted(set(canon.values()))
    which = {a: i for i, a in enumerate(reps)}
    coset = {a: which[canon[a]] for a in elements}
    qmul = [[coset[mul(a, b)] for b in reps] for a in reps]
    return reps, coset, coset[one], qmul


class SignedModel:
    """Retain every element and map needed for exact finite functoriality."""
    def __init__(self, C, r, s, kind):
        self.C, self.r, self.s, self.kind = C, r, s, kind
        aa, ai, aone, am, av = automorphisms(C, r, s)
        self.autos, self.ai, self.aone = aa, ai, aone
        self.e0 = C.m[s][r]
        self.L = {C.power(self.e0, k) for k in range(C.orders[self.e0])}
        center = {c for c in range(C.n)
                  if all(C.conj(c, x) == x for x in range(C.n))}
        assert self.L & center == {C.one}
        self.inners = {c: ai[tuple(C.conj(c, x) for x in range(C.n))]
                       for c in range(C.n)}
        units = (1, 5, 7, 11)
        classes = {x: {C.conj(c, x) for c in range(C.n)}
                   for x in (r, s, C.inv[r], C.inv[s])}
        D = []
        for k, u in enumerate(aa):
            for mu in units:
                if u[self.e0] != C.power(self.e0, mu):
                    continue
                signs = ([(1 if mu % 3 == 1 else -1,
                           1 if mu % 4 == 1 else -1)]
                         if kind == 'B' else product((1, -1), repeat=2))
                for er, es in signs:
                    if u[r] in classes[C.power(r, er)] and u[s] in classes[C.power(s, es)]:
                        D.append((k, mu, er, es))
        self.D = sorted(D)
        self.di = {d: k for k, d in enumerate(self.D)}
        self.done = self.di[(aone, 1, 1, 1)]

        def dm(i, j):
            a, b = self.D[i], self.D[j]
            return self.di[(am[a[0]][b[0]], a[1]*b[1] % 12,
                            a[2]*b[2], a[3]*b[3])]
        self.dm = dm
        self.dv = [self.di[(av[a], pow(mu, -1, 12), er, es)]
                   for a, mu, er, es in self.D]
        self.j = {l: self.di[(self.inners[l], 1, 1, 1)] for l in self.L}
        self.greps, self.dg, self.gone, self.gm = quotient_data(
            list(range(len(D))), self.done, dm, set(self.j.values()))
        self.ngamma = len(self.greps)

        def sm(a, b):
            c, d = a
            cp, dp = b
            return C.m[c][aa[self.D[d][0]][cp]], dm(d, dp)
        self.sm = sm
        semi = list(product(range(C.n), range(len(D))))
        anti = {(C.inv[l], self.j[l]) for l in self.L}
        self.reps, self.sq, self.one, self.m = quotient_data(
            semi, (C.one, self.done), sm, anti)
        self.n = len(self.reps)
        self.inv = [self.sq[(aa[self.D[self.dv[d]][0]][C.inv[c]], self.dv[d])]
                    for c, d in self.reps]
        self.ce = [self.sq[(c, self.done)] for c in range(C.n)]
        self.de = [self.sq[(C.one, d)] for d in range(len(D))]
        self.delta = [self.dg[d] for c, d in self.reps]
        self.N = {}
        for x, name, coord in ((r, 'rho', 2), (s, 'sigma', 3)):
            self.N[name] = [g for g in range(self.n)
                            if self.conj(g, self.ce[x]) == self.ce[C.power(
                                x, self.D[self.greps[self.delta[g]]][coord])]]
        self.nr = {k: [g for g in self.N['rho'] if self.delta[g] == k]
                   for k in range(self.ngamma)}
        self.ns = {k: [g for g in self.N['sigma'] if self.delta[g] == k]
                   for k in range(self.ngamma)}
        self.gg = {k: [g for g in range(self.n) if self.delta[g] == k]
                   for k in range(self.ngamma)}
        self.dd = {k: [d for d in range(len(D)) if self.dg[d] == k]
                   for k in range(self.ngamma)}
        tau = cayley_map(C, r, s, C.conj(s, C.inv[r]), C.inv[s])
        self.td = self.di[(ai[tau], 11, -1, -1)]
        self.t = self.de[self.td]
        self.tp = self.m[self.ce[C.inv[s]]][self.t]

    def conj(self, a, b):
        return self.m[self.m[a][b]][self.inv[a]]

    def objects(self):
        klist = range(self.ngamma)
        return {
            'D': list(range(len(self.D))),
            'gamma': list(klist),
            'G': list(range(self.n)),
            'Nrho_star': self.N['rho'],
            'Nsigma_star': self.N['sigma'],
            'Gamma': [(a, b) for k in klist for a in self.nr[k] for b in self.ns[k]],
            'M': [(a, b, g) for k in klist for a in self.nr[k]
                  for b in self.ns[k] for g in self.gg[k]],
            'S0Gamma': [(d, a, b) for k in klist for d in self.dd[k]
                        for a in self.nr[k] for b in self.ns[k]],
            'S0M': [(d, a, b, g) for k in klist for d in self.dd[k]
                    for a in self.nr[k] for b in self.ns[k] for g in self.gg[k]],
        }


def s4_to_s3():
    C, r, s = symmetric(4, (1, 2, 3), (3, 4))
    Cp, _, _ = symmetric(3, (1, 2, 3), (1, 2))
    partitions = [frozenset((frozenset((0, 1)), frozenset((2, 3)))),
                  frozenset((frozenset((0, 2)), frozenset((1, 3)))),
                  frozenset((frozenset((0, 3)), frozenset((1, 2))))]
    phi = []
    for a in C.elements:
        action = tuple(partitions.index(frozenset(
            frozenset(a[x] for x in pair) for pair in part)) for part in partitions)
        phi.append(Cp.index[action])
    assert len(set(phi)) == 6
    assert all(phi[C.m[a][b]] == Cp.m[phi[a]][phi[b]]
               for a in range(C.n) for b in range(C.n))
    return C, r, s, Cp, phi[r], phi[s], phi


def check_descent(kind):
    C, r, s, Cp, rp, sp, phi = s4_to_s3()
    S, T = SignedModel(C, r, s, kind), SignedModel(Cp, rp, sp, kind)
    N = {c for c in range(C.n) if phi[c] == Cp.one}
    assert len(N) == 4
    for u in S.autos:
        assert {u[c] for c in N} == N
    fibers = {x: [c for c in range(C.n) if phi[c] == x] for x in range(Cp.n)}
    dmap = []
    for a, mu, er, es in S.D:
        images = []
        for x in range(Cp.n):
            values = {phi[S.autos[a][c]] for c in fibers[x]}
            assert len(values) == 1
            images.append(values.pop())
        dmap.append(T.di[(T.ai[tuple(images)], mu, er, es)])
    assert set(dmap) == set(range(len(T.D)))
    assert all(dmap[S.dm(a, b)] == T.dm(dmap[a], dmap[b])
               for a in range(len(S.D)) for b in range(len(S.D)))
    gmap = [T.sq[(phi[c], dmap[d])] for c, d in S.reps]
    for c in range(C.n):
        for d in range(len(S.D)):
            assert gmap[S.sq[(c, d)]] == T.sq[(phi[c], dmap[d])]
    assert set(gmap) == set(range(T.n))
    assert all(gmap[S.m[a][b]] == T.m[gmap[a]][gmap[b]]
               for a in range(S.n) for b in range(S.n))
    gammap = [T.dg[dmap[d]] for d in S.greps]
    assert all(gammap[S.dg[d]] == T.dg[dmap[d]] for d in range(len(S.D)))
    assert all(gammap[S.gm[a][b]] == T.gm[gammap[a]][gammap[b]]
               for a in range(S.ngamma) for b in range(S.ngamma))
    assert all(T.delta[gmap[g]] == gammap[S.delta[g]] for g in range(S.n))
    A = {d for d in range(len(S.D)) if dmap[d] == T.done}
    LN = S.L & N
    KG = {g for g in range(S.n) if gmap[g] == T.one}
    assert A == {S.j[l] for l in LN}
    assert KG == {S.ce[c] for c in N}
    assert len(KG) == len(N)*len(A)//len(LN)
    for x, name in ((r, 'rho'), (s, 'sigma')):
        actual = {g for g in S.N[name] if gmap[g] == T.one}
        assert actual == {g for g in KG if S.conj(g, S.ce[x]) == S.ce[x]}

    sobj, tobj = S.objects(), T.objects()
    for M, obj in ((S, sobj), (T, tobj)):
        ci = {g: c for c, g in enumerate(M.ce)}
        parameters = set()
        for d, a, b, U in obj['S0M']:
            f = M.m[M.de[d]][M.inv[U]]
            assert f in ci
            assert M.m[M.inv[f]][M.de[d]] == U
            parameters.add((d, a, b, ci[f]))
        assert len(parameters) == len(obj['S0Gamma'])*M.C.n
        centralizers = {x: [M.ce[c] for c in range(M.C.n)
                            if M.C.conj(c, x) == x] for x in (M.r, M.s)}
        for d, a, b in obj['S0Gamma']:
            for x, coordinate, element in ((M.r, 2, a), (M.s, 3, b)):
                tv = M.one if M.D[d][coordinate] == 1 else M.tp
                alpha = M.m[M.m[M.de[d]][M.inv[element]]][tv]
                for a0 in centralizers[x]:
                    element_new = M.m[M.conj(tv, M.inv[a0])][element]
                    alpha_new = M.m[M.m[M.de[d]][M.inv[element_new]]][tv]
                    assert alpha_new == M.m[alpha][a0]
                for ell in M.L:
                    dl = M.dm(M.j[ell], d)
                    alpha_left = M.m[M.m[M.de[dl]][M.inv[element]]][tv]
                    assert alpha_left == M.m[M.ce[ell]][alpha]
    maps = {'D': lambda d: dmap[d], 'gamma': lambda k: gammap[k],
            'G': lambda g: gmap[g], 'Nrho_star': lambda g: gmap[g],
            'Nsigma_star': lambda g: gmap[g],
            'Gamma': lambda z: tuple(gmap[g] for g in z),
            'M': lambda z: tuple(gmap[g] for g in z),
            'S0Gamma': lambda z: (dmap[z[0]], gmap[z[1]], gmap[z[2]]),
            'S0M': lambda z: (dmap[z[0]], gmap[z[1]], gmap[z[2]], gmap[z[3]])}
    identities = {'D': T.done, 'gamma': T.gone, 'G': T.one,
                  'Nrho_star': T.one, 'Nsigma_star': T.one,
                  'Gamma': (T.one, T.one), 'M': (T.one,)*3,
                  'S0Gamma': (T.done, T.one, T.one),
                  'S0M': (T.done, T.one, T.one, T.one)}
    stats = {}
    for name, domain in sobj.items():
        image_fibers = Counter(maps[name](x) for x in domain)
        assert set(image_fibers) == set(tobj[name]), name
        assert len(set(image_fibers.values())) == 1, name
        kernel = image_fibers[identities[name]]
        stats[name] = {'source': len(domain), 'target': len(tobj[name]),
                       'image': len(image_fibers), 'kernel': kernel}
    # The smallest natural coefficient subgroup need not contain j(L0).
    D0 = {S.done, S.td}
    assert all(S.dm(a, b) in D0 for a in D0 for b in D0)
    L0 = {l for l in S.L if S.j[l] in D0}
    G0 = {S.sq[(c, d)] for c in range(C.n) for d in D0}
    assert len(L0) == 1 and len(G0) == 2*C.n
    assert S.conj(S.t, S.ce[r]) != S.ce[r]
    assert S.conj(S.t, S.ce[r]) not in {S.ce[r], S.ce[C.inv[r]]}
    assert S.conj(S.tp, S.ce[r]) == S.ce[C.inv[r]]
    assert S.tp not in set(S.de), "tau prime should not be confused with tau in D"
    # The action of tau prime does not normalize the distinguished L0 in S4.
    assert {S.conj(S.tp, S.ce[l]) for l in S.L} != {S.ce[l] for l in S.L}
    return {
        'kind': kind, 'numeric_modulus': 12,
        'source_generators': {'rho': C.as_list(r), 'sigma': C.as_list(s)},
        'target_generators': {'rho': Cp.as_list(rp), 'sigma': Cp.as_list(sp)},
        'kernel_S4_to_S3': [C.as_list(c) for c in sorted(N)],
        'L_intersection_N': [C.as_list(c) for c in sorted(LN)],
        'A_order': len(A), 'all_automorphisms_preserve_kernel': True,
        'objects': stats,
        'natural_D0': {'order': len(D0), 'L_intersection': len(L0),
                       'G0_order': len(G0), 'tau_prime_not_in_D': True,
                       'action_is_nontrivial': True},
        'all_component_maps_and_fibers_verified': True,
        'effective_parameter_extension_verified': True,
    }


def matrix_descent():
    import sympy as sp
    a, mu = sp.symbols('a mu', nonzero=True)
    r = sp.Matrix([[0, 1], [-1, 1]])
    s = sp.Matrix([[0, -1], [1, 0]])
    g = sp.Matrix([[mu, a*mu], [0, 1]])
    ss = sp.Matrix([[a, -mu*(1+a*a)], [1/mu, -a]])
    rr = -ss*sp.Matrix([[1, -mu], [0, 1]])
    assert (g*s*g.inv()-ss).applyfunc(sp.simplify) == sp.zeros(2)
    assert (g*r*g.inv()-rr).applyfunc(sp.simplify) == sp.zeros(2)
    assert sp.simplify(ss.det()) == sp.simplify(rr.det()) == 1
    assert sp.simplify(ss.trace()) == 0 and sp.simplify(rr.trace()) == 1
    results = []
    for n in (2, 3, 4, 5, 8, 9):
        count = 0
        units = [v for v in range(n) if gcd(v, n) == 1]
        r0, s0 = (0, 1, n-1, 1), (0, n-1, 1, 0)
        for v in units:
            local = 0
            for ss0 in product(range(n), repeat=4):
                x, y, z, w = ss0
                if (x+w) % n or (x*w-y*z) % n != 1:
                    continue
                rr0 = tuple(-q % n for q in matmul(ss0, (1, -v % n, 0, 1), n))
                if (rr0[0]+rr0[3]) % n != 1:
                    continue
                assert z == pow(v, -1, n)
                assert y == -v*(1+x*x) % n
                g0 = (v, x*v % n, 0, 1)
                gi = (pow(v, -1, n), -x % n, 0, 1)
                assert matmul(matmul(g0, s0, n), gi, n) == ss0
                assert matmul(matmul(g0, r0, n), gi, n) == rr0
                local += 1
            assert local == n
            count += local
        results.append({'modulus': n, 'units': len(units), 'solutions': count,
                        'solutions_per_multiplier': n})
    # First explicit unlifted adelic parameter: mu_5=2, mu_p=1 elsewhere.
    # These calculations prove its individual conjugacy conditions at 5;
    # they do not assert the compatible profinite lift.
    r5, s5, g5, gi5 = (0, 1, 4, 1), (0, 4, 1, 0), (2, 0, 0, 1), (3, 0, 0, 1)
    kr, ks = (3, 3, 1, 3), (1, 1, 2, 3)
    for k, x in ((kr, r5), (ks, s5)):
        assert (k[0]*k[3]-k[1]*k[2]) % 5 == 1
        ki = (k[3], -k[1] % 5, -k[2] % 5, k[0])
        assert matmul(matmul(k, x, 5), ki, 5) == matmul(matmul(g5, x, 5), gi5, 5)
    return {'symbolic_conjugation_identities': True, 'finite_trace_pair_counts': results,
            'specified_adelic_lifting_instance': {'mu_5': 2, 'other_components': 1,
                'rho_conjugator_mod5': list(kr), 'sigma_conjugator_mod5': list(ks),
                'individual_conjugacies_verified': True, 'full_profinite_lift': 'not decided'}}


def nonlifting_normalizer():
    C, r, s = sl2(3)
    center = {c for c in range(C.n) if all(C.conj(c, x) == x for x in range(C.n))}
    projective = []
    for a, b, c, d in C.elements:
        perm = []
        for x in (0, 1, 2, 3):  # 3 denotes infinity.
            num, den = ((a, c) if x == 3 else ((a*x+b) % 3, (c*x+d) % 3))
            perm.append(3 if den == 0 else num*pow(den, -1, 3) % 3)
        projective.append(tuple(perm))
    assert len(set(projective)) == 12
    assert all(sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2 == 0
               for p in projective)
    assert {c for c, p in enumerate(projective) if p == tuple(range(4))} == center
    reps, phi, qone, qm = quotient_data(list(range(C.n)), C.one,
                                        lambda a, b: C.m[a][b], center)
    qv = [next(j for j in range(len(reps)) if qm[i][j] == qone)
          for i in range(len(reps))]
    Cp = FiniteGroup('A4=SL2(F3)/center', range(len(reps)), qone,
                     lambda a, b: qm[a][b], lambda a: qv[a])
    S, T = SignedModel(C, r, s, 'Z'), SignedModel(Cp, phi[r], phi[s], 'Z')
    dmap = []
    for a, mu, er, es in S.D:
        images = tuple(phi[S.autos[a][c]] for c in reps)
        assert all(phi[S.autos[a][c]] == images[phi[c]] for c in range(C.n))
        dmap.append(T.di[(T.ai[images], mu, er, es)])
    assert set(dmap) == set(range(len(T.D)))
    assert sum(d == T.done for d in dmap) == 1
    gmap = [T.sq[(phi[c], dmap[d])] for c, d in S.reps]
    assert set(gmap) == set(range(T.n))
    KG = {g for g in range(S.n) if gmap[g] == T.one}
    assert KG == {S.ce[c] for c in center}
    j = C.index[(1, 1, 1, 2)]
    omega = C.power(s, 2)
    assert C.conj(j, s) == C.m[omega][s] != s
    target = T.ce[phi[j]]
    assert target in T.N['sigma']
    lifts = [g for g in range(S.n) if gmap[g] == target]
    assert len(lifts) == 2
    assert all(g not in S.N['sigma'] for g in lifts)
    image = {gmap[g] for g in S.N['sigma']}
    assert len(image)*2 == len(T.N['sigma'])
    return {'source': 'SL2(F3)', 'target': 'A4', 'kind': 'Z',
            'D_orders': [len(S.D), len(T.D)], 'A_q_order': 1,
            'projective_identification_A4_verified': True, 'G_orders': [S.n, T.n],
            'G_kernel_order': len(KG),
            'sigma_star_orders': [len(S.N['sigma']), len(T.N['sigma'])],
            'sigma_star_image_order': len(image),
            'unliftable_target_representative': C.as_list(j),
            'every_possible_group_lift_fails': True}


def gluing_check():
    # A=C2, quotient=C2, trivial action: C4 and V4 are different extensions.
    from itertools import combinations
    extensions = {
        'C4': {'els': list(range(4)), 'mul': lambda a, b: (a+b) % 4,
               'q': lambda a: a % 2, 'j': lambda a: 2*a},
        'V4': {'els': list(range(4)), 'mul': lambda a, b: a ^ b,
               'q': lambda a: a % 2, 'j': lambda a: 2*a},
    }
    reconstruction = {}
    for name, H in extensions.items():
        # Reconstruct (A x H)/{(a,j(a)^-1)} from the one-factor data.
        mul = lambda z, w: (z[0] ^ w[0], H['mul'](z[1], w[1]))
        anti = {(0, 0), (1, 2)}
        reps, cos, one, table = quotient_data(list(product(range(2), range(4))),
                                             (0, 0), mul, anti)
        iso = [H['mul'](H['j'](a), h) for a, h in reps]
        assert len(set(iso)) == 4
        assert all(iso[table[i][j]] == H['mul'](iso[i], iso[j])
                   for i in range(4) for j in range(4))
        reconstruction[name] = len(reps)
    gluings = {}
    for left, right in [('C4', 'C4'), ('C4', 'V4')]:
        H, J = extensions[left], extensions[right]
        fiber = [(h, j) for h in range(4) for j in range(4)
                 if H['q'](h) == J['q'](j)]
        kernel = {z for z in fiber if H['q'](z[0]) == 0}
        diag = {(0, 0), (2, 2)}
        mul = lambda z, w: (H['mul'](z[0], w[0]), J['mul'](z[1], w[1]))
        found = []
        for rest in combinations([z for z in fiber if z != (0, 0)], 3):
            S = {(0, 0), *rest}
            if not all(mul(z, w) in S for z in S for w in S):
                continue
            if S & kernel != diag or {H['q'](z[0]) for z in S} != {0, 1}:
                continue
            found.append(sorted(S))
        assert len(found) == (2 if left == right else 0)
        gluings[f'{left}_with_{right}'] = {'fiber_product_order': len(fiber),
                                          'diagonal_extensions': found}
    return {'single_factor_reconstruction_orders': reconstruction, 'gluing': gluings}


if __name__ == '__main__':
    result = {'finite_descent': [check_descent(kind) for kind in ('B', 'Z')],
              'matrix_congruence_descent': matrix_descent(),
              'normalizer_nonlifting': nonlifting_normalizer(),
              'reconstruction': gluing_check()}
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print('All exact functoriality, matrix, and reconstruction checks passed.')
    for row in result['finite_descent']:
        print('\nS4 -> S3, signed numerical group', row['kind'])
        print('object source target image kernel')
        for name, counts in row['objects'].items():
            print(name, counts['source'], counts['target'], counts['image'], counts['kernel'])
        print('natural D0:', row['natural_D0'])
    print('\nCongruence trace-pair counts:', result['matrix_congruence_descent'])
    print('\nNon-surjective starred normalizer:', result['normalizer_nonlifting'])
    print('\nGluing:', result['reconstruction'])



#!/usr/bin/env python3
"""Exact signed constructions of LM C3:530--559 in four finite quotients.

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


def compute_model(C, r, s):
    autos, aindex, aone, amul, ainv = automorphisms(C, r, s)
    n = len(autos)
    omega = C.power(r, 3)
    assert omega == C.power(s, 2) and C.power(omega, 2) == C.one
    assert all(C.conj(g, omega) == omega for g in range(C.n))
    tau = cayley_map(C, r, s, C.conj(s, C.inv[r]), C.inv[s])
    assert tau is not None and tuple(tau[tau[i]] for i in range(C.n)) == tuple(range(C.n))
    tauindex = aindex[tau]
    e0, e1 = C.m[s][r], C.m[r][s]
    ell1 = C.power(e1, 2)
    m = C.orders[e0]
    modulus = lcm(12, m)
    assert modulus == 12
    units = [a for a in range(modulus) if gcd(a, modulus) == 1]
    L = {C.power(e0, i) for i in range(m)}
    center = {c for c in range(C.n) if all(C.conj(c, g) == g for g in range(C.n))}
    assert L & center == {C.one}
    inners = {c: aindex[tuple(C.conj(c, g) for g in range(C.n))] for c in range(C.n)}
    classes = {x: {C.conj(c, x) for c in range(C.n)} for x in (r, s, C.inv[r], C.inv[s])}
    E = {x: [e for e in (1, -1) if C.power(x, e) in classes[x]] for x in (r, s)}
    centralizers = {x: {c for c in range(C.n) if C.conj(c, x) == x} for x in (r, s)}
    Lambda = [mu for mu in units if C.power(e0, mu) == e0]

    def er(mu):
        return 1 if mu % 3 == 1 else -1

    def es(mu):
        return 1 if mu % 4 == 1 else -1

    Ds = {}
    for kind in ("B", "Z"):
        D = []
        for ai, u in enumerate(autos):
            for mu in units:
                if u[e0] != C.power(e0, mu):
                    continue
                signs = [(er(mu), es(mu))] if kind == "B" else product((1, -1), repeat=2)
                for sr, ss in signs:
                    if u[r] in classes[C.power(r, sr)] and u[s] in classes[C.power(s, ss)]:
                        D.append((ai, mu, sr, ss))
        D = sorted(D)
        di = {d: i for i, d in enumerate(D)}
        done = di[(aone, 1, 1, 1)]

        def dm(i, j):
            a, b = D[i], D[j]
            return di[(amul[a[0]][b[0]], a[1]*b[1] % modulus, a[2]*b[2], a[3]*b[3])]

        dinv = [di[(ainv[a], pow(mu, -1, modulus), sr, ss)] for a, mu, sr, ss in D]
        jL = {c: di[(inners[c], 1, 1, 1)] for c in L}
        assert len(set(jL.values())) == len(L)
        for i in range(len(D)):
            for c in L:
                assert dm(dm(i, jL[c]), dinv[i]) == jL[autos[D[i][0]][c]]
        greps, dg, gone, gmul = quotient_data(list(range(len(D))), done, dm, set(jL.values()))
        gamma = len(greps)

        def sm(a, b):
            c, d = a
            cp, dp = b
            return C.m[c][autos[D[d][0]][cp]], dm(d, dp)

        semi = list(product(range(C.n), range(len(D))))
        anti = {(C.inv[c], jL[c]) for c in L}
        # The antidiagonal centralizes C, and D carries it to itself.
        for c in range(C.n):
            for q in anti:
                assert sm((c, done), q) == sm(q, (c, done))
        for d in range(len(D)):
            for q in anti:
                assert sm(sm((C.one, d), q), (C.one, dinv[d])) in anti
        reps, sq, one, mul = quotient_data(semi, (C.one, done), sm, anti)
        sizeG = len(reps)
        invG = [sq[(autos[D[dinv[d]][0]][C.inv[c]], dinv[d])] for c, d in reps]
        Cembed = [sq[(c, done)] for c in range(C.n)]
        Dembed = [sq[(C.one, d)] for d in range(len(D))]
        assert len(set(Cembed)) == C.n and len(set(Dembed)) == len(D)
        delta = [dg[d] for c, d in reps]
        assert all(delta[sq[a]] == dg[a[1]] for a in semi)
        assert Counter(delta) == {g: C.n for g in range(gamma)}
        chiR = [D[d][2] for d in greps]
        chiS = [D[d][3] for d in greps]
        chiMu = [D[d][1] for d in greps]
        assert all(D[d][1:] == (chiMu[dg[d]], chiR[dg[d]], chiS[dg[d]]) for d in range(len(D)))

        def cg(a, b):
            return mul[mul[a][b]][invG[a]]

        tauD = di[(tauindex, modulus - 1, -1, -1)]
        t = Dembed[tauD]
        tp = mul[Cembed[C.inv[s]]][t]
        assert mul[t][t] == one and mul[tp][tp] == one
        assert cg(tp, Cembed[r]) == Cembed[C.inv[r]]
        assert cg(tp, Cembed[s]) == Cembed[C.inv[s]]
        Cprime = {mul[Cembed[c]][one if v == 0 else tp]: v
                  for c in range(C.n) for v in (0, 1)}
        assert len(Cprime) == 2*C.n

        signed = {}
        for x, name, chi in ((r, "rho", chiR), (s, "sigma", chiS)):
            xG = Cembed[x]
            Zx = [g for g in range(sizeG) if cg(g, xG) == xG]
            Nx = [(g, e) for g in range(sizeG) for e in (1, -1)
                  if cg(g, xG) == Cembed[C.power(x, e)]]
            star = [(g, e) for g, e in Nx if e == chi[delta[g]]]
            Zstar = [g for g in Zx if chi[delta[g]] == 1]
            projected = {g for g, e in Nx}
            assert len(projected) == sum(1 for g in range(sizeG)
                                         if cg(g, xG) in {Cembed[C.power(x, e)] for e in (1, -1)})
            kernel_i = [(g, e) for g, e in Nx if g == one]
            assert len(kernel_i) == (2 if C.power(x, 2) == C.one else 1)
            assert len({g for g, e in star}) == len(star)
            assert Counter(delta[g] for g, e in star) == {d: len(centralizers[x]) for d in range(gamma)}
            assert {delta[g] for g in Zx} == {d for d in range(gamma) if chi[d] in E[x]}
            assert len(Zstar)*2 == len(star)
            buckets = {d: [g for g, e in star if delta[g] == d] for d in range(gamma)}
            mismatch = next((g for g in Zx if chi[delta[g]] == -1), None)
            signed[name] = dict(Z=Zx, N=Nx, star=star, Zstar=Zstar, buckets=buckets,
                                kernel_i=len(kernel_i), mismatch=mismatch)

        parameter_count = 0
        for d, (ai, mu, sr, ss) in enumerate(D):
            uG = Dembed[d]
            vgR, vgS = (0 if sr == 1 else 1), (0 if ss == 1 else 1)
            candidatesA = {a for a, v in Cprime.items()
                           if v == vgR and cg(a, Cembed[r]) == Cembed[autos[ai][r]]}
            candidatesB = {b for b, v in Cprime.items()
                           if v == vgS and cg(b, Cembed[s]) == Cembed[autos[ai][s]]}
            assert len(candidatesA) == len(centralizers[r])
            assert len(candidatesB) == len(centralizers[s])
            actual = set()
            for a in signed["rho"]["buckets"][dg[d]]:
                for b in signed["sigma"]["buckets"][dg[d]]:
                    alpha = mul[mul[uG][invG[a]]][one if vgR == 0 else tp]
                    beta = mul[mul[uG][invG[b]]][one if vgS == 0 else tp]
                    actual.add((alpha, beta))
                    # Explicit inverse of the parameterization.
                    assert mul[mul[one if vgR == 0 else tp][invG[alpha]]][uG] == a
                    assert mul[mul[one if vgS == 0 else tp][invG[beta]]][uG] == b
            assert actual == set(product(candidatesA, candidatesB))
            parameter_count += len(actual)

        sigma_numerical = set()
        for mu in units:
            signs = [(er(mu), es(mu))] if kind == "B" else product((1, -1), repeat=2)
            for sr, ss in signs:
                for rp in classes[C.power(r, sr)]:
                    for sp in classes[C.power(s, ss)]:
                        xi = C.m[rp][C.inv[r]]
                        eta = C.m[sp][C.inv[s]]
                        if xi == C.m[eta][C.power(ell1, (mu-1)//2)]:
                            sigma_numerical.add((rp, sp, mu, sr, ss))
        sigma_effective = {(autos[a][r], autos[a][s], mu, sr, ss) for a, mu, sr, ss in D}
        assert sigma_effective <= sigma_numerical
        # All numerical solutions happen to be effective in these four models.
        assert sigma_effective == sigma_numerical
        numkernel = [d for d in D if d[0] == aone]
        expected_kernel = (len(Lambda)*len(E[r])*len(E[s]) if kind == "Z" else
                           sum(1 for mu in Lambda if er(mu) in E[r] and es(mu) in E[s]))
        assert len(numkernel) == expected_kernel
        effective_aut = {d[0] for d in D}
        assert len(D) == len(effective_aut)*len(numkernel)
        cr, cs = len(centralizers[r]), len(centralizers[s])
        Gamma = cr*cs*gamma
        M = Gamma*C.n
        S0Gamma = m*Gamma
        S0M = m*M
        assert parameter_count == S0Gamma
        counts = dict(D=len(D), effective_automorphisms=len(effective_aut),
                      numerical_kernel=len(numkernel), gamma=gamma, G=sizeG,
                      Zrho=len(signed["rho"]["Z"]), Zsigma=len(signed["sigma"]["Z"]),
                      Nrho=len(signed["rho"]["N"]), Nsigma=len(signed["sigma"]["N"]),
                      Nrho_star=len(signed["rho"]["star"]), Nsigma_star=len(signed["sigma"]["star"]),
                      Zrho_star=len(signed["rho"]["Zstar"]), Zsigma_star=len(signed["sigma"]["Zstar"]),
                      kernel_i_rho=signed["rho"]["kernel_i"], kernel_i_sigma=signed["sigma"]["kernel_i"],
                      Gamma=Gamma, M=M, S0Gamma=S0Gamma, S0M=S0M,
                      Sigma_numerical=len(sigma_numerical), Sigma_effective=len(sigma_effective),
                      chi_image=sorted(set(chiMu)),
                      centralizer_sign_mismatch_rho=signed["rho"]["mismatch"] is not None,
                      centralizer_sign_mismatch_sigma=signed["sigma"]["mismatch"] is not None,
                      every_star_fibre_verified=True, parameter_bijection_verified=True)
        Ds[kind] = counts
    assert Ds["Z"]["D"] // Ds["B"]["D"] in (1, 2, 4)
    result = dict(group=C.name, order=C.n, automorphisms=n, rho=C.as_list(r), sigma=C.as_list(s),
                  orders=dict(rho=C.orders[r], sigma=C.orders[s], epsilon0=m),
                  centralizer_rho=len(centralizers[r]), centralizer_sigma=len(centralizers[s]),
                  rho_inverse_conjugate=(-1 in E[r]), sigma_inverse_conjugate=(-1 in E[s]),
                  modulus=modulus, units=units, multiplier_kernel=Lambda, L0_central_kernel=1,
                  independent_sign_index=Ds["Z"]["D"] // Ds["B"]["D"], models=Ds)
    print("SIGNED_MODEL", json.dumps(result, sort_keys=True))
    return result


records = [compute_model(*data) for data in (
    symmetric(3, (1, 2, 3), (1, 2)),
    symmetric(4, (1, 2, 3), (3, 4)),
    sl2(3), sl2(4))]

# C3:546 (64): the orientation-reversing factor belongs on the right.
n = 3
rho, sigma, tp = (0, 1, 2, 1), (0, 2, 1, 0), (0, 1, 1, 0)

def glinv(a):
    z = pow((a[0]*a[3]-a[1]*a[2]) % n, -1, n)
    return tuple(z*b % n for b in (a[3], -a[1], -a[2], a[0]))

def glconj(a, b):
    return matmul(matmul(a, b, n), glinv(a), n)

rhs = tuple(-a % n for a in glconj(rho, sigma))
left = glconj(matmul(tp, rho, n), sigma)
right = glconj(matmul(rho, tp, n), sigma)
assert left != rhs and right == rhs
side_correction = dict(modulus=n, beta=rho, tau_prime=tp, sigma=sigma,
                       desired_negative_conjugate=rhs, left_factor_result=left,
                       right_factor_result=right)
print("RIGHT_FACTOR_CORRECTION", json.dumps(side_correction, sort_keys=True))
answer = dict(models=records, scan546_correction=side_correction,
              all_assertions_passed=True,
              scope="Finite U(12) shadows; profinite groups are obtained by fibre product with Zhat*.")
(OUT / "AB_signed_finite.json").write_text(json.dumps(answer, indent=2) + "\n")
print("ALL SIGNED ASSERTIONS PASSED")

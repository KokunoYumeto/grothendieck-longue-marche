"""Referee B check: the finite and combinatorial steps of LM4 D.34 (global signs and the cusp cycle).

Written by Claude Opus 5.5 at effort max, 14 Nov 2026.  Reads no file of the return.
Run: python -I -B check_lm4_d34.py
"""
import itertools
from math import gcd

FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)

print("== (D.34d): local classes ker(1+mu)/(1-mu) in a truncated Zhat ==")
# model Zhat by Z/M with M = 2^6 3^4 5^3 7^2; mu given by CRT from its prime coordinates
primes = {2: 6, 3: 4, 5: 3, 7: 2}
M = 1
for p_, k in primes.items():
    M *= p_**k
def crt(coords):
    x = 0
    for p_, k in primes.items():
        m = p_**k
        Mi = M // m
        x += coords[p_] * Mi * pow(Mi, -1, m)
    return x % M
for signs in itertools.product([1, -1], repeat=3):
    co = {2: -1, 3: signs[0], 5: signs[1], 7: signs[2]}
    mu = crt(co)
    ker = [t for t in range(M) if ((1 + mu)*t) % M == 0]
    img = {((1 - mu)*w) % M for w in range(M)}
    # quotient size = |ker| / |img intersect ker|
    q = len(ker) // len([t for t in ker if t in img])
    ok = q == 2
    check("mu_2 = -1, (mu_3,mu_5,mu_7) = %s: |ker(1+mu)/(1-mu)| = 2" % (signs,), ok)
mu = crt({2: -1, 3: -1, 5: -1, 7: -1})
e2 = crt({2: 1, 3: 0, 5: 0, 7: 0})
check("t = -e_2 lies in ker(1+mu) and not in (1-mu)Zhat (second class c^{e_2} b)", ((1 + mu)*(-e2)) % M == 0 and (-e2) % M not in {((1 - mu)*w) % M for w in range(M)})
check("e_2 is odd (its image in Zhat/2 is 1)", e2 % 2 == 1)

print("== (D.34i): the cyclic cover chi: x -> 1, y -> 0 of degree q ==")
for qq in (3, 5, 7, 11, 13):
    # boundary components over a puncture with chi-value c: gcd(c, q) components? number = q / order(c)
    def comps(cval):
        order = qq // gcd(cval % qq, qq) if cval % qq else 1
        return qq // order, order          # (number of boundaries, degree of each)
    bx, dx = comps(1); by, dy = comps(0); bz, dz = comps(-1)
    b = bx + by + bz
    euler = -qq
    genus = (2 - b - euler) // 2
    check("q=%d: boundaries over x,y,z = %d,%d,%d with degrees %d,%d,%d; genus %d" % (qq, bx, by, bz, dx, dy, dz, genus),
          (bx, by, bz) == (1, qq, 1) and (dx, dy, dz) == (qq, 1, qq) and genus == 0 and b == qq + 2)
    # k_i = x^{lam i} f^{-1} x^{-i} has chi = (lam - 1) i = 0 when lam = 1 mod q
    check("q=%d: chi(k_i) = (lam-1) i = 0 mod q for lam = 1 mod q" % qq, all(((1 - 1)*i) % qq == 0 for i in range(qq)))

print("== the graph step: Aut of the (q+2)-cycle has no element acting on edges as a q-cycle fixing two edges ==")
for qq in (3, 5, 7, 11, 13):
    n = qq + 2
    # cycle graph with vertices 0..n-1 and edges {i,i+1}; automorphisms = dihedral group
    auts = []
    for r in range(n):
        auts.append(lambda v, r=r: (v + r) % n)
        auts.append(lambda v, r=r: (r - v) % n)
    edges = [frozenset({i, (i + 1) % n}) for i in range(n)]
    def edge_perm(a):
        return tuple(edges.index(frozenset({a(i), a((i + 1) % n)})) for i in range(n))
    perms = {edge_perm(a) for a in auts}
    def cycle_type(p):
        seen = set(); ct = []
        for i in range(n):
            if i in seen: continue
            j = i; L = 0
            while j not in seen:
                seen.add(j); j = p[j]; L += 1
            ct.append(L)
        return sorted(ct)
    target = sorted([1, 1, qq])
    check("q=%d: |Aut(C_%d)| = %d, q does not divide it, no edge permutation of type (q,1,1)" % (qq, n, len(perms), ),
          len(perms) == 2*n and (2*n) % qq != 0 and all(cycle_type(p) != target for p in perms))

print("== the cycle argument: [c_1],...,[c_n] in F2^{n-1} have only the full relation ==")
for n in (3, 4, 5, 6, 7):
    vecs = [tuple(1 if j == i else 0 for j in range(n - 1)) for i in range(n - 1)] + [tuple([1]*(n - 1))]
    rels = []
    for k in range(1, n + 1):
        for sub in itertools.combinations(range(n), k):
            s = tuple(sum(vecs[i][j] for i in sub) % 2 for j in range(n - 1))
            if not any(s):
                rels.append(sub)
    check("n=%d: the only nonempty zero-sum subset of cusp vectors is the full set" % n, rels == [tuple(range(n))])

print("== (D.34l) and (D.34b) ==")
# images in H1(E,F2) = F2^2 + F2 of s, x^{e2} s, y^{e2} f s (f in F'): (0,0,1),(1,0,1),(0,1,1)
imgs = {'s': (0, 0, 1), 'x^e2 s': (1 % 2, 0, 1), 'y^e2 f s': (0, 1 % 2, 1)}
check("three distinct images (0,0,1),(1,0,1),(0,1,1)", len(set(imgs.values())) == 3)
check("triangle edge vectors: s--x^e2 s is [x], s--y^e2 fs is [y], x^e2 s--y^e2 fs is [x]+[y] = [z]",
      tuple((a - b) % 2 for a, b in zip(imgs['x^e2 s'], imgs['s'])) == (1, 0, 0)
      and tuple((a - b) % 2 for a, b in zip(imgs['y^e2 f s'], imgs['s'])) == (0, 1, 0)
      and tuple((a - b) % 2 for a, b in zip(imgs['y^e2 f s'], imgs['x^e2 s'])) == (1, 1, 0))
# abelianization of f = h^{-1} alpha(h) with alpha = -1 on Zhat^2: [f] = -2[h]
for hv in itertools.product(range(-3, 4), repeat=2):
    f_ab = tuple(-h - h for h in hv)
    if f_ab == (0, 0) and hv != (0, 0):
        FAILS.append("abelian step")
check("[f] = -2[h] = 0 forces [h] = 0 (integer test of the torsion-free step)", "abelian step" not in FAILS)

print("== group law: (lam,f)(mu,g) = (lam mu, f alpha_{(lam,f)}(g)) gives tau c = (1, f) for c = (-1, 1) ==")
# word check in the free group <x,y>: Phi_{(-1,f)} o Phi_{(-1,1)} = Phi_{(1,f)} on x and y, for sample f in F'
def red(w):
    out = []
    for t in w:
        if out and out[-1] == -t: out.pop()
        else: out.append(t)
    return tuple(out)
def inv(w):
    return tuple(-t for t in reversed(w))
def apply(img, w):   # img: dict letter -> word
    out = []
    for t in w:
        out.extend(img[t] if t > 0 else inv(img[-t]))
    return red(out)
def phi(lam, f):
    xl = (1,)*lam if lam > 0 else (-1,)*(-lam)
    yl = (2,)*lam if lam > 0 else (-2,)*(-lam)
    return {1: xl, 2: red(inv(f) + yl + f)}
samples = [red((1, 2, -1, -2)), red((1, 2, -1, -2, 1, 1, 2, -1, -1, -2)), red((2, 1, 1, -2, -1, -1))]
ok = True
for f in samples:
    left = {k: apply(phi(-1, f), v) for k, v in phi(-1, ()).items()}
    right = phi(1, f)
    ok &= left == right
check("Phi_{(-1,f)} o Phi_{(-1,1)} = Phi_{(1,f)} on x, y for three sample commutator words f (so tau c = (1, f))", ok)

print()
print("TOTAL FAILS:", len(FAILS))
for f_ in FAILS:
    print("  ", f_)

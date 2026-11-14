"""Referee B check: is the orbifold formula E.64.28 a homomorphism for every pair satisfying the
two-cycle (I) and three-cycle (II) equations?  Test in characteristic finite quotients of F2.

Written by Claude Opus 5.5 at effort max, 14 Nov 2026.  G = F2/K with K the intersection of the kernels
of all homomorphisms F2 -> P (P a small finite group); K is fully invariant, so every substitution
x -> w1, y -> w2 acts on G by permuting coordinates.  For every shadow (lam, f) with f in G' satisfying
(I) f(x,y) f(y,x) = 1 and (II) f(z,x) z^m f(y,z) y^m f(x,y) x^m = 1 (z = (xy)^{-1}, m = (lam-1)/2)
we evaluate candidate images of z.  Run: python -I -B check_gt_shadow_formulas.py
"""
import itertools, sys

def perm_mul(p, q):  # (p*q)(i) = p(q(i))
    return tuple(p[i] for i in q)
def perm_inv(p):
    r = [0]*len(p)
    for i, j in enumerate(p):
        r[j] = i
    return tuple(r)

def make_group(name):
    if name == 'S3':
        elems = [tuple(p) for p in itertools.permutations(range(3))]
        return elems, perm_mul, perm_inv, tuple(range(3))
    if name == 'A4':
        def sign(p):
            s = 1
            for i in range(len(p)):
                for j in range(i+1, len(p)):
                    if p[i] > p[j]: s = -s
            return s
        elems = [tuple(p) for p in itertools.permutations(range(4)) if sign(p) == 1]
        return elems, perm_mul, perm_inv, tuple(range(4))
    if name == 'D4':
        # dihedral of order 8 acting on 4 points
        r = (1, 2, 3, 0); s = (0, 3, 2, 1)
        elems = {tuple(range(4))}
        fr = [tuple(range(4))]
        while fr:
            nw = []
            for g in fr:
                for h in (r, s):
                    k = perm_mul(g, h)
                    if k not in elems:
                        elems.add(k); nw.append(k)
            fr = nw
        return sorted(elems), perm_mul, perm_inv, tuple(range(4))
    if name == 'Heis3':
        # Heisenberg group mod 3 as triples (a,b,c): (a,b,c)(a',b',c') = (a+a', b+b', c+c'+a b')
        elems = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]
        def mul(p, q):
            return ((p[0]+q[0]) % 3, (p[1]+q[1]) % 3, (p[2]+q[2]+p[0]*q[1]) % 3)
        def inv(p):
            a, b, c = p
            return ((-a) % 3, (-b) % 3, (-c + a*b) % 3)
        return elems, mul, inv, (0, 0, 0)
    if name == 'C7C3':
        # C7 x| C3, pairs (a, k): (a,k)(b,l) = (a + 2^k b, k+l)
        elems = [(a, k) for a in range(7) for k in range(3)]
        def mul(p, q):
            return ((p[0] + pow(2, p[1], 7)*q[0]) % 7, (p[1]+q[1]) % 3)
        def inv(p):
            a, k = p
            kk = (-k) % 3
            return ((-pow(2, kk, 7)*a) % 7, kk)
        return elems, mul, inv, (0, 0)
    raise ValueError(name)

def run(name, maxorder=400000):
    P, pm, pi, pe = make_group(name)
    homs = [(p, q) for p in P for q in P]          # all homomorphisms F2 -> P
    hidx = {h: i for i, h in enumerate(homs)}
    def gmul(g, h):
        return tuple(pm(a, b) for a, b in zip(g, h))
    def ginv(g):
        return tuple(pi(a) for a in g)
    X = tuple(h[0] for h in homs); Y = tuple(h[1] for h in homs)
    E = tuple(pe for _ in homs)
    # enumerate G
    G = {E}; fr = [E]
    while fr:
        nw = []
        for g in fr:
            for h in (X, Y, ginv(X), ginv(Y)):
                k = gmul(g, h)
                if k not in G:
                    G.add(k); nw.append(k)
                    if len(G) > maxorder:
                        print(name, ": G too large, skipped"); return None
        fr = nw
    # derived subgroup: normal closure of [X,Y]
    def gcomm(a, b):
        return gmul(gmul(a, b), gmul(ginv(a), ginv(b)))
    c0 = gcomm(X, Y)
    D = {E}; fr = [E]
    gens = [c0]
    # closure under multiplication by conjugates of c0 by X, Y
    conjs = set([c0]); frc = [c0]
    while frc:
        nw = []
        for c in frc:
            for g in (X, Y, ginv(X), ginv(Y)):
                k = gmul(gmul(g, c), ginv(g))
                if k not in conjs:
                    conjs.add(k); nw.append(k)
        frc = nw
    conjs = list(conjs)
    while fr:
        nw = []
        for g in fr:
            for c in conjs:
                k = gmul(g, c)
                if k not in D:
                    D.add(k); nw.append(k)
        fr = nw
    # exponent
    def order(g):
        k = 1; h = g
        while h != E:
            h = gmul(h, g); k += 1
        return k
    from math import gcd
    e = 1
    for g in list(G)[:5000]:
        o = order(g); e = e*o//gcd(e, o)
    def gpow(g, k):
        k %= e
        r = E
        for _ in range(k):
            r = gmul(r, g)
        return r
    # word evaluation on homs: substitution
    def subst(g, w1, w2):
        """g in G as function on homs; returns g(w1, w2) where w1, w2 in G (functions)"""
        out = []
        for i, h in enumerate(homs):
            newh = (w1[i], w2[i])
            out.append(g[hidx[newh]])
        return tuple(out)
    Zz = ginv(gmul(X, Y))
    print("%s: |G| = %d, |G'| = %d, exponent = %d" % (name, len(G), len(D), e))
    results = {}
    lams = [l for l in range(1, 2*e, 2) if gcd(l, e) == 1]
    nsol = 0
    stats = {}
    for lam in lams:
        m = (lam - 1)//2
        for f in D:
            fyx = subst(f, Y, X)
            if gmul(f, fyx) != E:
                continue
            fzx = subst(f, Zz, X); fyz = subst(f, Y, Zz)
            II = gmul(gmul(gmul(gmul(gmul(fzx, gpow(Zz, m)), fyz), gpow(Y, m)), f), gpow(X, m))
            if II != E:
                continue
            nsol += 1
            fxz = subst(f, X, Zz); fzy = subst(f, Zz, Y)
            Ox = gpow(X, lam)
            Oy = gmul(gmul(fyx, gpow(Y, lam)), f)
            Oz_E64 = gmul(gmul(gmul(gmul(gpow(X, m), fzx), gpow(Zz, lam)), fxz), gpow(X, -m))
            Oz_true = ginv(gmul(Ox, Oy))
            cands = {
                'E.64.28: x^m f(z,x) z^lam f(x,z) x^-m': Oz_E64,
                'f(z,x)^-1 x^-m z^lam x^m f(z,x)': gmul(gmul(gmul(gmul(fxz, gpow(X, -m)), gpow(Zz, lam)), gpow(X, m)), fzx),
                'f^-1 y^-m f(z,y) z^lam f(y,z) y^m f': gmul(gmul(gmul(gmul(gmul(gmul(ginv(f), gpow(Y, -m)), fzy), gpow(Zz, lam)), fyz), gpow(Y, m)), f),
                'f(x,z) z^lam f(z,x)  (no x^m)': gmul(gmul(fxz, gpow(Zz, lam)), fzx),
                'x^-m f(x,z)^-1... = x^-m f(z,x) z^lam f(x,z) x^m': gmul(gmul(gmul(gmul(gpow(X, -m), fzx), gpow(Zz, lam)), fxz), gpow(X, m)),
            }
            key = (lam, f == E)
            for cname, val in cands.items():
                stats.setdefault((lam, cname), [0, 0])
                stats[(lam, cname)][0] += 1
                if val == Oz_true:
                    stats[(lam, cname)][1] += 1
    print("  shadows (lam, f) satisfying (I),(II): %d" % nsol)
    for (lam, cname), (tot, ok) in sorted(stats.items()):
        print("  lam=%2d  %-55s holds for %d of %d" % (lam, cname, ok, tot))
    return stats

if __name__ == '__main__':
    for name in ['S3', 'A4', 'D4', 'Heis3', 'C7C3']:
        run(name)
        sys.stdout.flush()

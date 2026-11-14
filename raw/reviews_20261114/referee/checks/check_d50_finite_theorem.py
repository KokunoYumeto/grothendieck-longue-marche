"""Referee A (Claude Opus 5.5 at effort max), 14 Nov 2026.
Brute-force test of the finite theorem behind LM7_PUSH D.50 (D.50.15-16) and E.58.

Statement tested (a consequence of D.50.16, with D-dagger replaced by the universal
object D# = Lambda/[Lambda,K], K = ker(Lambda -> D), which maps onto every D-dagger
of the proof compatibly with the source maps):

  Let Lambda be F(x1,x2) (free source) or C2*C3 (modular source, x1 = s, x2 = r,
  x3 = tau^{-1}); let q_E: Lambda ->> E be onto a finite group E, A normal in E,
  D = E/A, X_i = q_E(x_i), T_i = A-conjugacy class of X_i.  For h = (h1,h2,h3) in D^3
  such that x_i -> h_i d_i h_i^{-1} is a homomorphism Lambda -> D and the obstruction
      o(h) = class of  w = t(h1) x1 t(h1)^-1 . t(h2) x2 t(h2)^-1 . t(h3) x3 t(h3)^-1
  in K/[Lambda,K] vanishes (i.e. the conjugators lift to D# with a peripheral map),
  the number of epimorphisms f: Lambda ->> E with f(x_i) in H_i T_i H_i^{-1}
  (H_i any lift of h_i) equals the reference number for h = (1,1,1).

K/[Lambda,K] is computed by Reidemeister-Schreier and integer Hermite reduction.
For D = (Z/a)^2 (free source) the obstruction is cross-checked against the
Heisenberg formula  -v1 + u2 + v3 - u3 = 0 mod a.
Also recorded: the counts on triples whose obstruction does NOT vanish (the theorem
says nothing there; a difference there shows the central refinement is needed).
Standard library only; reads no file of the return.
"""
import sys, time, json, itertools
from collections import defaultdict

T0 = time.time()
RESULTS = []

# ---------------------------------------------------------------- finite groups
class FG:
    def __init__(self, gens, mul, e, name):
        self.name = name
        elems = [e]; seen = {e: 0}; frontier = [e]
        while frontier:
            nf = []
            for g in frontier:
                for h in gens:
                    k = mul(g, h)
                    if k not in seen:
                        seen[k] = len(elems); elems.append(k); nf.append(k)
            frontier = nf
        self.elems = elems; self.idx = seen; self.n = len(elems); self.e = 0
        n = self.n
        self.tab = [[seen[mul(a, b)] for b in elems] for a in elems]
        inv = [0] * n
        for i in range(n):
            row = self.tab[i]
            for j in range(n):
                if row[j] == 0:
                    inv[i] = j; break
        self.inv = inv
        self.gens = [seen[g] for g in gens]

    def closure(self, gens):
        tab = self.tab
        S = {0}; frontier = [0]
        while frontier:
            nf = []
            for g in frontier:
                row = tab[g]
                for h in gens:
                    k = row[h]
                    if k not in S:
                        S.add(k); nf.append(k)
            frontier = nf
        return S

    def generates(self, a, b):
        tab = self.tab; n = self.n
        S = {0}; frontier = [0]
        while frontier:
            nf = []
            for g in frontier:
                row = tab[g]
                for h in (a, b):
                    k = row[h]
                    if k not in S:
                        S.add(k); nf.append(k)
                        if 2 * len(S) > n:
                            return True
            frontier = nf
        return len(S) == n

    def comm(self, g, h):
        t, i = self.tab, self.inv
        return t[t[t[g][h]][i[g]]][i[h]]

    def conj(self, g, h):  # g h g^-1
        t = self.tab
        return t[t[g][h]][self.inv[g]]

    def gamma_infty(self, N):
        cur = set(N)
        while True:
            gens = {self.comm(g, c) for g in N for c in cur}
            nxt = self.closure(list(gens))
            if nxt == cur:
                return cur
            cur = nxt

# ---------------------------------------------------------------- integer lattice
def hnf_rows(rows, ncols):
    rows = [list(r) for r in rows if any(r)]
    piv = []
    col = 0
    while rows and col < ncols:
        nz = [r for r in rows if r[col] != 0]
        if not nz:
            col += 1; continue
        rest = [r for r in rows if r[col] == 0]
        while len(nz) > 1:
            nz.sort(key=lambda r: abs(r[col]))
            p = nz[0]
            new = [p]
            for r in nz[1:]:
                qd = r[col] // p[col]
                rr = [a - qd * b for a, b in zip(r, p)]
                if rr[col] != 0:
                    new.append(rr)
                elif any(rr):
                    rest.append(rr)
            nz = new
        p = nz[0]
        if p[col] < 0:
            p = [-a for a in p]
        piv.append((col, p))
        rows = rest
        col += 1
    return piv

def in_lattice(v, piv):
    v = list(v)
    for col, p in piv:
        if v[col] % p[col] != 0:
            return False
        qd = v[col] // p[col]
        if qd:
            v = [a - qd * b for a, b in zip(v, p)]
    return not any(v)

# ---------------------------------------------------------------- the test
def run_test(name, G, X1, X2, A, modular, heis=None, max_seconds=900):
    t_start = time.time()
    tab, inv = G.tab, G.inv
    n = G.n
    X = [X1, X2]
    X3 = inv[tab[X1][X2]]
    assert G.closure([X1, X2]) == set(range(n)), "q_E not onto"
    if modular:
        assert tab[X1][X1] == 0 and tab[tab[X2][X2]][X2] == 0
    A = set(A)
    for g in G.gens + [X1, X2]:
        for a in A:
            assert G.conj(g, a) in A, "A not normal"
    # D = E/A
    pi = [min(tab[g][a] for a in A) for g in range(n)]
    Dids = sorted(set(pi)); Dn = len(Dids); dmap = {c: k for k, c in enumerate(Dids)}
    pi = [dmap[c] for c in pi]
    rep = [None] * Dn
    for g in range(n):
        if rep[pi[g]] is None:
            rep[pi[g]] = g
    dmul = [[pi[tab[rep[c1]][rep[c2]]] for c2 in range(Dn)] for c1 in range(Dn)]
    dinv = [pi[inv[rep[c]]] for c in range(Dn)]
    d1 = pi[0]
    dX = [pi[X1], pi[X2]]
    dXinv = [dinv[dX[0]], dinv[dX[1]]]
    def dstep(d, l, ep):
        return dmul[d][dX[l] if ep == 1 else dXinv[l]]
    # Schreier transversal
    t = {d1: []}
    order = [d1]
    for d in order:
        for l in (0, 1):
            for ep in (1, -1):
                d2 = dstep(d, l, ep)
                if d2 not in t:
                    t[d2] = t[d] + [(l, ep)]
                    order.append(d2)
    assert len(t) == Dn
    gid = {}
    ng = 0
    for d in range(Dn):
        for l in (0, 1):
            d2 = dstep(d, l, 1)
            if t[d2] == t[d] + [(l, 1)] or t[d] == t[d2] + [(l, -1)]:
                gid[(d, l)] = None
            else:
                gid[(d, l)] = ng; ng += 1
    def winv(w):
        return [(l, -ep) for (l, ep) in reversed(w)]
    def rewrite(w):
        vec = [0] * ng; d = d1
        for (l, ep) in w:
            if ep == 1:
                g = gid[(d, l)]
                if g is not None: vec[g] += 1
                d = dstep(d, l, 1)
            else:
                d2 = dstep(d, l, -1)
                g = gid[(d2, l)]
                if g is not None: vec[g] -= 1
                d = d2
        return vec, d
    rels = []
    if modular:
        for d in range(Dn):
            for R in ([(0, 1), (0, 1)], [(1, 1), (1, 1), (1, 1)]):
                v, dd = rewrite(t[d] + R + winv(t[d]))
                assert dd == d1
                rels.append(v)
    for (d, l), g in gid.items():
        if g is None: continue
        wg = t[d] + [(l, 1)] + winv(t[dstep(d, l, 1)])
        for gl in (0, 1):
            v, dd = rewrite([(gl, 1)] + wg + [(gl, -1)])
            assert dd == d1
            v[g] -= 1
            rels.append(v)
    piv = hnf_rows(rels, ng)
    # torsion of K/[Lambda,K] (diagonal of the echelon form gives the cokernel order only up to
    # the free part; record rank and the product of pivots for information)
    rank_L = len(piv)
    # classes
    def Aclass(g):
        return frozenset(G.conj(a, g) for a in A)
    T = [Aclass(X1), Aclass(X2), Aclass(X3)]
    clsid = [dict(), dict(), dict()]
    classes = {}
    for i in range(3):
        for h in range(Dn):
            H = rep[h]
            S = frozenset(G.conj(H, x) for x in T[i])
            k = min(S)
            classes[(i, k)] = S
            clsid[i][h] = k
    # conjugation in D
    dconj = lambda h, d: dmul[dmul[h][d]][dinv[h]]
    dXs = [dX[0], dX[1], pi[X3]]
    conj_to = [defaultdict(list) for _ in range(3)]
    for i in range(3):
        for h in range(Dn):
            conj_to[i][dconj(h, dXs[i])].append(h)
    x_words = [[(0, 1)], [(1, 1)], [(1, -1), (0, -1)]]
    ocache = {}
    key_info = {}
    ntrip = 0
    heis_disagree = 0
    for h1 in range(Dn):
        c1 = dconj(h1, dXs[0])
        w1 = t[h1] + x_words[0] + winv(t[h1])
        for h2 in range(Dn):
            c2 = dconj(h2, dXs[1])
            c3 = dinv[dmul[c1][c2]]
            if not conj_to[2][c3]:
                continue
            w12 = w1 + t[h2] + x_words[1] + winv(t[h2])
            for h3 in conj_to[2][c3]:
                w = w12 + t[h3] + x_words[2] + winv(t[h3])
                v, dd = rewrite(w)
                assert dd == d1
                tv = tuple(v)
                if tv not in ocache:
                    ocache[tv] = in_lattice(v, piv)
                per = ocache[tv]
                if heis is not None:
                    a_mod, coord = heis
                    (u1, v1), (u2, v2), (u3, v3) = coord[h1], coord[h2], coord[h3]
                    hp = ((-v1 + u2 + v3 - u3) % a_mod == 0)
                    if hp != per:
                        heis_disagree += 1
                key = (clsid[0][h1], clsid[1][h2], clsid[2][h3])
                inf = key_info.setdefault(key, [False, 0, 0])
                if per: inf[0] = True; inf[1] += 1
                else: inf[2] += 1
                ntrip += 1
        if time.time() - t_start > max_seconds:
            break
    # counts
    gcache = {}
    def count(key):
        S1, S2, S3 = classes[(0, key[0])], classes[(1, key[1])], classes[(2, key[2])]
        c = 0
        for a1 in S1:
            row = tab[a1]
            for a2 in S2:
                if inv[row[a2]] in S3:
                    pk = (a1, a2)
                    gg = gcache.get(pk)
                    if gg is None:
                        gg = G.generates(a1, a2); gcache[pk] = gg
                    if gg: c += 1
        return c
    key0 = (clsid[0][d1], clsid[1][d1], clsid[2][d1])
    N0 = count(key0)
    per_keys = [k for k, v in key_info.items() if v[0]]
    non_keys = [k for k, v in key_info.items() if not v[0]]
    per_counts = {}
    bad = []
    for k in per_keys:
        Nk = count(k)
        per_counts[Nk] = per_counts.get(Nk, 0) + 1
        if Nk != N0:
            bad.append((k, Nk))
    non_counts = {}
    for k in non_keys:
        Nk = count(k)
        non_counts[Nk] = non_counts.get(Nk, 0) + 1
    res = {
        "test": name, "source": "C2*C3" if modular else "free F2",
        "|E|": n, "|A|": len(A), "|D|": Dn,
        "|T1|,|T2|,|T3|": [len(T[0]), len(T[1]), len(T[2])],
        "Schreier generators": ng, "rank of [Lambda,K]-relation lattice": rank_L,
        "triples h with D-level homomorphism": ntrip,
        "triples with vanishing obstruction": sum(v[1] for v in key_info.values()),
        "reference count N0": N0,
        "distinct transported class triples (peripheral)": len(per_keys),
        "counts on peripheral class triples {count: how many}": per_counts,
        "peripheral class triples with count != N0": len(bad),
        "distinct class triples reached only with nonzero obstruction": len(non_keys),
        "counts there {count: how many}": non_counts,
        "seconds": round(time.time() - t_start, 1),
    }
    if heis is not None:
        res["Heisenberg formula disagreements with RS obstruction"] = heis_disagree
    res["PASS"] = (N0 >= 1 and not bad and (heis is None or heis_disagree == 0))
    RESULTS.append(res)
    print(json.dumps(res), flush=True)
    return res

# ---------------------------------------------------------------- constructors
def pmul(p, q):  # (p*q)(i) = p(q(i))
    return tuple(p[i] for i in q)

def mat_perm(Mx, p, pts):
    idx = {v: k for k, v in enumerate(pts)}
    a, b, c, d = Mx
    return tuple(idx[((a * v[0] + b * v[1]) % p, (c * v[0] + d * v[1]) % p)] for v in pts)

def aff_perm(Mx, tvec, p, pts):
    idx = {v: k for k, v in enumerate(pts)}
    a, b, c, d = Mx
    return tuple(idx[((a * v[0] + b * v[1] + tvec[0]) % p, (c * v[0] + d * v[1] + tvec[1]) % p)] for v in pts)

def concat(*perms):
    out = []; off = 0
    for p in perms:
        out.extend(off + i for i in p); off += len(p)
    return tuple(out)

def ident(m):
    return tuple(range(m))

def cyc(m, cycles):
    p = list(range(m))
    for c in cycles:
        for k in range(len(c)):
            p[c[k]] = c[(k + 1) % len(c)]
    return tuple(p)

V3 = [(a, b) for a in range(3) for b in range(3)]
V5 = [(a, b) for a in range(5) for b in range(5)]

def grp(gens, name):
    return FG(gens, pmul, ident(len(gens[0])), name)

def heis_coords(G, X1, X2, A, a):
    # coordinates of D = E/A = (Z/a)^2 in the basis d1 = [X1], d2 = [X2]
    tab = G.tab
    pi = {}
    for g in range(G.n):
        pi[g] = min(tab[g][x] for x in A)
    coord_by_coset = {}
    for u in range(a):
        for v in range(a):
            g = 0
            for _ in range(u): g = tab[g][X1]
            for _ in range(v): g = tab[g][X2]
            coord_by_coset[pi[g]] = (u, v)
    return pi, coord_by_coset

def heis_for_test(G, X1, X2, A, a):
    pi, cbc = heis_coords(G, X1, X2, A, a)
    Dids = sorted(set(pi.values())); dmap = {c: k for k, c in enumerate(Dids)}
    return (a, {dmap[c]: uv for c, uv in cbc.items()})

def proj_mat_group(Nmod, gens):
    def norm(Mx):
        A_ = tuple(x % Nmod for x in Mx); B_ = tuple((-x) % Nmod for x in Mx)
        return min(A_, B_)
    def mul(P, R):
        a, b, c, d = P; e, f, g, h = R
        return norm((a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h))
    return FG([norm(g) for g in gens], mul, norm((1, 0, 0, 1)), "PSL2(Z/%d)" % Nmod), norm

# ---------------------------------------------------------------- tests
which = sys.argv[1:] or ["all"]
def want(t):
    return "all" in which or t in which

S_ = (0, 1, -1, 0); R_ = (0, -1, 1, -1)

if want("F1"):  # Q8, A = centre, D = V4 (non-split projective class)
    i_ = mat_perm((0, 1, 2, 0), 3, V3); j_ = mat_perm((1, 1, 1, 2), 3, V3)
    G = grp([i_, j_], "Q8")
    X1, X2 = G.idx[i_], G.idx[j_]
    Z = {0, G.tab[X1][X1]}
    run_test("F1 Q8, A=Z(Q8), D=V4", G, X1, X2, Z, False, heis=heis_for_test(G, X1, X2, Z, 2))

if want("F2"):  # S3 x S3, A = gamma_inf = C3^2, D = V4
    t12 = cyc(3, [(0, 1)]); c123 = cyc(3, [(0, 1, 2)])
    g1 = concat(t12, c123); g2 = concat(c123, t12)
    G = grp([g1, g2], "S3xS3")
    X1, X2 = G.idx[g1], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F2 S3xS3, A=gamma_inf, D=V4", G, X1, X2, A, False, heis=heis_for_test(G, X1, X2, A, 2))

if want("F3"):  # SL2(F3): A = centre (D = A4) and A = Q8 = gamma_inf (D = C3)
    U = mat_perm((1, 1, 0, 1), 3, V3); L = mat_perm((1, 0, 1, 1), 3, V3)
    G = grp([U, L], "SL2(F3)")
    X1, X2 = G.idx[U], G.idx[L]
    Z = {g for g in range(G.n) if all(G.tab[g][h] == G.tab[h][g] for h in range(G.n))}
    run_test("F3a SL2(F3), A=centre, D=A4", G, X1, X2, Z, False)
    A = G.gamma_infty(set(range(G.n)))
    run_test("F3b SL2(F3), A=gamma_inf=Q8, D=C3", G, X1, X2, A, False)

if want("F4"):  # SL2(F3) x C3, A = gamma_inf = Q8, D = C3^2
    U = mat_perm((1, 1, 0, 1), 3, V3); L = mat_perm((1, 0, 1, 1), 3, V3)
    c = cyc(3, [(0, 1, 2)])
    g1 = concat(U, c); g2 = concat(L, ident(3))
    G = grp([g1, g2], "SL2(F3)xC3")
    X1, X2 = G.idx[g1], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F4 SL2(F3)xC3, A=gamma_inf, D=C3^2", G, X1, X2, A, False, heis=heis_for_test(G, X1, X2, A, 3))

if want("F5"):  # F3^2 : Q8, A = gamma_inf = F3^2, D = Q8 (nonabelian nilpotent)
    g1 = aff_perm((0, 1, 2, 0), (1, 0), 3, V3); g2 = aff_perm((1, 1, 1, 2), (0, 0), 3, V3)
    G = grp([g1, g2], "F3^2:Q8")
    X1, X2 = G.idx[g1], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F5 F3^2:Q8, A=gamma_inf, D=Q8", G, X1, X2, A, False)

if want("F6"):  # GL2(F3): A = centre (D = S4), A = gamma_inf = SL2(F3) (D = C2)
    U = mat_perm((1, 1, 0, 1), 3, V3); W = mat_perm((0, 1, 1, 0), 3, V3)
    G = grp([U, W], "GL2(F3)")
    X1, X2 = G.idx[U], G.idx[W]
    Z = {g for g in range(G.n) if all(G.tab[g][h] == G.tab[h][g] for h in range(G.n))}
    run_test("F6a GL2(F3), A=centre, D=S4", G, X1, X2, Z, False)
    A = G.gamma_infty(set(range(G.n)))
    run_test("F6b GL2(F3), A=gamma_inf, D=C2", G, X1, X2, A, False)

if want("F7"):  # S4 x C2, A = gamma_inf = A4, D = V4
    g1 = concat(cyc(4, [(0, 1)]), cyc(2, [(0, 1)])); g2 = concat(cyc(4, [(0, 1, 2, 3)]), ident(2))
    G = grp([g1, g2], "S4xC2")
    X1, X2 = G.idx[g1], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F7 S4xC2, A=gamma_inf, D=V4", G, X1, X2, A, False, heis=heis_for_test(G, X1, X2, A, 2))

if want("F8"):  # F5^2 : Q8 (Q8 in SL2(F5)), A = gamma_inf = F5^2, D = Q8
    # quaternion generators in SL2(F5): i = [[2,0],[0,3]] has order 4; j = [[0,1],[4,0]]
    g1 = aff_perm((2, 0, 0, 3), (1, 0), 5, V5); g2 = aff_perm((0, 1, 4, 0), (0, 0), 5, V5)
    G = grp([g1, g2], "F5^2:Q8")
    X1, X2 = G.idx[g1], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F8 F5^2:Q8, A=gamma_inf, D=Q8", G, X1, X2, A, False)

if want("F9"):  # SL2(F5), A = centre, D = A5 (Schur cover)
    Gm, norm = None, None
    def mul5(P, R):
        a, b, c, d = P; e, f, g, h = R
        return ((a * e + b * g) % 5, (a * f + b * h) % 5, (c * e + d * g) % 5, (c * f + d * h) % 5)
    G = FG([(1, 1, 0, 1), (1, 0, 1, 1)], mul5, (1, 0, 0, 1), "SL2(F5)")
    X1, X2 = G.idx[(1, 1, 0, 1)], G.idx[(1, 0, 1, 1)]
    Z = {G.idx[(1, 0, 0, 1)], G.idx[(4, 0, 0, 4)]}
    run_test("F9 SL2(F5), A=centre, D=A5", G, X1, X2, Z, False)

if want("F10"):  # S3 wr C2 on 6 points
    sw = (3, 4, 5, 0, 1, 2)
    g2 = concat(cyc(3, [(0, 1, 2)]), cyc(3, [(0, 1)]))
    G = grp([sw, g2], "S3wrC2")
    X1, X2 = G.idx[sw], G.idx[g2]
    A = G.gamma_infty(set(range(G.n)))
    run_test("F10 S3 wr C2 (order %d), A=gamma_inf" % G.n, G, X1, X2, A, False)

# modular source: images of C2*C3 retaining the S3 quotient
def modular_group(Nmod):
    G, norm = proj_mat_group(Nmod, [S_, R_])
    return G, G.idx[norm(S_)], G.idx[norm(R_)], norm

def pure_kernel(G, Nmod, norm):
    # elements congruent to +-I modulo 2 (kernel of reduction to SL2(F2) = S3)
    out = set()
    for k, Mx in enumerate(G.elems):
        if all((x - y) % 2 == 0 for x, y in zip(Mx, (1, 0, 0, 1))):
            out.add(k)
    return out

for Nmod, tag in ((6, "M1"), (10, "M2"), (14, "M3"), (12, "M4"), (18, "M5")):
    if want(tag):
        G, Xs, Xr, norm = modular_group(Nmod)
        Npure = pure_kernel(G, Nmod, norm)
        assert G.n % 6 == 0 and len(Npure) * 6 == G.n
        A = G.gamma_infty(Npure)
        run_test("%s PSL2(Z/%d) (order %d), A=gamma_inf(pure)=order %d" % (tag, Nmod, G.n, len(A)),
                 G, Xs, Xr, A, True)

if want("M6"):  # PSL2(Z/12) with A = O_2-type choices: A = whole pure kernel and A = q(H)
    G, Xs, Xr, norm = modular_group(12)
    Npure = pure_kernel(G, 12, norm)
    run_test("M6a PSL2(Z/12), A = pure kernel (D = S3)", G, Xs, Xr, Npure, True)
    # A = image of H = F'F^3
    Fl = list(Npure)
    gensH = {G.comm(a, b) for a in Fl for b in Fl} | {G.tab[G.tab[a][a]][a] for a in Fl}
    AH = G.closure(list(gensH))
    run_test("M6b PSL2(Z/12), A = q(H) (order %d)" % len(AH), G, Xs, Xr, AH, True)

print("TOTAL_SECONDS", round(time.time() - T0, 1))
print("ALL_PASS", all(r["PASS"] for r in RESULTS), "tests", len(RESULTS))

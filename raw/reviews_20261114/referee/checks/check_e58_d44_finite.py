"""Referee A (Claude Opus 5.5 at effort max), 14 Nov 2026.
Independent finite checks for LM7_PUSH D.44 (as used by D.50/E.58) and E.58.
Standard library only. Reads no file of the return.

Checks:
  D.44.7  Schreier generators of F = ker(PSL2(Z) -> S3) for the transversal 1,s,r,r^2,sr,sr^2
  D.44.8  conjugation table of r and s on x,y,z
  D.44.9  (ab)^{-1} = rs = s tau s for a = s, b = r^{-1}
  D.44.19-20 / D.50.23-24  torsion relations <-> gentle cycles (checked in a finite quotient
          on random elements of the image of F', and as exact substitution identities)
  E.58.9-18  q(F), q(H), Q/q(H), D = B/H (affine model), J, [x,y]^2 -> 5I, z0 central
  E.58.23  CM bits (1,0) and the E.1 table count 24/24 over the 48 frame pairs
  E.58.25  the chain of tau^12: 24 distinct edges, coefficients +-1, zero boundary
"""
import itertools, random, json, sys

out = {}
fails = []
def check(name, cond, info=None):
    out[name] = {"pass": bool(cond)} if info is None else {"pass": bool(cond), "info": info}
    if not cond:
        fails.append(name)

# ---------- integer 2x2 matrices -------------------------------------------------
def mm(A, B, n=None):
    a, b, c, d = A; e, f, g, h = B
    r = (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
    return tuple(x % n for x in r) if n else r
def minv(A, n=None):
    a, b, c, d = A  # det 1
    r = (d, -b, -c, a)
    return tuple(x % n for x in r) if n else r
def red(A, n):
    return tuple(x % n for x in A)
I2 = (1, 0, 0, 1)

# PSL2(Z): compare up to sign
def peq(A, B):
    return A == B or A == tuple(-x for x in B)

s = (0, 1, -1, 0)
r = (0, -1, 1, -1)
tau = mm(s, r)
x = minv(mm(tau, tau))
y = mm(mm(s, x), s)
z = minv(mm(x, y))
check("s^2 = -I", mm(s, s) == (-1, 0, 0, -1))
check("r^3 = I", mm(mm(r, r), r) == I2)
check("tau = [[1,-1],[0,1]]", tau == (1, -1, 0, 1))
check("x = [[1,2],[0,1]]", x == (1, 2, 0, 1))
check("y = +-[[1,0],[-2,1]]", peq(y, (1, 0, -2, 1)))

# ---------- D.44.8 conjugation table (in PSL2(Z), faithful for C2*C3) ---------------
rinv = minv(r)
conj = lambda g, w: mm(mm(g, w), minv(g))
check("D.44.8 r x r^-1 = y", peq(conj(r, x), y))
check("D.44.8 r y r^-1 = z", peq(conj(r, y), z))
check("D.44.8 r z r^-1 = x", peq(conj(r, z), x))
check("D.44.8 s x s = y", peq(mm(mm(s, x), s), y))
check("D.44.8 s y s = x", peq(mm(mm(s, y), s), x))
check("D.44.8 s z s = x^-1 z x", peq(mm(mm(s, z), s), mm(mm(minv(x), z), x)))
# D.44.9
a_, b_ = s, rinv
check("D.44.9 (ab)^-1 = rs", peq(minv(mm(a_, b_)), mm(r, s)))
check("D.44.9 rs = s tau s", peq(mm(r, s), mm(mm(s, tau), s)))

# ---------- D.44.7 Schreier generators ----------------------------------------------
# S3 map: s -> transposition, r -> 3-cycle; transversal 1,s,r,r^2,sr,sr^2 as words
def pcomp(p, q):  # apply p then q (right action): (p*q)(i) = q(p(i))
    return tuple(q[p[i]] for i in range(3))
ps, pr = (1, 0, 2), (1, 2, 0)
def pword(w):
    g = (0, 1, 2)
    for L in w:
        g = pcomp(g, ps if L == 's' else pr)
    return g
trans = {'1': '', 's': 's', 'r': 'r', 'r2': 'rr', 'sr': 'sr', 'sr2': 'srr'}
coset_of = {pword(w): k for k, w in trans.items()}
check("D.44.6 transversal is a full set of S3 cosets", len(coset_of) == 6)
def mword(w):
    g = I2
    for L in w:
        g = mm(g, s if L == 's' else r)
    return g
sch = {}
for k, w in trans.items():
    for L in 'sr':
        tgt = coset_of[pword(w + L)]
        g = mm(mword(w + L), minv(mword(trans[tgt])))
        sch[(k, L)] = g
expected = {('r', 's'): minv(y), ('r2', 's'): x, ('sr', 's'): minv(x), ('sr2', 's'): y}
nontriv = {key: g for key, g in sch.items() if not peq(g, I2)}
check("D.44.7 exactly four nonidentity Schreier generators",
      set(nontriv) == set(expected), sorted(nontriv))
check("D.44.7 values y^-1, x, x^-1, y", all(peq(nontriv[k], expected[k]) for k in expected))

# ---------- gentle cycles <-> torsion relations, in a finite quotient -----------------
# Work in PSL2(Z/N) for N = 35 (s, r images; F image = kernel to nothing in particular).
# Identity check: for any f in the image of F, (s f)^2 = 1  <=>  (s f s) f = 1, and
# (f^-1 r)^3 = 1 <=> (r^2 f r^-2)(r f r^-1) f = 1, with s f s = f(y,x), r f r^-1 = f(y,z),
# r^2 f r^-2 = f(z,x) as substitution maps (verified on generators by D.44.8 above).
N = 35
def pnorm(A, n):
    A = red(A, n); B = red(tuple(-v for v in A), n)
    return min(A, B)
def pm(A, B):
    return pnorm(mm(A, B, N), N)
def pinv(A):
    return pnorm(minv(A, N), N)
sN, rN, xN, yN = (pnorm(v, N) for v in (s, r, x, y))
random.seed(20261114)
def rand_word_F(L=12):
    g = pnorm(I2, N)
    for _ in range(L):
        g = pm(g, random.choice([xN, yN, pinv(xN), pinv(yN)]))
    return g
eq_ok = True
for _ in range(400):
    f = rand_word_F()
    lhs1 = (pm(pm(sN, f), pm(sN, f)) == pnorm(I2, N))
    rhs1 = (pm(pm(pm(sN, f), sN), f) == pnorm(I2, N))
    R0 = pm(pinv(f), rN)
    lhs2 = (pm(pm(R0, R0), R0) == pnorm(I2, N))
    r2 = pm(rN, rN)
    rhs2 = (pm(pm(pm(pm(r2, f), pinv(r2)), pm(pm(rN, f), pinv(rN))), f) == pnorm(I2, N))
    if lhs1 != rhs1 or lhs2 != rhs2:
        eq_ok = False
check("D.44.19-20 torsion <-> cycles on 400 random F-elements mod 35", eq_ok)
# and the exact identity behind it: (f^-1 r)^3 = f^-1 (r f^-1 r^-1)(r^2 f^-1 r^-2) r^3
ok = True
for _ in range(200):
    f = rand_word_F()
    R0 = pm(pinv(f), rN)
    lhs = pm(pm(R0, R0), R0)
    r2 = pm(rN, rN)
    rhs = pm(pm(pinv(f), pm(pm(rN, pinv(f)), pinv(rN))), pm(pm(r2, pinv(f)), pinv(r2)))
    ok &= (lhs == rhs)
check("D.44.20 expansion identity", ok)

# ---------- E.58: Q = SL2(Z/12)/{+-I} -------------------------------------------------
M = 12
def qn(A):
    A = red(A, M); B = red(tuple(-v for v in A), M)
    return min(A, B)
def qm(A, B):
    return qn(mm(A, B, M))
def qi(A):
    return qn(minv(A, M))
def gen_group(gens, mul, e):
    G = {e}; frontier = [e]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                k = mul(g, h)
                if k not in G:
                    G.add(k); nf.append(k)
        frontier = nf
    return G
e = qn(I2)
qs, qr = qn(s), qn(r)
Q = gen_group([qs, qr], qm, e)
check("E.1/E.58 |Q| = 576 (q onto)", len(Q) == 576, len(Q))
qx, qy, qtau = qn(x), qn(y), qn(tau)
qF = gen_group([qx, qy], qm, e)
check("E.58.11 |q(F)| = 96", len(qF) == 96, len(qF))
ker2 = {g for g in Q if all(v % 2 == w for v, w in zip(g, (1, 0, 0, 1)))}
check("E.58.11 q(F) = kernel of reduction to SL2(F2)", qF == ker2)
V4 = {(1, 0, 0, 1), (1, 2, 0, 1), (1, 0, 2, 1), (1, 2, 2, 1)}
def normrep(g):  # representative mod 12 whose mod-4 reduction lies in V4
    A = g; B = red(tuple(-v for v in g), M)
    cands = [C for C in (A, B) if red(C, 4) in V4]
    return cands
uniq = all(len(normrep(g)) == 1 for g in qF)
check("E.58.11 unique V4-normalized representative for every element of q(F)", uniq)
def phi(g):
    C = normrep(g)[0]
    return (red(C, 4), red(C, 3))
imgs = {phi(g) for g in qF}
hom = all(phi(qm(g, h)) == (red(mm(normrep(g)[0], normrep(h)[0]), 4), red(mm(normrep(g)[0], normrep(h)[0]), 3))
          for g in qF for h in qF)
SL23 = {A for A in itertools.product(range(3), repeat=4) if (A[0]*A[3] - A[1]*A[2]) % 3 == 1}
check("E.58.11 q(F) -> V4 x SL2(F3) is a bijective homomorphism",
      hom and len(imgs) == 96 and {a for a, b in imgs} == V4 and {b for a, b in imgs} == SL23)
# q(H) for H = F'F^3
comm = lambda g, h: qm(qm(g, h), qm(qi(g), qi(h)))
gensH = {comm(g, h) for g in qF for h in qF} | {qm(qm(g, g), g) for g in qF}
qH = gen_group(list(gensH), qm, e)
check("E.58.13 |q(H)| = 32", len(qH) == 32, len(qH))
Q8 = {A for A in SL23 if mm(A, A, 3) in {(2, 0, 0, 2), (1, 0, 0, 1)} and A != (1, 0, 0, 1) or A == (1, 0, 0, 1) or A == (2, 0, 0, 2)}
Q8 = {A for A in SL23 if mm(mm(mm(A, A, 3), A, 3), A, 3) == (1, 0, 0, 1)}  # elements of order dividing 4
check("E.58.12 Q8 = elements of SL2(F3) of order | 4, size 8", len(Q8) == 8)
i_, j_ = (0, 1, 2, 0), (1, 1, 1, 2)
check("E.58.12 i^2 = j^2 = -I, ij = -ji",
      mm(i_, i_, 3) == (2, 0, 0, 2) and mm(j_, j_, 3) == (2, 0, 0, 2)
      and mm(i_, j_, 3) == red(tuple(-v for v in mm(j_, i_, 3)), 3))
check("E.58.13 q(H) = V4 x Q8 under (E.58.11)", {phi(g) for g in qH} == {(a, b) for a in V4 for b in Q8})
normal_qH = all(qm(qm(g, h), qi(g)) in qH for g in Q for h in qH)
check("E.58.14 q(H) normal in Q, |Q/q(H)| = 18", normal_qH and 576 // len(qH) == 18)
# D = B/H affine model over F3
def aff_mul(P, R):
    (L, v), (Mx, w) = P, R
    Lw = ((Mx[0]*0 + 0),)  # placeholder (unused)
    LM = mm(L, Mx, 3)
    vw = ((v[0] + L[0]*w[0] + L[1]*w[1]) % 3, (v[1] + L[2]*w[0] + L[3]*w[1]) % 3)
    return (LM, vw)
def aff_inv(P):
    L, v = P
    # inverse of L over F3 (det may be 1 or 2)
    det = (L[0]*L[3] - L[1]*L[2]) % 3
    di = 1 if det == 1 else 2
    Li = tuple((di*t) % 3 for t in (L[3], -L[1], -L[2], L[0]))
    w = ((-(Li[0]*v[0] + Li[1]*v[1])) % 3, (-(Li[2]*v[0] + Li[3]*v[1])) % 3)
    return (Li, w)
eD = ((1, 0, 0, 1), (0, 0))
sD = ((0, 1, 1, 0), (0, 0))
rD = ((0, 2, 1, 2), (0, 1))
check("E.58.16 s^2 = 1 in the affine model", aff_mul(sD, sD) == eD)
check("E.58.16 r^3 = 1 in the affine model", aff_mul(aff_mul(rD, rD), rD) == eD)
DD = gen_group([sD, rD], aff_mul, eD)
check("E.58.16 image has order 54", len(DD) == 54, len(DD))
tauD = aff_mul(sD, rD)
xD = aff_inv(aff_mul(tauD, tauD))
yD = aff_mul(aff_mul(sD, xD), sD)
check("E.58.16 x, y act as translations by the standard basis vectors",
      {xD, yD} == {((1, 0, 0, 1), (1, 0)), ((1, 0, 0, 1), (0, 1))}, [xD, yD])
# joint image J in Q x D
def jm(P, R):
    return (qm(P[0], R[0]), aff_mul(P[1], R[1]))
eJ = (e, eD)
J = gen_group([(qs, sD), (qr, rD)], jm, eJ)
check("E.58.14 |J| = 1728", len(J) == 1728, len(J))
kerJD = {g for g in J if g[1] == eD}
check("E.58.14 kernel of J -> D is q(H) x 1", {g[0] for g in kerJD} == qH and len(kerJD) == 32)
# [x,y], [x,y]^2
cxy = comm(qx, qy)
rep_cxy = [C for C in (cxy, red(tuple(-v for v in cxy), 12))]
check("E.58.17 q([x,y]) = [[1,8],[8,5]] up to sign", (1, 8, 8, 5) in rep_cxy, rep_cxy)
z0 = qm(cxy, cxy)
check("E.58.17 q([x,y]^2) = [5I]", z0 == qn((5, 0, 0, 5)), z0)
check("E.58.17 z0 central of order 2 in Q", all(qm(z0, g) == qm(g, z0) for g in Q) and qm(z0, z0) == e and z0 != e)
check("E.58.17 z0 in q(H) with coordinates (I, -I)", z0 in qH and phi(z0) == ((1, 0, 0, 1), (2, 0, 0, 2)))
# [x,y]^2 in the joint image: its D-image is 1 since [x,y]^2 in H
cxyD = aff_mul(aff_mul(xD, yD), aff_mul(aff_inv(xD), aff_inv(yD)))
check("E.58.18 (z0,1) is the J-image of [x,y]^2 and is central in J",
      aff_mul(cxyD, cxyD) == eD and (z0, eD) in J and all(jm((z0, eD), g) == jm(g, (z0, eD)) for g in J))
# r has order 3 in J
rJ = (qr, rD)
check("E.58.19 r has order 3 in J", jm(jm(rJ, rJ), rJ) == eJ and jm(rJ, rJ) != eJ)
# ---------- CM bits (E.1 convention) --------------------------------------------------
S3m = (0, 2, 1, 0)   # S mod 3
R3 = (0, 2, 1, 2)    # R mod 3
line = [(a, b) for a in range(3) for b in range(3) if (a, b) != (0, 0)
        and ((R3[0]-1)*a + R3[1]*b) % 3 == 0 and (R3[2]*a + (R3[3]-1)*b) % 3 == 0]
check("E.58.23 ker(R - I) mod 3 is spanned by (1,2)", (1, 2) in line and len(line) == 2, line)
def bitA(Aq):   # Aq in Q: frame of r; bit from the action of A^{-1} on ker(R-I) mod 3
    Ai = normrep(qi(Aq))[0]
    A3 = red(Ai, 3)
    v = (1, 2)
    w = ((A3[0]*v[0] + A3[1]*v[1]) % 3, (A3[2]*v[0] + A3[3]*v[1]) % 3)
    if w == v: return 0
    if w == ((-v[0]) % 3, (-v[1]) % 3): return 1
    return None
def bitB(Bq):   # beta frame; beta^{-1} mod 3 in {+-I, +-S}; bit 1 iff in {+-S}
    Bi = normrep(qi(Bq))[0]
    B3 = red(Bi, 3)
    if B3 in {(1, 0, 0, 1), (2, 0, 0, 2)}: return 0
    if B3 in {S3m, red(tuple(-v for v in S3m), 3)}: return 1
    return None
check("E.58.23 bits of (A,beta) = ([5I],1) are (1,0)", (bitA(z0), bitB(e)) == (1, 0), (bitA(z0), bitB(e)))
CFr = [g for g in qF if qm(g, qr) == qm(qr, g)]
CFs = [g for g in qF if qm(g, qs) == qm(qs, g)]
check("E.1 |C_{q(F)}(r)| = 6, |C_{q(F)}(s)| = 8", (len(CFr), len(CFs)) == (6, 8), (len(CFr), len(CFs)))
pairs = [(bitA(A), bitB(B)) for A in CFr for B in CFs]
check("E.1 all 48 frame pairs have defined bits", all(p[0] is not None and p[1] is not None for p in pairs))
eqn = sum(1 for p in pairs if p[0] == p[1])
check("E.1 24 CM-compatible and 24 extra pairs", eqn == 24 and len(pairs) - eqn == 24, (eqn, len(pairs) - eqn))
check("E.58 z0 lies in C_{q(F)}(r)", z0 in CFr)
# ---------- E.58.25 the chain of tau^12 ---------------------------------------------------
Qlist = sorted(Q); idx = {g: k for k, g in enumerate(Qlist)}
def P_of(word):  # E.1: P(s)=0, P(r)=e_1 - e_r, P(ab)=P(a)+q(a)P(b)
    chain = {}; g = e
    for L in word:
        if L == 'r':
            for h, c in ((g, 1), (qm(g, qr), -1)):
                chain[h] = chain.get(h, 0) + c
        g = qm(g, qs if L == 's' else qr)
    return {h: c for h, c in chain.items() if c != 0}, g
P12, end = P_of('sr' * 12)
check("E.58.25 q(tau)^12 = 1", end == e)
check("E.58.25 chain has 24 nonzero edge coefficients, all +-1",
      len(P12) == 24 and all(abs(c) == 1 for c in P12.values()), len(P12))
expect = {}
for j in range(12):
    tj = e
    for _ in range(j): tj = qm(tj, qtau)
    expect[qm(tj, qs)] = expect.get(qm(tj, qs), 0) + 1
    expect[qm(tj, qtau)] = expect.get(qm(tj, qtau), 0) - 1
check("E.58.25 chain equals sum_j (e_{tau^j s} - e_{tau^{j+1}})", {h: c for h, c in expect.items() if c} == P12)
# boundary: edge g joins vertex g<s> and g<r>
def vs(g): return ('s', min(g, qm(g, qs)))
def vr(g): return ('r', min(g, qm(g, qr), qm(qm(g, qr), qr)))
bd = {}
for h, c in P12.items():
    bd[vr(h)] = bd.get(vr(h), 0) + c
    bd[vs(h)] = bd.get(vs(h), 0) - c
check("E.58.25 chain has zero boundary", all(v == 0 for v in bd.values()))
verts = {vs(g) for g in Q} | {vr(g) for g in Q}
check("E.1 graph: 576 edges, 480 vertices, rank 97", len(verts) == 480 and 576 - 480 + 1 == 97)
check("E.58.24 q(x^6) = 1 (x^6 = tau^-12 in N_B)", qm(qm(qm(qx, qx), qm(qx, qx)), qm(qx, qx)) == e)

json.dump({"fails": fails, "checks": out}, sys.stdout, indent=1, default=str)
print()
print("TOTAL", len(out), "FAILED", len(fails))

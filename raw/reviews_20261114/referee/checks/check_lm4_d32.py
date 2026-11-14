"""Referee A (Claude Opus 5.5 at effort max), 14 Nov 2026.
Independent finite checks for LM4 D.32 (and the parts of D.28 it uses).
Standard library only; reads no file of the return.

1. Finite covers of the pants (D.32, lines 31270-31311): for transitive actions of
   F(x,y) of degree n (exhaustive for n <= 5, random samples for 6 <= n <= 9) and every
   prime p | n, compute H_1(U, F_p) of the cover via Reidemeister-Schreier, the classes of all
   boundary loops (orbits of x, y and c3 = (xy)^-1), and check:
     (a) dim H_1(U,F_p) = n + 1;
     (b) the boundary classes span a space of dimension b - 1 and sum to zero
         (the only relation is their sum);
     (c) whenever each c_i has an orbit of length prime to p, there are b >= 4 boundaries and
         every such choice of three classes (one over each c_i) is linearly independent.
2. D.28h: u in Z^ with u_7 the cube root of unity = 2 mod 7 and u_q = 1 otherwise has
   u = 9 mod 14; in D_7 with x -> s, y -> sr: x^u y^u -> r, (xy)^u -> r^2, not conjugate.
3. The appended source check of Lochak-Schneps Lemma 9: central coordinate of
   x^n (xy)^-n y^n in the integral Heisenberg group is -n(n+1)/2; the dihedral evaluation
   forces n_q = n_2-sign globally (checked for q = 3,5,7,11,13 on all residues).
"""
import itertools, random, sys, json

random.seed(32)
results = {}
fails = []
def check(name, cond, info=None):
    results[name] = {"pass": bool(cond), "info": info}
    if not cond:
        fails.append(name)

# ------------------------------------------------------------------ covers
def rank_mod_p(vecs, p):
    rows = [list(v) for v in vecs]
    r = 0
    ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] % p:
                piv = i; break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][c], p - 2, p)
        rows[r] = [(a * inv) % p for a in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] % p:
                f = rows[i][c]
                rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        r += 1
    return r

def analyse(sx, sy, n):
    # right action of letters on cosets 0..n-1; letter 0 = x, 1 = y
    perm = [sx, sy]
    inv = [[0] * n, [0] * n]
    for l in (0, 1):
        for k in range(n):
            inv[l][perm[l][k]] = k
    def act(k, l, e):
        return perm[l][k] if e == 1 else inv[l][k]
    t = {0: []}
    order = [0]
    for k in order:
        for l in (0, 1):
            for e in (1, -1):
                k2 = act(k, l, e)
                if k2 not in t:
                    t[k2] = t[k] + [(l, e)]
                    order.append(k2)
    if len(t) != n:
        return None  # not transitive
    gid = {}
    ng = 0
    for k in range(n):
        for l in (0, 1):
            k2 = act(k, l, 1)
            if t[k2] == t[k] + [(l, 1)] or t[k] == t[k2] + [(l, -1)]:
                gid[(k, l)] = None
            else:
                gid[(k, l)] = ng; ng += 1
    def rewrite(w):
        v = [0] * ng; k = 0
        for (l, e) in w:
            if e == 1:
                g = gid[(k, l)]
                if g is not None: v[g] += 1
                k = act(k, l, 1)
            else:
                k2 = act(k, l, -1)
                g = gid[(k2, l)]
                if g is not None: v[g] -= 1
                k = k2
        return v, k
    def winv(w):
        return [(l, -e) for (l, e) in reversed(w)]
    cwords = [[(0, 1)], [(1, 1)], [(1, -1), (0, -1)]]  # x, y, (xy)^-1
    def cperm(i, k):
        for (l, e) in cwords[i]:
            k = act(k, l, e)
        return k
    boundaries = []  # (i, length, vector)
    for i in range(3):
        seen = set()
        for k0 in range(n):
            if k0 in seen: continue
            orb = [k0]; k = cperm(i, k0)
            while k != k0:
                orb.append(k); k = cperm(i, k)
            seen.update(orb)
            d = len(orb)
            w = t[k0] + cwords[i] * d + winv(t[k0])
            v, kend = rewrite(w)
            assert kend == 0
            boundaries.append((i, d, v))
    return ng, boundaries

stats = defaultdict_dummy = None
from collections import defaultdict
summary = defaultdict(lambda: defaultdict(int))
bad = []
def test_pair(sx, sy, n):
    res = analyse(sx, sy, n)
    if res is None:
        return False
    ng, bnds = res
    for p in (2, 3, 5, 7):
        if n % p:
            continue
        key = "n=%d,p=%d" % (n, p)
        summary[key]["covers"] += 1
        if ng != n + 1:
            bad.append((key, "rank", sx, sy)); continue
        vecs = [b[2] for b in bnds]
        b = len(bnds)
        rk = rank_mod_p(vecs, p)
        tot = [sum(col) % p for col in zip(*vecs)]
        if rk != b - 1 or any(tot):
            bad.append((key, "boundary relation", sx, sy, rk, b)); continue
        choices = [[bb for bb in bnds if bb[0] == i and bb[1] % p] for i in range(3)]
        if all(choices):
            summary[key]["covers with a prime-to-p orbit over every cusp"] += 1
            if b < 4:
                bad.append((key, "fewer than four boundaries", sx, sy)); continue
            for trip in itertools.product(*choices):
                summary[key]["selections tested"] += 1
                if rank_mod_p([trip[0][2], trip[1][2], trip[2][2]], p) != 3:
                    bad.append((key, "dependent selection", sx, sy)); break
    return True

for n in range(1, 6):
    perms = list(itertools.permutations(range(n)))
    for sx in perms:
        for sy in perms:
            test_pair(list(sx), list(sy), n)
for n in range(6, 10):
    cnt = 0
    tries = 0
    while cnt < 3000 and tries < 200000:
        tries += 1
        sx = list(range(n)); random.shuffle(sx)
        sy = list(range(n)); random.shuffle(sy)
        if test_pair(sx, sy, n):
            cnt += 1
check("D.32 finite covers: rank n+1, single boundary relation, b>=4 and independent selections",
      not bad, {"summary": {k: dict(v) for k, v in summary.items()}, "first failures": bad[:5]})

# ------------------------------------------------------------------ D.28h
# u_7: Hensel lift of the cube root of unity congruent to 2 mod 7 (check modulo 7^6)
m = 7 ** 6
u7 = 2
for _ in range(10):
    # Newton for u^2 + u + 1 = 0
    f = (u7 * u7 + u7 + 1) % m
    df = (2 * u7 + 1) % m
    u7 = (u7 - f * pow(df, -1, m)) % m
check("D.28h u_7 is a primitive cube root of unity mod 7^6, = 2 mod 7",
      pow(u7, 3, m) == 1 and u7 % 7 == 2 and u7 != 1)
u_mod14 = next(v for v in range(14) if v % 2 == 1 and v % 7 == 2)
check("D.28h u = 9 mod 14", u_mod14 == 9)
# D_7 as pairs (a, e) meaning r^a s^e, with s r s = r^-1
def dmul(g, h):
    a, e = g; b, f = h
    return ((a + (b if e == 0 else -b)) % 7, (e + f) % 2)
def dpow(g, k):
    out = (0, 0)
    for _ in range(k % 14):
        out = dmul(out, g)
    return out
s_, r_ = (0, 1), (1, 0)
X, Y = s_, dmul(s_, r_)
lhs = dmul(dpow(X, 9), dpow(Y, 9))
rhs = dpow(dmul(X, Y), 9)
cls_r = {(1, 0), (6, 0)}
check("D.28h x^u y^u -> r, (xy)^u -> r^2, not conjugate in D7",
      lhs == (1, 0) and rhs == (2, 0) and rhs not in cls_r, [lhs, rhs])

# ------------------------------------------------------------------ LS.1 source check
def hmul(g, h):
    return (g[0] + h[0], g[1] + h[1], g[2] + h[2] + g[0] * h[1])
def hinv(g):
    return (-g[0], -g[1], -g[2] + g[0] * g[1])
def hpow(g, k):
    out = (0, 0, 0)
    base = g if k >= 0 else hinv(g)
    for _ in range(abs(k)):
        out = hmul(out, base)
    return out
ok = True
for nn in range(-12, 13):
    x_, y_ = (1, 0, 0), (0, 1, 0)
    w = hmul(hmul(hpow(x_, nn), hpow(hmul(x_, y_), -nn)), hpow(y_, nn))
    if w != (0, 0, -nn * (nn + 1) // 2):
        ok = False
check("LS.1 central coordinate of x^n (xy)^-n y^n is -n(n+1)/2", ok)
ok = True
for q in (3, 5, 7, 11, 13):
    def qmul(g, h):
        a, e = g; b, f = h
        return ((a + (b if e == 0 else -b)) % q, (e + f) % 2)
    def qpow(g, k):
        out = (0, 0)
        for _ in range(k % (2 * q)):
            out = qmul(out, g)
        return out
    sq, rq = (0, 1), (1, 0)
    xq, yq = sq, rq
    for n2 in (0, 1):          # parity of n (2-adic class mod 2)
        for nq in range(q):    # n mod q
            nmod = next(v for v in range(2 * q) if v % 2 == n2 and v % q == nq)
            w = qmul(qmul(qpow(xq, nmod), qpow(qmul(xq, yq), (-nmod) % (2 * q))), qpow(yq, nmod))
            holds = (w == (0, 0))
            predicted = (n2 == 0 and nq == 0) or (n2 == 1 and nq == q - 1)
            if holds != predicted:
                ok = False
check("LS.1 dihedral evaluation: relation holds iff (n even and n=0 mod q) or (n odd and n=-1 mod q)", ok)

json.dump({"fails": fails, "checks": results}, sys.stdout, indent=1, default=str)
print()
print("TOTAL", len(results), "FAILED", len(fails))

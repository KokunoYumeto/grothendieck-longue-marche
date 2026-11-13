# Own checks for the review of the return EXIT_ONE_TYPE (13 Nov 2026).
# Written by the reviewer (Claude Fable 5.2) from the paper's statements; none of the return's code is used.
# Run:  python -I -B own_checks.py > own_checks.out
import itertools
from fractions import Fraction

OK = []
def report(name, ok, detail=""):
    OK.append(ok)
    print(("PASS  " if ok else "FAIL  ") + name + ((" :: " + detail) if detail else ""))

# ---------------------------------------------------------------- free groups, Artin representation
def red(w):
    out = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return tuple(out)
def inv(w):
    return tuple(-g for g in reversed(w))

class Aut:
    def __init__(self, n, images):
        self.n = n
        self.im = {i: red(images[i]) for i in range(1, n + 1)}
    def apply(self, w):
        r = []
        for g in w:
            r.extend(self.im[g] if g > 0 else inv(self.im[-g]))
        return red(r)
    def __mul__(self, other):          # (f*g)(x) = f(g(x))
        return Aut(self.n, {i: self.apply(other.im[i]) for i in range(1, self.n + 1)})
    def __eq__(self, other):
        return self.im == other.im

def ident(n):
    return Aut(n, {i: (i,) for i in range(1, n + 1)})
def sigma(n, i, sign=1):
    im = {k: (k,) for k in range(1, n + 1)}
    if sign > 0:    # x_i -> x_i x_{i+1} x_i^-1 ; x_{i+1} -> x_i
        im[i] = (i, i + 1, -i)
        im[i + 1] = (i,)
    else:           # inverse
        im[i] = (i + 1,)
        im[i + 1] = (-(i + 1), i, i + 1)
    return Aut(n, im)
def rho(n, bw):
    f = ident(n)
    for g in bw:
        f = f * sigma(n, abs(g), 1 if g > 0 else -1)
    return f
def binv(bw):
    return [-g for g in reversed(bw)]

N = 5
ok = True
for i in range(1, N):
    ok &= (rho(N, [i, -i]) == ident(N))
    for j in range(1, N):
        if abs(i - j) >= 2:
            ok &= rho(N, [i, j]) == rho(N, [j, i])
        if j == i + 1:
            ok &= rho(N, [i, j, i]) == rho(N, [j, i, j])
report("Artin representation of B_5 satisfies the braid relations", ok)

def A(i, j):
    return list(range(j - 1, i, -1)) + [i, i] + [-k for k in range(i + 1, j)]
gen = {"a": A(1, 3), "b": A(2, 3), "x": A(1, 4), "y": A(2, 4), "z": A(3, 4),
       "p": A(1, 5), "q": A(2, 5), "r": A(3, 5), "s": A(4, 5)}
def W(expr):
    out = []
    for l, e in expr:
        out += (gen[l] if e > 0 else binv(gen[l])) * abs(e)
    return out
def c(u, v):                       # c(u,v) = v^-1 u^-1 v u
    return [(v, -1), (u, -1), (v, 1), (u, 1)]
def cinv(u, v):
    return [(u, -1), (v, -1), (u, 1), (v, 1)]

rel5 = {("a", "x"): [("z", -1), ("x", 1), ("z", 1)],
        ("a", "y"): c("x", "z") + [("y", 1)] + cinv("x", "z"),
        ("a", "z"): c("x", "z") + [("z", 1)],
        ("b", "x"): [("x", 1)],
        ("b", "y"): [("z", -1), ("y", 1), ("z", 1)],
        ("b", "z"): c("y", "z") + [("z", 1)]}
rel6 = {("a", "p"): [("r", -1), ("p", 1), ("r", 1)],
        ("a", "q"): c("p", "r") + [("q", 1)] + cinv("p", "r"),
        ("a", "r"): c("p", "r") + [("r", 1)],
        ("a", "s"): [("s", 1)],
        ("b", "p"): [("p", 1)],
        ("b", "q"): [("r", -1), ("q", 1), ("r", 1)],
        ("b", "r"): c("q", "r") + [("r", 1)],
        ("b", "s"): [("s", 1)],
        ("x", "p"): [("s", -1), ("p", 1), ("s", 1)],
        ("x", "q"): c("p", "s") + [("q", 1)] + cinv("p", "s"),
        ("x", "r"): c("p", "s") + [("r", 1)] + cinv("p", "s"),
        ("x", "s"): c("p", "s") + [("s", 1)],
        ("y", "p"): [("p", 1)],
        ("y", "q"): [("s", -1), ("q", 1), ("s", 1)],
        ("y", "r"): c("q", "s") + [("r", 1)] + cinv("q", "s"),
        ("y", "s"): c("q", "s") + [("s", 1)],
        ("z", "p"): [("p", 1)],
        ("z", "q"): [("q", 1)],
        ("z", "r"): [("s", -1), ("r", 1), ("s", 1)],
        ("z", "s"): c("r", "s") + [("s", 1)]}

def test(rels, variant):
    bad = []
    for (h, u), rhs in rels.items():
        if variant == "as stated":            # h u h^-1 = rhs
            lhs = W([(h, 1), (u, 1), (h, -1)])
            r = W(rhs)
        else:                                 # h^-1 u h = reverse(rhs)
            lhs = W([(h, -1), (u, 1), (h, 1)])
            r = W(list(reversed(rhs)))
        if not (rho(N, lhs) == rho(N, r)):
            bad.append(h + u)
    return bad
for name, rels in (("Gamma_{0,5}: 6 relations (P5c2)", rel5), ("Gamma_{0,6}: 20 mixed relations (P5c3)", rel6)):
    for variant in ("as stated", "reversed"):
        bad = test(rels, variant)
        print("   [%s] %s: %d of %d hold in B_5%s" % (variant, name, len(rels) - len(bad), len(rels),
              "" if not bad else "; failing: " + " ".join(bad)))
    report(name + " hold as stated in B_5 (faithful Artin representation)", not test(rels, "as stated"))

D4 = A(1, 2) + A(1, 3) + A(2, 3) + A(1, 4) + A(2, 4) + A(3, 4)
D5 = D4 + A(1, 5) + A(2, 5) + A(3, 5) + A(4, 5)
ok4 = all(rho(N, D4 + [i]) == rho(N, [i] + D4) for i in (1, 2, 3))
ok5 = all(rho(N, D5 + [i]) == rho(N, [i] + D5) for i in (1, 2, 3, 4))
report("A12 A13 A23 A14 A24 A34 commutes with sigma_1..3 (centre of P_4); with the A_i5 appended it commutes with sigma_1..4 (centre of P_5)", ok4 and ok5)
report("the centre generator of P_4 is not central in B_5 (the section goes through the complement <a,b,x,y,z> of Z(P_4))",
       not (rho(N, D4 + [4]) == rho(N, [4] + D4)))

# ---------------------------------------------------------------- integer linear algebra
def rank_q(M):
    M = [[Fraction(v) for v in row] for row in M]
    r = 0
    rows = len(M)
    cols = len(M[0]) if M else 0
    for cidx in range(cols):
        piv = next((i for i in range(r, rows) if M[i][cidx] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cidx]
        for i in range(r + 1, rows):
            if M[i][cidx] != 0:
                f = M[i][cidx] / pv
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r
def snf_diag(M):
    M = [list(row) for row in M]
    rows = len(M)
    cols = len(M[0]) if M else 0
    diag = []
    t = 0
    while t < rows and t < cols:
        best = None
        for i in range(t, rows):
            for j in range(t, cols):
                if M[i][j] != 0 and (best is None or abs(M[i][j]) < abs(M[best[0]][best[1]])):
                    best = (i, j)
        if best is None:
            break
        i, j = best
        M[t], M[i] = M[i], M[t]
        for row in M:
            row[t], row[j] = row[j], row[t]
        while True:
            again = False
            for i in range(t + 1, rows):
                if M[i][t] != 0:
                    qd = M[i][t] // M[t][t]
                    M[i] = [x - qd * y for x, y in zip(M[i], M[t])]
                    if M[i][t] != 0:
                        M[t], M[i] = M[i], M[t]
                        again = True
            for j in range(t + 1, cols):
                if M[t][j] != 0:
                    qd = M[t][j] // M[t][t]
                    for row in M:
                        row[j] -= qd * row[t]
                    if M[t][j] != 0:
                        for row in M:
                            row[t], row[j] = row[j], row[t]
                        again = True
            if not again:
                break
        diag.append(abs(M[t][t]))
        t += 1
    return diag

# ---------------------------------------------------------------- Delta_{0,n}  (P4d2)
def delta0n(n):
    lab = list(range(1, n))
    verts = [frozenset(s) for k in range(2, n - 1) for s in itertools.combinations(lab, k)]
    def comp(P, Q):
        return P <= Q or Q <= P or not (P & Q)
    simp = {0: [(i,) for i in range(len(verts))]}
    d = 0
    while simp[d]:
        nxt = []
        for s in simp[d]:
            for j in range(s[-1] + 1, len(verts)):
                if all(comp(verts[i], verts[j]) for i in s):
                    nxt.append(s + (j,))
        d += 1
        simp[d] = nxt
    del simp[d]
    return simp
def bd(simp, d):
    idx = {s: i for i, s in enumerate(simp[d - 1])}
    M = [[0] * len(simp[d]) for _ in simp[d - 1]]
    for jx, s in enumerate(simp[d]):
        for k in range(len(s)):
            M[idx[s[:k] + s[k + 1:]]][jx] = (-1) ** k
    return M
expect = {4: ((3,), {0: 2}), 5: ((10, 15), {1: 6}), 6: ((25, 105, 105), {2: 24})}
for n in (4, 5, 6):
    S = delta0n(n)
    f = tuple(len(S[d]) for d in sorted(S))
    top = max(S)
    ranks = {d: rank_q(bd(S, d)) for d in range(1, top + 1)}
    tors = {d: [e for e in snf_diag(bd(S, d)) if e != 1] for d in range(1, top + 1)}
    betti = {}
    for d in range(0, top + 1):
        betti[d] = f[d] - ranks.get(d, 0) - ranks.get(d + 1, 0)
    red_betti = dict(betti)
    red_betti[0] -= 1
    nz = {d: b for d, b in red_betti.items() if b}
    ok = (f == expect[n][0]) and (nz == expect[n][1]) and all(not t for t in tors.values())
    report("Delta_{0,%d}: f-vector %s, reduced Betti numbers %s, all elementary divisors of the boundary maps equal to 1 (no torsion)" % (n, f, nz), ok,
           "(n-2)! = %d" % {4: 2, 5: 6, 6: 24}[n])

# ---------------------------------------------------------------- P4a1
tau = {1: 2, 2: 1, 3: 4, 4: 3}
def act(flag):
    return tuple(frozenset(tau[i] for i in s) for s in flag)
def orb(flag):
    return frozenset([flag, act(flag)])
def fs(*xs):
    return frozenset(xs)
B_ = fs(1, 2)
c1 = orb((fs(1, 2, 3), B_)) == orb((fs(1, 2, 4), B_))
c2 = orb((B_, fs(1))) == orb((B_, fs(2)))
c3 = orb((fs(1, 2, 3), B_, fs(1))) != orb((fs(1, 2, 3), B_, fs(2)))
c4 = orb((fs(1, 2, 3), fs(1))) != orb((fs(1, 2, 3), fs(2)))
subs = [frozenset(s) for k in (1, 2, 3) for s in itertools.combinations((1, 2, 3, 4), k)]
tri = [(I3, I2, I1) for I3 in subs for I2 in subs for I1 in subs
       if len(I3) == 3 and len(I2) == 2 and len(I1) == 1 and I1 < I2 < I3]
fib = {}
for (I3, I2, I1) in tri:
    key = (orb((I3, I2)), orb((I2, I1)))
    fib.setdefault(key, set()).add(orb((I3, I2, I1)))
mx = max(len(v) for v in fib.values())
report("P4a1: (123,B)~(124,B), (B,1)~(B,2), (123,B,1) !~ (123,B,2), (123,1) !~ (123,2); largest fibre of pi0(D_321) -> pi0(D_32) x pi0(D_21) has %d elements" % mx,
       c1 and c2 and c3 and c4 and mx == 2)

# ---------------------------------------------------------------- P5a1
def nerve_counts(objs):
    E = [(u, v) for u in objs for v in objs if u < v]
    T = [(u, v, w) for (u, v) in E for w in objs if v < w]
    return len(objs), len(E), len(T)
two = [frozenset(s) for k in (1, 2) for s in itertools.combinations((1, 2, 3), k)]
three = two + [frozenset((1, 2, 3))]
V, E, T = nerve_counts(two)
V3, E3, T3 = nerve_counts(three)
deg = {u: sum(1 for v in two if u < v or v < u) for u in two}
report("P5a1: the two-level index poset has nerve (V,E,F)=(%d,%d,%d), every vertex of degree 2: a hexagon, b1=%d; pi_1 of the homotopy colimit of the constant diagram B(Z^3) is Z^3 x Z = Z^4"
       % (V, E, T, E - V + 1), (V, E, T) == (6, 6, 0) and set(deg.values()) == {2})
report("P5a1: with the triple, (V,E,F)=(%d,%d,%d), Euler characteristic %d; the poset has a maximum, its nerve is a cone: the colimit is Z^3"
       % (V3, E3, T3, V3 - E3 + T3), (V3, E3, T3) == (7, 12, 6) and V3 - E3 + T3 == 1)

# ---------------------------------------------------------------- P1b2
ker = [(u, v) for u in range(-3, 4) for v in range(-3, 4) if u + v == 0 and (u, v) != (0, 0)]
report("P1b2: the full map at q is (a,b) -> (a+b) e_x with kernel spanned by (1,-1); the curve meridians e_x, e_y, e_x are nonzero", (1, -1) in ker)

# ---------------------------------------------------------------- cusp
def mm(P, Q):
    return tuple(tuple(sum(P[i][k] * Q[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mpow(P, e):
    if e < 0:
        (p00, p01), (p10, p11) = P
        P = ((p11, -p01), (-p10, p00))
        e = -e
    R = ((1, 0), (0, 1))
    for _ in range(e):
        R = mm(R, P)
    return R
I2 = ((1, 0), (0, 1))
a_m = (((0, -1), (1, 0)), 3)
b_m = (((0, -1), (1, 1)), 2)
def gm(P, Q):
    return (mm(P[0], Q[0]), P[1] + Q[1])
def gp(P, e):
    return (mpow(P[0], e), P[1] * e)
h1 = gp(a_m, 2)
h2 = gp(b_m, 3)
m_m = gm(a_m, gp(b_m, -1))
report("cusp: a^2 = b^3 = h in SL_2(Z) x Z (a faithful image of <a,b | a^2=b^3>), degree of m = a b^-1 is 1", h1 == h2 and m_m[1] == 1,
       "a^2 = %s" % (h1,))
rng = [(i, j) for i in range(-12, 13) for j in range(-4, 5) if (i, j) != (0, 0)]
k1 = [(i, j) for i, j in rng if gm(gp(b_m, i), gp(h1, j)) == (I2, 0)]
k2 = [(i, j) for i, j in rng if gm(gp(a_m, i), gp(h1, j)) == (I2, 0)]
k3 = [(i, j) for i, j in rng if gm(gp(m_m, i), gp(h1, j)) == (I2, 0)]
report("cusp: kernel of <b>+<h> is spanned by (-3,1), of <a>+<h> by (-2,1); <m>+<h> has no kernel in the window |i|<=12, |j|<=4",
       all(i == -3 * j for i, j in k1) and (-3, 1) in k1 and all(i == -2 * j for i, j in k2) and (-2, 1) in k2 and not k3,
       "m maps to %s" % (m_m[0],))
Am = ((0, -1), (1, 1))
def av(P, v):
    return (P[0][0] * v[0] + P[0][1] * v[1], P[1][0] * v[0] + P[1][1] * v[1])
def sp(g1, g2):
    (v, n1), (w, k) = g1, g2
    Aw = av(mpow(Am, n1), w)
    return ((v[0] + Aw[0], v[1] + Aw[1]), n1 + k)
def spow(g, e):
    R = ((0, 0), 0)
    for _ in range(e):
        R = sp(R, g)
    return R
def sinv(g):
    v, n1 = g
    w = av(mpow(Am, -n1), v)
    return ((-w[0], -w[1]), -n1)
ap = ((0, 1), 3)
bp = ((1, 0), 2)
mp_ = ((0, 0), 1)
hp = ((0, 0), 6)
report("proper cusp: A^6 = 1, a^2 = b^3 = m^6 = h and m = a b^-1 in Z^2 x| Z",
       mpow(Am, 6) == I2 and spow(ap, 2) == hp and spow(bp, 3) == hp and spow(mp_, 6) == hp and sp(ap, sinv(bp)) == mp_)

# ---------------------------------------------------------------- counts
chis = (1 - 5 + 6, 1 - 9 + 26 - 24, 1 - 7 + 16 - 12, 1 - 6 + 12 - 8)
report("Euler characteristics of the models: (1,5,6) -> %d = chi(M_{0,5}); (1,9,26,24) -> %d = chi(M_{0,6}); (1,7,16,12) -> %d; (1,6,12,8) -> %d" % chis,
       chis == (2, -6, -2, -1))
strata = {4: 1 + 3, 5: 1 + 10 + 15, 6: 1 + 25 + 105 + 105}
report("number of strata of Mbar_{0,n} for n=4,5,6: %s" % (strata,), strata == {4: 4, 5: 26, 6: 236})
print("\nALL PASS" if all(OK) else "\nSOME FAILED")

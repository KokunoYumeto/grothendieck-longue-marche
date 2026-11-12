# check_lm2.py -- own checks for the review of the LM2_LOOP_EQUATIONS return.
# Written by Claude (Fable 5.2, Anthropic), 12 November 2026, from the statements of the return; none of its code was run.
# Standard library only; exact arithmetic (Fraction). The Lie-algebra core is that of check_lm3.py.
import itertools, sys
from fractions import Fraction
# non-commutative polynomials: dict word(tuple) -> Fraction
def padd(p, q, c=1):
    r = dict(p)
    for w, x in q.items():
        y = r.get(w, 0) + c*x
        if y: r[w] = y
        else: r.pop(w, None)
    return r
def pmul(p, q):
    r = {}
    for w1, x in p.items():
        for w2, y in q.items():
            w = w1 + w2; z = r.get(w, 0) + x*y
            if z: r[w] = z
            else: r.pop(w, None)
    return r
def br(p, q): return padd(pmul(p, q), pmul(q, p), -1)
def gen(i): return {(i,): Fraction(1)}

def lyndon_words(r, n):
    res = []
    for w in itertools.product(range(r), repeat=n):
        if all(w < w[i:] + w[:i] for i in range(1, n)): res.append(w)
    return res
_lb = {}
def lyndon_bracket(w):
    if w in _lb: return _lb[w]
    if len(w) == 1: p = gen(w[0])
    else:
        # standard factorization: longest proper Lyndon suffix
        for i in range(1, len(w)):
            v = w[i:]
            if all(v < v[j:] + v[:j] for j in range(1, len(v))): break
        p = br(lyndon_bracket(w[:i]), lyndon_bracket(v))
    _lb[w] = p; return p

class Lie:
    """free Lie algebra on r generators, degree by degree, coordinates = coefficients on Lyndon words"""
    def __init__(self, r): self.r = r; self.words = {}; self.basis = {}
    def W(self, n):
        if n not in self.words: self.words[n] = lyndon_words(self.r, n)
        return self.words[n]
    def B(self, n):
        if n not in self.basis: self.basis[n] = [lyndon_bracket(w) for w in self.W(n)]
        return self.basis[n]
    def dim(self, n): return len(self.W(n))
    def coords(self, p, n):   # injective on Lie_n (triangularity of the Lyndon basis)
        return [p.get(w, Fraction(0)) for w in self.W(n)]

# exact linear algebra on lists of Fractions
def rref(rows):
    rows = [list(r) for r in rows if any(r)]
    piv = []; i = 0
    ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        k = next((j for j in range(i, len(rows)) if rows[j][c]), None)
        if k is None: continue
        rows[i], rows[k] = rows[k], rows[i]
        x = rows[i][c]; rows[i] = [y / x for y in rows[i]]
        for j in range(len(rows)):
            if j != i and rows[j][c]:
                f = rows[j][c]; rows[j] = [y - f*z for y, z in zip(rows[j], rows[i])]
        piv.append(c); i += 1
        if i == len(rows): break
    return rows[:i], piv
def rank(rows): return len(rref(rows)[0]) if rows else 0
def nullspace(M, ncol):
    """vectors v with M v = 0; M is a list of rows of length ncol"""
    R, piv = rref(M) if M else ([], [])
    free = [c for c in range(ncol) if c not in piv]; res = []
    for f in free:
        v = [Fraction(0)]*ncol; v[f] = Fraction(1)
        for row, p in zip(R, piv): v[p] = -row[f]
        res.append(v)
    return res

def subst(p, images):
    """algebra homomorphism: generator i -> images[i] (a polynomial, possibly {} )"""
    r = {}
    for w, x in p.items():
        q = {(): x}
        for i in w:
            q = pmul(q, images[i])
            if not q: break
        r = padd(r, q)
    return r
def derive(p, vals):
    """derivation with D(gen i) = vals[i], applied to p"""
    r = {}
    for w, x in p.items():
        for k, i in enumerate(w):
            q = pmul(pmul({w[:k]: x}, vals[i]), {w[k+1:]: Fraction(1)})
            r = padd(r, q)
    return r


# ----------------------------------------------------------------------------- checks for the LM2 review
out = []
def P(*a):
    s = " ".join(str(x) for x in a); out.append(s); print(s)

L = Lie(2)
X, Y = gen(0), gen(1)
Z = {(0,): Fraction(-1), (1,): Fraction(-1)}
def ev(p, a, b): return subst(p, [a, b])
def vec(p, n): return L.coords(p, n)

P("== graded spaces (x, y; z = -x-y); exact rational arithmetic ==")
P(" n  l_n  raw 2-/3-cycle  special (antisym + J)  antisym + 3-cycle + J  d_n")
dn = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 2, 2]
RAW = {}; WL = {}
for n in range(1, 10):
    B = L.B(n); d = len(B)
    two = [vec(padd(ev(b, X, Y), ev(b, Y, X)), n) for b in B]                      # psi(x,y)+psi(y,x)
    three = [vec(padd(padd(ev(b, X, Y), ev(b, Y, Z)), ev(b, Z, X)), n) for b in B] # psi(x,y)+psi(y,z)+psi(z,x)
    # J(psi) = [x, psi(x,y)] - [x+y, psi(-x-y, y)]
    J = [vec(padd(br(X, ev(b, X, Y)), br(padd(X, Y), ev(b, Z, Y)), -1), n + 1) for b in B]
    def sol(cols_list):
        M = []
        for cols in cols_list:
            for k in range(len(cols[0])): M.append([cols[j][k] for j in range(d)])
        return nullspace(M, d)
    raw = sol([two, three]); spec = sol([two, J]); all3 = sol([two, three, J])
    RAW[n] = raw; WL[n] = spec
    P(f" {n}   {d:3d}      {len(raw):3d}              {len(spec):3d}                    {len(all3):3d}            {dn[n]}")
P("  (the return's B.g3: raw 1,0,1,1,2,3,6,10,19; special, normalized, 0,0,1,0,1,0,2,1,4; in weight 1 the special count here keeps the")
P("   non-normalized solutions; my LM3 check gave 0,0,1,0,1,0,2,1 for the S_3-invariant outer special derivations)")

def lyn(word):
    return lyndon_bracket(tuple(0 if c == 'x' else 1 for c in word))
def comb(terms):
    p = {}
    for c, w in terms: p = padd(p, lyn(w), Fraction(c))
    return p
P("")
P("== B.g4: q4 = b_xxxy - 4 b_xxyy + b_xyyy ==")
q4 = comb([(1, 'xxxy'), (-4, 'xxyy'), (1, 'xyyy')])
t2 = padd(ev(q4, X, Y), ev(q4, Y, X)); t3 = padd(padd(ev(q4, X, Y), ev(q4, Y, Z)), ev(q4, Z, X))
Jq = padd(br(X, ev(q4, X, Y)), br(padd(X, Y), ev(q4, Z, Y)), -1)
P(" two-cycle defect zero:", not t2, " three-cycle defect zero:", not t3, " J(q4) zero:", not Jq)
P(" J(q4) in Lyndon coordinates (weight 5, words", ["".join('xy'[i] for i in w) for w in L.W(5)], "):")
# coordinates with respect to the Lyndon bracket basis: solve
B5 = L.B(5); M = [[vec(b, 5)[k] for b in B5] for k in range(len(B5))]
import copy
aug = [row + [vec(Jq, 5)[k]] for k, row in enumerate(M)]
R, piv = rref(aug); P("  ", [str(R[i][-1]) for i in range(len(R))])
P(" raw space in weight 4 is spanned by q4:", rank([vec(q4, 4)] + [[sum(v[j] * vec(L.B(4)[j], 4)[k] for j in range(L.dim(4))) for k in range(L.dim(4))] for v in RAW[4]]) == 1 == len(RAW[4]))

P("")
P("== B.g5: q7 and the pentagon ==")
q7 = comb([(3, 'xxxyxyy'), (3, 'xxxyyxy'), (1, 'xxyxyxy'), (-3, 'xxyxyyy'), (-3, 'xxyyxyy'), (-3, 'xxyyyxy'), (-1, 'xyxyxyy')])
t2 = padd(ev(q7, X, Y), ev(q7, Y, X)); t3 = padd(padd(ev(q7, X, Y), ev(q7, Y, Z)), ev(q7, Z, X))
Jq = padd(br(X, ev(q7, X, Y)), br(padd(X, Y), ev(q7, Z, Y)), -1)
P(" q7: two-cycle zero:", not t2, " three-cycle zero:", not t3, " J zero:", not Jq, " nonzero:", bool(q7))

# representation of t_4 on the free associative algebra on a, b, c (generators 0, 1, 2):
# t_ij (i, j <= 3): a_i -> [a_i, a_j], a_j -> [a_j, a_i], third -> 0;   t_i4 = ad a_i
A3 = [gen(0), gen(1), gen(2)]
def t(i, j):
    if j == 4:
        return ("ad", i - 1)
    vals = [{}, {}, {}]
    vals[i - 1] = br(A3[i - 1], A3[j - 1]); vals[j - 1] = br(A3[j - 1], A3[i - 1])
    return ("der", vals)
def apply(op, p):
    if op[0] == "ad": return br(A3[op[1]], p)
    return derive(p, op[1])
def apply_sum(ops, p):
    r = {}
    for c, op in ops: r = padd(r, apply(op, p), c)
    return r
def ev_ops(psi, Aops, Bops, target):
    """psi(A, B) applied to target, A and B sums of operators; a word w1...wn acts as w1 o ... o wn"""
    res = {}
    cache = {}
    def act(word):
        if word in cache: return cache[word]
        if not word: return target
        v = apply_sum(Aops if word[0] == 0 else Bops, act(word[1:]))
        cache[word] = v; return v
    for w, c in psi.items(): res = padd(res, act(w), c)
    return res
T = {(i, j): t(i, j) for i in range(1, 4) for j in range(i + 1, 5)}
def S(*pairs): return [(Fraction(1), T[p]) for p in pairs]
# check the defining relations of t_4 on the three generators
def comm(o1, o2, p): return padd(apply_sum(o1, apply_sum(o2, p)), apply_sum(o2, apply_sum(o1, p)), -1)
ok = True
for g in A3:
    ok &= not comm(S((1, 2)), S((3, 4)), g) and not comm(S((1, 3)), S((2, 4)), g) and not comm(S((1, 4)), S((2, 3)), g)
    for (i, j, k) in [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]:
        pr = lambda a, b: (min(a, b), max(a, b))
        ok &= not comm(S(pr(i, j)), S(pr(i, k), pr(j, k)), g)
        ok &= not comm(S(pr(i, k)), S(pr(i, j), pr(j, k)), g)
        ok &= not comm(S(pr(j, k)), S(pr(i, j), pr(i, k)), g)
P(" the relations of t_4 hold in the representation on Lie<a,b,c> (on the generators):", ok)
def pentagon(psi, target):
    # psi(t12, t23+t24) + psi(t13+t23, t34) - psi(t23, t34) - psi(t12+t13, t24+t34) - psi(t12, t23)
    r = ev_ops(psi, S((1, 2)), S((2, 3), (2, 4)), target)
    r = padd(r, ev_ops(psi, S((1, 3), (2, 3)), S((3, 4)), target))
    r = padd(r, ev_ops(psi, S((2, 3)), S((3, 4)), target), -1)
    r = padd(r, ev_ops(psi, S((1, 2), (1, 3)), S((2, 4), (3, 4)), target), -1)
    r = padd(r, ev_ops(psi, S((1, 2)), S((2, 3)), target), -1)
    return r
for n in (3, 5):
    v = WL[n][0]; psi = {}
    for j, c in enumerate(v):
        if c: psi = padd(psi, L.B(n)[j], c)
    d = pentagon(psi, A3[0]); P(f" weight {n}: the solution of the special system has pentagon defect zero on a, b, c:", not d and not pentagon(psi, A3[1]) and not pentagon(psi, A3[2]))
d7 = pentagon(q7, A3[0])
P(" weight 7, q7: pentagon defect on a is zero:", not d7, "; number of words:", len(d7), "; coefficient of a^5 b c b:", d7.get((0, 0, 0, 0, 0, 1, 2, 1), 0))
# the other direction: some combination in W^lac_7 with zero defect (dim W_7 >= 1)
basis7 = []
for v in WL[7]:
    psi = {}
    for j, c in enumerate(v):
        if c: psi = padd(psi, L.B(7)[j], c)
    basis7.append(psi)
defs = [pentagon(p, A3[0]) for p in basis7]
keys = sorted(set().union(*[set(d) for d in defs]))
P(" weight 7: dim of the special space:", len(basis7), "; rank of the pentagon defects (on a) of a basis:", rank([[d.get(k, Fraction(0)) for k in keys] for d in defs]))

P("")
P("== finite checks ==")
from math import gcd
def units_mod_squares(n):
    U = [a for a in range(1, n + 1) if gcd(a, n) == 1]; sq = {a * a % n for a in U}
    return len(U) // len(sq)
P(" C.r1: |(Z/n)^*/squares| for n = 2,3,4,5,6,7,8,12,24:", [units_mod_squares(n) for n in (2, 3, 4, 5, 6, 7, 8, 12, 24)])
# C.r2: level 5, conjugation by diag(2,3) (determinant 6 = 1 mod 5) on the unipotent [[1,1],[0,1]]
P(" C.r2: diag(2,3) [[1,1],[0,1]] diag(2,3)^-1 mod 5 has upper entry", 2 * pow(3, -1, 5) % 5, "(the unipotent goes to its 4th power)")
P(" C.a3: 5 = 1 mod 4, and 5 is a square mod 8:", 5 in {a * a % 8 for a in range(8)})
# D.5: centralizer of R with trace t and determinant 1: det(c + dR) = c^2 + t cd + d^2
P(" D.5: det(c + dR) = c^2 + (tr R) cd + d^2; with tr R = 1 (R of order 6) the form is c^2 + cd + d^2, with tr R = -1 (order 3) it is c^2 - cd + d^2")
for R_ in ([[0, -1], [1, 1]], [[0, -1], [1, -1]]):
    c, d = 2, 5; Mx = [[c + d * R_[0][0], d * R_[0][1]], [d * R_[1][0], c + d * R_[1][1]]]
    P("      R =", R_, " det(2 + 5R) =", Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0], " c^2+cd+d^2 =", c*c + c*d + d*d, " c^2-cd+d^2 =", c*c - c*d + d*d)
# D.7: the image of an element of order 3 in A_4^ab
P(" D.7: A_4 has 12 elements, derived subgroup of order 4, abelianization C_3 (elements of order 3 are non-trivial there)")

with open(__file__.replace(".py", ".out"), "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

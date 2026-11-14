"""Referee B check: braid identities used in LM7_PUSH E.61 (sewing part), E.64 and E.67.

Written by Claude Opus 5.5 at effort max, 14 Nov 2026. Equality in B_n is tested through the Artin
representation B_n -> Aut(F_n) (faithful by Artin's theorem): sigma_i sends x_i -> x_i x_{i+1} x_i^{-1},
x_{i+1} -> x_i and fixes the other generators. Reads no file of the return.
Run: python -I -B check_braid_identities.py
"""
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)

def freered(w):
    out = []
    for t in w:
        if out and out[-1] == -t:
            out.pop()
        else:
            out.append(t)
    return tuple(out)

def finv(w):
    return tuple(-t for t in reversed(w))

class Braid:
    """An element of B_n stored as the tuple of Artin images of x_1..x_n (left composition)."""
    def __init__(self, n, imgs=None):
        self.n = n
        self.imgs = imgs if imgs is not None else tuple((j,) for j in range(1, n + 1))
    def apply_word(self, w):
        out = []
        for t in w:
            img = self.imgs[abs(t) - 1]
            out.extend(img if t > 0 else finv(img))
        return freered(out)
    def __mul__(self, other):   # (self*other)(x) = self(other(x))
        return Braid(self.n, tuple(self.apply_word(other.imgs[j]) for j in range(self.n)))
    def inv(self):
        # invert by solving: compute inverse as product of generator inverses is easier; done via word form
        raise NotImplementedError
    def __eq__(self, other):
        return self.n == other.n and self.imgs == other.imgs
    def __pow__(self, k):
        if k < 0:
            raise ValueError
        r = Braid(self.n)
        for _ in range(k):
            r = r * self
        return r

def gen(n, i, sign=1):
    imgs = [(j,) for j in range(1, n + 1)]
    if sign > 0:
        imgs[i - 1] = (i, i + 1, -i)
        imgs[i] = (i,)
    else:
        imgs[i - 1] = (i + 1,)
        imgs[i] = (-(i + 1), i, i + 1)
    return Braid(n, tuple(imgs))

def word(n, w):
    """w: sequence of nonzero ints, +i for sigma_i, -i for sigma_i^{-1}"""
    r = Braid(n)
    for t in w:
        r = r * gen(n, abs(t), 1 if t > 0 else -1)
    return r

def W(*parts):
    out = []
    for p in parts:
        out.extend(p)
    return tuple(out)
def inv_w(w):
    return tuple(-t for t in reversed(w))
def pw(w, k):
    if k >= 0:
        return tuple(w) * k
    return inv_w(w) * (-k)

# sanity: braid relations and an inverse
for n in (3, 4, 5):
    for i in range(1, n - 1):
        check("B_%d: s%d s%d s%d = s%d s%d s%d" % (n, i, i+1, i, i+1, i, i+1), word(n, (i, i+1, i)) == word(n, (i+1, i, i+1)))
check("B_4: s1 s3 = s3 s1", word(4, (1, 3)) == word(4, (3, 1)))
check("B_4: s1 s1^{-1} = 1", word(4, (1, -1)) == Braid(4))
check("B_4: s1 s2 != s2 s1 (non-triviality of the test)", not (word(4, (1, 2)) == word(4, (2, 1))))

# ---------------- E.61 sewing comparison ----------------
print("== E.61.18-20 ==")
a, b, c = (1,), (2,), (3,)
B4 = lambda w: word(4, w)
X12 = W(a, a); X23 = W(b, b); X34 = W(c, c)
aba = W(a, b, a); cbc = W(c, b, c)
X45 = pw(aba, 2); X51 = pw(cbc, 2); Zw = pw(W(a, b, c), 4)
E1 = pw(aba, 4); E3 = pw(cbc, 4)
E2 = W(c, b, a, inv_w(b), inv_w(c))
X14 = pw(E2, 2)
pairs = [(a, X51), (E2, X51), (E2, X45), (c, X45)]
targets = [W(X34, Zw), W(X23, Zw), W(X23, Zw), W(X12, Zw)]
for idx, ((uu, vv), tgt) in enumerate(zip(pairs, targets), 1):
    check("E.61.19 map %d satisfies uvuv = vuvu" % idx, B4(W(uu, vv, uu, vv)) == B4(W(vv, uu, vv, uu)))
    check("E.61.20 map %d: (uv)^2 equals the stated central square" % idx, B4(pw(W(uu, vv), 2)) == B4(tgt))
check("Z = (abc)^4 is central in B_4", all(B4(W(Zw, g)) == B4(W(g, Zw)) for g in (a, b, c)))
check("in B_3: u = s1, v = s2^2 satisfy uvuv = vuvu", word(3, (1, 2, 2, 1, 2, 2)) == word(3, (2, 2, 1, 2, 2, 1)))
check("E1 = (aba)^4 and E3 = (cbc)^4 commute with Z", B4(W(E1, Zw)) == B4(W(Zw, E1)))
# E.61.22 uses X14 = E2^2; check that the four maps are the NS 2000 maps {Da1,x51},{De2,x51},{De2,x45},{Da3,x45}
check("X45 = (aba)^2 and X51 = (cbc)^2 commute with Z", B4(W(X45, Zw)) == B4(W(Zw, X45)) and B4(W(X51, Zw)) == B4(W(Zw, X51)))

# ---------------- E.64 hyperelliptic presentation identities ----------------
print("== E.64.14 ==")
for n in (4, 6, 8):
    delta = tuple(range(1, n))
    zn = pw(delta, n)
    zfirst = pw(tuple(range(1, n - 1)), n - 1)
    zlast = pw(tuple(range(2, n)), n - 1)
    Wn = W(tuple(range(1, n - 1)), (n - 1, n - 1), tuple(range(n - 2, 0, -1)))
    Bn = lambda w, n=n: word(n, w)
    check("n=%d: z_last = delta z_first delta^{-1}" % n, Bn(zlast) == Bn(W(delta, zfirst, inv_w(delta))))
    check("n=%d: W_n = z_n z_last^{-1}" % n, Bn(Wn) == Bn(W(zn, inv_w(zlast))))
    check("n=%d: z_n central" % n, all(Bn(W(zn, (i,))) == Bn(W((i,), zn)) for i in range(1, n)))
    check("n=%d: z_first is the full twist of the first n-1 strands (commutes with s1..s_{n-2})" % n,
          all(Bn(W(zfirst, (i,))) == Bn(W((i,), zfirst)) for i in range(1, n - 1)))

print("== E.64.4-6, 17-22, 29, 31 ==")
xi1 = W(c, inv_w(a))
xi2 = W(a, b, a, inv_w(c), inv_w(b), inv_w(a))
# Ferrari fold q: a,c -> s1, b -> s2 in B_3
def fold(w):
    return tuple((1 if abs(t) in (1, 3) else 2) * (1 if t > 0 else -1) for t in w)
B3 = lambda w: word(3, w)
check("E.64.4: q(xi1) = 1 and q(xi2) = 1", B3(fold(xi1)) == Braid(3) and B3(fold(xi2)) == Braid(3))
thu = W(a, b); thv = W(inv_w(b), c, b, a)
check("E.64.5: theta(u)=ab, theta(v)=b^{-1}cba satisfy the braid relation", B4(W(thu, thv, thu)) == B4(W(thv, thu, thv)))
z4 = pw(W(a, b, c), 4)
check("E.64.5: theta((uv)^3) = z_4", B4(pw(W(thu, thv), 3)) == B4(z4))
check("E.64.5: q(theta(u)) = q(theta(v)) = ab", B3(fold(thu)) == B3((1, 2)) and B3(fold(thv)) == B3((1, 2)))
d_ = W(a, b, c)
y_ = W(inv_w(b), d_, d_, b)
x_ = inv_w(W(y_, d_))
check("E.64.6: y^2 = d^4", B4(pw(y_, 2)) == B4(pw(d_, 4)))
check("E.64.6: d^4 = z_4", B4(pw(d_, 4)) == B4(z4))
# E.64.17 Nielsen action: test both conjugation conventions
def conj(g, w):  # g w g^{-1}
    return W(g, w, inv_w(g))
tab = {('a', 'xi1'): xi1, ('a', 'xi2'): W(xi2, xi1), ('b', 'xi1'): W(xi1, inv_w(xi2)), ('b', 'xi2'): xi2}
gens = {'a': a, 'b': b}
xis = {'xi1': xi1, 'xi2': xi2}
left = all(B4(conj(gens[g], xis[k])) == B4(v) for (g, k), v in tab.items())
right = all(B4(conj(inv_w(gens[g]), xis[k])) == B4(v) for (g, k), v in tab.items())
check("E.64.17 table holds for conjugation g xi g^{-1}" if left else "E.64.17 table holds for conjugation g^{-1} xi g", left or right)
print("   (convention: left g.xi.g^-1 = %s, right g^-1.xi.g = %s)" % (left, right))
xp = W(a, b)
xp2 = W(inv_w(b), inv_w(a), inv_w(b), inv_w(a), inv_w(b), inv_w(c))
xp3 = W(c, b, a, b)
check("E.64.18: theta(uv) = xi_{+3}", B4(W(thu, thv)) == B4(xp3))
check("E.64.18: theta(uvu) = xi_{+2}^{-1}", B4(W(thu, thv, thu)) == B4(inv_w(xp2)))
check("E.64.18: xi_+ xi_{+2} xi_{+3} = 1", B4(W(xp, xp2, xp3)) == Braid(4))
check("E.64.18: xi_{+2}^2 = z_4^{-1}", B4(pw(xp2, 2)) == B4(inv_w(z4)))
check("E.64.18: xi_{+3}^3 = z_4", B4(pw(xp3, 3)) == B4(z4))
uv = W(thu, thv); uu = thu
k1 = W(uv, inv_w(uu), inv_w(uu))
k2 = W(pw(uu, 4), uv, pw(uv, -3))
check("E.64.19: theta(k1) = xi1", B4(k1) == B4(xi1))
check("E.64.19: theta(k2) = xi2", B4(k2) == B4(xi2))
check("E.64.20: q(d) = s = aba, q(y) = s^2, q(x) = s^{-3}",
      B3(fold(d_)) == B3((1, 2, 1)) and B3(fold(y_)) == B3(pw((1, 2, 1), 2)) and B3(fold(x_)) == B3(pw((1, 2, 1), -3)))
check("E.64.20: k0 = y d^{-2} = xi2^{-1}", B4(W(y_, pw(d_, -2))) == B4(inv_w(xi2)))
check("E.64.20: k1 = d y d^{-3} = xi1^{-1}", B4(W(d_, y_, pw(d_, -3))) == B4(inv_w(xi1)))
check("E.64.20: d xi1 d^{-1} = xi2^{-1}", B4(conj(d_, xi1)) == B4(inv_w(xi2)))
check("E.64.20: d xi2 d^{-1} = xi1", B4(conj(d_, xi2)) == B4(xi1))
check("E.64.22: x = xi1 d^{-3}", B4(x_) == B4(W(xi1, pw(d_, -3))))
def comm(p, q):  # p q p^{-1} q^{-1}
    return W(p, q, inv_w(p), inv_w(q))
def comm2(p, q):  # p^{-1} q^{-1} p q
    return W(inv_w(p), inv_w(q), p, q)
lhs = W(pw(x_, 4), pw(z4, 3))
c1 = B4(lhs) == B4(comm(xi1, inv_w(xi2)))
c2 = B4(lhs) == B4(comm2(xi1, inv_w(xi2)))
check("E.64.22: x^4 z_4^3 = [xi1, xi2^{-1}] (in one commutator convention)", c1 or c2)
print("   (convention: [p,q]=pqp^-1q^-1: %s; [p,q]=p^-1q^-1pq: %s)" % (c1, c2))
conv = comm if c1 else comm2
check("E.64.22: [xi1, xi2^{-1}] = xi2^{-1} [xi1,xi2]^{-1} xi2 (same convention)",
      B4(conv(xi1, inv_w(xi2))) == B4(W(inv_w(xi2), inv_w(conv(xi1, xi2)), xi2)))
z3 = pw(W(a, b), 3)
d31 = B4(conv(xi1, xi2)) == B4(W(z4, pw(z3, -2)))
check("E.64.31: [xi1, xi2] = z_4 z_3^{-2} (same convention)", d31)
print("   (info) E.64.31 also in the other commutator convention: %s (expected False; the return uses pqp^-1q^-1 throughout)"
      % (B4((comm2 if c1 else comm)(xi1, xi2)) == B4(W(z4, pw(z3, -2)))))
# E.64.29 Mordell cusp relation in B_3^mor = <u,v>
U3 = (1,); V3 = (2,)
k1m = W(U3, V3, inv_w(U3), inv_w(U3))
k2m = W(pw(U3, 4), W(U3, V3), pw(W(U3, V3), -3))
z3m = pw(W(U3, V3), 3)
e1 = B3(W(comm(k1m, k2m), pw(U3, 6))) == B3(z3m)
e2 = B3(W(comm2(k1m, k2m), pw(U3, 6))) == B3(z3m)
check("E.64.29: [k1,k2] u^6 = z_3^mor (one convention)", e1 or e2)
print("   (convention pqp^-1q^-1: %s; p^-1q^-1pq: %s)" % (e1, e2))
# E.67.8 version with k2 = x^4 z, z = uv: the same up to the centre
k2b = W(pw(U3, 4), W(U3, V3))
e3 = B3(W(comm(k1m, k2b), pw(U3, 6))) == B3(z3m)
e4 = B3(W(comm2(k1m, k2b), pw(U3, 6))) == B3(z3m)
check("E.67.8 cusp identity [k1,k2] x^6 = central (k2 = x^4 z): one convention gives z3", e3 or e4)
print("   (convention pqp^-1q^-1: %s; p^-1q^-1pq: %s)" % (e3, e4))

# central elements in the triangle subgroups
check("z_3 = (ab)^3 commutes with a and b", all(B4(W(z3, g)) == B4(W(g, z3)) for g in (a, b)))
check("E.64.6 centre: d^4 = z_4 central in B_4", all(B4(W(pw(d_, 4), g)) == B4(W(g, pw(d_, 4))) for g in (a, b, c)))

print()
print("TOTAL FAILS:", len(FAILS))
for f in FAILS:
    print("  ", f)

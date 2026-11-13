# Review checks for LM7_FERMAT_TOWER: finite groups, lattices, arithmetic.
# Author: Claude Fable 5.2 (effort max), 13 Nov 2026. Own code; the return's code was not run.
# Run: python -I -B check_finite.py > check_finite.out
import itertools, math
from fractions import Fraction

def mm(A, B, n=None):
    C = tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    if n: C = tuple(tuple(x % n for x in r) for r in C)
    return C
def inv2(A, n=None):
    (a, b), (c, d) = A
    det = a*d - b*c
    if n is None:
        assert det in (1, -1)
        return ((d*det, -b*det), (-c*det, a*det))
    di = pow(det % n, -1, n)
    return ((d*di % n, -b*di % n), (-c*di % n, a*di % n))
def red(A, n): return tuple(tuple(x % n for x in r) for r in A)
I2 = ((1, 0), (0, 1))

print("== A.2: words, conjugations")
rho = ((0, 1), (-1, 1)); sig = ((0, -1), (1, 0)); tau = ((-1, 0), (0, 1)); om = ((-1, 0), (0, -1))
l0 = ((-1, 2), (0, -1)); l1 = ((-1, 0), (-2, -1))
def prod(*Ms):
    P = I2
    for M in Ms: P = mm(P, M)
    return P
print("lambda0 = w s r s r:", prod(om, sig, rho, sig, rho) == l0, "; lambda1 = w r s r s:", prod(om, rho, sig, rho, sig) == l1)
print("rho l0 rho^-1 = l1:", prod(rho, l0, inv2(rho)) == l1, "; rho l1 rho^-1 = (l1 l0)^-1:", prod(rho, l1, inv2(rho)) == inv2(mm(l1, l0)))
print("sig l0 sig^-1 = l1:", prod(sig, l0, inv2(sig)) == l1, "; sig l1 sig^-1 = l0:", prod(sig, l1, inv2(sig)) == l0)
print("tau inverts l0, l1:", prod(tau, l0, inv2(tau)) == inv2(l0), prod(tau, l1, inv2(tau)) == inv2(l1))
print("rho^3 = sig^2 = -I:", prod(rho, rho, rho) == om, mm(sig, sig) == om)
# action on M = Z e0 + Z e1 (columns = images of e0, e1): rho: e0->e1, e1->-e0-e1 ; sigma: swap; tau: -1
R = ((0, -1), (1, -1)); S = ((0, 1), (1, 0)); mI = ((-1, 0), (0, -1))
def gen_group(gens, n):
    gens = [red(g, n) for g in gens]
    seen = {red(I2, n)}; frontier = [red(I2, n)]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                k = mm(g, h, n)
                if k not in seen: seen.add(k); new.append(k)
        frontier = new
    return seen
print("N | image order of <R,S,-I> on M/N (kernel = 24/order):")
print("  ", [(N, len(gen_group([R, S, mI], N)) if N > 1 else 1) for N in (1, 2, 3, 4, 6, 8, 12, 24)])

print("== A.3, A.4: level 12")
n = 12
SL = gen_group([((1, 1), (0, 1)), ((1, 0), (1, 1))], n)
GL = [((a, b), (c, d)) for a in range(n) for b in range(n) for c in range(n) for d in range(n) if math.gcd((a*d - b*c) % n, n) == 1]
print("|SL2(Z/12)| =", len(SL), " |GL2(Z/12)| =", len(GL), " |det = +-1| =", sum(1 for g in GL if (g[0][0]*g[1][1]-g[0][1]*g[1][0]) % n in (1, 11)))
delta = mm(l1, inv2(l0)); print("delta =", delta, " delta^2 mod 12 =", red(mm(delta, delta), n))
def normal_closure(elts, G, n):
    conj = set()
    for g in G:
        gi = inv2(g, n)
        for e in elts: conj.add(mm(mm(g, red(e, n), n), gi, n))
    return gen_group(list(conj), n)
K32 = normal_closure([delta], SL, n)
print("|normal closure of delta in SL2(Z/12)| =", len(K32), " index =", len(SL)//len(K32))
K4 = {red(g, 4) for g in K32}; K3 = {red(g, 3) for g in K32}
print("image mod 4 has order", len(K4), "; image mod 3 has order", len(K3), "; product order", len(K4)*len(K3))
def order(g, n):
    k = 1; h = g
    while h != red(I2, n): h = mm(h, g, n); k += 1
    return k
from collections import Counter
print("element orders mod 3 image:", sorted(Counter(order(g, 3) for g in K3).items()), "(Q8: 1,1,6 of orders 1,2,4)")
print("element orders mod 4 image:", sorted(Counter(order(g, 4) for g in K4).items()), "(V4)")
print("normal in GL2(Z/12):", all(mm(mm(g, k, n), inv2(g, n), n) in K32 for g in GL for k in K32))
print("image of Pi_0 mod 12 has order", len(gen_group([l0, l1], n)), "; image of Pi_00-generators check: T^m in K32 only for m =", [m for m in range(1, 13) if ((1, m % n), (0, 1)) in K32])
com = prod(l0, l1, inv2(l0), inv2(l1)); print("[l0,l1] mod 12 =", red(com, n), " in K32:", red(com, n) in K32)
# index of Pi_00: Pi_0 -> M -> Z/3 ; full preimage of K32 has index 1152/32
print("index of preimage of K32 in SL2(Z) =", len(SL)//len(K32), "(= 36 = [SL2(Z):Pi_00])")

print("== A.12: cocycle c=(a+b)b' on C2^2 gives D8")
els = [(i, a, b) for i in range(2) for a in range(2) for b in range(2)]
def mul8(u, v): return ((u[0]+v[0]+(u[1]+u[2])*v[2]) % 2, (u[1]+v[1]) % 2, (u[2]+v[2]) % 2)
assoc = all(mul8(mul8(u, v), w) == mul8(u, mul8(v, w)) for u in els for v in els for w in els)
def ord8(u):
    k = 1; h = u
    while h != (0, 0, 0): h = mul8(h, u); k += 1
    return k
print("associative:", assoc, " orders:", sorted(Counter(ord8(u) for u in els).items()), "(D8: 1 of order 1, 5 of order 2, 2 of order 4)")

print("== B.10, B.13: H^0, H^1 of S3 on M/N by brute force")
def act(A, v, N): return ((A[0][0]*v[0]+A[0][1]*v[1]) % N, (A[1][0]*v[0]+A[1][1]*v[1]) % N)
for N in (2, 3, 4, 6, 8, 12):
    MN = [(u, v) for u in range(N) for v in range(N)]
    h0 = sum(1 for v in MN if act(R, v, N) == v and act(S, v, N) == v)
    # crossed homs: f(r)=a, f(s)=b with relations r^3, s^2, (rs)^2
    def add(u, v): return ((u[0]+v[0]) % N, (u[1]+v[1]) % N)
    cnt = 0
    RS = mm(R, S)
    for a in MN:
        fr3 = add(add(a, act(R, a, N)), act(mm(R, R), a, N))
        if fr3 != (0, 0): continue
        for b in MN:
            if add(b, act(S, b, N)) != (0, 0): continue
            frs = add(a, act(R, b, N))
            if add(frs, act(RS, frs, N)) != (0, 0): continue
            cnt += 1
    print("  N=%d: |H^0|=%d, |Z^1|=%d, |B^1|=%d, |H^1|=%d" % (N, h0, cnt, N*N//h0, cnt*h0//(N*N)))

print("== B.11: affine complement")
F = Fraction
def aff(g, h):  # (A,u)(B,v) = (AB, u + A v)
    (A, u), (B, v) = g, h
    return (mm(A, B), tuple(u[i] + sum(A[i][k]*v[k] for k in range(2)) for i in range(2)))
t = (F(1, 3), F(-1, 3)); rp = (R, (F(1), F(0))); sp = (S, t)
r3 = aff(aff(rp, rp), rp)
s2 = aff(sp, sp); rs = aff(rp, sp); rs2 = aff(rs, rs)
print("rho'^3 =", r3, "; sigma'^2 =", s2, "; (rho' sigma')^2 =", rs2)
p = (F(2, 3), F(1, 3))
print("(1-R)p =", tuple(p[i] - sum(R[i][k]*p[k] for k in range(2)) for i in range(2)), "; (1-S)p =", tuple(p[i] - sum(S[i][k]*p[k] for k in range(2)) for i in range(2)))

print("== B.6: Smith form of R_n/(S_X,S_Y,P_n)")
def snf_diag(M):
    M = [row[:] for row in M]; rows = len(M); cols = len(M[0]) if M else 0
    diag = []; r = 0; c = 0
    while r < rows and c < cols:
        piv = None; best = None
        for i in range(r, rows):
            for j in range(c, cols):
                if M[i][j] != 0 and (best is None or abs(M[i][j]) < best): best = abs(M[i][j]); piv = (i, j)
        if piv is None: break
        i, j = piv; M[r], M[i] = M[i], M[r]
        for row in M: row[c], row[j] = row[j], row[c]
        while True:
            done = True
            for i in range(r+1, rows):
                if M[i][c] != 0:
                    q = M[i][c] // M[r][c]
                    if q: M[i] = [a - q*b for a, b in zip(M[i], M[r])]
                    if M[i][c] != 0:
                        M[r], M[i] = M[i], M[r]; done = False
            for j in range(c+1, cols):
                if M[r][j] != 0:
                    q = M[r][j] // M[r][c]
                    if q:
                        for row in M: row[j] -= q*row[c]
                    if M[r][j] != 0:
                        for row in M: row[c], row[j] = row[j], row[c]
                        done = False
            if done: break
        diag.append(abs(M[r][c])); r += 1; c += 1
    return diag
for n in range(1, 7):
    idx = {(a, b): a*n + b for a in range(n) for b in range(n)}
    def vec(poly):
        v = [0]*(n*n)
        for (a, b), cf in poly.items(): v[idx[(a % n, b % n)]] += cf
        return v
    SX = {(i, 0): 1 for i in range(n)}; SY = {(0, j): 1 for j in range(n)}
    P = {(i, j): 1 for i in range(n) for j in range(i+1)}
    rowsM = []
    for g in (SX, SY, P):
        for a in range(n):
            for b in range(n):
                rowsM.append(vec({(i+a, j+b): cf for (i, j), cf in g.items()}))
    d = snf_diag(rowsM)
    print("  n=%d: rank of ideal %d, nontrivial invariant factors %s, quotient rank %d (expected (n-1)(n-2)=%d)" % (n, len(d), [x for x in d if x != 1], n*n - len(d), (n-1)*(n-2)))

print("== D.7: point counts over F_43, n=6 (expect 12 and 108)")
p = 43; n6 = 6
pw = [pow(x, n6, p) for x in range(p)]
def count(sign):
    c = 0
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if (x, y, z) != (0, 0, 0) and (pw[x] + pw[y] + sign*pw[z]) % p == 0: c += 1
    return c // (p - 1)
print("  #{x^6+y^6=z^6} =", count(-1), "; #{x^6+y^6+z^6=0} =", count(1))

print("== D.10: Soule/Vandiver certificates")
def primroot(q):
    fs = set(); m = q - 1; d = 2
    while d*d <= m:
        while m % d == 0: fs.add(d); m //= d
        d += 1
    if m > 1: fs.add(m)
    g = 2
    while any(pow(g, (q-1)//f, q) == 1 for f in fs): g += 1
    return g
wit = {5: [101], 7: [197, 491], 11: [727], 13: [677, 2029], 17: [3469], 19: [10831], 23: [12697], 29: [10093, 13457], 31: [15377], 37: [5477], 41: [16811], 43: [22189], 47: [8837]}
for l, qs in wit.items():
    cert = {}
    for q in qs:
        assert (q - 1) % (l*l) == 0, (l, q)
        g = primroot(q); r = pow(g, (q-1)//l, q)
        for m in range(3, l-1, 2):
            c = 1
            for a in range(1, l):
                c = c * pow((1 - pow(r, a, q)) % q, pow(a, m-1, l), q) % q
            if pow(c, (q-1)//l, q) != 1: cert.setdefault(m, q)
    missing = [m for m in range(3, l-1, 2) if m not in cert]
    print("  l=%d: q=%s, all odd m in [3,l-2] certified: %s %s" % (l, qs, not missing, missing if missing else ""))
# irregular pairs below 50 via Bernoulli numbers
B = [Fraction(1)]
for m in range(1, 50):
    B.append(-sum(Fraction(math.comb(m+1, k))*B[k] for k in range(m))/(m+1))
irr = [(l, k) for l in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47) for k in range(2, l-2, 2) if B[k].numerator % l == 0]
print("  irregular pairs (l,k), l<50:", irr)

print("== D.4 examples; E.28/E.29 examples")
def v(p, x):
    k = 0
    while x % p == 0: x //= p; k += 1
    return k
print("  v_11(3^10-1) =", v(11, 3**10-1), "; v_7(19^6-1) =", v(7, 19**6-1))
def mord(a, q):
    k = 1; x = a % q
    while x != 1: x = x*a % q; k += 1
    return k
print("  ord(6 mod 109) =", mord(6, 109), "; ord(2 mod 163) =", mord(2, 163), "; ord(6^3 mod 109) =", mord(216, 109), "; ord(2^9 mod 163) =", mord(512, 163))

print("== D.17: equal-norm pairs and norm image")
def d17(m, p):
    # O_K3 = Z[z], z^2 = z - 1 ; O_K4 = Z[i]; O_L = Z[i,z]: a+bz+i(c+dz)
    def mulz(u, v): return ((u[0]*v[0] - u[1]*v[1]) % m, (u[0]*v[1] + u[1]*v[0] + u[1]*v[1]) % m)
    def muli(u, v): return ((u[0]*v[0] - u[1]*v[1]) % m, (u[0]*v[1] + u[1]*v[0]) % m)
    def addp(u, v): return ((u[0]+v[0]) % m, (u[1]+v[1]) % m)
    nz = {}; ni = {}
    for a in range(m):
        for b in range(m):
            N3 = (a*a + a*b + b*b) % m
            if N3 % p: nz.setdefault(N3, 0); nz[N3] += 1
            N4 = (a*a + b*b) % m
            if N4 % p: ni.setdefault(N4, 0); ni[N4] += 1
    pairs = sum(nz[k]*ni.get(k, 0) for k in nz)
    img = set()
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    u = (a, b); w = (c, d)
                    n3 = addp(mulz(u, u), mulz(w, w))          # (a+bz)^2+(c+dz)^2 in Z[z]
                    if (n3[0]*n3[0] + n3[0]*n3[1] + n3[1]*n3[1]) % p == 0: continue
                    s = (a, c); tt = (b, d)                     # a+ci, b+di in Z[i]
                    n4 = addp(addp(muli(s, s), muli(s, tt)), muli(tt, tt))
                    img.add((n3, n4))
    return pairs, len(img)
for m, p in ((2, 2), (4, 2), (8, 2), (16, 2), (3, 3), (9, 3), (27, 3)):
    print("  p^k=%d: equal-norm pairs %d, norm image %d" % ((m,) + d17(m, p)))

print("== E.25 / item 2: Hilbert symbols (-1,-1)_v")
def iso_mod(pk, p):
    # primitive solution of x^2+y^2+z^2 = 0 mod p^k ?
    for x in range(pk):
        for y in range(pk):
            for z in range(pk):
                if (x % p or y % p or z % p) and (x*x + y*y + z*z) % pk == 0: return True
    return False
print("  x^2+y^2+z^2=0 primitive mod 8:", iso_mod(8, 2), "(False => anisotropic over Q_2, (-1,-1)_2 = -1)")
for p in (3, 5, 7, 11, 13):
    print("  mod %d: primitive solution %s (nonsingular, lifts by Hensel => (-1,-1)_%d = +1)" % (p, iso_mod(p, p), p))
print("  over R: positive definite => (-1,-1)_inf = -1. Product formula: ramified exactly at {2, inf}.")

print("== E.26: (x rho)^3 = [x,y] in PSL2(Z), x=(sig rho)^2, y=(rho sig)^2")
x = prod(sig, rho, sig, rho); y = prod(rho, sig, rho, sig)
c = prod(x, y, inv2(x), inv2(y)); xr3 = prod(x, rho, x, rho, x, rho)
neg = lambda A: tuple(tuple(-e for e in r) for r in A)
print("  (x rho)^3 = +-c:", xr3 == c or xr3 == neg(c), "; ((x rho) sig)^2 = +-I:", prod(x, rho, sig, x, rho, sig) in (I2, neg(I2)))

print("== E.32 / item 1: the witness and the Mittag-Leffler failure")
def isprime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True
prev = 3
for j in range(3, 9):
    q = prev + 1
    while True:
        if q % 3**j == 1 and isprime(q) and pow(3, (q-1)//3, q) != 1: break
        q += 1
    prev = q
    e = v(3, q-1); g = primroot(q); eta = pow(g, (q-1)//3**e, q)
    tgt = pow(3, (q-1)//3**e, q); r = next(k for k in range(3**e) if pow(eta, k, q) == tgt)
    b = Fraction(q-1, 9*r)   # b_{q_j} as a rational; r is a 3-adic unit
    Aq = r; zq = 9*Aq*b; cq = -zq/(q-1)
    v3b = v(3, b.numerator) - v(3, b.denominator)
    print("  j=%d: q_j=%d, e=v_3(q-1)=%d, r_j=%d (r mod 3 = %d), v_3(b_q)=%d, z_q=9 A_q b_q = %s = q-1: %s, c_q=%s" % (j, q, e, r, r % 3, v3b, zq, zq == q-1, cq))
primes = [q for q in range(5, 200000) if isprime(q)]
cnt = Counter(v(3, q-1) for q in primes)
print("  primes q<200000 with v_3(q-1) >= m, m=1..10:", [sum(c for e, c in cnt.items() if e >= m) for m in range(1, 11)])
print("  image of K_m -> K_1 is the sum over q with v_3(q-1) >= m of Z/3: nonzero for every m, strictly decreasing: not Mittag-Leffler.")

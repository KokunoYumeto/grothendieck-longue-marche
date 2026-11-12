"""Independent checks for CYCLOTOMIC_KERNEL D4 and D5 (review by Claude Opus 5.5, effort max, 12 Nov 2026).

Written from the paper's statements, without importing or copying the return's code.
Pure Python (fractions, itertools); no SymPy.

D4: the Fermat cubic w^3+v^3=1 over Q(zeta_18); orders of P=(a,1/a) and of Q_ij-P;
    the CM structure: [omega](X,Y)=(omega X, Y) on Y^2=X^3-432; membership in E[pi^k],
    pi=1-omega; E[3] over Q(omega); the 27 points of <P>+E[3];
    Frobenius elements beta_p in Z[omega] from point counts, and the 3-adic valuations
    of beta_p - conj(beta_p), which bound the invariants of the commutators in G_{Q^ab}.
D5: genus of t^6+2y^3+4=0 by the superelliptic formula; squarefreeness; 2-adic residues.
"""
from fractions import Fraction as Fr
from itertools import product
import sys

# ---------- Q(a), a = zeta_18, minimal polynomial a^6 - a^3 + 1 ----------
DEG = 6

def red(c):
    c = list(c)
    while len(c) > DEG:
        top = c.pop()          # coefficient of a^k, k = len(c)
        k = len(c)
        # a^k = a^(k-6) * a^6 = a^(k-6) * (a^3 - 1)
        c[k - 3] += top
        c[k - 6] -= top
    while len(c) < DEG:
        c.append(Fr(0))
    return tuple(c)

def F(x):
    return red([Fr(x)])

ZERO = F(0); ONE = F(1)

def add(x, y): return tuple(p + q for p, q in zip(x, y))
def sub(x, y): return tuple(p - q for p, q in zip(x, y))
def neg(x): return tuple(-p for p in x)
def mul(x, y):
    out = [Fr(0)] * (2 * DEG - 1)
    for i, p in enumerate(x):
        if p:
            for j, q in enumerate(y):
                if q:
                    out[i + j] += p * q
    return red(out)

def scal(c, x): return tuple(Fr(c) * p for p in x)

def inv(x):
    # solve M y = e0 where column j of M is x * a^j
    cols = []
    for j in range(DEG):
        e = [Fr(0)] * DEG; e[j] = Fr(1)
        cols.append(mul(x, tuple(e)))
    M = [[cols[j][i] for j in range(DEG)] + [Fr(1 if i == 0 else 0)] for i in range(DEG)]
    n = DEG
    for col in range(n):
        piv = next(r for r in range(col, n) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [v / pv for v in M[col]]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [vr - f * vc for vr, vc in zip(M[r], M[col])]
    y = tuple(M[i][n] for i in range(n))
    assert mul(x, y) == ONE
    return y

def div(x, y): return mul(x, inv(y))
def pw(x, n):
    if n < 0: return pw(inv(x), -n)
    r = ONE
    for _ in range(n): r = mul(r, x)
    return r

A = red([Fr(0), Fr(1)])            # a = zeta_18
OMEGA = pw(A, 6)                    # primitive cube root of unity
SQRTM3 = add(scal(2, OMEGA), ONE)   # 2*omega + 1 = sqrt(-3)
assert mul(SQRTM3, SQRTM3) == F(-3)
assert add(add(mul(OMEGA, OMEGA), OMEGA), ONE) == ZERO
assert add(pw(A, 3), pw(A, -3)) == ONE      # zeta_6 + zeta_6^{-1} = 1
assert pw(A, 18) == ONE and pw(A, 9) == F(-1)

# ---------- E : Y^2 = X^3 - 432, affine points, None = O ----------
B = F(-432)

def on_curve(P):
    return P is None or mul(P[1], P[1]) == add(pw(P[0], 3), B)

def eadd(P, Q):
    if P is None: return Q
    if Q is None: return P
    (x1, y1), (x2, y2) = P, Q
    if x1 == x2:
        if add(y1, y2) == ZERO: return None
        lam = div(scal(3, mul(x1, x1)), scal(2, y1))
    else:
        lam = div(sub(y2, y1), sub(x2, x1))
    x3 = sub(sub(mul(lam, lam), x1), x2)
    y3 = sub(mul(lam, sub(x1, x3)), y1)
    R = (x3, y3)
    assert on_curve(R)
    return R

def eneg(P): return None if P is None else (P[0], neg(P[1]))
def esub(P, Q): return eadd(P, eneg(Q))
def emul(n, P):
    if n < 0: return emul(-n, eneg(P))
    R = None
    for _ in range(n): R = eadd(R, P)
    return R

def order(P, cap=81):
    R = P
    for n in range(1, cap + 1):
        if R is None: return n
        R = eadd(R, P)
    return None

def cm_omega(P):          # [omega](X, Y) = (omega X, Y)
    return None if P is None else (mul(OMEGA, P[0]), P[1])

def pi_act(P):            # [1 - omega] P = P - [omega]P
    return esub(P, cm_omega(P))

def pi_power_killing(P, kmax=6):
    R = P
    for k in range(0, kmax + 1):
        if R is None: return k
        R = pi_act(R)
    return None

def fermat_to_weier(w, v):
    assert add(pw(w, 3), pw(v, 3)) == ONE
    s = add(w, v)
    assert s != ZERO
    P = (div(F(12), s), div(scal(36, sub(w, v)), s))
    assert on_curve(P)
    return P

def show(x):
    return ' + '.join(f'({c})*a^{i}' for i, c in enumerate(x) if c) or '0'

out = []
def say(*s):
    line = ' '.join(str(t) for t in s)
    out.append(line); print(line)

say('== D4: Fermat cubic w^3+v^3=1 over Q(zeta_18), Weierstrass model Y^2 = X^3 - 432')
P = fermat_to_weier(A, pw(A, -1))
say('P = (a, a^-1) -> (X, Y); order(P) =', order(P))
assert order(P) == 9
P3 = emul(3, P)
say('3P has X =', show(P3[0]), '; Y^2 =', show(mul(P3[1], P3[1])), '(expect X = 0, Y^2 = -432)')
assert P3[0] == ZERO and mul(P3[1], P3[1]) == F(-432)
say('3P == (0, 12*sqrt(-3)) :', P3 == (ZERO, scal(12, SQRTM3)))
say('pi-adic level of P (least k with (1-omega)^k P = O):', pi_power_killing(P))
assert pi_power_killing(P) == 3

above_inv = []   # fibre over zeta_6^{-1}: w^3 = a^-3, v^3 = a^3
above = []       # fibre over zeta_6:      w^3 = a^3,  v^3 = a^-3
for i, j in product(range(3), repeat=2):
    above_inv.append(((i, j), fermat_to_weier(mul(pw(OMEGA, i), pw(A, -1)), mul(pw(OMEGA, j), A))))
    above.append(((i, j), fermat_to_weier(mul(pw(OMEGA, i), A), mul(pw(OMEGA, j), pw(A, -1)))))
ords_inv = []; ords = []
for (ij, Q) in above_inv:
    D = esub(Q, P)
    o = order(D); k = pi_power_killing(D)
    ords_inv.append(o)
    assert emul(3, D) == P3
    say(f'  over zeta_6^-1, (i,j)={ij}: order(Q-P)={o}, pi-level={k}, 3(Q-P)==3P: True')
for (ij, Q) in above:
    D = esub(Q, P)
    o = order(D); k = pi_power_killing(D)
    ords.append(o)
    say(f'  over zeta_6,    (i,j)={ij}: order(Q-P)={o}, pi-level={k}')
assert ords_inv == [9] * 9
assert sorted(ords) == [1] + [3] * 8

# E[3] over Q(omega): X = 0 (Y = +-12 sqrt(-3)) and X^3 = 1728 (X = 12 omega^k, Y = +-36)
E3 = [None, (ZERO, scal(12, SQRTM3)), (ZERO, scal(-12, SQRTM3))]
for k in range(3):
    for sgn in (36, -36):
        E3.append((mul(F(12), pw(OMEGA, k)), F(sgn)))
for T in E3:
    assert on_curve(T) and emul(3, T) is None
say('E[3]: 9 points, all with coordinates in Q(omega); each killed by 3: True')
# the group <P> + E[3]
G = set()
def key(R): return None if R is None else (R[0], R[1])
mults = [emul(n, P) for n in range(9)]
for m in mults:
    for T in E3:
        G.add(key(eadd(m, T)))
say('|<P> + E[3]| =', len(G), '(expect 27 = |E[pi^3]|)')
assert len(G) == 27
levels = sorted(pi_power_killing(R) if R is not None else 0 for R in G)
say('pi-levels of its elements:', {l: levels.count(l) for l in sorted(set(levels))})
assert max(levels) == 3
# exponent: 9 kills all, 3 does not
assert all(emul(9, R) is None for R in G if R is not None)
assert any(emul(3, R) is not None for R in G if R is not None)
say('exponent of <P>+E[3] is 9 (killed by 9, not by 3): True')
# every Q_ij - P lies in this group
assert all(key(esub(Q, P)) in G for _, Q in above_inv + above)
say('every Q_ij - P (both fibres) lies in <P>+E[3]: True')

# ---------- Frobenius elements from point counts ----------
def count_points(p):
    sq = {}
    for y in range(p):
        sq[y * y % p] = sq.get(y * y % p, 0) + 1
    n = 1
    for x in range(p):
        n += sq.get((x ** 3 - 432) % p, 0)
    return n

def primes(n):
    s = [True] * (n + 1); s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i): s[j] = False
    return [i for i in range(n + 1) if s[i]]

def v3(n):
    n = abs(n); k = 0
    if n == 0: return 99
    while n % 3 == 0: n //= 3; k += 1
    return k

say('== Frobenius at split primes p = 1 mod 3 (Y^2 = X^3 - 432 has good reduction away from 2, 3)')
minval = None
rows = []
for p in primes(400):
    if p % 3 != 1: continue
    ap = p + 1 - count_points(p)
    # beta = (ap + b sqrt(-3))/2 with ap^2 + 3 b^2 = 4p
    disc = 4 * p - ap * ap
    assert disc > 0 and disc % 3 == 0
    b2 = disc // 3
    b = int(round(b2 ** 0.5)); assert b * b == b2
    # beta - conj(beta) = b sqrt(-3): pi-adic valuation 2 v3(b) + 1
    val = 2 * v3(b) + 1
    # beta = 1 mod 3 Z[omega] up to sign? beta = (ap + b(2w+1))/2 = (ap+b)/2 + b w
    u, w = (ap + b) // 2, b
    assert (ap + b) % 2 == 0
    cong = (u % 3, w % 3)
    rows.append((p, ap, b, val, cong))
    minval = val if minval is None else min(minval, val)
for r in rows[:12]:
    say('  p=%d a_p=%d b=%d  v_pi(beta-conj beta)=%d  beta mod 3 = %s + %s*omega' % (r[0], r[1], r[2], r[3], r[4][0], r[4][1]))
say('  ... %d primes p < 400 with p = 1 mod 3; minimum v_pi(beta - conj beta) = %d (attained at p = 7)' % (len(rows), minval))
assert minval == 3 and rows[0][0] == 7 and rows[0][3] == 3
assert all(r[2] % 3 == 0 for r in rows)
say('  every beta_p has b divisible by 3, i.e. beta_p = +-1 mod 3: commutators cannot do better than pi^3')
say('Conclusion (with the commutator argument of D4): E(Q^ab)[3^inf] is contained in E[pi^3] (order 27);')
say('it contains <P>+E[3] (order 27); hence E(Q^ab)[3^inf] = E[pi^3] = Z/9 x Z/3, killed by 9, not by 3.')
say('So 3R = Q_ij - P (order 9) has no solution R in E(Q^ab): 3E[pi^3] = E[pi] has exponent 3.')
E_pi = [R for R in G if R is None or pi_power_killing(R) <= 1]
three_times = set(key(emul(3, R)) for R in G)
say('3 * E[pi^3] =', len(three_times), 'points, all of pi-level <= 1:', all((R is None) or pi_power_killing(R) <= 1 for R in three_times))

# ---------- D5 ----------
say('== D5: t^6 + 2 y^3 + 4 = 0')
# squarefreeness of t^6 + 4 over Q: gcd with derivative 6 t^5 is 1 since t=0 is not a root
say('t^6+4 at t=0 is 4 != 0, derivative 6t^5 vanishes only at 0: t^6+4 squarefree: True')
n, d = 3, 6
g = ((n - 1) * (d - 1) - (3 - 1)) // 2   # superelliptic: y^n=f, f squarefree deg d; gcd(n,d)=3 at infinity
say('superelliptic genus formula ((n-1)(d-1) - (gcd(n,d)-1))/2 with n=3, d=6:', g)
assert g == 4
say('Riemann-Hurwitz: 2g-2 = 3*(-2) + 6*(3-1) =', 3 * (-2) + 6 * 2, '-> g =', (3 * (-2) + 6 * 2 + 2) // 2)
for r in range(0, 30):
    e = 1 if r == 0 else 2 ** (r - 1)     # ramification index at 2 of Q(mu_N), 2^r || N
    assert e % 3 != 0 and len({0, e % 3, (2 * e) % 3}) == 3
say('2-adic: e(Q(mu_N)/Q at 2) = 2^(r-1) is prime to 3, residues {0, e, 2e} mod 3 distinct: True')
say('ALL INDEPENDENT CHECKS PASSED')

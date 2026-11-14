"""Referee B check: finite and symbolic matrix steps of LM7_PUSH E.61, E.65 (and E.64.25/27, E.58 bits, E.1 split).

Written by Claude Opus 5.5 at effort max, 14 Nov 2026. Reads no file of the return; every matrix is typed
from the statements. Run: python -I -B check_e61_e65_matrices.py
"""
import itertools
import sympy as sp

FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)

# ---------- integer 2x2 helpers ----------
def mul(A, B, m=None):
    r = ((A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
         (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]))
    return red(r, m) if m else r
def red(A, m):
    return tuple(tuple(x % m for x in row) for row in A)
def det(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def inv(A, m):
    d = det(A) % m
    di = pow(d, -1, m)
    return red(((A[1][1]*di, -A[0][1]*di), (-A[1][0]*di, A[0][0]*di)), m)
def neg(A, m):
    return red(((-A[0][0], -A[0][1]), (-A[1][0], -A[1][1])), m)
def mpow(A, k, m):
    R = I2
    B = red(A, m)
    if k < 0:
        B = inv(B, m); k = -k
    for _ in range(k):
        R = mul(R, B, m)
    return R
def scal(c, m):
    return red(((c, 0), (0, c)), m)
def gen_group(gens, m):
    gens = [red(g, m) for g in gens]
    seen = {red(I2, m)}
    frontier = [red(I2, m)]
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = mul(a, g, m)
                if b not in seen:
                    seen.add(b); new.append(b)
        frontier = new
    return seen

I2 = ((1, 0), (0, 1))
U = ((1, 1), (0, 1))
L = ((1, 0), (-1, 1))
S = mul(mul(U, L), U)          # ULU
Rp = mul(U, L)                 # R_+
R0 = ((-Rp[0][0], -Rp[0][1]), (-Rp[1][0], -Rp[1][1]))   # R_0 = -R_+
R_E1 = ((0, -1), (1, -1))      # E.1 / E.58 / E.61.10 matrix R
U2 = mul(U, U); L2 = mul(L, L)

print("== basic matrices ==")
check("S = ULU = [[0,1],[-1,0]]", S == ((0, 1), (-1, 0)))
check("R_+ = UL = [[0,1],[-1,1]]", Rp == ((0, 1), (-1, 1)))
check("R_0 = -R_+ equals the E.1 matrix R", R0 == R_E1)
check("S*R = U^{-1} (E.61 proof: SR = U^{-1})", mul(S, R0) == ((1, -1), (0, 1)))
check("R_0^3 = I over Z", mul(mul(R0, R0), R0) == I2)
check("R_+^3 = -I over Z", mul(mul(Rp, Rp), Rp) == ((-1, 0), (0, -1)))
Sinv = ((0, -1), (1, 0))
check("S U^2 S^{-1} = L^2", mul(mul(S, U2), Sinv) == L2)
check("S L^2 S^{-1} = U^2", mul(mul(S, L2), Sinv) == U2)
check("S U S^{-1} = L (so q(v) = L for v = s u s)", mul(mul(S, U), Sinv) == L)
check("R_+ U^2 R_+^{-1} = L^2 (r x r^{-1} = y)", mul(mul(Rp, U2), ((1, -1), (1, 0))) == L2)
XY = mul(U2, L2)
Z = ((XY[1][1], -XY[0][1]), (-XY[1][0], XY[0][0]))   # (xy)^{-1} over Z
RyRi = mul(mul(Rp, L2), ((1, -1), (1, 0)))
check("R_+ L^2 R_+^{-1} = -(U^2 L^2)^{-1} (r y r^{-1} = z projectively)", RyRi == ((-Z[0][0], -Z[0][1]), (-Z[1][0], -Z[1][1])))
for i in range(2):
    pass

print("== V_4 and the signed image of F (E.61.9) ==")
V4 = gen_group([U2, L2], 4)
check("<U^2,L^2> mod 4 has order 4", len(V4) == 4)
check("V_4 = {I, [[1,2],[0,1]], [[1,0],[2,1]], [[1,2],[2,1]]}",
      V4 == {((1, 0), (0, 1)), ((1, 2), (0, 1)), ((1, 0), (2, 1)), ((1, 2), (2, 1))})
check("V_4 abelian", all(mul(a, b, 4) == mul(b, a, 4) for a in V4 for b in V4))
check("-I not in V_4", neg(I2, 4) not in V4)
H12 = gen_group([U2, L2], 12)
check("signed image q12(F) in SL2(Z/12) has order 96", len(H12) == 96)
check("-I not in q12(F)", neg(I2, 12) not in H12)
H3 = gen_group([U2, L2], 3)
check("q12(F) mod 3 = SL2(F3) (order 24)", len(H3) == 24)

print("== SL2(F3), the character epsilon, E.61.12-14 ==")
SL3 = [((a, b), (c, d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3)
       if (a*d - b*c) % 3 == 1]
check("|SL2(F3)| = 24", len(SL3) == 24)
X = red(U2, 3)
Q8 = {g for g in SL3 if mpow(g, 4, 3) == I2 and (mpow(g, 2, 3) != I2 or g in (I2, neg(I2, 3)))}
Q8 = gen_group(list(Q8), 3)
check("Q8 (elements of order dividing 4) has order 8", len(Q8) == 8)
check("Q8 = <S, [[1,1],[1,2]]>", gen_group([red(S, 3), ((1, 1), (1, 2))], 3) == Q8)
def eps(g):
    for k in range(3):
        if mul(mpow(X, -k, 3), g, 3) in Q8:
            return k
    raise ValueError
check("epsilon is a homomorphism SL2(F3) -> F3", all(eps(mul(a, b, 3)) == (eps(a) + eps(b)) % 3 for a in SL3 for b in SL3))
check("epsilon(X) = epsilon(L^2) = 1", eps(X) == 1 and eps(red(L2, 3)) == 1)
R3 = red(R0, 3); S3m = red(S, 3); S3i = inv(S3m, 3)
passing = []
failing = []
for g in SL3:
    comm = mul(mul(mul(S3m, g, 3), S3i, 3), inv(g, 3), 3)
    cube = mpow(mul(inv(comm, 3), R3, 3), 3, 3)
    if cube == I2:
        passing.append(g)
    else:
        failing.append((g, cube))
XkSj = {mul(mpow(X, k, 3), mpow(S3m, j, 3), 3) for k in range(3) for j in range(4)}
check("E.61.13: cubic condition holds exactly for g = X^k S^j (12 elements)", set(passing) == XkSj and len(passing) == 12)
check("E.61.13: the other twelve give cube -I", len(failing) == 12 and all(c == neg(I2, 3) for _, c in failing))
ok14 = True
for g in passing:
    k = eps(g)
    comm = mul(mul(mul(S3m, g, 3), S3i, 3), inv(g, 3), 3)
    if comm != red(((1, k), (k, 1 + k*k)), 3):
        ok14 = False
check("E.61.14: S g S^{-1} g^{-1} = [[1,k],[k,1+k^2]] with k = epsilon(g)", ok14)

print("== E.61.4 directly modulo 12 over the whole signed image of F ==")
R12 = red(R0, 12); S12 = red(S, 12); S12i = inv(S12, 12)
eps12 = {}
cnt = 0
ok = True
for g in H12:
    comm = mul(mul(mul(S12, g, 12), S12i, 12), inv(g, 12), 12)
    if red(comm, 4) != I2:
        continue                      # f must be in F': its image is I mod 4
    cube = mpow(mul(inv(comm, 12), R12, 12), 3, 12)
    if cube != I2:
        continue
    cnt += 1
    k = eps(red(g, 3))                # = rho mod 3, since epsilon(q(beta)) = -2 rho = rho
    rho = k
    target = red(((1, -8*rho), (-8*rho, 1 + 64*rho*rho)), 12)
    if comm != target:
        ok = False
check("E.61.4 holds for every g in q12(F) with f in F' and the signed cubic condition (%d such g)" % cnt, ok and cnt > 0)
ok = all(red(((1, -8*r), (-8*r, 1 + 64*r*r)), 4) == I2 for r in range(12))
check("E.61.4 right side is I mod 4 for every rho", ok)
ok = all(red(((1, -8*r), (-8*r, 1 + 64*r*r)), 3) == red(((1, r), (r, 1 + r*r)), 3) for r in range(12))
check("E.61.4 right side mod 3 = [[1,rho],[rho,1+rho^2]]", ok)

print("== symbolic covariance E.65.10 and E.64.27 over Z[n] ==")
n = sp.symbols('n')
Us = sp.Matrix([[1, 1], [0, 1]]); Ls = sp.Matrix([[1, 0], [-1, 1]])
Ss = Us*Ls*Us; R0s = -(Us*Ls)
Vs = sp.Matrix([[1, n], [0, 1]]); Vsi = sp.Matrix([[1, -n], [0, 1]])
Fr = sp.Matrix([[1, -n], [-n, 1 + n**2]])
Fri = Fr.inv()
check("Frho has determinant 1", sp.simplify(Fr.det()) == 1)
check("E.65.10a: V S V^{-1} = S F_rho", sp.simplify(Vs*Ss*Vsi - Ss*Fr) == sp.zeros(2))
check("E.65.10b: V R_0 V^{-1} = F_rho^{-1} R_0", sp.simplify(Vs*R0s*Vsi - Fri*R0s) == sp.zeros(2))
check("E.64.27: V L V^{-1} = F_rho^{-1} L F_rho", sp.simplify(Vs*Ls*Vsi - Fri*Ls*Fr) == sp.zeros(2))
check("V U V^{-1} = U", sp.simplify(Vs*Us*Vsi - Us) == sp.zeros(2))

print("== E.65 modulo-four steps ==")
R4 = red(R0, 4)
cent = [v for v in V4 if mul(v, R4, 4) == mul(R4, v, 4)]
check("centralizer of R_0 in V_4 (mod 4) is trivial", cent == [I2])
check("trace distinguishes R_0 from -R_0 mod 4 and mod 12", (R0[0][0]+R0[1][1]) % 4 != (-(R0[0][0]+R0[1][1])) % 4)
S4 = red(S, 4)
check("S != -S mod 4", S4 != neg(S, 4))
# projective centralizer statement: for v in V_4, v R v^{-1} = +-R forces v = I and the sign +
ok = True
for v in V4:
    c = mul(mul(v, R4, 4), inv(v, 4), 4)
    if c == neg(R4, 4):
        ok = False
check("no v in V_4 conjugates R_0 to -R_0 mod 4", ok)

print("== centralizers and normalizers at three (E.65.3, E.65.17) ==")
CR = [g for g in SL3 if mul(g, R3, 3) == mul(R3, g, 3)]
CRexp = {mul(scal(e, 3), mpow(R3, k, 3), 3) for e in (1, 2) for k in range(3)}
check("C_{SL2(F3)}(R_0) = <-I> x <R_0> of order 6", set(CR) == CRexp and len(CR) == 6)
CS = [g for g in SL3 if mul(g, S3m, 3) == mul(S3m, g, 3)]
check("C_{SL2(F3)}(S) = <S> of order 4", set(CS) == {mpow(S3m, j, 3) for j in range(4)} and len(CS) == 4)
line = (1, 2)   # (1,-1) mod 3
def apply(A, v, m=3):
    return ((A[0][0]*v[0]+A[0][1]*v[1]) % m, (A[1][0]*v[0]+A[1][1]*v[1]) % m)
check("ker(R_0 - I) = F3(1,-1) and ker(R_+ + I) = F3(1,-1)",
      {v for v in itertools.product(range(3), repeat=2) if apply(R3, v) == v} == {(0, 0), (1, 2), (2, 1)}
      and {v for v in itertools.product(range(3), repeat=2) if apply(red(Rp, 3), v) == ((-v[0]) % 3, (-v[1]) % 3)} == {(0, 0), (1, 2), (2, 1)})
def eps3(T):
    w = apply(T, line)
    if w == line: return 0
    if w == ((-line[0]) % 3, (-line[1]) % 3): return 1
    raise ValueError
check("epsilon_3 is a character of C(R_0) with kernel <R_0>", all(eps3(mul(a, b, 3)) == (eps3(a) + eps3(b)) % 2 for a in CR for b in CR)
      and {g for g in CR if eps3(g) == 0} == {mpow(R3, k, 3) for k in range(3)})
GL3 = [((a, b), (c, d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a*d - b*c) % 3 != 0]
check("|GL2(F3)| = 48", len(GL3) == 48)
NR = [N for N in GL3 if mul(mul(N, R3, 3), inv(N, 3), 3) in {R3, inv(R3, 3), neg(R3, 3), neg(inv(R3, 3), 3)}]
ok = all(apply(N, line) in {(1, 2), (2, 1)} for N in NR)
ok2 = all(eps3(mul(mul(N, T, 3), inv(N, 3), 3)) == eps3(T) for N in NR for T in CR)
check("every projective normalizer of <R_0> in GL2(F3) preserves F3(1,-1) (%d normalizers)" % len(NR), ok)
check("conjugation by every such normalizer preserves epsilon_3 on C(R_0)", ok2)
NS = [N for N in GL3 if mul(mul(N, S3m, 3), inv(N, 3), 3) in {S3m, neg(S3m, 3)}]
def eps2(W):
    for j in range(4):
        if W == mpow(S3m, j, 3): return j % 2
    raise ValueError
check("conjugation by every projective normalizer of <S> preserves epsilon_2 (%d normalizers)" % len(NS),
      all(eps2(mul(mul(N, W, 3), inv(N, 3), 3)) == eps2(W) for N in NS for W in CS))

print("== class-two identities (E.65 'integral sign') ==")
rho, d, c = sp.symbols('rho d c')
def hx(a): return sp.Matrix([[1, a, 0], [0, 1, 0], [0, 0, 1]])
def hy(b): return sp.Matrix([[1, 0, 0], [0, 1, b], [0, 0, 1]])
def hc(e): return sp.Matrix([[1, 0, e], [0, 1, 0], [0, 0, 1]])
xx, yy = hx(1), hy(1)
comm = xx*yy*xx.inv()*yy.inv()
check("[x,y] = x y x^{-1} y^{-1} is the central e13 in the Heisenberg model", comm == hc(1))
h = hx(rho)*hy(rho)*hc(d)
th = hy(rho)*hx(rho)*hc(-d)                # theta swaps x,y and inverts [x,y]
check("E.65.11: theta(h)^{-1} h = [x,y]^{rho^2 + 2d}", sp.simplify(th.inv()*h - hc(rho**2 + 2*d)) == sp.zeros(3))
zz = (xx*yy).inv()
def comm_(a, b): return a*b*a.inv()*b.inv()
check("[y,z] = [x,y] and [z,x] = [x,y] in class two (z = (xy)^{-1})", sp.simplify(comm_(yy, zz) - comm) == sp.zeros(3)
      and sp.simplify(comm_(zz, xx) - comm) == sp.zeros(3))
# the swapped-convention commutator a^{-1}b^{-1}ab gives the same exponent rho^2 (sign-free check)
check("x^{-rho} y^{-rho} x^{rho} y^{rho} = [x,y]^{rho^2}", sp.simplify(hx(-rho)*hy(-rho)*hx(rho)*hy(rho) - hc(rho**2)) == sp.zeros(3))

print("== Marin-type intertwiner (E.65.15) ==")
a, b, cc, dd, lam, u = sp.symbols('a b c d lambda u')
N = sp.Matrix([[1, lam], [0, 1]])
M = sp.Matrix([[a, b], [cc, 2 - a]])
eqs = sp.expand(N*M*N - M*N*M)
check("(2,1) entry of NMN - MNM is -c(1 + lambda c)", sp.simplify(eqs[1, 0] + cc*(1 + lam*cc)) == 0)
Msol = sp.Matrix([[1 - u, lam*u**2], [-1/lam, 1 + u]])
check("the second family [[1-u, lambda u^2],[-1/lambda, 1+u]] satisfies the braid relation with U^lambda and det 1",
      sp.simplify(N*Msol*N - Msol*N*Msol) == sp.zeros(2) and sp.simplify(Msol.det() - 1) == 0)
Msub = M.subs(cc, -1/lam)
sol = sp.solve([sp.expand(N*Msub*N - Msub*N*Msub)[i, j] for i in range(2) for j in range(2)] + [sp.expand(Msub.det() - 1)], [b], dict=True)
check("with c = -1/lambda the relation forces b = lambda (a-1)^2", len(sol) >= 1 and all(sp.simplify(s[b] - lam*(a - 1)**2) == 0 for s in sol))
Msub0 = M.subs(cc, 0)
sol0 = sp.solve([sp.expand(Msub0.det() - 1)], [a], dict=True)
check("with c = 0 and det 1, a = d = 1 (abelian pair)", all(s[a] == 1 for s in sol0))
V = sp.Matrix([[lam, lam*u], [0, 1]])
check("V U V^{-1} = U^lambda and V L V^{-1} = second matrix", sp.simplify(V*Us*V.inv() - N) == sp.zeros(2) and sp.simplify(V*Ls*V.inv() - Msol) == sp.zeros(2))
A_ = sp.Matrix([[a, b], [cc, dd]])
check("E.64.25: AU - UA = [[-c, a-d],[0, c]] and AL - LA = [[-b, 0],[a-d, b]]",
      sp.simplify(A_*Us - Us*A_ - sp.Matrix([[-cc, a - dd], [0, cc]])) == sp.zeros(2)
      and sp.simplify(A_*Ls - Ls*A_ - sp.Matrix([[-b, 0], [a - dd, b]])) == sp.zeros(2))
l1, l2, t1, t2 = sp.symbols('l1 l2 t1 t2')
check("product of normalized intertwiners is normalized: [[l1,t1],[0,1]][[l2,t2],[0,1]] = [[l1 l2, l1 t2 + t1],[0,1]]",
      sp.Matrix([[l1, t1], [0, 1]])*sp.Matrix([[l2, t2], [0, 1]]) == sp.Matrix([[l1*l2, l1*t2 + t1], [0, 1]]))
m_ = sp.symbols('m')
Sh = sp.Matrix([[1, m_], [0, 1]])
conj = sp.expand(Sh*Ss*Sh.inv())
check("a shear [[1,m],[0,1]] conjugates S to [[-m, 1+m^2],[-1, m]] (so +-S forces m = 0 mod 12)",
      conj == sp.Matrix([[-m_, 1 + m_**2], [-1, m_]]))
check("conjugate of unipotent shear by normalized intertwiner: [[l,t],[0,1]][[1,k],[0,1]][[l,t],[0,1]]^{-1} = [[1,l k],[0,1]]",
      sp.simplify(sp.Matrix([[lam, u], [0, 1]])*sp.Matrix([[1, n], [0, 1]])*sp.Matrix([[lam, u], [0, 1]]).inv() - sp.Matrix([[1, lam*n], [0, 1]])) == sp.zeros(2))

print("== E.58 value and the H^3 step ==")
A58 = scal(5, 12)
check("5I is I mod 4 and -I mod 3", red(A58, 4) == I2 and red(A58, 3) == neg(I2, 3))
check("-5I is not in V_4 mod 4 (so 5I is the normalized lift of [5I])", red(neg(A58, 12), 4) not in V4)
check("5I is in the signed image q12(F)", A58 in H12)
T58 = inv(A58, 12)
check("E.58: T = (5I)^{-1} = 5I, epsilon_3 = 1; W = I, epsilon_2 = 0; delta = 1",
      T58 == A58 and eps3(red(T58, 3)) == 1 and eps2(I2) == 0)
check("V_{H^3} = U^{24 rho} = I mod 12 for all rho", all(mpow(U, 24*r, 12) == I2 for r in range(12)))
check("q12(f_{H^3}) = I mod 12 for all rho (E.61.4 at 3 rho)", all(red(((1, -24*r), (-24*r, 1 + 576*r*r)), 12) == I2 for r in range(12)))

print("== E.1 / LM7 D.25 matrix-pair split (projective H = q(F), order 96) ==")
def proj(A, m=12):
    return frozenset({red(A, m), neg(A, m)})
Hproj = {proj(g) for g in H12}
check("projective image H of F has order 96", len(Hproj) == 96)
def norm_lift(cls):
    lifts = [g for g in cls if red(g, 4) in V4]
    assert len(lifts) == 1
    return lifts[0]
CHr = [cls for cls in Hproj if proj(mul(mul(norm_lift(cls), R12, 12), inv(norm_lift(cls), 12), 12)) == proj(R12)]
CHs = [cls for cls in Hproj if proj(mul(mul(norm_lift(cls), S12, 12), inv(norm_lift(cls), 12), 12)) == proj(S12)]
check("|C_H(r)| = 6 and |C_H(s)| = 8", len(CHr) == 6 and len(CHs) == 8)
same = diff = 0
for Acl in CHr:
    for Bcl in CHs:
        A = norm_lift(Acl); B = norm_lift(Bcl)
        e3 = eps3(red(inv(A, 12), 3))          # sign of A^{-1} on the rational line
        Wm = red(inv(B, 12), 3)
        e2 = 0 if Wm in (I2, neg(I2, 3)) else 1
        if e3 == e2: same += 1
        else: diff += 1
check("E.1: 48 pairs, 24 CM compatible and 24 extra", same == 24 and diff == 24)
check("all normalized lifts of C_H(r) are I mod 4 (D.25: A_4 = I)", all(red(norm_lift(cl), 4) == I2 for cl in CHr))
check("normalized lifts of C_H(s) commute with S (signed) mod 12", all(mul(norm_lift(cl), S12, 12) == mul(S12, norm_lift(cl), 12) for cl in CHs))

print()
print("TOTAL FAILS:", len(FAILS))
for f in FAILS:
    print("  ", f)

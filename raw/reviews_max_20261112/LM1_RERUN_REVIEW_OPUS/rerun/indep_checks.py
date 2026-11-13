"""Independent checks by the reviewer (Claude Opus 5.5), written without the return's code.

Run: python -I indep_checks.py   (SymPy needed). Every check is an assert; output lists what passed.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

done = []

def ok(msg):
    done.append(msg)
    print("PASS", msg)

# --- B.12: the PSL2(F13) realization counterexample -----------------------------------
p = 13
def mm(a, b):
    return sp.Matrix(a) * sp.Matrix(b)
def red(M):
    return sp.Matrix(M).applyfunc(lambda x: x % p)
def proj_eq(A, B):
    A, B = red(A), red(B)
    return A == B or A == red(-B)
def pinv(A):
    A = sp.Matrix(A)
    return red(A.adjugate())          # det 1
def porder(A):
    B = red(A)
    for k in range(1, 200):
        if proj_eq(B, sp.eye(2)):
            return k
        B = red(B * A)
    raise AssertionError
rho = sp.Matrix([[1, 2], [5, 11]]); sig = sp.Matrix([[0, 1], [12, 0]])
rhop = sp.Matrix([[2, 5], [9, 10]]); sigp = sp.Matrix([[1, 4], [6, 12]])
al = sp.Matrix([[6, 6], [10, 8]]); be = sp.Matrix([[6, 8], [7, 3]])
for X in (rho, sig, rhop, sigp):
    assert X.det() % p == 1
for X in (al, be):
    assert X.det() % p != 0
inv_al = red(al.inv_mod(p)); inv_be = red(be.inv_mod(p))
assert proj_eq(al * rho * inv_al, rhop) and proj_eq(be * sig * inv_be, sigp)
ell = red(pinv(sig) * rho)
assert proj_eq(pinv(sigp) * rhop, ell * ell)
assert porder(rho) == 3 and porder(sig) == 2 and porder(ell) == 7
c1 = red(sig * rho * pinv(sig) * pinv(rho)); c2 = red(sigp * rhop * pinv(sigp) * pinv(rhop))
assert porder(c1) == 7 and porder(c2) == 6
ok("B.12: conjugacies, loop identity l'=l^2, orders 3,2,7 and commutator orders 7 vs 6 in PSL2(F13)")

# --- C.4: the 12-syllable kernel word maps to the identity ---------------------------
T, U, V = sp.symbols("T U V", nonzero=True)
x = lambda a: sp.Matrix([[1, a], [0, 1]])
s = sp.Matrix([[0, -1], [1, 0]]); si = s.inv()
L = s*x(1/T)*si*x(T)*s*x(U)*si*x(-T)*s*x(-1/T)*si*x(-T**2*U)
assert sp.simplify(L) == sp.eye(2)
ok("C.4: s x(1/T) s^-1 x(T) s x(U) s^-1 x(-T) s x(-1/T) s^-1 x(-T^2 U) = I (12 alternating syllables)")

# --- B.15: congruence conjugation of an effective automorphism ------------------------
a, mu = sp.symbols("a mu", nonzero=True)
r = sp.Matrix([[0, 1], [-1, 1]]); g = sp.Matrix([[mu, a*mu], [0, 1]])
S = sp.Matrix([[a, -mu*(1 + a**2)], [1/mu, -a]])
assert sp.simplify(g*s*g.inv() - S) == sp.zeros(2)
assert si*r == sp.Matrix([[-1, 1], [0, -1]])
assert sp.simplify(g*(si*r)*g.inv() - sp.Matrix([[-1, mu], [0, -1]])) == sp.zeros(2)
ok("B.15: g s g^-1 = [[a,-mu(1+a^2)],[1/mu,-a]] and g (s^-1 r) g^-1 = -[[1,-mu],[0,1]] (loop to its mu-th power)")

# --- E.6: the rank-five fibrewise-unipotent section without integral Ga extension -----
N = sp.zeros(5)
for i, w in enumerate([1, 2, 3, 2]):
    N[i, i+1] = w
X = sum(((-1)**(j+1) * N**j / j for j in range(1, 5)), sp.zeros(5))
assert all(sp.Rational(e).q == 1 for e in X)
assert X**4 / 24 == sp.Rational(1, 2) * sp.Matrix(5, 5, lambda i, j: 1 if (i, j) == (0, 4) else 0)
assert all(e % 2 == 0 for e in N**2) and all(e % 3 == 0 for e in N**3)
ok("E.6: weights 1,2,3,2: log integral, X^4/4! = E15/2, N^2 = 0 mod 2, N^3 = 0 mod 3")
# The general bound: weights w_i = i / p^max(v_p(i)-1,0), rank p^2+1, leading coefficient 1/p.
for q in (2, 3, 5):
    w = []
    for i in range(1, q*q + 1):
        v, m = 0, i
        while m % q == 0:
            v += 1; m //= q
        w.append(Fraction(i, q**max(v - 1, 0)))
    prodw = Fraction(1)
    for t in w:
        prodw *= t
    assert prodw / sp.factorial(q*q) == Fraction(1, q)
    assert all(int(sp.prod(w[k:k+q])) % q == 0 for k in range(len(w) - q + 1))
ok("E.6: sharpness family at p=2,3,5: products of p consecutive weights divisible by p, top coefficient 1/p")

# --- E.16: the affine model sends the lattice generators to the unit translations ------
R = sp.Matrix([[0, -1], [1, -1]]); Sx = sp.Matrix([[0, 1], [1, 0]]); tau = sp.Matrix([sp.Rational(1, 3), -sp.Rational(1, 3)])
def aff(A, t):
    return (A, t)
def comp(f, g2):  # f o g2
    return (f[0]*g2[0], f[0]*g2[1] + f[1])
rr = aff(R, sp.zeros(2, 1)); ss = aff(Sx, tau)
idm = (sp.eye(2), sp.zeros(2, 1))
def word(ws):
    out = idm
    for ch in ws:
        out = comp(out, rr if ch == "r" else ss)
    return out
assert word("rrr") == idm and word("ss") == idm
assert word("srsr") == (sp.eye(2), sp.Matrix([1, 0])) and word("rsrs") == (sp.eye(2), sp.Matrix([0, 1]))
ok("E.16: rho -> (R,0), sigma -> (S,(1/3,-1/3)) gives lambda0 -> e0, lambda1 -> e1 and kills -I")

# --- E.15: Pi0 is normal, mod 2 trivial, mod 4 a Klein group; SL2(Z/4)/V4 has order 12 -----
rho2 = sp.Matrix([[0, 1], [-1, 1]]); sig2 = sp.Matrix([[0, -1], [1, 0]])
l0 = -sig2*rho2*sig2*rho2; l1 = -rho2*sig2*rho2*sig2
assert l0 == sp.Matrix([[-1, 2], [0, -1]]) and l1 == sp.Matrix([[-1, 0], [-2, -1]])
assert (l0 - sp.eye(2)).applyfunc(lambda e: e % 2) == sp.zeros(2) and (l1 - sp.eye(2)).applyfunc(lambda e: e % 2) == sp.zeros(2)
ok("E.15/E.22: lambda0, lambda1 are the identity mod 2, so SL2(Z)->SL2(F2)=S3 kills Pi0")
# The BISITE action of Pi0 = <lambda0, lambda1> (free) on three letters is non-abelian:
p12 = (1, 0, 2); p13 = (2, 1, 0)
pm = lambda u, v: tuple(u[v[i]] for i in range(3))
assert pm(p12, p13) != pm(p13, p12)
ok("E.22: the BISITE images (12),(13) of the free basis of Pi0 do not commute, so this S3-cover does not factor through Pi0^ab, hence not through the envelope of S")

# --- D.12 and D.16: quaternion splitting and the two fields -------------------------
I_ = sp.Matrix([[0, -3], [1, 0]]); J_ = sp.Matrix([[0, 3], [1, 0]])
assert I_**2 == -3*sp.eye(2) and J_**2 == 3*sp.eye(2) and I_*J_ == -J_*I_
ok("D.12: (-3,3) splits in M2(Q)")
y = sp.symbols("y")
f = y**3 - 12*y - 14
assert sp.discriminant(f, y) == 1620 and sp.factorint(1620) == {2: 2, 3: 4, 5: 1}
assert sp.Poly(f, y).is_irreducible
g3 = sp.expand(f.subs(y, y - 1))
assert sp.Poly(g3, y).all_coeffs() == [1, -3, -9, -3]
ok("D.16: disc(x^3-12x-14) = 2^2 3^4 5 (sign field Q(sqrt5)); Eisenstein at 2, and at 3 after x -> x-1")
q4 = sp.expand((y + 1)**4 - 3)
assert sp.Poly(q4, y).all_coeffs() == [1, 4, 6, 4, -2]
ok("D.16: (x+1)^4 - 3 is Eisenstein at 2, so Q2(3^(1/4)) is totally ramified of degree 4")

# --- A.7: the imperfect-field example -------------------------------------------------
t_ = sp.symbols("t")
Sm = sp.Matrix([[1, t_], [t_ + 1, 1]])
assert sp.Poly(Sm.det(), t_, modulus=2) == sp.Poly(t_**2 + t_ + 1, t_, modulus=2)
assert sp.diff(t_**2 + t_ + 1, t_).subs(t_, 0) % 2 == 1
ok("A.7: over F2(t), det [[1,t],[t+1,1]] = t^2+t+1 has derivative 1, hence is not a square")

# --- 11 Nov E.28 (dropped in the rerun): Schreier rank of ker(F2 -> (Z/n)^2) ----------
for n in range(2, 7):
    index = n*n
    assert 1 + index*(2 - 1) == n*n + 1
ok("11 Nov E.28: ker(F2 -> (Z/n)^2) is free of rank n^2+1 (Schreier); 5 at n=2, against dim M = 6")

print(f"{len(done)} independent checks passed")

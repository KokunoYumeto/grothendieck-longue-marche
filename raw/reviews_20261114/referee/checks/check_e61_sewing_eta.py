"""Referee B check: E.61.7-E.61.17 (the affine map eta_m and the sewing value E.61.8), symbolically over Z.

Written by Claude Opus 5.5 at effort max, 14 Nov 2026.  Run: python -I -B check_e61_sewing_eta.py
"""
import sympy as sp

FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)

def amul(g, h):
    return (g[0] + g[1]*h[0], g[1]*h[1])
def ainv(g):
    Mi = g[1].inv()
    return (-(Mi*g[0]), Mi)
def apow(g, k):
    r = (sp.zeros(2, 1), sp.eye(2))
    base = g if k >= 0 else ainv(g)
    for _ in range(abs(k)):
        r = amul(r, base)
    return r
def aeq(g, h):
    return sp.simplify(g[0] - h[0]) == sp.zeros(2, 1) and sp.simplify(g[1] - h[1]) == sp.zeros(2)
def word(*gs):
    r = (sp.zeros(2, 1), sp.eye(2))
    for g in gs:
        r = amul(r, g)
    return r

U = sp.Matrix([[1, 1], [0, 1]]); L = sp.Matrix([[1, 0], [-1, 1]])
e1 = sp.Matrix([1, 0]); e2 = sp.Matrix([0, 1]); z = sp.zeros(2, 1)
a = (z, U); b = (z, L); c = (e1, U)
ai, bi, ci = ainv(a), ainv(b), ainv(c)
check("eta: aba = bab", aeq(word(a, b, a), word(b, a, b)))
check("eta: bcb = cbc", aeq(word(b, c, b), word(c, b, c)))
check("eta: ac = ca", aeq(word(a, c), word(c, a)))
check("eta(c a^{-1}) = translation e1 (Ferrari xi1)", aeq(word(c, ai), (e1, sp.eye(2))))
check("eta(aba c^{-1} b^{-1} a^{-1}) = translation e2 (Ferrari xi2)", aeq(word(a, b, a, ci, bi, ai), (e2, sp.eye(2))))
E1 = apow(word(a, b, a), 4); E3 = apow(word(c, b, c), 4)
check("eta(E1) = eta(E3) = 1", aeq(E1, (z, sp.eye(2))) and aeq(E3, (z, sp.eye(2))))
check("linear part of cbc is ULU = S, S^2 = -I", sp.simplify(word(c, b, c)[1] - U*L*U) == sp.zeros(2) and (U*L*U)**2 == -sp.eye(2))
wv = sp.Matrix([0, -1]); tw = (wv, sp.eye(2))
check("E.61.16: t_w (0,L^2) t_w^{-1} = (0,L^2)", aeq(word(tw, (z, L**2), ainv(tw)), (z, L**2)))
check("E.61.16: t_w (0,U^2) t_w^{-1} = (2e1,U^2) = eta(c)^2", aeq(word(tw, (z, U**2), ainv(tw)), (2*e1, U**2)) and aeq(apow(c, 2), (2*e1, U**2)))
A_, B_, C_, D_, n = sp.symbols('A B C D n')
q = sp.Matrix([[A_, B_], [C_, D_]])
qi = sp.Matrix([[D_, -B_], [-C_, A_]])          # inverse when det = 1
# E.61.17: f(eta(b)^2, eta(c)^2) = t_w f((0,L^2),(0,U^2)) t_w^{-1} = t_w (0, f(L^2,U^2)) t_w^{-1}, and f(L^2,U^2) = q^{-1}
val17 = word(tw, (z, qi), ainv(tw))
check("E.61.17: t_w (0,q^{-1}) t_w^{-1} = ((I - q^{-1}) w, q^{-1}) = ((-B, A-1), q^{-1})",
      sp.simplify(val17[0] - sp.Matrix([-B_, A_ - 1])) == sp.zeros(2, 1))
# E.61.8: eta(c)^{-n} ((-B, A-1), q^{-1}) (0, q) eta(a)^{n}, with eta(c)^k = (k e1, U^k), eta(a)^k = (0, U^k)
Un = sp.Matrix([[1, n], [0, 1]]); Umn = sp.Matrix([[1, -n], [0, 1]])
val = word((-n*e1, Umn), (sp.Matrix([-B_, A_ - 1]), qi), (z, q), (z, Un))
detsub = {D_: (1 + B_*C_)/A_}
check("E.61.8: product = ((-B - nA, A - 1), I) with n = 8 rho (using det q = 1)",
      sp.simplify((val[0] - sp.Matrix([-B_ - n*A_, A_ - 1])).subs(detsub)) == sp.zeros(2, 1)
      and sp.simplify((val[1] - sp.eye(2)).subs(detsub)) == sp.zeros(2))
check("eta(c)^k = (k e1, U^k) for k = 5 and -3", aeq(apow(c, 5), (5*e1, U**5)) and aeq(apow(c, -3), (-3*e1, U**-3)))
rho = sp.symbols('rho')
# with E.61.4: A = 1, B = -8 rho mod 12, so -B - 8 rho A = 0 and A - 1 = 0
check("E.61.8 at m = 12 with E.61.4 (A=1, B=-8rho) is the identity", sp.simplify((-(-8*rho) - 8*rho*1)) == 0)

print()
print("TOTAL FAILS:", len(FAILS))
for f in FAILS:
    print("  ", f)

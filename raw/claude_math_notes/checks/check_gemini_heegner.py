"""Checks of Gemini's last answer (16 Nov 2026)."""
from sympy import (symbols, Rational, series, sqrt, simplify, expand, factor, hyper, Matrix, zeros, solve,
                   nsimplify, Poly, S)
t, w = symbols('t w')
# (a) flat coordinate at rho: c(t) = t 2F1(2/3,2/3;4/3;-t^3)/2F1(1/3,1/3;2/3;-t^3); j in w = c(t)
N = 14
def F(a, b, c, x, n):
    s, term = S(0), S(1)
    for k in range(n):
        s += term * x**k
        term = term * (a + k) * (b + k) / ((c + k) * (k + 1))
    return s
x = -t**3
c = expand(series(t * F(Rational(2,3), Rational(2,3), Rational(4,3), x, 6) / F(Rational(1,3), Rational(1,3), Rational(2,3), x, 6), t, 0, N).removeO())
# invert w = c(t): t = w + ...
tinv = w
for _ in range(5):
    tinv = expand(series(w - (c.subs(t, tinv) - tinv), w, 0, N).removeO())
J = 27 * t**3 * (8 - t**3)**3 / (1 + t**3)**3
Jw = expand(series(J.subs(t, tinv), w, 0, 13).removeO())
print("(a) j in the flat coordinate:", [Jw.coeff(w, k) for k in (3, 6, 9, 12)])
print("    j in t:", [expand(series(J, t, 0, 13).removeO()).coeff(t, k) for k in (3, 6, 9, 12)])
# (b) Hesse t at j = 1728
for tv in (-1 - sqrt(3), -1 + sqrt(3)):
    print("(b) t =", tv, " j =", simplify(J.subs(t, tv)), " norm of t in Q(sqrt3):", simplify(tv * (-2 - tv)))
print("    j - 1728 factor:", factor(J - 1728))
# (e) alternating forms invariant under the S6 monodromies A1, A2 (S6_02_PUSH conventions)
A1 = Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
E = zeros(4); E[3, 0] = 1     # E = delta-hat (x) gamma: e_4 e_1^T
Wm = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[-2,0,0,1]])  # I - 2E
print("    check orders: A1^3 = I:", A1**3 == Matrix.eye(4), " A2^4 = I:", A2**4 == Matrix.eye(4), " I-2E:", Wm == Matrix.eye(4) - 2*E)
v = symbols('o0:6')
O = Matrix([[0, v[0], v[1], v[2]], [-v[0], 0, v[3], v[4]], [-v[1], -v[3], 0, v[5]], [-v[2], -v[4], -v[5], 0]])
eqs = []
for M in (A1, A2):
    eqs += list(M.T * O * M - O)
sol = solve(eqs, v, dict=True)
print("(e) alternating forms invariant under A1, A2:", sol)
if sol:
    Os = O.subs(sol[0])
    print("    general invariant form:", Os, " det:", factor(Os.det()))
    print("    also invariant under I-2E:", simplify(Wm.T * Os * Wm - Os) == zeros(4))

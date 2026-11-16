"""The invariant alternating form Omega = 6 e1^e4 + e2^e3 of the S6 monodromy (A1, A2, I-2E) against the fibre periods
Pi_c = ((6mu, tau, 1, 0), (beta, mu, 0, 1)) (S6_02_PUSH conventions): first Riemann relation, Hermitian form, real
period determinant."""
from sympy import symbols, Matrix, I, simplify, conjugate, re, im, expand, factor
a1, a2, m1, m2, b1, b2 = symbols('a1 a2 m1 m2 b1 b2', real=True)
tau, mu, beta = a1 + I*a2, m1 + I*m2, b1 + I*b2
Pi = Matrix([[6*mu, tau, 1, 0], [beta, mu, 0, 1]])
Om = Matrix([[0, 0, 0, 6], [0, 0, 1, 0], [0, -1, 0, 0], [-6, 0, 0, 0]])
Oi = Om.inv()
print("Pi Om^-1 Pi^T =", simplify(Pi * Oi * Pi.T))
H = (I * Pi * Oi * Pi.conjugate().T).applyfunc(lambda z: simplify(expand(z)))
print("H = i Pi Om^-1 conj(Pi)^T =", H)
print("det H =", factor(simplify(H.det())), "  [D = b2 - 6 m2^2/a2]")
R = Matrix.vstack(Pi.applyfunc(lambda z: re(z)), Pi.applyfunc(lambda z: im(z)))
print("real period determinant =", factor(simplify(R.det())))
print("Pfaffian of Omega = 6 -> for a line bundle with this class, L^2 = 2 (-1)^s Pf = +12 (s=0) or -12 (s=1)")

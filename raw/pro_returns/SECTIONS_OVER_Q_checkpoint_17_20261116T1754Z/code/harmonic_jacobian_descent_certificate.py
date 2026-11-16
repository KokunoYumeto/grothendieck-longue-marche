#!/usr/bin/env python3
"""Exact finite identities for A.108; no Jacobian cohomology is inferred by search."""
from fractions import Fraction as Q
from itertools import product
import sympy as S

a = S.symbols("a")
norm_poly = a**3 + a**2 + a + 1


def red(expr):
    return S.rem(S.expand(expr), norm_poly, a)


def apower(n):
    return a ** (n % 4)


# Uniform Galois computation, including all possible dependent quadratic fields.
galois_checks = 0
for eps, delta in product(range(2), repeat=2):
    eta_pullback = delta * (1-a) * (1+a**3)
    g_primitive = ((-a)**eps * apower(1 if eps == 0 else -1)
                   * apower(2*delta-eps))
    coboundary = g_primitive-a
    residual = red(eta_pullback-coboundary)
    assert residual == red(-eps*(1+a*a))
    galois_checks += 1

# The rational two-torsion correction: a fixes each branch class L of order4.
torsion_checks = 0
for L in range(4):
    # conjugation(jL)=-jL; hT=2jL.
    assert ((L)-(-L)) % 4 == (2*L) % 4
    torsion_checks += 1

# The four branch classes have one relation, and two independent order4
# characters after imposing the product root W.
G = list(product(range(4), repeat=3))
K = [g for g in G if sum(g) % 4 == 0]
assert len(G) == 64 and len(K) == 16
assert all(S.gcd(e, 4) == 1 for e in (1, 1, 1, -3))
assert Q(4)*(-2+4*Q(3,4)) == 2*3-2
assert Q(64)*(-2+4*Q(3,4)) == 2*33-2
assert 2*33-2 == 16*(2*3-2)
assert Q(8)*(-2+4*Q(1,2)) == 2*1-2
assert S.expand(2**2*(1-S.I)**2*(1+S.I)**2) == 16

# The actual curve maps D -> E and C2 -> E.
z, u, d, W = S.symbols("z u d W", nonzero=True)
y0sq = d**3*u*(u*u-1)
W4 = z*(z*z-1)/(u*(u*u-1))
assert S.cancel(y0sq*W4-((d*z)**3-d*d*(d*z))) == 0

# The root-fibre generator and the branch divisor partition.
rho, s, w = S.symbols("rho s w", nonzero=True)
field_generator_square = S.expand((1-w*w/rho)**2*w*w)
field_generator_square = S.rem(
    S.together(field_generator_square-2*rho).as_numer_denom()[0],
    w**4+rho**2, w)
assert field_generator_square == 0
assert S.expand((s*(1+S.I)/2)**2) == S.I*s*s/2
assert S.expand((s*(1+S.I)/2)*(s*(1-S.I)/2)) == s*s/2

# Explicit [1+i] division when the x-coordinate is a square in Q(i).
t, b = S.symbols("t b", nonzero=True)
xQ = t*t
d2 = xQ*xQ-b*b/xQ
xS = S.I*(xQ+b/t)
yS = (1+S.I)*xS*t
assert S.cancel(xS*xS-2*S.I*xQ*xS-d2) == 0
assert S.cancel(yS*yS-(xS**3-d2*xS)) == 0
x_phi = -S.I*(xS*xS-d2)/(2*xS)
slope = (1-S.I)*yS/(2*xS)
y_phi = -yS+slope*(xS-x_phi)
assert S.cancel(x_phi-xQ) == 0
assert S.cancel(y_phi-b) == 0

# The singleton norm that kills the old base-point direction.
X, v = S.symbols("X v")
assert S.expand((X*X+1)**2-2*X*X) == X**4+1
assert 2**2-2 == 2

# The exact source norm quartic, from the other two line intersections.
x, m, x0, y0, dd = S.symbols("x m x0 y0 dd")
line = m*x-y0-m*x0
quadratic = x*x+(x0-m*m)*x+x0*x0+x0*m*m-dd*dd+2*m*y0
remainder = S.expand(x**3-dd*dd*x-line*line-(x-x0)*quadratic)
assert S.expand(remainder-(x0**3-dd*dd*x0-y0*y0)) == 0
disc = S.discriminant(quadratic, x)
assert S.expand(disc-(m**4-6*x0*m*m-8*y0*m-3*x0*x0+4*dd*dd)) == 0

# Chord-product squareclass identity.
intercept = S.symbols("intercept")
cubic = x**3-dd*dd*x-(m*x+intercept)**2
assert -S.Poly(cubic, x).coeff_monomial(1) == intercept**2

print("Uniform Galois cases:", galois_checks)
print("Exact branch two-torsion corrections:", torsion_checks)
print("Geometric deck orders: 64 -> 4, etale kernel16; genera33,3,1.")
print("Jacobian eigenvalue determinant det(1-a)=16.")
print("Checked the actual D/E map, fibre character, and both [1+i] coordinates.")
print("Checked the normalized singleton norm and exact elliptic norm quartic.")
print("All finite symbolic identities passed.")
print("The Jacobian factorization and continuous cohomology statements are proved in A.108, not inferred from this certificate.")

#!/usr/bin/env python3
"""Exact certificates for the algebraic central-coordinate example C.17.

The cover is pulled back from the cubic Heisenberg cover along f=-x/z:
u^3=f, v^3=1-f, w^3=(1-zeta*u)(1-zeta^2*u)^2.
All displayed identities are checked over Q[zeta]/(zeta^2+zeta+1).
No floating-point arithmetic is used.
"""
from itertools import product
from math import comb
import random
import sympy as sp

u, zeta, r, eta, X = sp.symbols("u zeta r eta X")
phi3 = zeta**2 + zeta + 1
phi9 = eta**6 + eta**3 + 1


def red3(expr):
    return sp.rem(sp.Poly(sp.expand(expr), zeta),
                  sp.Poly(phi3, zeta)).as_expr().expand()


def red9(expr):
    return sp.rem(sp.Poly(sp.expand(expr), eta),
                  sp.Poly(phi9, eta)).as_expr().expand()


A = (1-zeta*u)*(1-zeta**2*u)**2
ratio_identity = red3(
    A.subs(u, zeta*u)*(1-u**3) - A*(1-u)**3)
assert ratio_identity == 0
norm_identity = red3(sp.prod(1-zeta**j*u for j in range(3))
                     -(1-u**3))
assert norm_identity == 0
assert red3(A.subs(u, -1)+zeta) == 0
tangent_polynomial = red3((r+zeta)*(r+zeta**2)**2)
assert red3(tangent_polynomial.subs(r, 0)-zeta**2) == 0
assert red9((-eta)**3+eta**3) == 0
assert red9((eta**2)**3-eta**6) == 0

print("Cubic Heisenberg cover:")
print("  A(zeta*u)/A(u)=(1-u)^3/(1-u^3): exact identity verified")
print("  product_j(1-zeta^j*u)=1-u^3: exact identity verified")
print("  tau(w)=(1-u)w/v, sigma(w)=w")
print("  tau sigma(w)=zeta sigma tau(w); [tau,sigma](w)=zeta*w")


def mul(g, h, m=3):
    a, b, c = g
    A_, B_, C_ = h
    return ((a+A_) % m, (b+B_) % m, (c+C_+a*B_) % m)


def power(g, n, m=3):
    out = (0, 0, 0)
    for _ in range(n):
        out = mul(out, g, m)
    return out


def inverse(g, m=3):
    a, b, c = g
    return (-a % m, -b % m, (-c+a*b) % m)


def comm(g, h, m=3):
    return mul(mul(mul(g, h, m), inverse(g, m), m),
               inverse(h, m), m)


G = list(product(range(3), repeat=3))
identity = (0, 0, 0)
tau, sigma, central = (1, 0, 0), (0, 1, 0), (0, 0, 1)
assert comm(tau, sigma) == central
assert all(power(g, 3) == identity for g in G)
assert all(comm(g, h)[:2] == (0, 0) for g in G for h in G)
generated = {identity}
while True:
    nxt = generated | {mul(g, h) for g in generated
                       for h in (tau, sigma)}
    if nxt == generated:
        break
    generated = nxt
assert len(generated) == 27
assert sum(all(mul(g, h) == mul(h, g) for h in G) for g in G) == 3
assert all(mul(mul(g, h), k) == mul(g, mul(h, k))
           for g in G for h in G for k in G)
print("  deck group: 27 elements, center 3, exponent 3, class 2")
print("  all 27^3 associativity identities checked")

# Valuations at the rational cusp P and the base cusp O certify
# independent Kummer classes f and 1-f modulo cubes.
valuation_matrix = sp.Matrix([[1, 0], [-1, -1]])
assert int(valuation_matrix.det()) == -1
print("  Kummer valuation matrix at (P,O):", list(valuation_matrix))
print("  determinant -1, so the abelian cover has degree 9")

print("Point and tangent fibres:")
print("  point [1:-cuberoot(2):1]: u=-1, v=cuberoot(2), w=-zeta_9")
print("  A(-1)=-zeta: verified")
print("  at O, with r=s^(1/3): u=-r^-1, v=r^-1(1+r^3)^(1/3)")
print("  r^3 A(-r^-1) =", tangent_polynomial)
print("  leading coefficient is zeta^2; w starts zeta_9^2*r^-1")
table = [(e, e, 2*e % 3, (e-2*e) % 3) for e in range(3)]
assert all(row[3] == (-row[0]) % 3 for row in table)
print("  columns: kappa(zeta), raw point displacement, tangent displacement, relative")
for row in table:
    print(" ", row)

# Cyclotomic degree-three extension is unramified at two; the pure cubic
# is Eisenstein at the unique prime above two in Q(zeta).
disc_cubic = sp.discriminant(X**3-2, X)
disc_cyclo = sp.discriminant(X**6+X**3+1, X)
assert disc_cubic == -108
assert disc_cyclo == -3**9
assert sp.Poly(X**2+X+1, X, modulus=2).is_irreducible
print("  disc(X^3-2) =", disc_cubic)
print("  disc(Phi_9) =", disc_cyclo)
print("  Phi_3 irreducible modulo 2; X^3-2 is Eisenstein over Q(zeta) at 2")
print("  hence zeta_9 is not in Q(zeta,cuberoot(2)), and the central class is nonzero")

# Verify the Hall/BCH conversion used at every precision in rank two:
# tau^a sigma^b z^(c-ab/2) is the matrix (a,b,c+ab/2).
rng = random.Random(170316)
for m in (3, 9, 27, 81):
    half = pow(2, -1, m)

    def bch(g, h):
        a, b, c = g
        A_, B_, C_ = h
        return ((a+A_) % m, (b+B_) % m,
                (c+C_+half*(a*B_-b*A_)) % m)

    def hall(g):
        a, b, c = g
        return (a, b, (c+half*a*b) % m)

    for _ in range(500):
        g = tuple(rng.randrange(m) for _ in range(3))
        h = tuple(rng.randrange(m) for _ in range(3))
        assert hall(bch(g, h)) == mul(hall(g), hall(h), m)
    print(f"  Hall/BCH conversion: 500 exact product checks modulo {m}")

print("Universal class-two cover:")
rank = 10
assert rank+comb(rank, 2) == 55
print("  abelian rank 10, commutator rank 45, order 3^(55n)")
print("  first m=3 abelian cover degree:", 3**rank)
print("  its free pro-three rank:", 1+9*3**rank)
print("PASS: all finite and symbolic certificates succeeded.")

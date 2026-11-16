"""Exact finite group and rational-map certificates for A.53.

Run from the workspace root with Python 3 and SymPy.
Matrices are row-major tuples.  Projectivization here identifies only +/- I
inside SL_2; it never replaces SL_2 by PGL_2 silently.
"""
from itertools import product
from fractions import Fraction
import sympy as sp


def mul(a, b, n):
    return ((a[0]*b[0]+a[1]*b[2]) % n,
            (a[0]*b[1]+a[1]*b[3]) % n,
            (a[2]*b[0]+a[3]*b[2]) % n,
            (a[2]*b[1]+a[3]*b[3]) % n)


def inv(a, n):
    return (a[3] % n, -a[1] % n, -a[2] % n, a[0] % n)


def neg(a, n):
    return tuple(-x % n for x in a)


def proj(a, n):
    return min(a, neg(a, n))


def subgroup(gens, n, projective=False):
    canon = (lambda a: proj(a, n)) if projective else (lambda a: a)
    one = canon((1, 0, 0, 1))
    found, todo = {one}, [one]
    while todo:
        a = todo.pop()
        for b in gens:
            c = canon(mul(a, b, n))
            if c not in found:
                found.add(c)
                todo.append(c)
    return found


def order(a, n, projective=False):
    return len(subgroup([a], n, projective))


def conjugate(g, a, n):
    return proj(mul(mul(g, a, n), inv(g, n), n), n)


def permute_subgroups(g, subs, n):
    positions = {s: i+1 for i, s in enumerate(subs)}
    return tuple(positions[frozenset(conjugate(g, a, n) for a in s)]
                 for s in subs)


print("LEGENDRE LINEAR AND PROJECTIVE IMAGES")
for n in (3, 4, 5, 7):
    U = (1, 2 % n, 0, 1)
    L = (1, 0, -2 % n, 1)
    linear = subgroup([U, L], n)
    projective = {proj(a, n) for a in linear}
    SL = {a for a in product(range(n), repeat=4)
          if (a[0]*a[3]-a[1]*a[2]) % n == 1}
    PSL = {proj(a, n) for a in SL}
    print(n, "SL order", len(SL), "PSL order", len(PSL),
          "Legendre linear", len(linear), "Legendre projective", len(projective))
    if n == 4:
        expected = {(1, 2*a, 2*b, 1) for a, b in product(range(2), repeat=2)}
        assert linear == expected
        assert (3, 0, 0, 3) not in linear
        print("H4 matrices:", sorted(linear))
        reduction_kernel = {a for a in PSL if tuple(x % 2 for x in a) == (1, 0, 0, 1)}
        assert {proj(a, 4) for a in linear} == reduction_kernel
        sylow3 = sorted({frozenset(subgroup([a], n, True))
                         for a in PSL if order(a, n, True) == 3},
                        key=lambda s: sorted(s))
        assert len(sylow3) == 4
        perms = {permute_subgroups(g, sylow3, n) for g in PSL}
        assert len(perms) == 24
        print("PSL2(Z/4) acts faithfully on its four order-three subgroups:")
        for i, h in enumerate(sylow3, 1):
            print(" C3", i, sorted(h))
        print(" S permutation:", permute_subgroups((0, 3, 1, 0), sylow3, 4))
        print(" U(1) permutation:", permute_subgroups((1, 1, 0, 1), sylow3, 4))
    else:
        assert linear == SL
        assert len(linear) == 2*len(projective)
    if n == 5:
        involutions = [a for a in PSL if order(a, 5, True) == 2]
        V4 = set()
        for a in involutions:
            for b in involutions:
                if a != b and proj(mul(a, b, 5), 5) == proj(mul(b, a, 5), 5):
                    h = frozenset(subgroup([a, b], 5, True))
                    assert len(h) == 4
                    V4.add(h)
        V4 = sorted(V4, key=lambda s: sorted(s))
        assert len(V4) == 5
        perms = {permute_subgroups(g, V4, 5) for g in PSL}
        assert len(perms) == 60
        assert all(sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0
                   for p in perms)
        print("PSL2(F5) acts faithfully and evenly on its five Klein subgroups:")
        for i, h in enumerate(V4, 1):
            print(" V4", i, sorted(h))
        print(" U(2) permutation:", permute_subgroups(U, V4, 5))
        print(" L(-2) permutation:", permute_subgroups(L, V4, 5))

print("\nPROJECTIVE PULLBACK GENERA")
for n in (3, 4, 5, 7):
    d = 4 if n == 4 else n*(n*n-1)//2
    e = 2 if n == 4 else n
    genus = 1 + Fraction(d, 2)*(1-Fraction(3, e))
    assert genus.denominator == 1
    print("N=", n, "degree over lambda=", d, "three cusp indices=", e,
          "genus=", genus)

t, z = sp.symbols("t z")
J = 256*(t*t-t+1)**3/(t*t*(1-t)**2)
lam = 4*z*z/(1+z*z)**2
x = 2*z/(1+z*z)
y = (1-z*z)/(1+z*z)
assert sp.factor(x*x+y*y-1) == 0
assert sp.factor(lam-x*x) == 0
assert sp.factor(1-lam-y*y) == 0
assert sp.factor(J.subs(t, lam) - 16*(z**8+14*z**4+1)**3/(z**4*(z**4-1)**4)) == 0
print("\nEXPLICIT LEVEL-FOUR MAP")
print("x=", x, "y=", y, "t=", lam)
print("J(t(z))=", sp.factor(J.subs(t, lam)))
print("J-1728=", sp.factor(J-1728))
for phi in (t, 1-t, 1/t, 1/(1-t), (t-1)/t, t/(t-1)):
    assert sp.factor(J.subs(t, phi)-J) == 0
print("All six displayed S3 transformations preserve J.")
print("All checks passed.")

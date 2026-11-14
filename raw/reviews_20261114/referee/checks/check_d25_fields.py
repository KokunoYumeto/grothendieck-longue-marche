"""Referee B check: the field and sign identities behind the CM parity (LM7 D.25.1, its sign rule, and the
Legendre-fibre twists of LM7 D.15 that the Galois vanishing in E.65 needs).

Written by Claude Opus 5.5 at effort max, 14 Nov 2026.  Run: python -I -B check_d25_fields.py
"""
import sympy as sp

FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILS.append(name)

s3 = sp.sqrt(3)
r0 = sp.root(sp.Rational(3, 4), 4)
X, Y, lam = sp.symbols('X Y lambda')

print("== E3: y^2 = x^3 + 1, halves of 2-torsion and four-torsion field ==")
for sign in (1, -1):
    x = -(1 + sign*s3)          # e = -1, x = e(1 +- sqrt3)
    y2 = sp.expand(x**3 + 1)
    check("x = -(1%ssqrt3): y^2 = %s" % ('+' if sign > 0 else '-', y2), sp.simplify(y2 - (-9 - sign*6*s3)) == 0)
    # it is a half of (-1,0): duplication x-coordinate
    xd = sp.simplify(((3*x**2)**2/(4*y2)) - 2*x)
    check("  2P has x = -1 (P a half of (-1,0))", sp.simplify(xd + 1) == 0)
yP = s3*(s3 - 1)*r0
check("y = sqrt3 (sqrt3 - 1) r0 squares to -9 + 6 sqrt3", sp.simplify(sp.expand(yP**2) - (-9 + 6*s3)) == 0)
check("(-9 + 6 sqrt3)(-9 - 6 sqrt3) = -27 = (3 sqrt(-3))^2", sp.expand((-9 + 6*s3)*(-9 - 6*s3)) == -27)
# addition law: y(P) = x(P)^2/4 (x(P - Q0) - x(P + Q0)), Q0 = (0,1), for a generic point
xp, yp = sp.symbols('xp yp')
lp = (yp - 1)/xp; lm = (yp + 1)/xp
xplus = lp**2 - xp; xminus = lm**2 - xp
check("addition law: x(P-Q0) - x(P+Q0) = 4 y(P)/x(P)^2 (generic P, Q0 = (0,1))", sp.simplify(xminus - xplus - 4*yp/xp**2) == 0)
check("Q0 = (0,1) has order 3 on y^2 = x^3 + 1 (tangent line y = 1 meets with multiplicity 3)", sp.factor(sp.Integer(1) - (X**3 + 1)) == -X**3)

print("== E4: y^2 = x^3 - x, three-division polynomial ==")
a_, b_ = -1, 0
psi3 = 3*X**4 + 6*a_*X**2 + 12*b_*X - a_**2
check("psi_3 = 3x^4 - 6x^2 - 1", sp.expand(psi3 - (3*X**4 - 6*X**2 - 1)) == 0)
A = sp.sqrt(1 + 2/s3); B = sp.sqrt(1 - 2/s3)   # B is imaginary
check("a^2 = 1 + 2/sqrt3 and b^2 = 1 - 2/sqrt3 are roots of psi_3 in x^2", all(sp.simplify(psi3.subs(X, v)) == 0 for v in (A, B)))
AB = sp.simplify(sp.expand((1 + 2/s3)*(1 - 2/s3)))
check("(ab)^2 = -1/3, so ab = +-i/sqrt3", AB == sp.Rational(-1, 3))
a, b, w = sp.symbols('a b w')
# with a^2 = 1+2/s3, b^2 = 1-2/s3, ab = i/s3: w = a + i b
w2 = sp.expand((1 + 2/s3) - (1 - 2/s3) + 2*sp.I*(sp.I/s3))
check("w^2 = a^2 - b^2 + 2i ab = 2/sqrt3, so w^4 = 4/3", sp.simplify(w2 - 2/s3) == 0 and sp.simplify(w2**2 - sp.Rational(4, 3)) == 0)
# a = (w + 2/w)/2, b = (w - 2/w)/(2i) given w = a + i b and a^2 + b^2 = 2, ab = i/sqrt3? check algebraically:
# 2/w = 2 conj... use the identity (a+ib)(a-ib) = a^2 + b^2 = 2
check("a^2 + b^2 = 2, so 2/w = a - i b and the recovery formulas hold", sp.simplify((1 + 2/s3) + (1 - 2/s3) - 2) == 0)
check("w^4 = 4/3 = r0^{-4}: Q(i, w) = Q(i, r0)", sp.simplify(r0**4 - sp.Rational(3, 4)) == 0)

print("== the two Legendre CM fibres (LM7 D.15) ==")
x = sp.symbols('x')
leg = lambda l: x*(x - 1)*(x - l)
# lambda = 1/2: X = 4x - 2, Y = 8y gives Y^2 = X^3 - 4X
expr = sp.expand(64*leg(sp.Rational(1, 2)).subs(x, (X + 2)/4))
check("lambda = 1/2: 64 x(x-1)(x-1/2) with x = (X+2)/4 equals X^3 - 4X", sp.expand(expr - (X**3 - 4*X)) == 0)
# lambda0 root of l^2 - l + 1: shift x by (1+l)/3
l0 = (1 + sp.sqrt(-3))/2
check("lambda0 = (1+sqrt(-3))/2 satisfies l^2 - l + 1 = 0", sp.simplify(l0**2 - l0 + 1) == 0)
shifted = sp.expand(leg(l0).subs(x, X + (1 + l0)/3))
poly = sp.Poly(shifted, X)
c2, c1, c0 = [sp.simplify(poly.coeff_monomial(X**k)) for k in (2, 1, 0)]
check("shifted Legendre at lambda0 has no X^2 and no X term", c2 == 0 and c1 == 0)
check("constant term = (2 lambda0 - 1)/9", sp.simplify(c0 - (2*l0 - 1)/9) == 0)
cp = -(2*l0 - 1)/3
check("(2 lambda0 - 1)/9 = c'^3 with c' = -(2 lambda0 - 1)/3", sp.simplify(cp**3 - (2*l0 - 1)/9) == 0)
check("c' = -sqrt(-3)/3 = 1/sqrt(-3)", sp.simplify(cp - 1/sp.sqrt(-3)) == 0)
# sqrt(c')^4 = c'^2 = -1/3: so sqrt(c') = (-3)^(-1/4) up to a fourth root of unity; (-3)^(1/4) = zeta8 * 3^(1/4)
check("(sqrt c')^4 = -1/3, i.e. sqrt c' generates Q(i)((-3)^{1/4}) = Q(i, 3^{1/4}) over Q(i, sqrt2)", sp.simplify(cp**2 + sp.Rational(1, 3)) == 0)
check("3^{1/4} = sqrt2 * r0", sp.simplify(sp.root(3, 4) - sp.sqrt(2)*r0) == 0)

print()
print("TOTAL FAILS:", len(FAILS))
for f in FAILS:
    print("  ", f)

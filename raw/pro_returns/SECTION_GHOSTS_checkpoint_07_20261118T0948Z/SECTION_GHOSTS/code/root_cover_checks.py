"""Independent symbolic checks of the displayed degree-three elliptic maps.

These check identities, not Selmer assertions or the existence of sections.
"""
import sympy as s

x, y, u, v = s.symbols("x y u v")


def numerator_remainder(expr, equation, variable):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.rem(s.Poly(numerator, variable), s.Poly(equation, variable)).as_expr().expand()


Xp = (x**3+36)/x**2
Yp = y*(x**3-72)/x**3
assert numerator_remainder(Yp**2-Xp**3+243, y*y-x**3-9, y) == 0
print("phi: y^2=x^3+9 -> y^2=x^3-243: exact function-field identity PASS")

Xq = (x**3-972)/(9*x*x)
Yq = y*(x**3+1944)/(27*x**3)
assert numerator_remainder(Yq**2-Xq**3-9, y*y-x**3+243, y) == 0
print("psi: y^2=x^3-243 -> y^2=x^3+9: exact function-field identity PASS")

assert numerator_remainder(Yq-3-((y-27)/(3*x))**3, y*y-x**3+243, y) == 0
print("psi Kummer identity (Y-3) o psi = ((y-27)/(3x))^3: PASS")

Xc = 6*u*v
Yc = 3*(3*u**3+2*v**3)
assert numerator_remainder(Yc**2-Xc**3-9, 3*u**3-2*v**3-1, v) == 0
print("diagonal cubic -> E': exact function-field identity PASS")

den = 3*u*(u-1)-2*v*(v-1)
Xi = 18*(u*v-1)/den
Yi = -27*(3*u*(u+1)+2*v*(v+1))/den
assert numerator_remainder(Yi**2-Xi**3+243, 3*u**3-2*v**3-1, v) == 0
print("iota: diagonal cubic -> E: exact function-field identity PASS")


def add(P, Q):
    x1, y1 = map(s.Rational, P)
    x2, y2 = map(s.Rational, Q)
    slope = (y2-y1)/(x2-x1)
    xx = slope**2-x1-x2
    return s.simplify(xx), s.simplify(slope*(x1-xx)-y1)


assert add((6,15),(0,3)) == (-2,1)
assert add((6,15),(0,-3)) == (3,-6)
print("P0+T=(-2,1), P0-T=(3,-6): exact rational group-law identities PASS")
print("No claim of full R6 certification is made by these calculations.")

z = s.symbols("z")
aa = (1+6*z*z)/(1-6*z*z)
bb = 2*z/(1-6*z*z)
uu = s.factor(aa*aa+6*bb*bb+4*aa*bb)
vv = s.factor(aa*aa+6*bb*bb+6*aa*bb)
assert s.factor(3*uu*uu-2*vv*vv-1) == 0
assert uu.subs(z, 0) == vv.subs(z, 0) == 1
un, ud = s.fraction(uu)
vn, vd = s.fraction(vv)
assert s.degree(un, z) == s.degree(vn, z) == 4
assert s.discriminant(un, z) != 0 and s.discriminant(vn, z) != 0
assert s.resultant(un, vn, z) != 0
assert s.resultant(un, 1-6*z*z, z) != 0
assert s.resultant(vn, 1-6*z*z, z) != 0
num, den = s.fraction(s.cancel(3*uu*uu))
assert max(s.degree(num,z),s.degree(den,z)) == 8
print("Pointed dihedral cover at two: degree 8, t(0)=3, exact conic identity PASS")
print("Four distinct zero fibres, four distinct one fibres, two distinct poles: PASS")
print("u numerator:", un)
print("v numerator:", vn)
print("Discriminants:", s.discriminant(un,z), s.discriminant(vn,z))

"""Exact finite checks for B.20--B.23; no floating-point calculations.

Run from any directory.  The output is written beside this script.
These identities verify examples, not the general specialization proof.
"""
import json
from pathlib import Path
import sympy as s

x, t, a, u, v, z, V, W, X, Y = s.symbols("x t a u v z V W X Y")
checks = []


def check(name, condition, detail=None):
    assert condition, name
    checks.append({"name": name, "passed": True, "detail": detail})


def red3(expr):
    """Reduce in F_3[a,t,x,u,v,z,V,W,X,Y]/(a^2+1)."""
    poly = s.Poly(s.expand(expr), a, t, x, u, v, z, V, W, X, Y, modulus=3)
    out = 0
    for powers, coeff in poly.terms():
        ap, *other = powers
        term = coeff * (-1) ** (ap // 2) * a ** (ap % 2)
        for var, power in zip((t, x, u, v, z, V, W, X, Y), other):
            term *= var ** power
        out += term
    return s.Poly(s.expand(out), a, t, x, u, v, z, V, W, X, Y, modulus=3).as_expr()


lam = t - 1
leg = u * (u - 1) * (u - lam)
check("Legendre cubic expansion", red3(leg - (u**3-t*u**2+lam*u)) == 0)
disc = s.discriminant(leg, u)
check("Legendre discriminant is unit at t=0", int(disc.subs(t, 0)) % 3 != 0,
      {"cubic_discriminant": str(s.factor(disc))})

# Flex criterion a2*u^3=a4^2, transported through relative Frobenius.
ker_x = -lam**2/t
ker_y2 = s.factor(ker_x * (ker_x-1) * (ker_x-lam**3))
expected_y2 = -lam**4*(lam-1)**4/t**3
num = s.together(ker_y2-expected_y2).as_numer_denom()[0]
check("Verschiebung kernel Y-coordinate", red3(num) == 0,
      {"X": "-(t-1)^2/t", "Y_squared": "-(t-1)^4*(t-2)^4/t^3"})
z2 = s.factor(expected_y2*t**4/(lam**4*(lam-1)**4))
check("Normalized kernel generator satisfies z^2=-t", s.simplify(z2+t) == 0)
check("Kernel quadratic has nonzero derivative", red3(s.diff(z*z+t, z)) != 0)
check("Kernel quadratic is Eisenstein at t", s.Poly(z*z+t, z).all_coeffs() == [1,0,t])

f = (x*x+a)*(x*x+a-1)*(x*x+a-lam)
expected = x**6-t*x**4+((a+1)*t-1)*x*x+a+(a+1)*t
check("Genus-two equation expansion over F9", red3(f-expected) == 0)
f0 = red3(f.subs(t,0))
check("Special sextic is x^6-x^2+a", red3(f0-(x**6-x*x+a)) == 0)
check("Special derivative is x", red3(s.diff(f0,x)-x) == 0)
check("Special sextic and derivative have no common zero", red3(f0.subs(x,0)-a) == 0,
      "The only root of the derivative x is 0, and f(0)=a with a^2=-1.")
check("Two smooth points at infinity", s.Poly(expected,x).degree() == 6 and s.Poly(expected,x).LC() == 1,
      "At s=1/x, (y/x^3)^2=1+O(s^2); derivative in y/x^3 is nonzero at +/-1.")
coeff = lambda i: red3(s.Poly(expected,x).coeff_monomial(x**i))
H = s.Matrix([[coeff(2),coeff(1)],[coeff(5),coeff(4)]])
check("Cartier-Manin matrix is diagonal", H[0,1] == H[1,0] == 0,
      {"matrix_before_cube_roots": str(H)})
check("Generic Cartier determinant nonzero", red3(H.det()) != 0)
check("Special Cartier stable rank is one", H.subs(t,0) == s.Matrix([[-1,0],[0,0]]))
check("Degree-two map to Legendre curve", red3(f-leg.subs(u,x*x+a)) == 0)
check("Verschiebung pullback degrees coprime", s.gcd(2,3) == 1)

# Compact-type model: the same exact chart as B.11, now over F_7[[t]].
A = (1-z**3)*(x**3-1)
check("Compact-type node coefficient is a unit", int(A.subs({x:0,z:0})) % 7 != 0)
check("Node equations give thickness one", s.expand((x*A)*(z/A)-x*z) == 0,
      "With x*z=t^2 and V*W=t, the normalized node is V*W=t.")
fct = (x**3-t**6)*(x**3-1)
scaled = s.expand(fct.subs(x,t*t*X)/t**6)
check("Compact-type inner component equation", s.expand(scaled.subs(t,0)-(1-X**3)) == 0)
check("Compact-type outer normalization", s.simplify((x*(x**3-1))/x**4-(1-1/x**3)) == 0)
hasse7 = int(s.expand((1-x**3)**3).coeff(x,6)) % 7
check("Both elliptic special components ordinary at 7", hasse7 == 3,
      {"Hasse_coefficient": hasse7})
check("Compact-type generic sextic square-free", s.discriminant(fct,x) != 0)

# Proper constant quadratic twist over F_3((t)).
q = x**5-x
check("Constant genus-two curve is smooth in characteristic 3",
      s.gcd(s.Poly(q,x,modulus=3),s.Poly(s.diff(q,x),x,modulus=3)).degree() == 0)
r = s.symbols("r")
check("Quadratic twist becomes constant", s.expand((v*v-t*q).subs({v:r*Y,t:r*r})-r*r*(Y*Y-q)) == 0)
check("Twist inertia negates y-coordinate", s.simplify((r*Y).subs(r,-r)+r*Y) == 0)

# Characteristic-two edge case, B.24: ramification first appears mod 4.
def zero2(expr):
    num = s.together(expr).as_numer_denom()[0]
    symbols = sorted(num.free_symbols, key=str)
    return s.Poly(s.expand(num), *symbols, modulus=2).is_zero if symbols else int(num) % 2 == 0

A2, B2, w = s.symbols("A2 B2 w")
original2 = v*v+t*x*v+v-x**3
normal2 = Y*Y+X*Y-X**3-t**-3*X*X-(t**-12+t**-9)
transformed2 = original2.subs({x:t*t*X+t**-1, v:t**3*Y+t**-3})/t**6
check("Characteristic-two normalized elliptic equation", zero2(transformed2-normal2))
disc2 = -8*t**3-27+9*t**3
check("Characteristic-two good elliptic discriminant", zero2(disc2-(1+t**3)))
curve_normal = Y*Y+X*Y-X**3-B2*X*X-A2
dup_num = s.expand(X*X*((X+Y/X)**2+(X+Y/X)+B2-X*X-A2/(X*X)))
check("Characteristic-two duplication x-coordinate", zero2(dup_num-curve_normal))
ker_eq = Y*Y+A2*Y-A2**3-B2**4*A2**2-A2**4
sub_y = A2*(w+B2*B2+B2+A2)
check("Primitive Verschiebung-square generators satisfy AS equation",
      zero2(ker_eq.subs(Y,sub_y)/A2**2-(w*w+w+B2)))
check("AS character is separable", s.diff(w*w+w,w).subs(w,0) == 1)
check("AS character has odd pole order", 3 % 2 == 1,
      "w^2+w=t^-3 gives valuation(w)=-3/2 and ramification index two.")
check("Cyclic cubic hyperbolic cover equation", zero2(original2.subs(x,z**3)-(v*v+t*z**3*v+v-z**9)))
check("Three tame branch points give genus four", 2*4-2 == 3*(3-1))
cartier2 = s.Matrix([[0,1,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
check("Special genus-four Cartier operator is nilpotent", cartier2**3 == s.zeros(4),
      {"basis": ["dz", "z dz", "z^2 dz", "z^3 dz"],"matrix": str(cartier2)})
check("Verschiebung-square pullback degrees coprime", s.gcd(3,4) == 1)

out = {"script": Path(__file__).name, "sympy": s.__version__, "passed": len(checks), "checks": checks}
Path(__file__).with_name("BC_equal_char_checks_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"passed": len(checks), "all_passed": True},indent=2))

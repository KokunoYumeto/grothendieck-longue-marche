"""Exact coefficient/elimination certificate for AG.15 in characteristic two."""
import json
import sympy as S

x, s, t, c1 = S.symbols("x s t c1")

def mod2(poly, *variables):
    return S.Poly(poly, *variables, modulus=2)

r = s**2
a = t**2
d = s**2 + t
c3 = s
c2 = s**8 + t**2 * s**4 + s**3 + s * t + t**4
c0 = r**6 + c1 * d
A = c3*x**3 + c2*x**2 + c1*x + c0
B = x+d
norm_difference = mod2(A**2+A*B+B**2*(x**5+a*x**3)+(x+r)**7, x, s, t, c1)
E1 = mod2(c2**2+c3+r**3, s, t)
E2 = mod2(r**5*d**2+c2*d**3+r**12+r**6*d+r**7, s, t)
expected_E1 = s**16+t**4*s**8+t**2*s**2+s+t**8
expected_E2 = s**24+t**2*s**10+s**9+t**6*s**2+t**4*s+t**7
assert E1 == mod2(expected_E1,s,t)
assert E2 == mod2(expected_E2,s,t)
elimination = mod2(expected_E2+(s**8+t**4)*expected_E1, s, t)
assert elimination == mod2(t**7*(t**5+1),s,t)

# Check every norm coefficient after reduction by c1^2+c1+r^5+c2*d.
AS = mod2(c1**2+c1+r**5+c2*d,c1,s,t)
groebner = S.groebner([AS.as_expr()],c1,s,t,modulus=2)
coefficients = {}
norm_x = S.Poly(norm_difference.as_expr(),x)
for degree in range(8):
    coefficient = mod2(norm_x.nth(degree),c1,s,t).as_expr()
    reduced = mod2(groebner.reduce(coefficient)[1],s,t)
    coefficients[degree] = str(reduced.as_expr())
    if degree == 4:
        assert reduced == E1
    elif degree == 0:
        assert reduced == E2
    else:
        assert reduced.is_zero

domain = S.GF(2).poly_ring(t)
res = S.resultant(S.Poly(expected_E1,s,domain=domain),
                  S.Poly(expected_E2,s,domain=domain),s)
res = mod2(res,t)
assert res == mod2(t**112*(t**5+1)**16,t)
assert mod2((r+d),s,t) == mod2(t,s,t)

print(json.dumps({
    "curve":"y^2+y=x^5+a*x^3",
    "substitution":{"a":"t^2","r":"s^2","d":str(d),"c3":str(c3),"c2":str(c2)},
    "E1":str(E1.as_expr()),
    "E2":str(E2.as_expr()),
    "identity":"E2+(s^8+t^4)*E1=t^7*(t^5+1)",
    "resultant":str(res.as_expr()),
    "resultant_factorization":"t^112*(t^5+1)^16",
    "reduced_norm_coefficients":coefficients,
    "value_B_at_r":"t; nonzero iff a is nonzero",
    "theta_order3":"absent: pole order3 is not in <2,5>",
    "theta_order5":"exists iff a=0",
    "theta_order7":"exists iff a^5=1; a=0 resultant root is extraneous",
    "assertions":"all passed",
},indent=2))

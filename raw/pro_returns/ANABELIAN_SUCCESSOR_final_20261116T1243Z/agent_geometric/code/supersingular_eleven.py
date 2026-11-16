"""Exact local-series/resultant certificate for order-eleven theta points."""
import json
import sympy as S

u,a,v,b0,b1,b2 = S.symbols("u a v b0 b1 b2")
# v=c^4; coefficients below follow from
# y+y^2=u^5+a*u^3+c*u and B=u^3+b2*u^2+b1*u+b0.
# The five required high coefficients have degrees6,...,10.
equations = [
    b0*a**2+b1+b2*v+a,
    b1*a**2+b2+v,
    b0*v**2+b2*a**2+1,
    b1*v**2+a**2,
    b0+b2*v**2,
]
sub = {b2:a**4/v**2+v, b1:a**2/v**2, b0:a**4+v**3}

def clear_mod2(expr):
    num,den = S.fraction(S.cancel(expr))
    return S.Poly(num,a,v,modulus=2).as_expr(),S.Poly(den,a,v,modulus=2).as_expr()

E1 = v**7+a**4*v**4+a**2*v**3+v**2+a**6
E2 = a**2*v**5+v**4+(a**6+a)*v**2+a**4*v+a**2
reduced=[]
for i,e in enumerate(equations):
    num,den = clear_mod2(e.subs(sub))
    reduced.append({"coefficient_degree":i+6,"numerator":str(num),"denominator":str(den)})
    if i==0:assert S.Poly(num-E2,a,v,modulus=2).is_zero
    elif i==2:assert S.Poly(num-E1,a,v,modulus=2).is_zero
    else:assert S.Poly(num,a,v,modulus=2).is_zero

domain=S.GF(2).poly_ring(a)
resultant=S.Poly(S.resultant(S.Poly(E1,v,domain=domain),
                             S.Poly(E2,v,domain=domain),v),a,modulus=2)
assert resultant == S.Poly(a**4*(a**35+a**10+1),a,modulus=2)
# If B(0)=a^4+v^3=0, E1 reduces to v^2, so v cannot be nonzero.
assert S.Poly(E1,v,domain=domain).rem(S.Poly(v**3+a**4,v,domain=domain),auto=False).as_expr()==v**2
print(json.dumps({
    "curve":"y^2+y=x^5+a*x^3",
    "local_form":"y^2+y=u^5+a*u^3+c*u, v=c^4",
    "required_coefficients_degrees6_to10":[str(e) for e in equations],
    "B_coefficients":{str(k):str(z) for k,z in sub.items()},
    "reduced_coefficients":reduced,
    "E1":str(E1),"E2":str(E2),
    "resultant":str(resultant.as_expr()),
    "factorization":"a^4*(a^35+a^10+1)",
    "B0_zero_remainder":"E1 mod (v^3+a^4) = v^2",
    "excluded_case":"a=0 forces v=0 in E2, which was excluded by the degree8 coefficient",
    "conclusion":"Theta contains exact order11 iff a^35+a^10+1=0",
    "assertions":"all passed",
},indent=2))

"""Exact degree-thirteen theta locus for y^2+y=x^5+a*x^3.

All six local coefficient equations are checked symbolically in characteristic
two. The factorization and the independent counting obstruction are exact.
"""
import json
import sympy as s

a, v, b0, b1, b2, b3, t, U = s.symbols("a v b0 b1 b2 b3 t U")
eqs = [b1*a**2+b2+b3*v+a,
       b0*v**2+b2*a**2+b3+v,
       b1*v**2+b3*a**2+1,
       b0+b2*v**2+a**2,
       b1+b3*v**2,
       b0*a**4+b2+v**2]
subs = {a:t**8, v:t**4+t**-1,
        b3:t**4, b2:t**28+t**18+t**3,
        b1:t**12+t**2, b0:t**36+t**11+t}
checks=[]
for index, e in enumerate(eqs):
    num, den=s.fraction(s.together(e.subs(subs)))
    num=s.Poly(num,t,modulus=2).as_expr()
    den=s.Poly(den,t,modulus=2).as_expr()
    checks.append({"coefficient_degree":7+index,
                   "numerator":str(num),"denominator":str(den)})
    if index <5:
        assert num==0
P=U**14+U**9+U**7+U**6+U**4+U**2+U+1
num,den=s.fraction(s.together(eqs[-1].subs(subs)))
assert s.Poly(num-P.subs(U,t**5),t,modulus=2).is_zero
assert s.Poly(den,t,modulus=2).as_expr()==t**2
factors=(U+1)*(U**3+U+1)*(U**4+U+1)*(U**6+U**5+1)
assert s.Poly(P-factors,U,modulus=2).is_zero
assert {pow(2,j,13) for j in range(12)}==set(range(1,13))
f8=s.gcd(s.Poly(P,U,modulus=2),s.Poly(U**8-U,U,modulus=2))
f16=s.gcd(s.Poly(P,U,modulus=2),s.Poly(U**16-U,U,modulus=2))
print(json.dumps({
    "curve":"y^2+y=x^5+a*x^3",
    "local_form":"Y^2+Y=u^5+a*u^3+c*u, v=c^4",
    "function":"A+(u^4+b3*u^3+b2*u^2+b1*u+b0)*Y, deg(A)<=6",
    "coefficient_equations":[str(e) for e in eqs],
    "substitution":{str(k):str(val) for k,val in subs.items()},
    "substitution_checks":checks,
    "theta_condition":"P(a^5)=0",
    "P":str(P),
    "factorization":str(factors),
    "F8_parameter_factor":str(f8.as_expr()),
    "F16_parameter_factor":str(f16.as_expr()),
    "excluded_case":"a=0 is impossible because a*(v^4+a^2)^2=1",
    "assertions":"all passed"
},indent=2))

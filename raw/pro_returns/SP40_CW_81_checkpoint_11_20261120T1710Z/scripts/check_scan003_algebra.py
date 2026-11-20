"""Exact algebra checks of formulas supplied on scan 003; no reading inference."""
import sympy as s
P,Q,Pp,Qp=s.symbols('P Q Pprime Qprime')
a,b,T=s.symbols('a b T')
poly=a*T*T+b*T
checks={
 'NB live numerator':s.expand((Q-P)*Pp+P*(Pp-Qp)-(Q*Pp-P*Qp)),
 'NB struck numerator':s.expand(Q*(Pp-P)+P*(Q-Qp)-(Q*Pp-P*Qp)),
 'margin derivative':s.diff(poly,T)-(2*a*T+b),
 'margin rational critical-value identity':s.cancel(poly.subs(T,-b/(2*a))+b*b/(4*a)),
}
for label,residual in checks.items():
    print(label,': residual',residual)
    assert residual==0

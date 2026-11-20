"""Exact algebraic checks prompted by the source's stabilizer question; no image processing."""
from pathlib import Path
import sympy as s,json
E=s.zeros(3);E[0,1]=1
F=s.zeros(3);F[1,0]=1
H=s.diag(1,-1,0)
a=s.symbols('a0:9');A=s.Matrix(3,3,a)
eq=list(A*E-E*A)+list(A*F-F*A)+[s.trace(A)]
sol=s.linsolve(eq,a)
expected=(a[8]*s.Rational(-1,2),0,0,0,a[8]*s.Rational(-1,2),0,0,0,a[8])
assert tuple(next(iter(sol)))==expected
D=s.diag(1,1,-2)
assert D*E==E*D and D*F==F*D and D*H==H*D and s.trace(D)==0
t=s.symbols('t',nonzero=True);T=s.diag(t,t,t**-2)
assert s.det(T)==1 and T*E==E*T and T*F==F*T
out={'scope':'Characteristic-zero example in SL3: Sl2 acts on the first two coordinates and trivially on the third.',
 'linear_centralizer_solution':[str(x) for x in expected],
 'lie_centralizer_basis':[[str(x) for x in row] for row in D.tolist()],
 'group_centralizer_family':'diag(t,t,t^(-2)); determinant 1, commutes with E12 and E21',
 'conclusion':'This stabilizer has a one-dimensional torus; it is not semisimple. The source asks about semisimplicity and does not assert it.',
 'cancelled_isom_torsor_counterexample':{'group':'SL2 x SL2','embedding':'f(s)=(s,1)','centralizer_dimension':3,'G_orbit_dimension':3,'identity_component_AutG_dimension':6,'scope':'The cancelled canonical Isom-torsor identification fails in this example. No reason for the historical cancellation is inferred.'}}
p=Path('out/math_checks/123_018_stabilizer_certificate.json');p.write_text(json.dumps(out,indent=2)+'\n');print(p)

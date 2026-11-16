#!/usr/bin/env python3
"""Exact jet-interpolation and polynomial-defect certificates for D76."""
from pathlib import Path
import json
import sympy as s

u,v,z,h,d=s.symbols("u v z h d")
A,B,C=s.symbols("A B C")
order=9
F=2+3*u+5*u**2-7*u**4+11*u**7
G=2-4*v+6*v**3+13*v**6
H=2+7*u-9*u**2+17*u**5-19*u**8
diag=-u/(1+u)
base=F+G-2
disc=s.series(H-base.subs(v,diag),u,0,order).removeO()
assert disc.coeff(u,0)==disc.coeff(u,1)==0
L=s.series(-(1+u)*disc/u**2,u,0,order-2).removeO()
lift=s.expand(base+u*v*L)
assert s.expand(lift.subs(v,0)-F)==0
assert s.expand(lift.subs(u,0)-G)==0
assert s.series(lift.subs(v,diag)-H,u,0,order).removeO()==0

# The functional on coefficients0,1 evaluates on S_z(t) as
# A*z+B*binomial(z,2), and integral gauges preserve degree2.
measure_polynomial=A*z+B*z*(z-1)/2
gauged=s.expand(measure_polynomial.subs(z,z+d)-measure_polynomial.subs(z,d))
assert s.degree(gauged,z)<=2
P=A*z**2+B*z+C
Pdouble=s.expand(P.subs(z,z+h)+P)
defect=s.expand(Pdouble.subs(z,2*z)-P)
assert defect.coeff(z,2)==7*A
assert defect.coeff(z,1).subs(A,0)==3*B
assert defect.coeff(z,0).subs({A:0,B:0})==C
V=s.Matrix([[1,x,x*x] for x in (0,1,2)])
assert V.det()==2
unit_checks=[]
for n in range(1,8):
 m=5**n
 assert all(s.gcd(x,m)==1 for x in (2,3,7))
 unit_checks.append({"n":n,"modulus":m,
                     "inverse_2":pow(2,-1,m),
                     "inverse_3":pow(3,-1,m),
                     "inverse_7":pow(7,-1,m)})
result={
 "status":"PASS",
 "scope":"Exact finite jet interpolation and symbolic polynomial-defect identities; continuous invariant lifting is proved in D76.",
 "jet_order":order,
 "F":str(F),"G":str(G),"H":str(H),
 "correcting_L":str(L),
 "axis_restrictions_exact":True,
 "diagonal_restriction_through_degree":order-1,
 "gauged_measure_polynomial":str(gauged),
 "doubling_scaling_defect":str(defect),
 "successive_coefficients":["7*A","3*B after A=0","C after A=B=0"],
 "vandermonde_determinant":int(V.det()),
 "unit_checks":unit_checks,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))

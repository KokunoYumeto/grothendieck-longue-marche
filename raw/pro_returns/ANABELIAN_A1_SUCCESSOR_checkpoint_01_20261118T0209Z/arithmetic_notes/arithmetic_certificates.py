"""Finite certificates only: not a substitute for the profinite/analytic proofs.

Exact rational interpolation checks B.B8.3 for degrees 1--4.
Finite boundary matrices check B.N3.4--5's displayed examples.
"""
from pathlib import Path
from math import gcd
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
z,w,r,t=s.symbols('z w r t')
out={"scope":"Finite exact arithmetic checks only; no general theorem is inferred from this sample.","interpolation":[],"boundary_matrices":[],"small_prime_trace":{}}
for d in range(1,5):
    c=[s.Rational(k+1,k+2)+s.I*s.Rational(k*k+1,d+1) for k in range(d)]+[s.Integer(1)]
    P=sum(c[k]*z**k for k in range(d+1))
    points=list(range(2*d+1))
    V=s.Matrix([[s.Integer(x)**k for k in range(2*d+1)] for x in points])
    Vinv=V.inv()
    B=s.Matrix([[s.expand(P.subs(z,a+s.I*b)*s.conjugate(P.subs(z,a+s.I*b))) for b in points] for a in points])
    A=Vinv*B*Vinv.T
    realpoly=sum(A[i,j]*r**i*t**j for i in points for j in points)
    herm=s.Poly(s.expand(realpoly.subs({r:(z+w)/2,t:(z-w)/(2*s.I)},simultaneous=True)),z,w)
    recovered=[herm.coeff_monomial(z**k*w**d) for k in range(d+1)]
    assert all(s.simplify(a-b)==0 for a,b in zip(recovered,c))
    expected=s.Poly(s.expand(P*sum(s.conjugate(c[k])*w**k for k in range(d+1))),z,w)
    assert herm==expected
    out["interpolation"].append({"degree":d,"grid_size":len(points)**2,"coefficients":[str(x) for x in c],"recovered":[str(x) for x in recovered],"full_hermitian_outer_product":True})

sum_matrix=s.Matrix([[1,1]])
assert sum_matrix.nullspace()==[s.Matrix([-1,1])]
for n in range(2,33):
    image={(a+b)%n for a in range(n) for b in range(n)}
    kernel={(a,b) for a in range(n) for b in range(n) if (a+b)%n==0}
    assert len(image)==n and len(kernel)==n
    assert kernel=={(a,(-a)%n) for a in range(n)}
    diagimage={(2*a%n,3*b%n) for a in range(n) for b in range(n)}
    assert len(diagimage)==(n//gcd(n,2))*(n//gcd(n,3))
    out["boundary_matrices"].append({"modulus":n,"sum_image":len(image),"sum_kernel":len(kernel),"kernel_is_antidiagonal":True,"diag_2_3_image":len(diagimage)})
assert all(a+b>0 for a in range(1,33) for b in range(1,33))
out["positive_DVR_weights"]={"range":[1,32],"sum_strictly_positive":True,"proof_required_for_all_weights":True}
a=(2+s.sqrt(-3))/(2-s.sqrt(-3))
trace=s.simplify(a+1/a)
assert trace==s.Rational(2,7)
out["small_prime_trace"]={"element":str(a),"trace":str(trace),"rational_noninteger":True}
(ROOT/'arithmetic_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({"result":"PASS","interpolation_degrees":[1,2,3,4],"grid_values_checked":sum((2*d+1)**2 for d in range(1,5)),"boundary_moduli":[2,32],"small_prime_trace":str(trace),"scope":out["scope"]},indent=2))

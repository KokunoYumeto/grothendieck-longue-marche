#!/usr/bin/env python3
"""Actual Fermat-eight maps, 21 differential pullbacks, and old elliptic points.

This uses only local exact rational/polynomial/finite-field arithmetic.
The two companion programs supply the nine abelian-surface certificates.
"""
from pathlib import Path
import contextlib
import io
import json
import runpy
import sympy as s

BASE = Path(__file__).resolve().parent
u, v, x, y, Z = s.symbols("u v x y Z")
F = 3*u**8-2*v**8-1
dv = 3*u**7/(2*v**7)

def derivative(h):
    return s.diff(h,u)+dv*s.diff(h,v)

def zero_on_curve(h):
    numerator = s.together(h).as_numer_denom()[0]
    return s.rem(numerator,F,v) == 0

def verify_differential(h,a,b):
    omega = u**(a-1)*v**(b-8)
    ratio = s.cancel(h/omega)
    scalar = s.cancel(ratio.subs({u:1,v:1}))
    assert scalar != 0
    assert zero_on_curve(h-scalar*omega)
    return str(scalar)

def chi(a,p):
    a %= p
    return 0 if a==0 else 1 if pow(a,(p-1)//2,p)==1 else -1

def val(a,p):
    k=0
    while a%p==0:
        a//=p;k+=1
    return k

elliptics = [
    (3,-2,u**2/v**2,1/v**4,1,(2,2)),
    (6,3,v**2,3*u**4,3,(4,2)),
    (6,-2,u**2,2*v**4,2,(2,4)),
]
elliptic_data=[]
forms=[]
for A,B,xx,yy,y0,weight in elliptics:
    assert zero_on_curve(yy**2-A*xx**4-B)
    ex,ey=A*xx**2,A*xx*yy
    assert zero_on_curve(ey**2-ex**3-A*B*ex)
    assert s.expand((A*x*y)**2-(A*x*x)**3-A*B*(A*x*x)
                    -A*A*x*x*(y*y-A*x**4-B)) == 0
    scalar=verify_differential(derivative(ex)/(2*ey),*weight)
    rows=[]
    for p in [5,7,11,13,17,19,23,29,31]:
        assert (2*A*B)%p
        order=p+1+sum(chi(t**3+A*B*t,p) for t in range(p))
        rows.append({"p":p,"order":order})
    prime_set=set(ell for row in rows for ell in s.factorint(row["order"]))
    bound=1
    for ell in prime_set:
        bound*=ell**min(val(row["order"],ell) for row in rows if row["p"]!=ell)
    assert bound==2
    point=(A,A*y0)
    assert point[1]**2==point[0]**3+A*B*point[0] and point[1]!=0
    elliptic_data.append({"coefficient":A*B,"point":point,"orders":rows,
                          "torsion_order_bound":bound,"weight":weight,
                          "differential_scalar":scalar})
    forms.append(weight)
    print("ELLIPTIC",A*B,"point",point,"torsion bound",bound,
          "orders",[(row['p'],row['order']) for row in rows])

genus2=[
    (3,-2,u/v,1/v**4,[(1,3),(3,1)]),
    (6,3,v,3*u**4,[(4,1),(4,3)]),
    (6,-2,u,2*v**4,[(1,4),(3,4)]),
    (24,1,u*v,3*u**8+2*v**8,[(1,1),(3,3)]),
    (3,1,u/v**2,(3*u**8+1)/(2*v**8),[(1,6),(3,2)]),
    (-8,9,v/u**2,(2*v**8-1)/u**8,[(6,1),(2,3)]),
]
genus2_data=[]
for A,B,xx,yy,weights in genus2:
    assert zero_on_curve(yy**2-A*xx**8-B)
    X,Y=xx**2,xx*yy
    assert zero_on_curve(Y**2-A*X**5-B*X)
    scalars=[verify_differential(X**j*derivative(X)/Y,*weights[j])
             for j in range(2)]
    forms.extend(weights)
    genus2_data.append({"A":A,"B":B,"X":str(X),"Y":str(Y),
                        "weights":weights,"scalars":scalars})
    print("GENUS TWO",(A,B),"weights",weights,"scalars",scalars)

pryms=[
    (-12,1,-u**4/2,u*v**2,[(1,2),(5,2)]),
    (18,1,v**4/3,u**2*v,[(2,1),(2,5)]),
    (3,-2,u**4/v**4,u/v**3,[(1,5),(5,1)]),
]
prym_data=[]
for A,B,zz,ww,weights in pryms:
    assert zero_on_curve(ww**4-A*zz**3-B*zz)
    scalars=[verify_differential(zz**j*derivative(zz)/ww**3,*weights[j])
             for j in range(2)]
    forms.extend(weights)
    prym_data.append({"A":A,"B":B,"z":str(zz),"w":str(ww),
                      "weights":weights,"scalars":scalars})
    print("PRYM",(A,B),"weights",weights,"scalars",scalars)

all_weights={(a,b) for a in range(1,8) for b in range(1,8) if a+b<=7}
assert len(forms)==len(set(forms))==len(all_weights)==21
assert set(forms)==all_weights
assert sum(1 for a,b in forms if a%2==0 and b%2==0)==3
print("PASS: all 21 literal pulled-back differentials, each with its exact nonzero scalar")

# The elementary irreducibility alternatives for all Euler quartics used.
irreducibility=[]
for a,p in [(0,5),(0,13),(8,5),(-24,13)]:
    polynomial=Z**4+a*Z**2+p*p
    numbers=[a*a-4*p*p,2*p-a,-2*p-a]
    def rational_square(n):
        return n>=0 and s.integer_nthroot(n,2)[1]
    assert all(not rational_square(n) for n in numbers)
    assert s.Poly(polynomial,Z).is_irreducible
    irreducibility.append({"polynomial":str(polynomial),"square_tests":numbers})
print("PASS: four exact irreducibility certificates")

# Re-execute the complete surface proofs, rather than trusting stale data files.
for name in ["point3_fermat8_genus2_certificate.py",
             "point3_fermat8_quartic_prym_certificate.py"]:
    buffer=io.StringIO()
    with contextlib.redirect_stdout(buffer):
        runpy.run_path(str(BASE/name),run_name="__main__")
    (BASE/name.replace(".py","_output.txt")).write_text(buffer.getvalue())
    print("PASS: independent local companion execution",name)

payload={"elliptics":elliptic_data,"genus_two_maps":genus2_data,
         "prym_maps":prym_data,"all_holomorphic_weights":sorted(forms),
         "irreducibility":irreducibility,
         "certified_rank_lower_bound":12,
         "rank_upper_bound":"not established by this certificate",
         "external_computation_used":False}
(BASE/"point3_fermat8_decomposition_certificate_data.json").write_text(
    json.dumps(payload,indent=2)+"\n")
print("PASS: actual dimension 3+12+6=21 and certified rational rank at least 12")

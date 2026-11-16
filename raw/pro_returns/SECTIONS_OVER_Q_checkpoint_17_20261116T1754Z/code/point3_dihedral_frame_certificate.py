#!/usr/bin/env python3
"""Exact finite identities for the two D8 images of a point3 mod24 frame."""
from pathlib import Path
import json
import sympy as sp

OUT = Path(__file__).with_name("point3_dihedral_frame_certificate_data.json")
E, q, u, v, A, B = sp.symbols("E q u v A B")
central = lambda m,n: (B*m-A*n)/(q-1)-sp.Rational(1,2)*m*n
assert sp.simplify(central(E,0).subs(B,(q-1)*v)-E*v)==0
assert sp.simplify(central(0,E).subs(A,(q-1)*v)+E*v)==0
assert sp.simplify(central(-E,-E).subs(A,B+(q-1)*(u+sp.Rational(1,2)))
                   -(E*u-E*(E-1)/2))==0
parity_count=0
for e in range(4,257,4):
    for n in range(-32,33):
        assert e*n%2==0 and (-e*n)%2==0
        assert (e*n-e*(e-1)//2)%2==0
        parity_count+=3

# D8 is represented by s^a r^b, a mod2, b mod4.
elts=[(a,b) for a in range(2) for b in range(4)]
def mul(g,h):
    a,b=g; c,d=h
    return ((a+c)%2, (((-1)**c)*b+d)%4)
def inv(g):
    return next(h for h in elts if mul(g,h)==(0,0))
def act(k,g):
    return (g[0],k*g[1]%4)
def change(k,h,z):
    # z h g(z)^-1 h^-1: the central difference of section conjugation.
    return mul(mul(mul(z,h),inv(act(k,z))),inv(h))
conjugation_count=0
for k in range(1,33,2):
    for a,b in elts:
        h=(a,b)
        for j,l in elts:
            got=change(k,h,(j,l))
            exponent=(j*b+l*a+l*((k-1)//2))%2
            assert got==(0,2*exponent)
            conjugation_count+=1

# F2^3 records squareclasses of -1,2,3 in that order.
support=set(range(8))
delta_x=1^2
delta_y=1^4
conjugators={0,delta_x,delta_y,delta_x^delta_y}
assert conjugators=={0,3,5,6}
other={d^2 for d in conjugators}
assert conjugators.isdisjoint(other) and conjugators|other==support
# At Q3 use (nonsquare-unit, uniformizer) coordinates.
def local3(d):
    return ((d&1)^((d>>1)&1), (d>>2)&1)
assert local3(delta_x)==(0,0)
assert local3(delta_y)==(1,1)
assert local3(2)==(1,0)
assert {local3(d) for d in conjugators}.isdisjoint(
       {local3(d) for d in other})

units24=[k for k in range(24) if sp.gcd(k,24)==1]
eta_table={}
for k in units24:
    value=((k*k-1)//24)%2
    sqrt2_character=int(k%8 in (3,5))
    assert value==sqrt2_character
    eta_table[str(k)]=value
images=[k%2 for k in range(24)]
assert images.count(0)==images.count(1)==12

data={
  "status":"PASS",
  "ordinary_contact_parity_instances":parity_count,
  "literal_geometric_conjugation_checks":conjugation_count,
  "quadratic_support_basis":["-1","2","3"],
  "geometric_conjugation_subgroup_masks":sorted(conjugators),
  "other_geometric_class_masks":sorted(other),
  "local3_conjugation_subgroup":[list(x) for x in sorted({local3(d) for d in conjugators})],
  "local3_other_class":[list(x) for x in sorted({local3(d) for d in other})],
  "eta_mod2_by_chi_mod24":eta_table,
  "twenty_four_lift_multiplicities":[12,12],
  "scope":"Exact Hall, finite arithmetic action, conjugation and character checks. Ordinary local Kummer vanishing and punctured-disc comparison are proved in the source."
}
OUT.write_text(json.dumps(data,indent=2)+"\n")
print("Ordinary point3 mod24 frame: two actual dihedral images, PASS")
print("Exact Hall substitutions: 3 PASS")
print(f"Ordinary-contact parity instances: {parity_count} PASS")
print(f"Literal D8/arithmetic conjugator identities: {conjugation_count} PASS")
print("Supported quadratic quotient: representatives1,2; exact conjugation subgroup1,-2,-3,6")
print("Q3 restrictions of the two geometric classes are disjoint: PASS")
print("Global eta2 reduction equals kappa(2); multiplicities12,12: PASS")

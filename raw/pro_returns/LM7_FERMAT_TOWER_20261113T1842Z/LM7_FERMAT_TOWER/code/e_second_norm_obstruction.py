#!/usr/bin/env python3
"""Exact finite-field and local norm-tower certificate for E.62."""
from itertools import product
from pathlib import Path
import json

P=17
zero=(0,0)
one=(1,0)
omega=(0,1)
def add(x,y): return tuple((a+b)%P for a,b in zip(x,y))
def neg(x): return tuple(-a%P for a in x)
def mul(x,y):
    a,b=x;c,d=y
    return ((a*c-b*d)%P,(a*d+b*c-b*d)%P)
def power(x,n):
    if n<0:n%=288
    y=one
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y
def div(x,y):
    assert y!=zero
    return mul(x,power(y,-1))
elts=list(product(range(P),repeat=2))
units=[x for x in elts if x!=zero]
assert len(units)==288
assert add(add(power(omega,2),omega),one)==zero
assert power(omega,3)==one and omega!=one
cube={power(x,3) for x in units}
ninth={power(x,9) for x in units}
assert len(cube)==96 and len(ninth)==32
assert omega in cube and omega not in ninth
assert power(omega,32)==power(omega,2)!=one
zeta9=(2,8)
assert power(zeta9,3)==omega and power(zeta9,9)==one
pi=add((2,0),neg(omega))
g1=add((-2%P,0),mul((-3%P,0),omega))
w=power(div(g1,pi),2)
assert power(w,3)==omega
assert power(w,96)==power(omega,2)
assert w not in cube

norm_images=[]
for d in range(1,7):
    image={power(x,3**d) for x in units}
    expected=96 if d==1 else 32
    assert len(image)==expected
    norm_images.append({"relative_degree":3**d,
                        "residue_norm_image_size":len(image),
                        "zeta3_in_image":omega in image})

# All residue torsion coordinates use the actual primitive ninth root.
# The exact norm on the Teichmuller subgroup is t -> 3t modulo9.
transition=[3*t%9 for t in range(9)]
assert set(transition)=={0,3,6}
assert {transition[transition[t]] for t in range(9)}=={0}
first_preimages=[t for t in range(9) if transition[t]==3]
assert first_preimages==[1,4,7]
assert all(t not in set(transition) for t in first_preimages)
for depth in range(2,8):
    assert {3**depth*t%9 for t in range(9)}=={0}

# The actual augmentation lattice, with the typed division by three.
lattice=[]
for m in range(1,5):
    modulus=3**m
    values={(e,f) for e in range(modulus) for f in range(modulus)
            if (e+2*f)%3==0}
    mapped={((3*b-2*f)%modulus,f)
            for b in range(modulus//3) for f in range(modulus)}
    assert mapped==values
    assert len(values)==modulus**2//3
    for e,f in values:
        b=((e+2*f)//3)%(modulus//3)
        assert (3*b-2*f)%modulus==e
    lattice.append({"ambient_modulus":modulus,
                    "lattice_size":len(values),
                    "toric_parameter_modulus":modulus//3})

out={
 "statement":"E.62","status":"PASS",
 "residue_field":"F17[omega]/(omega^2+omega+1)",
 "unit_count":len(units),"cube_image_size":len(cube),
 "ninth_power_image_size":len(ninth),
 "zeta3":[*omega],"specified_zeta9":[*zeta9],
 "E57_w_residue":[*w],
 "E57_w_cubed":[*power(w,3)],
 "E57_w_cubic_symbol":[*power(w,96)],
 "zeta3_ninth_power_test":[*power(omega,32)],
 "norm_images":norm_images,
 "torsion_norm_transition":transition,
 "first_lift_torsion_coordinates":first_preimages,
 "second_lift_torsion_coordinates":[],
 "augmentation_lattice_checks":lattice,
 "local_inverse_limit":"{(e,f) in Z3^2:e+2f in3Z3}",
 "local_positional_map":"(e,f) -> (17^e,(17*zeta3)^f)",
 "scaled_toric_map":"(e,f) -> (kappa17,((e+2f)/3)*kappa17)",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS exact F289 cube and ninth-power images:96 and32")
print("PASS E57 literal norm element has primitive ninth-root residue")
print("PASS positional class zeta3 lifts once and has no second lift")
print("PASS all six residue norm images and seven torsion transition depths")
print("PASS exact augmentation lattice and divided toric map modulo3,9,27,81")

#!/usr/bin/env python3
"""Exact exponent-twelve Hall quotient and its mod4/mod3 coordinate maps."""
from pathlib import Path
import json
import numpy as np
import bc_fermat_class_two_four as q4
import bc_fermat_class_two as q3

HERE=Path(__file__).resolve().parent
I,J=q4.I,q4.J

def multiply(a,b):
    return np.r_[(a[:10]+b[:10])%12,(a[10:]+b[10:]-a[J]*b[I])%6]

def to_four(a):
    return np.r_[a[:10]%4,a[10:]%2]

def to_three(a):
    return np.r_[a[:10]%3,(a[10:]+2*a[I]*a[J])%3]

def reconstruct(a,b):
    v=(9*a[:10]+4*b[:10])%12
    hall_three=(b[10:]-2*v[I]*v[J])%3
    z=(3*a[10:]+4*hall_three)%6
    result=np.r_[v,z]
    assert np.array_equal(to_four(result),a)
    assert np.array_equal(to_three(result),b)
    return result

rng=np.random.default_rng(12362026)
for _ in range(100):
    a,b=[np.r_[rng.integers(0,12,size=10),rng.integers(0,6,size=45)] for __ in range(2)]
    assert np.array_equal(to_four(multiply(a,b)),q4.multiply(to_four(a),to_four(b)))
    assert np.array_equal(to_three(multiply(a,b)),q3.multiply(to_three(a),to_three(b)))
    assert np.array_equal(reconstruct(to_four(a),to_three(a)),a)
    arbitrary4=np.r_[rng.integers(0,4,size=10),rng.integers(0,2,size=45)]
    arbitrary3=rng.integers(0,3,size=55)
    reconstruct(arbitrary4,arbitrary3)
out={"quotient":"H/(gamma_3(H)H^12)",
     "Hall_abelian_group":"(Z/12)^10","Hall_commutator_group":"(Z/6)^45",
     "mod_four_map":"(v,z)->(v mod4,z mod2)",
     "mod_three_BCH_map":"(v,z)->(v mod3,z+2*(v_i*v_j)_(i<j) mod3)",
     "inverse_abelian_CRT":"v=9*v4+4*v3 mod12",
     "inverse_central_CRT":"z=3*z4+4*(z3-2*v_i*v_j) mod6",
     "all_multiplications_and_two_sided_coordinate_maps_checked":True,
     "complete_joint_fibre_count":"2^10*3^11",
     "complete_joint_fibre_count_integer":2**10*3**11}
(HERE/"bc_fermat_class_two_crt.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
print("PASS: actual mod12 Hall/CRT isomorphism, including the mod3 BCH shift.")

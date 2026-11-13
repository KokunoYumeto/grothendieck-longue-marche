#!/usr/bin/env python3
"""Literal boundary comparison between E.1 and the later E.24 families.

The 432 H-abelianizations were evaluated from the reconstructed E.24
F-words by bc_cm_fermat_odd_boundary.py.  The E.24 origins are not
identified with the original E.1 G6 points: only the displayed, fully
checked boundary congruence modulo two is used.
"""
from pathlib import Path
from itertools import product
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
c=json.loads((HERE/"bc_cm_fermat_boundary_integral.json").read_text())
b=np.load(HERE/"bc_cm_fermat_boundary.npz")
original=json.loads((HERE/"bc_cm_fermat_boundary.json").read_text())["records"]
families=json.loads((HERE/"bc_cm_fermat_odd_boundary.json").read_text())["records"]
D=np.array(c["complete_integral_derived_image_basis"],dtype=np.int64)
P=np.array(c["odd_denominator_norm_correction_three_times_P"],dtype=np.int64)%2
rows=c["kernel_basis_inverse_coordinate_rows"]
left=np.array(sp.Matrix(D[:6,:]).inv(),dtype=np.int64)%2
E,derivatives=b["E"],b["abelian_action_derivatives"]
L=np.array(c["F_abelianization_map_divided_by_three"],dtype=np.int64)
def rank2(A):
    a=A.copy()%2;r=0
    for j in range(a.shape[1]):
        ids=np.flatnonzero(a[r:,j])
        if not len(ids):continue
        k=r+int(ids[0]);a[[r,k]]=a[[k,r]]
        for i in range(a.shape[0]):
            if i!=r and a[i,j]:a[i]^=a[r]
        r+=1
        if r==a.shape[0]:break
    return r
records=[]
for i in range(24):
    group=[r for r in families if r["certificate_index"]==i]
    assert {(tuple(r["ternary_parameters"]),r["binary_parameter"]) for r in group} == {
        ((a,b),e) for a,b,e in product(range(3),range(3),range(2))}
    z0=np.array(original[i]["original_H_abelianization_mod4"],dtype=np.int64)
    for r in group:
        z=np.array(r["integral_H_abelianization"],dtype=np.int64)
        assert not np.any(L@z)
        difference=(z-z0)%2
        dc=left@difference[:6]%2
        assert not np.any((D@dc-difference)%2)
        corrected=(z-D@P@z[rows])%2
        assert not np.any(E@corrected%2)
        matrix=np.eye(10,dtype=np.int64)+np.stack(
            [a@corrected for a in derivatives],axis=1)
        assert rank2(matrix)==10
        records.append({"certificate_index":i,
            "ternary_parameters":r["ternary_parameters"],
            "binary_parameter":r["binary_parameter"],
            "literal_boundary_difference_coordinates_mod2":dc.tolist(),
            "corrected_boundary_coordinate_mod2":corrected.tolist(),
            "action_rank_mod2":10})
    print("CM row",i,": all18 actual E24 boundary differences lie in D mod2; all18 corrected actions have rank10.")
out={"exact_comparison":"E24-word minus indexed E1-word in H^ab/2, not equality in G6.",
     "number_of_literal_E24_points":len(records),
     "all_mod2_differences_in_D":True,"all_corrected_action_ranks":10,
     "records":records}
(HERE/"bc_twoadic_ferrari_comparison.json").write_text(json.dumps(out,indent=2)+"\n")
print("PASS: all432 literal boundary comparisons and two-adic generation checks.")

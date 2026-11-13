#!/usr/bin/env python3
"""Exact ternary boundary norms for all 432 multiplier-one E24 words.

Corrections are confined to the six specified gamma5 words, whose
entire integral image is D(Q-1)^3.  A negative row means failure for
this exact correction subgroup, not exclusion from the full source.
"""
from pathlib import Path
from unittest.mock import patch
from collections import Counter
import json
import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
import de_fermat_schreier as f
import de_ferrari_two_family_words as family

HERE=Path(__file__).resolve().parent
with patch.object(Path,"write_text",return_value=0):
    data=family.load_data()
cert=np.load(HERE/"bc_cm_fermat_boundary_integral.npz")
base=np.load(HERE/"bc_cm_fermat_boundary.npz")
D,E,Q=map(sp.Matrix,(cert["D"],cert["E"],cert["Q"]))
Pdeep=(Q-sp.eye(6))**3
B=E*D*Pdeep
S,U,V=map(lambda a:a.to_Matrix(),
          smith_normal_decomp(DomainMatrix.from_Matrix(B).convert_to(sp.ZZ)))
assert S==U*B*V and abs(U.det())==abs(V.det())==1
diagonal=[abs(int(S[i,i])) for i in range(6)]
assert diagonal==[3,9,9,9,9,0]
derivatives=[sp.Matrix(a) for a in base["abelian_action_derivatives"]]

def rank_mod3(A):
    a=np.asarray(A,dtype=np.int64).copy()%3;r=0
    for j in range(a.shape[1]):
        ids=np.flatnonzero(a[r:,j])
        if not len(ids):continue
        k=r+int(ids[0]);a[[r,k]]=a[[k,r]]
        a[r]=a[r]*pow(int(a[r,j]),-1,3)%3
        for i in range(a.shape[0]):
            if i!=r:a[i]=(a[i]-a[i,j]*a[r])%3
        r+=1
        if r==a.shape[0]:break
    return r

records=[]
for i in range(24):
    local=[]
    for row in family.family_words(data,i,lam=1):
        z=sp.Matrix(f.integral_abel(row["literal_F_word"]))
        b=-E*z; ub=U*b
        assert ub[5:,:]==sp.zeros(15,1)
        residues=[int(ub[j])%diagonal[j] for j in range(5)]
        passes=not any(residues)
        coordinates=None;action_rank=None;corrected=None
        if passes:
            y=sp.Matrix([ub[j]/S[j,j] if j<5 else 0 for j in range(6)])
            assert all(a.q==1 for a in y)
            coordinates=V*y
            assert B*coordinates==b
            corrected=z+D*Pdeep*coordinates
            action=sp.eye(10)+sp.Matrix.hstack(*(a*corrected for a in derivatives))
            action_rank=rank_mod3(np.array(action,dtype=np.int64))
        rec={
            "certificate_index":i,
            "ternary_parameters":row["ternary_parameters"],
            "binary_parameter":row["binary_parameter"],
            "integral_H_abelianization":[int(a) for a in z],
            "gamma5_norm_obstruction_moduli":diagonal[:5],
            "gamma5_norm_obstruction":residues,
            "gamma5_norm_solvable":passes,
            "gamma5_word_coefficients":None if coordinates is None else [int(a) for a in coordinates],
            "corrected_H_abelianization":None if corrected is None else [int(a) for a in corrected],
            "corrected_H_action_rank_mod3":action_rank,
            "generates_all_three_power_boundary_levels":action_rank==10}
        records.append(rec);local.append(rec)
    print(json.dumps({"certificate_index":i,"rows":len(local),
        "norm_solvable":sum(r["gamma5_norm_solvable"] for r in local),
        "generating":sum(r["generates_all_three_power_boundary_levels"] for r in local),
        "distinct_obstructions":len({tuple(r["gamma5_norm_obstruction"]) for r in local})}),flush=True)

result={
    "family":"All432 multiplier-one E24 points, literal source-word reconstruction",
    "restricted_correction_image":"D(Q-1)^3, image of the six explicit gamma5 words",
    "norm_smith":diagonal,
    "records":records,
    "norm_solvable_count":sum(r["gamma5_norm_solvable"] for r in records),
    "generating_count":sum(r["generates_all_three_power_boundary_levels"] for r in records),
    "scope":"Failures exclude only the exact displayed gamma5 correction image; no full-source or full-CM-fibre exclusion is asserted."}
(HERE/"bc_cm_fermat_odd_boundary.json").write_text(json.dumps(result,indent=2)+"\n")
np.savez_compressed(HERE/"bc_cm_fermat_odd_boundary.npz",
                    deep_norm_matrix=np.array(B,dtype=np.int64),
                    smith=np.array(S,dtype=np.int64),
                    smith_left=np.array(U,dtype=np.int64),
                    smith_right=np.array(V,dtype=np.int64))
print("Totals:",result["norm_solvable_count"],"norm solutions;",
      result["generating_count"],"generating all-three-power lifts.")
print("PASS: exact restricted gamma5 boundary correction test for all432 actual words.")

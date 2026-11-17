#!/usr/bin/env python3
"""Actual integral Smith operations for the uniform canonical power relations."""
from pathlib import Path
import json
import numpy as np
from flint import fmpz_mat
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

HERE=Path(__file__).resolve().parent
old=np.load(HERE.parent/'centralizer_code/check_modular_binary_central_obstruction.npz')
I=np.eye(97,dtype=np.int64)
R=np.vstack((old['s_action']-I,old['r_action']-I)).astype(np.int64)
M=DomainMatrix.from_list_sympy(*R.shape,R.tolist()).convert_to(ZZ)
D,U,V=smith_normal_decomp(M)
D=np.array(D.to_Matrix().tolist(),dtype=np.int64)
U=np.array(U.to_Matrix().tolist(),dtype=np.int64)
V=np.array(V.to_Matrix().tolist(),dtype=np.int64)
assert fmpz_mat(U.tolist())*fmpz_mat(R.tolist())*fmpz_mat(V.tolist())==fmpz_mat(D.tolist())
assert abs(int(fmpz_mat(U.tolist()).det()))==1
assert abs(int(fmpz_mat(V.tolist()).det()))==1
assert [abs(int(D[i,i])) for i in range(97)]==[1]*96+[2]
assert not np.any(D[97:])
Q2=old['central_relations'][:194,97:].astype(np.int64)%2
transformed=U%2@Q2%2
assert transformed.shape==(194,15)
assert not np.any(transformed[96:])
out={'scope':'Integral Smith power-coordinate changes and exact binary vanishing of every residual quadratic class.',
     'power_coinvariants':'C2','unit_smith_entries':96,'last_smith_entry':2,
     'residual_quadratic_rows':98,'all_residual_rows_zero_in_W_mod2':True,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),power_relations=R,smith=D,
    smith_left=U,smith_right=V,quadratic_classes_mod2=Q2,
    transformed_quadratic_classes_mod2=transformed)
print('PASS exact integral power Smith form: 96 unit entries and one2.',flush=True)
print('PASS all98 residual quadratic classes vanish in the actual W/2W.',flush=True)

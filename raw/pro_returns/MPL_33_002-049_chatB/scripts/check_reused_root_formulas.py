#!/usr/bin/env python3
"""Research checks on literal formulas, after freeze; no transcription edits.

Coordinates below are explicitly copied from the frozen typed formulas.
The calculation tests internal mathematical compatibility, not visual readings.
"""
from pathlib import Path
import json
import sympy as s

root=Path(__file__).resolve().parent.parent
h=s.Rational(1,2)
W=s.Matrix.hstack(*[s.Matrix(x) for x in [
 [0,0,0,0,0,0,0,2],
 [h,h,h,h,h,h,h,5*h],
 [-h,h,h,h,h,h,h,7*h],
 [0,0,1,1,1,1,1,5],
 [0,0,0,1,1,1,1,4],
 [0,0,0,0,1,1,1,3],
 [0,0,0,0,0,1,1,2],
 [0,0,0,0,0,0,1,1],
]])
# Weights are stated to be dual to the coroots; in this same-length
# normalization the typed source identifies coroot coordinates with roots.
A=W.T.inv()
theta=W[:,7]
C=s.Matrix.hstack(*[s.Matrix(x) for x in [
 [4,5,7,10,8,6,4,2],
 [5,8,10,15,12,9,6,3],
 [7,10,14,20,16,12,8,4],
 [10,15,20,30,24,18,12,6],
 [8,12,16,24,20,15,10,5],
 [6,9,12,18,15,12,8,4],
 [4,6,8,12,10,8,6,3],
 [2,3,4,6,5,4,3,2],
]])
u=s.Matrix([1,-1]);v=s.Matrix([0,1])
results={
 'E8_weight_matrix_invertible':W.det()!=0,
 'E8_recovered_simple_roots':[[str(x) for x in A[:,j]] for j in range(8)],
 'E8_root_squared_norms':[str((A[:,j].T*A[:,j])[0]) for j in range(8)],
 'E8_all_eight_weight_expansions_consistent':A*C==W,
 'E8_theta_pairing_alpha8_from_weight_data':str((theta.T*A[:,7])[0]),
 'E8_scan049_literal_theta_pairing_alpha8':'-1',
 'E8_rho_sum_weights_coordinates':[str(x) for x in W*s.ones(8,1)],
 'E8_rho_sum_weight_coefficients':[str(x) for x in C*s.ones(8,1)],
 'E6_scan023_remaining_factor_literal':str(s.Rational(2**7*3**4*5,(1+1)*(5+1)*(7+1)*(12+1))),
 'E6_if_last_factor_were_11_plus_1':str(s.Rational(2**7*3**4*5,(1+1)*(5+1)*(7+1)*(11+1))),
 'E6_candidates_with_sum_12_and_product_shift_45':[(m,12-m) for m in range(1,12) if (m+1)*(13-m)==45],
 'B2_u':list(u),'B2_v':list(v),
 'B2_single_Cartan_integer':str(2*(u.T*v)[0]/(u.T*u)[0]),
 'B2_squared_length_ratio':str((v.T*v)[0]/(u.T*u)[0]),
 'A3_contract_literal_m_prime':2+3,
 'A3_literal_q_prime':str(-s.cos(s.pi/5)),
 'A3_sum_of_original_q_entries':str(-s.cos(s.pi/2)-s.cos(s.pi/3)),
 'D4_contract_literal_5_5_chain_Gram_determinant':str(s.simplify(1-2*s.cos(s.pi/5)**2)),
}
results['B2_u']=[int(x) for x in results['B2_u']]
results['B2_v']=[int(x) for x in results['B2_v']]
(root/'records/reused_root_formula_checks.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))

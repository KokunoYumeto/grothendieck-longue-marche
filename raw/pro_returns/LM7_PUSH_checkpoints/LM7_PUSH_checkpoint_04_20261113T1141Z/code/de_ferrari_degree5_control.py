#!/usr/bin/env python3
"""Identity, exact multiplier periods, and obstruction separation controls."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy
import numpy as np
from de_ferrari_degree5_kernel import CombinedFive,InducedFive,old_span
from de_ferrari_degree4_lift import Combined,InducedCombined
from de_ferrari_mod9_lift import solve,rref

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
H=CombinedFive();W=InducedFive(H,d);oldH=Combined();oldW=InducedCombined(oldH,d)
u=W.word([-1,0]);ou=oldW.word([-1,0])
periods=[]
for n in (12,24,36,72,108,216,648):
    periods.append({'power':n,'degree4_cusp_power_trivial':oldW.equal(oldW.power(ou,n),oldW.one),
                    'degree5_cusp_power_trivial':W.equal(W.power(u,n),W.one)})
print(json.dumps({'cusp_power_controls':periods}),flush=True)

# An exact known-genuine source point, independently of the random CM
# fibre representative: lambda1 and the literal empty commutator word.
identity_values=np.broadcast_to(H.one,(6,len(H.one))).copy()
assert np.array_equal(H.word([]),identity_values)
assert np.array_equal(H.pentagon(identity_values),H.one)
H.check_braids(H.braid_images(identity_values))
s,r=W.letters[0],W.letters[1]
assert W.equal(W.power(s,2),W.one) and W.equal(W.power(r,3),W.one)
v=d['d'];unit=(v['unit'],np.zeros(576,dtype=np.int64));xi,yi=v['xi'],v['yi']
gens={1:xi,-1:v['gi'](xi,6),2:yi,-2:v['gi'](yi,6)}
g6s=(v['ss'],np.zeros(576,dtype=np.int64));g6r=(v['rr'],v['Pr']%6)
g6u=v['gm'](v['gi'](g6r,6),g6s,6)
assert v['equal'](v['gp'](g6u,72,6),unit)
assert not v['equal'](v['gp'](g6u,36,6),unit)
assert not v['equal'](v['gp'](g6u,24,6),unit)
assert W.equal(W.power(u,36),W.one)
assert all(np.array_equal(H.power(a,9),H.one) for a in (H.a,H.b,H.c))
multiplier_control={'exact_combined_cusp_order':72,'pure_peripheral_power_order_divides':36,
    'four_strand_braid_generator_orders_divide':9,
    'compatible_lambda_residue':1,'lambda_modulus':72,
    'compatible_m_residue':0,'m_modulus':36,
    'all_compatible_multiplier_lifts_have_identical_hexagon_and_braid_powers':True}
def g6_word(word):
    value=unit
    for letter in word:value=v['gm'](value,gens[letter],6)
    return value
e17=json.loads(here.joinpath('de_ferrari_fibres.json').read_text())['records']
original_f=d['words_for_further_tests'][0][0]
assert v['equal'](g6_word(original_f),unit)
e17zero=g6_word(e17[0]['actual_commutator_word_f'])
assert not v['equal'](e17zero,unit)
identity_comparison={'original_E1_index0_has_identity_G6_conjugator':True,
    'E17_index0_has_identity_G6_conjugator':False,
    'E17_index0_f_Q_coordinate':list(e17zero[0]),
    'E17_index0_f_nonzero_homology_coordinates':{str(i):int(c) for i,c in enumerate(e17zero[1]) if c},
    'E17_index0_induced_G6_y_map_is_identity':v['equal'](v['gc'](v['gi'](e17zero,6),yi,6),yi),
    'literal_identity_passes_every_new_relation':True}
print(json.dumps(identity_comparison),flush=True)

result=json.loads(here.joinpath('de_ferrari_degree5_lift.json').read_text())
matrices=np.load(here/'de_ferrari_degree5_lift_certificate.npz');rows=[]
old_points=json.loads(here.joinpath('de_ferrari_degree4_lift.json').read_text())['records']
nonzero_bases=[i for i in range(24) if np.any(matrices[f'norm_rhs_{i}_0'][:6])]
assert nonzero_bases
control_index=nonzero_bases[0]
beta=W.word(e17[control_index]['base_beta_word_B'])
oldk=W.word(old_points[control_index]['literal_B_correction_word'])
provisional_S=W.mul(W.conj(beta,s),oldk);cusp=W.mul(s,r)
assert not W.equal(W.mul(provisional_S,W.mul(provisional_S,cusp)),cusp)
assert W.equal(W.mul(provisional_S,W.mul(W.inv(provisional_S),cusp)),cusp)
product_regression={'control_index':control_index,'old_base_square_is_nontrivial':True,
    'R_equals_S_times_t_fails_the_cusp_product':True,
    'R_equals_inverse_S_times_t_preserves_the_cusp_product':True,
    'nonzero_provisional_square_count':len(nonzero_bases)}
for rec in result['records']:
    i=rec['certificate_index'];branches=[]
    for b in rec['branches']:
        j=b['old_affine_parameter'];A=matrices[f'norm_matrix_{i}_{j}'];rhs=matrices[f'norm_rhs_{i}_{j}']
        P=matrices[f'pentagon_braid_matrix_{i}_{j}'][:96];error=matrices[f'pentagon_braid_constant_{i}_{j}'][:96]
        branches.append({'old_affine_parameter':j,
             'gentle_lift_exists':solve(A,rhs) is not None,
             'pentagon_alone_lift_exists':solve(P,-error%3) is not None,
             'simultaneous_lift_exists':b['solution_exists'],
             'joint_coefficient_rank':len(rref(np.vstack((A,P)))[1]),
             'joint_augmented_rank':len(rref(np.column_stack((np.vstack((A,P)),np.r_[rhs,-error%3])))[1])})
    rows.append({'certificate_index':i,'missing_coset':rec['missing_coset'],'branches':branches})
out={'cusp_power_controls':periods,'identity_control':identity_comparison,
     'complete_multiplier_control':multiplier_control,
     'permanent_provisional_involution_regression':product_regression,
     'all_old_affine_line_points_tested':72,
     'gentle_pass_count':sum(b['gentle_lift_exists'] for r in rows for b in r['branches']),
     'pentagon_alone_pass_count':sum(b['pentagon_alone_lift_exists'] for r in rows for b in r['branches']),
     'simultaneous_pass_indices':[r['certificate_index'] for r in rows if any(b['simultaneous_lift_exists'] for b in r['branches'])],
     'records':rows}
here.joinpath('de_ferrari_degree5_control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('records','identity_control')},indent=2),flush=True)

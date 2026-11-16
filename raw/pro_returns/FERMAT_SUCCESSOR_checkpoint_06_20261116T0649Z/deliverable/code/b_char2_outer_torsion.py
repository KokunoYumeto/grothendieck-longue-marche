#!/usr/bin/env python3
"""Independent rectangular-cokernel test for the actual outer eta.

No adapted quotient basis is used.  The target is presented directly
as A/(D4*A+ad_w(V)).  Torsion global classes over K must restrict to
classes fixed by both actual Frobenii above seven.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import numpy as np

PREC=10
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={t:n for n,t in enumerate(hall)}
# Reuse only the published Hall arithmetic and rectangular Smith
# implementation, not its data or any of C's quotient calculation.
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
functions=[node for node in source.body
           if isinstance(node,ast.FunctionDef)
           and node.name in {'bracket','lie3','smith_transport'}]
exec(compile(ast.Module(body=functions,type_ignores=[]),'b_Hall_functions','exec'))
sym=np.load('deliverable/code/b_char2_symmetry_matrices.npz')
aff=np.load('deliverable/code/b_char2_translation_affine_matrices.npz')
quats=sym['Q8_matrices']
I2=np.eye(2,dtype=np.int64)
S=-(I2+quats[2,:2,:2]+quats[4,:2,:2]+quats[6,:2,:2])*pow(2,-1,MOD)%MOD
assert not np.any((S@S+S+I2)%MOD)
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
F4=np.zeros((10,10),dtype=np.int64)
F4[:2,:2]=-2*I2
F4[2:,:2]=-2*U
F4[2:,2:]=4*np.eye(8,dtype=np.int64)
D=lie3(F4)*pow(4,-1,MOD)%MOD-np.eye(330,dtype=np.int64)
D%=MOD
adw=aff['ad_w']
vals,Q=smith_transport(np.hstack((D,adw)))
hist=dict(sorted(Counter(vals).items()))
assert hist=={0:132,1:70,2:26,3:82,4:20}
print('Rectangular presentation A/(D4*A+ad_w(V)) Smith:',hist,flush=True)
positive=[i for i,e in enumerate(vals) if e]
moduli=np.array([3**vals[i] for i in positive],dtype=np.int64)
data=json.loads(Path('deliverable/code/b_char2_translation_affine.json').read_text())
candidates=[]
comparisons=[]
for row in data['comparisons']:
    for x in row['all_solution_smith_coordinates']:
        candidates.append(x)
        comparisons.append(row['comparison'])
candidate_columns=aff['embedding_F2_to_full_F4']@np.array(candidates,dtype=np.int64).T%MOD
local=(Q@candidate_columns%MOD)[positive,:]%moduli[:,None]

def order_exponents(columns):
    return [next(k for k in range(5) if not np.any(3**k*x%moduli))
            for x in columns.T]

assert set(order_exponents(local))=={3}
results=[]
differences=[]
detector=Q[positive[74],:]%9
assert not np.any(detector@D%9)
assert not np.any(detector@adw%9)
detector_rows=[]
short_detector=np.zeros(330,dtype=np.int64)
for triple,coefficient in [((2,0,4),-1),((4,0,2),-2),((4,0,4),3),((4,0,8),1),((8,0,4),-4)]:
    short_detector[lookup[triple]]=coefficient%9
assert not np.any(short_detector@D%9)
assert not np.any(short_detector@adw%9)
short_rows=[]
for label,cm in [('tau',S),('tau_bar',S@S%MOD)]:
    T=np.zeros((10,10),dtype=np.int64)
    T[:2,:2]=I2+3*cm
    T[2:,:2]=U@(cm-2*I2)
    T[2:,2:]=7*np.eye(8,dtype=np.int64)
    T%=MOD
    TA=lie3(T)*pow(7,-1,MOD)%MOD
    assert not np.any((TA@D-D@TA)%MOD)
    assert not np.any((TA@adw-adw@T)%MOD)
    difference=(TA-np.eye(330,dtype=np.int64))@candidate_columns%MOD
    image=(Q@difference%MOD)[positive,:]%moduli[:,None]
    orders=order_exponents(image)
    assert set(orders)=={2}
    print(label,'differences: all27 have exact order9 in the outer local cokernel',flush=True)
    detector_row=detector@(TA-np.eye(330,dtype=np.int64))%MOD@aff['embedding_F2_to_full_F4']%MOD%9
    detector_values=detector_row@np.array(candidates,dtype=np.int64).T%9
    expected=3 if label=='tau' else 6
    assert np.all(detector_values==expected)
    detector_rows.append(detector_row)
    print('  one common mod9 detector takes value',expected,'on every candidate',flush=True)
    short_row=short_detector@(TA-np.eye(330,dtype=np.int64))%MOD@aff['embedding_F2_to_full_F4']%MOD%9
    short_values=short_row@np.array(candidates,dtype=np.int64).T%9
    short_expected=6 if label=='tau' else 3
    assert np.all(short_values==short_expected)
    short_rows.append(short_row)
    print('  five-Hall-entry detector takes value',short_expected,'on every candidate',flush=True)
    differences.append(image)
    results.append({'generator':label,'order_histogram':dict(Counter(3**e for e in orders)),
                    'fixed_candidates':sum(e==0 for e in orders),
                    'all_difference_order_exponents':orders})
assert np.array_equal(detector_rows[0],np.array([0,0,0,0,0,3,3,6,0,6,3,6,1]))
assert not np.any((detector_rows[0]+detector_rows[1])%9)
assert np.array_equal(short_rows[0],np.array([0,0,0,0,0,0,3,6,6,6,6,0,0]))
assert not np.any((short_rows[0]+short_rows[1])%9)
result={'status':'independent rectangular outer quotient test passed',
        'quotient_presentation':'A/(D4 A+ad_w V)',
        'Smith_histogram':hist,'local_candidate_orders':[27]*27,
        'global_generator_tests':results,
        'mod9_detector':{'Hall_coefficients':[
            {'index_zero_based':int(i),'Hall_triple':list(hall[i]),'coefficient':int(detector[i])}
            for i in np.flatnonzero(detector)],
            'tau_row_on_thirteen_coordinates':detector_rows[0].tolist(),
            'tau_bar_row_on_thirteen_coordinates':detector_rows[1].tolist(),
            'values_on_all_twenty_seven':[3,6]},
        'five_entry_mod9_detector':{'Hall_coefficients':[
            {'Hall_triple':list(hall[i]),'coefficient_mod9':int(short_detector[i])}
            for i in np.flatnonzero(short_detector)],
            'tau_row_on_thirteen_coordinates':short_rows[0].tolist(),
            'tau_bar_row_on_thirteen_coordinates':short_rows[1].tolist(),
            'values_on_all_twenty_seven':[6,3]},
        'conclusion':'None of the27 candidates is the local image of a global torsion class over K; the actual outer eta is rationally nonzero.'}
Path('deliverable/code/b_char2_outer_torsion.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/b_char2_outer_torsion_matrices.npz',
                    modulus=np.array([MOD]),D4=D,ad_w=adw,
                    outer_Smith_rows=Q,outer_Smith_exponents=np.array(vals),
                    local_candidates=candidate_columns,local_outer_Smith=local,
                    local_moduli=moduli,differences=np.stack(differences),
                    candidate_comparisons=np.array(comparisons),
                    mod9_detector=detector,mod9_detector_rows=np.stack(detector_rows),
                    five_entry_detector=short_detector,five_entry_detector_rows=np.stack(short_rows))

#!/usr/bin/env python3
"""Explicit centralizer correction for binary affine mask31.

Checks vanishing in the full integral canonical multiplier, and constructs
the correction in the common source J/J2, so it joins with identity at3.
"""
from pathlib import Path
import json
import numpy as np
from sympy import Matrix
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
s=(HERE/'check_modular_binary_central_family.py').read_text()
env={'__name__':'canonical_correction_prefix','__file__':str(HERE/'canonical_correction_prefix.py')}
exec(compile(s.split('rows=[];saves={}',1)[0],str(HERE/'check_modular_binary_central_family.py'),'exec'),env)
ns=env['ns'];rewrite=env['rewrite'];coord=env['coord'];pi=env['pi'];sourceword=env['sourceword']
wi=env['wi'];subst=env['subst'];SX=env['SX'];RX=env['RX'];rref=env['rref'];L=env['L'];P=env['P']
rel=env['rel'];kap=env['kap'];z=env['z']
def central_vector(word):
    a=[0]*97;c=0
    for letter in rewrite(word):
        i=abs(letter)-1
        for j in range(i+1,97):
            if a[j]%2:c^=coord[pi[(i,j)]]
        a[i]+=1 if letter>0 else -1
    assert not any(t%2 for t in a)
    return np.array([t//2 for t in a]+[(c>>i)&1 for i in range(15)],dtype=np.int64)
record=np.load(HERE/'common_mod6_liftable_record.npz')
beta=record['b0_p2_beta_1'];A=record['b0_p2_A_1']
bw=sourceword(beta,252);aw=sourceword(A,0)
delta_word=bw+subst(wi(bw)+aw+subst(wi(aw),RX),SX)
delta=central_vector(delta_word)
_,full_dual=rref(rel)
assert full_dual.shape==(16,112)
target=delta@full_dual.T%2
coeff,_=rref((kap@full_dual.T%2).T,target)
coeff=coeff[:,0]
assert np.array_equal(coeff@kap@full_dual.T%2,target)
S=z['s_action'].astype(np.int64)
# Match exactly the earlier order of the 52 centralizer basis vectors.
_,nullproj=ns['row_space_projection']((S-np.eye(97,dtype=np.int64)).T,2)
fixed=nullproj.T.astype(np.int64)
hK=coeff@fixed%2
assert not np.any(hK@(S-np.eye(97,dtype=np.int64))%2)
module=np.load(HERE.parent/'ghost_code/check_fivepoint_binary_module.npz')
factor=module['modular_factor'].astype(np.int64)
assert np.array_equal(P@factor%2,module['modular_restriction']%2)
h,_=rref(factor.T,hK)
h=h[:,0]
assert np.array_equal(h@factor%2,hK)
Scommon=module['quotient_s'].astype(np.int64)
assert np.array_equal(h@Scommon%2,h)
hw=sourceword(h,0)
corrected_bw=bw+hw
corrected_delta_word=corrected_bw+subst(wi(corrected_bw)+aw+subst(wi(aw),RX),SX)
corrected_delta=central_vector(corrected_delta_word)
assert not np.any(corrected_delta@full_dual.T%2)
Hrows=[r for r in fmpz_mat(rel.tolist()).hnf().tolist() if any(r)]
H=Matrix(Hrows).T
lattice_coordinates=H.inv(method='DM')*Matrix(corrected_delta.tolist())
assert all(a.q==1 for a in lattice_coordinates)
assert not np.any(record['b0_p3_A_1'])
assert not np.any(record['b0_p3_particular'][:,1])
out={'scope':'Explicit pure s-centralizer correction killing the selected binary defect in the full integral canonical cover.',
     'affine_parameter':31,'base':0,'candidate':1,
     'uncorrected_defect_in_full_multiplier':target.tolist(),
     'correction_coefficients_support':np.flatnonzero(coeff).tolist(),
     'correction_common_coordinates':h.tolist(),
     'corrected_defect_in_full_multiplier':[0]*16,
     'integral_hnf_coordinates':[int(a) for a in lattice_coordinates],
     'correction_has_common_base':0,'correction_is_s_fixed':True,
     'ternary_f_and_A_are_identity':True,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),uncorrected_defect=delta,
    corrected_defect=corrected_delta,correction_coefficients=coeff,correction_K=hK,
    correction_common=h,full_dual=full_dual,full_hnf=np.array(Hrows,dtype=np.int64),
    corrected_integral_hnf_coordinates=np.array([int(a) for a in lattice_coordinates],dtype=np.int64),
    beta_word=np.array(bw,dtype=np.int16),A_word=np.array(aw,dtype=np.int16),
    correction_word=np.array(hw,dtype=np.int16))
print('PASS explicit pure s-fixed common-source correction; support',np.flatnonzero(coeff).tolist(),flush=True)
print('PASS corrected cusp defect is zero in the full integral canonical multiplier.',flush=True)
print('PASS ternary f=A=1; correction joins with identity through the actual common-base CRT.',flush=True)

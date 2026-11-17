#!/usr/bin/env python3
"""Reproduce the selected common-mod6 record directly from affine outputs."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
original=np.load(HERE/'census_common_mod6_frames.npz')
family=np.load(HERE/'check_modular_binary_central_family.npz')
items={k:original[k].copy() for k in original.files}
passing=family['b0_p2_c1_survivors']
assert len(passing)==2048
mask=int(passing[0]);assert mask==31
v=np.array([(mask>>i)&1 for i in range(16)],dtype=np.int64)
items['b0_p2_particular'][:,1]=(items['b0_p2_particular'][:,1]+v@items['b0_p2_nullspace'])%2
items['b0_p2_beta_1']=(items['b0_p2_beta_1']+v@family['b0_p2_beta_variations'])%2
items['b0_p2_A_1']=(items['b0_p2_A_1']+v@family['b0_p2_A_variations'])%2
assert np.any(items['b0_p2_particular'][:,1])
assert not np.any(items['b0_p3_particular'][:,1])
assert not np.any(items['b0_p3_A_1'])
for p in (2,3):
    k=f'b0_p{p}'
    assert not np.any((items[k+'_A97']@items[k+'_particular'][:,1]-items[k+'_rhs'][:,1])%p)
np.savez_compressed(HERE/'common_mod6_liftable_record.npz',**items)
Path(__file__).with_suffix('.json').write_text(json.dumps({
    'base':0,'candidate':1,'selected_binary_mask':mask,
    'binary_passing_count':len(passing),'ternary_f_and_A_are_identity':True,
    'literal_affine_constraints_verified':True,'all_assertions_passed':True},indent=2)+'\n')
print('PASS mask31 selected and all literal common-source affine equations verified.')

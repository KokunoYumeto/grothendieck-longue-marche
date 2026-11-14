#!/usr/bin/env python3
"""All thirty independent sign choices on the ten central-pullback lifts.

The complete raw run has ten generator-exponent columns and three
center columns.  Its field 'original_generator_sign_freedoms' counts
the ten generator slots; the actual sign-choice space is Mat(10,3,F2).
Each elementary lift change is an invertible column operation.  This
certificate retains that exact comparison without changing the original
complete-run artifacts.
"""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np

HERE=Path(__file__).resolve().parent


def rank2(A):
    A=A.copy()%2;r=0
    for j in range(A.shape[1]):
        k=next((k for k in range(r,len(A)) if A[k,j]),None)
        if k is None:continue
        A[[r,k]]=A[[k,r]]
        for k in range(len(A)):
            if k!=r and A[k,j]:A[k]^=A[r]
        r+=1
    return r


def main():
    started=time.time();names=['de_a6_gl_central.json','de_a6_gl_central_replay.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());A=np.load(HERE/names[1])['relation_matrix']
    assert A.shape==(13,13) and rank2(A)==13
    assert raw['original_generator_sign_freedoms']==10
    transforms=[]
    for i in range(10):
        for j in range(3):
            M=np.eye(13,dtype=np.int64);M[i,10+j]=1
            assert np.array_equal(M@M%2,np.eye(13,dtype=np.int64))
            B=A@M%2;expected=A.copy();expected[:,10+j]^=expected[:,i]
            assert np.array_equal(B,expected) and rank2(B)==13
            transforms.append(M)
    # All30 elementary matrices commute and independently parameterize
    # the full Mat(10,3,F2) block.  Their products cover every lift choice.
    assert all(np.array_equal(M@N%2,N@M%2) for M in transforms for N in transforms)
    assert rank2(np.array([(M-np.eye(13,dtype=np.int64)).ravel()%2 for M in transforms]))==30
    out={'status':'PASS_ALL_CENTRAL_LIFT_SIGN_FREEDOMS',
         'original_generator_exponent_columns':10,'center_columns':3,
         'independent_central_lift_sign_parameters':30,
         'number_of_lift_sign_choices':2**30,
         'all30_elementary_changes_verified':True,
         'exact_matrix_comparison':'(e,z) maps to (e,z+eD), D in Mat(10,3,F2)',
         'full_rank_and_perfection_independent_of_all_lift_choices':True,
         'raw_metadata_clarification':'The original run field counts ten generator slots; it is not the binary dimension of the lift-choice space.',
         'original_complete_run_files_preserved':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_central_signs.npz',elementary_column_changes=np.array(transforms))
    (HERE/'de_a6_gl_central_signs.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()

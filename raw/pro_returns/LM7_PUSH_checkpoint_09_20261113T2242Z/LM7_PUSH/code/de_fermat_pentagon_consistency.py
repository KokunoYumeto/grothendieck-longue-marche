#!/usr/bin/env python3
"""Compare the complete original and degree-pruned pentagon executions."""
from pathlib import Path
import json
import numpy as np
here=Path(__file__).resolve().parent
A=np.load(here/'de_fermat_pentagon_arithmetic_certificate.npz')
B=np.load(here/'de_fermat_pentagon_arithmetic_fast_certificate.npz')
assert A.files==B.files and all(np.array_equal(A[k],B[k]) for k in A.files)
a=json.loads((here/'de_fermat_pentagon_arithmetic.json').read_text())
b=json.loads((here/'de_fermat_pentagon_arithmetic_fast.json').read_text())
assert a['branch_results']==b['branch_results']
assert a['base_pentagon_residual']==b['base_pentagon_residual']
def rank(M):
    M=np.array(M,dtype=np.int64)%3;r=0
    for c in range(M.shape[1]):
        inds=np.flatnonzero(M[r:,c])
        if not len(inds):continue
        j=r+inds[0];M[[r,j]]=M[[j,r]]
        M[r]=M[r]*pow(int(M[r,c]),-1,3)%3
        q=M[:,c].copy();q[r]=0;M=(M-q[:,None]*M[r])%3;r+=1
        if r==M.shape[0]:break
    return r
out={'unpruned_and_pruned_full_results_equal':True,
     'unpruned_seconds':a['elapsed_seconds'],'pruned_seconds':b['elapsed_seconds'],
     'full_direction_rank':rank(B['direction_residuals']),
     'true_kernel_rank':rank(B['direction_residuals'][:,6:]),
     'remaining_candidate_coordinate_kernel_ranks':[
         [r['branch'],rank(r['candidate_coordinate_kernel'])] for r in b['branch_results']]}
(here/'de_fermat_pentagon_consistency.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

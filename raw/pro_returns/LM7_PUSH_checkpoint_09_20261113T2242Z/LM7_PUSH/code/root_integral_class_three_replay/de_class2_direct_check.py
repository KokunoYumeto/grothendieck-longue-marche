#!/usr/bin/env python3
"""Independent direct exterior-square check of the order-three obstruction.
Builds the full 9312-by-4656 dual relation matrix instead of the Jordan
block reduction, and compares its nullspace with that construction.
"""
from contextlib import redirect_stdout
from pathlib import Path
import ctypes,io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_class2_refinement.py'))
S,R=d['S'],d['R'];n=97;up=np.triu_indices(n,1);w=len(up[0]);SR=S@R%3
matrix=np.zeros((2*w,w),dtype=np.uint8)
for k,(i,j) in enumerate(zip(*up)):
    a=(np.outer(S[:,i],S[:,j])-np.outer(S[:,j],S[:,i]))[up]%3
    b=(np.outer(SR[:,i],SR[:,j])-np.outer(SR[:,j],SR[:,i]))[up]%3
    matrix[k]=(-a)%3;matrix[k,k]=(int(matrix[k,k])+1)%3
    matrix[w+k]=(a-b)%3
original=matrix.copy();piv=np.zeros(w,dtype=np.int32);start=time.time()
rank=d['gf'](matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8)),*matrix.shape,piv.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
piv=piv[:rank].tolist();free=[j for j in range(w) if j not in piv]
kernel=np.zeros((w,len(free)),dtype=np.uint8)
for k,j in enumerate(free):kernel[j,k]=1;kernel[piv,k]=(-matrix[:rank,j].astype(np.int16))%3
assert len(free)==8
assert not np.any(original.astype(np.uint16)@kernel.astype(np.uint16)%3)
J=np.stack([B[up] for B in d['invariant_matrices']],axis=1)%3
_,p=d['rref'](np.column_stack((J,kernel)).T);assert len(p)==8
assert d['vr_rank']==3
out={'full_relation_matrix_shape':list(original.shape),'relation_rank':rank,'cokernel_dimension':len(free),'jordan_and_direct_nullspaces_agree':True,'centralizer_variation_rank':d['vr_rank'],'pass_counts':d['counts'],'elapsed_elimination_seconds':round(time.time()-start,3)}
(here/'de_class2_direct_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

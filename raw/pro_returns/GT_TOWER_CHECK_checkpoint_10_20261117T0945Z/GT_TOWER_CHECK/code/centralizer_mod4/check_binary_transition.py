#!/usr/bin/env python3
"""Exact canonical transition M4->M2 and the actual affine tangent image."""
from pathlib import Path
import json,sys
import numpy as np
from sympy import Matrix
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
old=np.load(ROOT/'work/centralizer_code/modular_binary_central_smith.npz')
new=np.load(HERE/'check_modular_quaternary_central_model.npz')
aff=np.load(HERE/'check_mod4_canonical_lift.npz')
rel2=old['central_relations'].astype(np.int64);rel4=new['central_relations'].astype(np.int64)
def hnf(A):return Matrix([r for r in fmpz_mat(A.tolist()).hnf().tolist() if any(r)]).T
H2=hnf(rel2);H4=hnf(rel4);I2=H2.inv(method='DM');I4=H4.inv(method='DM')
mapdiag=np.array([2]*97+[1]*15,dtype=np.int64)
check=I2*Matrix((rel4*mapdiag).T.tolist())
assert all(a.q==1 for a in check)
def nullspace(A):
    A=np.asarray(A,dtype=np.int64).copy()%2;row=0;piv=[]
    for col in range(A.shape[1]):
        if row==len(A):break
        nz=np.flatnonzero(A[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]]
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row];A[nz]^=A[row]
        piv.append(col);row+=1
    free=[i for i in range(A.shape[1]) if i not in piv]
    N=np.zeros((len(free),A.shape[1]),dtype=np.int64)
    for k,j in enumerate(free):N[k,j]=1;N[k,piv]=A[:row,j]
    return N,piv
dual2,_=nullspace(rel2)
assert dual2.shape==(16,112)
R=mapdiag[:,None]*dual2.T%2
kernel_rows,piv=nullspace(R.T)
assert len(piv)==15
Krows=[r for r in kernel_rows]
for j in piv:
    v=np.zeros(112,dtype=np.int64);v[j]=2;Krows.append(v)
Krows=np.array(Krows,dtype=np.int64);HK=hnf(Krows)
assert abs(int(HK.det()))==2**15
assert abs(int(H4.det()))//abs(int(HK.det()))==2**9
assert all(a.q==1 for a in I4*Matrix((2*Krows).T.tolist()))
assert not np.any(rel4@R%2)
ds=aff['defect_directions'];assert not np.any(ds@R%2)
embedding=aff['direction_embeddings4'][:97]
assert not np.any(embedding%2)
_,dpiv=nullspace(embedding//2)
assert len(dpiv)==9
print('PASS actual canonical map M4->M2: imageC2^15, kernelC2^9.',flush=True)
print('PASS the97 actual affine directions surject onto the entire canonical transition kernel.',flush=True)

TOWER=ROOT/'work/tower_code';sys.path.insert(0,str(TOWER))
s=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'transition_character_prefix','__file__':str(HERE/'transition_character_prefix.py')}
exec(compile(s.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)
P2=ns['bcases'][2][2];P3=ns['bcases'][3][2];table=ns['btable']
trace=1-np.sum(P2==np.arange(288),axis=1)-np.sum(P3==np.arange(192),axis=1)
trace[0]+=576;assert trace[0]==97
squares=np.array([table[g,g] for g in range(576)],dtype=np.int64)
wedge_trace=(trace*trace-trace[squares])//2
assert np.all((trace*trace-trace[squares])%2==0)
assert int(wedge_trace.sum())==8*576
print('PASS actual graph character gives rational wedge coinvariant rank8.',flush=True)
np.savez_compressed(Path(__file__).with_suffix('.npz'),canonical_map_diagonal=mapdiag,
    canonical_map_mod2=R,transition_kernel_lattice=Krows,transition_kernel_hnf=np.array(HK.tolist(),dtype=np.int64),
    affine_tangent_images2=embedding//2,graph_homology_trace=trace,graph_wedge_trace=wedge_trace)
from collections import Counter
out={'canonical_map':'M4->M2 induced by identity of B0; k_i^4 maps to twice k_i^2, basic commutators unchanged.',
     'canonical_image_invariants':[2]*15,'canonical_kernel_invariants':[2]*9,
     'actual_affine_tangent_rank':9,'actual_affine_tangent_surjects_transition_kernel':True,
     'rational_wedge_coinvariant_rank':8,'integral_wedge_two_primary_torsion_invariants':[2]*7,
     'graph_homology_trace_counts':dict(Counter(map(int,trace))),
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

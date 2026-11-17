#!/usr/bin/env python3
"""Saturated integral affine lattice and its binary canonical tangent image."""
from pathlib import Path
import json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
d=np.load(HERE/'check_integral_affine_system.npz')
A=d['free_matrix'];b=d['free_rhs'];seed=d['binary_seed']
AZ=fmpz_mat(A.tolist());H,T=AZ.transpose().hnf(transform=True)
assert H==T*AZ.transpose()
rank=195
assert all(not any(H[i,j] for j in range(H.ncols())) for i in range(rank,H.nrows()))
piv=[next(j for j in range(H.ncols()) if H[i,j]) for i in range(rank)]
HS=fmpz_mat([[H[i,j] for j in piv] for i in range(rank)])
rhs=fmpz_mat([[int(b[j])] for j in piv])
sol=HS.transpose().solve(rhs)
assert all(v.denominator==1 for v in sol.entries())
w=fmpz_mat([[int(sol[i,0])] if i<rank else [0] for i in range(291)])
point=T.transpose()*w
assert AZ*point==fmpz_mat([[int(a)] for a in b])
K=fmpz_mat([[T[i,j] for j in range(291)] for i in range(rank,291)])
assert not any((AZ*K.transpose()).entries())
def solve2(M,v):
    M=np.asarray(M,dtype=np.int64).copy()%2;v=np.asarray(v,dtype=np.int64).copy()%2
    if v.ndim==1:v=v[:,None]
    orig=M.copy();ov=v.copy();r=0;p=[]
    for j in range(M.shape[1]):
        if r==len(M):break
        nz=np.flatnonzero(M[r:,j])
        if not len(nz):continue
        k=r+int(nz[0]);M[[r,k]]=M[[k,r]];v[[r,k]]=v[[k,r]]
        nz=np.flatnonzero(M[:,j]);nz=nz[nz!=r];M[nz]^=M[r];v[nz]^=v[r];p.append(j);r+=1
    good=not np.any(v[r:]);ans=np.zeros((M.shape[1],v.shape[1]),dtype=np.int64);ans[p]=v[:r]
    if good:assert not np.any((orig@ans-ov)%2)
    return good,ans,r
K2=np.array([[int(K[i,j])%2 for j in range(291)] for i in range(96)],dtype=np.int64)
point2=np.array([int(point[i,0])%2 for i in range(291)],dtype=np.int64)
good,coeff,r=solve2(K2.T,(seed-point2)%2)
assert good and r==96
matched=point+K.transpose()*fmpz_mat(coeff.tolist())
assert AZ*matched==fmpz_mat([[int(a)] for a in b])
assert all((int(matched[i,0])-int(seed[i]))%2==0 for i in range(291))

integral=np.load(ROOT/'work/ghost_mod4/check_integral_eight_map.npz')
change=integral['coefficient_four_change'].astype(np.int64)%4
kernel4=np.array([[int(K[i,j])%4 for j in range(291)] for i in range(96)],dtype=np.int64)
matched4=np.array([int(matched[i,0])%4 for i in range(291)],dtype=np.int64)
kernel_old=np.hstack([kernel4[:,97*i:97*(i+1)]@change%4 for i in range(3)])
matched_old=np.concatenate([matched4[97*i:97*(i+1)]@change%4 for i in range(3)])
aff=np.load(HERE/'check_mod4_canonical_lift.npz')
good,coordinates,rank2=solve2(aff['affine_directions2'].T,kernel_old.T%2)
assert good and rank2==97
images=coordinates.T@(aff['direction_embeddings4'][:97]//2)%2
_,_,tangent_rank=solve2(images.T,np.zeros(112,dtype=np.int64))
print('PASS saturated integral affine lattice: rank96, with an integral point matching the corrected binary record.',flush=True)
print('HONEST affine lattice tangent rank in M4:',tangent_rank,flush=True)
out={'scope':'Saturated integral affine solution lattice, with actual reduction into the coefficient-four source.',
     'kernel_rank':96,'integer_point_matches_binary_record':True,
     'honest_affine_tangent_rank_at_first_transition':tangent_rank,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
# Exact full integer arrays are JSON because the unimodular transform can
# contain entries beyond a machine integer; small reductions remain NPZ.
exact={'kernel':[[str(K[i,j]) for j in range(291)] for i in range(96)],
       'particular':[str(matched[i,0]) for i in range(291)],
       'hnf_transform':[[str(T[i,j]) for j in range(291)] for i in range(291)]}
Path(__file__).with_name('integral_affine_lattice_exact.json').write_text(json.dumps(exact)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),kernel_mod4=kernel4,particular_mod4=matched4,
    kernel_old_mod4=kernel_old,particular_old_mod4=matched_old,
    first_transition_tangent=images,first_transition_coordinates=coordinates.T)

#!/usr/bin/env python3
"""Independent free-wedge Jacobian of the honest integral frame lattice.

All coordinates come from the retained integral source and the actual
modulus-four canonical central cover.  This computes a finite Jacobian,
not a lift of a profinite parameter.
"""
from pathlib import Path
import hashlib,json
import numpy as np
from flint import fmpz_mat

ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'work/centralizer_mod4'
files=['check_integral_affine_lattice.npz','check_mod4_canonical_lift.npz','check_modular_quaternary_central_model.npz']
aff=np.load(D/files[0]); cen=np.load(D/files[1]); mod=np.load(D/files[2])

def rref2(a):
    a=np.asarray(a,dtype=np.int64).copy()%2
    rank=0;piv=[]
    for j in range(a.shape[1]):
        if rank==len(a):break
        nz=np.flatnonzero(a[rank:,j])
        if not len(nz):continue
        k=rank+int(nz[0]);a[[rank,k]]=a[[k,rank]]
        rows=np.flatnonzero(a[:,j]);rows=rows[rows!=rank]
        a[rows]^=a[rank]
        piv.append(j);rank+=1
    return a[:rank],piv

def rank2(a):return len(rref2(a)[1])
def solve2(a,b):
    a=np.asarray(a,dtype=np.int64)%2;b=np.asarray(b,dtype=np.int64)%2
    if b.ndim==1:b=b[:,None]
    n=a.shape[1]
    rr,piv=rref2(np.hstack((a,b)))
    good=not any(j>=n for j in piv)
    out=np.zeros((n,b.shape[1]),dtype=np.int64)
    if good:
        out[piv]=rr[:,n:]
        assert not np.any((a@out-b)%2)
    return good,out

# The seven even relations are precisely the kernel of doubling W4.
even=mod['wedge_even_relations'].astype(np.int64)%2
rr,piv=rref2(even);assert len(piv)==7
free=[j for j in range(15) if j not in piv]
P=np.zeros((15,8),dtype=np.int64);P[free]=np.eye(8,dtype=np.int64)
P[piv]=rr[:,free]
assert not np.any(even@P%2)

# Literal embedding of doubled wedge classes in the full canonical M4.
H=fmpz_mat(cen['full_hnf'].tolist()).transpose()
HI=H.inv()
E=[]
for j in range(15):
    column=[8*HI[i,97+j] for i in range(112)]
    assert all(x.denominator==1 for x in column)
    emb=np.array([int(x)%4 for x in column],dtype=np.int64)
    assert not np.any(emb%2)
    E.append(emb//2)
E=np.array(E,dtype=np.int64)
assert rank2(E)==8 and not np.any(even@E%2)
# Complete comparison with the chosen eight free quotient coordinates.
ES=E[free]
assert np.array_equal(P@ES%2,E)
assert rank2(ES)==8

Di=aff['first_transition_tangent'].astype(np.int64)%2
ok,Dfree=solve2(ES.T,Di.T);assert ok
Dfree=Dfree.T
assert np.array_equal(Dfree@ES%2,Di)
assert rank2(Dfree)==8
A=aff['kernel_old_mod4'][:,194:].astype(np.int64)%2
R=mod['r_action'].astype(np.int64)%2
RA=A@R%2
ij=np.triu_indices(97,1)
WP=mod['wedge_projection4'].astype(np.int64)%2@P%2
assert WP.shape==(4656,8)
q=(A[:,ij[0]]*RA[:,ij[1]]-A[:,ij[1]]*RA[:,ij[0]])%2@WP%2
J=(Dfree+q)%2
rankJ=rank2(J)
print('PASS literal doubling map: Wfree/2 -> 2W4 has dimension8 and injects in the full canonical M4.',flush=True)
print('PASS all96 genuine integral affine directions lift through this exact doubling map.',flush=True)
print('Free finite-difference rank:',rank2(Dfree),'quadratic diagonal rank:',rank2(q),'Jacobian rank:',rankJ,flush=True)

# Check every cross coefficient, not only a sample.
cross=[]
for i in range(96):
    jj=np.arange(i+1,96)
    if not len(jj):continue
    raw=(A[i,ij[0]]*RA[jj][:,ij[1]]-A[i,ij[1]]*RA[jj][:,ij[0]]
         +A[jj][:,ij[0]]*RA[i,ij[1]]-A[jj][:,ij[1]]*RA[i,ij[0]])%2
    out=raw@WP%2
    for j,row in zip(jj,out):
        if np.any(row):cross.append((i,int(j),row.tolist()))
print('All4560 quadratic cross coefficients vanish:',not cross,flush=True)
assert not cross
_,jr=rref2(J.T)
ind=np.array(jr,dtype=np.int64)
minor=J[ind]
assert len(ind)==rankJ
save=Path(__file__).with_suffix('.npz')
np.savez_compressed(save,wedge_free_projection=P,doubling_embedding=E,
    free_embedding=ES,finite_difference=Dfree,quadratic_diagonal=q,
    jacobian=J,independent_directions=ind,independent_rows=minor,
    wedge_projected=WP,A_directions=A,r_action=R)
out={'scope':'Exact free canonical Jacobian on all96 honest integral affine directions; no profinite lift is asserted.',
 'input_sha256':{f:hashlib.sha256((D/f).read_bytes()).hexdigest() for f in files},
 'doubling_dimension':8,'finite_difference_rank':rank2(Dfree),
 'quadratic_diagonal_rank':rank2(q),'jacobian_rank':rankJ,
 'independent_directions':ind.tolist(),'cross_coefficients_checked':4560,
 'all_cross_coefficients_zero':not cross,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

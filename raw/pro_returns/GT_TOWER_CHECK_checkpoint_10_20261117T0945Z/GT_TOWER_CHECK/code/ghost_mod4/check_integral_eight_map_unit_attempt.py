#!/usr/bin/env python3
"""Exact integral target reduction and the actual eight-map common lattice.

All row and column operations are over Z.  No coefficient rank is used
to infer integral saturation.  Every factorization is checked in both
the free target coordinates and its actual order-six coordinates.
"""
from pathlib import Path
import json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent
src=(HERE/'check_fivepoint_quartic_module.py').read_text()
exec(compile(src.split('R,piv=rref(C.matrix)',1)[0],str(HERE/'integral_prefix.py'),'exec'),globals())

def unit_reduce_integer(matrix):
    A=np.asarray(matrix,dtype=np.int64).copy()
    r=0;piv=[]
    while True:
        available=[i for i in range(A.shape[1]) if i not in piv]
        sub=A[r:,available]
        possible=np.argwhere(np.abs(sub)==1)
        if not len(possible):break
        # Choose the first column with a unit, then its first row.
        cpos=int(possible[:,1].min())
        rr=int(possible[possible[:,1]==cpos,0].min())
        col=available[cpos];j=r+rr
        A[[r,j]]=A[[j,r]]
        if A[r,col]==-1:A[r]*=-1
        assert A[r,col]==1
        coeff=A[:,col].copy();coeff[r]=0
        bound=int(np.abs(A).max())+int(np.abs(coeff).max())*int(np.abs(A[r]).max())
        assert bound<2**62,('integer arithmetic bound',bound)
        nz=np.flatnonzero(coeff)
        A[nz]-=coeff[nz,None]*A[r]
        piv.append(col);r+=1
        assert np.array_equal(A[:,piv],np.vstack((np.eye(r,dtype=np.int64),np.zeros((len(A)-r,r),dtype=np.int64))))
        if r%100==0:print('INTEGRAL unit pivots',r,'max entry',int(np.abs(A).max()),flush=True)
        if r==len(A):break
    return A,piv

rel,piv=unit_reduce_integer(C.matrix)
assert len(piv)==667
free=[j for j in range(769) if j not in piv]
P0=np.zeros((769,102),dtype=np.int64)
P0[free]=np.eye(102,dtype=np.int64);P0[piv]=-rel[:667,free]
residual=rel[667:,free]
assert not np.any(residual%6)
small,sp=unit_reduce_integer(residual//6)
assert len(sp)==2 and not np.any(small[2:])
sf=[j for j in range(102) if j not in sp]
P1=np.zeros((102,102),dtype=np.int64)
for j,c in enumerate(sf):
    P1[c,j]=1;P1[sp,j]=-small[:2,c]
for j,c in enumerate(sp):P1[c,100+j]=1
assert abs(int(fmpz_mat(P1.tolist()).det()))==1
PN=P0@P1
assert not np.any(C.matrix@PN[:,:100])
assert not np.any(C.matrix@PN[:,100:]%6)
assert np.array_equal(small[:2]@P1,np.hstack((np.zeros((2,100),dtype=np.int64),np.eye(2,dtype=np.int64))))
print('PASS actual integral target Z^100 plus C6^2, with explicit generator projection.',flush=True)

chunk=src.split('x12=',1)[1].split('T=np.hstack',1)[0]
exec(compile('x12='+chunk,str(HERE/'integral_target_words.py'),'exec'),globals())
rawblocks=[];blocks=[]
for pair in pairs:
    raw=np.array([target_chain(subst(w,pair)) for w in loops],dtype=np.int64)
    rawblocks.append(raw)
    blocks.append(raw@PN)
T=np.hstack(blocks)
freecols=[102*i+j for i in range(8) for j in range(100)]
torscols=[102*i+j for i in range(8) for j in (100,101)]
T[:,torscols]%=6

# Rebuild the modular Schreier map integrally (no reduction modulo four).
chunk='kgens='+src.split('kgens=',1)[1].split('modular_rank=',1)[0]
chunk=chunk.replace('return row%4','return row')
exec(compile(chunk,str(HERE/'integral_modular_words.py'),'exec'),globals())
Q=modular.astype(np.int64)
HH,UU=fmpz_mat(Q.tolist()).hnf(transform=True)
H=np.array(HH.tolist(),dtype=np.int64);U=np.array(UU.tolist(),dtype=np.int64)
assert np.array_equal(U@Q,H)
assert not np.any(H[97:])
W=H[:97];assert abs(int(fmpz_mat(W.tolist()).det()))==3
WI=fmpz_mat(W.tolist()).inv()
CQ=fmpz_mat(Q.tolist())*WI
assert all(v.denominator==1 for row in CQ.tolist() for v in row)
CP=np.array([[int(v) for v in row] for row in CQ.tolist()],dtype=np.int64)
left=U[:97]
assert np.array_equal(CP@W,Q)
assert np.array_equal(left@CP,np.eye(97,dtype=np.int64))
F=left@T
defect=T-CP@F
assert not np.any(defect[:,freecols]),('rational factorization defect',np.count_nonzero(defect[:,freecols]))
assert not np.any(defect[:,torscols]%6),('torsion factorization defect',np.count_nonzero(defect[:,torscols]%6))
print('PASS both exact common-lattice/modular maps and all eight integral target factorizations.',flush=True)

FD=fmpz_mat(F[:,freecols].tolist()).snf()
diag=[int(FD[i,i]) for i in range(97)]
assert all(a>0 for a in diag)
print('Common image free-target Smith invariants:',{a:diag.count(a) for a in sorted(set(diag))},flush=True)

out={'scope':'Exact integral target and actual eight-map image of the common kernel J.',
     'target_free_rank':100,'target_torsion':[6,6],
     'modular_lattice_index':3,'common_integral_rank':97,
     'free_target_smith_invariants':diag,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
    target_relation_matrix=C.matrix,target_unit_reduction=rel,target_unit_pivots=np.array(piv),
    target_unit_free_columns=np.array(free),target_initial_projection=P0,
    target_six_relation_reduction=small,target_six_pivots=np.array(sp),
    target_basis_change=P1,target_projection=PN,raw_eight_chain=np.hstack(rawblocks),
    eight_map=T,target_free_columns=np.array(freecols),target_torsion_columns=np.array(torscols),
    modular_restriction=Q,modular_lattice_basis=W,common_projection=CP,
    common_left_inverse=left,target_from_common=F,free_target_smith=np.array(diag,dtype=np.int64))
print('PASS full integral maps and exact arithmetic witnesses saved.',flush=True)

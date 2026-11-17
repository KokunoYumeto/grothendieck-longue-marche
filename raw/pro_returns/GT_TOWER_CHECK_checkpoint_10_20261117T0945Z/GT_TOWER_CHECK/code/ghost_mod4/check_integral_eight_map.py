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

print('Reducing integral unit relations before the small residual Hermite form.',flush=True)
rel,piv=unit_reduce_integer(C.matrix)
print('Integral unit count',len(piv),'residual max',int(np.abs(rel[len(piv):]).max()),flush=True)
np.savez_compressed(HERE/'target_integral_unit_precheck.npz',relation=rel,pivots=np.array(piv))
# A unit Smith invariant may remain hidden in a small nonunit matrix.
# Retain and diagonalize that exact residual with both transformations.
free=[j for j in range(769) if j not in piv]
P0=np.zeros((769,len(free)),dtype=np.int64)
P0[free]=np.eye(len(free),dtype=np.int64);P0[piv]=-rel[:len(piv),free]
residual=rel[len(piv):,free]
residual=residual[np.any(residual,axis=1)]
residual_before_hnf=residual.copy()
print('Small integral Hermite stage',residual.shape,flush=True)
residual=np.array(fmpz_mat(residual.tolist()).hnf().tolist(),dtype=np.int64)
residual=residual[np.any(residual,axis=1)]
print('Exact nonzero residual rank',len(residual),flush=True)
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
DM=DomainMatrix.from_list_sympy(*residual.shape,residual.tolist()).convert_to(ZZ)
DD,LL,VV=smith_normal_decomp(DM)
small=np.array(DD.to_Matrix().tolist(),dtype=np.int64)
resleft=np.array(LL.to_Matrix().tolist(),dtype=np.int64)
resright=np.array(VV.to_Matrix().tolist(),dtype=np.int64)
assert np.array_equal(resleft@residual@resright,small)
assert abs(int(fmpz_mat(resleft.tolist()).det()))==1
assert abs(int(fmpz_mat(resright.tolist()).det()))==1
rd=[int(small[i,i]) for i in range(min(small.shape))]
units=[i for i,a in enumerate(rd) if abs(a)==1]
tors=[i for i,a in enumerate(rd) if abs(a)>1]
zeros=[i for i in range(len(free)) if i>=len(rd) or rd[i]==0]
assert len(piv)+len(units)==667
assert [abs(rd[i]) for i in tors]==[6,6] and len(zeros)==100
P1=resright[:,zeros+tors]
PN=P0@P1
assert not np.any(C.matrix@PN[:,:100])
assert not np.any(C.matrix@PN[:,100:]%6)
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

# An explicit integral right inverse proves primitivity without
# inferring it from rational rank or any finite set of reductions.
FH,FU=fmpz_mat(F[:,freecols].T.tolist()).hnf(transform=True)
FH=np.array(FH.tolist(),dtype=np.int64);FU=np.array(FU.tolist(),dtype=np.int64)
assert np.array_equal(FH[:97],np.eye(97,dtype=np.int64)) and not np.any(FH[97:])
G=FU[:97].T
assert np.array_equal(F[:,freecols]@G,np.eye(97,dtype=np.int64))
# The integral B action is collected on the same actual source words.
def integral_jchain(w):
    q=0;row=np.zeros(289,dtype=np.int64)
    for a in w:
        if a>0:edge=(q,a-1);q=int(jtable[q,jgens[a-1]]);sign=1
        else:q=int(jtable[q,jinvtable[jgens[-a-1]]]);edge=(q,-a-1);sign=-1
        if edge in ci:row[ci[edge]]+=sign
    assert q==0
    return row
QA={};SA={}
for name,aut in deck.items():
    SA[name]=np.array([integral_jchain(subst(w,aut)) for w in loops],dtype=np.int64)
    QA[name]=left@SA[name]@CP
    assert np.array_equal(SA[name]@CP,CP@QA[name])
assert np.array_equal(QA['s']@QA['s'],np.eye(97,dtype=np.int64))
assert np.array_equal(QA['r']@QA['r']@QA['r'],np.eye(97,dtype=np.int64))
exponents=np.array([[sum((1 if a==j else -1 if a==-j else 0) for a in w)//6
                    for j in (1,2)] for w in loops],dtype=np.int64)
exponent_factor=left@exponents
assert np.array_equal(CP@exponent_factor,exponents)
old4=np.load(HERE/'check_fivepoint_quartic_mixed_module.npz')
assert np.array_equal(CP@W%4,old4['common_projection'])
assert np.array_equal(QA['s']@W%4,W@old4['quotient_s']%4)
assert np.array_equal(QA['r']@W%4,W@old4['quotient_r']%4)
pinv=fmpz_mat(resright.tolist()).inv()
pinv=np.array([[int(a) for a in row] for row in pinv.tolist()],dtype=np.int64)
pzero=np.zeros((len(free),769),dtype=np.int64);pzero[:,free]=np.eye(len(free),dtype=np.int64)
PNleft=pinv[zeros+tors]@pzero
assert np.array_equal(PNleft@PN,np.eye(102,dtype=np.int64))
print('PASS integral split free-target embedding, literal B action and coefficient-four change.',flush=True)

out={'scope':'Exact integral target and actual eight-map image of the common kernel J.',
     'target_free_rank':100,'target_torsion':[6,6],
     'modular_lattice_index':3,'common_integral_rank':97,
     'free_target_smith_invariants':diag,'source_kernel_all_m':'Kprime J^m = (Kprime K^m) intersect (Fprime F^(6m))',
     'Schreier_words':loops,'pairwords':pairs,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
    target_relation_matrix=C.matrix,target_unit_reduction=rel,target_unit_pivots=np.array(piv),
    target_unit_free_columns=np.array(free),target_initial_projection=P0,
    target_residual_before_hnf=residual_before_hnf,target_residual_matrix=residual,target_residual_smith=small,
    target_residual_left=resleft,target_residual_right=resright,
    target_basis_change=P1,target_projection=PN,target_projection_left_inverse=PNleft,raw_eight_chain=np.hstack(rawblocks),
    eight_map=T,target_free_columns=np.array(freecols),target_torsion_columns=np.array(torscols),
    modular_restriction=Q,modular_lattice_basis=W,common_projection=CP,
    common_left_inverse=left,target_from_common=F,free_target_smith=np.array(diag,dtype=np.int64),
    common_from_free_target=G,source_s=SA['s'],source_r=SA['r'],
    quotient_s=QA['s'],quotient_r=QA['r'],divided_exponent_factor=exponent_factor,
    coefficient_four_change=W%4,source_table=jtable,source_generators=jgens,
    source_chords=np.array(chords),modular_table=ktable,modular_generators=kgi,
    modular_chords=np.array(kchords))
print('PASS full integral maps and exact arithmetic witnesses saved.',flush=True)

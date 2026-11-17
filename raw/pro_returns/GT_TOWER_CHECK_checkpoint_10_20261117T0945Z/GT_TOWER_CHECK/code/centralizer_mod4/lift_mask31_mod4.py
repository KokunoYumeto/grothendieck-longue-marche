#!/usr/bin/env python3
"""Actual affine mod2-to-mod4 pentagon/frame lift, retaining mixed target torsion."""
from pathlib import Path
import json,sys
import numpy as np

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
WORK=ROOT/'work';TOWER=WORK/'tower_code'
sys.path.insert(0,str(TOWER))
src=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'quartic_affine_prefix','__file__':str(HERE/'quartic_affine_prefix.py')}
exec(compile(src.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)
mod=np.load(WORK/'ghost_mod4/check_fivepoint_quartic_mixed_module.npz')
P=mod['common_projection'].astype(np.int64);L=mod['projection_left_inverse'].astype(np.int64)
assert np.array_equal(L@P%4,np.eye(97,dtype=np.int64))
target=mod['target_h1_projection'].astype(np.int64).copy()
target[:,100:]*=2;target%=4
assert not np.any(mod['target_relation_matrix']@target%4)
ns['projections'][4]=target
jt=ns['jtable'];jg=ns['jgens'];ji=ns['jinverse'];jp=ns['jpaths'];jl=ns['jloops']
ci={tuple(a):i for i,a in enumerate(ns['jchords'])}
inverse=ns['inverse'];subst=ns['subst'];SX=((2,),(1,));RX=((2,),(-2,-1))
def chain(w):
    a=0;v=np.zeros(289,dtype=np.int64)
    for j in w:
        k=abs(int(j))-1
        if j>0:e=(a,k);a=int(jt[a,jg[k]]);sgn=1
        else:a=int(jt[a,ji[jg[k]]]);e=(a,k);sgn=-1
        if e in ci:v[ci[e]]+=sgn
    return a,v

matrices=[];rhs=[]
for name,tokens in ns['expressions'].items():
    raw,b=ns['expression_matrix'](0,tokens,4)
    A=raw@L.T%4
    assert np.array_equal(A@P.T%4,raw)
    matrices.append(np.hstack((A,np.zeros((len(A),194),dtype=np.int64))))
    rhs.extend(b.tolist())
ab=mod['divided_exponent_factor'].astype(np.int64)
matrices.append(np.hstack((ab.T,np.zeros((2,194),dtype=np.int64))));rhs.extend([0,0])
I=np.eye(97,dtype=np.int64);Z=np.zeros_like(I)
S=mod['quotient_s'].astype(np.int64);R=mod['quotient_r'].astype(np.int64)
bbase=252;abase=0
ds=(chain(subst(jp[bbase],SX))[1]-chain(jp[bbase])[1])@P%4
dr=np.zeros(97,dtype=np.int64)
matrices.append(np.hstack((I,-(S-I).T,Z)));rhs.extend(ds.tolist())
matrices.append(np.hstack((I,Z,-(R-I).T)));rhs.extend(dr.tolist())
matrices.append(np.hstack((np.zeros((2,194),dtype=np.int64),ab.T)));rhs.extend([0,0])
A=np.vstack(matrices)%4;b=np.array(rhs,dtype=np.int64)%4
old=np.load(WORK/'centralizer_code/check_common_mod6_liftable_automorphism.npz')
oldmod=np.load(WORK/'ghost_code/check_fivepoint_binary_module.npz')
u=old['f_2']@oldmod['projection_left_inverse']%2
fw=tuple(t for i in range(289) if u[i] for t in jl[i])
cor=np.load(WORK/'centralizer_code/check_common_mod6_canonical_correction.npz')
bw=tuple(map(int,cor['beta_word']))+tuple(map(int,cor['correction_word']))
aw=tuple(map(int,cor['A_word']))
assert chain(fw)[0]==0 and chain(bw)[0]==bbase and chain(aw)[0]==0
seed=np.concatenate([chain(w)[1]@P%4 for w in (fw,bw,aw)])
residual=(b-A@seed)%4
assert not np.any(residual%2)

def solve2(M,v):
    M=np.asarray(M,dtype=np.int64).copy()%2;v=np.asarray(v,dtype=np.int64).copy()%2
    if v.ndim==1:v=v[:,None]
    origM=M.copy();origv=v.copy();row=0;piv=[]
    for col in range(M.shape[1]):
        if row==len(M):break
        nz=np.flatnonzero(M[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);M[[row,j]]=M[[j,row]];v[[row,j]]=v[[j,row]]
        nz=np.flatnonzero(M[:,col]);nz=nz[nz!=row]
        M[nz]^=M[row];v[nz]^=v[row]
        piv.append(col);row+=1
    good=not np.any(v[row:]);point=np.zeros((M.shape[1],v.shape[1]),dtype=np.int64)
    point[piv]=v[:row]
    free=[j for j in range(M.shape[1]) if j not in piv]
    basis=np.zeros((len(free),M.shape[1]),dtype=np.int64)
    for i,j in enumerate(free):basis[i,j]=1;basis[i,piv]=M[:row,j]
    assert not np.any(origM@basis.T%2)
    if good:assert not np.any((origM@point-origv)%2)
    return good,point[:,0],basis,row
good,point,kernel,rank=solve2(A,residual//2)
print('ACTUAL fixed-frame mod4 lift:',good,'rank',rank,'free binary lift coordinates',len(kernel),flush=True)
out={'scope':'Actual common-source affine lifting of mask31 through coefficient4, with the full mixed target.',
     'target_free_rank':100,'target_binary_torsion_rank':2,
     'equations':len(A),'variables':291,'rank_mod2':rank,'fixed_frame_lift_exists':good,
     'fixed_frame_lift_dimension':len(kernel)}
save={'matrix4':A,'rhs4':b,'seed4':seed,'residual2':residual//2,'lift_kernel2':kernel}
if good:
    answer=(seed+2*point)%4
    assert not np.any((A@answer-b)%4)
    save['solution4']=answer
    save['f4']=answer[:97];save['beta4']=answer[97:194];save['A4']=answer[194:]
    assert np.array_equal(answer[:97]@mod['binary_reduction_change']%2,old['f_2'])
    out['literal_equations_verified']=True
else:
    out['literal_equations_verified']=False
np.savez_compressed(Path(__file__).with_suffix('.npz'),**save)
out['all_assertions_passed']=True
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

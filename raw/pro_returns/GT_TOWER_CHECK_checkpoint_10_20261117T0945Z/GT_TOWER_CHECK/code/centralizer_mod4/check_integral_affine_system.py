#!/usr/bin/env python3
"""Exact integral affine source system for the fixed harmonic base frame.

The100 free target coordinates are integral.  The two C6 coordinates
per expression remain explicit torsion conditions.
"""
from pathlib import Path
import sys,json
import numpy as np
from flint import fmpz_mat

HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
TOWER=ROOT/'work/tower_code';sys.path.insert(0,str(TOWER))
src=(TOWER/'test_fivepoint_cm_level.py').read_text()
ns={'__name__':'integral_affine_prefix','__file__':str(HERE/'integral_affine_prefix.py')}
exec(compile(src.split('records=[];base_records=[]',1)[0],str(TOWER/'test_fivepoint_cm_level.py'),'exec'),ns)
data=np.load(ROOT/'work/ghost_mod4/check_integral_eight_map.npz')
Q=data['common_projection'].astype(np.int64);L=data['common_left_inverse'].astype(np.int64)
T=data['target_projection'].astype(np.int64)
assert np.array_equal(L@Q,np.eye(97,dtype=np.int64))
jt=ns['jtable'];jg=ns['jgens'];ji=ns['jinverse'];jp=ns['jpaths'];jl=ns['jloops']
ci={tuple(a):i for i,a in enumerate(ns['jchords'])}
wi=ns['inverse'];subst=ns['subst'];SX=((2,),(1,));RX=((2,),(-2,-1))
def chain(w):
    q=0;v=np.zeros(289,dtype=np.int64)
    for j in w:
        k=abs(j)-1
        if j>0:e=(q,k);q=int(jt[q,jg[k]]);sign=1
        else:q=int(jt[q,ji[jg[k]]]);e=(q,k);sign=-1
        if e in ci:v[ci[e]]+=sign
    return q,v
actions={}
for name,imgs in [('s',SX),('r',RX)]:
    raw=np.array([chain(subst(w,imgs))[1] for w in jl],dtype=np.int64)
    actions[name]=L@raw@Q
    assert np.array_equal(raw@Q,Q@actions[name])
assert np.array_equal(actions['s']@actions['s'],np.eye(97,dtype=np.int64))
assert np.array_equal(actions['r']@actions['r']@actions['r'],np.eye(97,dtype=np.int64))

matrices=[];rhs=[];torsA=[];torsb=[]
for name,tokens in ns['expressions'].items():
    current=0;linear=np.zeros((289,769),dtype=np.int64);constant=np.zeros(769,dtype=np.int64)
    for token in tokens:
        if isinstance(token,tuple):
            current,v=ns['chain'](current,token);constant+=v
        else:
            i=abs(token)-1
            linear+=(1 if token>0 else -1)*ns['loops_at'](i,current)
    assert current==0
    exact=linear@T
    common=L@exact
    assert np.array_equal(Q@common[:,:100],exact[:,:100])
    assert not np.any((Q@common[:,100:]-exact[:,100:])%6)
    matrices.append(np.hstack((common[:,:100].T,np.zeros((100,194),dtype=np.int64))))
    rhs.extend((-constant@T[:,:100]).tolist())
    torsA.append(np.hstack((common[:,100:].T,np.zeros((2,194),dtype=np.int64))))
    torsb.extend((-constant@T[:,100:]).tolist())
ab=L@ns['abloops'].T.astype(np.int64)
assert np.array_equal(Q@ab,ns['abloops'].T)
matrices.append(np.hstack((ab.T,np.zeros((2,194),dtype=np.int64))));rhs.extend([0,0])
I=np.eye(97,dtype=np.int64);Z=np.zeros_like(I)
ds=(chain(subst(jp[252],SX))[1]-chain(jp[252])[1])@Q
matrices.append(np.hstack((I,-(actions['s']-I).T,Z)));rhs.extend(ds.tolist())
matrices.append(np.hstack((I,Z,-(actions['r']-I).T)));rhs.extend([0]*97)
matrices.append(np.hstack((np.zeros((2,194),dtype=np.int64),ab.T)));rhs.extend([0,0])
A=np.vstack(matrices);b=np.array(rhs,dtype=np.int64);TA=np.vstack(torsA);tb=np.array(torsb,dtype=np.int64)
assert A.shape==(598,291) and TA.shape==(8,291)
print('Exact integral affine system assembled:',A.shape,'plus8 modulo6 equations.',flush=True)
S=fmpz_mat(A.tolist()).snf()
diag=[abs(int(S[i,i])) for i in range(291) if S[i,i]]
rank=len(diag);rank_aug=fmpz_mat(np.column_stack((A,b)).tolist()).rank()
from collections import Counter
print('INTEGRAL affine Smith invariants',dict(Counter(diag)),'rank',rank,'augmented rank',rank_aug,flush=True)
old=np.load(ROOT/'work/centralizer_code/check_common_mod6_liftable_automorphism.npz')
oldmod=np.load(ROOT/'work/ghost_code/check_fivepoint_binary_module.npz')
u=old['f_2']@oldmod['projection_left_inverse']%2
fw=tuple(t for i in range(289) if u[i] for t in jl[i])
cor=np.load(ROOT/'work/centralizer_code/check_common_mod6_canonical_correction.npz')
bw=tuple(map(int,cor['beta_word']))+tuple(map(int,cor['correction_word']))
aw=tuple(map(int,cor['A_word']))
seed=np.concatenate([chain(w)[1]@Q for w in (fw,bw,aw)])
assert not np.any((A@seed-b)%2)
assert not np.any((TA@seed-tb)%2)
out={'scope':'Exact integral affine equations on the actual common relation lattice.',
     'free_equation_shape':list(A.shape),'torsion_equations':8,
     'smith_nonzero_invariants':diag,'rank':rank,'augmented_rank':int(rank_aug),
     'binary_mask31_seed_verified':True,'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),free_matrix=A,free_rhs=b,
    torsion_matrix=TA,torsion_rhs=tb,common_projection=Q,common_left_inverse=L,
    s_action=actions['s'],r_action=actions['r'],abelian_factor=ab,binary_seed=seed,
    smith=np.array(diag,dtype=np.int64))

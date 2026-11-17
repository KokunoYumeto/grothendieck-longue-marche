#!/usr/bin/env python3
"""Actual mod-four target with its mixed torsion, and the common source map."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
src=(HERE/'check_fivepoint_quartic_module.py').read_text()
exec(compile(src.split('R,piv=rref(C.matrix)',1)[0],str(HERE/'quartic_prefix.py'),'exec'),globals())

def reduce(A,p=4):
    A=np.asarray(A,dtype=np.int64).copy()%p
    row=0;piv=[]
    for col in range(A.shape[1]):
        if row==len(A):break
        nz=np.flatnonzero(A[row:,col]%2) if p==4 else np.flatnonzero(A[row:,col])
        if not len(nz):continue
        j=row+int(nz[0]);A[[row,j]]=A[[j,row]]
        A[row]=A[row]*pow(int(A[row,col]),-1,p)%p
        nz=np.flatnonzero(A[:,col]);nz=nz[nz!=row]
        A[nz]=(A[nz]-A[nz,col,None]*A[row])%p
        piv.append(col);row+=1
    return A,piv

def left_inverse(Q):
    _,rows=reduce(Q.T)
    assert len(rows)==Q.shape[1]
    n=len(rows);sq=Q[rows]
    aug,piv=reduce(np.hstack((sq,np.eye(n,dtype=np.int64))))
    assert piv[:n]==list(range(n))
    ans=np.zeros((n,len(Q)),dtype=np.int64)
    ans[:,rows]=aug[:n,n:]
    assert np.array_equal(ans@Q%4,np.eye(n,dtype=np.int64))
    return ans,rows

rel,piv=reduce(C.matrix)
r=len(piv);free=[i for i in range(769) if i not in piv]
assert r==667 and len(free)==102
P0=np.zeros((769,102),dtype=np.int64)
P0[free]=np.eye(102,dtype=np.int64)
P0[piv]=-rel[:r,free]%4
residual=rel[r:,free]
assert not np.any(residual%2)
br,bp=reduce(residual//2,2);t=len(bp)
assert not np.any(br[t:])
bf=[i for i in range(102) if i not in bp]
P1=np.zeros((102,102),dtype=np.int64)
for j,c in enumerate(bf):
    P1[c,j]=1
    P1[bp,j]=-br[:t,c]
for j,c in enumerate(bp):P1[c,len(bf)+j]=1
P=P0@P1%4
assert not np.any(C.matrix@P[:,:len(bf)]%4)
assert not np.any(C.matrix@P[:,len(bf):]%2)
assert np.array_equal((br[:t]@P1%2)[:,len(bf):],np.eye(t,dtype=np.int64))
assert not np.any((br[:t]@P1%2)[:,:len(bf)])
print('PASS exact target H1 over Z4: free rank',len(bf),'binary torsion rank',t,flush=True)

chunk=src.split('x12=',1)[1].split('T=np.hstack',1)[0]
exec(compile('x12='+chunk,str(HERE/'quartic_target_words.py'),'exec'),globals())
blocks=[];rawblocks=[]
for pair in pairs:
    raw=np.array([target_chain(subst(w,pair)) for w in loops],dtype=np.int64)
    val=raw@P%4
    val[:,len(bf):]%=2
    rawblocks.append(val.copy())
    val[:,len(bf):]*=2
    blocks.append(val)
T=np.hstack(blocks)%4

chunk='kgens='+src.split('kgens=',1)[1].split('modular_rank=',1)[0]
exec(compile(chunk,str(HERE/'quartic_modular_words.py'),'exec'),globals())
Q=modular
left,rows=left_inverse(Q)
target_from_common=left@T%4
defect=(T-Q@target_from_common)%4
np.savez_compressed(HERE/'quartic_mixed_precheck.npz',target_relation_matrix=C.matrix,
    target_projection=P,target_binary_residual=br[:t],target_binary_pivots=np.array(bp),
    eight_map=T,raw_eight_map=np.hstack(rawblocks),modular_restriction=modular,
    proposed_common_left_inverse=left,factorization_defect=defect)
assert not np.any(defect),('extra common image beyond modular rank97',np.count_nonzero(defect))
tr,tp=reduce(T)
assert len(tp)==97 and not np.any(tr[97:])
qt=T[:,tp];lt,_=left_inverse(qt)
common_from_target=np.zeros((816,97),dtype=np.int64)
common_from_target[tp]=lt@Q%4
assert np.array_equal(T@common_from_target%4,Q)
print('PASS both exact eight-map/modular rank97 factorization maps over Z4',flush=True)

qa={}
for name,a in homology_actions.items():
    qa[name]=left@a@Q%4
    assert np.array_equal(a@Q%4,Q@qa[name]%4)
divided_exponents=np.array([[sum((1 if z==j else -1 if z==-j else 0) for z in w)//6
                             for j in (1,2)] for w in loops],dtype=np.int64)%4
assert np.array_equal(Q@(left@divided_exponents%4)%4,divided_exponents)
binary=np.load(HERE.parent/'ghost_code/check_fivepoint_binary_module.npz')
change=left@binary['common_projection']%2
assert np.array_equal(Q@change%2,binary['common_projection']%2)
target_left,_=left_inverse(P)
target_binary_change=target_left@binary['target_h1_projection']%2
assert np.array_equal(P@target_binary_change%2,binary['target_h1_projection']%2)
for name in ('s','r'):
    assert np.array_equal(qa[name]@change%2,change@binary['quotient_'+name]%2)
print('PASS literal B actions, divided-exponent map, and reduction to the original binary common module',flush=True)

out={'coefficient_modulus':4,'base_order':288,'source_rank':289,
     'target_free_rank':len(bf),'target_binary_torsion_rank':t,
     'actual_common_module':'C4^97','common_rank':97,
     'source_kernel':'(Kprime K^4) intersect (Fprime F^24)',
     'all_assertions_passed':True,'Schreier_words':loops,
     'pairwords':pairs,'common_projection_basis':'the97 modular Schreier generators',
     'binary_coordinate_change':'row v in common4 maps to (v mod2)*binary_reduction_change'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),
    target_relation_matrix=C.matrix,target_h1_projection=P,target_free_rank=len(bf),
    target_binary_torsion_rank=t,target_binary_relation_rows=br[:t],
    target_unit_relation_reduction=rel,target_unit_pivots=np.array(piv),
    target_unit_free_columns=np.array(free),target_initial_projection=P0,
    target_mixed_basis_change=P1,target_binary_residual=residual,
    target_binary_pivots=np.array(bp),target_projection_left_inverse=target_left,
    target_binary_reduction_change=target_binary_change,
    eight_map=T,raw_eight_map=np.hstack(rawblocks),common_projection=Q,
    projection_left_inverse=left,target_from_common=target_from_common,
    common_from_target=common_from_target,
    source_s=homology_actions['s'],source_r=homology_actions['r'],
    quotient_s=qa['s'],quotient_r=qa['r'],base_s=base_actions['s'],base_r=base_actions['r'],
    source_table=jtable,source_generators=jgens,source_chords=np.array(chords),
    modular_restriction=modular,modular_factor=np.eye(97,dtype=np.int64),
    modular_table=ktable,modular_generators=kgi,modular_chords=np.array(kchords),
    divided_exponent_factor=left@divided_exponents%4,binary_reduction_change=change)
print('PASS actual mixed target and common source; complete coefficient maps saved.',flush=True)

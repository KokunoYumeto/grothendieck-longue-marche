#!/usr/bin/env python3
"""Six actual Cayley lifts and the exact four-dimensional outer discrepancy.

All matrix maps use the retained eighteen-to-six quotient and free basis.
Actual pure source realization is the perfect-image theorem A.4.23.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
paths={'homology':ROOT/'tower_code/translation_quaternion_homology.npz',
       'form':ROOT/'tower_code/translation_quaternion_image.npz',
       'quotient':HERE/'check_main_normalizer_joint.npz',
       'normalizer_record':HERE/'check_main_normalizer_joint.json'}
H=np.load(paths['homology'])['H18'].astype(np.int64)%3
F=np.load(paths['form'])['form'].astype(np.int64)%3
data=np.load(paths['quotient'])
phi=data['quotient_map'].astype(np.int64)%3
T=data['quotient_free_basis'].astype(np.int64)%3
geometric_kernel=data['first_order_kernel'].astype(np.int64)%3
normalizer_record=json.loads(paths['normalizer_record'].read_text())
H0=np.array(normalizer_record['reduced_binary_form'],dtype=np.int64)%3
assert np.array_equal(H0,2*np.eye(2,dtype=np.int64))
assert normalizer_record['period_order']==192
assert normalizer_record['exact_order']==384*3**6
assert (6*normalizer_record['exact_order']//18)//(6*normalizer_record['period_order'])==81
I=np.eye(18,dtype=np.int64);I6=np.eye(6,dtype=np.int64)


def rref(a):
    a=np.array(a,dtype=np.int64).copy()%3;r=0;p=[]
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        j=r+int(nz[0]);a[[r,j]]=a[[j,r]]
        a[r]=a[r]*pow(int(a[r,c]),-1,3)%3
        ix=np.flatnonzero(a[:,c]);ix=ix[ix!=r]
        a[ix]=(a[ix]-a[ix,c,None]*a[r])%3
        p.append(c);r+=1
        if r==len(a):break
    return a,p


def inv(a):
    n=len(a);out,p=rref(np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1))
    assert p[:n]==list(range(n));return out[:,n:]


def power(a,n):
    out=np.eye(len(a),dtype=np.int64)
    for _ in range(n):out=out@a%3
    return out


_,columns=rref(phi)
right=np.zeros((18,6),dtype=np.int64)
right[columns]=inv(phi[:,columns])
assert np.array_equal(phi@right%3,I6)
Ti=inv(T);Fi=inv(F)


def quotient(a):
    out=phi@a@right%3
    assert np.array_equal(out@phi%3,phi@a%3)
    return out


group=[power(H[0],i)@power(H[1],j)%3 for i,j in product(range(3),repeat=2)]
v=[right@T[:,i]%3 for i in range(2)]
Abasis=np.stack([g@w%3 for w in v for g in group],axis=1)
assert len(rref(Abasis)[1])==18
Abi=inv(Abasis)
X=(H[0]-I)%3;Y=(H[1]-I)%3
assert np.array_equal(Ti@quotient(H[0])@T%3,
                      np.block([[np.eye(2,dtype=np.int64),np.zeros((2,4),dtype=np.int64)],
                                [np.eye(2,dtype=np.int64),np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64)],
                                [np.zeros((2,4),dtype=np.int64),np.eye(2,dtype=np.int64)]]))
assert np.array_equal(Ti@quotient(H[1])@T%3,
                      np.block([[np.eye(2,dtype=np.int64),np.zeros((2,4),dtype=np.int64)],
                                [np.zeros((2,2),dtype=np.int64),np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64)],
                                [np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64),np.eye(2,dtype=np.int64)]]))

selfadjoint=[np.array([[1,0],[0,0]],dtype=np.int64),
             np.array([[0,0],[0,1]],dtype=np.int64),
             np.array([[0,1],[1,0]],dtype=np.int64)]
directions=[];lifts=[];quotients=[];cayley_records=[]
for slot in range(2):
    for coefficient in selfadjoint:
        assert np.array_equal(coefficient.T@H0%3,H0@coefficient%3)
        D=coefficient if slot==0 else np.zeros((2,2),dtype=np.int64)
        E=coefficient if slot==1 else np.zeros((2,2),dtype=np.int64)
        Dl=Abasis@np.kron(D,np.eye(9,dtype=np.int64))@Abi%3
        El=Abasis@np.kron(E,np.eye(9,dtype=np.int64))@Abi%3
        assert all(np.array_equal(Dl@h%3,h@Dl%3) and np.array_equal(El@h%3,h@El%3) for h in H)
        W=2*(X@Dl+Y@El)%3
        adjoint=Fi@W.T@F%3
        Z=2*(W-adjoint)%3
        assert np.array_equal(Fi@Z.T@F%3,-Z%3)
        assert not np.any(power(Z,5))
        g=(I+Z)@inv(I-Z)%3
        assert np.array_equal(g.T@F@g%3,F)
        assert all(np.array_equal(g@h%3,h@g%3) for h in H)
        assert np.array_equal(power(g,9),I)
        expected=I6.copy();expected[2:4,:2]=D;expected[4:6,:2]=E
        actual=Ti@quotient(g)@T%3
        assert np.array_equal(actual,expected)
        directions.append(np.concatenate([D.reshape(-1),E.reshape(-1)]))
        lifts.append(g);quotients.append(expected)
        cayley_records.append({'D':D.tolist(),'E':E.tolist(),'W':W.tolist(),'Z':Z.tolist(),
                               'g18':g.tolist(),'g6_adapted':actual.tolist(),
                               'order':next(n for n in (1,3,9) if np.array_equal(power(g,n),I))})
directions=np.array(directions,dtype=np.int64)
assert len(rref(directions)[1])==6
assert len(rref(np.concatenate([directions,geometric_kernel]))[1])==6
for a,b in product(quotients,repeat=2):
    assert not np.any((a-I6)@(b-I6)%3)

# Literal actual inner deck subgroup in the same basis.
inner_rows=[]
for h in H:
    adapted=Ti@quotient(h)@T%3
    assert np.array_equal(adapted[:2],I6[:2])
    assert np.array_equal(adapted[2:,2:],I6[2:,2:])
    inner_rows.append(adapted[2:,:2].reshape(-1))
inner_rows=np.array(inner_rows,dtype=np.int64)
assert len(rref(inner_rows)[1])==2
assert np.array_equal(inner_rows[0],np.array([1,0,0,1,0,0,0,0]))
assert np.array_equal(inner_rows[1],np.array([0,0,0,0,1,0,0,1]))

# Quotient coordinates are diagonal difference and the off-diagonal
# coefficient in each of the two self-adjoint blocks.
outer_projection=np.array([[1,-1,0,0,0,0],[0,0,1,0,0,0],
                           [0,0,0,1,-1,0],[0,0,0,0,0,1]],dtype=np.int64)%3
assert len(rref(outer_projection)[1])==4
inner_parameters=np.array([[1,1,0,0,0,0],[0,0,0,1,1,0]],dtype=np.int64)
assert not np.any(outer_projection@inner_parameters.T%3)
counts=Counter(tuple(outer_projection@np.array(c)%3) for c in product(range(3),repeat=6))
assert len(counts)==81 and set(counts.values())=={9}
all_matrices=set()
for parameters in product(range(3),repeat=6):
    c=np.array(parameters)@directions%3
    a=I6.copy();a[2:,:2]=c.reshape(4,2)
    all_matrices.add(a.tobytes())
assert len(all_matrices)==729
actual_inner=[Ti@quotient(h)@T%3 for h in group]
assert all(a.tobytes() in all_matrices for a in actual_inner)
assert all((-a%3).tobytes() not in all_matrices for a in actual_inner)

print('PASS six actual H-linear Cayley isometries, each of order3 or9 and hence inOmega',flush=True)
print('PASS exact eighteen-to-six maps and equality with all six retained geometric first-order directions',flush=True)
print('PASS inner translation rank2; negative inner coset disjoint from the constant-I subgroup',flush=True)
print('PASS729 first-order elements ->81 outer classes, exactly9 representatives each',flush=True)
print('PASS the complete ordinary signed-period kernel has order81 by the retained1152*81 image and1152 period quotient',flush=True)
record={'scope':__doc__,'input_sha256':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()},
        'reduced_form':H0.tolist(),'actual_A_free_basis':Abasis.tolist(),
        'directions':directions.tolist(),'cayley_lifts':cayley_records,
        'full_direction_rank':6,'inner_rows':inner_rows.tolist(),'inner_rank':2,
        'outer_projection':outer_projection.tolist(),'outer_rank':4,
        'first_order_order':729,'outer_image_order':81,'inner_fibre_order':9,
        'period_kernel_order':81,'all_assertions_passed':True}
(HERE/'check_cm_discrepancy_family.json').write_text(json.dumps(record,indent=2)+'\n')
np.savez_compressed(HERE/'check_cm_discrepancy_family.npz',A_basis=Abasis,
                    cayley_lifts=np.array(lifts),quotient_lifts=np.array(quotients),
                    directions=directions,inner_rows=inner_rows,outer_projection=outer_projection)

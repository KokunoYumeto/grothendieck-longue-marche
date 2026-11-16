#!/usr/bin/env python3
"""Exact invariant rational cosets controlling homogeneous eta torsion.

Work in the original CM basis, where global complex conjugation is
explicit.  The finite group is (A_Q3/A)^(G_K,Aut(E,D)), followed by c.
Its elements are necessary possible differences of integral classes
with fixed rational class and fixed automorphism/path identities.
No assertion is made that every formal difference is geometric.
"""
from collections import Counter
import json
import time
import numpy as np

started=time.monotonic()
PREC=10
MOD=3**PREC
I2=np.eye(2,dtype=np.int64)
I10=np.eye(10,dtype=np.int64)
I330=np.eye(330,dtype=np.int64)
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
R=np.array([[0,-1],[1,-1]],dtype=np.int64)
CE=np.array([[1,-1],[0,-1]],dtype=np.int64)
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
point_index={p:i for i,p in enumerate(coords)}
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
hall_index={h:i for i,h in enumerate(hall)}
assert len(hall)==330

def boundary_matrix(point_map):
    B=np.zeros((8,8),dtype=np.int64)
    for j,p in enumerate(coords):
        target=point_map(np.array(p,dtype=np.int64))%3
        target=tuple(int(x) for x in target)
        if target==(0,0):B[:,j]=-1
        else:B[point_index[target],j]=1
    return B

def full_matrix(compact,boundary):
    cross=U@compact-boundary@U
    assert not np.any(cross%3)
    return np.block([[compact,np.zeros((2,8),dtype=np.int64)],
                     [cross//3,boundary]])

geometry=[]
for d in [(1,0),(0,1)]:
    W=boundary_matrix(lambda p,d=np.array(d,dtype=np.int64):p+d)
    geometry.append(full_matrix(I2,W))
geometry.append(full_matrix(R,boundary_matrix(lambda p:R@p)))
geometry.append(full_matrix(-I2,boundary_matrix(lambda p:-p)))
geometry_names=['translation_P1','translation_P2','sigma','elliptic_involution']

# Check the full group over the integers before passing to a finite ring.
def key(M):return tuple(int(x) for x in M.flatten())
group={key(I10):I10}
queue=[I10]
while queue:
    M=queue.pop()
    for g in geometry:
        product=g@M
        k=key(product)
        if k not in group:
            group[k]=product;queue.append(product)
            assert len(group)<=54
assert len(group)==54
print('Four actual integral geometric generators form exactly54 automorphisms: PASS',flush=True)

T1=full_matrix(I2+3*R,7*np.eye(8,dtype=np.int64))
T2=full_matrix(I2+3*(R@R),7*np.eye(8,dtype=np.int64))
CV=full_matrix(CE,-boundary_matrix(lambda p:CE@p))
assert np.array_equal(CV@CV,I10)
assert np.array_equal(CV@T1@CV,T2)
assert np.array_equal(T1@T2,T2@T1)
for g in group.values():
    assert np.array_equal(g@T1,T1@g)
    assert np.array_equal(g@T2,T2@g)
    assert key(CV@g@CV) in group
compact_columns=np.vstack((3*I2,U))
for g in group.values():
    assert np.array_equal(g@compact_columns,compact_columns@g[:2,:2])
    assert int(g[0,0])*int(g[1,1])-int(g[0,1])*int(g[1,0])==1
print('Actual tau,tau_bar commute with all54; c swaps tau pair and normalizes geometry: PASS',flush=True)

def hall_bracket(a,b,c):
    if a==b:return ()
    sign=1
    if a<b:a,b,sign=b,a,-sign
    if c>=b:return ((hall_index[a,b,c],sign),)
    return ((hall_index[a,c,b],sign),(hall_index[b,c,a],-sign))

def lie3(M):
    M=M%MOD
    nz=[[(i,int(M[i,j])) for i in range(10) if M[i,j]] for j in range(10)]
    result=np.zeros((330,330),dtype=np.int64)
    for col,(i,j,k) in enumerate(hall):
        for a,x in nz[i]:
            for b,y in nz[j]:
                for c,z in nz[k]:
                    coefficient=x*y*z%MOD
                    for row,sgn in hall_bracket(a,b,c):
                        result[row,col]=(int(result[row,col])+sgn*coefficient)%MOD
    return result

arith=[pow(7,-1,MOD)*lie3(T1)%MOD,pow(7,-1,MOD)*lie3(T2)%MOD]
conjugation=(-lie3(CV))%MOD
geometric_actions=[lie3(g) for g in geometry]
assert np.array_equal(conjugation@conjugation%MOD,I330)
assert np.array_equal(conjugation@arith[0]%MOD@conjugation%MOD,arith[1])

def invariant_cosets(actions):
    """DVR Smith with column transport of stacked(g-I).

If U*stack*V = diag(3^e), rational invariant cosets have independent
generators V_j/3^e_j modulo the integral lattice.  Every generator is
verified directly against every original action.
"""
    original=np.vstack([(g-I330)%MOD for g in actions])
    A=original.copy()
    m,n=A.shape
    V=np.eye(n,dtype=np.int64)
    vals=[]
    for k in range(n):
        active=A[k:,k:]
        power=1
        for valuation in range(PREC):
            mask=(active//power)%3!=0
            if np.any(mask):break
            power*=3
        else:raise AssertionError('Full-column-rank pivot not visible')
        flat=int(np.argmax(mask))
        rr,cc=divmod(flat,active.shape[1]);rr+=k;cc+=k
        A[[k,rr]]=A[[rr,k]]
        A[:,[k,cc]]=A[:,[cc,k]];V[:,[k,cc]]=V[:,[cc,k]]
        assert not np.any(A[k:,k:]%power)
        unit=int(A[k,k])//power
        A[k,k:]=A[k,k:]*pow(unit,-1,MOD)%MOD
        assert A[k,k]==power
        quot=A[k+1:,k]//power
        A[k+1:,k:]=(A[k+1:,k:]-quot[:,None]*A[k,k:][None,:])%MOD
        assert not np.any(A[k+1:,k])
        factors=A[k,k+1:]//power
        assert not np.any(A[k,k+1:]%power)
        V[:,k+1:]=(V[:,k+1:]-V[:,k,None]*factors[None,:])%MOD
        A[k,k+1:]=0
        vals.append(valuation)
    assert np.array_equal(A[:n],np.diag([3**v for v in vals]))
    assert not np.any(A[n:])
    positive=[i for i,e in enumerate(vals) if e]
    for j in positive:
        assert not np.any(original@V[:,j]%(3**vals[j]))
    return vals,V,positive

stages=[
    ('arithmetic_Q',arith+[conjugation]),
    ('arithmetic_K_and_geometry',arith+geometric_actions),
    ('arithmetic_Q_and_geometry',arith+geometric_actions+[conjugation])]
records=[];stored={}
for name,actions in stages:
    print('Computing',name,'with',len(actions),'generators',flush=True)
    vals,columns,positive=invariant_cosets(actions)
    histogram=dict(sorted(Counter(vals).items()))
    torsion={int(k):int(v) for k,v in histogram.items() if k}
    record={'stage':name,'Smith_histogram':histogram,
            'positive_exponents':[vals[i] for i in positive],
            'log3_order':sum(vals),'exponent':3**max(vals),
            'number_of_cyclic_factors':len(positive)}
    records.append(record)
    stored[name+'_Smith_exponents']=np.array(vals,dtype=np.int64)
    stored[name+'_Smith_columns']=columns
    stored[name+'_positive_indices']=np.array(positive,dtype=np.int64)
    stored[name+'_coset_numerators']=columns[:,positive]
    stored[name+'_coset_denominators']=np.array([3**vals[i] for i in positive],dtype=np.int64)
    print(name,'Smith:',histogram,'; finite order3^',sum(vals),flush=True)
    if name=='arithmetic_Q':
        assert histogram=={0:237,1:59,2:27,3:7}
        print('Independent agreement with B21 full arithmetic torsion: PASS',flush=True)

result={
    'status':'invariant rational cosets computed with exact original CM basis',
    'modulus':MOD,'geometric_group_order':len(group),
    'geometric_generators':geometry_names,'stages':records,
    'scope':'Homogeneous cohomological torsion ambiguity with fixed rational class and fixed global automorphism/path identities. No geometric realization of every ambiguity is asserted.',
    'elapsed_seconds':time.monotonic()-started}
with open('deliverable/code/c_global_action_ambiguity.json','w') as output:
    json.dump(result,output,indent=2);output.write('\n')
np.savez_compressed('deliverable/code/c_global_action_ambiguity_matrices.npz',
    modulus=np.array([MOD]),U=U,CM=R,Tau_V=T1,Tau_bar_V=T2,Conjugation_V=CV,
    geometric_generators_V=np.stack(geometry),
    arithmetic_actions=np.stack(arith),conjugation_action=conjugation,
    geometric_actions=np.stack(geometric_actions),**stored)
print('Saved complete invariant-coset generators for every stage.',flush=True)
print('Elapsed seconds:',round(result['elapsed_seconds'],3),flush=True)

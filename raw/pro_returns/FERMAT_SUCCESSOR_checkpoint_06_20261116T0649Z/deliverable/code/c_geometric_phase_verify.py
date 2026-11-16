#!/usr/bin/env python3
"""Independent phase verification from chronological Schreier words.

Recompute the actual quadratic maps by reversing each fibre word;
average their genuine rank320 extension action; use a DIFFERENT strict
CM intertwiner; invert Frob4−1 by transported DVR elimination rather
than the other program's polynomial; and test all 27 candidates against
the exact integral invariant lattice found by our separate integer code.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import time
import numpy as np

start=time.monotonic()
PREC=10
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
hi={h:i for i,h in enumerate(hall)}
pairs=[(i,j) for i in range(10) for j in range(i)]
sch=json.loads(Path('deliverable/code/b_elliptic_schreier.json').read_text())
schm=np.load('deliverable/code/b_elliptic_schreier_matrices.npz')
quo=np.load('deliverable/code/c_char2_inner_quotient_matrices.npz')
invdata=np.load('deliverable/code/c_geometric_extension_test_matrices.npz')
sym=np.load('deliverable/code/b_char2_symmetry_matrices.npz')
P=schm['original_basis_in_Schreier']
Pinv=schm['Schreier_basis_in_original']
assert np.array_equal(Pinv@P,np.eye(10,dtype=np.int64))
projection=invdata['quotient_projection_exact']
inclusion=(quo['Lie_basis_change'][:,quo['kept_indices']]+MOD//2)%MOD-MOD//2
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
H=np.vstack((3*np.eye(2,dtype=np.int64),U))
u,v=H[:,0],H[:,1]

# Reuse only our exact integer Hall-bracket implementation, not the other
# phase program's arithmetic or intermediate matrices.
source=ast.parse(Path('deliverable/code/c_geometric_extension_test.py').read_text())
exec(compile(ast.Module(body=[f for f in source.body if isinstance(f,ast.FunctionDef)
       and f.name in {'triple','lie3_exact'}],type_ignores=[]),'own_Hall_functions','exec'))

def wedge(x,y):
    return np.array([int(x[i])*int(y[j])-int(x[j])*int(y[i]) for i,j in pairs],dtype=np.int64)

def log2(word):
    x=np.zeros(10,dtype=np.int64);b=np.zeros(45,dtype=np.int64)
    for letter in word:
        e=np.zeros(10,dtype=np.int64);e[abs(letter)-1]=1 if letter>0 else -1
        b+=wedge(x,e);x+=e
    return x,b

def L2(B):
    return np.array([[int(B[a,i])*int(B[b,j])-int(B[a,j])*int(B[b,i])
                     for i,j in pairs] for a,b in pairs],dtype=np.int64)

def cubic(b,x):
    out=np.zeros(330,dtype=np.int64)
    for n,(i,j) in enumerate(pairs):
        for k in range(10):
            coeff=int(b[n])*int(x[k])%MOD
            if coeff:
                for row,s in triple(i,j,k):out[row]=(out[row]+s*coeff)%MOD
    return out

gens=[]
for index,words in enumerate(sch['images_of_Schreier_generators']):
    formal=[log2(w) for w in words]
    actual=[log2(w[::-1]) for w in words]
    for (a,b),(c,d) in zip(formal,actual):
        assert np.array_equal(a,c) and np.array_equal(b,-d)
    C=Pinv@np.column_stack([a for a,b in actual])@P
    B=L2(Pinv)@np.column_stack([b for a,b in actual])%MOD@P%MOD*pow(2,-1,MOD)%MOD
    t=projection@(cubic(B@u%MOD,C@v)-cubic(B@v%MOD,C@u))%MOD
    Aq=projection@(lie3_exact(C)%MOD)%MOD@inclusion%MOD
    gens.append((C,Aq,t))
    assert np.array_equal(C,schm['translation_V'][index])
print('All forty actual fibre words reconstructed; linear part unchanged, quadratic part negated: PASS',flush=True)

I10=np.eye(10,dtype=np.int64)
ident=tuple(map(int,I10.flatten()))
group={ident:(I10,np.zeros(320,dtype=np.int64))}
queue=[ident]
while queue:
    old,old_t=group[queue.pop()]
    for C,A,t in gens:
        new=C@old;new_t=(t+A@old_t)%MOD
        key=tuple(map(int,new.flatten()))
        if key in group:
            assert np.array_equal(group[key][1],new_t)
        else:
            group[key]=(new,new_t);queue.append(key)
            assert len(group)<=54
assert len(group)==54
h27=-sum((t for g,t in group.values()),start=np.zeros(320,dtype=np.int64))*pow(2,-1,MOD)%MOD
for C,A,t in gens:
    assert not np.any(((A-np.eye(320,dtype=np.int64))@h27-27*t)%MOD)
print('All54 actual outer extension actions close; h27=-sum(t)/2 verified: PASS',flush=True)

# A different intertwiner from B's: first column (1,3), not (1,0).
q=sym['Q8_matrices']
S=-(np.eye(2,dtype=np.int64)+q[2,:2,:2]+q[4,:2,:2]+q[6,:2,:2])*pow(2,-1,MOD)%MOD
R=np.array([[0,-1],[1,-1]],dtype=np.int64)
first=np.array([1,3],dtype=np.int64)
B0=np.column_stack((first,S@first%MOD))
det=int(B0[0,0])*int(B0[1,1])-int(B0[0,1])*int(B0[1,0])
target=pow(det,-1,MOD)
root=1
for p in [3**i for i in range(1,PREC)]:
    candidates=[root+k*p for k in range(3) if ((root+k*p)**2-target)%(3*p)==0]
    assert len(candidates)==1
    root=candidates[0]
B=B0*root%MOD
assert np.array_equal(B%3,np.eye(2,dtype=np.int64))
assert (int(B[0,0])*int(B[1,1])-int(B[0,1])*int(B[1,0]))%MOD==1
assert not np.any((S@B-B@R)%MOD)
cross=U@B-U
assert not np.any(cross%3)
K=np.block([[B,np.zeros((2,8),dtype=np.int64)],[cross//3,np.eye(8,dtype=np.int64)]])%MOD
# The exact Hall evaluator needs small integer lifts to avoid overflow.
Ksmall=(K+MOD//2)%MOD-MOD//2
Kq=projection@(lie3_exact(Ksmall)%MOD)%MOD@inclusion%MOD
h27local=Kq@h27%MOD
invariants=Kq@invdata['invariant_basis_exact']%MOD

# Independent inverse by a full DVR Smith calculation, transporting the
# 27 right-hand sides and column changes. No inverse polynomial is used.
D=(quo['quotient_Frob4']-np.eye(320,dtype=np.int64))%MOD
original_rhs=81*quo['local_candidates']%MOD
A=D.copy();rhs=original_rhs.copy();columns=np.eye(320,dtype=np.int64);vals=[]
for k in range(320):
    active=A[k:,k:]
    p=1
    for val in range(PREC):
        nz=np.argwhere((active//p)%3)
        if len(nz):break
        p*=3
    else:raise AssertionError('Missing nonzero Frobenius pivot')
    i,j=map(int,nz[0]);i+=k;j+=k
    A[[k,i]]=A[[i,k]];rhs[[k,i]]=rhs[[i,k]]
    A[:,[k,j]]=A[:,[j,k]];columns[:,[k,j]]=columns[:,[j,k]]
    factor=pow(int(A[k,k])//p,-1,MOD)
    A[k]=A[k]*factor%MOD;rhs[k]=rhs[k]*factor%MOD
    q=A[:,k]//p;q[k]=0
    assert not np.any(A[:,k]%p)
    A=(A-q[:,None]*A[k][None,:])%MOD
    rhs=(rhs-q[:,None]*rhs[k][None,:])%MOD
    q=A[k,k+1:]//p
    assert not np.any(A[k,k+1:]%p)
    columns[:,k+1:]=(columns[:,k+1:]-columns[:,k,None]*q[None,:])%MOD
    A[k,k+1:]=0
    vals.append(val)
assert max(vals)==4
assert np.array_equal(A,np.diag([3**v for v in vals]))
coordinates=np.empty_like(rhs)
for i,val in enumerate(vals):
    p=3**val
    assert not np.any(rhs[i]%p)
    coordinates[i]=rhs[i]//p
q81=columns@coordinates%MOD
assert not np.any((D@q81-original_rhs)%MOD)
print('Frobenius inverse independently solved by DVR elimination; Smith',dict(Counter(vals)),flush=True)

def inverse_unit(A):
    n=len(A);X=np.column_stack((A%81,np.eye(n,dtype=np.int64)))
    for j in range(n):
        i=next(i for i in range(j,n) if X[i,j]%3)
        X[[i,j]]=X[[j,i]]
        X[j]=X[j]*pow(int(X[j,j]),-1,81)%81
        for i in range(n):
            if i!=j:X[i]=(X[i]-X[i,j]*X[j])%81
    assert np.array_equal(X[:,:n],np.eye(n,dtype=np.int64))
    return X[:,n:]

# Find a unit minor independently in the transported exact invariant basis.
rows=[]
rank=0
echelon=invariants.T.copy()%3
for col in range(320):
    nz=np.flatnonzero(echelon[rank:,col])
    if not len(nz):continue
    i=rank+int(nz[0]);echelon[[rank,i]]=echelon[[i,rank]]
    echelon[rank]=echelon[rank]*int(echelon[rank,col])%3
    for i in range(4):
        if i!=rank:echelon[i]=(echelon[i]-echelon[i,col]*echelon[rank])%3
    rows.append(col);rank+=1
    if rank==4:break
assert rank==4
inv=inverse_unit(invariants[rows,:])
diff=(q81-3*h27local[:,None])%81
coeff=inv@diff[rows,:]%81
errors=(diff-invariants@coeff)%81
survivors=np.flatnonzero(~np.any(errors,axis=0))
assert survivors.tolist()==[5]
candidate=quo['candidate_Q2_coordinates'][5]
assert candidate.tolist()==[0,0,1,2,0,2,5,9,6,9,24,57,36]
print('Independent exact phase selection:',survivors.tolist(),'of27',flush=True)
print('Actual local Smith coordinates:',candidate.tolist(),flush=True)
print('lambda81 eta(Frob2)=57; lambdaJ eta(Frob2)=19 modulo27',flush=True)

result={'status':'independent reversed-word, different-intertwiner, DVR-inverse verification passed',
        'surviving_candidate_indices':survivors.tolist(),
        'actual_local_Q2_coordinates':candidate.tolist(),
        'lambda81_value':57,'lambdaJ_value_mod27':19,
        'intertwiner_first_column_seed':[1,3],
        'compact_intertwiner_modulus':B.tolist(),
        'Frobenius_inverse_Smith_histogram':dict(Counter(vals)),
        'elapsed_seconds':time.monotonic()-start}
Path('deliverable/code/c_geometric_phase_verify.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/c_geometric_phase_verify_matrices.npz',
                    actual_geometric_displacements=np.stack([t for C,A,t in gens]),
                    actual_geometric_coset_times27=h27,
                    different_intertwiner_compact=B,different_intertwiner_Q=Kq,
                    local_geometric_coset_times27=h27local,
                    local_invariant_basis=invariants,candidate_rational_cosets_times81=q81,
                    candidate_compatibility_errors=errors,survivor_indices=survivors)
print('Elapsed seconds:',round(time.monotonic()-start,3),flush=True)

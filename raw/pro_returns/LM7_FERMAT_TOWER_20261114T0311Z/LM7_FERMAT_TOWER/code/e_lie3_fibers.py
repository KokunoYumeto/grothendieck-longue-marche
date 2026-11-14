#!/usr/bin/env python3
"""E.40: exact degree-three intrinsic lifting fibers over Q.

Hall coordinates [[x_i,x_j],x_k], i>j and k>=j, form the
integral degree-three free Lie lattice.  Modular Smith operations
retain both invertible transformations.  The proof gives the
independent torsion exponent bound 3^5, so modulus 3^6 suffices.
"""
from pathlib import Path
import json
import numpy as np

DIM = 10
MOD = 3**6
cusps = [(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U = np.array([(v,-u) for u,v in cusps],dtype=np.int64)
R = np.array([[0,-1],[1,-1]],dtype=np.int64)
CE = np.array([[1,-1],[0,-1]],dtype=np.int64)
CT = np.zeros((8,8),dtype=np.int64)
for j,i in enumerate([0,2,1,3,5,4,7,6]):
    CT[i,j] = -1

def vmat(E,T):
    lower = U@E-T@U
    assert np.all(lower%3==0)
    A = np.zeros((DIM,DIM),dtype=np.int64)
    A[:2,:2]=E
    A[2:,:2]=lower//3
    A[2:,2:]=T
    return A

At = vmat(np.eye(2,dtype=np.int64)+3*R,7*np.eye(8,dtype=np.int64))
Ac = vmat(CE,CT)
A2 = vmat(-2*np.eye(2,dtype=np.int64),4*np.eye(8,dtype=np.int64))
assert np.array_equal(Ac@Ac,np.eye(DIM,dtype=np.int64))

basis = [(i,j,k) for i in range(DIM) for j in range(i)
         for k in range(j,DIM)]
index = {t:i for i,t in enumerate(basis)}
assert len(basis)==330

def reduce_triple(i,j,k):
    if i==j:
        return []
    sign = 1
    if i<j:
        i,j=j,i
        sign=-1
    if k>=j:
        return [(index[i,j,k],sign)]
    # Jacobi: [[i,j],k]=[[i,k],j]-[[j,k],i].
    return [(index[i,k,j],sign),(index[j,k,i],-sign)]

def lie3(A):
    ans = np.zeros((330,330),dtype=np.int64)
    nz = [[(r,int(A[r,c])) for r in range(DIM) if A[r,c]]
          for c in range(DIM)]
    for col,(i,j,k) in enumerate(basis):
        for a,aa in nz[i]:
            for b,bb in nz[j]:
                for c,cc in nz[k]:
                    for row,sgn in reduce_triple(a,b,c):
                        ans[row,col]+=aa*bb*cc*sgn
    return ans

Lt,Lc,L2 = [lie3(A) for A in (At,Ac,A2)]
eye = np.eye(330,dtype=np.int64)
assert np.array_equal(Lc@Lc,eye)
assert np.array_equal(lie3(Ac@At@Ac),Lc@Lt@Lc)
assert np.trace(Lc)==-2
assert np.array_equal(lie3(np.eye(DIM,dtype=np.int64)),eye)
P = (Lt-eye)@(eye+Lc)

def smith_mod(matrix,modulus):
    A=matrix.copy()%modulus
    m,n=A.shape
    left=np.eye(m,dtype=np.int64)
    right=np.eye(n,dtype=np.int64)
    vals=[]
    operations=[]
    for k in range(min(m,n)):
        sub=A[k:,k:]
        nz=np.argwhere(sub)
        if len(nz)==0:
            break
        best=None
        for v in range(6):
            p=3**v
            candidates=np.argwhere((sub%p==0)&(sub%(3*p)!=0))
            if len(candidates):
                best=candidates[0]+k
                break
        assert best is not None
        i,j=map(int,best)
        if i!=k:
            A[[i,k]]=A[[k,i]]
            left[[i,k]]=left[[k,i]]
        if j!=k:
            A[:,[j,k]]=A[:,[k,j]]
            right[:,[j,k]]=right[:,[k,j]]
        p=3**v
        unit=int(A[k,k])//p
        inv=pow(unit,-1,modulus)
        A[k]=(A[k]*inv)%modulus
        left[k]=(left[k]*inv)%modulus
        assert int(A[k,k])==p
        factors=A[:,k]//p
        factors[k]=0
        assert np.all(A[:,k]%p==0)
        A=(A-factors[:,None]*A[k][None,:])%modulus
        left=(left-factors[:,None]*left[k][None,:])%modulus
        factors2=A[k,:]//p
        factors2[k]=0
        assert np.all(A[k,:]%p==0)
        A=(A-A[:,k][:,None]*factors2[None,:])%modulus
        right=(right-right[:,k][:,None]*factors2[None,:])%modulus
        vals.append(v)
        operations.append({'pivot':k,'row_swap':i,'column_swap':j,
                           'row_scale':inv,'valuation':v,
                           'row_elimination':factors.tolist(),
                           'column_elimination':factors2.tolist()})
    # Matrix products stay below 330*728^2 before each reduction.
    assert np.array_equal(((left@(matrix%modulus))%modulus@right)%modulus,A)
    diagonal=np.zeros_like(A)
    for k,v in enumerate(vals):
        diagonal[k,k]=3**v
    assert np.array_equal(A,diagonal)
    assert all(op['row_scale']%3 for op in operations)
    return vals,left,right,operations

print('Constructed exact330-dimensional Hall action matrices.',flush=True)
vals,left,right,ops=smith_mod(P,MOD)
assert len(vals)==164
assert all(v<=5 for v in vals)
counts={str(v):vals.count(v) for v in sorted(set(vals))}
print('Smith valuations:',counts,'free rank',330-len(vals),flush=True)

# Independent invariant calculation: stack the two arithmetic generators
# and conjugation.  Frobenius at2 gives the proved exponent bound3^5.
# It is enough to include At,Ac since tau and c*tau*c generate P_S.
stack=np.vstack([Lt-eye,Lc-eye])
ivals,il,ir,iops=smith_mod(stack,MOD)
assert len(ivals)==330
assert sorted(v for v in ivals if v)>[]
assert sorted(v for v in vals if v)==sorted(v for v in ivals if v)
print('Independent simultaneous-invariant Smith torsion agrees.',flush=True)

# Verify the denominator bound directly by an integer matrix identity.
# B maps the split sublattice T_D + j(T3E) into V.  Its index is9
# and 3V is contained in it.  The degree-three matrix satisfies
# B3*C3=27I, while Frobenius2 is scalar on each letter-count block.
B=np.zeros((10,10),dtype=np.int64)
B[:2,:2]=3*np.eye(2,dtype=np.int64)
B[2:,:2]=U
B[2:,2:]=np.eye(8,dtype=np.int64)
C=np.zeros((10,10),dtype=np.int64)
C[:2,:2]=np.eye(2,dtype=np.int64)
C[2:,:2]=-U
C[2:,2:]=3*np.eye(8,dtype=np.int64)
assert np.array_equal(B@C,3*np.eye(10,dtype=np.int64))
B3,C3=lie3(B),lie3(C)
assert np.array_equal(B3@C3,27*eye)
split=np.diag([-2,-2]+[4]*8).astype(np.int64)
D3=lie3(split)
assert np.array_equal(L2@B3,B3@D3)
eigen=[int(D3[k,k]) for k in range(330)]
assert set(eigen)=={64,-32,16,-8}
# 9/(eigen-1) has 3-integral denominator; save its rational coordinates.
from fractions import Fraction
denom_cert=[str(Fraction(9,v-1)) for v in sorted(set(eigen))]
assert all(Fraction(9,v-1).denominator%3 for v in eigen)
print('Verified exact split-lattice identity proving torsion exponent divides3^5.',flush=True)

result={'rank':330,'conjugation_trace':-2,'plus_rank':164,'minus_rank':166,
        'Hall_basis':basis,'input_V_tau':At.tolist(),'input_V_c':Ac.tolist(),
        'Lie_tau':Lt.tolist(),'Lie_c':Lc.tolist(),
        'cohomology_matrix':P.tolist(),'modulus':MOD,
        'torsion_bound_3_exponent':5,'Smith_valuation_counts':counts,
        'free_rank':166,'left_transform_mod729':left.tolist(),
        'right_transform_mod729':right.tolist(),
        'elementary_operations':ops,
        'independent_invariant_valuation_counts':{str(v):ivals.count(v) for v in sorted(set(ivals))},
        'split_Frobenius2_eigenvalues':sorted(set(eigen)),
        'nine_over_eigenvalue_minus_one':denom_cert,
        'status':'PASS'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print('PASS: saved transformations, all modular identities, torsion bound and independent check.',flush=True)

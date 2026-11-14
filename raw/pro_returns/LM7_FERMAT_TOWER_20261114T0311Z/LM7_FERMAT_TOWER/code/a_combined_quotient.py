#!/usr/bin/env python3
"""Exact integral fiber-product comparison for E.53.

The Hall graded calculation uses the actual cusp-image lattice
3 Z_3 x + Z_3 y.  It records integer quotient maps and integer
right inverses, including the relative factors three.
"""
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import json
import numpy as np
import sympy as sp
import a_class3_frobenius as mag

D=10
T=set(range(2,D))
B2=[(i,j) for i in range(D) for j in range(i)]
B3=[(i,j,k) for i in range(D) for j in range(i) for k in range(j,D)]
I3={t:i for i,t in enumerate(B3)}
H=[(1,0),(0,0),(3,0),(0,1)]+[(0,0)]*6
assert len(B2)==45 and len(B3)==330 and len(H)==D

# Positive peripheral classes ordered A0,A1,A2,B0,B1,B2,C1,C2.
# Their actual h,1-h valuations give the cusp matrix.  This
# unimodular basis change isolates 3x,y and six zero images.
cusp=np.array([[0,0,0,0,0,0,0,-3],
               [0,0,0,1,1,1,0,-3]],dtype=np.int64)
TB=np.zeros((8,8),dtype=np.int64)
TB[7,0]=-1;TB[3,0]=-3;TB[3,1]=1
for j,i in enumerate([0,1,2],start=2):TB[i,j]=1
TB[4,5]=1;TB[3,5]=-1
TB[5,6]=1;TB[3,6]=-1
TB[6,7]=1
assert abs(int(sp.Matrix(TB).det()))==1
assert np.array_equal(cusp@TB,np.array([[3,0,0,0,0,0,0,0],
                                      [0,1,0,0,0,0,0,0]],dtype=np.int64))

def det(a,b):return a[0]*b[1]-a[1]*b[0]
M2=np.array([[det(H[i],H[j]) for i,j in B2]],dtype=np.int64)
M3=np.array([[-det(H[i],H[j])*H[k][v] for i,j,k in B3]
             for v in range(2)],dtype=np.int64)
K2=[i for i,t in enumerate(B2) if all(x in T for x in t)]
R2=[i for i in range(45) if i not in K2]
R3=[r for r,(i,j,k) in enumerate(B3)
    if (i<2 and j<2 and k<2) or (i in T and j<2 and k<2)]
K3=[i for i in range(330) if i not in R3]
assert (len(K2),len(R2),len(K3),len(R3))==(28,17,304,26)

# The degree-two image is exactly 3c, with an actual unit preimage
# when coordinates on that image are taken relative to 3c.
assert np.all(M2[:,K2]%3==0)
W2=M2[:,K2]//3
p2=K2.index(B2.index((3,2)))
assert W2[0,p2]==-1 and np.count_nonzero(W2)==1
S2=np.zeros((28,1),dtype=np.int64);S2[p2,0]=-1

# The degree-three image is exactly 3d,e.  The two specified
# Hall rows give the literal integer right inverse.
assert np.all(M3[0,K3]%3==0)
W3=M3[:,K3].copy();W3[0,:]//=3
p3=[K3.index(B3.index((3,0,2))),K3.index(B3.index((3,0,3)))]
assert np.array_equal(W3[:,p3],np.eye(2,dtype=np.int64))
S3=np.zeros((304,2),dtype=np.int64)
for j,p in enumerate(p3):S3[p,j]=1

def kernel_certificate(W,S,pivots):
    rows,cols=W.shape
    assert np.array_equal(W@S,np.eye(rows,dtype=np.int64))
    free=[i for i in range(cols) if i not in pivots]
    E=np.eye(cols,dtype=np.int64)[:,free]
    K=E-S@W[:,free]
    C=np.concatenate([S,K],axis=1)
    inv=np.concatenate([W,np.eye(cols,dtype=np.int64)[free,:]],axis=0)
    assert np.array_equal(W@K,np.zeros((rows,len(free)),dtype=np.int64))
    assert np.array_equal(inv@C,np.eye(cols,dtype=np.int64))
    assert np.array_equal(C@inv,np.eye(cols,dtype=np.int64))
    return K,C,inv,free

J2,C2,CI2,F2=kernel_certificate(W2,S2,[p2])
J3,C3,CI3,F3=kernel_certificate(W3,S3,p3)
assert J2.shape==(28,27) and J3.shape==(304,302)

def quotient_certificate(n,retained,discarded,W,S,J):
    r=len(retained);s=W.shape[0]
    q=np.zeros((r+s,n),dtype=np.int64)
    q[:r,retained]=np.eye(r,dtype=np.int64)
    q[r:,discarded]=W
    split=np.zeros((n,r+s),dtype=np.int64)
    split[retained,:r]=np.eye(r,dtype=np.int64)
    split[discarded,r:]=S
    kernel=np.zeros((n,J.shape[1]),dtype=np.int64)
    kernel[discarded,:]=J
    assert np.array_equal(q@split,np.eye(r+s,dtype=np.int64))
    assert not np.any(q@kernel)
    assert np.array_equal(q@np.eye(n,dtype=np.int64),q)
    return q,split,kernel

Q2,QS2,JK2=quotient_certificate(45,R2,K2,W2,S2,J2)
Q3,QS3,JK3=quotient_certificate(330,R3,K3,W3,S3,J3)
assert Q2.shape==(18,45) and Q3.shape==(28,330)
assert not np.any(M2@JK2) and not np.any(M3@JK3)

def triple(i,j,k):
    if i==j:return {}
    sign=1
    if i<j:i,j,sign=j,i,-1
    if k>=j:return {I3[i,j,k]:sign}
    return {I3[i,k,j]:sign,I3[j,k,i]:-sign}

# Bracketing every degree-two joint-kernel generator with every
# degree-one generator stays in the precise degree-three joint kernel.
normality=0
for col in range(JK2.shape[1]):
    for k in range(D):
        out=np.zeros(330,dtype=np.int64)
        for row in np.flatnonzero(JK2[:,col]):
            i,j=B2[int(row)]
            for r,a in triple(i,j,k).items():out[r]+=int(JK2[row,col])*a
        assert not np.any(Q3@out)
        normality+=1
assert normality==270

# Independent target tensor substitution verifies the graded maps
# on all forty-five and three-hundred-thirty Hall basis vectors.
def bracket(a,b):
    out=defaultdict(int)
    for u,x in a.items():
        for v,y in b.items():
            out[u+v]+=x*y;out[v+u]-=x*y
    return {u:x for u,x in out.items() if x}
X={(0,):1};Y={(1,):1}
C=bracket(X,Y);DD=bracket(X,C);EE=bracket(Y,C)
def linear_h(i):return {(j,):v for j,v in enumerate(H[i]) if v}
def lincomb(vs,coeffs):
    out=defaultdict(int)
    for v,c in zip(vs,coeffs):
        for w,x in v.items():out[w]+=int(c)*x
    return {w:x for w,x in out.items() if x}
tensor_checks=0
for r,(i,j) in enumerate(B2):
    assert bracket(linear_h(i),linear_h(j))==lincomb([C],M2[:,r])
    tensor_checks+=1
for r,(i,j,k) in enumerate(B3):
    assert bracket(bracket(linear_h(i),linear_h(j)),linear_h(k))==lincomb([DD,EE],M3[:,r])
    tensor_checks+=1

# Actual class-three group identities, independent of the graded maps.
x,y,c,d,e=mag.x,mag.y,mag.c,mag.d,mag.e
assert mag.comm(mag.power(x,3),y)==mag.prod(mag.power(c,3),mag.power(d,3))
assert mag.comm(mag.power(x,3),c)==mag.power(d,3)
assert mag.comm(y,c)==e
assert mag.comm(x,mag.power(c,3))==mag.power(d,3)
assert mag.comm(y,mag.power(c,3))==mag.power(e,3)
for z in [mag.power(c,3),mag.power(d,3),e]:
    for w in [mag.power(c,3),mag.power(d,3),e]:
        assert mag.comm(z,w)==mag.one

def multiply(g,h):
    a,b,n,r,s=g;A,B,N,R,S=h
    return (a+A,b+B,n+N-A*b,r+R+b*A*(A+1)/2-A*n,
            s+S+A*b*(b+1)/2-B*n+A*b*B)
def residue3(x):
    x=Q(x);assert x.denominator%3
    return int(x.numerator*pow(x.denominator,-1,3)%3)
def quotient(g):
    return [str(g[0]),str(g[1]),residue3(g[2]),residue3(g[3])]
def hall_action(lam,k):
    return [
      (lam,0,0,0,0),
      (0,lam,k*lam,lam*k*(k-1)/2,lam*mag.c2(lam)-k*lam*(lam+1)/2),
      (0,0,lam**2,lam**2*(lam-1)/2+k*lam**2,lam**2*(lam-1)/2),
      (0,0,0,lam**3,0),
      (0,0,0,0,lam**3)]
common_action_checks=0
for lam in [Q(-5),Q(-2),Q(1),Q(4),Q(7),Q(10),Q(1,4),Q(4,7)]:
    assert residue3(lam)==1
    r=(lam-1)/3
    ref=[quotient(g) for g in hall_action(lam,r)]
    for shift in range(-4,5):
        assert [quotient(g) for g in hall_action(lam,r+3*shift)]==ref
        common_action_checks+=1
assert [quotient(g) for g in hall_action(Q(4),Q(1))]==[
    ['4','0',0,0],['0','4',1,0],['0','0',1,1],
    ['0','0',0,1],['0','0',0,0]]

def sparse_cols(M):
    return [[[int(i),int(M[i,j])] for i in np.flatnonzero(M[:,j])]
             for j in range(M.shape[1])]

result={'statement':'E.53','status':'PASS',
 'homology_map_basis_images':H,
 'actual_cusp_valuation_matrix':cusp.tolist(),
 'unimodular_cusp_basis_change':TB.tolist(),
 'intrinsic_graded_ranks':[10,45,330],
 'old_kernel_graded_ranks':[0,28,304],
 'joint_kernel_graded_ranks':[0,27,302],
 'combined_quotient_graded_ranks':[10,18,28],
 'joint_abelian_kernel_rank':329,'combined_hirsch_rank':56,
 'old_kernel_image_in_C':'<c^3,d^3,e> = Z_3^3',
 'old_kernel_degree3_image':'<d^3,e>',
 'common_quotient_Hall_coordinates':'Z_3^2 times (Z/3)^2; e=1,c^3=d^3=1',
 'actual_commutator_identities':['[x^3,y]=c^3 d^3','[x^3,c]=d^3','[y,c]=e'],
 'degree_two_relative_map':W2.tolist(),
 'degree_three_relative_map':W3.tolist(),
 'degree_two_kernel_basis_sparse':sparse_cols(JK2),
 'degree_three_kernel_basis_sparse':sparse_cols(JK3),
 'degree_two_quotient_right_inverse_sparse':sparse_cols(QS2),
 'degree_three_quotient_right_inverse_sparse':sparse_cols(QS3),
 'integral_inverse_identities':True,
 'maximum_kernel_certificate_entry':max(int(np.max(np.abs(JK2))),int(np.max(np.abs(JK3)))),
 'graded_tensor_checks':tensor_checks,'joint_kernel_normality_checks':normality,
 'common_action_checks':common_action_checks,
 'common_Frobenius4_images':['x^4','y^4 c','c d','d']}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS actual image identities: [x^3,y]=c^3 d^3, [x^3,c]=d^3, [y,c]=e.')
print('PASS exact common quotient C/<c^3,d^3,e> and normality.')
print('PASS integral joint-kernel ranks [0,27,302], total329.')
print('PASS integral combined-quotient ranks [10,18,28], total56.')
print('PASS',tensor_checks,'tensor maps,',normality,'normality checks,',
      common_action_checks,'common-action checks.')
print('PASS integer quotient maps and right inverses saved.')

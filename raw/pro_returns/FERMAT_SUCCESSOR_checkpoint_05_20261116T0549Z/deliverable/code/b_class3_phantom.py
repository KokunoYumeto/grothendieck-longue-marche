"""Independent exact certificate for the matrix and detector in LM6 E.38.

Build the degree-three free Lie action in the integral Hall basis, then
compute its 3-adic Smith valuations by unimodular operations modulo 3^12.
Every pivot is below the precision, and the independent eigenvalue norm
calculation verifies the determinant valuation.  No inherited matrix
or previous output is loaded.
"""
from collections import Counter
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form

N=12
MOD=3**N
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
index={t:n for n,t in enumerate(hall)}
assert len(hall)==330

def bracket(a,b,c):
    """Expansion of [[e_a,e_b],e_c] in the integral Hall basis."""
    if a==b:return []
    sign=1
    if a<b:a,b,sign=b,a,-1
    if c>=b:return [(index[a,b,c],sign)]
    # Jacobi: [[a,b],c] = [[a,c],b] - [[b,c],a].
    return [(index[a,c,b],sign),(index[b,c,a],-sign)]

def lie3(A):
    A=np.array(A,dtype=np.int64)%MOD
    nz=[[(i,int(A[i,j])) for i in range(10) if A[i,j]] for j in range(10)]
    B=np.zeros((330,330),dtype=np.int64)
    for col,(i,j,k) in enumerate(hall):
        for a,x in nz[i]:
            for b,y in nz[j]:
                for c,z in nz[k]:
                    v=(x*y*z)%MOD
                    for row,t in bracket(a,b,c):
                        B[row,col]=(int(B[row,col])+t*v)%MOD
    return B

U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
R=s.Matrix([[0,-1],[1,-1]])
AE=s.eye(2)+3*R
T=AE.row_join(s.zeros(2,8)).col_join((U*(AE-7*s.eye(2))/3).row_join(7*s.eye(8)))
CE=s.Matrix([[1,-1],[0,-1]])
CT=s.zeros(8)
for j,i in enumerate([0,2,1,3,5,4,7,6]):CT[i,j]=-1
C=CE.row_join(s.zeros(2,8)).col_join(((U*CE-CT*U)/3).row_join(CT))
assert all(x.q==1 for x in T) and all(x.q==1 for x in C)
assert C*C==s.eye(10)
LT=lie3(T)
LC=lie3(C)
L3=lie3(T**3)
assert np.array_equal(L3,((LT@LT)%MOD@LT)%MOD)
D=(pow(7,-3,MOD)*L3-np.eye(330,dtype=np.int64))%MOD
assert not np.any(D%3)

ell=[0,2,0,0,0,3,0,0,0,0]
def det(a,b):
    return (1 if (a,b)==(0,1) else -1 if (a,b)==(1,0) else 0)
def phi(i,j,k):
    return ell[i]*det(j,k)-ell[j]*det(i,k)-ell[k]*det(i,j)+ell[k]*det(j,i)
phirow=np.array([phi(*t) for t in hall],dtype=np.int64)
assert not np.any(phirow%3)
psi=phirow//3
assert {t:int(psi[i]) for i,t in enumerate(hall) if psi[i]}=={(1,0,1):2,(1,0,5):2,(5,0,1):1}
assert not np.any((psi@LT-49*psi)%MOD)
assert not np.any((psi@LC-psi)%MOD)
print('Integral detector Phi/3: nonzero Hall coordinates',[(t,int(psi[i])) for i,t in enumerate(hall) if psi[i]])
print('Equivariance Psi Lie3(T7)=49 Psi and Psi Lie3(c)=Psi: PASS')

def smith3(A,rank=None):
    A=A.copy()
    valuations=[]
    rank=len(A) if rank is None else rank
    for k in range(rank):
        active=A[k:,k:]
        power=1
        for v in range(N):
            pos=np.argwhere((active//power)%3)
            if pos.size:break
            power*=3
        else:raise AssertionError('pivot lost at precision '+str(N))
        r,c=map(int,pos[0]);r+=k;c+=k
        if r!=k:A[[k,r],:]=A[[r,k],:]
        if c!=k:A[:,[k,c]]=A[:,[c,k]]
        # The selected pivot has the least 3-adic valuation in this block.
        assert not np.any(A[k:,k:]%power)
        unit=int(A[k,k])//power
        A[k,k:]=(A[k,k:]*pow(unit,-1,MOD))%MOD
        assert A[k,k]==power
        multipliers=A[k+1:,k]//power
        A[k+1:,k:]=(A[k+1:,k:]-multipliers[:,None]*A[k,k:][None,:])%MOD
        assert not np.any(A[k+1:,k])
        valuations.append(v)
    if rank<len(A):assert not np.any(A[rank:,rank:])
    return valuations

vals=smith3(D)
hist=dict(sorted(Counter(vals).items()))
print('3-adic Smith valuation multiplicities at precision 3^12:',hist)
assert hist=={1:132,2:82,3:52,4:49,5:14,6:1}
assert sum(vals)==724

# Exact arithmetic in Z[zeta], zeta^2+zeta+1=0.
def mul(a,b):
    x,y=a;u,v=b
    return x*u-y*v,x*v+y*u-y*v
def power(a,n):
    ans=(1,0)
    for _ in range(n):ans=mul(ans,a)
    return ans
def norm(a):x,y=a;return x*x-x*y+y*y
def sub1(a):return a[0]-1,a[1]
def v3(x):
    assert x
    x=abs(x);v=0
    while x%3==0:x//=3;v+=1
    return v
pi=(1,3)
contributions=[v3(norm(sub1(power(pi,3)))),
               8*v3(norm(sub1(power(pi,6)))),
               16*v3(7**3-1),
               64*v3(norm(sub1(power((7,21),3)))),
               168*v3(7**6-1)]
print('Independent exact eigenvalue determinant contributions:',contributions)
print('Determinant valuation:',sum(contributions))
assert contributions==[4,32,32,320,336]
assert sum(contributions)==sum(vals)==724
print('All 330 pivots below precision; exact integral inverse bound 3^6 D^-1: PASS')
print('Uniform consequence: 3^(n+6) (R^(3^(n+1))-1)^-1 integral for every n>=0.')

# The ambient action-class cohomology is not the F3^3 path ambiguity.
# Twisted c acts by -Lie3(c); invariant coboundary parameters are
# therefore (1-Lie3(c))A.  Scalar 7 is a 3-adic unit.
assert s.trace(C)==-2
trace_lie_c=(int(s.trace(C))**3-int(s.trace(C)))/3
assert trace_lie_c==-2
rank=(330-int(trace_lie_c))//2
assert rank==166
rel=((LT-7*np.eye(330,dtype=np.int64))@(np.eye(330,dtype=np.int64)-LC))%MOD
ambient=smith3(rel,rank=rank)
ambient_hist=dict(sorted(Counter(ambient).items()))
assert ambient_hist=={0:73,1:59,2:27,3:7}
print('Ambient H1(Gamma,Lie3(V)(-1)): free rank',330-rank,'; Smith valuations',ambient_hist)
print('Its torsion is C3^59 + C9^27 + C27^7, distinct from E39 path-kernel C3^3.')

# Central coefficient group of the specific LM7 E.38 quotient of order 3^30.
# Coordinates below are U^2,U^3,U^4 in (Z/3^6)[U]/U^5.
G3=s.Matrix([[27,0,0],[54,9,0],[45,18,9]])
G4=s.Matrix([[0,0],[81,0],[243,27]])
L3=hermite_normal_form(G3.row_join(729*s.eye(3)))
L4=hermite_normal_form(G4.row_join(729*s.eye(3)))
relative=L3.inv()*L4
assert all(t.q==1 for t in relative)
diag=smith_normal_form(relative,domain=s.ZZ)
central=[abs(int(diag[i,i])) for i in range(3)]
assert s.prod(central)==3**6
print('Central gamma3 of LM7 E38 finite quotient: Smith orders',central,'; total order 3^6.')
torsion_log=59+2*27+3*7
assert torsion_log==134
print('Ambient action torsion order 3^134; its map to the finite central H1 has kernel order at least 3^128.')

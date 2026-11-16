"""Exact integral-at-three centralizer of the actual icosahedral action.

Use the independently certified twelve-strand A5 braid generators.
This is a separate geometric marking of the same unlabelled A5 action;
no comparison with a particular common monodromy word is inferred.
"""
from pathlib import Path
from collections import Counter,defaultdict
import json,itertools,math,time
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent;BASE=HERE.parent;ROOT=BASE.parent
start=time.monotonic();n=10;I=np.eye(n,dtype=np.int64)
d=json.loads((ROOT/'data/icosahedral_braids.json').read_text())
epsilon=np.array([(-1)**i for i in range(12)],dtype=np.int64)
inc=np.vstack([I,-epsilon[:10],np.zeros((1,10),dtype=np.int64)])
assert not np.any(epsilon@inc)
gens={}
old=json.loads((BASE/'next_finite_symplectic/matrices.json').read_text())
Jq=np.array(old['integral_symplectic_form'],dtype=np.int64)
change=I+np.ones((10,1),dtype=np.int64)*epsilon[:10]
J=change.T@Jq@change
for j in range(1,12):
    B=np.eye(12,dtype=np.int64);B[j-1:j+1,j-1:j+1]=[[2,-1],[1,0]]
    A=B@inc;R=A[:10]-np.ones((10,1),dtype=np.int64)*A[11]
    assert np.array_equal(R.T@J@R,J)
    gens[j]=R
def ev(word):
    A=I.copy()
    for j in word:A=A@gens[j]
    return A
S=-ev(d['beta2']);R=ev(d['beta3'])
assert np.array_equal(S@S,I)
assert np.array_equal(R@R@R,I)
assert np.array_equal(np.linalg.matrix_power(S@R@R,5),I)

def perm(word):
    p=list(range(12))
    for j in word:p[j-1],p[j]=p[j],p[j-1]
    return tuple(p)
def mul(p,q):return tuple(p[j] for j in q)
def order(p):
    r=tuple(range(12))
    for k in range(1,61):
        r=mul(r,p)
        if r==tuple(range(12)):return k
    raise AssertionError
identity=tuple(range(12));seen={identity:I};todo=[identity]
for p in todo:
    for q,B in [(perm(d['beta2']),S),(perm(d['beta3']),R)]:
        pp=mul(p,q);A=seen[p]@B
        if pp in seen:assert np.array_equal(seen[pp],A)
        else:seen[pp]=A;todo.append(pp)
assert len(seen)==60
char=defaultdict(Counter)
for p,A in seen.items():char[order(p)][int(np.trace(A))]+=1
assert dict(char)=={1:Counter({10:1}),2:Counter({2:15}),3:Counter({-2:20}),5:Counter({0:24})}
print('PASS actual integral A5 action, order60, character twice the degree5 character',flush=True)

def rref3(A):
    A=np.array(A,dtype=np.int64,copy=True)%3;r=0;piv=[]
    for j in range(A.shape[1]):
        k=next((k for k in range(r,A.shape[0]) if A[k,j]),None)
        if k is None:continue
        A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
        f=A[:,j].copy();f[r]=0;A=(A-f[:,None]*A[r])%3
        r+=1;piv.append(j)
        if r==A.shape[0]:break
    return A,piv

def kernel3(A):
    A,piv=rref3(A);free=[j for j in range(A.shape[1]) if j not in piv]
    out=[]
    for j in free:
        v=np.zeros(A.shape[1],dtype=np.int64);v[j]=1
        for i,k in enumerate(piv):v[k]=-A[i,j]%3
        out.append(v)
    return out

def integral3_kernel(A):
    vectors=A.nullspace();out=[]
    for v in vectors:
        den=s.ilcm(*[x.q for x in v]);out.append(v*den)
    K=s.Matrix.hstack(*out);steps=0
    while True:
        null=kernel3(np.array(K,dtype=np.int64))
        if not null:break
        v=K*s.Matrix(null[0].tolist())/3
        assert all(x.q==1 for x in v)
        K=hermite_normal_form(K.row_join(v));steps+=1
    assert A*K==s.zeros(A.rows,K.cols)
    print('kernel dimension',K.cols,'3-saturation steps',steps,flush=True)
    return K

SS=s.Matrix(S);RR=s.Matrix(R);II=s.eye(n)
comm=(s.kronecker_product(II,SS.T)-s.kronecker_product(SS,II)).col_join(
      s.kronecker_product(II,RR.T)-s.kronecker_product(RR,II))
End=integral3_kernel(comm)
symp=[]
for i,j in itertools.combinations(range(n),2):
    row=[0]*100
    for k in range(n):row[k*n+i]+=int(J[k,j]);row[k*n+j]+=int(J[i,k])
    symp.append(row)
eq=comm.col_join(s.Matrix(symp));Lie=integral3_kernel(eq)
assert (End.cols,Lie.cols)==(4,3)
rankmod3=100-len(rref3(np.array(eq,dtype=np.int64))[1])
print('Actual integral symplectic centralizer Lie dimension3; mod3 centralizer dimension',rankmod3,flush=True)
BM=[s.Matrix(n,n,list(Lie.col(i))) for i in range(3)]
qdiag=[];qcross={}
for i,A in enumerate(BM):
    q=A*A;v=q[0,0];assert q==v*s.eye(n);qdiag.append(v)
    for j,B in enumerate(BM[:i]):
        q=A*B+B*A;v=q[0,0];assert q==v*s.eye(n);qcross[(j,i)]=v
print('Quadratic form diagonal',qdiag,'cross',qcross,flush=True)
def q(v):return sum(v[i]*v[i]*qdiag[i] for i in range(3))+sum(v[i]*v[j]*a for (i,j),a in qcross.items())
def valuation3(a):
    a=s.Rational(a);num,den=int(a.p),int(a.q);v=0
    if num==0:return 100000
    while num%3==0:num//=3;v+=1
    while den%3==0:den//=3;v-=1
    return v
isotropic=[]
for v in itertools.product(range(-5,6),repeat=3):
    if not any(v) or math.gcd(*v)!=1 or next(x for x in v if x)<0:continue
    if q(v)==0:isotropic.append(s.Matrix(v))
print('Small primitive isotropic vectors:',len(isotropic),flush=True)
_,pivot=Lie.T.rref();small=Lie[list(pivot),:];small_inv=small.inv()
found=None
for ec in isotropic:
    E=sum((ec[i]*BM[i] for i in range(3)),s.zeros(n))
    for fc in isotropic:
        F0=sum((fc[i]*BM[i] for i in range(3)),s.zeros(n))
        v=E*F0+F0*E;k=v[0,0]
        assert v==k*s.eye(n)
        if k==0 or valuation3(k)!=1:continue
        H=(E*F0-F0*E)/k
        hc=small_inv*s.Matrix(list(H))[list(pivot),:]
        if any(valuation3(x)<0 for x in hc):continue
        fc=3*fc/k;F=3*F0/k
        coords=s.Matrix.hstack(hc,ec,fc)
        if valuation3(coords.det())!=0:continue
        assert H*H==s.eye(n) and E*E==F*F==s.zeros(n)
        assert H*E-E*H==2*E and H*F-F*H==-2*F
        assert E*F-F*E==3*H
        assert E*F==3*(s.eye(n)+H)/2 and F*E==3*(s.eye(n)-H)/2
        found=(H,E,F,coords);break
    if found:break
assert found is not None
H,E,F,coords=found
print('PASS exact Iwahori Lie basis over Z_(3): [H,E]=2E,[H,F]=-2F,[E,F]=3H',flush=True)
print('Basis determinant valuation3:',valuation3(coords.det()),'; coordinates:',coords.tolist(),flush=True)
orderbasis=s.Matrix.hstack(s.Matrix(list(s.eye(n))),s.Matrix(list(H)),s.Matrix(list(E)),s.Matrix(list(F)))
assert all(valuation3(x)>=0 for x in orderbasis)
order_mod3=np.array([[int(s.Rational(x).p)*pow(int(s.Rational(x).q),-1,3)%3 for x in orderbasis.row(i)] for i in range(100)],dtype=np.int64)
assert len(rref3(order_mod3)[1])==4
assert comm*orderbasis==s.zeros(comm.rows,4)
print('PASS full integral-at3 commuting order is the level3 Eichler order',flush=True)

def ser(A):return [[str(x) for x in A.row(i)] for i in range(A.rows)]
record={'S':S.tolist(),'R':R.tolist(),'symplectic_form':J.tolist(),
        'character_by_order':{str(k):{str(v):c for v,c in C.items()} for k,C in char.items()},
        'commuting_order_basis':ser(End),'Lie_basis':ser(Lie),
        'Lie_mod3_dimension':rankmod3,'quadratic_diagonal':[str(x) for x in qdiag],
        'quadratic_cross':{str(k):str(v) for k,v in qcross.items()},
        'Iwahori_H':ser(H),'Iwahori_E':ser(E),'Iwahori_F':ser(F),
        'Iwahori_basis_coordinates':ser(coords),
        'scope':'Actual A5 integral-at3 homology centralizer. No equality with the residual K or with either completed monodromy image is inferred.'}
(HERE/'icosahedral_integral_centralizer_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS exact centralizer calculation in',round(time.monotonic()-start,3),'seconds',flush=True)

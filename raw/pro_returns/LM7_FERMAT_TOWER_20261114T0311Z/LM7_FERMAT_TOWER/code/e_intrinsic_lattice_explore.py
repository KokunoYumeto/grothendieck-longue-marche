from pathlib import Path
import json
from itertools import combinations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

R=s.Matrix([[0,-1],[1,-1]])
CE=s.Matrix([[1,-1],[0,-1]])
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([[-v,u] for u,v in coords])
perm=[0,2,1,3,5,4,7,6]
CT=s.zeros(8)
for i,j in enumerate(perm):CT[i,j]=-1

def Vmat(A,Q):
    return A.row_join(s.zeros(2,8)).col_join(((U*A-Q*U)/3).row_join(Q))
A1=Vmat(-2*s.eye(2),4*s.eye(8))
A2=Vmat(s.eye(2)+3*R,7*s.eye(8))
C=Vmat(CE,CT)
assert all(x.q==1 for A in [A1,A2,C] for x in A)
assert C*C==s.eye(10)
assert A1*A2==A2*A1
assert C*A1*C==A1
A2bar=Vmat(s.eye(2)+3*R*R,7*s.eye(8))
assert C*A2*C==A2bar
assert C*s.Matrix.vstack(3*s.eye(2),U)==s.Matrix.vstack(3*s.eye(2),U)*CE

def exterior(A):
    inds=list(combinations(range(A.rows),2))
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in inds] for i,j in inds])

def val3(x):
    x=abs(int(x));r=0
    if x==0:return None
    while x%3==0:x//=3;r+=1
    return r

def local_smith(matrix,rank):
    # Work over Z/3^5. The first matrix has eigenvalues -2,4 on V,
    # hence 4,-8,16 on wedge2 V. Evaluating its annihilating
    # polynomial at1 shows that 3^4 kills every invariant torsion
    # element. Thus all elementary-divisor valuations are <5.
    n=matrix.cols
    modulus=3**5
    a=[[int(v)%modulus for v in row] for row in matrix.tolist()]
    rows=len(a);cols=n;vs=[]
    for k in range(rank):
        best=min(((val3(a[i][j]) if a[i][j] else 5,i,j)
                  for i in range(k,rows) for j in range(k,cols)))
        v,i,j=best
        assert v<5, 'annihilator bound excludes a zero residual column'
        a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        power=3**v
        unit=(a[k][k]//power)%(modulus//power)
        inv=pow(unit,-1,modulus)
        a[k]=[(z*inv)%modulus for z in a[k]]
        assert a[k][k]==power
        for i in range(k+1,rows):
            assert a[i][k]%power==0
            c=a[i][k]//power
            a[i]=[(x-c*y)%modulus for x,y in zip(a[i],a[k])]
        for j in range(k+1,cols):
            assert a[k][j]%power==0
            c=a[k][j]//power
            for i in range(rows):a[i][j]=(a[i][j]-c*a[i][k])%modulus
        vs.append(v)
    assert all(a[i][j]==(3**vs[i] if i==j and i<rank else 0)
               for i in range(rows) for j in range(cols))
    return vs
def invariant(A):
    n=A[0].rows
    return local_smith(s.Matrix.vstack(*[a-s.eye(n) for a in A]),n)
v=invariant([A1,A2,C]);print('V invariants exponents',v,flush=True)
assert sorted(x for x in v if x)==[1,1,1]
w=invariant([exterior(A1),exterior(A2),exterior(C)])
print('wedge2 V invariants exponents',w,flush=True)
print('positive',sorted(x for x in w if x),flush=True)
print('order exponent',sum(w),flush=True)
W2=exterior(A2);WC=exterior(C)
cochain_matrix=(W2-s.eye(45))*(WC+s.eye(45))
cochain=local_smith(cochain_matrix,21)
print('H1 unramified direct cocycle-cokernel nonzero Smith exponents',cochain,flush=True)
assert sorted(x for x in cochain if x)==sorted(x for x in w if x)
print('H1 unramified = Z3^24 + (Z/3)^9 + (Z/9)^5',flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'U':U.tolist(),'A1':A1.tolist(),'A2':A2.tolist(),'C':C.tolist(),'V_exponents':v,'W_exponents':w,'cochain_matrix':cochain_matrix.tolist(),'cochain_Smith_exponents':cochain},indent=2,default=int)+'\n')

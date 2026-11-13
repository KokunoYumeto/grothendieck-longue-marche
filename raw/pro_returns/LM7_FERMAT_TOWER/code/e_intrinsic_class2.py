#!/usr/bin/env python3
"""Exact lattice, cusp and cohomology certificates for E.37."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import sympy as s
from e_cubic_abelian import K

OUT=Path(__file__).resolve().parent
zeta=K(0,1);lam=1-zeta;epsilon=-(zeta**2)
R=s.Matrix([[0,-1],[1,-1]])
CE=s.Matrix([[1,-1],[0,-1]])
labels=['A0','A1','A2','B0','B1','B2','C1','C2']
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([[-v,u] for u,v in coords])
perm=[0,2,1,3,5,4,7,6]
CT=s.zeros(8)
for i,j in enumerate(perm):CT[i,j]=-1

def Vmat(A,Q):
    ans=A.row_join(s.zeros(2,8)).col_join(((U*A-Q*U)/3).row_join(Q))
    assert all(x.q==1 for x in ans)
    return ans

def ext(A):
    ix=list(combinations(range(A.rows),2))
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in ix] for i,j in ix])

def val3(x):
    x=F(x);n,d=abs(x.numerator),x.denominator
    if not n:return 1000000
    v=0
    while n%3==0:n//=3;v+=1
    while d%3==0:d//=3;v-=1
    return v

def smith_dvr(matrix, rank):
    """Exact rational elementary operations, all matrices invertible over Z3."""
    a=[[F(x) for x in row] for row in matrix.tolist()]
    m,n=matrix.shape
    left=[[F(i==j) for j in range(m)] for i in range(m)]
    right=[[F(i==j) for j in range(n)] for i in range(n)]
    vals=[]
    for k in range(rank):
        v,i,j=min((val3(a[i][j]),i,j) for i in range(k,m) for j in range(k,n))
        assert 0<=v<1000000
        a[k],a[i]=a[i],a[k];left[k],left[i]=left[i],left[k]
        for mat in (a,right):
            for row in mat:row[k],row[j]=row[j],row[k]
        u=F(3**v)/a[k][k]
        assert val3(u)==0
        a[k]=[x*u for x in a[k]];left[k]=[x*u for x in left[k]]
        for i in range(k+1,m):
            c=a[i][k]/(3**v);assert val3(c)>=0
            if c:
                a[i]=[x-c*y for x,y in zip(a[i],a[k])]
                left[i]=[x-c*y for x,y in zip(left[i],left[k])]
        for j in range(k+1,n):
            c=a[k][j]/(3**v);assert val3(c)>=0
            if c:
                for mat in (a,right):
                    for i in range(len(mat)):mat[i][j]-=c*mat[i][k]
        vals.append(v)
    assert all(a[i][j]==(3**vals[i] if i==j and i<rank else 0)
               for i in range(m) for j in range(n))
    return vals,left,right

A1=Vmat(-2*s.eye(2),4*s.eye(8))
A2=Vmat(s.eye(2)+3*R,7*s.eye(8))
C=Vmat(CE,CT)
assert C*C==s.eye(10)
assert A1*A2==A2*A1
assert C*A2*C==Vmat(s.eye(2)+3*R*R,7*s.eye(8))
j=s.Matrix.vstack(3*s.eye(2),U)
assert C*j==j*CE
assert A2*j==j*(s.eye(2)+3*R)
ix=list(combinations(range(10),2))
ell=s.Matrix([j[i,0]*j[k,1]-j[i,1]*j[k,0] for i,k in ix])
pivot=ix.index((2,4)) # cusp A0 wedge A2
assert ell[pivot]==1 and ell[ix.index((0,1))]==9
for A,q in [(A1,4),(A2,7),(C,-1)]:assert ext(A)*ell==q*ell

# Exact cohomology quotient; I+C has image M^c over Z3 because2 is a unit.
B2=ext(A2);BC=ext(C)
D=(B2-s.eye(45))*(s.eye(45)+BC)
print('Computing exact DVR Smith form of the 45x45 cocycle map...',flush=True)
vals,left,right=smith_dvr(D,21)
assert vals==[0]*7+[1]*9+[2]*5
L=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row] for row in left])
RR=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row] for row in right])
diag=L*D*RR
assert diag==s.diag(*([3**v for v in vals]+[0]*24))
print('Exact cocycle Smith: 7 units, 9 factors3, 5 factors9, 24 free coordinates.',flush=True)

# Weil pairing sign at the actual negative Weierstrass points A0,A2.
assert -(zeta-1)/(zeta**2-1)==zeta

cusps={**{'A'+str(i):(K(0),-(zeta**i),K(1)) for i in range(3)},
       **{'B'+str(i):(-(zeta**i),K(0),K(1)) for i in range(3)},
       **{'C'+str(i):(K(1),-(zeta**i),K(0)) for i in range(3)}}
def tangent_line(d,p):
    i=int(d[1]);x,y,z=p
    if d[0]=='A':return y+(zeta**i)*z
    if d[0]=='B':return x+(zeta**i)*z
    return x+(zeta**(2*i))*y

def leading(d,at):
    i=int(d[1])
    if at=='C0':
        if d[0]=='A':return K(3)
        if d[0]=='B':return K(-3)
        return -3*(1-zeta**(2*i))
    assert at==d
    if d[0] in 'AB':return K(F(1,3))
    return -1/(3*(1-zeta**i))

def unit_form(x):
    for e in range(-10,11):
        for r in range(6):
            if x==(epsilon**r)*(lam**e):return {'epsilon_exponent':r,'lambda_exponent':e}
    raise AssertionError('not an exact lambda S-unit')

frames=[]
for d in labels:
    kO=leading(d,'C0');row=[]
    for r in labels:
        kr=leading(d,r) if r==d else tangent_line(d,cusps[r])/tangent_line('C0',cusps[r])
        row.append(unit_form(kr/kO))
    frames.append(row)
print('All64 normalized third-power cusp frame values are exact epsilon/lambda S-units.',flush=True)

# Primary Frobenius matrices and all nonzero quotient eigenvalues in examples.
local=[]
for a,b in [(-2,0),(1,3),(-2,-3),(4,3),(1,-3),(-2,3)]:
    q=a*a-a*b+b*b
    assert a%3==1 and b%3==0
    A=Vmat(a*s.eye(2)+b*R,q*s.eye(8));B=ext(A)
    assert B*ell==q*ell
    rows=[i for i in range(45) if ix[i]!=(0,1)]
    cols=[i for i in range(45) if i!=pivot]
    dq=(B-q*s.eye(45)).extract(rows,cols)
    nE=q+1-(2*a-b)
    expected=q**44*nE**8*(q-1)**28//9
    det=abs(int(dq.det()))
    assert det==expected
    local.append({'primary':[a,b],'norm':q,'elliptic_points':nE,
                  'rank44_integer_matrix_determinant':str(det),
                  'determinant_3_valuation':val3(det)})
print('Rank44 quotient determinants verified at six primary Frobenius examples.',flush=True)

result={'statement':'E.37','cusp_labels':labels,'cusp_E3_coordinates':coords,'U':U.tolist(),
        'A_psi_minus2':A1.tolist(),'A_psi_1_plus3zeta':A2.tolist(),'complex_conjugation':C.tolist(),
        'wedge_basis':[list(x) for x in ix],'primitive_Tate_line':list(ell),
        'quotient_pivot_index':pivot,'cohomology_matrix':D.tolist(),
        'smith_valuations':vals,'free_rank':24,
        'smith_left':[[str(x) for x in row] for row in left],
        'smith_right':[[str(x) for x in row] for row in right],
        'third_power_cusp_frames':frames,'frame_unit_generator':'epsilon=-zeta^2',
        'local_matrix_examples':local,'status':'PASS',
        'scope':'Exact lattice and finite algebra certificates. The continuous localization, tangential comparison and all-fiber criterion are proved in E.37.'}
(OUT/'e_intrinsic_class2.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
print('PASS: all exact integral and rational certificates.',flush=True)

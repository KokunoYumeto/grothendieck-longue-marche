"""Independent, exact lattice certificate for A_norm_kernel.py.

We use elementary extended-Euclidean column operations, tracking every
operation, to produce integer X,Y with M X=H and H Y=M.  These two
identities certify equality of column lattices without trusting a
normal-form label.  det(H), a mod-2 rank calculation, and 4 H^-1
then determine the invariant factors independently of Smith form.
"""
from pathlib import Path
import json
import math
import sympy as S

here=Path(__file__).resolve().parent
data=json.loads((here/'A_norm_kernel_matrix.json').read_text())
M=S.Matrix(data['matrix'])
A=[[int(x) for x in row] for row in M.tolist()]
rows,cols=M.shape
U=[[int(i==j) for j in range(cols)] for i in range(cols)]

def egcd(a,b):
    old_r,r=abs(a),abs(b)
    old_s,s=1,0
    old_t,t=0,1
    while r:
        q=old_r//r
        old_r,r=r,old_r-q*r
        old_s,s=s,old_s-q*s
        old_t,t=t,old_t-q*t
    return old_s*(1 if a>=0 else -1),old_t*(1 if b>=0 else -1),old_r

def two_columns(B,k,j,a,b,c,d):
    assert k!=j and abs(a*d-b*c)==1
    for row in B:
        x,y=row[k],row[j]
        row[k],row[j]=a*x+b*y,c*x+d*y

def transform(k,j,a,b,c,d):
    two_columns(A,k,j,a,b,c,d)
    two_columns(U,k,j,a,b,c,d)

k=cols
for i in range(rows-1,-1,-1):
    k-=1
    for j in range(k-1,-1,-1):
        if A[i][j]:
            a,b,d=egcd(A[i][k],A[i][j])
            r,s=A[i][k]//d,A[i][j]//d
            transform(k,j,a,b,-s,r)
    if A[i][k]<0:
        for B in (A,U):
            for row in B:row[k]=-row[k]
    pivot=A[i][k]
    if not pivot:
        k+=1
        continue
    for j in range(k+1,cols):
        q=A[i][j]//pivot
        transform(j,k,1,-q,0,1)

H=S.Matrix(A)[:,k:]
X=S.Matrix(U)[:,k:]
assert H.shape==(rows,rows)
assert M*X==H
Y=H.inv()*M
assert all(x.q==1 for x in Y)
assert H*Y==M
H_inv=H.inv()
assert all(x.q==1 for x in 4*H_inv)
assert any(x.q!=1 for x in 2*H_inv)

def rank_mod_two(B):
    words=[sum((int(B[i,j])%2)<<j for j in range(B.cols)) for i in range(B.rows)]
    basis={}
    for word in words:
        while word:
            leading=word.bit_length()-1
            if leading in basis:word^=basis[leading]
            else:
                basis[leading]=word
                break
    return len(basis)

index=abs(int(H.det()))
rank2=rank_mod_two(M)
assert index==2**34 and rank2==24
# If Q=(Z/2)^a+(Z/4)^b, then a+b=49-rank(M mod 2)=25,
# and a+2b=log_2(index)=34.  Thus a=16 and b=9.
report={
 'lattice_MX_equals_H':True,
 'lattice_HY_equals_M':True,
 'X_shape':list(X.shape),'Y_shape':list(Y.shape),'H_shape':list(H.shape),
 'H_determinant_absolute':index,
 'four_times_H_inverse_integral':True,
 'two_times_H_inverse_integral':False,
 'M_rank_mod_2':rank2,
 'quotient_generator_count_mod_2':rows-rank2,
 'invariant_factors':{'2':16,'4':9},
 'maximum_abs_X_entry':max(abs(int(x)) for x in X),
 'maximum_abs_Y_entry':max(abs(int(x)) for x in Y),
}
certificate={'H':[[int(x) for x in row] for row in H.tolist()],
 'X':[[int(x) for x in row] for row in X.tolist()],
 'Y':[[int(x) for x in row] for row in Y.tolist()]}
(here/'A_norm_kernel_lattice_certificate.json').write_text(json.dumps(certificate)+'\n')
(here/'A_norm_kernel_certificate_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

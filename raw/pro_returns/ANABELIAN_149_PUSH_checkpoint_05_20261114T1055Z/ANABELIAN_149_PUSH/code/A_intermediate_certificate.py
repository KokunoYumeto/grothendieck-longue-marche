"""Exact lattice certificates for all index-four and index-eight quotients.

This uses integer elementary column operations and verifies both lattice
inclusions by saved matrices X,Y, as in A_norm_kernel_certificate.py.
"""
from pathlib import Path
import json
import sympy as S

here=Path(__file__).resolve().parent

def egcd(a,b):
    r0,r1=abs(a),abs(b);s0,s1=1,0;t0,t1=0,1
    while r1:
        q=r0//r1;r0,r1=r1,r0-q*r1;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
    return s0*(1 if a>=0 else -1),t0*(1 if b>=0 else -1),r0

def certify(rank):
    M=S.Matrix(json.loads((here/('A_intermediate_norms_matrix_rank%d.json'%rank)).read_text())['matrix'])
    A=[[int(x) for x in row] for row in M.tolist()]
    nr,nc=M.shape
    U=[[int(i==j) for j in range(nc)] for i in range(nc)]
    def op(k,j,a,b,c,d):
        assert k!=j and abs(a*d-b*c)==1
        for B in (A,U):
            for row in B:
                x,y=row[k],row[j];row[k],row[j]=a*x+b*y,c*x+d*y
    k=nc
    for i in range(nr-1,-1,-1):
        k-=1
        for j in range(k-1,-1,-1):
            if A[i][j]:
                a,b,d=egcd(A[i][k],A[i][j]);r,s=A[i][k]//d,A[i][j]//d
                op(k,j,a,b,-s,r)
        if A[i][k]<0:
            for B in (A,U):
                for row in B:row[k]=-row[k]
        if not A[i][k]:k+=1;continue
        for j in range(k+1,nc):op(j,k,1,-(A[i][j]//A[i][k]),0,1)
    H=S.Matrix(A)[:,k:];X=S.Matrix(U)[:,k:]
    assert M*X==H
    Y=H.inv()*M
    assert all(v.q==1 for v in Y) and H*Y==M
    exponent=2 if rank==2 else 1
    assert all(v.q==1 for v in exponent*H.inv())
    index=abs(int(H.det()))
    assert index==(512 if rank==2 else 1)
    certificate={name:[[int(x) for x in row] for row in mat.tolist()] for name,mat in [('H',H),('X',X),('Y',Y)]}
    (here/('A_intermediate_lattice_certificate_rank%d.json'%rank)).write_text(json.dumps(certificate)+'\n')
    return {'quotient_rank':rank,'M_shape':list(M.shape),'MX_equals_H':True,'HY_equals_M':True,
        'index':index,'exponent_divides':exponent,'invariant_factors':{'2':9} if rank==2 else {}}

reports=[certify(2),certify(3)]
(here/'A_intermediate_certificate_output.json').write_text(json.dumps(reports,indent=2)+'\n')
print(json.dumps(reports,indent=2))

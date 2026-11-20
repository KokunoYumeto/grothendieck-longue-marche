"""Exact matrix checks for questions on 123/023; no image processing."""
from pathlib import Path
import json
import sympy as S

def flat(M):return S.Matrix(list(M))
def serial(M):return [[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)]

I=S.eye(2); Z=S.zeros(2); J=Z.row_join(I).col_join((-I).row_join(Z))
N=Z.row_join(I).col_join(Z.row_join(Z)); U=S.eye(4)+N
basis=[]; labels=[]
for i in range(2):
 for j in range(2):
  A=S.zeros(2);A[i,j]=1
  basis.append(A.row_join(Z).col_join(Z.row_join(-A.T)));labels.append(f'A{i}{j}')
for block in ['B','C']:
 for i,j in [(0,0),(0,1),(1,1)]:
  M=S.zeros(2);M[i,j]=1;M[j,i]=1
  basis.append(Z.row_join(M if block=='B' else Z).col_join((M if block=='C' else Z).row_join(Z)))
  labels.append(f'{block}{i}{j}')
assert all(Y.T*J+J*Y==S.zeros(4) for Y in basis)
ad=S.Matrix.hstack(*(flat(N*Y-Y*N) for Y in basis))
lie=S.Matrix([[2*S.trace(N*Y) for Y in basis],[4*S.trace(N**3*Y) for Y in basis]])
group=S.Matrix([[S.trace(U*Y) for Y in basis],
 [S.trace(U)*S.trace(U*Y)-S.trace(U**2*Y) for Y in basis]])
adjoint=group.copy();adjoint[0,:]=2*S.trace(U)*group[0,:]
assert N**2==S.zeros(4) and U.T*J*U==J
assert ad.rank()==6 and lie.rank()==group.rank()==adjoint.rank()==1
cert={'sp4':dict(J=serial(J),N=serial(N),U=serial(U),basis_labels=labels,
 dimension=10,rank=2,orbit_dimension=ad.rank(),centralizer_dimension=10-ad.rank(),
 subregular_dimension=10-2-2,lie_differentials=serial(lie),lie_quotient_rank=lie.rank(),
 group_differentials=serial(group),group_quotient_rank=group.rank(),
 adjoint_group_differentials=serial(adjoint),adjoint_group_quotient_rank=adjoint.rank(),
 strict_bound_predicted_by_letter='rank < r-1 = 1',strict_bound_holds=False)}

def sl_basis(n):
 b=[]
 for i in range(n):
  for j in range(n):
   if i!=j:
    M=S.zeros(n);M[i,j]=1;b.append(M)
 for i in range(n-1):
  M=S.zeros(n);M[i,i]=1;M[n-1,n-1]=-1;b.append(M)
 return b

cert['type_A_subregular']=[]
for n in range(2,7):
 b=sl_basis(n);X=S.zeros(n)
 for i in range(n-2):X[i,i+1]=1
 V=S.eye(n)+X
 adX=S.Matrix.hstack(*(flat(X*Y-Y*X) for Y in b))
 dlie=S.Matrix([[k*S.trace(X**(k-1)*Y) for Y in b] for k in range(2,n+1)])
 dgroup=S.Matrix([[k*S.trace(V**k*Y) for Y in b] for k in range(1,n)])
 assert dlie.rank()==dgroup.rank()==n-2
 assert adX.rank()==n*n-n-2
 cert['type_A_subregular'].append(dict(matrix_size=n,rank=n-1,orbit_dimension=adX.rank(),
  lie_quotient_rank=dlie.rank(),group_quotient_rank=dgroup.rank(),predicted=n-2))

# The rank-one nilpotent in sl3 used in the two-projective-line flag argument.
b=sl_basis(3);X=S.zeros(3);X[0,1]=1
adX=S.Matrix.hstack(*(flat(X*Y-Y*X) for Y in b))
assert adX.rank()==4
cert['sl3_flag_example']=dict(nilpotent=serial(X),orbit_dimension=4,number_roots=6,
 predicted_flag_dimension=(6-4)//2,geometric_components='two P1 components meeting at (im X, ker X)')

Path('out/math_checks/123_023_rank_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps({'sp4_orbit_dim':ad.rank(),'sp4_rank':lie.rank(),
 'type_A_sizes':[x['matrix_size'] for x in cert['type_A_subregular']],
 'sl3_subregular_orbit_dimension':adX.rank(),'assertions':'passed'}))

"""Exact small matrix checks prompted by the supplied 123/022 letter.

No image reading or external data. The certificate concerns explicit type-A
models, not a classification of all pairs called in apposition.
"""
import json
from pathlib import Path
import sympy as s

def mat(m):return [[str(s.simplify(x)) for x in row] for row in m.tolist()]
def flat(m):return s.Matrix(list(m))
def sl_borel_basis(n,change):
    basis=[]
    for i in range(n-1):
        m=s.zeros(n);m[i,i]=1;m[n-1,n-1]=-1;basis.append(change*m*change.inv())
    for i in range(n):
        for j in range(i+1,n):
            m=s.zeros(n);m[i,j]=1;basis.append(change*m*change.inv())
    return basis
def flag_check(A,B):
    n=A.rows
    intersections=[]
    for k in range(1,n):
        rank=A[:,:k].row_join(B[:,:n-k]).rank()
        intersections.append({'k':k,'intersection_dimension':n-rank})
    ba=sl_borel_basis(n,A);bb=sl_borel_basis(n,B)
    union=s.Matrix.hstack(*(flat(x) for x in ba+bb)).rank()
    return {'opposite':all(x['intersection_dimension']==0 for x in intersections),
            'complementary_flag_intersections':intersections,
            'sl_borel_intersection_dimension':len(ba)+len(bb)-union}

I=s.I
F=s.Matrix([[I**(r*c) for c in range(4)] for r in range(4)])
D=s.diag(1,I,-1,-I)
cyclic=F.inv()*D*F
assert all(sum(cyclic[r,c]!=0 for r in range(4))==1 for c in range(4))
assert all(sum(cyclic[r,c]!=0 for c in range(4))==1 for r in range(4))
assert D**4==s.eye(4)
sigma=[0,2,1,3]
P=s.eye(4)[:,sigma]
op=flag_check(s.eye(4),F)
nonop=flag_check(P,F*P)
assert op['opposite'] and op['sl_borel_intersection_dimension']==3
assert not nonop['opposite'] and nonop['sl_borel_intersection_dimension']>3
v=F[:,0]+F[:,2]
assert v==s.Matrix([2,0,2,0])
# A diagonal matrix in the Fourier-conjugate diagonal algebra must be scalar.
diag_unknown=s.diag(*s.symbols('d0:4'))
conj=F.inv()*diag_unknown*F
eq=s.Matrix([conj[i,j] for i in range(4) for j in range(4) if i!=j])
coefficient,_=s.linear_eq_to_matrix(list(eq),list(s.symbols('d0:4')))
kernel=coefficient.nullspace()
assert len(kernel)==1 and kernel[0]==s.ones(4,1)

F2=s.Matrix([[1,1],[1,-1]])
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
K=[s.eye(2),X,Z,X*Z]
def monomial(M):return all(sum(M[r,c]!=0 for r in range(2))==1 for c in range(2)) and all(sum(M[r,c]!=0 for c in range(2))==1 for r in range(2))
assert all(monomial(M) and monomial(F2.inv()*M*F2) for M in K)
rank1=[]
for a in [s.eye(2),X]:
    for b in [F2,F2*X]:rank1.append(flag_check(a,b))
assert all(x['opposite'] and x['sl_borel_intersection_dimension']==1 for x in rank1)
result={
 'field':'exact rational complex arithmetic, Q(i) for n=4',
 'rank1':{'Fourier_change':mat(F2),'common_normalizer_projective_representatives':[mat(x) for x in K],
          'four_Borel_pairs':rank1,'h':2,'z':2,'phi_h':1,'conditional_count':1},
 'rank3':{'Fourier_change':mat(F),'regular_diagonal':mat(D),'normalizer_action_in_Fourier_basis':mat(cyclic),
          'shared_diagonal_algebra_kernel':[mat(x) for x in kernel],
          'standard_orders':op,'orders_0_2_1_3':nonop,'common_two_plane_vector':mat(v)},
 'limits':'No complete classification of apposition pairs or proof of the general hz phi(h) normalizer formula. The explicit Fourier pair has regular diagonal and Coxeter-cycle normalization; identifying all such models with Kostant terminology is a separately stated background input.'}
Path('out/math_checks/123_022_flag_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'rank1_pairs':len(rank1),'rank3_opposite':op,'rank3_nonopposite':nonop}))

"""Exact small coefficient calculations; no OCR or external mathematical data."""
from pathlib import Path
import json
from sympy import Matrix

# Basis 1,a,a^2 of Z[C3]; C2 acts by inversion.
J=Matrix([[1,0,0],[0,0,1],[0,1,0]])
q1=Matrix([1,0,0]);qs=Matrix([0,1,1])
def tensor(v,w):return Matrix([v[i]*w[j] for i in range(len(v)) for j in range(len(w))])
cols=[tensor(v,w) for v in (q1,qs) for w in (q1,qs)]
A=Matrix.hstack(*cols)
ds=Matrix([1 if (i,j) in [(1,1),(2,2)] else 0 for i in range(3) for j in range(3)])
assert J*q1==q1 and J*qs==qs
assert A.rank()==4 and A.row_join(ds).rank()==5
# On the regular two-point set the nonidentity action has no fixed point.
regular_fixed=[x for x in range(2) if (x+1)%2==x]
assert regular_fixed==[]
# Free abelian group on the swapped two-point set; invariants are span(1,1).
swap=Matrix([[0,1],[1,0]])
assert (swap-Matrix.eye(2)).nullspace()==[Matrix([1,1])]
# Sign module: invariants vanish; tensor of two signs has trivial action.
assert (Matrix([[-1]])-Matrix.eye(1)).nullspace()==[]
assert (-1)*(-1)==1
data=dict(regular_C2_fixed_points=regular_fixed,free_module_invariant_basis=[[1,1]],sign_module_fixed_rank=0,tensor_of_two_signs_fixed_rank=1,bialgebra_basis=['1','a','a^2'],inversion_matrix=J.tolist(),invariant_basis=[list(q1),list(qs)],tensor_comparison_matrix=A.tolist(),delta_s=list(ds),comparison_rank=A.rank(),augmented_rank=A.row_join(ds).rank(),outcome='delta(s) is not even in the rational span of the invariant-tensor comparison image, hence not in its integral image')
dest=Path('out/math_checks/123_040_fixed_point_certificate.json')
dest.write_text(json.dumps(data,indent=2,default=int)+'\n')
print(json.dumps({'regular_fixed':regular_fixed,'comparison_rank':4,'augmented_rank':5,'all_assertions_passed':True}))

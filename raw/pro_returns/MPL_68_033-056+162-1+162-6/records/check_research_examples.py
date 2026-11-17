"""Exact finite-dimensional check of the base-change example in research E03.

This checks an assistant-proposed example, not the manuscript transcription.
K = Q[epsilon]/epsilon^2, M = K direct-sum Q.
The Q-basis of M is (1 in K, epsilon in K, 1 in Q).
"""
from pathlib import Path
import json
from sympy import Matrix, symbols, linsolve, zeros
N=Matrix([[0,0,0],[1,0,0],[0,0,0]])
x=symbols('x0:9');X=Matrix(3,3,x)
solution=next(iter(linsolve(list(X*N-N*X),x)))
parameters=sorted(set().union(*(entry.free_symbols for entry in solution)),key=str)
basis=[]
for parameter in parameters:
    basis.append(Matrix(3,3,[entry.subs({p:int(p==parameter) for p in parameters}) for entry in solution]))
flatten=lambda m:Matrix(list(m))
rank_J=Matrix.hstack(*(flatten(N*B) for B in basis)).rank()
rank_reduction=Matrix.hstack(*(flatten(B.extract([0,2],[0,2])) for B in basis)).rank()
assert len(basis)==5 and rank_J==1 and rank_reduction==3
assert all((N*B).extract([0,2],[0,2])==zeros(2) for B in basis)
report={
 'note':'E03','field':'Q','ring':'Q[epsilon]/epsilon^2','module':'K direct-sum K/(epsilon)',
 'dim_End_K_M':len(basis),'dim_epsilon_End_K_M':rank_J,
 'dim_End_K_M_tensor_Q':len(basis)-rank_J,'dim_End_Q_Mmod_epsilon':4,
 'rank_canonical_base_change_map':rank_reduction,
 'kernel_dimension_after_base_change':len(basis)-rank_J-rank_reduction,
 'checked':'exact symbolic rational linear algebra',
}
target=Path(__file__).with_name('research_example_check.json')
target.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))

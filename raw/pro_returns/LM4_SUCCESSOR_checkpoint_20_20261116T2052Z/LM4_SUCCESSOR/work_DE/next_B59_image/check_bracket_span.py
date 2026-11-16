"""Exploratory exact class-two restriction to the tetrahedral H1 image.

This checks only brackets of source generators.  It does NOT include
the central images of the seven source-abelian relations, and hence
does NOT compute the full class-two image of H_T.
"""
from pathlib import Path
import itertools,json
import sympy as s
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
d=json.loads((BASE/'full_pair_linking_certificate.json').read_text())
inv=json.loads((BASE/'rigid7_class2_invariants_certificate.json').read_text())
M=s.Matrix(d['full_matrix_rows_pairs_columns_basis'])
pairs=[tuple(p) for p in d['pair_rows']]
pi={p:i for i,p in enumerate(pairs)}
triples=list(itertools.combinations(d['finite_labels'],3))
def bracket(v,u):
 out=[]
 for i,j,k in triples:
  a,b,c=[pi[p] for p in [(i,j),(i,k),(j,k)]]
  out.append(v[a]*u[b]-v[b]*u[a]-v[a]*u[c]+v[c]*u[a]+v[b]*u[c]-v[c]*u[b])
 return out
B=s.Matrix([bracket(M.col(i),M.col(j)) for i,j in itertools.combinations(range(13),2)]).T
w=s.Matrix(inv['primitive_fixed_vector_ambient'])
assert B.rows==165 and w.rows==165
r=B.rank();rw=B.row_join(w).rank()
print(__doc__)
print('Ambient H1 image rank',M.rank())
print('Bracket image rank',r)
print('Bracket image plus B59w rank',rw)
print('B59w belongs to bracket image over Q:',r==rw)
record={'bracket_matrix':[[int(x) for x in B.row(i)] for i in range(B.rows)],
        'bracket_rank':r,'augmented_rank':rw,
        'w_in_rational_bracket_image':r==rw,
        'scope':__doc__}
if r==rw:
 sol,parameters=B.gauss_jordan_solve(w)
 sol=sol.subs({x:0 for x in parameters})
 assert B*sol==w
 record['rational_w_expression']=[str(x) for x in sol]
 print('Rational expression:',[(i,str(x)) for i,x in enumerate(sol) if x])
(HERE/'bracket_span.json').write_text(json.dumps(record,indent=2)+'\n')
print('EXACT CHECK COMPLETE')

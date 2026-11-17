"""Exact class-two bracket image of the geometric pure C5 centralizer.

With its two fixed poles at0,infinity and the two regular orbits
{zeta^i} and {u zeta^i}, the parameter is C* minus the five fifth
roots of unity. Its six meridian H1 images are computed by pair
divisors and transformed to the B58 ambient normalization.
Only brackets are used; source-abelian relation corrections, if any,
are not inferred or omitted silently.
"""
from pathlib import Path
import itertools,json
import sympy as s
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
h1=json.loads((BASE/'ambient_rigid7_abelian_certificate.json').read_text())
iv=json.loads((BASE/'rigid7_class2_invariants_certificate.json').read_text())
geom=json.loads((BASE/'rigid7_subsets.json').read_text())
perm=geom['D_permutation'];done=set();cycles=[]
for i in range(12):
 if i in done:continue
 cyc=[];j=i
 while j not in done:done.add(j);cyc.append(j+1);j=perm[j]
 cycles.append(cyc)
poles=[c[0] for c in cycles if len(c)==1]
orbits=[c for c in cycles if len(c)==5]
assert len(poles)==2 and len(orbits)==2
zero,infinity=poles;X,Y=orbits
sphere_pairs=[tuple(p) for p in h1['sphere_pair_variables']]
pi={p:i for i,p in enumerate(sphere_pairs)}
E=s.zeros(66,6)
for pair in itertools.combinations(Y+[zero],2):E[pi[tuple(sorted(pair))],0]=1
for r in range(5):
 for j in range(5):
  pair=tuple(sorted((X[(j+r)%5],Y[j])))
  E[pi[pair],r+1]=1
A=s.Matrix(h1['ambient_covector_matrix']);M=A*E
ambient_pairs=[tuple(p) for p in h1['ambient_pair_basis']]
ap={p:i for i,p in enumerate(ambient_pairs)}
triples=list(itertools.combinations([i for i in range(1,13) if i!=2],3))
def get(v,p):return v[ap[p]] if p in ap else 0
def bracket(v,u):
 out=[]
 for i,j,k in triples:
  a,b,c=(i,j),(i,k),(j,k)
  va,vb,vc=[get(v,p) for p in (a,b,c)]
  ua,ub,uc=[get(u,p) for p in (a,b,c)]
  out.append(va*ub-vb*ua-va*uc+vc*ua+vb*uc-vc*ub)
 return out
D=A[:,[pi[tuple(sorted((perm[i-1]+1,perm[j-1]+1)))] for i,j in ambient_pairs]]
assert D*M==M
B=s.Matrix([bracket(M.col(i),M.col(j)) for i,j in itertools.combinations(range(6),2)]).T
w=s.Matrix(iv['primitive_fixed_vector_ambient'])
r=B.rank();rw=B.row_join(w).rank()
print(__doc__)
print('D cycles:',cycles)
print('H1 rank:',M.rank(),'; all six meridian classes fixed by D:PASS')
print('Bracket rank:',r,'; adding w:',rw)
record={'cyclic_permutation':perm,'cycles':cycles,
 'poles_zero_infinity':poles,'orbits':orbits,
 'meridian_ambient_H1_columns':[[int(x) for x in M.col(i)] for i in range(6)],
 'bracket_matrix':[[int(x) for x in B.row(i)] for i in range(B.rows)],
 'bracket_rank':r,'augmented_rank':rw,'scope':__doc__}
if r==rw:
 sol,params=B.gauss_jordan_solve(w)
 sol=sol.subs({x:0 for x in params})
 assert B*sol==w
 record['rational_w_expression']=[str(x) for x in sol]
 print('w rational bracket expression:',[(i,str(x)) for i,x in enumerate(sol) if x])
else:print('w not in the rational bracket image.')
(HERE/'cyclic_bracket_span.json').write_text(json.dumps(record,indent=2)+'\n')
print('EXACT CHECK COMPLETE')

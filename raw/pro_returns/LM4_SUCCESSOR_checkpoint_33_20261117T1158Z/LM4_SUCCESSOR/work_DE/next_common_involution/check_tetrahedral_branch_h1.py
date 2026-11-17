"""Exploratory exact H1 in the faithful quotient by a common involution.
No assertion about a new profinite intersection follows from the ranks.
The involution is z -> -z in the fixed tetrahedral coordinate.
"""
from pathlib import Path
import sympy as s, itertools, json, time
HERE=Path(__file__).resolve().parent
u=s.Symbol('u'); I=s.I
F=s.QQ.algebraic_field(I,s.sqrt(3))
pts=[u,1/u,(u+I)/(u-I),(u-I)/(u+I),(u+1)/(-I*u+I),(u-1)/(I*u+I)]
z=[s.cancel((p/u)**2) for p in pts]
assert z[0]==1
# Coordinates 0, infinity, and z[0]=1 are fixed.
coords=[s.S(0)]+z
pairs=[p for p in itertools.combinations(range(7),2) if p!=(0,1)]
a=(s.sqrt(3)-1)/2;b=(s.sqrt(3)+1)/2
roots=[-b+I*b,I,b+I*b,-a+I*a,-1,a+I*a,0,-a-I*a,-b-I*b,a-I*a,1,-I,b-I*b]
factors=[s.Poly(u-r,u,domain=F) for r in roots]
def mult(P,f):
 n=0
 while P.degree()>0:
  Q,R=P.div(f)
  if not R.is_zero:break
  P=Q;n+=1
 return n
def orders(g):
 N,D=s.fraction(s.cancel(g));N=s.Poly(N,u,domain=F);D=s.Poly(D,u,domain=F)
 out=[mult(N,f)-mult(D,f) for f in factors]
 assert sum(out)+D.degree()-N.degree()==0
 return out
M=s.Matrix([orders(coords[i]-coords[j]) for i,j in pairs])
assert M.shape==(20,13)
old=json.loads((HERE.parent/'full_pair_linking_certificate.json').read_text())
A=s.Matrix(old['full_matrix_rows_pairs_columns_basis'])
K=s.Matrix.hstack(*A.nullspace())
print('Quotient PMod0,8 H1 rank',M.rank())
print('Original PMod0,12 H1 rank',A.rank())
print('New quotient H1 rank on the seven-dimensional old source kernel',(M*K).rank())
print('Joint rank',A.col_join(M).rank())
# The target quotient with its two branch labels unordered uses coinvariants.
# Swapping 0 and infinity fixes ordinary label z[0]=1, hence z_i -> 1/z_i.
def zr(i):return s.zeros(1,13) if i==1 else M.row(pairs.index((0,i)))
SM=s.Matrix.vstack(*[-M.row(k) if i==0 else M.row(k)-zr(i)-zr(j)
                     for k,(i,j) in enumerate(pairs)])
plus=M+SM;minus=M-SM
print('Branch-swap coinvariant/invariant rank',plus.rank())
print('Branch-swap anti-invariant rank',minus.rank())
print('Coinvariant rank on old source kernel',(plus*K).rank())
print('Anti-invariant rank on old source kernel',(minus*K).rank())
assert M.rank()==9 and A.rank()==6 and (M*K).rank()==3
assert plus.rank()==6 and minus.rank()==3 and (plus*K).rank()==0

(HERE/'tetrahedral_branch_h1.json').write_text(json.dumps({'source_roots':[str(x) for x in roots],'quotient_coordinates':[str(x) for x in coords],'pairs':pairs,'matrix':M.tolist(),'rank':int(M.rank()),'rank_on_old_kernel':int((M*K).rank()),'branch_swap_matrix_applied_to_source':SM.tolist(),'coinvariant_rank':int(plus.rank()),'coinvariant_rank_on_old_kernel':int((plus*K).rank()),'anti_invariant_rank':int(minus.rank()),'anti_invariant_rank_on_old_kernel':int((minus*K).rank())},indent=2,default=int)+'\n')

"""Exact H1 test after the faithful common-involution quotient and forgetting
one of its branch marks on the index-two cyclic source. No group injection
or surjection is inferred from the resulting rank.
"""
from pathlib import Path
import sympy as S,itertools,json,time
H=Path(__file__).resolve().parent
s=S.Symbol('s');zeta=S.exp(2*S.pi*S.I/5)
F=S.QQ.algebraic_field(zeta)
z=F.ext.as_expr()
# Work with rational functions over the exact cyclotomic field.
R=F.frac_field(s)
x=R.gens[0]
c=[F.from_sympy(zeta**i) for i in range(5)]
g=[R.convert(a,F)/(x-R.convert(a,F))**2 for a in c]
g=[(v-g[0])/(g[1]-g[0]) for v in g]
roots=[a for a in c]+[-a for a in c]
# finite normalized labels 0,1 and three variables; infinity is the retained branch.
pairs=[p for p in itertools.combinations(range(5),2) if p!=(0,1)]
def mult(p,r):
 n=0
 while p.degree()>0:
  q,rem=p.div(S.Poly(s-F.to_sympy(r),s,domain=F))
  if not rem.is_zero:break
  p=q;n+=1
 return n
def orders(f):
 e=R.to_sympy(f);a,b=S.fraction(e);a=S.Poly(a,s,domain=F);b=S.Poly(b,s,domain=F)
 o=[mult(a,r)-mult(b,r) for r in roots]
 assert sum(o)==0 and a.degree()==b.degree()
 return o
M=S.Matrix([orders(g[i]-g[j]) for i,j in pairs])
print('One retained branch: target PMod0,6, source P1 minus mu10')
print('Exact target H1 matrix shape',M.shape,'rank',M.rank())
print('Geometric candidate cusp types (not used to infer the computed rank): positive-root three pairs; negative-root two pairs')
(H/'cyclic_one_branch_h1.json').write_text(json.dumps({'pairs':pairs,'source_roots':['zeta^'+str(i) for i in range(5)]+['-zeta^'+str(i) for i in range(5)],'matrix':M.tolist(),'rank':M.rank()},indent=2,default=int)+'\n')

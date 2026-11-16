"""Exact H1 comparison for the faithful decorated seven-point cyclic map.
This verifies a limitation of an abelian test; no group-kernel claim follows.
"""
from pathlib import Path
import sympy as S,itertools,json
H=Path(__file__).resolve().parent
s=S.Symbol('s'); zeta=S.exp(2*S.pi*S.I/5)
F=S.QQ.algebraic_field(zeta);R=F.frac_field(s);x=R.gens[0]
c=[F.from_sympy(zeta**i) for i in range(5)]
z=[R.convert(a,F) for a in c]
g=[R.zero,R.one]+[((x+a)*(x-1)/((x-a)*(x+1)))**2 for a in z[1:]]
roots=[F.zero]+c+[-a for a in c]
pairs=[p for p in itertools.combinations(range(6),2) if p!=(0,1)]
def mult(p,r):
 n=0;l=S.Poly(s-F.to_sympy(r),s,domain=F)
 while p.degree()>0:
  q,rem=p.div(l)
  if not rem.is_zero:break
  p=q;n+=1
 return n
def orders(f):
 a,b=S.fraction(R.to_sympy(f));a=S.Poly(a,s,domain=F);b=S.Poly(b,s,domain=F)
 o=[mult(a,r)-mult(b,r) for r in roots]
 # Every zero/pole is at one of the twelve source punctures.
 assert sum(o)==a.degree()-b.degree()
 return o
M=S.Matrix([orders(g[i]-g[j]) for i,j in pairs])
J=S.zeros(11);J[0,0]=1
for i in range(5): J[1+i,6+i]=1;J[6+i,1+i]=1
assert J*J==S.eye(11)
# The infinite meridian is minus the sum of the finite ones.
assert M[:,0]==-M*S.ones(11,1)
print('Two retained branches: target PMod0,7; source P1 minus {0,infinity,mu10}')
print('H1 matrix shape',M.shape,'rank',M.rank())
print('Deck-invariant source-image rank',(M*(S.eye(11)+J)).rank())
print('Deck-anti-invariant source-image rank',(M*(S.eye(11)-J)).rank())
print('The zero and infinity cusp columns are equal: PASS')
print('One-branch experiment is different; no full source group kernel is inferred.')
(H/'cyclic_two_branch_h1.json').write_text(json.dumps({'pairs':pairs,'source_roots':['0']+['zeta^'+str(i) for i in range(5)]+['-zeta^'+str(i) for i in range(5)],'matrix':M.tolist(),'rank':M.rank(),'plus_rank':(M*(S.eye(11)+J)).rank(),'minus_rank':(M*(S.eye(11)-J)).rank()},indent=2,default=int)+'\n')

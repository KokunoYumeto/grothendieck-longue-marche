"""Exact even-source actions on the ordered family; tests the restricted D8 gate only."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from weighted_stallings import substitute as sub,multiply as mul,inverse as inv,WeightedFold
P=Path(__file__).resolve().parent
d=json.loads((P/'tangent_ordered_family.json').read_text())
A={int(k):{int(i):tuple(w) for i,w in a.items()} for k,a in d['V_basis_actions'].items()}
Ai={int(k):{int(i):tuple(w) for i,w in a.items()} for k,a in d['V_basis_inverse_actions'].items()}
ordered={int(i):tuple(w) for i,w in d['ordered_basis_in_V'].items()}
f=WeightedFold(list(ordered.values()))
def rw(w):
 z=f.rewrite(w);assert z is not None and sub(z,ordered)==mul(w);return z
def fill(w):return mul(tuple(x-4 if x>0 else x+4 for x in w if abs(x)>4))
def ab(w):
 a=[0]*9
 for x in w:a[abs(x)-1]+=1 if x>0 else -1
 return s.Matrix(a)
def comp(a,b):return {i:sub(b[i],a) for i in range(1,8)}
G={};Gi={}
for k in (0,2,3,4,5):
 G[f'alpha{k}']=A[k];Gi[f'alpha{k}']=Ai[k]
 G[f'alpha1_alpha{k}_alpha1inv']=comp(A[1],comp(A[k],Ai[1]));Gi[f'alpha1_alpha{k}_alpha1inv']=comp(A[1],comp(Ai[k],Ai[1]))
G['alpha1_squared']=comp(A[1],A[1]);Gi['alpha1_squared']=comp(Ai[1],Ai[1])
shifts={j:[] for j in [1,2,4,6]};matrices=[];result={}
for name,g in G.items():
 for sig,a in [(1,g),(-1,Gi[name])]:
  oa={i:rw(sub(w,a)) for i,w in ordered.items()}
  assert all(not fill(oa[i]) for i in range(1,5))
  M=s.Matrix.hstack(*(ab(fill(oa[i])) for i in range(5,14)));assert abs(M.det())==1
  conj={}
  for j in shifts:
   h=[];core=a[j]
   while len(core)>1 and core[0]==-core[-1]:h.append(core[0]);core=core[1:-1]
   assert core==(j,)
   hq=fill(rw(h));conj[j]=hq;shifts[j].append(ab(hq))
  matrices.append(M)
  result[name+('^-1' if sig<0 else '')]={'ordered_actions':oa,'peripheral_conjugators_F9':conj,'H1_matrix':M.tolist()}
print('All22 even-source actions/inverses preserve N_selected: PASS')
lattices={}
for j in shifts:
 L=hermite_normal_form(s.Matrix.hstack(*shifts[j]));ranks=[L.cols]
 for n in range(10):
  N=hermite_normal_form(s.Matrix.hstack(L,*(M*L for M in matrices)))
  if N==L:break
  L=N;ranks.append(L.cols)
 else:raise AssertionError('no stabilization')
 S=smith_normal_form(L,domain=s.ZZ);diag=[int(S[i,i]) for i in range(min(S.shape))]
 print('label',j,'affine index-lattice rank',L.cols,'Smith',diag)
 lattices[j]={'basis':L.tolist(),'rank':L.cols,'Smith':diag}
# The old restricted character sees the missing alpha1^2 explicitly.
q=result['alpha1_squared'];ells={j:sum(1 if x==6 else -1 if x==-6 else 0 for x in w) for j,w in q['peripheral_conjugators_F9'].items()}
print('alpha1^2 peripheral E-index shifts:',ells)
D2=(5,7,5,7);rr=rw(D2);print('D^2 in ordered basis',rr)
assert rr==(12,10,13,9)
out={'description':__doc__,'even_actions':result,'affine_H1_shift_lattices':lattices,'alpha1_squared_E_shifts':ells,'D_squared_in_ordered_basis':rr,'scope':'Exact even-source action table and index obstruction audit; full affine lattice rank does not imply transitivity or subgroup equality.'}
(P/'tangent_even_family_actions.json').write_text(json.dumps(out,indent=2,default=int)+'\n')

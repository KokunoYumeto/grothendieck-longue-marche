"""Exact ordered F13 marking and restricted-family action; no source-normality inference."""
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from weighted_stallings import substitute as sub,multiply as mul,inverse as inv
P=Path(__file__).resolve().parent
raw=json.loads((P/'tangent_bundle_fiber_data.json').read_text())
b=json.loads((P/'tangent_infinity_action.json').read_text())
v=json.loads((P/'tangent_node_strips.json').read_text())
newold={int(i):tuple(w) for i,w in b['basis_new2_in_original'].items()};oldnew={int(i):tuple(w) for i,w in b['basis_original_in_new2'].items()}
vo={int(i):tuple(w) for i,w in v['V_basis_in_new2'].items()};ov={int(i):tuple(w) for i,w in v['new2_basis_in_V'].items()}
actions={};inverses={}
for k in range(6):
 for out,key in [(actions,'old_actions'),(inverses,'old_inverse_actions')]:
  a={int(i):tuple(w) for i,w in raw[key][str(k)].items()}
  out[k]={j:sub(sub(sub(sub(vo[j],newold),a),oldnew),ov) for j in range(1,8)}
# Second V basis uses labels 1,2,4,6; retained A=3,B=5,C=7.
js=[1,2,4,6]
ordered={i+1:(j,) for i,j in enumerate(js)}
ordered.update({i+5:(3,j,-3) for i,j in enumerate(js)})
ordered.update({9:(7,),10:(3,7,-3),11:(3,3),12:(5,-3),13:(3,5)})
pos={}
for i,j in enumerate(js):pos[0,j]=(i+1,);pos[1,j]=(i+5,)
pos.update({(0,7):(9,),(1,7):(10,),(0,3):(),(1,3):(11,),(0,5):(12,),(1,5):(13,)})
def rewrite(w):
 st=0;ans=()
 for c in w:
  odd=int(abs(c) in (3,5));pre=st if c>0 else st^odd
  piece=pos[pre,abs(c)];ans=mul(ans,piece if c>0 else inv(piece));st^=odd
 assert st==0,('not ordered',w)
 assert sub(ans,ordered)==mul(w)
 return ans
def fill(w):return tuple((x-4 if x>0 else x+4) for x in w if abs(x)>4)
def redfill(w):return mul(fill(w))
def ab(w):
 a=[0]*9
 for x in w:a[abs(x)-1]+=1 if x>0 else -1
 return s.Matrix(a)
for i,w in ordered.items():assert rewrite(w)==(i,)
print('13-generator index-two Schreier basis and literal round trips: PASS')
# The four original inverse source words become V1,V4 and C^-1 V2/V6 C.
seeds={}
for key,w in raw['new_fiber_words'].items():
 ww=sub(sub(inv(w),oldnew),ov);seeds[int(key)]=ww
print('Source inverse words in V marking:',seeds)
assert set(seeds.values())=={(1,),(4,),(-7,2,7),(-7,6,7)}
assert sub((-7,2,7),actions[5])==(2,)
assert sub((-7,6,7),actions[3])==(6,)
print('J0 is exactly the Gamma0 orbit subgroup of the four original source seeds: PASS')
Gamma=[0,2,3,4,5]
result={};matrices=[];shifts={j:[] for j in js}
for k in Gamma:
 for sign,act in [(1,actions[k]),(-1,inverses[k])]:
  oa={j:rewrite(sub(w,act)) for j,w in ordered.items()}
  for i in range(1,5):assert not redfill(oa[i])
  M=s.Matrix.hstack(*(ab(redfill(oa[i])) for i in range(5,14)));assert abs(M.det())==1
  conj={}
  for j in js:
   w=act[j];h=[]
   while len(w)>1 and w[0]==-w[-1]:h.append(w[0]);w=w[1:-1]
   assert w==(j,)
   hh=redfill(rewrite(h));conj[j]=hh;shifts[j].append(ab(hh))
  matrices.append(M)
  result[str(sign*(k+1))]={'ordered_action':oa,'quotient_F9_action':{i-4:redfill(oa[i]) for i in range(5,14)},'peripheral_conjugators_F9':conj,'H1_matrix':M.tolist()}
print('All ten Gamma0 actions preserve the selected normal family kernel: PASS')
lattices={}
for j in js:
 L=hermite_normal_form(s.Matrix.hstack(*shifts[j]));dims=[L.cols]
 for n in range(10):
  N=hermite_normal_form(s.Matrix.hstack(L,*(M*L for M in matrices)))
  if N==L:break
  L=N;dims.append(L.cols)
 else:raise AssertionError('lattice did not stabilize')
 smith=smith_normal_form(L,domain=s.ZZ);diag=[int(smith[i,i]) for i in range(min(smith.shape))]
 print('Selected label',j,'affine H1 shift lattice ranks',dims,'Smith',diag)
 lattices[j]={'basis':L.tolist(),'rank':L.cols,'Smith':diag,'ranks':dims}
out={'description':__doc__,'V_basis_actions':actions,'V_basis_inverse_actions':inverses,'ordered_basis_in_V':ordered,'source_inverse_words_in_V':seeds,'Gamma0_actions':result,'affine_H1_shift_lattices':lattices,'scope':'The exact action and invariant lattices are necessary information only; no transitivity or full J0 normality is inferred.'}
(P/'tangent_ordered_family.json').write_text(json.dumps(out,indent=2,default=int)+'\n')

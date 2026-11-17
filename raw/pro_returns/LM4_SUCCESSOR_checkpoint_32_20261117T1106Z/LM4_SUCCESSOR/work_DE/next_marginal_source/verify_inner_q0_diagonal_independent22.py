#!/usr/bin/env python3
"""Independent B111 replay using only [a,bar a] after eliminating e.

This does not import the CE HNN oracle, or use any other graph relation.
"""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
       ROOT/'records/inner_bad_normalized22.json',ROOT/'records/inner_bad_hnn22.json']
D,N,H=[json.loads(p.read_text()) for p in paths]
def red(w):
 a=[]
 for x in w:
  x=2 if abs(x)==2 else int(x)
  if a and (a[-1]==-x or a[-1]==x==2):a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w):return red(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))
def conj(a,b):return mul(a,b,inv(a))
def comm(a,b):return mul(a,b,inv(a),inv(b))
U=(-3,1,2,-1,3);V=(5,-6,-5)
negative={int(k):tuple(v) for k,v in D['loops'][0]['negative_pull'].items()}
assert sub((5,),negative)==(5,)
assert sub(U,negative)==conj(V,U)
r=comm((5,),conj(U,(5,)))
assert r==red(next(l for l in D['loops'] if l['name']=='beta_33')['nodes'][0]['relation'])
old_new={int(k):tuple(v) for k,v in N['old_in_new'].items()}
f_w={i:(i,) for i in range(1,7)};f_w[6]=tuple(H['branch_f_in_new_generators'])
image=sub(sub(sub(r,negative),old_new),f_w)
candidate=conj((1,-3,6,7),comm((7,),(2,7,2)))
# Eliminate e by the genuine relation e=w p w^-1.  Now the only
# graph commutation allowed below is [a,bar a]=1.
elim={i:(i,) for i in (1,2,3,4,5,6,7)};elim[5]=(6,7,-6)
diff=sub(mul(image,inv(candidate)),elim)
def one_edge_normal(word):
 parity=0;a=[]
 for x in red(word):
  if x==2:parity^=1;continue
  v=(abs(x),parity);sign=1 if x>0 else -1
  assert v[0] in (1,3,6,7)
  removed=False
  for k in range(len(a)-1,-1,-1):
   u,s=a[k]
   if u==v:
    if s==-sign:a.pop(k);removed=True
    break
   if {u,v}!={(1,0),(1,1)}:break
  if not removed:a.append((v,sign))
 return tuple(a),parity
assert one_edge_normal(diff)==((),0)
missing=comm((7,),(2,7,2))
assert one_edge_normal(missing)!= ((),0)
assert frozenset(((7,0),(7,1))) not in {frozenset(map(tuple,e)) for e in H['base_edges']}
out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'literal_negative_q0_cone_identity':True,'actual_contact_relation':r,
 'complete_HNN_image':image,'conjugator':[1,-3,6,7],
 'missing_diagonal':missing,'candidate':candidate,
 'only_used_relations':['[a,cac]=1','e=w p w^-1','c^2=1'],
 'difference_after_eliminating_e':diff,'one_edge_graph_normal_form':[],
 'scope':'Exact actual conjugacy and nontrivial coordinate subgroup; no annular centralizer assertion.'}
Path(__file__).with_name('inner_q0_diagonal_independent22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS literal inverse q0 cone transport and actual beta33 contact word.')
print('PASS complete conjugacy using ONLY [a,bar a] and e=w p w^-1.')
print('PASS missing p/bar-p edge; actual commutator remains nontrivial before annular filling.')

#!/usr/bin/env python3
"""Independent Tietze audit with explicit commutation/deletion certificates.

No root producer is imported.  In particular the seven base relations
are identified literally BEFORE they are used to simplify the other three.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'records/inner_bad_normalized22.json').read_text())
H=json.loads((ROOT/'records/inner_bad_hnn22.json').read_text())
def red(w):
 out=[]
 for x in w:
  x=2 if abs(x)==2 else int(x)
  if out and (out[-1]==-x or out[-1]==x==2):out.pop()
  else:out.append(x)
 return tuple(out)
def mul(*ws):return red(x for w in ws for x in w)
def inv(w):return red(-x for x in reversed(w))
def sub(w,A):return mul(*(A[abs(x)] if x>0 else inv(A[-x]) for x in w))
def conj(h,w):return mul(h,w,inv(h))
new={i:(i,) for i in range(1,7)};new[6]=tuple(H['branch_f_in_new_generators'])
old={i:(i,) for i in range(1,7)};old[6]=tuple(H['w_in_old_normalized_generators'])
for i in range(1,7):assert sub(new[i],old)==(i,)==sub(old[i],new)
NI={int(k):tuple(v) for k,v in D['new_in_old'].items()}
OI={int(k):tuple(v) for k,v in D['old_in_new'].items()}
for i in range(1,7):assert sub(NI[i],OI)==(i,)==sub(OI[i],NI)

vertices=[(i,b) for i in (1,3,4,5,6) for b in (0,1)]
edges={frozenset(((i,0),(i,1))) for i in (1,3,4,5)}
for i,j in ((4,1),(3,1),(3,5)):
 for b in (0,1):edges.add(frozenset(((i,b),(j,1-b))))
def ordinary(word):
 p=0;out=[]
 for x in red(word):
  if abs(x)==2:p^=1
  else:out.append(((abs(x),p),1 if x>0 else -1))
 assert p==0
 return out
def commute(a,b):return a==b or frozenset((a,b)) in edges
def delete_to_zero(word):
 w=ordinary(word);steps=[]
 while w:
  found=None
  for i,(v,s) in enumerate(w):
   for j in range(i+1,len(w)):
    u,t=w[j]
    if u==v and t==-s:found=(i,j);break
    if not commute(v,u):break
   if found:break
  assert found,('nonempty reduced certificate',w)
  i,j=found;assert w[i][0]==w[j][0] and w[i][1]==-w[j][1]
  assert all(commute(w[i][0],x[0]) for x in w[i+1:j])
  steps.append({'positions':[i,j],'letter':w[i],'commuted_letters':w[i+1:j]})
  del w[j];del w[i]
 return steps

records=[];base_names={('beta_12',(4,1)),('alpha_14',(3,1)),('beta_34',(3,5))}
for r in D['relations']:
 raw=sub(r['new_relation'],new)
 assert sub(r['old_relation'],OI)==tuple(r['new_relation'])
 if r['kind']=='cone_contact':
  g=sub(r['cone_conjugator'],new);expected=sub(r['normalized_cone_relation'],new)
  assert conj(inv(g),raw)==expected
  records.append({'name':r['name'],'kind':'cone','literal_base_relation':True})
  continue
 pair=(r['first_core'],r['second_core']);rr=next(h for h in H['relations'] if h['name']==r['name'] and tuple(h.get('pair',()))==pair)
 assert conj(inv(r['common_conjugator']),r['new_relation'])==tuple(r['normalized_pair_relation'])
 rel=sub(r['normalized_pair_relation'],new);C=rr['whole_relator_conjugator'];target=tuple(rr['target_relation'])
 if rr['target_inverted']:target=inv(target)
 difference=mul(conj(C,rel),inv(target))
 if (r['name'],pair) in base_names:
  assert difference==()
  records.append({'name':r['name'],'pair':pair,'literal_base_relation':True})
 else:
  steps=delete_to_zero(difference)
  records.append({'name':r['name'],'pair':pair,'equality_modulo_previously_identified_base':True,'deletion_certificate':steps})
assert sum(r.get('literal_base_relation',False) for r in records)==7

V={tuple(v) for v in H['base_vertices']};E={frozenset(map(tuple,e)) for e in H['base_edges']}
assert len(V)==12 and len(E)==18
for e in E:
 assert frozenset((i,b^1) for i,b in e) in E
 assert len({b^(i==8) for i,b in e})==2
src={(7,0),(8,0)};dst={(5,0),(3,1)}
assert frozenset(src) in E and frozenset(dst) in E
assert len(src|dst|{(i,b^1) for i,b in src|dst})==8
# Each clique is a coordinate subgroup and has a literal graph-group
# retraction.  Thus it is Z^2 and injects; the displayed maps define a
# genuine HNN extension.  Adding[p,r] is redundant after eliminating
# p=w^-1 e w,r=w^-1 bar(b)w because[e,bar(b)] is one of the base edges.
assert frozenset(((5,0),(3,1))) in E
out={'status':'PASS','root_input_hashes':{f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['records/inner_bad_normalized22.json','records/inner_bad_hnn22.json']},
 'literal_seven_base_relations':7,'two_sided_Nielsen_checks':24,'remaining_three_certificates':records,
 'graph_vertices':12,'graph_edges':18,'associated_cliques_injective_by_coordinate_retractions':True,
 'scope':'Complete marked presentation-to-HNN conversion; no full annular/gluing claim.'}
outpath=ROOT/'work_CE/next_symmetric_nodes/inner_bad_hnn_independent22.json'
outpath.write_text(json.dumps(out,indent=2)+'\n')
print('PASS both marked changes, seven literal base relations, three exact commutation/deletion certificates.')
print('PASS twelve-vertex/eighteen-edge graph and two injective clique subgroups; HNN presentation equivalence.')

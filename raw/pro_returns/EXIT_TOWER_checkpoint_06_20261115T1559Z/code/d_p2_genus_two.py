"""Complete local presentations, inverse generators and open-cone data for P2(2,0).
Consumes the independently executed B genus-two face dictionary without altering it.
The word verifier combines the faithful sphere quotient action with Sp4(Z).
"""
from pathlib import Path
import json
from itertools import combinations
from collections import deque
P=Path(__file__).resolve().parent
H={'__file__':str(P/'b_genus2_checks.py')}
exec((P/'b_genus2_checks.py').read_text().split('checks=[')[0],H)
cat,inv=H['cat'],H['inv']
data=json.loads((P/'b_genus2_faces.json').read_text())

def neg(w):return tuple(x[1:] if x.startswith('-') else '-'+x for x in reversed(w))
def rel_eq(a,b):return tuple(a)+neg(tuple(b))
def comm(a,b):return (a,b,'-'+a,'-'+b)
def conjugacy(t,a,w):return rel_eq((t,a,'-'+t),w)
def braid(a,b):return rel_eq((a,b,a),(b,a,b))
def central(z,others):return [comm(z,a) for a in others]
def parse(s):return tuple(s.split())
def group_rels(name):
 if name=='N':
  return [braid('b','d'),braid('d','c'),comm('b','c')]+central('a',('b','d','c'))+[rel_eq(('b','d','c')*4,('a','a')),('W','W')]+central('W',('a','b','d','c'))
 if name=='S':
  h=('a','s')*3;hr=('d','c')*3
  return [braid('a','s'),braid('d','c')]+[comm(x,y) for x in ('a','s') for y in ('d','c')]+[rel_eq(h+h,hr+hr),rel_eq(('W',),h+neg(hr)),('W','W'),('q','q')]+central('W',('a','s','d','c','q'))+[conjugacy('q',x,(y,)) for x,y in [('a','d'),('s','c'),('d','a'),('c','s')]]
 if name in ('H','B'):
  out=[comm(x,y) for x,y in [('a','b'),('a','c'),('a','e'),('b','c'),('b','e')]]+[('e','e'),('W','W')]+central('W',('a','b','c','e'))
  if name=='B':out+=central('W',('t',))+[conjugacy('t',x,(y,)) for x,y in [('a','b'),('b','a'),('c','c')]]+[conjugacy('t','e',('W','c','e','-c')),rel_eq(('t','t'),('c','c'))]
  return out
 if name=='L':return [braid('d','c')]+central('a',('d','c'))+[('W','W')]+central('W',('a','d','c'))
 if name in ('Theta','TB','TN'):
  swaps=[]
  if name in ('Theta','TB'):swaps.append(('u',[('a','b'),('b','a'),('c','c')]))
  if name in ('Theta','TN'):swaps.append(('v',[('a','a'),('b','c'),('c','b')]))
  out=[comm(x,y) for x,y in combinations(('a','b','c'),2)]+[('W','W')]
  for t,pairs in swaps:out+=[(t,t)]+[conjugacy(t,x,(y,)) for x,y in pairs]
  if name=='Theta':out+=[('u','v')*3]
  return out+central('W',('a','b','c')+tuple(t for t,_ in swaps))
 if name in ('AD','D','Z3W'):
  gens=('a','b','c','W') if name=='Z3W' else ('a','c','h','W')
  out=[comm(x,y) for x,y in combinations(gens,2)]+[('W','W')]
  if name=='D':out+=[('t','t'),conjugacy('t','a',('c',)),conjugacy('t','c',('a',)),conjugacy('t','h',('W','h')),comm('t','W')]
  return out
 raise ValueError(name)

groups={}
for cell,z in data['cells'].items():
 name=z['group']
 if name in groups:continue
 gens=z['generators'];rels=group_rels(name)
 for rel in rels:
  word=cat(*(inv(gens[x[1:]]) if x.startswith('-') else gens[x] for x in rel))
  assert H['outer_identity'](word)[0] and H['symplectic'](word)==H['S'].eye(4),(name,rel)
 groups[name]={'generators':gens,'relators':rels}

arrows=data['face_injections'];q={(a['source'],a['target']):tuple(a['transport']) for a in arrows}
adj={c:[] for c in data['cells']}
for (s,t),w in q.items():
 if not w:adj[s].append(t);adj[t].append(s)
seen={'N'};todo=deque(['N']);tree=[]
while todo:
 s=todo.popleft()
 for t in sorted(adj[s]):
  if t not in seen:seen.add(t);todo.append(t);tree.append([s,t])
assert seen==set(adj) and len(tree)==18
inverse=[{'sigma':1,'cell':'N','generator':'a'},
         {'sigma':2,'cell':'S','generator':'s'},
         {'sigma':3,'cell':'N','generator':'b'},
         {'sigma':4,'cell':'N','generator':'d'},
         {'sigma':5,'cell':'N','generator':'c'}]
for x in inverse:assert data['cells'][x['cell']]['generators'][x['generator']]==[x['sigma']]

cone=[]
for tri in data['coherence_triangles']:
 a,b,c=tri['source'],tri['middle'],tri['target']
 left=cat(q[b,c],q[a,b]);right=cat(tri['twist'],q[a,c])
 assert left==right,(a,b,c,left,right)
 cone.append({'flag':[a,b,c,'O'],'formula':'q(b,c) q(a,b) = twist(a,b,c) q(a,c)',
              'left_global_word':left,'right_global_word':right})
assert len(cone)==24
G=json.loads((P/'a_graphs_2_0.json').read_text())
rank_counts={str(r):sum(len(g[2])==r for g in G['graphs']) for r in range(4)}
assert rank_counts=={'0':1,'1':2,'2':2,'3':2}
counts={'cells':19,'vertices':6,'edges':9,'triangles':4,'face_maps':42,
        'generator_images':178,'face_coherences':24,'nontrivial_face_twists':1,
        'local_group_presentations':len(groups),'local_relators':sum(len(z['relators']) for z in groups.values()),
        'maximal_tree_edges':18,'inverse_compact_generators':5,'open_stratum_coherences':24}
out={'type':[2,0],'global_generators':['sigma1','sigma2','sigma3','sigma4','sigma5'],
     'counts':counts,'graph_rank_counts':rank_counts,'groups':groups,**data,
     'counts':counts,'maximal_tree':tree,'inverse_compact_generators':inverse,
     'dimension_three_open_stratum_identities':cone,
     'higher_scope':'These are exact complex-of-groups cocycle identities. A Peiffer expansion in a compact global presentation is not claimed.'}
(P/'d_p2_genus_two.json').write_text(json.dumps(out,indent=2)+'\n')
print('Complete P2(2,0) data:',counts)
print('Stable graph orbit counts by number of curves:',rank_counts)
print('All local relators checked by sphere outer action and Sp4(Z).')
print('The 24 open-stratum coherence identities are freely equal B6 words.')
print('All five compact generators are literal named local generators.')

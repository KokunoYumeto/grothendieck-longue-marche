"""Bounded exact orbit gate for two prescribed S4 zero-direction tuples.
No finite-group census: one successful all-filled tuple, then its four
length-one retained-base translates.  A failure at length one is shortest.
"""
from pathlib import Path
import json,itertools,hashlib
ROOT=Path(__file__).resolve().parents[2];CE=ROOT/'work_CE';P=ROOT/'work_DE/next_marginal_source/complete_pencil_words.json'
D=json.loads(P.read_text());rows={r['name']:r for r in D['loops']}
I=tuple(range(4))
def pm(a,b):return tuple(a[b[i]] for i in range(4))
def pi(a):return tuple(a.index(i) for i in range(4))
def pc(a,b):return pm(pm(a,b),pi(a))
def tr(i,j):
 a=list(I);a[i-1],a[j-1]=a[j-1],a[i-1];return tuple(a)
def act(q,w):
 p=list(q)
 for v in w:
  i=abs(v)-1;a,b=p[i],p[i+1]
  p[i],p[i+1]=(pc(a,b),a) if v>0 else (b,pc(pi(b),a))
 return tuple(p)
def invword(w):return [-x for x in w[::-1]]
def filled(q):
 out=[]
 for r in D['loops']:
  if r['name'].startswith('base'):continue
  a=act(q,r['word'])
  if a!=q:out.append({'name':r['name'],'changed':[i+1 for i in range(20) if a[i]!=q[i]],'after':a})
 return out
initials=[]
for zero in (7,14):
 q=[I]*20;q[zero-1]=tr(1,3);q[8]=tr(1,2);q[9]=q[10]=tr(3,4);q=tuple(q)
 fails=filled(q);initials.append({'zero_index':zero,'generic_tuple':q,'filled_failures':fails})
 print('zero index',zero,'filled failures',[r['name'] for r in fails])
 assert ([r['name'] for r in fails]==([] if zero==7 else ['zero_double_4_constant']))
q=tuple(tuple(a) for a in initials[0]['generic_tuple']);trans=[]
for b in ('base1','base2'):
 for e in (1,-1):
  w=rows[b]['word'] if e==1 else invword(rows[b]['word'])
  p=act(q,w);assert act(p,invword(w))==q
  fails=filled(p)
  inners=[a for a in itertools.permutations(range(4)) if all(pc(a,q[i])==p[i] for i in range(20))]
  trans.append({'base_word':[[b,e]],'tuple':p,'filled_failures':fails,'inner_implementers':inners})
  print('translate',b,e,'filled failures',[r['name'] for r in fails],'inner implementers',len(inners))
assert [r['name'] for r in trans[0]['filled_failures']]==['b_triple_4','special0']
assert not initials[0]['filled_failures'] and trans[0]['filled_failures']
# The translated special-node commutator is a3-cycle; any factor of
# this prescribed S4 head compatible with the full presentation kills A4.
p=trans[0]['tuple'];node_value=pm(pc(p[9],p[10]),pi(p[10]))
assert node_value!=I and pm(pm(node_value,node_value),node_value)==I
conj=[pc(g,node_value) for g in itertools.permutations(range(4))]
normal={I};todo=[I]
while todo:
 a=todo.pop()
 for g in conj:
  v=pm(a,g)
  if v not in normal:normal.add(v);todo.append(v)
assert len(normal)==12
out={'scope':'The x7 tuple satisfies all29 filled monodromies but fails after the shortest retained-base translation of length one. It cannot be coinduced to the actual total pencil.',
 'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'initial_tuples':initials,
 'shortest_depth':1,'length_one_translates':trans,
 'translated_node_value':node_value,'normal_closure_in_S4':sorted(normal),'largest_possible_factor_order':2,
 'convention':'A tuple is q composed with the recorded pullback Artin automorphism. Thus testing beta_d on q composed with beta1 tests the transported variation Phi_beta1(Phi_betad(y_i)y_i^-1).'}
(CE/'zero_direction_monodromy_orbit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: complete29 filled list, literal braid/inverse actions, and all four length-one base translates.')
print('The translated node is a3-cycle with normal closure A4; any compatible factor of this S4 head has order at most2.')
print('NO actual total-group representation follows: the retained-base translates of the special node and fourth b-triple already obstruct this tuple.')

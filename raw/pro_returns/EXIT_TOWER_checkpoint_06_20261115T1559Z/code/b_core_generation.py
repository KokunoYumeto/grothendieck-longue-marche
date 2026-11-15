"""Exact subgroup and relator computation for the sixty quartic core paths.
Uses the proved F3 semidirect F2 normal form and certified weighted Stallings folds.
Every generated element retains its word in the eleven core graph cycles.
"""
from pathlib import Path
from collections import deque
import json
ROOT=Path(__file__).parent
aux={};exec((ROOT/'b_genus_zero.py').read_text().split('\ndata={}')[0],aux)
red,inv,subst,action,A=[aux[k] for k in ('red','inv','subst','action','A')]
D=json.loads((ROOT/'b_core_paths.json').read_text());loops=D['loops']
def C(u,v):return inv(v)+inv(u)+v+u
def conj(u,v):return u+v+inv(u)
x,y,z=(1,),(2,),(3,)
phi=[(inv(z)+x+z,conj(C(x,z),y),C(x,z)+z),(x,inv(z)+y+z,C(y,z)+z)]
base_braids=(A(1,3),A(2,3));fiber_braids=(A(1,4),A(2,4),A(3,4))
phi_inv=[]
for h in base_braids:
 phi_inv.append(tuple(red(k for k in aux['conjugator'](action(4,conj(inv(h),v))[-1],4) if abs(k)!=4) for v in fiber_braids))
for f,g in zip(phi,phi_inv):
 for k in range(1,4):assert subst(subst((k,),f),g)==(k,) and subst(subst((k,),g),f)==(k,)
def apply(b,f):
 for h in reversed(b):f=subst(f,phi[h-1] if h>0 else phi_inv[-h-1])
 return f
def mul(g,h):
 b,f=g;c,k=h
 return red(b+c),red(apply(inv(c),f)+k)
def inverse(g):b,f=g;return inv(b),apply(b,inv(f))
identity=((),())
def val(w,gens):
 out=identity
 for a in w:out=mul(out,gens[a-1] if a>0 else inverse(gens[-a-1]))
 return out
def normal(p):
 b=[];f=[]
 for i,j,s in p:
  if j==3:assert i in(1,2);b.append(i*s)
  elif j==4:assert i in(1,2,3);f.append(i*s)
  else:raise AssertionError((i,j,s))
 return red(b),red(f)
gens=[normal(l['pure']) for l in loops]
# The group arithmetic is cross-checked against the exact braid action.
for g,h,l,m in zip(gens,gens[1:]+gens[:1],loops,loops[1:]+loops[:1]):
 bw=tuple(l['braid'])+tuple(m['braid']);assert mul(g,h)==normal(aux['comb'](4,bw))
 assert mul(g,inverse(g))==identity

class Fold:
 """An inverse-labelled graph; edge weights are words in the original11 cycles."""
 def __init__(self,words):
  self.edges={};self.next_vertex=1;self.next_edge=0
  for lab,weight in words:self.add(lab,weight)
  self.fold()
 def add(self,word,weight):
  word=red(word);weight=red(weight)
  if not word:return
  u=0
  for j,a in enumerate(word):
   v=0 if j==len(word)-1 else self.next_vertex
   if v:self.next_vertex+=1
   w=weight if j==len(word)-1 else ()
   self.edges[self.next_edge]=[u,v,a,w];self.next_edge+=1;u=v
 def oriented(self):
  for eid,(u,v,a,w) in self.edges.items():
   yield eid,u,v,a,w
   yield eid,v,u,-a,inv(w)
 def fold(self):
  while True:
   seen={};pair=None
   for e in self.oriented():
    key=e[1],e[3]
    if key in seen:pair=(seen[key],e);break
    seen[key]=e
   if pair is None:break
   e,f=pair;eid,origin,v,a,alpha=e;fid,_,w,_,beta=f
   assert eid!=fid
   if v!=w:
    if w==0:keep,drop=w,v;connect=red(inv(beta)+alpha)
    else:keep,drop=v,w;connect=red(inv(alpha)+beta)
    for j,(s,t,b,weight) in list(self.edges.items()):
     if s==drop:weight=red(connect+weight);s=keep
     if t==drop:weight=red(weight+inv(connect));t=keep
     self.edges[j]=[s,t,b,weight]
   del self.edges[fid]
 def vertices(self):return {0}|{v for e in self.edges.values() for v in e[:2]}
 def rose(self,rank):
  if self.vertices()!={0}:return None
  d={a:w for _,u,v,a,w in self.oriented() if u==v==0}
  if set(d)!=set(range(1,rank+1))|set(range(-rank,0)):return None
  return tuple(d[i] for i in range(1,rank+1))
 def basis(self):
  adj={v:[] for v in self.vertices()}
  for e in self.oriented():adj[e[1]].append(e)
  paths={0:((),())};tree=set();queue=deque([0])
  while queue:
   u=queue.popleft();lab,wt=paths[u]
   for eid,_,v,a,w in adj[u]:
    if v not in paths:
     paths[v]=(red(lab+(a,)),red(wt+w));tree.add(eid);queue.append(v)
  assert len(paths)==len(adj)
  out=[]
  for eid,(u,v,a,w) in self.edges.items():
   if eid in tree:continue
   lu,wu=paths[u];lv,wv=paths[v]
   out.append((red(lu+(a,)+inv(lv)),red(wu+w+inv(wv))))
  return out
 def certify(self,evaluate):
  for lab,w in self.basis():assert evaluate(w)==lab,(lab,w,evaluate(w))

base_words=[(g[0],(i+1,)) for i,g in enumerate(gens)]
basegraph=Fold(base_words);basegraph.certify(lambda w:val(w,gens)[0])
print('Base image folded graph: vertices',len(basegraph.vertices()),'edges',len(basegraph.edges),flush=True)
lifts=basegraph.rose(2)
assert lifts is not None,'core does not generate the base F2'
la,lb=[val(w,gens) for w in lifts]
assert la[0]==(1,) and lb[0]==(2,)
print('Exact base lifts found; source-word lengths:',[len(w) for w in lifts],flush=True)
initial=[]
for i,g in enumerate(gens):
 wl=red(subst(g[0],lifts));wg=red((i+1,)+inv(wl));k=val(wg,gens)
 assert not k[0]
 initial.append((k[1],wg))
G=Fold(initial);G.certify(lambda w:val(w,gens)[1] if not val(w,gens)[0] else None)
history=[]
for step in range(20):
 history.append(dict(step=step,vertices=len(G.vertices()),edges=len(G.edges),rank=len(G.edges)-len(G.vertices())+1))
 print('Fibre saturation step',step,history[-1],flush=True)
 fw=G.rose(3)
 if fw is not None:break
 current=G.basis();added=list(current)
 for k,w in current:
  for h in (lifts[0],lifts[1],inv(lifts[0]),inv(lifts[1])):
   new=red(h+w+inv(h));g=val(new,gens);assert not g[0]
   added.append((g[1],new))
 G=Fold(added);G.certify(lambda w:val(w,gens)[1] if not val(w,gens)[0] else None)
else:raise AssertionError('fibre saturation has not proved surjectivity')
for j,w in enumerate(fw):assert val(w,gens)==((),(j+1,))
wa=red(lifts[0]+subst(inv(la[1]),fw));wb=red(lifts[1]+subst(inv(lb[1]),fw))
fold_standard=(wa,wb)+fw
expected=(((1,),()),((2,),()),((),(1,)),((),(2,)),((),(3,)))
for w,g in zip(fold_standard,expected):assert val(w,gens)==g
# The computed image table gives the following shorter exact inverse.
standard=((11,),(-11,3,-2),(2,-6,-2),(2,-4,-2),(2,))
for w,g in zip(standard,expected):assert val(w,gens)==g
print('All five standard generators expressed in eleven core loops; lengths:',[len(w) for w in standard],flush=True)
# Complete finite relators on the eleven loops: 11 substitution relators + 6 compact relators.
def targetword(g):return tuple(g[0])+tuple((1 if a>0 else -1)*(abs(a)+2) for a in g[1])
subrels=[]
for j,g in enumerate(gens):
 lifted=red(subst(targetword(g),standard));rel=red((j+1,)+inv(lifted));assert val(rel,gens)==identity
 subrels.append(rel)
compact=json.loads((ROOT/'b_genus_zero.json').read_text())['compact']['M05_relators']
comp_rels=[]
for rel in compact:
 w=red(subst(rel,standard));assert val(w,gens)==identity;comp_rels.append(w)
allrels=[w for w in subrels+comp_rels if w]
assert sum(bool(w) for w in subrels)==6 and len(allrels)==12
edge_basis=[tuple(l['edge_word']) for l in loops]
stdedges=[red(subst(w,edge_basis)) for w in standard]
reledges=[red(subst(w,edge_basis)) for w in allrels]
print('Complete core groupoid relators:',len(allrels),'(6 nonempty substitution +6 compact)',flush=True)
print('Every witness and every relator verified in the exact semidirect normal form.',flush=True)
result=dict(scope='Complete fundamental-groupoid presentation for the 60 explicit K(r) core paths; does not identify the other1560 manuscript arrows.',base_lifts=lifts,fiber_saturation=history,fold_standard_words=fold_standard,standard_generators=['a=A13','b=A23','x=A14','y=A24','z=A34'],standard_words_in_11_loops=standard,standard_words_in_60_edges=stdedges,relators_in_11_loops=allrels,relators_in_60_edges=reledges,core_loop_images=[targetword(g) for g in gens],comparison='Send each of60 arrows to its certified braid path from b_core_paths.json; kill these12 based relators. The standard-generator words give a two-sided inverse on vertex groups.')
(ROOT/'b_core_generation.json').write_text(json.dumps(result,indent=2)+'\n')

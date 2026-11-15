"""Explicit one-node square-triangle families extending the60-path core.
Counts182 objects/360 arrows, with actual plumbing, twist and erasure paths.
This does not assign the tetrahedron-triangle or triple-triangle families.
"""
from pathlib import Path
from collections import deque
import itertools,json
import sympy as S
ROOT=Path(__file__).parent
H={'__file__':str(ROOT/'b_core_paths.py')};exec((ROOT/'b_core_paths.py').read_text().split("\nedges=D['arrows']")[0],H)
Q,Z,zero,one=[H[k] for k in ('Q','Z','zero','one')]
r,I,rt,oo=[H[k] for k in ('r','I','rt','oo')]
curves,bridge,braid_polygon,red,inv,comb,expand,aux=[H[k] for k in ('curves','bridge','braid_polygon','red','inv','comb','expand','aux')]
sim=H['sim'];eps=S.Rational(1,10);eta=Q(S.Rational(1,37));base=(zero,one,(Q(10),Q()),(Q(20),Q()))
D=json.loads((ROOT/'b_quartic.json').read_text());C=json.loads((ROOT/'b_core_paths.json').read_text());G=json.loads((ROOT/'b_core_generation.json').read_text())
perms=tuple(itertools.permutations(range(5)));ident=tuple(range(5))
def comp(p,q):return tuple(p[q[j]] for j in range(5))
def cyc(seq):
 p=list(ident)
 for a,b in zip(seq,seq[1:]+seq[:1]):p[a]=b
 return tuple(p)
def closure(gens):
 got={ident};queue=[ident]
 while queue:
  p=queue.pop()
  for q in gens:
   w=comp(p,q)
   if w not in got:got.add(w);queue.append(w)
 return got
HP=closure([cyc([0,3,1,2,4]),(0,2,1,4,3)])
assert len(HP)==10
left=set(perms);pcos=[];prep={}
while left:
 g=min(left);co={comp(g,h) for h in HP};j=len(pcos);pcos.append(sorted(co));left-=co
 for h in co:prep[h]=j
assert len(pcos)==12

def poly_range(xy,a,b):
 x,y=xy;diffs=(S.Integer(1),x,y,x-1,y-1,x-y);stack=[(a,b)];out=[]
 while stack:
  aa,bb=stack.pop();c=H['rational_mid'](aa,bb);cert=[H['halfplane'](d,aa,bb,c) for d in diffs]
  if all(v is not None for v in cert):out.append((aa,bb,cert))
  else:stack.extend([(c,bb),(aa,c)])
  assert len(out)+len(stack)<1000
 out.sort(key=lambda x:float(S.N(x[0])));knots=[out[0][0]]+[x[1] for x in out]
 configs=[(zero,one,Z(sim(x.subs(r,t))),Z(sim(y.subs(r,t)))) for t in knots]
 cert=[dict(a=str(a),b=str(b),pairs=c) for a,b,c in out]
 return configs,cert

def cfg(xy,t):return zero,one,Z(sim(xy[0].subs(r,t))),Z(sim(xy[1].subs(r,t)))
vertices={int(v):tuple(Z(S.sympify(z)) for z in zs) for v,zs in C['vertices'].items()}
transports={v:braid_polygon(bridge(c,base),eta) for v,c in vertices.items()}
assert all(w is not None for w in transports.values())
xylist=[curves(tuple(e['representative'])) for e in D['arrows']]
for j,xy in enumerate(xylist):
 for v,t in [(62+j,-I*eps),(122+j,eps)]:
  vertices[v]=cfg(xy,t);transports[v]=braid_polygon(bridge(vertices[v],base),eta);assert transports[v] is not None
# The pentagonal endpoint is q=sqrt(5)-2. Its erasure is real, hence no braid crossings.
pent_vertices={};pent_sources={}
for j,(e,xy) in enumerate(zip(D['arrows'],xylist)):
 v=50+prep[tuple(e['representative'])]
 endpoint=tuple(S.simplify(f.subs(r,-I*(S.sqrt(5)-2))) for f in xy)
 if v in pent_vertices:assert all(S.simplify(a-b)==0 for a,b in zip(pent_vertices[v],endpoint))
 else:pent_vertices[v]=endpoint;pent_sources[v]=j;transports[v]=transports[62+j]
 # Along the real erasure no pair collides, so the ordering is constant.
 assert all(S.im(z)==0 for z in endpoint)
 start_order=sorted(range(4),key=lambda k:H['proj'](vertices[62+j][k],eta))
 vals=(S.Integer(0),S.Integer(1))+endpoint
 end_order=sorted(range(4),key=lambda k:float(S.N(vals[k])))
 assert start_order==end_order
assert len(pent_vertices)==12
arrows=[]
for j,e in enumerate(C['arrows']):arrows.append(dict(name='f_Bs',index=j,source=e['source'],target=20+e['target'],braid=e['braid'],pure=e['pure']))
def add(name,j,u,v,raw):
 w=red(transports[u]+raw+inv(transports[v]));assert aux['permutation'](4,w)==(1,2,3,4) and aux['link12'](4,w)==0
 nf=comb(4,w);assert aux['eq'](4,w,expand(nf))
 arrows.append(dict(name=name,index=j,source=u,target=v,braid=w,pure=nf))
for j,e in enumerate(D['arrows']):add('gamma_pent',j,62+j,50+prep[tuple(e['representative'])],())
certificates=[]
for j,xy in enumerate(xylist):
 # q=eps*((1-t)+i*t), the straightened positive quarter turn.
 xyt=tuple(sim(f.subs(r,eps*r-I*eps*(1-r))) for f in xy)
 p,cert=poly_range(xyt,S.Integer(0),S.Integer(1));w=braid_polygon(p,eta);assert w is not None
 assert p[0]==vertices[62+j] and p[-1]==vertices[122+j]
 add('tau_quarter',j,62+j,122+j,w);certificates.append(dict(name='tau_quarter',index=j,intervals=cert))
for j,(e,xy) in enumerate(zip(D['arrows'],xylist)):
 p,cert=poly_range(xy,eps,rt/3);w=braid_polygon(p,eta);assert w is not None
 assert p[0]==vertices[122+j] and p[-1]==vertices[e['source']]
 add('gamma_bipyramid',j,122+j,e['source'],w);certificates.append(dict(name='gamma_bipyramid',index=j,intervals=cert))
# Each f_Q,a is the prescribed erasure followed by the other-apex core path.
for j,e in enumerate(D['arrows']):
 other=[k for k,f in enumerate(D['arrows']) if f['source']==e['source'] and k!=j]
 assert len(other)==2
 for k in other:
  w=red(tuple(arrows[180+j]['braid'])+tuple(arrows[k]['braid']));nf=comb(4,w)
  assert aux['eq'](4,w,expand(nf))
  arrows.append(dict(name='f_Qa',index=[j,k],source=122+j,target=20+D['arrows'][k]['target'],braid=w,pure=nf,composite=[180+j,k]))
assert len(arrows)==360
print('One-node extension objects/arrows:182/360',flush=True)
print('Families:f_Bs60,gamma_pent60,tau_quarter60,gamma_bipyramid60,f_Qa120',flush=True)
print('All240 independent path images and120 composite images exactly verified.',flush=True)
print('Certified rational-path segments:',sum(len(c['intervals']) for c in certificates),flush=True)
# Extend the original tree, without changing its eleven core cycles.
parent=list(range(182))
def find(v):
 while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
 return v
def union(u,v):
 u,v=find(u),find(v)
 if u==v:return False
 parent[v]=u;return True
tree=set(C['tree_edges'])
for j in tree:assert union(arrows[j]['source'],arrows[j]['target'])
for j in range(60,360):
 e=arrows[j]
 if union(e['source'],e['target']):tree.add(j)
assert len(tree)==181 and len({find(j) for j in range(182)})==1
adj={v:[] for v in range(182)}
for j in sorted(tree):
 e=arrows[j];u,v=e['source'],e['target'];adj[u].append((v,j,1));adj[v].append((u,j,-1))
paths={0:()};queue=deque([0])
while queue:
 u=queue.popleft()
 for v,j,s in adj[u]:
  if v not in paths:paths[v]=paths[u]+(s*(j+1),);queue.append(v)
assert len(paths)==182

def edge_expand(w):return red(x for a in w for x in (arrows[a-1]['braid'] if a>0 else inv(arrows[-a-1]['braid'])))
def target(pure):
 lookup={(1,3):1,(2,3):2,(1,4):3,(2,4):4,(3,4):5}
 return tuple(lookup[i,j]*s for i,j,s in pure)
loops=[];relators=[];core_basis=[tuple(l['edge_word']) for l in C['loops']]
std=[tuple(w) for w in G['standard_words_in_11_loops']]
for j,e in enumerate(arrows):
 if j in tree:continue
 ew=paths[e['source']]+(j+1,)+inv(paths[e['target']]);bw=edge_expand(ew);pure=comb(4,bw);tw=target(pure)
 assert aux['eq'](4,bw,expand(pure))
 entry=dict(edge_index=j+1,edge_word=ew,braid=bw,pure=pure,standard_word=tw)
 if j>=60:
  core_word=red(aux['subst'](tw,std));core_edges=red(aux['subst'](core_word,core_basis))
  rel=red(ew+inv(core_edges));assert aux['eq'](4,edge_expand(rel),())
  entry['word_in_core_loops']=core_word;relators.append(rel)
 loops.append(entry)
assert len(loops)==179 and len(relators)==168
relators=[tuple(w) for w in G['relators_in_60_edges']]+relators
assert len(relators)==180
print('Extended spanning tree181 edges; free cycles179; complete relators180.',flush=True)
result=dict(scope='A specified geometric one-node extension of the core; the other1260 source paths remain outside this calculation.',epsilon='1/10',pentagon_parameter='sqrt(5)-2',pentagon_stabilizer=sorted(HP),pentagon_objects=pcos,pentagon_vertices={str(v):[str(x) for x in xy] for v,xy in pent_vertices.items()},pentagon_transport_sources=pent_sources,vertices={str(v):[str(H['zsym'](z)) for z in c] for v,c in vertices.items()},arrows=arrows,certificates=certificates,tree_edges=sorted(tree),loops=loops,relators=relators,counts=[182,360,179,180])
out=ROOT/'b_first_tier.json';tmp=out.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)

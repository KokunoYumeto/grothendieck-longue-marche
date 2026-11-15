"""A specified two-node plumbing realization of six triple-triangle families.

This is an explicit geometric extension, with the erasure conventions stated
in the paper. It does not assign the tetrahedron-triangle families. Exact
Sturm certificates compare normalized rational curves with polygons; exact
quadratic-field crossing arithmetic and Artin combing verify every word.
"""
from pathlib import Path
from collections import deque, Counter
import itertools,json,time
import sympy as S
ROOT=Path(__file__).parent
H={'__file__':str(ROOT/'b_core_paths.py')}
exec((ROOT/'b_core_paths.py').read_text().split("\nedges=D['arrows']")[0],H)
Q,Z,zero,one=[H[k] for k in ('Q','Z','zero','one')]
r,I,oo=[H[k] for k in ('r','I','oo')]
bridge,braid_polygon,red,inv,comb,expand,aux=[H[k] for k in ('bridge','braid_polygon','red','inv','comb','expand','aux')]
sim=H['sim'];eps=S.Rational(1,10);eta=Q(S.Rational(1,37))
base=(zero,one,(Q(10),Q()),(Q(20),Q()))
C=json.loads((ROOT/'b_core_paths.json').read_text())
T=json.loads((ROOT/'b_first_tier.json').read_text())
G=json.loads((ROOT/'b_core_generation.json').read_text())
D=json.loads((ROOT/'b_quartic.json').read_text())
perms=tuple(itertools.permutations(range(5)));ident=tuple(range(5))
h=(0,2,1,4,3)
def comp(p,q):return tuple(p[q[j]] for j in range(5))
def prelabel(points,p):return tuple(points[p.index(j)] for j in range(5))
def normalized(points):
 return tuple(H['cr'](points[j],points[0],points[1],points[4]) for j in (2,3))
def canon(p):return min(p,comp(p,h))
cosets=sorted({canon(p) for p in perms});coset_index={p:i for i,p in enumerate(cosets)}
assert len(cosets)==60
core_coset_index={tuple(e['representative']):i for i,e in enumerate(D['arrows'])}
assert set(core_coset_index)==set(cosets)
qcos={tuple(p):j for j,co in enumerate(D['target_objects']) for p in co}

# Labels: node clusters A={1,3}, B={2,4}; central marked point 0.
R=(oo,-1-eps,1+eps,-1+eps,1-eps)
M=(oo,-1-I*eps,1+eps,-1+I*eps,1-eps)
L=(oo,-1-I*eps,1+I*eps,-1+I*eps,1-I*eps)
def aut(points):
 xy=normalized(points)
 return tuple(p for p in perms if all(sim(a-b)==0 for a,b in zip(xy,normalized(prelabel(points,p)))))
assert set(aut(R))=={ident,h}
assert aut(M)==(ident,)
assert set(aut(L))=={ident,h}
print('Triple-triangle stabilizers:2,1,2; object counts60,120,60.',flush=True)

def poly_range(xy):
 x,y=xy;diffs=(S.Integer(1),x,y,x-1,y-1,x-y)
 stack=[(S.Integer(0),S.Integer(1))];out=[]
 while stack:
  a,b=stack.pop();c=(a+b)/2
  cert=[H['halfplane'](d,a,b,c) for d in diffs]
  if all(z is not None for z in cert):out.append((a,b,cert))
  else:stack.extend([(c,b),(a,c)])
  assert len(stack)+len(out)<200
 out.sort(key=lambda x:x[0]);knots=[out[0][0]]+[v[1] for v in out]
 configs=[(zero,one,Z(sim(x.subs(r,t))),Z(sim(y.subs(r,t)))) for t in knots]
 return configs,[dict(a=str(a),b=str(b),pairs=c) for a,b,c in out]

vertices={int(v):tuple(Z(S.sympify(z)) for z in zs) for v,zs in T['vertices'].items()}
transports={v:braid_polygon(bridge(c,base),eta) for v,c in vertices.items()}
for v,j in T['pentagon_transport_sources'].items():transports[int(v)]=transports[62+int(j)]
assert all(w is not None for w in transports.values())
def add_vertices(offset,ps,model):
 for j,p in enumerate(ps):
  xy=normalized(prelabel(model,p));cfg=(zero,one,Z(xy[0]),Z(xy[1]))
  vertices[offset+j]=cfg;transports[offset+j]=braid_polygon(bridge(cfg,base),eta)
  assert transports[offset+j] is not None
add_vertices(182,cosets,R)
add_vertices(242,perms,M)
add_vertices(362,cosets,L)
assert len(vertices)==410 # The twelve pentagons are retained separately.
rid=lambda p:182+coset_index[canon(p)]
mid=lambda p:242+perms.index(p)
lid=lambda p:362+coset_index[canon(p)]
ii=lambda p:62+core_coset_index[canon(p)]
iip=lambda p:122+core_coset_index[canon(p)]
qq=lambda p:20+qcos[p]

# Positive rotations, straightened within the two disjoint node discs.
turnA=(oo,-1-eps*(1-r+I*r),1+eps,-1+eps*(1-r+I*r),1-eps)
turnB=(oo,-1-I*eps,1+eps*(1-r+I*r),-1+I*eps,1-eps*(1-r+I*r))
# Real chamber erasure. This target is -1/(z+1) applied to pR.V(eps).
pR=(2,1,3,0,4)
Rtarget=(oo,-1/(1-eps),S.Integer(0),-1/(1+eps),-S.Rational(1,2))
eraseR=tuple(oo if a==oo else sim((1-r)*a+r*b) for a,b in zip(R,Rtarget))
# The other erasures carry the retained A-tail; q_B grows while its centre moves.
pM=(0,1,3,4,2)
eraseM=(oo,-(1-r)-I*eps,(1-r)+(eps+(1-eps)*r),-(1-r)+I*eps,(1-r)-(eps+(1-eps)*r))
eraseL=(oo,-(1-r)-I*eps,(1-r)+I*(eps+(1-eps)*r),-(1-r)+I*eps,(1-r)-I*(eps+(1-eps)*r))
pQ=(0,4,3,1,2)
eraseBoth=(oo,-1-I*(eps+(1-eps)*r),1+I*(eps+(1-eps)*r),-1+I*(eps+(1-eps)*r),1-I*(eps+(1-eps)*r))
families=[
 ('tau_pi_rho',perms,turnA,rid,mid),
 ('gamma_pi_rho',perms,eraseR,rid,lambda p:ii(comp(p,pR))),
 ('tau_r_1',perms,turnB,mid,lid),
 ('gamma_r_1',perms,eraseM,mid,lambda p:iip(comp(p,pM))),
 ('gamma_r_2',perms,eraseL,lid,lambda p:ii(comp(p,pM))),
 ('gamma_r_2prime',cosets,eraseBoth,lid,lambda p:qq(comp(p,pQ))),
]
arrows=list(T['arrows']);certificates=[]
for name,ps,model,source,target in families:
 for j,p in enumerate(ps):
  xy=normalized(prelabel(model,p));poly,cert=poly_range(xy)
  u,v=source(p),target(p)
  assert poly[0]==vertices[u],(name,j,'source')
  assert poly[-1]==vertices[v],(name,j,'target')
  raw=braid_polygon(poly,eta)
  if raw is None:raise AssertionError((name,j,'projection degeneracy'))
  w=red(transports[u]+raw+inv(transports[v]))
  assert aux['permutation'](4,w)==(1,2,3,4) and aux['link12'](4,w)==0
  nf=comb(4,w);assert aux['eq'](4,w,expand(nf))
  arrows.append(dict(name=name,index=j,representative=p,source=u,target=v,braid=w,pure=nf))
  certificates.append(dict(name=name,index=j,intervals=cert))
 print(name,len(ps),'exact path images verified',flush=True)
assert len(arrows)==1020
print('Two-node extension:422 objects,1020 arrows.',flush=True)
print('New rational segments:',sum(len(c['intervals']) for c in certificates),flush=True)

# Preserve the old spanning tree and extend it greedily by the new arrows.
parent=list(range(422))
def find(v):
 while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
 return v
def union(u,v):
 u,v=find(u),find(v)
 if u==v:return False
 parent[v]=u;return True
tree=set(T['tree_edges'])
for j in tree:assert union(arrows[j]['source'],arrows[j]['target'])
for j in range(360,1020):
 e=arrows[j]
 if union(e['source'],e['target']):tree.add(j)
assert len(tree)==421 and len({find(j) for j in range(422)})==1
adj={v:[] for v in range(422)}
for j in sorted(tree):
 e=arrows[j];u,v=e['source'],e['target'];adj[u].append((v,j,1));adj[v].append((u,j,-1))
paths={0:()};queue=deque([0])
while queue:
 u=queue.popleft()
 for v,j,s in adj[u]:
  if v not in paths:paths[v]=paths[u]+(s*(j+1),);queue.append(v)
def edge_expand(w):return red(x for a in w for x in (arrows[a-1]['braid'] if a>0 else inv(arrows[-a-1]['braid'])))
def target_word(pure):
 lookup={(1,3):1,(2,3):2,(1,4):3,(2,4):4,(3,4):5}
 return tuple(lookup[i,j]*s for i,j,s in pure)
std=[tuple(w) for w in G['standard_words_in_11_loops']]
core_basis=[tuple(l['edge_word']) for l in C['loops']]
loops=list(T['loops']);relators=list(T['relators'])
for j in range(360,1020):
 if j in tree:continue
 e=arrows[j];ew=paths[e['source']]+(j+1,)+inv(paths[e['target']])
 bw=edge_expand(ew);nf=comb(4,bw);tw=target_word(nf)
 cw=red(aux['subst'](tw,std));ce=red(aux['subst'](cw,core_basis))
 rel=red(ew+inv(ce));assert aux['eq'](4,edge_expand(rel),())
 loops.append(dict(edge_index=j+1,edge_word=ew,braid=bw,pure=nf,standard_word=tw,word_in_core_loops=cw))
 relators.append(rel)
assert len(loops)==599 and len(relators)==600
print('Free cycles599; complete relators600; all420 new relations verified.',flush=True)
result=dict(scope='Specified two-node plumbing extension. The three tetrahedron-triangle families (600 arrows) remain unassigned. Original finite erasure conventions are retained as a separate comparison question.',epsilon=str(eps),models={k:[str(x) for x in v] for k,v in [('III2',R),('III1',M),('IIIp2',L)]},endpoint_permutations={'gamma_pi_rho':pR,'gamma_r_1':pM,'gamma_r_2':pM,'gamma_r_2prime':pQ},vertices={str(v):[str(H['zsym'](z)) for z in c] for v,c in vertices.items()},arrows=arrows,certificates=certificates,tree_edges=sorted(tree),loops=loops,relators=relators,counts=[422,1020,599,600])
out=ROOT/'b_second_tier.json';tmp=out.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)

"""Exact geometric realization of all 542/1620 incidences.

The three tetrahedral erasure choices are explicitly the positive cyclic
choices in the real component, with their pin convention recorded below.
This does not silently identify an absent manuscript path convention.
"""
from pathlib import Path
from collections import deque,Counter
from math import comb as choose
import itertools,json
import sympy as S
ROOT=Path(__file__).parent
H={'__file__':str(ROOT/'b_core_paths.py')}
exec((ROOT/'b_core_paths.py').read_text().split("\nedges=D['arrows']")[0],H)
Q,Z,zero,one=[H[k] for k in ('Q','Z','zero','one')]
r,I,rt,oo=[H[k] for k in ('r','I','rt','oo')]
bridge,braid_polygon,red,inv,comb,expand,aux=[H[k] for k in ('bridge','braid_polygon','red','inv','comb','expand','aux')]
sim=H['sim'];eps=S.Rational(1,10);eta=Q(S.Rational(1,37))
base=(zero,one,(Q(10),Q()),(Q(20),Q()))
C=json.loads((ROOT/'b_core_paths.json').read_text())
T=json.loads((ROOT/'b_first_tier.json').read_text())
U=json.loads((ROOT/'b_second_tier.json').read_text())
G=json.loads((ROOT/'b_core_generation.json').read_text())
D=json.loads((ROOT/'b_quartic.json').read_text())
perms=tuple(itertools.permutations(range(5)));ident=tuple(range(5))
def comp(p,q):return tuple(p[q[j]] for j in range(5))
def prelabel(points,p):return tuple(points[p.index(j)] for j in range(5))
def normalized(points):return tuple(H['cr'](points[j],points[0],points[1],points[4]) for j in (2,3))
zeta=(-1+I*rt)/2;zeta6=(1+I*rt)/2
W=(S.Integer(1),zeta,zeta**2,-1/eps,1/eps)
M=(oo,-1-I*eps,1+eps,-1+I*eps,1-eps)
ptau=(1,2,0,4,3)
p0=(0,1,3,4,2);cc=(2,1,4,3,0)
ps=[p0,comp(cc,p0),comp(cc,comp(cc,p0))]
xyW=normalized(W)
auts=[p for p in perms if all(sim(a-b)==0 for a,b in zip(xyW,normalized(prelabel(W,p))))]
assert auts==[ident]
print('Tetrahedron-triangle configuration has trivial labelled stabilizer:120 objects.',flush=True)

def bernstein(poly,a,b):
 """Exact Bernstein coefficients in the specified real embedding of Q(sqrt3)."""
 t=S.symbols('t',real=True)
 p=S.Poly(S.expand(poly.as_expr().subs(r,a+(b-a)*t)),t,extension=rt)
 n=p.degree();power=[Q.of(p.nth(k)) for k in range(n+1)]
 coeff=[]
 for k in range(n+1):
  val=Q()
  for j in range(k+1):val+=power[j]*S.Rational(choose(k,j),choose(n,j))
  coeff.append(val)
 return coeff
def encq(q):return [str(q.a),str(q.b)]
def positive_certificate(d,a,b,c):
 dc=sim(d.subs(r,c));f=H['re'](d*S.conjugate(dc));num,den=S.fraction(f)
 n=S.Poly(num,r,extension=rt);h=S.Poly(den,r,extension=rt)
 if n.is_zero or h.is_zero:return None
 bn=bernstein(n,a,b);bh=bernstein(h,a,b)
 sn={v.sign() for v in bn};sh={v.sign() for v in bh}
 if sn not in ({1},{-1}) or sh!=sn:return None
 return dict(n=str(n.as_expr()),d=str(h.as_expr()),n_Bernstein=[encq(x) for x in bn],d_Bernstein=[encq(x) for x in bh],interval=[str(a),str(b)],center=str(c))
def poly_range(xy):
 x,y=xy;diffs=(S.Integer(1),x,y,x-1,y-1,x-y)
 stack=[(S.Integer(0),S.Integer(1))];out=[]
 while stack:
  a,b=stack.pop();c=(a+b)/2
  cert=[positive_certificate(d,a,b,c) for d in diffs]
  if all(z is not None for z in cert):out.append((a,b,cert))
  else:stack.extend([(c,b),(a,c)])
  assert len(stack)+len(out)<300
 out.sort(key=lambda x:x[0]);knots=[out[0][0]]+[v[1] for v in out]
 configs=[(zero,one,Z(sim(x.subs(r,t))),Z(sim(y.subs(r,t)))) for t in knots]
 return configs,[dict(a=str(a),b=str(b),pairs=c) for a,b,c in out]

# A single homogeneous-determinant certificate handles all120 relabellings.
# A normalized pair difference is a product of three nonzero determinants
# divided by three. Each determinant is kept within pi/12 of its midpoint
# ray; hence every normalized difference stays within pi/2 of its midpoint.
from fractions import Fraction as F
def ca(z,w):return z[0]+w[0],z[1]+w[1]
def cn(z):return -z[0],-z[1]
def cs(z,w):return ca(z,cn(w))
def cm(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def cj(z):return z[0],-z[1]
def sc(z,a):return z[0]*a,z[1]*a
def cd(z,w):
 n=w[0]*w[0]+w[1]*w[1]
 return sc(cm(z,cj(w)),Q(1)/n)
def compile_poly(z):
 p=S.Poly(S.expand(z),r)
 return tuple(Z(p.nth(j)) for j in range(max(0,p.degree())+1))
def evaluate(poly,t):
 z=zero
 for c0 in reversed(poly):z=ca(sc(z,t),c0)
 return z
def bernstein_complex(poly,a,b):
 n=len(poly)-1;power=[]
 for j in range(n+1):
  z=zero
  for k in range(j,n+1):z=ca(z,sc(poly[k],Q(choose(k,j))*Q(a**(k-j))*Q((b-a)**j)))
  power.append(z)
 return [sum_complex(sc(power[j],Q(F(choose(k,j),choose(n,j)))) for j in range(k+1)) for k in range(n+1)]
def sum_complex(zs):
 z=zero
 for w in zs:z=ca(z,w)
 return z
def encode_complex(z):return [encq(z[0]),encq(z[1])]
def universal_polygon(hom):
 coords=[(compile_poly(x),compile_poly(y)) for x,y in hom]
 dets=[]
 for i,j in itertools.combinations(range(5),2):
  dets.append((i,j,compile_poly(S.expand(hom[i][0]*hom[j][1]-hom[j][0]*hom[i][1]))))
 stack=[(F(0),F(1))];out=[];bound=Q(2,-1)
 while stack:
  a,b=stack.pop();m=(a+b)/2;cert=[];ok=True
  for i,j,poly in dets:
   center=evaluate(poly,Q(m));coeff=bernstein_complex(poly,a,b)
   for z in coeff:
    x,y=cm(z,cj(center))
    if min(x.sign(),(bound*x+y).sign(),(bound*x-y).sign())<=0:ok=False;break
   if not ok:break
   cert.append(dict(pair=[i,j],midpoint_value=encode_complex(center),Bernstein=[encode_complex(z) for z in coeff]))
  if ok:out.append((a,b,cert))
  else:stack.extend([(m,b),(a,m)])
  assert len(stack)+len(out)<1000
 out.sort(key=lambda x:x[0]);knots=[out[0][0]]+[x[1] for x in out]
 points=[tuple((evaluate(x,Q(t)),evaluate(y,Q(t))) for x,y in coords) for t in knots]
 return points,[dict(a=str(a),b=str(b),pairs=c) for a,b,c in out]
def normalized_homogeneous(points,p):
 vv=prelabel(points,p)
 def det(i,j):return cs(cm(vv[i][0],vv[j][1]),cm(vv[j][0],vv[i][1]))
 xy=tuple(cd(cm(det(j,0),det(1,4)),cm(det(j,4),det(1,0))) for j in (2,3))
 return (zero,one)+xy

vertices={int(v):tuple(Z(S.sympify(z)) for z in zs) for v,zs in U['vertices'].items()}
transports={v:braid_polygon(bridge(c,base),eta) for v,c in vertices.items()}
for v,j in T['pentagon_transport_sources'].items():transports[int(v)]=transports[62+int(j)]
for j,p in enumerate(perms):
 xy=normalized(prelabel(W,p));cfg=(zero,one,Z(xy[0]),Z(xy[1]))
 vertices[422+j]=cfg;transports[422+j]=braid_polygon(bridge(cfg,base),eta)
assert all(v is not None for v in transports.values())
wid=lambda p:422+perms.index(p)
mid=lambda p:242+perms.index(p)
bcos={tuple(p):j for j,co in enumerate(D['source_objects']) for p in co}
q=eps*((1-r)+zeta6*r)
twist=(S.Integer(1),zeta,zeta**2,-1/q,1/q)
erasure=(S.Integer(1),zeta,zeta**2,-(1-r)/eps,1/(eps*(1-r)))
lam0=sim(H['cr'](M[1],M[0],M[2],M[4]))
assert S.simplify(lam0-(-19+I)/181)==0
real_models=[];end_lambdas=[]
for p in ps:
 v=prelabel(W,p);lam1=sim(H['cr'](v[1],v[0],v[2],v[4]))
 assert Q.of(H['im'](lam1)).sign()>0
 lam=sim((1-r)*lam0+r*lam1)
 real_models.append((S.Integer(0),lam,S.Integer(1),S.conjugate(lam),oo))
 end_lambdas.append(lam1)
assert Q.of(H['re'](end_lambdas[0])).sign()<0
arrows=list(U['arrows']);certificates=[]
hom_twist=[(S.Integer(1),S.Integer(1)),(zeta,S.Integer(1)),(zeta**2,S.Integer(1)),(-S.Integer(1),q),(S.Integer(1),q)]
hom_erasure=[(S.Integer(1),S.Integer(1)),(zeta,S.Integer(1)),(zeta**2,S.Integer(1)),(-(1-r),eps),(S.Integer(1),eps*(1-r))]
families=[('tau_r_0',hom_twist,wid,lambda p:wid(comp(p,ptau))),('gamma_r_0',hom_erasure,wid,lambda p:bcos[p])]
for j,model in enumerate(real_models):
 hom=[(S.Integer(1),S.Integer(0)) if z==oo else (z,S.Integer(1)) for z in model]
 families.append(('gamma_r_1prime_'+str(j),hom,mid,lambda p,j=j:wid(comp(p,ps[j]))))
for name,hom,source,target in families:
 points,cert=universal_polygon(hom)
 certificates.append(dict(name=name,universal_for=120,intervals=cert))
 print(name,'universal determinant certificate:',len(cert),'intervals',flush=True)
 for j,p in enumerate(perms):
  poly=[normalized_homogeneous(pt,p) for pt in points]
  u,v=source(p),target(p)
  assert poly[0]==vertices[u],(name,j,'source')
  assert poly[-1]==vertices[v],(name,j,'target')
  raw=braid_polygon(poly,eta)
  assert raw is not None,(name,j,'projection')
  w=red(transports[u]+raw+inv(transports[v]));assert aux['permutation'](4,w)==(1,2,3,4) and aux['link12'](4,w)==0
  nf=comb(4,w);assert aux['eq'](4,w,expand(nf))
  arrows.append(dict(name=name,index=j,representative=p,source=u,target=v,braid=w,pure=nf))
 print(name,'120 exact path images verified',flush=True)
assert len(arrows)==1620 and len(vertices)==530
print('Full specified realization:542 objects,1620 arrows.',flush=True)
print('Universal exact determinant-certified subintervals:',sum(len(c['intervals']) for c in certificates),flush=True)
# Attach every new vertex by its j=0 one-node erasure. This is a bijection.
tree=set(U['tree_edges'])|set(range(1260,1380))
assert len(tree)==541
adj={v:[] for v in range(542)}
for j in sorted(tree):
 e=arrows[j];u,v=e['source'],e['target'];adj[u].append((v,j,1));adj[v].append((u,j,-1))
paths={0:()};queue=deque([0])
while queue:
 u=queue.popleft()
 for v,j,s in adj[u]:
  if v not in paths:paths[v]=paths[u]+(s*(j+1),);queue.append(v)
assert len(paths)==542
def edge_expand(w):return red(x for a in w for x in (arrows[a-1]['braid'] if a>0 else inv(arrows[-a-1]['braid'])))
def target_word(pure):
 lookup={(1,3):1,(2,3):2,(1,4):3,(2,4):4,(3,4):5}
 return tuple(lookup[i,j]*s for i,j,s in pure)
std=[tuple(w) for w in G['standard_words_in_11_loops']]
core_basis=[tuple(l['edge_word']) for l in C['loops']]
loops=list(U['loops']);relators=list(U['relators'])
for j in range(1020,1620):
 if j in tree:continue
 e=arrows[j];ew=paths[e['source']]+(j+1,)+inv(paths[e['target']]);bw=edge_expand(ew)
 nf=comb(4,bw);tw=target_word(nf);cw=red(aux['subst'](tw,std));ce=red(aux['subst'](cw,core_basis))
 rel=red(ew+inv(ce));assert aux['eq'](4,edge_expand(rel),())
 loops.append(dict(edge_index=j+1,edge_word=ew,braid=bw,pure=nf,standard_word=tw,word_in_core_loops=cw));relators.append(rel)
assert len(loops)==1079 and len(relators)==1080
print('Free cycles1079; complete relators1080; all480 new relations verified.',flush=True)
print('Relative-one dictionary uses60 core paths and541 tree edges; new120 tree edges are gamma_r_1prime_0.',flush=True)
result=dict(scope='Complete specified geometric realization of the542/1620 endpoint counts. The direct f_Qa and three tetrahedral erasure conventions are explicit; no unrecorded manuscript homotopy is identified by count alone.',epsilon=str(eps),tetrahedral_model=[str(x) for x in W],tau_endpoint_permutation=ptau,tetrahedral_erasure_endpoint_permutations=ps,real_source_lambda=str(lam0),real_target_lambdas=[str(x) for x in end_lambdas],vertices={str(v):[str(H['zsym'](z)) for z in c] for v,c in vertices.items()},arrows=arrows,certificates=certificates,tree_edges=sorted(tree),tree_paths={str(v):w for v,w in paths.items()},loops=loops,relators=relators,counts=[542,1620,1079,1080])
out=ROOT/'b_third_tier.json';tmp=out.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)

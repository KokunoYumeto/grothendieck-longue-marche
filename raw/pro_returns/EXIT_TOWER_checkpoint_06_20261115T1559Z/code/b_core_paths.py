"""Certified braid images of the sixty explicit quartic-family core paths.
No manuscript gamma path is inferred from endpoint data.
Homotopies from rational paths to polygons are certified by exact Sturm tests.
All polygon crossing times and signs are computed in Q(sqrt(3)).
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,math
import sympy as S
from collections import deque
ROOT=Path(__file__).parent
aux={};exec((ROOT/'b_genus_zero.py').read_text().split('\ndata={}')[0],aux)
red,inv,comb,expand,action=[aux[k] for k in ('red','inv','comb','expand','action')]
D=json.loads((ROOT/'b_quartic.json').read_text())
r=S.symbols('r',real=True);I=S.I;oo=S.oo;rt=S.sqrt(3)
def sim(z):return S.cancel(z)
def cr(z,a,b,c):
 if z==c:return oo
 if a==oo:return sim((b-c)/(z-c))
 if b==oo:return sim((z-a)/(z-c))
 if c==oo:return sim((z-a)/(b-a))
 if z==oo:return sim((b-c)/(b-a))
 return sim((z-a)*(b-c)/((z-c)*(b-a)))
def curves(p):
 qi=[p.index(j) for j in range(5)]
 v=[(oo,-I*r,I*r,-S.Integer(1),S.Integer(1))[qi[j]] for j in range(5)]
 return tuple(cr(v[j],v[0],v[1],v[4]) for j in (2,3))
def re(z):return S.cancel(S.expand_complex(z).as_real_imag()[0])
def im(z):return S.cancel(S.expand_complex(z).as_real_imag()[1])
def sg(z):return int(S.sign(S.simplify(z)))
# Real quadratic field, ordered exactly.
class Q:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):self.a=F(a);self.b=F(b)
 @staticmethod
 def of(z):
  z=S.radsimp(S.simplify(z)).expand()
  b=z.coeff(rt);a=z-b*rt
  assert a.is_Rational and b.is_Rational,(z,a,b)
  return Q(F(int(a.p),int(a.q)),F(int(b.p),int(b.q)))
 @staticmethod
 def co(z):return z if isinstance(z,Q) else Q(z)
 def __add__(self,z):z=Q.co(z);return Q(self.a+z.a,self.b+z.b)
 __radd__=__add__
 def __neg__(self):return Q(-self.a,-self.b)
 def __sub__(self,z):return self+-Q.co(z)
 def __rsub__(self,z):return Q.co(z)+-self
 def __mul__(self,z):z=Q.co(z);return Q(self.a*z.a+3*self.b*z.b,self.a*z.b+self.b*z.a)
 __rmul__=__mul__
 def __truediv__(self,z):
  z=Q.co(z);d=z.a*z.a-3*z.b*z.b
  return Q((self.a*z.a-3*self.b*z.b)/d,(self.b*z.a-self.a*z.b)/d)
 def sign(self):
  a,b=self.a,self.b
  if not b:return (a>0)-(a<0)
  if not a:return (b>0)-(b<0)
  if (a>0)==(b>0):return 1 if a>0 else -1
  d=a*a-3*b*b
  return ((a>0)-(a<0)) if d>0 else ((b>0)-(b<0))
 def __eq__(self,z):z=Q.co(z);return self.a==z.a and self.b==z.b
 def __lt__(self,z):return (self-Q.co(z)).sign()<0
 def __le__(self,z):return (self-Q.co(z)).sign()<=0
 def __hash__(self):return hash((self.a,self.b))
 def __repr__(self):return '%s+(%s)*sqrt(3)'%(self.a,self.b)
 def sym(self):return S.Rational(self.a.numerator,self.a.denominator)+S.Rational(self.b.numerator,self.b.denominator)*rt
 def __float__(self):return float(self.a)+float(self.b)*math.sqrt(3)
def Z(z):return Q.of(re(z)),Q.of(im(z))
def za(z,w):return z[0]+w[0],z[1]+w[1]
def zs(z,w):return z[0]-w[0],z[1]-w[1]
def zm(t,z):return t*z[0],t*z[1]
def zsym(z):return z[0].sym()+I*z[1].sym()
def proj(z,eta):return z[0]+eta*z[1]
def perp(z,eta):return z[1]-eta*z[0]
zero=(Q(),Q());one=(Q(1),Q())
# Half-plane certificates for the polygonal homotopies.
def rational_mid(a,b):
 if a==rt/3 and b==1:return S.Rational(3,4)
 f=F((float(S.N(a))+float(S.N(b)))/2).limit_denominator(10**7)
 x=S.Rational(f.numerator,f.denominator)
 assert sg(x-a)>0 and sg(b-x)>0
 return x
def enclosing(a,b):
 if a==rt/3 and b==1:return S.Rational(1,2),S.Integer(1)
 den=2**24;lo=S.Rational(math.floor(float(S.N(a))*den),den);hi=S.Rational(math.ceil(float(S.N(b))*den),den)
 while sg(a-lo)<0:lo-=S.Rational(1,den)
 while sg(hi-b)<0:hi+=S.Rational(1,den)
 return lo,hi
def halfplane(d,a,b,c):
 dc=sim(d.subs(r,c));f=re(d*S.conjugate(dc));n,h=S.fraction(f)
 n=S.Poly(n,r,domain=S.QQ);h=S.Poly(h,r,domain=S.QQ);lo,hi=enclosing(a,b)
 if n.is_zero or h.is_zero:return None
 if n.count_roots(lo,hi) or h.count_roots(lo,hi):return None
 assert sg(f.subs(r,c))>0
 return dict(n=str(n.as_expr()),d=str(h.as_expr()),interval=[str(lo),str(hi)],center=str(c))
def certified_polygon(xy):
 x,y=xy;diffs=(S.Integer(1),x,y,x-1,y-1,x-y)
 stack=[(rt/3,S.Integer(1))];out=[]
 while stack:
  a,b=stack.pop();c=rational_mid(a,b);cert=[halfplane(d,a,b,c) for d in diffs]
  if all(t is not None for t in cert):out.append((a,b,cert))
  else:stack.extend([(c,b),(a,c)])
  assert len(out)+len(stack)<1000
 out.sort(key=lambda v:float(S.N(v[0])))
 knots=[out[0][0]]+[v[1] for v in out]
 configs=[(zero,one,Z(sim(x.subs(r,t))),Z(sim(y.subs(r,t)))) for t in knots]
 return configs,dict(intervals=[dict(a=str(a),b=str(b),pairs=c) for a,b,c in out])
def clear_segment(u,v,obstacles):
 d=zs(v,u)
 if d==zero:return True
 for p in obstacles:
  e=zs(p,u)
  if (d[0]*e[1]-d[1]*e[0]).sign()==0:
   t=e[0]/d[0] if d[0]!=0 else e[1]/d[1]
   if Q(0)<=t<=Q(1):return False
 return True
def detour(u,v,obstacles):
 if u==v:return [u]
 for n in range(2,1000):
  q=(Q(n),Q(n*n))
  if clear_segment(u,q,obstacles) and clear_segment(q,v,obstacles):return [u,q,v]
 raise AssertionError('no detour')
def bridge(config,base):
 out=[base];x,y=config[2:]
 for z in detour(base[2],x,(zero,one,base[3]))[1:]:out.append((zero,one,z,base[3]))
 for z in detour(base[3],y,(zero,one,x))[1:]:out.append((zero,one,x,z))
 assert out[-1]==config
 return out

def braid_polygon(configs,eta):
 word=[]
 for U,V in zip(configs,configs[1:]):
  order=sorted(range(4),key=lambda j:proj(U[j],eta))
  if any(proj(U[order[j]],eta)==proj(U[order[j+1]],eta) for j in range(3)):return None
  if any(proj(V[j],eta)==proj(V[k],eta) for j,k in itertools.combinations(range(4),2)):return None
  events=[]
  for j,k in itertools.combinations(range(4),2):
   a=proj(zs(U[j],U[k]),eta);b=proj(zs(V[j],V[k]),eta)
   if a==b:continue
   t=-a/(b-a)
   if Q(0)<t<Q(1):events.append((t,j,k))
  events.sort()
  for idx,(t,j,k) in enumerate(events):
   if idx and events[idx-1][0]==t and len({j,k,events[idx-1][1],events[idx-1][2]})<4:return None
   loc=sorted((order.index(j),order.index(k)))
   assert loc[1]==loc[0]+1,(loc,order,events)
   left,right=order[loc[0]],order[loc[1]]
   L=za(U[left],zm(t,zs(V[left],U[left])))
   R=za(U[right],zm(t,zs(V[right],U[right])))
   s=-perp(zs(L,R),eta).sign();assert s
   word.append(s*(loc[0]+1));order[loc[0]],order[loc[1]]=order[loc[1]],order[loc[0]]
  assert order==sorted(range(4),key=lambda j:proj(V[j],eta))
 return red(word)

edges=D['arrows'];B=D['source_objects'];Qverts=D['target_objects']
polygons=[];certs=[];vertices={}
for k,e in enumerate(edges):
 xy=curves(tuple(e['representative']));poly,cert=certified_polygon(xy)
 polygons.append(poly);certs.append(cert)
 for v,cfg in [(e['source'],poly[0]),(20+e['target'],poly[-1])]:
  if v in vertices:assert vertices[v]==cfg
  else:vertices[v]=cfg
print('Exact rational-family polygon homotopies certified:',len(polygons),flush=True)
print('Total certified segments:',sum(len(p)-1 for p in polygons),flush=True)
base=(zero,one,(Q(10),Q()),(Q(20),Q()))
assert all(v[2]!=base[3] for v in vertices.values())
bridges={v:bridge(c,base) for v,c in vertices.items()}
for den in [37,41,43,47,53,59,61,67,71,73,79,83]:
 eta=Q(F(1,den))
 bs={v:braid_polygon(p,eta) for v,p in bridges.items()}
 fs=[braid_polygon(p,eta) for p in polygons]
 if all(w is not None for w in list(bs.values())+fs):break
else:raise AssertionError('projection list exhausted')
print('Exact regular projection slope:',eta,flush=True)
images=[]
for e,f in zip(edges,fs):
 w=red(bs[e['source']]+f+inv(bs[20+e['target']]))
 assert aux['permutation'](4,w)==(1,2,3,4)
 assert aux['link12'](4,w)==0
 nf=comb(4,w);assert aux['eq'](4,w,expand(nf))
 images.append(dict(braid=w,pure=nf))
print('All60 core arrow braid words combed and verified.',flush=True)
# A spanning tree of the actual fifty-vertex core.
adj={v:[] for v in vertices}
for j,e in enumerate(edges):
 u,v=e['source'],20+e['target'];adj[u].append((v,j,1));adj[v].append((u,j,-1))
paths={0:()};queue=deque([0]);tree=set()
while queue:
 u=queue.popleft()
 for v,j,s in adj[u]:
  if v not in paths:paths[v]=paths[u]+(s*(j+1),);queue.append(v);tree.add(j)
assert len(paths)==50 and len(tree)==49
loops=[]
def expand_edges(w):return red(x for a in w for x in (images[a-1]['braid'] if a>0 else inv(images[-a-1]['braid'])))
for j,e in enumerate(edges):
 if j in tree:continue
 w=paths[e['source']]+(j+1,)+inv(paths[20+e['target']])
 bw=expand_edges(w);nf=comb(4,bw);assert aux['eq'](4,bw,expand(nf))
 loops.append(dict(edge_word=w,braid=bw,pure=nf))
assert len(loops)==11
cols=[]
for l in loops:
 col=[]
 for p in [(1,3),(2,3),(1,4),(2,4),(3,4)]:col.append(sum(s for i,j,s in l['pure'] if (i,j)==p))
 cols.append(col)
M=S.Matrix(5,11,lambda i,j:cols[j][i]);rank=M.rank()
from sympy.matrices.normalforms import smith_normal_form
sn=smith_normal_form(M,domain=S.ZZ)
print('Core loop abelianization rank:',rank,';Smith diagonal:',[sn[i,i] for i in range(5)],flush=True)
result=dict(scope='Sixty explicit quartic paths; none of the remaining manuscript arrows is assigned here.',projection=str(eta),certificates=certs,base=[str(zsym(z)) for z in base],vertices={str(v):[str(zsym(z)) for z in c] for v,c in vertices.items()},arrows=[dict(**e,**im) for e,im in zip(edges,images)],tree_edges=sorted(tree),loops=loops,abelianization=cols,smith_diagonal=[int(sn[i,i]) for i in range(5)])
(ROOT/'b_core_paths.json').write_text(json.dumps(result,indent=2)+'\n')

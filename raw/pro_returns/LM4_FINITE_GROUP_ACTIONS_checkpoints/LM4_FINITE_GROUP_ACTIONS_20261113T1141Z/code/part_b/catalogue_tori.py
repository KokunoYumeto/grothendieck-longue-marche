#!/usr/bin/env python3
"""Exact affine classification of finite subgroups of Mod^+/-_{1,n}, 1<=n<=4.
Translation kernels have order <=n.  All finite GL(2,Z) linear parts and all
extension cocycles are enumerated, followed by decorated quotient strata.
Uses only Python's standard library; see B.27 for the completeness proof.
"""
from collections import defaultdict, Counter, deque
from fractions import Fraction
from functools import lru_cache
from itertools import product, combinations
from math import gcd
from pathlib import Path
import csv, json
from catalogue_low_complexity import mm,mv,det,matrix_inverse,closure,I,S,R,F

OUT=Path(__file__).resolve().parent
N=144
ZERO=(0,0)
ID=(I,ZERO)
GRID=tuple(product(range(N),repeat=2))

def add(x,y): return ((x[0]+y[0])%N,(x[1]+y[1])%N)
def sub(x,y): return ((x[0]-y[0])%N,(x[1]-y[1])%N)
def av(a,v): return tuple(x%N for x in mv(a,v))
def mul(x,y):
 a,t=x; b,u=y
 return mm(a,b),add(t,av(a,u))
def inv(x):
 a,t=x; b=matrix_inverse(a)
 return b,tuple(-v%N for v in mv(b,t))
def conj(x,y): return mul(mul(x,y),inv(x))
def act(x,p): return add(av(x[0],p),x[1])
def cgroup(x,h): return frozenset(conj(x,y) for y in h)
@lru_cache(None)
def order(x):
 y=ID
 for n in range(1,97):
  y=mul(y,x)
  if y==ID:return n
 raise AssertionError(('infinite',x))

def all_subgroups(h):
 hs={frozenset({ID})}; frontier=hs.copy()
 while frontier:
  new={closure(set(k)|{x},mul,ID) for k in frontier for x in h-k}-hs
  hs|=new; frontier=new
 return hs

@lru_cache(None)
def all_linear_subgroups(h):
 hs={frozenset({I})}; frontier=hs.copy()
 while frontier:
  new={closure(set(k)|{x},mm,I) for k in frontier for x in h-k}-hs
  hs|=new;frontier=new
 return hs

def linear_reps():
 verts=[closure([a,F],mm,I) for a in (S,R)]
 edge=verts[0]&verts[1]
 nodes=[(i,h) for i in range(2) for h in all_linear_subgroups(verts[i])]
 par={x:x for x in nodes}
 def root(x):
  while par[x]!=x:par[x]=par[par[x]];x=par[x]
  return x
 def union(x,y):
  x,y=root(x),root(y)
  if x!=y:par[y]=x
 for i,h in nodes:
  for a in verts[i]:
   ai=matrix_inverse(a)
   union((i,h),(i,frozenset(mm(mm(a,b),ai) for b in h)))
  if h<=edge:union((0,h),(1,h))
 cs=defaultdict(list)
 for x in nodes:cs[root(x)].append(x)
 reps=[min(v,key=lambda x:(x[0],sorted(x[1])))[1] for v in cs.values()]
 reps.sort(key=lambda h:(len(h),sum(det(a)==1 for a in h),sorted(h)))
 assert len(reps)==13
 return reps

# Every finite translation subgroup of order <=4 is contained in (1/12 Z)^2.
def translation_groups():
 ts={frozenset({ZERO})}
 for p in product(range(0,N,N//12),repeat=2):
  o=N//gcd(N,*p)
  if o<=4:ts.add(frozenset(((j*p[0])%N,(j*p[1])%N) for j in range(o)))
 ts.add(frozenset(product((0,N//2),repeat=2)))
 assert Counter(map(len,ts))=={1:1,2:3,3:4,4:7}
 return sorted(ts,key=lambda t:(len(t),sorted(t)))

TS=translation_groups()

def finite_normalizer(h):
 # For noncentral h these are all integral normalizers: the proof solves
 # the rotation norm form or the two rational reflection eigenspaces.
 out=[]
 for a in product(range(-2,3),repeat=4):
  if abs(det(a))!=1:continue
  ai=matrix_inverse(a)
  if frozenset(mm(mm(a,b),ai) for b in h)==h:out.append(a)
 assert out and len(out) in (4,8,12)
 return tuple(out)

def central(h): return h<=frozenset({I,(-1,0,0,-1)})

def stabilizer_generators(t):
 # Schreier's lemma for the GL2Z action on the complete finite set of T's.
 gens=(S,R,F,matrix_inverse(S),matrix_inverse(R))
 trans={t:I}; todo=deque([t])
 while todo:
  u=todo.popleft(); rep=trans[u]
  for a in gens:
   v=frozenset(av(a,x) for x in u)
   if v not in trans: trans[v]=mm(a,rep);todo.append(v)
 out=set()
 for u,b in trans.items():
  for a in gens:
   v=frozenset(av(a,x) for x in u)
   c=mm(mm(matrix_inverse(trans[v]),a),b)
   assert frozenset(av(c,x) for x in t)==t
   out.add(c)
 return tuple(sorted(out))

def invariant_covector(f):
 # primitive row w with w(I-F)=0.
 a,b,c,d=f
 candidates=[(c,1-a),(d-1,-b)]
 w=next(v for v in candidates if v!=ZERO)
 g=gcd(*map(abs,w));w=tuple(v//g for v in w)
 assert (w[0]*a+w[1]*c,w[0]*b+w[1]*d)==w
 return w

def affine_classes():
 answers=[];raw_stats=[]
 for hi,h in enumerate(linear_reps(),1):
  positive=[a for a in h if det(a)==1 and a!=I]
  r=max(positive,key=lambda a:order((a,ZERO))) if positive else None
  f=next((a for a in sorted(h) if det(a)==-1),None)
  raw=set()
  for t in TS:
   if not all(frozenset(av(a,x) for x in t)==t for a in h):continue
   tg=[(I,x) for x in t]
   if f is None:
    gens=tg+([(r,ZERO)] if r else [])
    raw.add(closure(gens,mul,ID));continue
   if r:
    bs=[p for p in GRID if sub(p,av(r,p)) in t
        and add(p,av(f,p)) in t]
   else:
    bs=[p for p in GRID if add(p,p) in t and add(p,av(f,p)) in t]
   for b in bs:
    gens=tg+[(f,b)]+([(r,ZERO)] if r else [])
    g=closure(gens,mul,ID)
    assert len(g)==len(t)*len(h)
    raw.add(g)
  raw=sorted(raw,key=lambda g:(len(g),sorted(g)))
  par={g:g for g in raw}
  def root(x):
   while par[x]!=x:par[x]=par[par[x]];x=par[x]
   return x
  def union(x,y):
   x,y=root(x),root(y)
   if x!=y:par[y]=x
  rawset=set(raw)
  normalizers=(S,R,F) if central(h) else finite_normalizer(h)
  for g in raw:
   t=frozenset(x[1] for x in g if x[0]==I)
   for a in normalizers:
    g1=cgroup((a,ZERO),g)
    assert g1 in rawset
    union(g,g1)
   if r:
    origins=[p for p in GRID if sub(p,av(r,p)) in t]
    for p in origins:
     g1=cgroup((I,p),g)
     assert g1 in rawset
     union(g,g1)
   elif f:
    # Arbitrary translations give exactly the quotient by im(I-F).
    w=invariant_covector(f)
    b=next(x[1] for x in g if x[0]==f)
    wt={(w[0]*p[0]+w[1]*p[1])%N for p in t}
    for g1 in raw:
     if frozenset(x[1] for x in g1 if x[0]==I)!=t:continue
     b1=next(x[1] for x in g1 if x[0]==f)
     delta=sub(b,b1)
     if (w[0]*delta[0]+w[1]*delta[1])%N in wt:union(g,g1)
  cs=defaultdict(list)
  for g in raw:cs[root(g)].append(g)
  reps=[min(v,key=lambda g:sorted(g)) for v in cs.values()]
  reps.sort(key=lambda g:(len(g),sorted(g)))
  raw_stats.append({'linear_id':hi,'linear_order':len(h),
                    'raw_groups':len(raw),'affine_classes':len(reps)})
  for g in reps:answers.append((hi,g))
 return answers,raw_stats

@lru_cache(None)
def fixed_grid(g):return frozenset(p for p in GRID if act(g,p)==p)

@lru_cache(None)
def reflection_graph(g):
 assert det(g[0])==-1 and order(g)==2
 a,b,c,d=g[0]; rows=((a-1,b),(c,d-1))
 row=next(v for v in rows if v!=ZERO)
 direction=(row[1],-row[0]);z=gcd(*map(abs,direction))
 direction=tuple(v//z for v in direction)
 pts=fixed_grid(g)
 graph={p:frozenset((add(p,direction),sub(p,direction))) for p in pts}
 assert all(len(v)==2 and v<=pts for v in graph.values())
 return graph

def components(graph,deleted=frozenset()):
 left=set(graph)-set(deleted);out=[]
 while left:
  p=min(left);seen=set();todo=[p]
  while todo:
   x=todo.pop()
   if x in seen or x in deleted:continue
   seen.add(x);todo.extend(graph[x]-seen-set(deleted))
  left-=seen
  oval=not any(graph[x]&set(deleted) for x in seen)
  out.append(('oval' if oval else 'line',frozenset(seen)))
 return out

def orbit(x,g,action):return frozenset(action(a,x) for a in g)

def permutation_closure(gens,n):
 identity=tuple(range(n));out={identity};todo=[identity]
 while todo:
  a=todo.pop()
  for b in gens:
   c=tuple(a[b[i]] for i in range(n))
   if c not in out:out.add(c);todo.append(c)
 return out

class Action:
 def __init__(self,hi,g):
  self.hi,self.g=hi,g
  self.h=frozenset(a for a,t in g)
  self.t=frozenset(t for a,t in g if a==I)
  self.elems=sorted(g);self.ids={x:i for i,x in enumerate(self.elems)}
  self.rotations=[x for x in g if det(x[0])==1 and x[0]!=I]
  self.reflections=[x for x in g if det(x[0])==-1 and order(x)==2
                    and fixed_grid(x)]
  self.vertices=frozenset().union(*(fixed_grid(x) for x in self.rotations))
  assert all(N % z.denominator == 0 for x in self.rotations
             for z in self.inverse_certificate(x))
  left=set(self.vertices);self.vertex_orbits=[]
  while left:
   p=min(left);orb=orbit(p,g,act);left-=orb;self.vertex_orbits.append(orb)
  self.vertex_orbits.sort(key=lambda x:sorted(x))
  edges=[]
  for x in self.reflections:
   for kind,c in components(reflection_graph(x),self.vertices):edges.append(c)
  assert len(set(edges))==len(edges)
  left=set(edges);self.edge_orbits=[]
  while left:
   e=min(left,key=lambda x:sorted(x))
   orb=frozenset(frozenset(act(a,p) for p in e) for a in g)
   assert orb<=set(edges)
   left-=orb;self.edge_orbits.append(orb)
  self.edge_orbits.sort(key=lambda x:sorted(sorted(e) for e in x))
  self.strata=[('vertex',v) for v in self.vertex_orbits]+[
     ('mirror',frozenset().union(*es)) for es in self.edge_orbits]
  self.point_to_stratum={p:i for i,(kind,s) in enumerate(self.strata) for p in s}
  self.weights=[len(v) for v in self.vertex_orbits]+[len(g)//2]*len(self.edge_orbits)
  self.perms=self.normalizer_permutations()
 def inverse_certificate(self,g):
  a,t=g;b=(a[0]-1,a[1],a[2],a[3]-1);d=det(b)
  assert d
  bi=tuple(Fraction(v,d) for v in (b[3],-b[1],-b[2],b[0]))
  p=mv(bi,tuple(Fraction(-v,N) for v in t))
  return bi+p
 def stratum_perm(self,x):
  return tuple(self.point_to_stratum[act(x,min(s))] for kind,s in self.strata)
 def normalizer_permutations(self):
  size=len(self.strata)
  if not size:return {()}
  positive=[a for a in self.h if det(a)==1 and a!=I]
  r=max(positive,key=lambda a:order((a,ZERO))) if positive else None
  if central(self.h):
   linear=stabilizer_generators(self.t)
  else:
   linear=[a for a in finite_normalizer(self.h)
           if frozenset(av(a,p) for p in self.t)==self.t]
  gens=set()
  origins=([p for p in GRID if sub(p,av(r,p)) in self.t] if r else GRID)
  for a in linear:
   for p in origins:
    x=(a,p)
    if cgroup(x,self.g)==self.g:gens.add(self.stratum_perm(x))
  assert gens
  return permutation_closure(gens,size)
 def decorations(self,nu):
  limits=[1]*len(self.vertex_orbits)+[nu//(len(self.g)//2) for _ in self.edge_orbits]
  seen=set();out=[]
  for d in product(*(range(q+1) for q in limits)):
   rem=nu-sum(x*w for x,w in zip(d,self.weights))
   if rem<0 or rem%len(self.g):continue
   a=rem//len(self.g)
   imgs={tuple(d[p[i]] for i in range(len(d))) for p in self.perms}
   key=min(imgs)+(a,)
   if key not in seen:seen.add(key);out.append(key)
  return sorted(out)
 def realize(self,dec):
  pts=set()
  nv=len(self.vertex_orbits)
  for d,v in zip(dec[:nv],self.vertex_orbits):
   if d:pts|=v
  for d,es in zip(dec[nv:-1],self.edge_orbits):
   component=min(es,key=lambda e:sorted(e));added=0
   for p in sorted(component):
    if p in pts:continue
    if added==d:break
    pts|=orbit(p,self.g,act);added+=1
   assert added==d
  added=0
  for p in GRID:
   if p in self.point_to_stratum or p in pts:continue
   if added==dec[-1]:break
   pts|=orbit(p,self.g,act);added+=1
  assert added==dec[-1]
  assert len(pts)==sum(d*w for d,w in zip(dec[:-1],self.weights))+dec[-1]*len(self.g)
  return frozenset(pts)
 def section_table(self,punctures):
  sections=[];point_groups={}
  for p in sorted(self.vertices-punctures):
   stabilizer=frozenset(x for x in self.g if act(x,p)==p)
   if stabilizer not in point_groups:point_groups[stabilizer]=all_subgroups(stabilizer)
   for k in point_groups[stabilizer]:
    if any(det(x[0])==1 and x[0]!=I for x in k):
     sections.append((k,'point',frozenset({p})))
  for x in self.reflections:
   for kind,pts in components(reflection_graph(x),punctures):
    sections.append((frozenset({ID,x}),kind,pts))
  sections=sorted(set(sections),key=lambda c:(len(c[0]),sorted(c[0]),c[1],sorted(c[2])))
  ids={c:i for i,c in enumerate(sections)}
  def included(c,d):return c[0]<d[0] and d[2]<=c[2]
  def action(x,c):
   return (cgroup(x,c[0]),c[1],frozenset(act(x,p) for p in c[2]))
  maxima=[c for c in sections if not any(included(c,d) for d in sections)]
  left=set(maxima);orbits=[]
  while left:
   c=min(left,key=lambda x:ids[x]);orb=orbit(c,self.g,action)
   assert orb<=set(maxima)
   orbits.append(sorted(ids[x] for x in orb));left-=orb
  records=[]
  for c in sections:
   k,kind,pts=c;extensions=[d for d in sections if included(c,d)]
   mx=[d for d in maxima if d==c or included(c,d)]
   if kind=='point':assert len(mx)==1
   mu={self.ids[x]:str(self.mu(x)) for x in k}
   for x in k:
    val=self.mu(x)
    assert val.denominator==order(x)
    y=ID
    for j in range(order(x)+1):
     assert self.mu(y)==(j*val)%1;y=mul(y,x)
   stabilizer=[x for x in self.g if action(x,c)==c]
   if c in maxima and kind=='point':assert set(stabilizer)==set(k)
   records.append({'id':ids[c],'image_elements':[self.ids[x] for x in sorted(k)],
     'kind':kind,'representative':list(min(pts)),
     'centralizer':'Z' if kind=='oval' else '1','mu':mu,'maximal':c in maxima,
     'strict_extensions':[ids[d] for d in extensions],
     'maximal_overgroups':[ids[d] for d in mx],
     'Gamma_stabilizer':[self.ids[x] for x in sorted(stabilizer)]})
  full=(1 if len(self.g)==1 else sum(c[0]==self.g for c in sections))
  return {'full':full,'partial':len(sections),'phi':len(maxima),'phi_orbits':len(orbits),
   'ovals':sum(c[1]=='oval' for c in sections),'lines':sum(c[1]=='line' for c in sections),
   'records':records,'orbits':orbits}
 def mu(self,x):
  if x==ID:return Fraction(0)
  a,t=x
  if det(a)==-1:return Fraction(1,2)
  tr=a[0]+a[3]
  if tr==-2:return Fraction(1,2)
  n={-1:3,0:4,1:6}[tr]
  assert a[2]
  return Fraction(1 if a[2]>0 else -1,n)%1
 def name(self):
  g=self.g;n=len(g);orders=Counter(order(x) for x in g)
  exp=max(orders);ab=all(mul(x,y)==mul(y,x) for x in g for y in g)
  if n==1:return '1'
  if n in orders:return 'C'+str(n)
  if ab:return f'Abelian(order={n},exponent={exp})'
  if n==6:return 'S3'
  if n==8 and orders[2]==5:return 'D8'
  if n==12 and orders[3]==8:return 'A4'
  if n==12 and orders[2]==7:return 'D12'
  if n==24 and orders=={1:1,2:9,3:8,4:6}:return 'S4'
  return f'Group(order={n},orders={dict(sorted(orders.items()))})'
 def data(self):
  return {'linear_class':self.hi,'translation_order':len(self.t),'order':len(self.g),
   'linear_part':sorted(self.h),'translation_kernel':sorted(self.t),
   'elements':[{'id':i,'matrix':a,'translation_numerator':t,'order':order((a,t)),
                'orientation':det(a)} for i,(a,t) in enumerate(self.elems)],
   'vertex_orbits':[sorted(v) for v in self.vertex_orbits],
   'mirror_strata':[{'components':len(es),'sample_point':min(min(e) for e in es),
                      'circle':all(kind=='oval' for x in self.reflections
                         for kind,c in components(reflection_graph(x),self.vertices)
                         if c in es)} for es in self.edge_orbits],
   'stratum_weights':self.weights,'normalizer_permutations':sorted(self.perms)}

def main():
 affine,stats=affine_classes()
 print('AFFINE NORMAL FORMS',len(affine),stats,flush=True)
 tables={n:[] for n in range(1,5)};details={n:[] for n in range(1,5)}
 normals=[]
 for ai,(hi,g) in enumerate(affine,1):
  action=Action(hi,g);normal=action.data();normal['affine_id']=ai
  normals.append(normal)
  for nu in range(1,5):
   if len(action.t)>nu:continue
   for dec in action.decorations(nu):
    punctures=action.realize(dec);s=action.section_table(punctures)
    cid=f'T{nu}_{len(tables[nu])+1:03}'
    row={'type':f'(1,{nu})','class_id':cid,'affine_id':ai,'group':action.name(),
      'order':len(g),'positive_order':sum(det(a)==1 for a,t in g),
      'translation_order':len(action.t),'linear_class':hi,
      'decoration':str(dec),'full_splitting_classes':s['full'],
      'nontrivial_partial_splitting_classes':s['partial'],'Phi':s['phi'],
      'Phi_orbits':s['phi_orbits'],'ovals':s['ovals'],'lines':s['lines']}
    tables[nu].append(row)
    ps=[]
    for p in sorted(punctures):
     stab=[x for x in g if act(x,p)==p]
     ps.append({'point':p,'stabilizer_elements':[action.ids[x] for x in sorted(stab)],
                'mu':{action.ids[x]:str(action.mu(x)) for x in stab}})
    details[nu].append({'class_id':cid,'affine_id':ai,'decoration':dec,
      'punctures':ps,'sections':s['records'],'Phi_orbits':s['orbits']})
  print('NORMAL',ai,'order',len(g),'linear',hi,'T',len(action.t),
        'strata',len(action.strata),'classes_so_far', {n:len(tables[n]) for n in tables},flush=True)
 for nu in range(1,5):
  rows=tables[nu]
  with (OUT/f'type_1_{nu}_affine_catalogue.csv').open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
  (OUT/f'type_1_{nu}_affine_sections.json').write_text(json.dumps({
   'type':f'(1,{nu})','grid_denominator':N,'catalogue':details[nu]},indent=2)+'\n')
 (OUT/'torus_affine_normal_forms.json').write_text(json.dumps(normals,indent=2)+'\n')
 counts={f'(1,{n})':len(tables[n]) for n in tables}
 # The independently computed GL2Z amalgam table is a complete cross-check.
 old=list(csv.DictReader((OUT/'type_1_1_finite_subgroups.csv').open()))
 sig=lambda r:tuple(int(r[k]) for k in ('order','positive_order','full_splitting_classes',
                                     'nontrivial_partial_splitting_classes'))
 assert len(tables[1])==13
 assert sorted(sig(r) for r in tables[1])==sorted(sig(r) for r in old)
 (OUT/'catalogue_tori_output.json').write_text(json.dumps({
  'counts':counts,'affine_forms':len(affine),'raw_linear_statistics':stats,
  'type_1_1_independent_crosscheck':'passed'},indent=2)+'\n')
 print('FINAL',json.dumps(counts),flush=True)
if __name__=='__main__':main()

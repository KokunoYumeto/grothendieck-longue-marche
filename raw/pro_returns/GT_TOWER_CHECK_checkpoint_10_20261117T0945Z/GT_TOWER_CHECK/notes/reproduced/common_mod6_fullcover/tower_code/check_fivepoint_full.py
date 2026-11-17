#!/usr/bin/env python3
"""Reconstruct EXIT_TOWER B22–B25's chosen 542-object,1620-arrow model.
Exact determinant Bernstein certificates imply collision-free straightening
for every relabelling; the graph, braid words and all relators are emitted.
The comparison with any additional unrecorded manuscript path choice is not
asserted. Inputs are the explicit formulas in B21–B25, written below.
"""
import check_fivepoint_paths as C
from check_fivepoint_paths import Q3,C3,F,zero,one,I,cyc,generate,rep,perm_mul,normalize,segment_braid,path_braid,concat,inverse,artin,subst,A,red
from pathlib import Path
from collections import deque
import json
from dataclasses import dataclass
EPS=F(1,10);SQRT3=Q3(0,1)
perms=C.perms;H,HB,HQ=C.H,C.HB,C.HQ
cosets=sorted({rep(g,H) for g in perms})
HP=generate([cyc(0,3,1,2,4),perm_mul(cyc(1,2),cyc(3,4))])
ps=sorted({rep(g,HP) for g in perms})
vertices=list(C.vertices);ends=list(C.ends);words=list(C.arrow_words);families=['core']*60
coords=C.coordinates
zeta=C3(-F(1,2),Q3(0,F(1,2)));xi=C3(F(1,2),Q3(0,F(1,2)))
VR=(None,C3(-EPS),C3(EPS),C3(-1),one)
VL=(None,-I*EPS,I*EPS,C3(-1),one)
TR=(None,C3(-1-EPS),C3(1+EPS),C3(-1+EPS),C3(1-EPS))
TM=(None,C3(-1)-I*EPS,C3(1+EPS),C3(-1)+I*EPS,C3(1-EPS))
TL=(None,C3(-1)-I*EPS,C3(1)+I*EPS,C3(-1)+I*EPS,C3(1)-I*EPS)
W=(one,zeta,zeta*zeta,C3(-1/EPS),C3(1/EPS))

@dataclass(frozen=True)
class Q5:
 a:F=F(0);b:F=F(0)
 def __post_init__(self):object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
 @staticmethod
 def of(x):return x if isinstance(x,Q5) else Q5(x)
 def __add__(self,x):x=Q5.of(x);return Q5(self.a+x.a,self.b+x.b)
 __radd__=__add__
 def __neg__(self):return Q5(-self.a,-self.b)
 def __sub__(self,x):return self+-Q5.of(x)
 def __mul__(self,x):x=Q5.of(x);return Q5(self.a*x.a+5*self.b*x.b,self.a*x.b+self.b*x.a)
 __rmul__=__mul__
 def __truediv__(self,x):
  x=Q5.of(x);d=x.a*x.a-5*x.b*x.b;assert d
  return self*Q5(x.a/d,-x.b/d)
 def sign(self):
  a,b=self.a,self.b
  if not a:return (b>0)-(b<0)
  if not b:return (a>0)-(a<0)
  if a*b>0:return (a>0)-(a<0)
  d=a*a-5*b*b
  return ((a>0)-(a<0))*((d>0)-(d<0))
 def serial(self):return [str(self.a),str(self.b)]

def normalize_real5(arr):
 def hom(x):return (Q5(1),Q5(0)) if x is None else (x,Q5(1))
 def det(x,y):return x[0]*y[1]-y[0]*x[1]
 a,b,c=[hom(arr[j]) for j in (0,1,4)]
 def n(w):w=hom(w);return det(w,a)*det(b,c)/(det(w,c)*det(b,a))
 return (Q5(0),Q5(1),n(arr[2]),n(arr[3]))

def relabel(arr,g):return tuple(arr[g.index(j)] for j in range(5))
# Check every shared pentagon endpoint over Q(sqrt5), independently of the
# crossing calculation: 0<epsilon<sqrt5-2<1, so all real erasures are
# collision-free and keep the real normalized order throughout.
qP=Q5(-2,1);assert (qP-Q5(EPS)).sign()>0 and (Q5(1)-qP).sign()>0
Pconfig=(None,-qP,qP,Q5(-1),Q5(1));pentagon_coords={}
for g in perms:
 v=('P',rep(g,HP));p=normalize_real5(relabel(Pconfig,g))
 if v in pentagon_coords:assert pentagon_coords[v]==p
 pentagon_coords[v]=p
assert len(set(pentagon_coords.values()))==12
print('PASS all12 pentagon endpoints, exact Q(sqrt5), and real-erasure order',flush=True)
def add_vertices(kind,parameters,arr):
 before=len(vertices)
 for g in parameters:
  v=(kind,g);vertices.append(v)
  if arr is not None:coords[v]=normalize(relabel(arr,g))
 if arr is not None:
  normalized=[coords[v] for v in vertices[before:]]
  assert len(set(normalized))==len(normalized),('duplicate normalized vertices',kind)
  print('PASS distinct normalized vertices',kind,len(normalized),flush=True)
add_vertices('P',ps,None);add_vertices('VR',cosets,VR);add_vertices('VL',cosets,VL)
# Polynomial arithmetic on homogeneous projective representatives.
def pol_add(a,b):return tuple((a[i] if i<len(a) else zero)+(b[i] if i<len(b) else zero) for i in range(max(len(a),len(b))))
def pol_neg(a):return tuple(-x for x in a)
def pol_mul(a,b):
 out=[zero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return tuple(out)
def pol_eval(p,t):
 out=zero
 for c in reversed(p):out=out*C3(t)+c
 return out

def const(x):return (C3.of(x),)
def linear(s,t):return (C3.of(s),C3.of(t)-C3.of(s))
def affine_path(a,b):
 out=[]
 for x,y in zip(a,b):
  if x is None:assert y is None;out.append((const(1),const(0)))
  else:out.append((linear(x,y),const(1)))
 return tuple(out)
def hom_at(path,t):return tuple((pol_eval(n,t),pol_eval(d,t)) for n,d in path)
def norm_hom(h):
 a,b,c=[h[j] for j in (0,1,4)]
 def det(x,y):return x[0]*y[1]-y[0]*x[1]
 def n(w):return det(w,a)*det(b,c)/(det(w,c)*det(b,a))
 return (zero,one,n(h[2]),n(h[3]))
def norm_path_at(path,g,t):return norm_hom(relabel(hom_at(path,t),g))
def conj(z):return C3(z.re,-z.im)
CONE=Q3(2,-1)
certificate_data={}
def certified_intervals(name,path):
 determinants=[]
 for i in range(5):
  for j in range(i+1,5):
   d=pol_add(pol_mul(path[i][0],path[j][1]),pol_neg(pol_mul(path[j][0],path[i][1])))
   assert len(d)<=3
   determinants.append(d)
 def test(a,b):
  mid=(a+b)/2
  for d in determinants:
   v0=pol_eval(d,a);v2=pol_eval(d,b);vm=pol_eval(d,mid)
   v1=vm*2-(v0+v2)/2
   for v in (v0,v1,v2):
    rot=v*conj(vm)
    if rot.re.sign()<=0:return False
    if not (-CONE*rot.re<rot.im<CONE*rot.re):return False
  return True
 todo=[(F(0),F(1),0)];intervals=[]
 while todo:
  a,b,depth=todo.pop()
  if test(a,b):intervals.append((a,b));continue
  assert depth<20,(name,a,b)
  m=(a+b)/2;todo.extend([(m,b,depth+1),(a,m,depth+1)])
 intervals.sort()
 certificate_data[name]={'intervals':[[str(a),str(b)] for a,b in intervals],'determinants':[[z.serial() for z in d] for d in determinants]}
 print('PASS determinant cone certificate',name,'intervals',len(intervals),flush=True)
 return intervals

def transport_word(v):
 if v[0]=='P':return pent_transport[v]
 return C.transport_braid(v)

def append_path(name,path,params,endfun):
 intervals=certified_intervals(name,path)
 for g in params:
  s,t=endfun(g)
  p0=norm_path_at(path,g,F(0));p1=norm_path_at(path,g,F(1))
  assert p0==coords[s],('source',name,g,s,p0,coords[s])
  assert p1==coords[t],('target',name,g,t,p1,coords[t])
  pure=concat(*(segment_braid(norm_path_at(path,g,a),norm_path_at(path,g,b)) for a,b in intervals))
  w=concat(transport_word(s),pure,inverse(transport_word(t)))
  ends.append((s,t));words.append(w);families.append(name)

# Real erasures have all normalized coordinates real and strictly ordered,
# so their projected braid is empty. Each pentagon transport uses first incoming erasure.
pent_transport={}
for g in cosets:
 s,t=('VR',g),('P',rep(g,HP))
 if t not in pent_transport:pent_transport[t]=transport_word(s)
 ends.append((s,t));words.append(concat(transport_word(s),inverse(pent_transport[t])));families.append('real_erasure')
assert len(pent_transport)==12
append_path('quarter_turn',affine_path(VR,VL),cosets,lambda g:(('VR',g),('VL',g)))
BK=(None,-I*C3(Q3(0,F(1,3))),I*C3(Q3(0,F(1,3))),C3(-1),one)
append_path('imaginary_erasure',affine_path(VL,BK),cosets,lambda g:(('VL',g),('B',rep(g,HB))))
# The120 composite f_Q,a paths exclude the core incidence with the same gH.
core_by_B={v:[] for v in C.vertices if v[0]=='B'}
for k,(s,t) in enumerate(C.ends):core_by_B[s].append(k)
for j,g in enumerate(cosets):
 s=('VL',g);mid=('B',rep(g,HB));gamma_index=180+j
 for k in core_by_B[mid]:
  if C.edges[k]==g:continue
  ends.append((s,C.ends[k][1]));words.append(concat(words[gamma_index],words[k]));families.append('f_Qa_composite')
assert (len(vertices),len(words))==(182,360)
print('PASS first tier182 objects360 arrows',flush=True)
# Second tier.
add_vertices('TR',cosets,TR);add_vertices('TM',perms,TM);add_vertices('TL',cosets,TL)
pR=(2,1,3,0,4);pL=(0,1,3,4,2);pQ=(0,4,3,1,2)
Rstar=(None,C3(-1/(1-EPS)),zero,C3(-1/(1+EPS)),C3(-F(1,2)))
Mstar=(None,-one/(one-I*EPS),zero,-one/(one+I*EPS),C3(-F(1,2)))
GLend=(None,-I*EPS,I,I*EPS,-I)
GLLend=(None,C3(-1)-I,C3(1)+I,C3(-1)+I,C3(1)-I)
append_path('T_A',affine_path(TR,TM),perms,lambda g:(('TR',rep(g,H)),('TM',g)))
append_path('G_R',affine_path(TR,Rstar),perms,lambda g:(('TR',rep(g,H)),('VR',rep(perm_mul(g,pR),H))))
append_path('T_B',affine_path(TM,TL),perms,lambda g:(('TM',g),('TL',rep(g,H))))
append_path('G_M',affine_path(TM,Mstar),perms,lambda g:(('TM',g),('VL',rep(perm_mul(g,pR),H))))
append_path('G_L',affine_path(TL,GLend),perms,lambda g:(('TL',rep(g,H)),('VR',rep(perm_mul(g,pL),H))))
append_path('G_LL',affine_path(TL,GLLend),cosets,lambda g:(('TL',g),('Q',rep(perm_mul(g,pQ),HQ))))
assert (len(vertices),len(words))==(422,1020)
print('PASS second tier422 objects1020 arrows',flush=True)
# Third tier.
add_vertices('W',perms,W)
ptau=(1,2,0,4,3)
qpoly=linear(C3(EPS),xi*EPS)
sixth=tuple([(const(z),const(1)) for z in (one,zeta,zeta*zeta)]+[(const(-1),qpoly),(const(1),qpoly)])
append_path('sixth_turn',sixth,perms,lambda g:(('W',g),('W',perm_mul(g,ptau))))
eraseW=tuple([(const(z),const(1)) for z in (one,zeta,zeta*zeta)]+[(linear(-1,0),const(EPS)),(const(1),linear(EPS,0))])
append_path('W_erasure',eraseW,perms,lambda g:(('W',g),('B',rep(g,HB))))
lambda_star=C3(-F(19,181),F(1,181))
lambdas=[C3(-F(30,91),Q3(0,F(110,819))),C3(F(27,37),Q3(0,F(30,407))),C3(F(121,40),Q3(0,F(33,40)))]
p0=(0,1,3,4,2);cc=cyc(0,2,4);pj=p0
for j,lam in enumerate(lambdas):
 start=(zero,lambda_star,one,conj(lambda_star),None);target=(zero,lam,one,conj(lam),None)
 append_path('TM_to_W_'+str(j),affine_path(start,target),perms,lambda g,pj=pj:(('TM',g),('W',perm_mul(g,pj))))
 pj=perm_mul(cc,pj)
assert (len(vertices),len(words))==(542,1620)
print('PASS full model542 objects1620 arrows',flush=True)
# Build exactly the staged spanning tree specified in B21–B25.
parent={v:v for v in vertices}
def find(v):
 while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
 return v
chosen=set()
def add_tree(i):
 s,t=ends[i-1];ps,pt=find(s),find(t)
 if ps!=pt:parent[ps]=pt;chosen.add(i);return True
 return False
for i in sorted(C.tree):add_tree(i)
for i in range(61,1021):add_tree(i)
assert len(chosen)==421
for i in range(1261,1381):assert add_tree(i)
assert len(chosen)==541
adj={v:[] for v in vertices}
for i in chosen:
 s,t=ends[i-1];adj[s].append((i,t));adj[t].append((-i,s))
paths={vertices[0]:()};todo=deque([vertices[0]])
while todo:
 v=todo.popleft()
 for i,w in adj[v]:
  if w not in paths:paths[w]=paths[v]+(i,);todo.append(w)
assert len(paths)==542
non=[i for i in range(1,1621) if i not in chosen]
assert len(non)==1079
# Combing of pure braids into A13,A23,A14,A24,A34, with exact Artin verification.
def delete_strand(w,n):
 order=list(range(1,n+1));out=[]
 for k in w:
  i=abs(k)-1;pos=order.index(n)
  if pos not in (i,i+1):out.append((1 if k>0 else -1)*(abs(k)-(1 if pos<i else 0)))
  order[i],order[i+1]=order[i+1],order[i]
 assert order==list(range(1,n+1))
 return red(out)
def kernel_conjugator(w,n):
 image=list(artin(tuple(w))[n-1]);stem=[]
 while len(image)>1:
  assert image[0]==-image[-1],('not conjugate',n,image)
  stem.append(image.pop(0));image.pop()
 assert image==[n]
 return red(x for x in stem if abs(x)!=n)
abelian_generators=[A(1,3),A(2,3),A(1,4),A(2,4),A(3,4)]
@C.lru_cache(None)
def comb(w):
 w=tuple(w);b0=delete_strand(w,4);u=concat(inverse(b0),w)
 ker=kernel_conjugator(u,4)
 base2=delete_strand(b0,3);assert not base2,('nonzero scalar linking',base2)
 ba=kernel_conjugator(b0,3)
 result=tuple(ba)+tuple((1 if x>0 else -1)*(abs(x)+2) for x in ker)
 assert artin(w)==artin(subst(result,abelian_generators)),('combing failure',w,result)
 return result
arrow_combed=[]
for i,w in enumerate(words,1):
 arrow_combed.append(comb(tuple(w)))
 if i%200==0:print('PASS combed and Artin-verified arrows',i,flush=True)

def eval_edges(w):return concat(*(words[i-1] if i>0 else inverse(words[-i-1]) for i in w))
# Keep the original11 core cycles. Each remaining cycle is one Tietze relator.
core_non=set(C.non);new_relators=[]
for i in non:
 if i in core_non:continue
 s,t=ends[i-1];cycle=concat(paths[s],(i,),inverse(paths[t]));bw=eval_edges(cycle);w5=comb(bw)
 new_relators.append({'edge':i,'cycle_edges':cycle,'braid_word':bw,'word_abxyz':w5})
 if len(new_relators)%200==0:print('PASS Tietze cycle words',len(new_relators),flush=True)
assert len(new_relators)==1068
# Exact inverse dictionary from B38 to the core cycle letters.
dictionary={1:(11,),2:(-11,3,-2),3:(2,-6,-2),4:(2,-4,-2),5:(2,)}
for rel in new_relators:
 rel['word_core_cycles']=concat(*(dictionary[x] if x>0 else inverse(dictionary[-x]) for x in rel['word_abxyz']))
core_cycles=C.cycles
for rel in new_relators:
 rel['rhs_edges']=concat(*(core_cycles[j-1] if j>0 else inverse(core_cycles[-j-1]) for j in rel['word_core_cycles']))
 assert artin(eval_edges(rel['cycle_edges']))==artin(eval_edges(rel['rhs_edges']))
print('PASS all1068 added relators verified via explicit core inverse',flush=True)
def core_to_edges(w):return concat(*(core_cycles[j-1] if j>0 else inverse(core_cycles[-j-1]) for j in w))
def five_to_core(w):return concat(*(dictionary[j] if j>0 else inverse(dictionary[-j]) for j in w))
core_relators=[]
for j,rhs in [(1,(3,-4)),(5,(11,2,-6)),(7,(-6,)),(8,(2,-3,11,4,-2)),(9,(2,-3,4,6,-2)),(10,(3,-6,-4))]:
 core_relators.append({'family':'B39_elimination','lhs_core':(j,),'rhs_core':rhs})
def comm(u,v):return (-v,-u,v,u)
for lhs,rhs in [((1,3,-1),(-5,3,5)),((1,4,-1),concat(comm(3,5),(4,),inverse(comm(3,5)))),((1,5,-1),concat(comm(3,5),(5,))),((2,3,-2),(3,)),((2,4,-2),(-5,4,5)),((2,5,-2),concat(comm(4,5),(5,)))]:
 core_relators.append({'family':'B40_free_by_free','lhs_core':five_to_core(lhs),'rhs_core':five_to_core(rhs)})
for rel in core_relators:
 rel['lhs_edges']=core_to_edges(rel['lhs_core']);rel['rhs_edges']=core_to_edges(rel['rhs_core'])
 assert artin(eval_edges(rel['lhs_edges']))==artin(eval_edges(rel['rhs_edges']))
assert len(core_relators)==12
print('PASS all12 core defining relators with expanded edge words',flush=True)
result={'scope':'Chosen realization of EXIT_TOWER B21–B25; manuscript convention comparison is separate.','vertices':[str(v) for v in vertices],'edges':[{'id':i,'family':fam,'source':str(s),'target':str(t),'braid_word':w,'word_abxyz':cw} for i,((s,t),w,cw,fam) in enumerate(zip(ends,words,arrow_combed,families),1)],'tree_edges':sorted(chosen),'tree_paths':{str(v):paths[v] for v in vertices},'core_cycles':core_cycles,'new_relators':new_relators,'core_relators':core_relators,'core_relator_count':12,'total_relator_count':1080,'bernstein_certificates':certificate_data,'pentagon_endpoints':{str(v):[x.serial() for x in p] for v,p in pentagon_coords.items()}}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Completed exact reconstruction:542 objects,1620 arrows,1080 defining relations.',flush=True)

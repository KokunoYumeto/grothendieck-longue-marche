#!/usr/bin/env python3
"""Reconstruct all sixty core paths of EXIT_TOWER B21 over Q(sqrt(3),i).
Uses exact arithmetic, projection crossings, and the faithful Artin action.
The rational-path-to-chord homotopy is supplied by B44's proved half-plane
bound; this program checks the chord and specified detour transports.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from collections import deque
from pathlib import Path
from functools import lru_cache
import json
@dataclass(frozen=True)
class Q3:
 a:F=F(0);b:F=F(0)
 def __post_init__(self):object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
 @staticmethod
 def of(x):return x if isinstance(x,Q3) else Q3(x)
 def __add__(self,x):x=Q3.of(x);return Q3(self.a+x.a,self.b+x.b)
 __radd__=__add__
 def __neg__(self):return Q3(-self.a,-self.b)
 def __sub__(self,x):return self+-Q3.of(x)
 def __rsub__(self,x):return Q3.of(x)+-self
 def __mul__(self,x):x=Q3.of(x);return Q3(self.a*x.a+3*self.b*x.b,self.a*x.b+self.b*x.a)
 __rmul__=__mul__
 def __truediv__(self,x):
  x=Q3.of(x);d=x.a*x.a-3*x.b*x.b
  assert d
  return self*Q3(x.a/d,-x.b/d)
 def __rtruediv__(self,x):return Q3.of(x)/self
 def sign(self):
  a,b=self.a,self.b
  if not a:return (b>0)-(b<0)
  if not b:return (a>0)-(a<0)
  if a*b>0:return (a>0)-(a<0)
  d=a*a-3*b*b
  return ((a>0)-(a<0))*((d>0)-(d<0))
 def __lt__(self,x):return (self-x).sign()<0
 def __le__(self,x):return (self-x).sign()<=0
 def __float__(self):return float(self.a)+float(self.b)*3**.5
 def serial(self):return [str(self.a),str(self.b)]
@dataclass(frozen=True)
class C3:
 re:Q3=Q3();im:Q3=Q3()
 def __post_init__(self):object.__setattr__(self,'re',Q3.of(self.re));object.__setattr__(self,'im',Q3.of(self.im))
 @staticmethod
 def of(x):return x if isinstance(x,C3) else C3(x)
 def __add__(self,x):x=C3.of(x);return C3(self.re+x.re,self.im+x.im)
 __radd__=__add__
 def __neg__(self):return C3(-self.re,-self.im)
 def __sub__(self,x):return self+-C3.of(x)
 def __rsub__(self,x):return C3.of(x)+-self
 def __mul__(self,x):x=C3.of(x);return C3(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
 __rmul__=__mul__
 def __truediv__(self,x):x=C3.of(x);d=x.re*x.re+x.im*x.im;return C3((self.re*x.re+self.im*x.im)/d,(self.im*x.re-self.re*x.im)/d)
 def __rtruediv__(self,x):return C3.of(x)/self
 def serial(self):return [self.re.serial(),self.im.serial()]
zero=C3();one=C3(1);I=C3(0,1)
def hom(z):return (one,zero) if z is None else (z,one)
def det(x,y):return x[0]*y[1]-y[0]*x[1]
def normalize(arr):
 a,b,c=[hom(arr[j]) for j in (0,1,4)]
 def n(w):w=hom(w);return det(w,a)*det(b,c)/(det(w,c)*det(b,a))
 return (zero,one,n(arr[2]),n(arr[3]))
def perm_mul(p,q):return tuple(p[q[i]] for i in range(5))
identity=tuple(range(5));perms=tuple(permutations(range(5)))
def cyc(*xs):
 p=list(identity)
 for a,b in zip(xs,xs[1:]+xs[:1]):p[a]=b
 return tuple(p)
def generate(gs):
 H={identity};todo=[identity]
 while todo:
  for g in gs:
   x=perm_mul(todo[0],g)
   if x not in H:H.add(x);todo.append(x)
  todo.pop(0)
 return H
H=generate([perm_mul(cyc(1,2),cyc(3,4))]);HB=generate([cyc(0,1,2),perm_mul(cyc(1,2),cyc(3,4))]);HQ=generate([cyc(1,3,2,4)])
def rep(p,H):return min(perm_mul(p,h) for h in H)
edges=sorted({rep(p,H) for p in perms});B=sorted({rep(p,HB) for p in perms});Q=sorted({rep(p,HQ) for p in perms})
vertices=[('B',p) for p in B]+[('Q',p) for p in Q]
ends=[(('B',rep(p,HB)),('Q',rep(p,HQ))) for p in edges]
def points(p,r):
 arr=[None,-I*r,I*r,C3(-1),C3(1)];p_inv=[p.index(j) for j in range(5)]
 return normalize([arr[j] for j in p_inv])
coordinates={}
for p,(s,t) in zip(edges,ends):
 ps,pt=points(p,Q3(0,F(1,3))),points(p,Q3(1))
 for v,c in ((s,ps),(t,pt)):
  if v in coordinates:assert coordinates[v]==c
  coordinates[v]=c
base=tuple(C3(k) for k in (0,1,10,20))
def avoids(s,t,obs):
 if s==t:return True
 for z in obs:
  u=(z-s)/(t-s)
  if u.im==Q3() and Q3()<=u.re<=Q3(1):return False
 return True
@lru_cache(None)
def transport(v):
 end=coordinates[v];path=[base];cur=list(base)
 for j in (2,3):
  target=end[j]
  if cur[j]==target:continue
  obs=[cur[k] for k in range(4) if k!=j]
  n=2
  while True:
   mid=C3(n,n*n)
   if avoids(cur[j],mid,obs) and avoids(mid,target,obs):break
   n+=1
  cur[j]=mid;path.append(tuple(cur));cur[j]=target;path.append(tuple(cur))
 assert tuple(cur)==end
 return tuple(path)
def projection(z):return z.re+z.im/37
def transverse(z):return z.im-z.re/37
def red(w):
 st=[]
 for x in w:
  if st and st[-1]==-x:st.pop()
  else:st.append(x)
 return tuple(st)
def inverse(w):return tuple(-x for x in reversed(w))
def concat(*ws):return red(x for w in ws for x in w)
def segment_braid(s,t):
 ps,pt=[projection(z) for z in s],[projection(z) for z in t]
 assert len(set(ps))==len(set(pt))==4
 order=sorted(range(4),key=lambda i:ps[i]);crossings=[]
 for i in range(4):
  for j in range(i+1,4):
   d0,d1=ps[i]-ps[j],pt[i]-pt[j]
   if d0.sign()!=d1.sign():crossings.append((-d0/(d1-d0),i,j))
 out=[]
 for tm,i,j in sorted(crossings):
  pi,pj=order.index(i),order.index(j)
  assert abs(pi-pj)==1,('non-adjacent',tm,i,j,order)
  left,right=(i,j) if pi<pj else (j,i)
  zl=s[left]+(t[left]-s[left])*C3(tm);zr=s[right]+(t[right]-s[right])*C3(tm)
  height=(transverse(zl)-transverse(zr)).sign();assert height
  index=min(pi,pj)+1
  out.append(index if height<0 else -index)
  order[pi],order[pj]=order[pj],order[pi]
 assert order==sorted(range(4),key=lambda i:pt[i])
 return tuple(out)
def path_braid(path):return concat(*(segment_braid(s,t) for s,t in zip(path,path[1:])))
@lru_cache(None)
def transport_braid(v):return path_braid(transport(v))
arrow_words=[]
for j,(p,(s,t)) in enumerate(zip(edges,ends),1):
 w=concat(transport_braid(s),segment_braid(coordinates[s],coordinates[t]),inverse(transport_braid(t)))
 arrow_words.append(w)
print('PASS all60 relabelled core paths,50 endpoint configurations,exact detour transports')
print('Raw based arrow braid lengths:',[len(w) for w in arrow_words])
# Rebuild BFS and compute all eleven core cycles as braid words.
adj={v:[] for v in vertices}
for i,(s,t) in enumerate(ends,1):adj[s].append((i,t));adj[t].append((-i,s))
paths={vertices[0]:()};todo=deque([vertices[0]]);tree=set()
while todo:
 v=todo.popleft()
 for i,w in sorted(adj[v],key=lambda q:abs(q[0])):
  if w not in paths:paths[w]=paths[v]+(i,);tree.add(abs(i));todo.append(w)
non=[i for i in range(1,61) if i not in tree]
cycles=[concat(paths[ends[i-1][0]],(i,),inverse(paths[ends[i-1][1]])) for i in non]
def eval_arrows(w):return concat(*(arrow_words[i-1] if i>0 else inverse(arrow_words[-i-1]) for i in w))
def subst(w,images):return concat(*(images[i-1] if i>0 else inverse(images[-i-1]) for i in w))
def gen_artin(i):
 j=abs(i);im=[(k,) for k in range(1,5)]
 if i>0:im[j-1]=(j,j+1,-j);im[j]=(j,)
 else:im[j-1]=(j+1,);im[j]=(-(j+1),j,j+1)
 return tuple(im)
@lru_cache(None)
def artin(w):
 im=tuple((j,) for j in range(1,5))
 for x in w:im=tuple(subst(v,gen_artin(x)) for v in im)
 return im
def A(i,j):return tuple(range(j-1,i,-1))+(i,i)+tuple(-k for k in range(i+1,j))
abxyz=[A(1,3),A(2,3),A(1,4),A(2,4),A(3,4)]
printed=[[1,2,4,5],[5],[1,2,5],[-5,-4,5],[1,3,5],[-5,-3,5],[-5,3,5],[-2,-5,-4],[-2,-1,-5,-4,-3],[1,2,3,4,5],[1]]
checks=[]
for j,(c,w) in enumerate(zip(cycles,printed),1):
 actual=eval_arrows(c);expected=subst(w,abxyz);ok=artin(actual)==artin(expected)
 checks.append(ok)
 print('PASS' if ok else 'FAIL','B37 g'+str(j),'actual length',len(actual),'expected length',len(expected))
 if not ok:
  print('actual word',actual);print('expected word',expected)
assert all(checks),'Geometric B37 table discrepancy'
result={'coordinates':{str(v):[z.serial() for z in coordinates[v]] for v in vertices},'edge_representatives':edges,'endpoints':[[str(s),str(t)] for s,t in ends],'arrow_braid_words':arrow_words,'cycles':cycles,'cycle_braid_words':[eval_arrows(c) for c in cycles],'B37_verified':checks}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('All eleven geometric B37 words verified exactly in the faithful Artin action.')

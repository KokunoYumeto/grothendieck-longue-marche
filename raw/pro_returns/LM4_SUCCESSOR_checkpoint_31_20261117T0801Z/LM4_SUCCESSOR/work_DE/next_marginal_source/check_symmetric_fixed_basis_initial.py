#!/usr/bin/env python3
"""Exact pointed involution and paired peripheral basis at q=9/25.
All meridian paths are literal rational polygons; Möbius images are read
against downward cuts using isolated rational quadratic roots.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,time
from weighted_stallings import WeightedFold,reduce_word as red,inverse as inv,substitute as sub,multiply as mulw
H=Path(__file__).resolve().parent
U=[tuple(map(F,x)) for x in json.loads((H/'symmetric_critical_deformation.json').read_text())['coefficient_points']]
zero=(F(0),F(0));one=(F(1),F(0));rot=(F(1),F(371,1000));rho=(F(1),F(1,100));q=F(9,25)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sb(a,b):return add(a,neg(b))
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def sc(c,a):return c*a[0],c*a[1]
def co(a):return a[0],-a[1]
def norm(a):return a[0]**2+a[1]**2
def dv(a,b):return sc(1/norm(b),cm(a,co(b)))
def enc(a):return [str(x) for x in a]
def mm(M,z):
 n1,n0,d1,d0=M;return dv(add(cm(n1,z),n0),add(cm(d1,z),d0))
physical=[zero,one,(q,F(0))]+U[1:]+[dv((q,F(0)),u) for u in U[1:]]+[dv(sb(u,(q,F(0))),sb(u,one)) for u in U[1:]]+[dv(sc(q,sb(one,u)),sb((q,F(0)),u)) for u in U[1:]]+[(F(3,5),F(0)),(-F(3,5),F(0))]
points=[cm(rot,z) for z in physical]
order=sorted(range(21),key=lambda i:points[i][0]);cuts=[points[i] for i in order]
assert len(set(p[0] for p in cuts))==21
source=cm(rot,(F(9,5),F(0)));assert source[0]>max(p[0] for p in cuts)
identity=(one,zero,zero,one)
involution=(rot,sc(-q,cm(rot,rot)),one,neg(rot))
assert mm(involution,source)==source
for p in points:
 if p!=rot:assert mm(involution,mm(involution,p))==p

def peval(p,x):return p[0]+x*(p[1]+x*p[2])
def mulint(a,b):
 vals=[x*y for x in a for y in b];return min(vals),max(vals)
def ieval(p,r):
 v=(p[2],p[2]);v=mulint(v,r);v=(v[0]+p[1],v[1]+p[1]);v=mulint(v,r);return v[0]+p[0],v[1]+p[0]
SCALE=10**90

def sqrtbox(d):
 a=isqrt(d.numerator*SCALE*SCALE//d.denominator)
 return F(a,SCALE),F(a+1,SCALE)
def real_roots(p):
 c,b,a=p
 if not a:
  if not b:return []
  r=-c/b;return [(r,r)] if 0<r<1 else []
 d=b*b-4*a*c
 if d<=0:return [] # a double contact contributes no cut crossing.
 l,h=sqrtbox(d);ans=[]
 for sign in (-1,1):
  r0=(-b+sign*l)/(2*a);r1=(-b+sign*h)/(2*a);lo,hi=min(r0,r1),max(r0,r1)
  if hi<=0 or lo>=1:continue
  assert 0<lo<=hi<1,('root meets endpoint',p,lo,hi)
  ans.append((lo,hi))
 return sorted(ans)

segment_records=[]
def read_segment(a,b,M,record=False):
 d=sb(b,a);n1,n0,d1,d0=M
 np0=add(cm(n1,a),n0);np1=cm(n1,d);dp0=add(cm(d1,a),d0);dp1=cm(d1,d)
 N=[cm(np0,co(dp0)),add(cm(np0,co(dp1)),cm(np1,co(dp0))),cm(np1,co(dp1))]
 D=[norm(dp0),2*cm(dp0,co(dp1))[0],norm(dp1)]
 minimum=min(peval(D,F(0)),peval(D,F(1)))
 if D[2]:
  t=-D[1]/(2*D[2])
  if 0<t<1:minimum=min(minimum,peval(D,t))
 assert minimum>0,'path meets Mobius pole'
 events=[]
 for j,p in enumerate(cuts,1):
  R=tuple(N[k][0]-p[0]*D[k] for k in range(3));J=tuple(N[k][1]-p[1]*D[k] for k in range(3))
  for endpoint in (F(0),F(1)):
   if peval(R,endpoint)==0:assert peval(J,endpoint)>0,('cut endpoint below puncture',j,a,b)
  for r in real_roots(R):
   lo,hi=ieval(J,r)
   assert lo>0 or hi<0,('unresolved puncture height',j,r)
   if lo>0:continue
   dl,dh=ieval((R[1],2*R[2],F(0)),r)
   assert dl>0 or dh<0
   events.append((r,j if dl>0 else -j))
 events.sort()
 for x,y in zip(events,events[1:]):assert x[0][1]<y[0][0]
 if record:segment_records.append({'start':enc(a),'end':enc(b),'denominator_minimum':str(minimum),'events':[{'root':[str(x) for x in r],'letter':j} for r,j in events]})
 return tuple(j for r,j in events)

def read_path(path,M,record=False):return red(j for a,b in zip(path,path[1:]) for j in read_segment(a,b,M,record))
def loop_path(p,base,delta,top):
 B=(base[0],top);up=(p[0]+delta,top);r=(p[0]+delta,p[1])
 return [base,B,up,r,(p[0]+delta,p[1]+delta),(p[0]-delta,p[1]+delta),(p[0]-delta,p[1]-delta),(p[0]+delta,p[1]-delta),r,up,B,base]
start=time.monotonic();gap=min(b[0]-a[0] for a,b in zip(cuts,cuts[1:]));delta=min(F(1,100),gap/8);top=max(p[1] for p in cuts)+1
A={};paths=[]
for j,p in enumerate(cuts,1):
 path=loop_path(p,source,delta,top);assert read_path(path,identity)==(j,)
 A[j]=read_path(path,involution,True);paths.append(path)
for j in range(1,22):assert sub(A[j],A)==(j,),('involution square',j)
print('PASS: all21 cut meridians and exact pointed Mobius images; F^2=id.',flush=True)
# Peripheral abelianizations provide an additional literal-label check.
for j,phys in enumerate(order,1):
 ab=[A[j].count(k)-A[j].count(-k) for k in range(1,22)]
 if phys==1:assert ab==[-1]*21
 else:
  target=mm(involution,points[phys]);k=points.index(target);assert ab==[int(order[x]==k) for x in range(21)]
print('PASS: every peripheral image has the exact F permutation; v=1 maps to the infinity peripheral.',flush=True)
# Right-half-plane paired system in eta=rho*(v-9/5)/(v-1/5).
xi=(one,(-F(9,5),F(0)),one,(-F(1,5),F(0)))
etaM=(rho,sc(-F(9,5),rho),one,(-F(1,5),F(0)))
right=[]
for name,v in [('old_plus1',None),('old_plus3',(-F(3,5),F(0))),('old_plus9',zero)]+[(f'A_{i}',physical[i]) for i in range(3,11)]:
 e=rho if v is None else mm(etaM,v)
 assert e[0]>0
 right.append((name,e))
right.sort(key=lambda x:x[1][0]);assert len(set(e[0] for n,e in right))==11
# v= (9*rho-eta)/(5*(rho-eta)); then rotate by the original ROT.
back=(neg(rot),sc(9,cm(rot,rho)),(-F(5),F(0)),sc(5,rho))
assert mm(back,zero)==source
rgap=min(b[1][0]-a[1][0] for a,b in zip(right,right[1:]));rd=min(F(1,100),rgap/8,min(e[0] for n,e in right)/8);rt=max(e[1] for n,e in right)+1
rightwords=[]
for name,e in right:
 path=loop_path(e,zero,rd,rt);w=read_path(path,back,True);rightwords.append((name,w,path))
X=mulw(*(w for n,w,p in rightwords))
assert sub(X,A)==inv(X),('right-boundary inverse relation',X,sub(X,A))
remove=next(i for i,(n,w,p) in enumerate(rightwords) if n=='old_plus9')
paired=[('axis',X)]+[(n,w) for i,(n,w,p) in enumerate(rightwords) if i!=remove]+[(n+'_F',sub(w,A)) for i,(n,w,p) in enumerate(rightwords) if i!=remove]
assert len(paired)==21
fold=WeightedFold([w for n,w in paired]);inverse={j:fold.rewrite((j,)) for j in range(1,22)}
assert all(w is not None for w in inverse.values())
forward={j:w for j,(n,w) in enumerate(paired,1)}
for j in range(1,22):assert sub(forward[j],inverse)==(j,)
assert sub(sub(forward[1],A),inverse)==(-1,)
for j in range(2,12):
 assert sub(sub(forward[j],A),inverse)==(j+10,)
 assert sub(sub(forward[j+10],A),inverse)==(j,)
print('PASS: actual right/left half-plane meridians give a21-word Nielsen basis; all42 inverse substitutions checked.',flush=True)
print('PASS: F in this basis inverts the axis and swaps ten pairs literally.',flush=True)
# Filling deletes exactly the eight added pairs. Retained pair indices
# are recorded explicitly, so the old-F5 Schreier conversion is concrete.
retained=[1]+[j for j,(n,w) in enumerate(paired,1) if n.startswith('old_')]
assert len(retained)==5
old_positions=[j for j,p in enumerate(order,1) if p in (0,1,2,19,20)]
fill_old={j:((old_positions.index(j)+1,) if j in old_positions else ()) for j in range(1,22)}
for j,(name,w) in enumerate(paired,1):
 if j not in retained:assert not sub(w,fill_old)
oldwords=[sub(forward[j],fill_old) for j in retained]
oldfold=WeightedFold(oldwords);oldinverse={j:oldfold.rewrite((j,)) for j in range(1,6)}
assert all(w is not None for w in oldinverse.values())
print('PASS: filling kills precisely eight swapped pairs and retains an explicit F5 basis.',flush=True)
out={'q':'9/25','source_v':'9/5','other_fixed_v':'1/5','rotation':enc(rot),'pairing_rotation':enc(rho),'physical_points':[enc(p) for p in physical],'original_generator_physical_order':order,'cut_basepoint':enc(source),'cut_delta':str(delta),'cut_top':str(top),'cut_paths':[[enc(p) for p in path] for path in paths],'involution_images':{str(j):list(w) for j,w in A.items()},'right_meridians':[{'name':n,'word':list(w),'path_eta':[enc(e) for e in p]} for n,w,p in rightwords],'paired_basis':[{'name':n,'word':list(w)} for n,w in paired],'inverse_basis':{str(j):list(w) for j,w in inverse.items()},'retained_paired_indices':retained,'old_original_positions':old_positions,'old_basis_inverse':{str(j):list(w) for j,w in oldinverse.items()},'exact_segment_records':segment_records,'elapsed_seconds':time.monotonic()-start,'claims_excluded':['full fixed lifting','source image equality','completed infinite-basis comparison']}
(H/'symmetric_fixed_basis.json').write_text(json.dumps(out,indent=2)+'\n')
print('Elapsed seconds',round(time.monotonic()-start,3),flush=True)

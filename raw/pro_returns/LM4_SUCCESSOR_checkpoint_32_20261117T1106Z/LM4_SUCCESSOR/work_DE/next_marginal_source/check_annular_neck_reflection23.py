#!/usr/bin/env python3
"""Actual selected upper-gap disk reflection, exact Cayley cut calculation."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json,time
from weighted_stallings import WeightedFold, reduce_word as red, inverse as inv, substitute as sub
H=Path(__file__).resolve().parent;ROOT=H.parents[1]
zero=(F(0),F(0));one=(F(1),F(0));I=(F(0),F(1));rot=(F(1),F(371,1000))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sb(a,b):return add(a,neg(b))
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def sc(c,a):return c*a[0],c*a[1]
def co(a):return a[0],-a[1]
def norm(a):return a[0]**2+a[1]**2
def dv(a,b):return sc(1/norm(b),cm(a,co(b)))
def enc(z):return list(map(str,z))
raw=json.loads((H/'symmetric_critical_deformation.json').read_text())['coefficient_points']
U=[]
for z in raw[1:]:
    x,y=map(F,z);v=y/(1+x)
    U.append(((1-v*v)/(1+v*v),2*v/(1+v*v)))
assert all(norm(u)==1 for u in U)
q=(F(4,5),F(3,5))
physical=[zero,q]
for u in U:
    u2=cm(u,u);h=dv(add(u2,cm(sb(one,sc(2,u)),q)),add(q,sb(u2,sc(2,u))))
    assert norm(h)==1 and h[0]>0 and h[1]>0
    physical.append(cm(h,h))
assert all(norm(y)==1 and y[1]>0 for y in physical[1:])
points=[cm(rot,y) for y in physical]
order=sorted(range(6),key=lambda j:points[j][0]);assert order==[2,5,0,3,4,1]
cuts=[points[j] for j in order];base=(F(10),F(0))
identity=(one,zero,zero,one)
# xi=i*(y+1)/(y-1); inverse y=(xi+i)/(xi-i).
M=(rot,cm(rot,I),one,neg(I))
def mm(A,z):
 a,b,c,d=A;return dv(add(cm(a,z),b),add(cm(c,z),d))
assert mm(M,zero)==neg(rot)
def peval(p,x):return p[0]+x*(p[1]+x*p[2])
def mulint(a,b):
 vals=[x*y for x in a for y in b];return min(vals),max(vals)
def ieval(p,r):
 v=mulint((p[2],p[2]),r);v=(v[0]+p[1],v[1]+p[1]);v=mulint(v,r)
 return v[0]+p[0],v[1]+p[0]
SCALE=10**80
def sqrtbox(d):
 a=isqrt(d.numerator*SCALE*SCALE//d.denominator);return F(a,SCALE),F(a+1,SCALE)
def roots(p):
 c,b,a=p
 if not a:
  if not b:return []
  x=-c/b;return [(x,x)] if 0<x<1 else []
 disc=b*b-4*a*c
 if disc<=0:return []
 l,h=sqrtbox(disc);ans=[]
 for sign in(-1,1):
  aa=(-b+sign*l)/(2*a);bb=(-b+sign*h)/(2*a);lo,hi=min(aa,bb),max(aa,bb)
  if hi<=0 or lo>=1:continue
  assert 0<lo<=hi<1
  ans.append((lo,hi))
 return sorted(ans)
records=[];contacts=[]
def read_segment(a,b,A):
 d=sb(b,a);n1,n0,d1,d0=A
 n=add(cm(n1,a),n0);nd=cm(n1,d);den=add(cm(d1,a),d0);dd=cm(d1,d)
 N=[cm(n,co(den)),add(cm(n,co(dd)),cm(nd,co(den))),cm(nd,co(dd))]
 D=[norm(den),2*cm(den,co(dd))[0],norm(dd)]
 mi=min(peval(D,F(0)),peval(D,F(1)))
 if D[2]:
  t=-D[1]/(2*D[2])
  if 0<t<1:mi=min(mi,peval(D,t))
 assert mi>0,'Mobius pole hit'
 ev=[]
 for j,p in enumerate(cuts,1):
  R=tuple(N[k][0]-p[0]*D[k] for k in range(3));J=tuple(N[k][1]-p[1]*D[k] for k in range(3))
  if not any(R):
   mn=min(peval(J,F(0)),peval(J,F(1)))
   if J[2]:
    t=-J[1]/(2*J[2])
    if 0<t<1:mn=min(mn,peval(J,t))
   assert mn>0,'unhandled vertical cut'
  if R[2] and R[1]**2-4*R[2]*R[0]==0:
   t=-R[1]/(2*R[2])
   if 0<=t<=1:assert peval(J,t)!=0;contacts.append((j,str(t)))
  for t in(F(0),F(1)):
   if peval(R,t)==0:assert peval(J,t)>0,'cut endpoint below puncture'
  for box in roots(R):
   lo,hi=ieval(J,box);assert lo>0 or hi<0
   if lo>0:continue
   dl,dh=ieval((R[1],2*R[2],F(0)),box);assert dl>0 or dh<0
   ev.append((box,j if dl>0 else -j))
 ev.sort()
 for x,y in zip(ev,ev[1:]):assert x[0][1]<y[0][0]
 records.append({'a':enc(a),'b':enc(b),'min_den':str(mi),'events':[{'root':list(map(str,box)),'letter':j}for box,j in ev]})
 return tuple(j for box,j in ev)
def read(poly,A):return tuple(red(j for a,b in zip(poly,poly[1:]) for j in read_segment(a,b,A)))
alpha=[base,(F(10),F(5)),(-F(2),F(5)),(-F(2),-F(742,1000)),neg(rot)]
aw=read(alpha,identity)
# All ordinary physical labels ordered on the upper unit arc from -1 to+1.
selected=[2,5,3,4,1]
xis=[]
for j in selected:
 z=cm(I,dv(add(physical[j],one),sb(physical[j],one)))
 assert z[1]==0 and z[0]>0
 xis.append(z[0])
assert all(a<b for a,b in zip(xis,xis[1:]))
delta=min([xis[0]]+[b-a for a,b in zip(xis,xis[1:])])/8
entry=xis[0]/4;top=F(1)
Dwords=[];paths=[]
for x in xis:
 arc=[zero,(entry,F(0)),(entry,top),(x+delta,top),(x+delta,F(0))]
 local=[arc[-1],(x+delta,delta),(x-delta,delta),(x-delta,-delta),(x+delta,-delta),arc[-1]]
 poly=arc+local[1:]+list(reversed(arc))[1:]
 w=tuple(red(aw+read(poly,M)+tuple(inv(aw))))
 assert 3 not in map(abs,w),('cone enters upper-disk word',w)
 Dwords.append(w);paths.append(poly)
# Endpoint ordinary positions are1,2,4,5,6. Relabel only that subgroup.
ordinary=[1,2,4,5,6];ren={x:(j+1,) for j,x in enumerate(ordinary)}
forward={j+1:tuple(sub(w,ren)) for j,w in enumerate(Dwords)}
fold=WeightedFold(list(forward.values()))
back={j:fold.rewrite((j,)) for j in range(1,6)}
assert all(w is not None for w in back.values())
for j in range(1,6):
 assert tuple(sub(forward[j],back))==(j,)
 assert tuple(sub(back[j],forward))==(j,)
reflection={j:tuple(range(1,j))+(-j,)+tuple(inv(tuple(range(1,j)))) for j in range(1,6)}
eta={j:tuple(sub(sub(back[j],reflection),forward)) for j in range(1,6)}
for j in range(1,6):assert tuple(sub(eta[j],eta))==(j,)
assert tuple(sub((1,2,3,4,5),eta))==(-5,-4,-3,-2,-1)
# Old K order O=(x1,x3,x4,x5,x6); the separate bridge cert must identify it
# with the same physical ordinary order before this is called the actual eta.
old_to_Y={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
Y_to_old={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
for j in range(1,6):
 assert tuple(sub(old_to_Y[j],Y_to_old))==(j,)
 assert tuple(sub(Y_to_old[j],old_to_Y))==(j,)
etaY={j:tuple(sub(sub(Y_to_old[j],eta),old_to_Y)) for j in range(1,6)}
for j in range(1,6):assert tuple(sub(etaY[j],etaY))==(j,)
out={'status':'PASS_ENDPOINT_AND_BASIS','q':['4/5','3/5'],'unit_rational_u':[enc(u)for u in U],
 'endpoint_physical_order':order,'ordinary_physical_order':selected,'cut_points':[enc(p)for p in cuts],
 'upper_connector':[enc(z)for z in alpha],'upper_connector_cut_word':aw,
 'xi_punctures':list(map(str,xis)),'xi_delta':str(delta),
 'xi_paths':[[enc(z)for z in path]for path in paths],
 'xi_basis_in_endpoint_full_cuts':Dwords,'xi_basis_in_ordinary_cuts':forward,'ordinary_cuts_in_xi_basis':back,
 'reflection_xi_basis':reflection,'eta_ordinary_cuts':eta,'eta_adapted_K_basis_a_barb_d_e_f':etaY,
 'exact_segment_records':records,'tangent_contacts':contacts,
 'scope':'Endpoint upper-gap Cayley calculation and exact inverse bases. Actual q_b bridge and true-root deformation recorded in separate companion.'}
(H/'annular_neck_reflection23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact unit-circle endpoint, all Mobius root/height tests, upper-gap basis and ten inverse substitutions')
print('upper connector',aw,'xi basis',forward)
print('eta ordinary cuts',eta)
print('eta in(a,barb,d,e,f)',etaY)

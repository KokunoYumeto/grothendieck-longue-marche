#!/usr/bin/env python3
"""Actual rational13-to7 covering comparison at q=9/25."""
from pathlib import Path
from fractions import Fraction as F
import json,time
import sympy as S
from weighted_stallings import WeightedFold,reduce_word as red,inverse as inv,substitute as sub,multiply as mw
H=Path(__file__).resolve().parent
D=json.loads((H/'symmetric_fixed_basis.json').read_text());U=[tuple(map(F,p)) for p in json.loads((H/'symmetric_critical_deformation.json').read_text())['coefficient_points']]
q=F(9,25);R=(F(1),F(371,1000));one=(F(1),F(0));zero=(F(0),F(0))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sc(t,a):return t*a[0],t*a[1]
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a):return a[0],-a[1]
def norm(a):return a[0]**2+a[1]**2
def dv(a,b):return sc(1/norm(b),cm(a,conj(b)))
def enc(a):return [str(x) for x in a]
physical=[tuple(map(F,p)) for p in D['physical_points']]
kept=list(range(11))+[19,20];vorder=sorted(kept,key=lambda j:cm(R,physical[j])[0]);vp=[cm(R,physical[j]) for j in vorder]
tphysical=[sc(F(1,2),add(u,dv((q,F(0)),u))) for u in U]+[(F(3,5),F(0)),(-F(3,5),F(0))]
torder=sorted(range(7),key=lambda j:cm(R,tphysical[j])[0]);cuts=[cm(R,tphysical[j]) for j in torder]
assert len(set(p[0] for p in cuts))==7
base=cm(R,(F(9,5),F(0)));gap=min(b[0]-a[0] for a,b in zip(vp,vp[1:]));delta=min(F(1,100),gap/8);top=max(p[1] for p in vp)+1

def loop(p):
 B=(base[0],top);up=(p[0]+delta,top);r=(p[0]+delta,p[1]);return [base,B,up,r,(p[0]+delta,p[1]+delta),(p[0]-delta,p[1]+delta),(p[0]-delta,p[1]-delta),(p[0]+delta,p[1]-delta),r,up,B,base]
def pconv(a,b):
 out=[zero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=add(out[i+j],cm(x,y))
 return out

def pint(p,box):
 lo=hi=F(0)
 for c in reversed(p):
  vals=[lo*box[0],lo*box[1],hi*box[0],hi*box[1]];lo,hi=min(vals)+c,max(vals)+c
 return lo,hi
X=S.symbols('X');eps=S.Rational(1,10**70);records=[]

def segment(a,b):
 d=(b[0]-a[0],b[1]-a[1]);num=[add(cm(a,a),sc(q,cm(R,R))),sc(2,cm(a,d)),cm(d,d)];den=[sc(2,a),sc(2,d)]
 N=pconv(num,[conj(v) for v in den]);DD=pconv(den,[conj(v) for v in den]);Q=[v[0] for v in DD]+[F(0)]
 assert all(v[1]==0 for v in DD)
 at=-Q[1]/(2*Q[2]) if Q[2] else F(0);assert min(pint(Q,(F(0),F(0)))[0],pint(Q,(F(1),F(1)))[0],pint(Q,(at,at))[0] if 0<at<1 else Q[0])>0
 events=[]
 for j,p in enumerate(cuts,1):
  rp=[N[k][0]-p[0]*Q[k] for k in range(4)];ip=[N[k][1]-p[1]*Q[k] for k in range(4)]
  poly=S.Poly(sum(S.Rational(v.numerator,v.denominator)*X**k for k,v in enumerate(rp)),X)
  if poly.is_zero:assert pint(ip,(F(0),F(1)))[0]>0;continue
  for end in (F(0),F(1)):
   if poly.eval(end)==0:assert pint(ip,(end,end))[0]>0
  for (lo,hi),m in poly.intervals(eps=eps):
   lo,hi=F(int(S.numer(lo)),int(S.denom(lo))),F(int(S.numer(hi)),int(S.denom(hi)))
   if hi<=0 or lo>=1:continue
   assert 0<lo<=hi<1
   jl,jh=pint(ip,(lo,hi));assert jl>0 or jh<0
   if jl>0 or m%2==0:continue
   dp=[rp[k]*k for k in range(1,4)];dl,dh=pint(dp,(lo,hi));assert dl>0 or dh<0
   events.append(((lo,hi),j if dl>0 else -j))
 events.sort()
 for x,y in zip(events,events[1:]):assert x[0][1]<y[0][0]
 records.append({'start':enc(a),'end':enc(b),'crossings':[{'interval':[str(t) for t in box],'letter':j} for box,j in events]})
 return tuple(j for box,j in events)
start=time.monotonic();images={}
for j,p in enumerate(vp,1):
 path=loop(p);images[j]=red(x for a,b in zip(path,path[1:]) for x in segment(a,b))
 phys=vorder[j-1];ab=[images[j].count(k)-images[j].count(-k) for k in range(1,8)]
 if phys==0:expected=[-1]*7
 else:
  target=0 if phys in (1,2) else phys-2 if phys in range(3,7) else phys-6 if phys in range(7,11) else 5 if phys==19 else 6
  expected=[(2 if phys in (19,20) else 1) if torder[k]==target else 0 for k in range(7)]
 assert ab==expected,('cover peripheral',phys,images[j],ab,expected)
print('PASS: actual13 meridian images under T=(v+q/v)/2, with all peripheral degrees/labels.',flush=True)
# Standard rank13 Schreier basis of the index-two branch-character kernel.
chi={j:int(torder[j-1] in (5,6)) for j in range(1,8)};r=next(j for j in chi if torder[j-1]==5)
sch=[];table={}
for state in (0,1):
 for j in range(1,8):
  nxt=state^chi[j];w=red(((r,) if state else ())+ (j,) + ((-r,) if nxt else ()))
  if w:sch.append(w);table[state,j]=len(sch)
  else:table[state,j]=0
assert len(sch)==13

def rewrite(w):
 state=0;out=[]
 for a in w:
  j=abs(a);nxt=state^chi[j];k=table[(state if a>0 else nxt),j]
  if k:out.append(k if a>0 else -k)
  state=nxt
 assert state==0
 ans=red(out);assert sub(ans,{i+1:w for i,w in enumerate(sch)})==red(w)
 return ans
rewritten=[rewrite(images[j]) for j in range(1,14)];fold=WeightedFold(rewritten);back={j:fold.rewrite((j,)) for j in range(1,14)}
assert all(w is not None for w in back.values());forward={j+1:w for j,w in enumerate(rewritten)}
for j in range(1,14):assert sub(forward[j],back)==(j,) and sub(back[j],forward)==(j,)
print('PASS: image is precisely the actual index-two F13 kernel; all26 inverse basis substitutions.',flush=True)
# Actual straight q bridge in the T model, using original engine with
# sourceT=1 rightmost. Its raw crossings are retained and interpreted
# with the now-calibrated chronological convention.
from tangent_bundle_braid import Segment,Q as QQ
bridge=Segment(QQ(1,100),QQ(9,25)).compute();assert bridge['initial_order'][-1]==bridge['final_order'][-1]==5
assert [j if j<5 else j-1 for j in bridge['final_order'][:-1]]==torder
assert all(abs(g)<7 for g in bridge['word'])

def art(w,n=7):
 A={j:(j,) for j in range(1,n+1)}
 for g in w:
  i=abs(g);a,b=A[i],A[i+1];A[i],A[i+1]=(mw(a,b,inv(a)),a) if g>0 else (b,mw(inv(b),a,b))
 return A
pull=art(tuple(-g for g in bridge['word']));push=art(tuple(reversed(bridge['word'])))
for j in range(1,8):assert sub(pull[j],push)==(j,) and sub(push[j],pull)==(j,)
Comp=json.loads((H/'B81_pointed_compensation.json').read_text());C={int(j):tuple(w) for j,w in Comp['basis_C_actual_cut_to_old_inverse_push'].items()}
oldcoords={j:sub(sub(w,pull),C) for j,w in images.items()}
out={'q':'9/25','v_base':'9/5','T_base':'1','v_generator_physical_order':vorder,'T_generator_physical_order':torder,'cover_images':{str(j):list(w) for j,w in images.items()},'branch_character':chi,'Schreier_basis':sch,'cover_images_in_Schreier_basis':rewritten,'inverse_cover_basis':{str(j):list(w) for j,w in back.items()},'T_bridge':bridge,'images_in_B81_original_Birman_coordinates':{str(j):list(w) for j,w in oldcoords.items()},'exact_segment_records':records,'elapsed_seconds':time.monotonic()-start,'scope':'actual covering and original B81 fiber-coordinate comparison; old action compatibility is separately audited directly on its eight-strand paths'}
(H/'symmetric_to_tangent_cover.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact T-bridge carries all13 images into B81 original intrinsic Birman coordinates.',flush=True)
print('Elapsed seconds',round(time.monotonic()-start,3),flush=True)

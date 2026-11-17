#!/usr/bin/env python3
"""Independent upper/lower gap cut comparison; actual selected lift is reviewed geometrically."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
src=P/'annular_gap_cone23.json'; D=json.loads(src.read_text())
pts=[tuple(map(Q,z)) for z in D['rational_projected_punctures']]
def pt(x,y=0):return(Q(x),Q(y))
def red(w,c=0):
 o=[]
 for x in w:
  if c and abs(x)==c:x=c
  if o and (o[-1]==-x or c and o[-1]==x==c):o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w):return tuple(-x for x in w[::-1])
events=[]
def read(path,tag):
 w=[]
 for a,b in zip(path,path[1:]):
  dx,dy=b[0]-a[0],b[1]-a[1];ev=[]
  for j,p in enumerate(pts,1):
   for z in(a,b):
    if z[0]==p[0]:assert z[1]>p[1],('endpoint cut',tag,j)
   if dx:
    s=(p[0]-a[0])/dx
    if 0<=s<=1:assert a[1]+s*dy!=p[1],('puncture',tag,j)
    if 0<s<1 and a[1]+s*dy<p[1]:ev.append((s,j if dx>0 else -j,p[1]-a[1]-s*dy))
   elif a[0]==p[0]:assert not min(a[1],b[1])<=p[1]<=max(a[1],b[1])
  ev.sort();w.extend(e[1] for e in ev)
  events.append({'tag':tag,'a':list(map(str,a)),'b':list(map(str,b)),
   'events':[{'s':str(s),'letter':j,'height_gap':str(g)} for s,j,g in ev]})
 return red(w)
e=Q(1,1000); base=pt(10); end=pt(-e)
lower=[base,pt(10,-2),pt(-e,-2),end]
upper=[base,pt(10,5),pt(-2,5),pt(-2,-Q(742,1000)),pt(-e,-Q(371,1000)*e),end]
circle=[end,pt(-e,-e),pt(e,-e),pt(e,e),pt(-e,e),end]
u=read(upper,'upper');l=read(lower,'lower');c=read(circle,'positive_cone')
assert u==(1,) and l==(-6,-5,-4,-3,-2) and c==(2,)
B=red(u+inv(l));assert B==(1,2,3,4,5,6)
cu=red(u+c+inv(u));cl=red(l+c+inv(l))
assert cu==(1,2,-1)
assert red(B+cl+inv(B))==cu
basis=P/'inner_q0_adapted_basis22.json';E=json.loads(basis.read_text())
A={int(k):tuple(v) for k,v in E['old_in_Y'].items()}
def sub(w):return red((y for x in w for y in(A[abs(x)] if x>0 else inv(A[-x]))),3)
cuY=sub(cu);assert cuY==(1,3,-1)
# Exact lift convention: upper section connector increases arg(y) to +pi,
# lower decreases to -pi. Principal z=sqrt(y) therefore ends +i/-i.
assert all(p[1]<Q(5) for p in pts)
out={'status':'PASS','input_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in(src,basis)},
 'upper_whisker':[list(map(str,z)) for z in upper],'lower_whisker':[list(map(str,z)) for z in lower],
 'upper_whisker_word':u,'lower_whisker_word':l,'positive_local_cone':c,
 'upper_minus_lower_word':B,'lower_cone_word':cl,'upper_cone_word':cu,'upper_cone_in_Y':cuY,
 'events':events,'lift_endpoints':{'upper':{'z':'+i','t':'-i'},'lower':{'z':'-i','t':'+i'}},
 'scope':'Exact cut and basis identities; upper-collar section/common selected-disk comparison is separately retained in the geometric supplement and independent DE review.'}
(P/'annular_upper_gap_cone23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS independent exact Fraction upper/lower cut paths')
print('upper whisker = x1; lower whisker = x6^-1 x5^-1 x4^-1 x3^-1 x2^-1')
print('upper minus lower = positive full boundary x1 x2 x3 x4 x5 x6')
print('c_upper = x1 x2 x1^-1 = a C a^-1')
print('Upper/lower principal lift endpoints retained as (+i,-i)/(−i,+i) in (z,t)')

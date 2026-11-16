#!/usr/bin/env python3
"""Exact PL positive half-twist check for downward-cut meridians."""
from fractions import Fraction as F
from pathlib import Path
import json
H=Path(__file__).resolve().parent

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def sc(t,a):return t*a[0],t*a[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def ori(a,b,c):return cross(sub(b,a),sub(c,a))
def rot(a):return -a[1],a[0]
def red(w):
 r=[]
 for a in w:
  if r and r[-1]==-a:r.pop()
  else:r.append(a)
 return r
unit=[(F(1),F(0)),(F(0),F(1)),(-F(1),F(0)),(F(0),-F(1))]
inner=[sc(F(2),a) for a in unit];outer=[sc(F(6),a) for a in unit]
tri=[]
for k in range(4):
 j=(k+1)%4
 tri += [((inner[k],outer[k],outer[j]),(rot(inner[k]),outer[k],outer[j])),((inner[k],outer[j],inner[j]),(rot(inner[k]),outer[j],rot(inner[j])))]
for a,b in tri:assert ori(*a)>0 and ori(*b)>0
# The linear inner-vertex interpolation defines an isotopy: triangle
# signed areas are either24 or8+8*t*(1-t), positive on[0,1].
for source,target in tri:
 vals=[]
 for t in (F(0),F(1,2),F(1)):
  v=[add(sc(1-t,a),sc(t,b)) for a,b in zip(source,target)];vals.append(ori(*v))
 assert vals in ([F(24),F(24),F(24)],[F(8),F(10),F(8)])

def bary(p,t):
 a,b,c=t;den=ori(a,b,c);v=ori(a,p,c)/den;w=ori(a,b,p)/den
 return 1-v-w,v,w

def T(p):
 r=abs(p[0])+abs(p[1])
 if r<=2:return rot(p)
 if r>=6:return p
 answers=[]
 for a,b in tri:
  lam=bary(p,a)
  if min(lam)>=0:answers.append(tuple(sum(lam[j]*b[j][i] for j in range(3)) for i in range(2)))
 assert answers and len(set(answers))==1
 return answers[0]
edges=set()
for a,b in tri:
 for x,y in zip(a,a[1:]+a[:1]):edges.add(tuple(sorted((x,y))))

def map_segment(a,b):
 d=sub(b,a);ts={F(0),F(1)}
 for c,e in edges:
  f=sub(e,c);den=cross(d,f)
  if den:
   t=cross(sub(c,a),f)/den;s=cross(sub(c,a),d)/den
   if 0<t<1 and 0<=s<=1:ts.add(t)
 return [T(add(a,sc(t,d))) for t in sorted(ts)]
def map_path(path):
 out=[]
 for a,b in zip(path,path[1:]):
  part=map_segment(a,b);out += part if not out else part[1:]
 return out

def loop(p):
 b=(F(8),F(8));top=F(10);e=F(10003,100000);B=(b[0],top);u=(p[0]+e,top);r=(p[0]+e,p[1])
 return [b,B,u,r,(p[0]+e,p[1]+e),(p[0]-e,p[1]+e),(p[0]-e,p[1]-e),(p[0]+e,p[1]-e),r,u,B,b]
points=[(-F(1),F(0)),(F(1),F(0))]
def read(path):
 out=[]
 for a,b in zip(path,path[1:]):
  if a==b:continue
  events=[]
  for j,p in enumerate(points,1):
   if b[0]==a[0]:
    assert a[0]!=p[0] or min(a[1],b[1])>p[1]
    continue
   t=(p[0]-a[0])/(b[0]-a[0])
   if 0<t<1:
    y=a[1]+t*(b[1]-a[1])
    assert y!=p[1]
    if y<p[1]:events.append((t,j if b[0]>a[0] else -j))
   if t in (0,1):assert (a[1] if t==0 else b[1])>p[1]
  out += [j for t,j in sorted(events)]
 return red(out)
rows=[]
for j,p in enumerate(points,1):
 path=loop(p);assert read(path)==[j]
 mapped=map_path(map_path(path));word=read(mapped)
 expected=[1,2,-1] if j==1 else [1]
 assert word==expected
 rows.append({'generator':j,'image':word,'mapped_polygon':[[str(x) for x in a] for a in mapped]})
out={'construction':'two quarter twists; inner diamond radius2 rotates90 degrees, outer diamond radius6 fixed, intervening8 triangles affine','isotopy_areas':['24','8+8*t*(1-t)'],'puncture_motion':'left puncture passes below under the positive CCW half twist','images':rows}
(H/'cut_Artin_convention.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all PL triangles preserve orientation throughout the exact quarter-twist isotopy.')
print('PASS: the positive CCW half twist sends left-below; downward-cut meridians transform x1->x1*x2*x1^-1, x2->x1.')

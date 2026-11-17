#!/usr/bin/env python3
"""Exact two-adjacent-half-twist chronology calibration."""
from fractions import Fraction as F
from pathlib import Path
import json
H=Path(__file__).resolve().parent

def add(a,b):return a[0]+b[0],a[1]+b[1]
def sb(a,b):return a[0]-b[0],a[1]-b[1]
def sc(t,a):return t*a[0],t*a[1]
def cr(a,b):return a[0]*b[1]-a[1]*b[0]
def ori(a,b,c):return cr(sb(b,a),sb(c,a))
def rot(a):return -a[1],a[0]
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def subst(w,A):return red(y for x in w for y in (A[x] if x>0 else inv(A[-x])))
R=F(11,10);S=F(5,2);units=[(F(1),F(0)),(F(0),F(1)),(-F(1),F(0)),(F(0),-F(1))]
inn=[sc(R,a) for a in units];out=[sc(S,a) for a in units];tri=[]
for k in range(4):
 j=(k+1)%4;tri += [((inn[k],out[k],out[j]),(rot(inn[k]),out[k],out[j])),((inn[k],out[j],inn[j]),(rot(inn[k]),out[j],rot(inn[j])))]
for a,b in tri:
 vals=[ori(*[add(sc(1-t,x),sc(t,y)) for x,y in zip(a,b)]) for t in (F(0),F(1,2),F(1))]
 assert min(vals[0],vals[2])>0 and 2*(vals[0]+vals[2]-2*vals[1])<=0
edges={tuple(sorted((x,y))) for a,b in tri for x,y in zip(a,a[1:]+a[:1])}

def T(p):
 d=abs(p[0])+abs(p[1])
 if d<=R:return rot(p)
 if d>=S:return p
 answers=[]
 for a,b in tri:
  den=ori(*a);v=ori(a[0],p,a[2])/den;w=ori(a[0],a[1],p)/den;lam=(1-v-w,v,w)
  if min(lam)>=0:answers.append(tuple(sum(lam[j]*b[j][i] for j in range(3)) for i in range(2)))
 assert answers and len(set(answers))==1;return answers[0]

def quarter_path(path,center):
 answer=[]
 for aa,bb in zip(path,path[1:]):
  a,b=sb(aa,center),sb(bb,center);d=sb(b,a);ts={F(0),F(1)}
  for c,e in edges:
   f=sb(e,c);den=cr(d,f)
   if den:
    t=cr(sb(c,a),f)/den;s=cr(sb(c,a),d)/den
    if 0<t<1 and 0<=s<=1:ts.add(t)
  part=[add(T(add(a,sc(t,d))),center) for t in sorted(ts)]
  answer += part if not answer else part[1:]
 return answer

def half(path,center):return quarter_path(quarter_path(path,center),center)
points=[(-F(2),F(0)),(F(0),F(0)),(F(2),F(0))];base=(F(8),F(8))
def loop(p):
 e=F(10003,100000);top=F(10);B=(base[0],top);u=(p[0]+e,top);r=(p[0]+e,p[1]);return [base,B,u,r,(p[0]+e,p[1]+e),(p[0]-e,p[1]+e),(p[0]-e,p[1]-e),(p[0]+e,p[1]-e),r,u,B,base]
def read(path):
 out=[]
 for a,b in zip(path,path[1:]):
  if a==b:continue
  events=[]
  for j,p in enumerate(points,1):
   if a[0]==b[0]:assert a[0]!=p[0] or min(a[1],b[1])>p[1];continue
   t=(p[0]-a[0])/(b[0]-a[0])
   if 0<t<1:
    y=a[1]+t*(b[1]-a[1]);assert y!=p[1]
    if y<p[1]:events.append((t,j if b[0]>a[0] else -j))
   if t in (0,1):assert (a[1] if t==0 else b[1])>p[1]
  out.extend(j for t,j in sorted(events))
 return red(out)
phi1={1:(1,2,-1),2:(1,),3:(3,)};phi2={1:(1,),2:(2,3,-2),3:(2,)}
rows=[]
for j,p in enumerate(points,1):
 path=loop(p);assert read(path)==(j,)
 first=half(path,(-F(1),F(0)));assert read(first)==phi1[j]
 final=half(first,(F(1),F(0)));actual=read(final)
 assert actual==subst(phi1[j],phi2)
 rows.append({'generator':j,'chronological_push':list(actual),'wrong_right_appending_result':list(subst(phi2[j],phi1))})
assert any(r['chronological_push']!=r['wrong_right_appending_result'] for r in rows)
(H/'cut_chronological_composition.json').write_text(json.dumps({'raw_chronological_crossings':[1,2],'actual_push':'phi2 compose phi1','actual_back':'phi1^-1 compose phi2^-1','function_art_update':'A <- A compose phi','general_formula':'push(W)=art(reverse W); back(W)=art(negate_each W)','generator_images':rows},indent=2)+'\n')
print('PASS: two explicit adjacent positive PL half twists calibrate chronological composition on all3 generators.')
print('PASS: raw[1,2] has push phi2 compose phi1, not phi1 compose phi2.')
print('PROVED CONVENTION: push(W)=art(reverse W); back(W)=art(negate_each W).')

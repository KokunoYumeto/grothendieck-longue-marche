#!/usr/bin/env python3
"""Based positive meridians for the actual two outer-pair arc classes."""
from fractions import Fraction as F
from pathlib import Path
import json
def red(w):
 out=[]
 for j in w:
  if out and out[-1]==-j:out.pop()
  else:out.append(j)
 return out
def inv(w):return [-j for j in reversed(w)]
def comm(a,b):return red(a+b+inv(a)+inv(b))
def pt(x,y):return (F(x),F(y))
cuts=[pt(j,0) for j in range(1,6)];events=[]
def segment(a,b):
 dx,dy=b[0]-a[0],b[1]-a[1];ee=[]
 for j,c in enumerate(cuts,1):
  # Every finite segment avoids every puncture exactly.
  if dx:
   t=(c[0]-a[0])/dx
   if 0<=t<=1:assert a[1]+t*dy!=0
  elif a[0]==c[0]:assert not min(a[1],b[1])<=0<=max(a[1],b[1])
  for z in (a,b):
   if z[0]==c[0]:assert z[1]>0
  if dx:
   t=(c[0]-a[0])/dx
   if 0<t<1 and a[1]+t*dy<0:ee.append((t,j if dx>0 else -j))
 ee.sort();events.append({'a':list(map(str,a)),'b':list(map(str,b)),'crossings':[[str(t),j] for t,j in ee]})
 return [j for _,j in ee]
def read(path):return red(j for a,b in zip(path,path[1:]) for j in segment(a,b))
base=pt(6,0);p=pt(F(1,2),0);eta=[base,pt(6,1),pt(F(1,2),1),p]
assert read(eta)==[]
eps=F(1,10)
def circle(j):
 # Positive square from its left midpoint.
 return [pt(j-eps,0),pt(j-eps,-eps),pt(j+eps,-eps),pt(j+eps,eps),pt(j-eps,eps),pt(j-eps,0)]
def lasso(path,j):
 cc=circle(j);assert path[-1]==cc[0]
 area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(cc,cc[1:]));assert area>0
 full=eta+path[1:]+cc[1:]+list(reversed(path))[1:]+list(reversed(eta))[1:]
 return read(full),full
aa,ap=lasso([p,pt(1-eps,0)],1)
up,upp=lasso([p,pt(F(1,2),F(1,2)),pt(5-eps,F(1,2)),pt(5-eps,0)],5)
dn,dnp=lasso([p,pt(F(1,2),-F(1,2)),pt(5-eps,-F(1,2)),pt(5-eps,0)],5)
assert aa==[1] and up==[5]
prefix=[1,2,3,4];middle=[2,3,4]
assert dn==prefix+[5]+inv(prefix)
raw_upper=comm(aa,up);raw_lower=comm(aa,dn)
normalized_lower=red([-1]+raw_lower+[1])
assert normalized_lower==comm([1],middle+[5]+inv(middle))
out={'status':'PASS','actual_order':['A2','A4','A3','branch_upper','B1'],
 'rotation':'z=-i Z, orientation preserving; right Z is lower z, left Z is upper z.',
 'flattening':'Any increasing real-axis homeomorphism to positions1..5, extended preserving the two half-planes; CE exact intervals certify the physical order.',
 'base':list(map(str,base)),'common_connector':[list(map(str,z)) for z in eta],
 'positive_cut_rule':'Downward rays; left-to-right crossing below puncture contributes +j.',
 'first_meridian':aa,'outer_upper_arc_second_meridian':up,'inner_lower_arc_second_meridian':dn,
 'outer_raw_commutator':raw_upper,'inner_raw_commutator':raw_lower,
 'inner_normalizing_whisker':[-1],'inner_normalized_commutator':normalized_lower,
 'middle_product':middle,'full_paths':{'first':ap,'outer':upp,'inner':dnp},'events':events}
out['full_paths']={k:[list(map(str,z)) for z in v] for k,v in out['full_paths'].items()}
Path(__file__).with_name('middle_neck_arc_words21.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS common connector and all exact segment/cut tests; positive meridians')
print('a',aa,'outer b',up,'inner b',dn)
print('outer relator',raw_upper)
print('inner raw relator',raw_lower)
print('inner conjugated by x1^-1',normalized_lower)

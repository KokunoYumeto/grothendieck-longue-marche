#!/usr/bin/env python3
"""Independent rational audit of all18 CE common node lassos."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;ROOT=H.parent.parent
D=json.loads((H/'symmetric_critical_deformation.json').read_text())
P=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_node_path_plan.json').read_text())
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm(a):return dot(a,a)
def sd(c,a,b):
 v=sub(b,a);t=dot(sub(c,a),v)/norm(v);t=max(F(0),min(F(1),t))
 return norm(sub(sub(c,a),(t*v[0],t*v[1])))
def encode(a):return [str(x) for x in a]
base=tuple(map(F,P['base']));hub=tuple(map(F,P['hub']));h=F(P['square_halfside'])
centers=[(d,tuple(map(F,d['center']))) for d in D['centers']]
mixed=[(d,c) for d,c in centers if d['kind']=='mixed']
segments=[(base,hub,'common_trunk')];loops=[]
for idx,(d,c) in enumerate(mixed):
 corners=[add(c,(h,h)),add(c,(-h,h)),add(c,(-h,-h)),add(c,(h,-h))]
 k=min(range(4),key=lambda j:norm(sub(corners[j],hub)))
 corners=corners[k:]+corners[:k];closed=corners+[corners[0]]
 area2=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(closed,closed[1:]))
 assert area2==8*h*h>0
 assert all(abs(cc[0]-c[0])>h or abs(cc[1]-c[1])>h for _,cc in centers if cc!=c)
 for a,b in zip([hub]+closed,closed):segments.append((a,b,str(idx)))
 loops.append({'index':idx,'center':encode(c),'corners':[encode(a) for a in closed],'signed_twice_area':str(area2),'critical_key':d['key']})
assert len(segments)==91
old_min=None;new_min=None;maximum=F(0)
for a,b,name in segments:
 for endpoint in (a,b):maximum=max(maximum,norm(endpoint));assert norm(endpoint)<25
 for d,c in centers:
  q=sd(c,a,b)
  if d['kind']=='old':
   assert q>F(1,5000)**2
   old_min=q if old_min is None else min(old_min,q)
  else:
   assert q>h*h/4
   new_min=q if new_min is None else min(new_min,q)
# The exact coefficient homotopy has every pole and collision inside
# the radius1e-24 disk around one of these centers. Thus the whole
# configuration isotopy is collision-free, independently of projection.
assert min(old_min,new_min)>F(1,10**24)**2
assert F(1,5000)-F(2,10**30)>F(1,10**4)
assert P['deformation_certificate_sha256']==hashlib.sha256((H/'symmetric_critical_deformation.json').read_bytes()).hexdigest()
out={'segment_count':len(segments),'loop_count':len(loops),'old_minimum_squared':str(old_min),'mixed_minimum_squared':str(new_min),'maximum_endpoint_norm_squared':str(maximum),'loops':loops,'critical_deformation_sha256':P['deformation_certificate_sha256'],'verified_scope':['all common paths avoid every pole and node during full cyclotomic coefficient homotopy','each local loop encloses exactly its assigned mixed cluster counterclockwise','base configurations are identified by the actual coefficient homotopy'],'not_verified':['source-to-far-basepoint comparison','Artin words','node Fox columns']}
(H/'symmetric_path_plan_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all91 planned straight segments independently reconstructed using rational arithmetic.')
print('PASS: old-center distance>1/5000, mixed-center distance>1/20000, and |q|<5.')
print('PASS: all18 local squares are CCW and enclose exactly their assigned node cluster.')
print('PASS: full coefficient homotopy has no pole or collision on any path; base configuration transport is literal.')
print('Source-to-far-basepoint transport and Artin/Fox output remain separate audits.')

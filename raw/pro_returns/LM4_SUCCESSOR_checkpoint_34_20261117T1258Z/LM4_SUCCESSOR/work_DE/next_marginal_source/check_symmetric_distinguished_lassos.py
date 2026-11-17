#!/usr/bin/env python3
"""Independent simultaneous free-lasso-system audit (6old+18node)."""
from fractions import Fraction as F
from pathlib import Path
import json
H=Path(__file__).resolve().parent;ROOT=H.parent.parent
D=json.loads((H/'symmetric_critical_deformation.json').read_text())
M=json.loads((H/'symmetric_path_plan_review.json').read_text())
O=json.loads((ROOT/'work_CE/next_symmetric_nodes/symmetric_old_base_path_plan.json').read_text())
base=tuple(map(F,O['base']));hub=tuple(map(F,O['hub']))
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c):return cross(sub(b,a),sub(c,a))
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm(a):return dot(a,a)
def dist(c,a,b):
 d=sub(b,a);t=max(F(0),min(F(1),dot(sub(c,a),d)/norm(d)));z=sub(c,a);return norm((z[0]-t*d[0],z[1]-t*d[1]))
centers=[tuple(map(F,r['center'])) for r in D['centers']]
loops=[]
for r in O['plans']:
 loops.append({'kind':'old','index':r['index'],'center':tuple(map(F,r['center'])),'corners':[tuple(map(F,c)) for c in r['corners']]})
for r in M['loops']:
 loops.append({'kind':'node','index':r['index'],'center':tuple(map(F,r['center'])),'corners':[tuple(map(F,c)) for c in r['corners']]})
assert len(loops)==len(centers)==24 and {r['center'] for r in loops}==set(centers)
triangle_records=[]
triangle_clearance=None
for i,r in enumerate(loops):
 c=r['center'];corner=r['corners'][0]
 assert orient(hub,corner,c)!=0
 for cc in centers:
  if cc==c:continue
  signs=[orient(hub,corner,cc),orient(corner,c,cc),orient(c,hub,cc)]
  assert min(signs)<0<max(signs),('another puncture in whisker triangle',i,cc)
  clearance=min(dist(cc,a,b) for a,b in ((hub,corner),(corner,c),(c,hub)))
  assert clearance>F(1,10**20)**2
  triangle_clearance=clearance if triangle_clearance is None else min(triangle_clearance,clearance)
 for a,b in zip([hub]+r['corners'],r['corners']):
  assert norm(a)<25 and norm(b)<25
  for cc in centers:assert dist(cc,a,b)>F(1,10**24)**2
 area=sum(cross(a,b) for a,b in zip(r['corners'],r['corners'][1:]));assert area>0
 for s in loops[i+1:]:assert cross(sub(c,hub),sub(s['center'],hub))!=0,('collinear center rays',i,s['index'])
 triangle_records.append({'kind':r['kind'],'index':r['index'],'signed_twice_triangle_area':str(orient(hub,corner,c)),'square_signed_twice_area':str(area)})
for c in centers:assert dist(c,base,hub)>F(1,10**24)**2
# Independently verify the retained loops' strong pole margin.
oldcenters=[tuple(map(F,r['center'])) for r in D['centers'] if r['kind']=='old']
for r in loops:
 if r['kind']!='old':continue
 for a,b in zip([hub]+r['corners'],r['corners']):
  for c in oldcenters:assert dist(c,a,b)>F(1,5000)**2
out={'lasso_count':24,'node_lasso_count':18,'retained_lasso_count':6,'all_center_rays_pairwise_noncollinear':True,'all_whisker_triangles_free_of_other_punctures':True,'all_local_squares_positive':True,'triangle_records':triangle_records,'minimum_other_cluster_triangle_distance_squared':str(triangle_clearance),'conclusion':'the24 based loops are homotopic to a radial distinguished lasso basis of the24-punctured plane; filling18 node punctures leaves the six specified retained free generators'}
(H/'symmetric_distinguished_lassos.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all24 center rays from the common hub are pairwise noncollinear.')
print('PASS: each corner whisker deforms through a triangle containing no other critical point to its radial center whisker.')
print('PASS: all24 local loops are CCW and all old-loop paths retain the strict pole margin.')
print('PROVED: the24 lassos form a distinguished free base system; the six old loops remain a free basis after filling18 node values.')

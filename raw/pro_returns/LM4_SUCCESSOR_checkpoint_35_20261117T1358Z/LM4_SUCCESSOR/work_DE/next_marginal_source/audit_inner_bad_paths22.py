#!/usr/bin/env python3
"""Independent Fraction audit of the actual ten radial lasso polygons."""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_plan22.json'
d=json.loads(p.read_text());base=tuple(map(F,d['base']));h=F(d['square_halfside'])
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def norm(a):return a[0]**2+a[1]**2
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dist2(c,a,b):
 v=sub(b,a);w=sub(c,a);t=sum(x*y for x,y in zip(v,w))/norm(v)
 t=max(F(0),min(F(1),t));return norm((w[0]-t*v[0],w[1]-t*v[1]))
rows=[]
for rr in d['centers']:
 c=tuple(map(F,rr['center']));cs=[(c[0]+h,c[1]+h),(c[0]-h,c[1]+h),(c[0]-h,c[1]-h),(c[0]+h,c[1]-h)]
 j=min(range(4),key=lambda j:norm(sub(cs[j],base)));cs=[cs[(j+k)%4] for k in range(5)]
 assert sum(cross(a,b) for a,b in zip(cs,cs[1:]))>0
 rows.append((rr['name'],c,cs))
margin=None;triangle_margin=None
for name,c,cs in rows:
 pts=[base]+cs
 assert all(norm(z)<F(9,10) for z in pts)
 for a,b in zip(pts,pts[1:]):
  for _,cc,_ in rows:
   x=dist2(cc,a,b);margin=x if margin is None else min(margin,x)
   assert x>F(1,30000)**2
 for other,cc,css in rows:
  if other==name:continue
  tri=[base,c,cs[0]]
  signs=[cross(sub(b,a),sub(cc,a)) for a,b in zip(tri,tri[1:]+tri[:1])]
  assert not(all(x>=0 for x in signs) or all(x<=0 for x in signs))
  dd=min(dist2(cc,a,b) for a,b in zip(tri,tri[1:]+tri[:1]))
  triangle_margin=dd if triangle_margin is None else min(triangle_margin,dd)
  assert dd>F(1,400000)**2
  assert max(abs(c[0]-cc[0]),abs(c[1]-cc[1]))>2*h
for (_,c,_),(_,cc,_) in itertools.combinations(rows,2):assert cross(sub(c,base),sub(cc,base))!=0
# Uniform true-root disk/far-section bound, using |q|<19/20, |beta|<3/5.
r=F(19,20);bb=F(3,5);hmax=(r+bb)/(1+r*bb);assert hmax==F(155,157)
rho=F(49,50);assert hmax*hmax<rho and r<rho and F(9,10)<r*r
assert F(3,5)**2>F(1,3)
out={'status':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'lassos':len(rows),'segments':5*len(rows),
 'minimum_rounded_center_distance_squared':str(margin),
 'minimum_other_center_to_whisker_triangle_boundary_squared':str(triangle_margin),
 'true_critical_center_error_bound':'1/400000 (rounding <2e-6 plus audited cyclotomic deformation <1e-27)',
 'all_corner_to_center_whisker_homotopies_avoid_actual_other_centers':True,
 'all_squares_disjoint':True,'all_radial_center_rays_distinct':True,
 'q_modulus_bound':str(r),'beta_modulus_bound':str(bb),'h_modulus_bound':str(hmax),
 'all_six_fiber_punctures_modulus_strictly_less_than':str(rho),
 'scope':'Actual path topology/empty far collar; no reuse or reconstruction of crossing polynomials.'}
Path(__file__).with_name('inner_bad_paths_independent22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS ten lassos/fifty segments, disjoint squares, distinguished common-base homotopies')
print('path squared margin',margin,'triangle squared margin',triangle_margin)
print('PASS true disk/far collar bound',hmax*hmax,'<',rho)

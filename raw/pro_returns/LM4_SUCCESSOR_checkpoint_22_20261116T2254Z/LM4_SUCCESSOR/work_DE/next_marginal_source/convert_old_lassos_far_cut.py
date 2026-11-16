#!/usr/bin/env python3
"""Exact static six-puncture old-lasso to far downward-cut comparison."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,time
from weighted_stallings import WeightedFold,reduce_word as red,inverse as inv,substitute as sub
H=Path(__file__).resolve().parent
ROOT=H.parents[1]
p=ROOT/'work_CE/next_symmetric_nodes/symmetric_old_base_braids.json'
d=json.loads(p.read_text());rot=(Q(1),Q(371,1000));zero=(Q(0),Q(0))
def pt(a):return tuple(map(Q,a))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def diff(a,b):return add(a,neg(b))
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def enc(a):return list(map(str,a))
def norm(a):return a[0]**2+a[1]**2
centers=[pt(x['center']) for x in d['loops']]
points=[cm(rot,x) for x in centers];order=sorted(range(6),key=lambda i:points[i][0]);cuts=[points[i] for i in order]
assert order==[3,4,2,0,5,1],order
assert len(set(x[0] for x in cuts))==6
records=[];minimum=None
def segment(a,b):
 global minimum
 dx=b[0]-a[0];dy=b[1]-a[1];events=[]
 for j,c in enumerate(cuts,1):
  # Exact point-to-closed-segment separation, also records deformation margin.
  v=diff(b,a);w=diff(c,a);t=(w[0]*v[0]+w[1]*v[1])/norm(v) if norm(v) else Q(0);t=max(Q(0),min(Q(1),t))
  e=(a[0]+t*v[0]-c[0],a[1]+t*v[1]-c[1]);n=norm(e);assert n>0
  minimum=n if minimum is None else min(minimum,n)
  for z in (a,b):
   if z[0]==c[0]:assert z[1]>c[1],('endpoint cut',j,z,c)
  if not dx:
   if a[0]==c[0]:assert min(a[1],b[1])>c[1]
   continue
  t=(c[0]-a[0])/dx
  if 0<t<1:
   h=a[1]+t*dy-c[1];assert h
   if h<0:events.append((t,j if dx>0 else -j))
 events.sort();assert len(set(t for t,j in events))==len(events)
 records.append({'start':enc(a),'end':enc(b),'events':[[str(t),j] for t,j in events]})
 return [j for t,j in events]
def read(path):return red(j for a,b in zip(path,path[1:]) for j in segment(a,b))
base=cm(rot,pt(d['common_trunk']['start']));hub=cm(rot,pt(d['common_trunk']['end']))
far=(Q(10),Q(0));eta=[far,(Q(10),Q(2)),(base[0],Q(2)),base]
assert read(eta)==()
forward={};paths=[]
for i,row in enumerate(d['loops'],1):
 segs=row['forward_segments'];assert pt(segs[0]['start'])==pt(d['common_trunk']['end'])
 for x,y in zip(segs,segs[1:]):assert x['end']==y['start']
 pp=[base,hub]+[cm(rot,pt(s['end'])) for s in segs]+[hub,base]
 w=read(pp);assert w
 # The actual square is positive and contributes its one physical meridian.
 sq=[cm(rot,pt(segs[0]['end']))]+[cm(rot,pt(s['end'])) for s in segs[1:]]
 assert sq[0]==sq[-1]
 signed_area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(sq,sq[1:]));assert signed_area>0
 ab=[w.count(j)-w.count(-j) for j in range(1,7)];assert ab==[int(order[j]==i-1) for j in range(6)]
 forward[i]=w;paths.append([enc(x) for x in pp]);print('old',i,'-> far cuts',list(w),flush=True)
fold=WeightedFold(list(forward.values()));back={j:fold.rewrite((j,)) for j in range(1,7)}
assert all(v is not None for v in back.values())
for j in range(1,7):
 assert sub(forward[j],back)==(j,)
 assert sub(back[j],forward)==(j,)
print('PASS all12 Nielsen inverse substitutions; far physical order',order,flush=True)
comm=(5,6,-5,-6);oldcomm=sub(comm,back);assert sub(oldcomm,forward)==comm
print('far [x5,x6] -> actual old lassos',list(oldcomm),flush=True)
# Existing geometric root certificate bounds every true zeta error by10^-30.
# Squaring the rational zeta² changes its ζ4 target by less than10^-28.
square=cm(centers[3],centers[3]);square_error=norm(diff(square,centers[5]));assert square_error<Q(1,10**56)
assert minimum>Q(1,10**8)
# Both point sets, all old polygons, and the common whisker deform without collision.
# Cut x orders retain a gap vastly larger than their perturbation.
gap=min(b[0]-a[0] for a,b in zip(cuts,cuts[1:]));assert gap>Q(1,100)
out={'scope':'actual based static lasso conversion,not the moving-v path certificate','old_names':[r['name'] for r in d['loops']], 'rot':enc(rot),'far_basepoint_projected':enc(far),'eta_far_to_old_projected':[enc(x) for x in eta],'eta_cut_word':[], 'far_cut_physical_old_indices':order,'forward_old_to_far':{str(k):list(v) for k,v in forward.items()},'inverse_far_to_old':{str(k):list(v) for k,v in back.items()},'far_commutator':[5,6,-5,-6],'old_commutator':list(oldcomm),'paths_projected':paths,'segments':records,'minimum_path_center_distance_squared':str(minimum),'minimum_cut_x_gap':str(gap),'square_zeta2_to_zeta4_distance_squared':str(square_error),'coefficient_deformation_bound':'10^-28','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(H/'old_lassos_far_cut_conversion.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact cut crossings,positive orientation,based whisker and coefficient deformation margin.',flush=True)

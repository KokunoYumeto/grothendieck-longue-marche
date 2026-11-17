#!/usr/bin/env python3
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
H=Path(__file__).resolve().parent;R=H.parents[1]
p=R/'work_CE/next_symmetric_nodes/symmetric_old_base_braids.json';d=json.loads(p.read_text())
U={r['name']:tuple(map(Q,r['center'])) for r in d['loops']}
rot=(Q(1),Q(371,1000))
def cm(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sc(t,a):return t*a[0],t*a[1]
def enc(z):return list(map(str,z))
zero=(Q(0),Q(0));one=(Q(1),Q(0))
path=[U['zeta^2'],(-Q(4,5),Q(1,5)),(-Q(999,1000),Q(1,1000))]
order=[4,3,2,0,5,1];rows=[]
for k,(a,b) in enumerate(zip(path,path[1:])):
 v=add(b,sc(-1,a));const=[zero,one,U['zeta'],U['zeta^3']]
 poly=[(c,zero,zero) for c in const]+[(a,v,zero),(cm(a,a),sc(2,cm(a,v)),cm(v,v))]
 projection=[tuple(cm(rot,x)[0] for x in coeff) for coeff in poly]
 for left,right in zip(order,order[1:]):
  c,l,q=tuple(projection[right][j]-projection[left][j] for j in range(3))
  vals=[(Q(0),c),(Q(1),c+l+q)]
  if q:
   t=-l/(2*q)
   if 0<t<1:vals.append((t,c+l*t+q*t*t))
  t,m=min(vals,key=lambda x:x[1]);assert m>Q(1,10000),(k,left,right,m)
  rows.append({'segment':k,'left':left,'right':right,'polynomial':list(map(str,(c,l,q))),'minimizer':str(t),'minimum':str(m)})
  print('PASS segment',k,'adjacent',left,right,'gap>',float(m),flush=True)
# Exact local endpoint node: q=v² and1 are the last adjacent pair.
assert order[-2:]==[5,1]
# The real path between endpoint and v=-1 has no other collision; this endpoint
# lies in a small disk around -1 disjoint from all other v critical values.
e=path[-1];assert (e[0]+1)**2+e[1]**2<Q(1,100000)
# True cyclotomic perturbation <10^-30, squaring displacement <10^-28,
# versus all projection gaps>10^-4, gives an explicit stable order.
out={'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'v_path':[enc(v) for v in path],'q_punctures':['0','1','zeta','zeta^3','v','v^2'],'physical_order':order,'gaps':rows,'uniform_lower_bound':'1/10000','coefficient_deformation_bound':'10^-28','braid_word':[],'scope':'independent exact adjacent projection-gap audit of the two segments;local node geometry remains separate'}
(H/'constant_v_broken_path_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS both segments have literal empty braid;last adjacent pair(v²,1).')

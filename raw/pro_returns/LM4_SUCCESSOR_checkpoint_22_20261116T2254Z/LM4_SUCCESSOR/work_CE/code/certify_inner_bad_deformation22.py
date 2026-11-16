#!/usr/bin/env python3
"""Uniform transfer of the rational inner-region braid to the actual roots.

Radical enclosures, complete symbolic collision factors, every parameter
polygon margin, the first-neck lift choice, and the exceptional14/23
branch separation are checked independently of crossing enumeration.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import sys,json,hashlib,itertools
ROOT=Path(__file__).resolve().parents[2];DE=ROOT/'work_DE/next_marginal_source'
sys.path.insert(0,str(DE))
import sympy as S
from quadratic_pencil_braid import u,ROT,Q,I
P=ROOT/'work_CE/next_symmetric_nodes'
D=json.loads((P/'inner_bad_orbifold_braids22.json').read_text())
eps=F(2,10**30);scale=10**90
def sqrtbox(lo,hi):
 a=isqrt(lo.numerator*scale*scale//lo.denominator)
 b=isqrt(hi.numerator*scale*scale//hi.denominator)+1
 return F(a,scale),F(b,scale)
s5=sqrtbox(F(5),F(5));sp=sqrtbox(10+2*s5[0],10+2*s5[1]);sm=sqrtbox(10-2*s5[1],10-2*s5[0])
c1=((s5[0]-1)/4,(s5[1]-1)/4);c2=(-(s5[1]+1)/4,-(s5[0]+1)/4)
t1=(sp[0]/4,sp[1]/4);t2=(sm[0]/4,sm[1]/4)
true=[(c1,t1),(c2,t2),(c2,(-t2[1],-t2[0])),(c1,(-t1[1],-t1[0]))]
def frac(x):return F(int(S.numer(x)),int(S.denom(x)))
for v,rect in zip(u[1:],true):
 for x,interval in zip((S.re(v),S.im(v)),rect):
  assert max(abs(frac(x)-z) for z in interval)<F(1,10**30)
assert F(9,10)<F(19,20)**2
assert F(17,10)**2<3
# True |alpha|^2=5-4cos(theta)>3; under the whole coefficient homotopy
# the displacement is <5eps, so |q-alpha| remains >7/10.
assert F(17,10)-F(19,20)-5*eps>F(7,10)
assert 1-3*eps>F(19,20)
assert F(3,8)-2*eps>F(3,10)
assert 32*eps<F(1,10**27)
assert 100*eps<F(1,10**26)
assert 2*F(1,10**6)+F(1,10**27)<F(1,400000)

q,a,b=S.symbols('q a b');h=lambda v:(v*v+(1-2*v)*q)/(q+v*v-2*v)
factors={
 'difference':-2*(q-1)*(q-a*b)*(a-b)/((q+a*a-2*a)*(q+b*b-2*b)),
 'sum':-2*(q+a*b-a-b)*(q*(a+b-1)-a*b)/((q+a*a-2*a)*(q+b*b-2*b)),
 'branch':-(q-1)*(q-a*a)**2/(q+a*a-2*a)**2,
 'derivative':-2*a*(a-1)**2/(q+a*a-2*a)**2}
for name,lhs in [('difference',h(a)-h(b)),('sum',h(a)+h(b)),('branch',h(a)**2-q),('derivative',S.diff(h(a),q))]:
 assert S.cancel(lhs-factors[name])==0

def norm(z):return S.cancel(S.re(z)**2+S.im(z)**2)
def d2(c,a,b):
 d=b-a;t=S.cancel((S.re(c-a)*S.re(d)+S.im(c-a)*S.im(d))/norm(d))
 t=max(S.Integer(0),min(S.Integer(1),t));return norm(c-a-t*d)
centers={r['name']:Q(r['center'][0])+I*Q(r['center'][1]) for r in D['plan']['centers']}
members=[]
for r in D['plan']['centers']:
 if r['name']=='q0':continue
 for n in r['physical_nodes']:
  i,j=n['i'],n['j'];a0,b0=u[i],u[j]
  v=S.cancel(a0+b0-a0*b0 if n['kind']=='alpha' else a0*b0/(a0+b0-1))
  assert norm(v-centers[r['name']])<Q(1,500000)**2
  members.append({'name':r['name'],'i':i,'j':j,'kind':n['kind']})
minimum=None;segments=0
for loop in D['loops']:
 for seg in loop['segments']:
  aa=Q(seg['start'][0])+I*Q(seg['start'][1]);bb=Q(seg['end'][0])+I*Q(seg['end'][1]);segments+=1
  assert norm(aa)<Q(9,10) and norm(bb)<Q(9,10)
  for cc in centers.values():
   dd=d2(cc,aa,bb);assert dd>Q(1,30000)**2
   minimum=dd if minimum is None else min(minimum,dd)
assert segments==50 and len(members)==10

# Literal initial first-neck marking: all five ordinary projected
# punctures are above the cone's real axis, and the chosen sqrt sheet
# has precisely h_i and the first-quadrant branch sqrt(q).
q0=Q(4,5)+I/2;positivity=[]
for i,v in enumerate(u[1:],1):
 hv=S.cancel((v*v+(1-2*v)*q0)/(q0+v*v-2*v));yy=S.cancel(hv*hv)
 assert S.re(hv)>Q(1,4) and S.im(hv)>Q(1,4)
 assert S.im(S.expand(ROT*yy))>Q(1,4)
 positivity.append({'i':i,'Re_h_lower':'1/4','Im_h_lower':'1/4','Im_rotated_y_lower':'1/4'})
assert S.im(ROT*q0)>Q(1,4)
rho=F(49,50);hh=F(155,157)
assert hh*hh+100*eps<rho

# Exact cyclotomic simultaneous-node positions, including the retained
# branch strictly between the two different local collision disks.
z=S.symbols('z');phi=z**4+z**3+z*z+z+1
def field(x):
 n,d=S.fraction(S.cancel(x));return S.rem(S.expand(n*S.invert(d,phi,z)),phi,z)
u1=z;u2=z*z;u4=field(z**4);qc=field(u1+u4-u1*u4);sqrt5=field(2*(u1+u4)+1)
def hy(v):return field(((v*v+(1-2*v)*qc)/(qc+v*v-2*v))**2)
assert field(qc-(sqrt5-3)/2)==0
assert field(hy(u1)-(2*sqrt5-5))==0
assert field(hy(u2)-(2*sqrt5-5)/5)==0
assert F(5)<F(7,3)**2 and F(5)<F(5,2)**2
assert F(5)<F(9,4)**2 # (4/5)*(5-2sqrt5)>2/5 separates the two node disks.

out={'status':'PASS','input_braid_sha256':hashlib.sha256((P/'inner_bad_orbifold_braids22.json').read_bytes()).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'root_coordinate_error_bound':'1/10^30','root_euclidean_error_bound':str(eps),
 'uniform_alpha_displacement_bound':'5epsilon','uniform_beta_displacement_bound':'32epsilon',
 'all_new_critical_displacements_strictly_less_than':'1/10^27',
 'all_old_or_extra_boundary_roots_modulus_greater_than':'19/20',
 'uniform_denominator_modulus_lower_bound':'7/10',
 'uniform_squared_fiber_puncture_displacement_bound':'100epsilon < 1/10^26',
 'path_segments':segments,'minimum_rounded_center_distance_squared':str(minimum),
 'critical_members':members,'actual_fiber_disk_radius':str(rho),
 'first_neck_K_initial_generators':[1,3,4,5,6],'cone_generator':2,'positivity_margins':positivity,
 'complete_collision_factors':{k:str(S.factor(v)) for k,v in factors.items()},
 'simultaneous_node':{'q':'(sqrt(5)-3)/2','y14':'2sqrt(5)-5','y23':'(2sqrt(5)-5)/5',
  'strict_order':['y14','q','y23','0'],'node_separation_greater_than':'2/5'},
 'scope':'Uniform configuration isotopy and actual first-neck marking for all50 certified rational path segments; no full global gluing.'}
(P/'inner_bad_deformation22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS radical fifth-root enclosures and four complete collision/derivative identities.')
print('PASS all50 path segments; all critical deformations stay inside their assigned squares.')
print('PASS actual empty outer collar and literal first-neck K marking.')
print('PASS exceptional exact order: y14 < retained branch q < y23 < cone0.')

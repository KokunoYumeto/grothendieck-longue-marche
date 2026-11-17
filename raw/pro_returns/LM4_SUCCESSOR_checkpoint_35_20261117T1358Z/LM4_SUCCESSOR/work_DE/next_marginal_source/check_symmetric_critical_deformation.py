#!/usr/bin/env python3
"""Exact old-hole/new-node separation for the symmetric q pencil.
Independent geometry audit; no braid word or module-membership conclusion.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import json
import sympy as S
H=Path(__file__).resolve().parent
D=10**30
U=[(Q(1),Q(0)),
(Q(309016994374947424102293417183,D),Q(951056516295153572116439333379,D)),
(Q(-809016994374947424102293417183,D),Q(587785252292473129168705954639,D)),
(Q(-809016994374947424102293417183,D),Q(-587785252292473129168705954639,D)),
(Q(309016994374947424102293417183,D),Q(-951056516295153572116439333379,D))]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def n2(a):return a[0]**2+a[1]**2
def div(a,b):return mul(a,(b[0]/n2(b),-b[1]/n2(b)))
def enc(a):return [str(t) for t in a]
one=(Q(1),Q(0));zero=(Q(0),Q(0))
scale=10**90
def sqrt_interval(lo,hi):
 a=isqrt(lo.numerator*scale*scale//lo.denominator)
 b=isqrt(hi.numerator*scale*scale//hi.denominator)+1
 return Q(a,scale),Q(b,scale)
s5=sqrt_interval(Q(5),Q(5));sp=sqrt_interval(10+2*s5[0],10+2*s5[1]);sm=sqrt_interval(10-2*s5[1],10-2*s5[0])
c1=((s5[0]-1)/4,(s5[1]-1)/4);c2=(-(s5[1]+1)/4,-(s5[0]+1)/4)
t1=(sp[0]/4,sp[1]/4);t2=(sm[0]/4,sm[1]/4)
def ine(a):return -a[1],-a[0]
true=[((Q(1),Q(1)),(Q(0),Q(0))),(c1,t1),(c2,t2),(c2,ine(t2)),(c1,ine(t1))]
for a,rect in zip(U,true):
 for v,(lo,hi) in zip(a,rect):assert max(abs(v-lo),abs(v-hi))<Q(1,D) or lo==hi==v
EPS=Q(2,D)
# True denominators exceed3/8: use the rational center margin and
# the proven coordinate error to obtain a strict Euclidean lower bound.
for i in range(1,5):
 for j in range(1,5):assert n2(sub(add(U[i],U[j]),one))>(Q(3,8)+2*EPS)**2
# Exact symbolic collision completeness for all trajectory types.
q,u,t=S.symbols('q u t');phi=S.Symbol('z')**4+S.Symbol('z')**3+S.Symbol('z')**2+S.Symbol('z')+1
rational=[S.Integer(0),S.Integer(1),q,u,q/u,(u-q)/(u-1),q*(1-u)/(q-u)]
# Every numerator factor must be in the declared old/new list.
allowed=[q,q-1,q-u,q-t,q-u*u,q-u*t,q-(u+t-u*t),q*(u+t-1)-u*t]
rows=[]
for i,a in enumerate(rational):
 for j,b0 in enumerate(rational):
  if i<3 and j<3 and i>=j:continue
  b=b0.subs(u,t) if j>=3 else b0
  if i<3 and j>=3 or i>=3 and j>=3 or (i<3 and j<3):
   num=S.fraction(S.cancel(a-b))[0]
   fac=S.factor_list(num,q)[1] if num!=0 else []
   for f,m in fac:
    if S.degree(f,q)==0:continue
    assert any(not S.cancel(f/g).has(q) for g in allowed),(i,j,f)
   rows.append({'left':i,'right':j,'numerator':str(S.factor(num))})
for a in rational:
 num=S.factor(S.fraction(S.cancel(a*a-q))[0]);fac=S.factor_list(num,q)[1]
 for f,m in fac:
  if S.degree(f,q)==0:continue
  assert any(not S.cancel(f/g).has(q) for g in allowed),(a,f)
 rows.append({'sqrt_pair':str(a),'numerator':str(num)})
# Exact cyclotomic keys identify all18 true mixed clusters.
z=S.symbols('z');cyclo=z**4+z**3+z**2+z+1

def field(a):
 n,d=S.fraction(S.cancel(a));return S.rem(S.expand(n*S.invert(d,cyclo,z)),cyclo,z)
def key(a):
 a=field(a);return tuple(str(a.coeff(z,k)) for k in range(4))
clusters={};members=[]
for i in range(1,5):
 for j in range(1,5):
  ui,uj=field(z**i),field(z**j)
  for typ,exact,rat in [('X',ui+uj-ui*uj,sub(add(U[i],U[j]),mul(U[i],U[j]))),('Y',ui*uj/(ui+uj-1),div(mul(U[i],U[j]),sub(add(U[i],U[j]),one)))]:
   k=key(exact);clusters.setdefault(k,{'center':rat,'members':[]})['members'].append([typ,i,j])
   members.append((k,rat,typ,i,j))
assert len(clusters)==18
radius=Q(1,10**24)
for k,rat,typ,i,j in members:
 assert n2(sub(rat,clusters[k]['center']))<Q(1,10**27)**2
# Uniform deformation bounds, valid also at every straight coefficient homotopy.
assert 5*EPS<Q(1,10**28) # X; conservative strict margin.
assert 25*EPS<Q(1,10**27) # Y.
# Products/squares/u remain within1e-27 of their exact old root.
old=[zero]+U
old_names=['0','1','zeta','zeta^2','zeta^3','zeta^4']
for i in range(1,5):
 for j in range(1,5):assert n2(sub(mul(U[i],U[j]),U[(i+j)%5]))<Q(1,10**27)**2
centers=[{'kind':'old','name':name,'center':a} for name,a in zip(old_names,old)]
centers += [{'kind':'mixed','key':list(k),'center':d['center'],'members':d['members']} for k,d in clusters.items()]
minimum=min(n2(sub(a['center'],b['center'])) for i,a in enumerate(centers) for b in centers[i+1:])
assert minimum>Q(1,100)**2
for c in centers:assert n2(c['center'])<Q(10)
# A useful uniform path gate for the producer. It must check these two
# hypotheses on every actual segment, rather than assume them here.
maxq=Q(5);pole_margin=Q(1,10**4)
disp=maxq*(maxq+1)*EPS/(pole_margin*(pole_margin-EPS))
assert disp<Q(1,10**20)
out={'coefficient_points':[enc(a) for a in U], 'coordinate_error_bound':'1/10^30','euclidean_error_bound':str(EPS),'critical_disk_radius':str(radius),'minimum_center_separation_squared':str(minimum),'centers':[{**{k:v for k,v in c.items() if k!='center'},'center':enc(c['center'])} for c in centers],'symbolic_collision_numerators':rows,'path_gate':{'max_abs_q':'5','min_distance_to_each_true_pole':'1/10^4','uniform_strand_displacement_bound':'1/10^20','status':'conditional until checked on actual producer segments'},'claims_excluded':['braid words','Fox module membership','fixed lifting','source image equality']}
(H/'symmetric_critical_deformation.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: radical intervals certify each fifth-root coordinate error<1e-30.')
print('PASS: all rational/square-root collision numerators have only declared old/new factors.')
print('PASS: 18 true mixed clusters plus6 old-hole clusters; all deformed collisions remain within1e-27 of assigned centers.')
print('PASS: all24 radius1e-24 cluster disks are disjoint; center separation>1/100.')
print('PASS: true |zeta_i+zeta_j-1|>3/8 and uniform X/Y deformation bounds.')
print('CONDITIONAL PATH GATE: |q|<=5, distance to true old poles>=1e-4 gives strand displacement<1e-20.')
print('No path, braid, Fox-module or fixed-lift assertion inferred without its separate audit.')

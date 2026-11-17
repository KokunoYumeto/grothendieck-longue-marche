#!/usr/bin/env python3
"""Independent exact quotient, collision, Blaschke, and half-plane checks."""
from pathlib import Path
import json,time,hashlib
import sympy as S

started=time.monotonic()
q,qbar,u,r,s,t,v,w,Q,Z=S.symbols('q qbar u r s t v w Q Z')
records=[]
def check(name,expression):
    result=S.cancel(expression)
    assert result==0,(name,S.factor(result))
    records.append(name)
def T(a):return (q+a*a-2*a)/(a*a+(1-2*a)*q)
def d(a):return a*a+(1-2*a)*q
alpha=u*(2-u); beta=u*u/(2*u-1)
f=lambda x:(x-q)/(x-1)
g=lambda x:q/x
check('fiber_F_squared',f(f(v))-v)
check('fiber_swap_squared',g(g(v))-v)
check('fiber_F_swap_commutes',f(g(v))-g(f(v)))
sf=(4*q-(1+q)*s)/(q+1-s)
check('descended_s', (f(v)+f(q/v))-sf.subs(s,v+q/v))
ts=(s-2)/(s-2*q); st=2*(q*t-1)/(t-1)
check('coordinate_inverse_s',st.subs(t,ts)-s)
check('coordinate_inverse_t',ts.subs(s,st)-t)
check('descended_sign',ts.subs(s,sf)+ts)
check('discriminant',st**2-4*q-4*(q-1)*(q*t*t-1)/(t-1)**2)
check('A_graph',ts.subs(s,u+q/u)-T(u))
check('T_minus_one',d(u)*(T(u)-1)-2*u*(q-1))
check('T_plus_one',d(u)*(T(u)+1)-2*(1-u)*(q-u))
check('retained_branch',d(u)**2*(q*T(u)**2-1)-(q-1)*(q-u*u)**2)
check('same_sign',d(u)*d(r)*(T(u)-T(r))-2*(u-r)*(q-1)*(q-u*r))
check('opposite_sign',d(u)*d(r)*(T(u)+T(r))+2*(q+u*r-r-u)*(q*(r+u-1)-u*r))
check('zero_alpha',T(u).subs(q,alpha))
check('pole_beta',d(u).subs(q,beta))
alphabar=(1/u)*(2-1/u)
check('reciprocal_zero_pole',beta*alphabar-1)
check('zero_modulus',alpha*alphabar-1-(4-2*(u+1/u)))
dbar=1/u**2+(1-2/u)*qbar
check('Blaschke_norm_identity',(q-alpha)*(qbar-alphabar)-d(u)*dbar-(alpha*alphabar-1)*(1-q*qbar))
conjT=T(1/u).subs(q,qbar)
check('reciprocal_conjugate',T(u).subs(q,1/qbar)*conjT-1)
h=1/T(u)
lam=1-(u+1/u)/2; nu=(1/u-u)/2
check('halfplane_affine',(1+h)/(1-h)-lam*(1+q)/(1-q)-nu)
check('halfplane_opposite',(1-h)/(1+h)-1/((1+h)/(1-h)))
z=(Z-1)/(Z+1)
check('retained_Joukowski',(1+z*z)/(1-z*z)-(Z*Z+1)/(2*Z))
pv=S.Rational(399,200);pw=S.Rational(1,200);pq=pv*pw
assert pq==S.Rational(399,40000)
assert ts.subs({q:pq,s:pv+pw})==0
assert f(v).subs({q:pq,v:pv})==pv
assert f(v).subs({q:pq,v:pw})==pw
records.append('literal_based_point_and_fixed_source')

# Reflection-chart covering formula is checked from the original v,w.
aa=(2*v*w-v-w)/(w-v);bb=(v+w-2)/(w-v)
tv=ts.subs({q:v*w,s:v+w})
check('reflection_t',tv+bb/aa)
check('reflection_double_cover',aa**2-(v*w-1)/(v*w*tv**2-1))

out={'result':'PASS','identities':records,'count':len(records),
 'conjugation_convention':'bar(u)=u^-1; qbar is an independent formal conjugate variable',
 'positive_factor':'|alpha_u|^2-1=4(1-cos(theta))>0 for u=e^(i theta)!=1',
 'inner_collar':'m=max(sqrt(|q|),max_u |1/T_u(q)|)<1; delta=(1-m)/4; every moving |t|>=1/m>1+delta',
 'scope':'Exact algebra and separation; geometric and profinite proofs separately reviewed. No global fixed-source equality.',
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-started}
(Path(__file__).resolve().parent/'swap_blaschke_independent_review21.json').write_text(json.dumps(out,indent=2)+'\n')
for name in records:print('PASS',name)
print('DONE',len(records),'identities; elapsed',out['elapsed_seconds'])

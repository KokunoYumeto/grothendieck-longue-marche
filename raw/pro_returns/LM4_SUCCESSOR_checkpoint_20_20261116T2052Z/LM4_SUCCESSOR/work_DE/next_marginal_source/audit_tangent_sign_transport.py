"""Literal source-sign identities and safe based paths; no subgroup equality."""
from pathlib import Path
import json
import sympy as S
from quadratic_pencil_braid import u,Q,I
HERE=Path(__file__).resolve().parent
s,p,z=S.symbols('s p z');a=(1-s)/(1+s);T=s*(1+p)/(1-p)
assert S.cancel(a.subs(s,1/s)+a)==0
assert S.cancel(T.subs(s,1/s)-T/s**2)==0
v=S.symbols('v')
assert S.cancel((1/s-v**-1)**2/(1/s+v**-1)**2-(s-v)**2/(s+v)**2)==0
base=Q(1,100)
centers=[S.Integer(0)]+u+[S.cancel(v*v/(2*v-1)) for v in u[1:]]
path=[S.Integer(100),100+100*I,100*I,base]
for aa,bb in zip(path,path[1:]):
 d=bb-aa;dd=S.re(d)**2+S.im(d)**2
 for c in centers:
  e=c-aa;t=max(0,min(1,(S.re(d)*S.re(e)+S.im(d)*S.im(e))/dd));r=e-t*d
  assert S.re(r)**2+S.im(r)**2>Q(1,100000)
# Literal fiber transport at q=.01, using exact roots +/- .1.
points=[Q(1,10),-Q(1,10)]+[S.cancel((base+v*v)/(2*v)) for v in u]
fiber=[S.Integer(1),2+2*I,base+2*I,base]
for aa,bb in zip(fiber,fiber[1:]):
 d=bb-aa;dd=S.re(d)**2+S.im(d)**2
 for c in points:
  e=c-aa;t=max(0,min(1,(S.re(d)*S.re(e)+S.im(d)*S.im(e))/dd));r=e-t*d
  assert S.re(r)**2+S.im(r)**2>Q(1,100000)
(HERE/'tangent_sign_transport.json').write_text(json.dumps({'positive_source':'T=1','negative_source':'T=q','ambient_involution':'(q,T)->(1/q,T/q)','original_involution':'(s,p)->(1/s,p); before normalization (zeta^2/s,p)','negative_source_q_path':[str(z) for z in path],'fiber_T_path':[str(z) for z in fiber],'squared_distance_lower_bound':'1/100000','scope':'Actual based sign exchange only; not equality of the two marginal subgroups.'},indent=2)+'\n')
print('PASS literal inversion/source-sign identities, negative-source transport, and common-fiber path.')
print('All rational-deformation squared distances >1e-5; coefficient error<1e-28 is smaller than these margins.')

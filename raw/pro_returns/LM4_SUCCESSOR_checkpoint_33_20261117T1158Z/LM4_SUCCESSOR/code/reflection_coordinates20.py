"""Exact affine reflection chart for the actual B89 symmetric surface."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

root=Path(__file__).resolve().parents[1]
v,w,a,b,u,z=s.symbols('v w a b u z')
aa=(2*v*w-v-w)/(w-v)
bb=(v+w-2)/(w-v)
vv=(a+1)/(b+1)
ww=(a-1)/(b-1)
Fv=v*(w-1)/(1-v)
Fw=w*(v-1)/(1-w)
sub={v:vv,w:ww}
assert s.cancel(aa.subs(sub,simultaneous=True)-a)==0
assert s.cancel(bb.subs(sub,simultaneous=True)-b)==0
assert s.cancel(vv.subs({a:aa,b:bb},simultaneous=True)-v)==0
assert s.cancel(ww.subs({a:aa,b:bb},simultaneous=True)-w)==0
assert s.cancel(aa.subs({v:Fv,w:Fw},simultaneous=True)-aa)==0
assert s.cancel(bb.subs({v:Fv,w:Fw},simultaneous=True)+bb)==0
assert s.cancel((v*w).subs(sub,simultaneous=True)-(a*a-1)/(b*b-1))==0
P={v:s.Rational(399,200),w:s.Rational(1,200)}
assert aa.subs(P)==s.Rational(199,200) and bb.subs(P)==0
old={
 'v':v, 'w':w, 'v_minus_1':v-1,'w_minus_1':w-1,
 'v_minus_w':v-w,'q_minus_1':v*w-1,
 'q_minus_u':v*w-u,
 'A_v':v-u,'A_w':w-u,
 'B_v':v*w+(u-1)*v-u,'B_w':v*w+(u-1)*w-u}
transformed={name:s.factor(s.cancel(f.subs(sub,simultaneous=True))) for name,f in old.items()}
# The union of old retained factors is exactly six affine lines.
retained_lines=[a-1,a+1,b-1,b+1,a-b,a+b]
paired_lines=[a-u*b-(u-1),a+u*b-(u-1),a-u*b+(u-1),a+u*b+(u-1)]
q_conic=a*a-1-u*(b*b-1)
assert s.factor(paired_lines[0]*paired_lines[1])==(a-u+1)**2-u*u*b*b or s.expand(paired_lines[0]*paired_lines[1]-((a-u+1)**2-u*u*b*b))==0
for sign in [-1,1]:
 assert s.expand((a+sign*(u-1)-u*b)*(a+sign*(u-1)+u*b)-((a+sign*(u-1))**2-u*u*b*b))==0
quotient=[s.Integer(1),a*a,1+(a*a-1)/u,((a-u+1)/u)**2,((a+u-1)/u)**2]
source=[a,a-1,a+1,a*a-(1-u),a-(u-1),a+(u-1)]
out={
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'forward':{'a':str(aa),'b':str(bb)},
 'inverse':{'v':str(vv),'w':str(ww)},
 'involution':'(a,b) -> (a,-b)',
 'basepoint':['199/200','0'],
 'q':'(a**2-1)/(b**2-1)',
 'transformed_actual_factors':{k:str(val) for k,val in transformed.items()},
 'retained_affine_lines':[str(x) for x in retained_lines],
 'four_paired_lines_per_u':[str(x) for x in paired_lines],
 'conic_per_u':str(q_conic),
 'u_values':'mu_5 minus {1}; all four values used',
 'counts':{'affine_lines':22,'conics':4,'generic_b_punctures':28,
           'generic_quotient_z_punctures':14,'source_a_punctures':19},
 'quotient_z_puncture_schemas':[str(x) for x in quotient],
 'fixed_source_polynomial_factor_schemas':[str(x) for x in source],
 'inverse_and_F_checks':'PASS',
 'scope':'Exact coordinate/factor identities only. Distinctness, bundle and source statements require the accompanying proof; no fixed-subgroup conclusion.'}
(root/'records/reflection_coordinates20.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

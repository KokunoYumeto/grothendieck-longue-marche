"""Exact rational-function certificates for the arithmetic S3 envelope.

The three ordered S3 covers have a compositum whose constant field is Q(sqrt3).
The proof that there are no further constants is given in Proposition B.f4.
"""
import sympy as s
import json
from pathlib import Path

t,T=s.symbols('t T')
b=27*t**2*(t-1)**2/(4*(t*t-t+1)**3)
a=(t**3-3*t+1)/(t*(t-1))
w=a-s.Rational(3,2)
checks={
 'beta_invariant_under_1_minus_t':s.factor(b.subs(t,1-t)-b),
 'beta_invariant_under_1_over_t':s.factor(b.subs(t,1/t)-b),
 'a_invariant_under_order_three':s.factor(a.subs(t,1/(1-t))-a),
 'a_reflected':s.factor(a.subs(t,1-t)+a-3),
 'quadratic_identity':s.factor(w*w-s.Rational(27,4)*(1-b)/b),
 'product_square_classes':s.factor((3*T*(1-T))*(3*(T-1))*(-3*T)-27*T*T*(T-1)**2)
}
assert all(v==0 for v in checks.values())
result={'beta':str(b),'w':str(w),'checks':{k:str(v) for k,v in checks.items()},
        'quadratic_subfields_square_classes':['3*T*(1-T)','3*(T-1)','-3*T'],
        'product_square_class':3,'geometric_group_order':108,
        'arithmetic_group_order':216,'constant_field':'Q(sqrt(3))',
        'arithmetic_outer_image_order':2,'complex_conjugation_outer_image':'identity'}
path=Path(__file__).resolve().parent
(path/'finite_s3_fields.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

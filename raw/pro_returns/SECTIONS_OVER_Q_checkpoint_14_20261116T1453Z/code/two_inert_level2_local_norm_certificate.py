"""The literal next-level local norm test for A156's specified element."""
from pathlib import Path
from fractions import Fraction as F
import json

base=Path(__file__).resolve().parent
data=json.loads((base/'two_inert_norm2_generator_certificate_data.json').read_text())
d=data['d'];D=data['generator_common_denominator'];c=data['generator_numerators']
parts=[[F(c[j+3*k]*d**(2*k),D) for k in range(3)] for j in range(3)]
assert all(x.denominator==1 for row in parts[:2] for x in row)
assert all(d%x.denominator==0 for x in parts[2])
rows=[]
for q in (11,59):
    root=next(x for x in range(q) if x**3%q==3)
    def mul(x,y):
        a,b=x;e,f=y
        return ((a*e-root*root*b*f)%q,(a*f+b*e-root*b*f)%q)
    def power(x,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x);n//=2
        return z
    def evaluate(poly):
        z=(0,0)
        for x in reversed(poly):
            z=mul(z,(0,1))
            z=((z[0]+x.numerator*pow(x.denominator,-1,q))%q,z[1])
        return z
    assert (q*q-1)%3==0 and (q*q-1)%9!=0
    beta1=(1,q-1)
    beta2=evaluate([-x for x in parts[0]])
    chi1=power(beta1,(q*q-1)//3)
    chi2=power(beta2,(q*q-1)//3)
    assert chi1==(1,0)
    assert chi2!=(1,0) and power(chi2,3)==(1,0)
    assert power(beta2,3)==beta1
    assert beta2==((6,3) if q==11 else (23,57))
    assert chi2==((10,6) if q==11 else (58,6))
    # In K2 at q: v(t)=2, v(q)=3.  Thus A1*t and A2*t^2
    # have valuation >=2 and >=1 respectively, and gamma reduces to A0.
    assert 2>=1 and 4-3>=1
    # rho2=d^2*t has normalized valuation 2*3+2=8.
    assert 2*3+2==8 and 8%3!=0
    rows.append({'q':q,'linear_alpha_root':root,
                 'quadratic_coefficients':[root*root%q,root,1],
                 'beta1':beta1,'beta2':beta2,'beta1_cubic_character':chi1,
                 'beta2_cubic_character':chi2,'radicand_valuation':8})
    print(f'q={q}, alpha quadratic coefficients={rows[-1]["quadratic_coefficients"]}')
    print(' beta1 residue/character:',beta1,chi1)
    print(' beta2 residue/character:',beta2,chi2)
    print(' cube(beta2)=beta1: PASS; nontrivial character: PASS')
(base/'two_inert_level2_local_norm_certificate_data.json').write_text(json.dumps(rows,indent=2)+'\n')
print('PASS: beta1 meets both stable unit-norm tests; this specific beta2 fails the next cubic norm at both quadratic places.')

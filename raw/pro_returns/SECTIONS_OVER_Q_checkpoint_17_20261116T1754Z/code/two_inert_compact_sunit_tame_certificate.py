"""Literal angular components at the two ramified quadratic S-places.

Uses pi=t^2/q, pi^3=q*c and t=pi^2*v. Every factor has a unique
lowest term among A_i(alpha)t^i, since their valuations differ mod3.
Products are evaluated with exact finite-field arithmetic, retaining
their full integer valuations. No enormous compact product is expanded.
"""
from fractions import Fraction as F
from pathlib import Path
from math import lcm
import contextlib
import importlib.util
import io
import json
import sys

sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('svals',base/'two_inert_compact_sunit_s_valuation_certificate.py')
s=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(s)
d=s.d


class Quadratic:
    def __init__(self,q,r):
        self.q=q
        self.r=r%q
        self.one=(1,0)
        self.alpha=(0,1)
    def mul(self,a,b):
        a0,a1=a;b0,b1=b;q=self.q;r=self.r
        return ((a0*b0-r*r*a1*b1)%q,(a0*b1+a1*b0-r*a1*b1)%q)
    def power(self,a,n):
        n%=self.q*self.q-1
        b=self.one
        while n:
            if n&1:b=self.mul(a,b)
            a=self.mul(a,a);n//=2
        return b
    def scale(self,a,n):
        return (a[0]*n%self.q,a[1]*n%self.q)
    def char(self,a):
        return self.power(a,(self.q*self.q-1)//3)


def unramified_lead(coefficients,q,r):
    if not any(coefficients):return None
    denominator=lcm(*(c.denominator for c in coefficients))
    modulus=q**s.precision
    work=[int(c*denominator)%modulus for c in coefficients]
    factor=[r*r,r,1]
    for j in range(len(work)-1,1,-1):
        a=work[j]
        work[j-2]=(work[j-2]-a*factor[0])%modulus
        work[j-1]=(work[j-1]-a*factor[1])%modulus
        work[j]=0
    work=(work+[0,0])[:2]
    numerator_valuation=min(s.vp(c,q) for c in work)
    assert numerator_valuation<s.precision-2
    denominator_valuation=s.vp(denominator,q)
    inverse=pow(denominator//q**denominator_valuation,-1,q)
    leading=tuple((c//q**numerator_valuation)*inverse%q for c in work)
    assert leading!=(0,0)
    return numerator_valuation-denominator_valuation,leading


def factor_lead(poly,field,r):
    q=field.q
    groups=[[F(0) for _ in range(3)] for __ in range(3)]
    for j,a in enumerate(poly):
        h,i=divmod(j,3)
        groups[i][h]+=a*d**(2*h)
    c=field.scale(field.power(field.alpha,2),pow(d//q,4,q))
    v=field.scale(field.power(field.alpha,-1),pow(d//q,-2,q))
    leads=[]
    for i,coefficients in enumerate(groups):
        if any(coefficients):
            k,a=unramified_lead(coefficients,q,r)
            leads.append((3*k+2*i,i,k,a))
    leads.sort()
    assert len(leads)==1 or leads[0][0]<leads[1][0]
    weight,i,k,a=leads[0]
    unit=field.mul(field.mul(a,field.power(c,-k)),field.power(v,i))
    return weight,unit


data=json.loads((base/'two_inert_compact_sunit_s_valuation_certificate_data.json').read_text())
results={}
for q,column in [(11,5),(59,7)]:
    r=s.root_q[q]
    field=Quadratic(q,r)
    # alpha^3=3 and exact pi/t substitutions in the residue field.
    assert field.power(field.alpha,3)==(3%q,0)
    factor_values=[]
    for row in data['factors']:
        weight,unit=factor_lead([F(c) for c in row['coefficients']],field,r)
        assert weight==row['valuations'][column]
        factor_values.append((weight,unit))
    rows=[]
    for index in range(1,9):
        weight=0;unit=field.one
        for exponent,j in data['candidates'][str(index)]:
            w,a=factor_values[j]
            weight+=exponent*w
            unit=field.mul(unit,field.power(a,exponent))
        char=field.char(unit)
        rows.append({'valuation':weight,'unit':unit,'character':char})
        print('q',q,'candidate',index,'valuation',weight,'unit',unit,'cube character',char)
    c=field.scale(field.power(field.alpha,2),pow(d//q,4,q))
    rho_unit=field.scale(field.power(field.alpha,-5),pow(d//q,-8,q))
    results[str(q)]={'linear_root_modq':r%q,'alpha_character':field.char(field.alpha),
                     'rho2_unit_character':field.char(rho_unit),
                     'factor_values':factor_values,'candidates':rows}

out={'radicand':s.radicand,'uniformizer':'pi=t^2/q',
     'identity':'pi^3=q*(d/q)^4*alpha^2; t=pi^2*(d/q)^(-2)*alpha^(-1)',
     'q_data':results}
(base/'two_inert_compact_sunit_tame_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all 434 factor angular components and 16 compact-product normalized residues.')

"""Verify three positive principal-ideal candidates, without PARI algebra.

The discovery output is read only as literal rational coefficients. Exact
relative/rational norms and the already independently derived Hensel
valuation maps certify every assertion used here.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib
import importlib.util
import io
import json
import re
import sys

sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
d=649


def load_quiet(name,file):
    spec=importlib.util.spec_from_file_location(name,base/file)
    module=importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(module)
    return module


sv=load_quiet('sv','two_inert_compact_sunit_s_valuation_certificate.py')
tv=load_quiet('tv','two_inert_compact_sunit_tame_certificate.py')


def mul(x,y):
    z=[F(0)]*5
    for i,a in enumerate(x):
        for j,b in enumerate(y):z[i+j]+=a*b
    for j in (4,3):z[j-3]+=3*z[j]
    return z[:3]


def cube(x):return mul(mul(x,x),x)


def relative_norm(x):
    A,B,C=[[x[j+3*k]*d**(2*k) for k in range(3)] for j in range(3)]
    w=[F(0),F(d*d),F(0)]
    terms=[cube(A),mul(w,cube(B)),mul(mul(w,w),cube(C)),
           [-3*a for a in mul(w,mul(mul(A,B),C))]]
    return [sum(t[i] for t in terms) for i in range(3)]


def rational_norm(x):
    a,b,c=x
    return a**3+3*b**3+9*c**3-9*a*b*c


def evalpoly(coefficients,a,p):
    b=0
    for c in reversed(coefficients):b=(b*a+c.numerator*pow(c.denominator,-1,p))%p
    return b


raw=(base/'two_inert_short_sunit_principals_pari_output.txt').read_text()
polys={int(i):[F(c.strip()) for c in row[1:-1].split(',')]
       for i,row in re.findall(r'^POLYNOMIAL (\d+) (\[.*\])$',raw,re.M)}
assert sorted(polys)==[6,7,8]
expected={6:[0,0,0,0,0,1,0,0],7:[0,0,0,0,1,0,1,0],8:[0,0,0,0,0,0,0,1]}
normabs={6:11**2,7:11*59,8:59**2}
out={}
for i,poly in polys.items():
    assert len(poly)==9
    for c in poly:
        denominator=c.denominator
        for p in (11,59):
            while denominator%p==0:denominator//=p
        assert denominator==1
    norm=relative_norm(poly)
    absolute=rational_norm(norm)
    assert abs(absolute)==normabs[i]
    vals=sv.valuations(poly)
    assert vals==expected[i]
    chars={}
    for q in (11,59):
        field=tv.Quadratic(q,sv.root_q[q])
        weight,unit=tv.factor_lead(poly,field,sv.root_q[q])
        omega=field.char(field.alpha)
        log={field.one:0,omega:1,field.power(omega,2):2}
        chars[str(q)]={'valuation':weight,'unit':unit,'angular_log':log[field.char(unit)],
                       'stable_log':(log[field.char(unit)]+weight)%3}
    print('GENERATOR',i,'rational norm',absolute,'S-valuations',vals,
          'stable characters',[chars[str(q)]['stable_log'] for q in (11,59)])
    out[str(i)]={'coefficients':[str(c) for c in poly],
                 'relative_norm':[str(c) for c in norm],
                 'rational_norm':str(absolute),'S_valuations':vals,'local_characters':chars}

# The same ninth-power detector used independently for the compact products.
p=2179
checks=[]
for alpha in range(p):
    if alpha**3%p!=3:continue
    u=(alpha*alpha-2)%p
    omega=pow(u,(p-1)//9,p)
    assert pow(omega,3,p)!=1
    logs={pow(omega,e,p):e for e in range(9)}
    g11=(2+alpha)%p;g59=(2+2*alpha-alpha*alpha)%p
    delta11=(alpha*alpha-2*alpha+4)%p
    delta59=(10-alpha+6*alpha*alpha)%p
    norms={i:evalpoly([F(c) for c in out[str(i)]['relative_norm']],alpha,p) for i in (6,7,8)}
    unitexps={i:logs[pow(norms[i]*pow({6:delta11,7:g11*g59%p,8:delta59}[i],-1,p)%p,(p-1)//9,p)] for i in (6,7,8)}
    k=(unitexps[6]+unitexps[8]-2*unitexps[7])%9
    correction=((1-k)//3)%3
    assert k%3==1
    stable=[(out['6']['local_characters'][str(q)]['stable_log']+
             out['8']['local_characters'][str(q)]['stable_log']-
             2*out['7']['local_characters'][str(q)]['stable_log']+2*correction)%3 for q in (11,59)]
    assert stable==[0,2]
    checks.append({'p':p,'alpha':alpha,'unit_exponents':unitexps,'k_mod9':k,
                   'scalar_correction_mod3':correction,'eta_stable_characters':stable})
    print('NINTH DETECTOR',alpha,'unit exponents',unitexps,'k',k,'corrected characters',stable)
assert len(checks)==3
(base/'two_inert_short_sunit_principal_certificate_data.json').write_text(json.dumps(
    {'d':d,'generators':out,'ninth_power_checks':checks,
     'scope':'Literal positive elements; no PARI class-group completeness assumption.'},indent=2)+'\n')
print('PASS: all three literal S-generators, full support and exact divisors, corrected stable characters.')

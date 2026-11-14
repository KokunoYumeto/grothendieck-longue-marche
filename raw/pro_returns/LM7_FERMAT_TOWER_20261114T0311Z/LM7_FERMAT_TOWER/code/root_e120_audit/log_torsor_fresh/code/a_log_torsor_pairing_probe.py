#!/usr/bin/env python3
"""Independent Miller pairing on the already retained E[27] point basis."""
from pathlib import Path
import json

base=Path(__file__).resolve().parent
source=json.loads((base/'a_elliptic_theta_pi.json').read_text())
mod=source['finite_field']['irreducible_modulus_bits']
q=source['finite_field']['size']

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a>=q:a^=mod
    return out

def power(a,n):
    out=1
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n>>=1
    return out

def div(a,b):
    assert b
    return mul(a,power(b,q-2))

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y!=v:return None
        slope=mul(x,x)
    else:slope=div(y^v,x^u)
    w=mul(slope,slope)^x^u
    return w,mul(slope,w^x)^y^1

def scale(k,P):
    out=None
    if k<0:
        P=P[0],P[1]^1;k=-k
    while k:
        if k&1:out=add(out,P)
        P=add(P,P);k>>=1
    return out

def line_step(P,Q,R):
    if P is None or Q is None:return 1
    x,y=P;u,v=Q;X,Y=R
    if x==u and y!=v:return X^x
    slope=mul(x,x) if P==Q else div(y^v,x^u)
    top=Y^y^mul(slope,X^x)
    S=add(P,Q)
    assert S is not None
    return div(top,X^S[0])

def miller(n,P,R):
    value=1;T=P;steps=[]
    for bit in bin(n)[3:]:
        factor=line_step(T,T,R)
        value=mul(mul(value,value),factor)
        T=add(T,T)
        steps.append({'type':'double','factor':factor,'point':T,'value':value})
        if bit=='1':
            factor=line_step(T,P,R)
            value=mul(value,factor);T=add(T,P)
            steps.append({'type':'add','factor':factor,'point':T,'value':value})
    assert T is None
    return value,steps

P,Q=map(tuple,source['actual_E27_basis'])
zeta9=source['finite_field']['zeta9']
zeta3=source['finite_field']['zeta3']
roots=[a for a in range(1,q) if power(a,3)==zeta9]
assert len(roots)==3
zeta27=min(roots)
assert power(zeta27,27)==1 and power(zeta27,9)==zeta3
records=[]
for n,step,zeta in [(3,9,zeta3),(9,3,zeta9),(27,1,zeta27)]:
    p,r=scale(step,P),scale(step,Q)
    f,fs=miller(n,p,r);g,gs=miller(n,r,p)
    e=div(f,g)
    exponents=[a for a in range(n) if power(zeta,a)==e]
    assert len(exponents)==1 and exponents[0]%3==1
    # Independent bilinearity checks use differently multiplied inputs.
    tests=[]
    for a,b in [(2,1),(1,2),(2,2),(4,5)]:
        pp,rr=scale(a,p),scale(b,r)
        ff,_=miller(n,pp,rr);gg,_=miller(n,rr,pp)
        ee=div(ff,gg)
        assert ee==power(e,(a*b)%n)
        tests.append([a,b,ee])
    records.append({'order':n,'points':[p,r],'root':zeta,'forward_function':f,
                    'reverse_function':g,'pairing':e,'exponent':exponents[0],
                    'forward_steps':fs,'reverse_steps':gs,'bilinear_tests':tests})
assert records[1]['exponent']%3==records[0]['exponent']
assert records[2]['exponent']%9==records[1]['exponent']
output={'status':'PASS','field':source['finite_field'],'zeta27':zeta27,
        'pairings':records,'scope':'actual retained division basis; no unknown intrinsic action assigned'}
(base/'a_log_torsor_pairing_probe.json').write_text(json.dumps(output,indent=2)+'\n')
print('PASS: literal Miller pairings on E[3], E[9], E[27] and 12 bilinearity identities')
print('Weil unit modulo 27:',records[-1]['exponent'],'; zeta27:',zeta27)

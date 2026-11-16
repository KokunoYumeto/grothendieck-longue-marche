#!/usr/bin/env python3
"""Exact Hall-coordinate inertia correction for the three actual cusp meridians.

This is finite symbolic algebra in the degree-three Magnus ring.  The source
proof supplies local comparison, strict continuous residue, and global lifting.
"""
from collections import defaultdict
from pathlib import Path
import json
import sympy as S

r,s,h,m=S.symbols('r s h m')
one={():S.Integer(1)}
def clean(p):
    return {w:S.expand(v) for w,v in p.items() if S.expand(v)!=0}
def add(*ps):
    out=defaultdict(lambda:S.Integer(0))
    for p in ps:
        for w,v in p.items():out[w]+=v
    return clean(out)
def scale(p,a):return clean({w:a*v for w,v in p.items()})
def mul(*ps):
    out=one
    for p in ps:
        nxt=defaultdict(lambda:S.Integer(0))
        for w,v in out.items():
            for u,z in p.items():
                if len(w)+len(u)<=3:nxt[w+u]+=v*z
        out=clean(nxt)
    return out
def power(p,n):
    u=add(p,scale(one,-1));n=S.sympify(n)
    return add(one,scale(u,n),scale(mul(u,u),n*(n-1)/2),
               scale(mul(u,u,u),n*(n-1)*(n-2)/6))
def comm(p,q):return mul(p,q,power(p,-1),power(q,-1))
x={():S.Integer(1),('X',):S.Integer(1)}
y={():S.Integer(1),('Y',):S.Integer(1)}
C=comm(x,y);D=comm(C,x);F=comm(C,y)
def hall(a,b,c):return mul(power(y,b),power(x,a),power(C,c))
delta=hall(r,s,h)
data=[]
for label,c in [('0',x),('1',y),('infinity',power(mul(x,y),-1))]:
    word=mul(delta,power(c,m),power(delta,-1))
    a=word.get(('X',),0);b=word.get(('Y',),0);cc=word.get(('X','Y'),0)
    correction=mul(word,power(hall(a,b,cc),-1))
    assert all(w==() or len(w)==3 for w in correction)
    d=-correction.get(('X','X','Y'),0)
    f=correction.get(('X','Y','Y'),0)
    assert correction==mul(power(D,d),power(F,f))
    assert S.expand(d.subs(m,0))==S.expand(f.subs(m,0))==0
    bounds=[]
    for v in [d,f]:
        p=S.Poly(S.cancel(6*v/m),r,s,h,m)
        assert all(z.is_Integer for z in p.coeffs())
        bounds.append(str(p.as_expr()))
    print('PASS: cusp',label,'abelian coordinates',a,b,'and Hall coordinate',S.factor(cc))
    print('  central D =',S.factor(d))
    print('  central F =',S.factor(f))
    data.append({'cusp':label,'a':str(a),'b':str(b),'hall_h':str(S.factor(cc)),
                 'D':str(S.factor(d)),'F':str(S.factor(f)),
                 'six_correction_divided_by_m':bounds})
print('PASS: both central coordinates satisfy v_ell(correction)>=v_ell(m)-v_ell(6), uniformly in the conjugator.')
out={'rows':data,'uniform_denominator':6,
     'scope':'Literal free class-three Hall word identities; continuous cohomology and local section comparisons are proved separately.'}
Path(__file__).with_name('selmer_class_two_to_three_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')

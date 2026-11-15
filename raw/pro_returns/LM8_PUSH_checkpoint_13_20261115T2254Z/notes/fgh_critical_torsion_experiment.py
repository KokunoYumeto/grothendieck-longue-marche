#!/usr/bin/env python3
"""Exact finite tests: can critical centres have odd order?

This does not assert a stable model for enlarged marked sets. It tests
division functions modulo every critical x-factor over finite fields.
"""
from pathlib import Path
from functools import lru_cache
import importlib.util,json
import sympy as s

here=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('a',here/'fgh_A61_certificate.py')
a=importlib.util.module_from_spec(sp);sp.loader.exec_module(a)
x=a.x


def test_factor(p,pol):
    pol=pol.monic();d=pol.degree()
    def red(t): return s.Poly(t,x,modulus=p).rem(pol)
    one=red(1);zero=red(0);X=red(x);f=red(x**3-x)
    @lru_cache(None)
    def div(n):
        if n==0:return zero
        if n in (1,2):return one
        if n==3:return red(3*x**4-6*x*x-1)
        if n==4:return red(2*(x**6-5*x**4-5*x*x+1))
        if n%2:
            m=(n-1)//2
            A=red(div(m+2)*red(div(m)**3))
            B=red(div(m-1)*red(div(m+1)**3))
            return red(A-16*f*f*B) if m%2 else red(16*f*f*A-B)
        m=n//2
        return red(div(m)*red(div(m+2)*red(div(m-1)**2)-div(m-2)*red(div(m+1)**2)))
    count=1+sum(sum((y*y-(z**3-z))%p==0 for y in range(p)) for z in range(p))
    trace=p+1-count
    t0,t1=2,trace
    for k in range(2,2*d+1):t0,t1=t1,trace*t1-p*t0
    N=p**(2*d)+1-t1
    odd=N
    while odd%2==0:odd//=2
    v=div(odd)
    exact_order=None
    if v.is_zero:
        exact_order=odd
        for prime in s.factorint(odd):
            while exact_order%prime==0 and div(exact_order//prime).is_zero:
                exact_order//=prime
    return {'p':p,'factor':str(pol.as_expr()),'degree':d,
            'field_extension_degree':2*d,'elliptic_group_order':N,
            'odd_part':odd,'odd_order_points':v.is_zero,'exact_odd_order':exact_order,
            'division_remainder':str(v.as_expr())}


rows=[]
for p in (7,11,13,17,19,23,29,31,37,41):
    Q=a.pairmod(a.dpow((a.X,a.ZERO),p-2),p)[1].set_modulus(p)
    factors=s.factor_list(Q)[1]
    rr=[]
    for P,e in factors:
        assert e==1
        if s.gcd(P,a.f.set_modulus(p)).degree()>0:continue
        z=test_factor(p,P);rows.append(z);rr.append(z)
    print(p,[(z['factor'],z['odd_order_points']) for z in rr],flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact finite torsion checks only; no enlarged-cover conclusion.','rows':rows},indent=2)+'\n')

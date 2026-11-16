#!/usr/bin/env python3
"""Actual finite Heisenberg Frobenius probes at the two flex-pencil values.

For m=3^r the cover is u^m=t, v^m=1-t,
w^m=prod_i(1-zeta_m^i*u)^i.  We use primes where both
abelian Kummer coordinates vanish, so its central Frobenius
is independent of all choices of u and v.  No finite output
is interpreted as an infinite 3-adic value.
"""
from pathlib import Path
import json
import sympy as sp
from math import gcd

arithmetic_checks=0
for m in [3,9,27,81]:
    units=[c for c in range(1,m) if gcd(c,m)==1]
    for c in units:
        rc=pow(c,-1,m)
        assert all((rc*j)%m==rc*j-m*((rc*j)//m) for j in range(m))
        for d in units:
            rd=pow(d,-1,m);r_cd=pow(c*d,-1,m)
            k=(rc*rd-r_cd)//m
            assert all(k*j-rd*((rc*j)//m)-(rd*((rc*j)%m))//m+(r_cd*j)//m==0
                       for j in range(m))
            arithmetic_checks+=1

def central(q,m,z,g):
    xi=pow(g,(q-1)//m,q)
    # A finite field root is found exactly; m<=81 in this certificate.
    root=sp.nthroot_mod(z,m,q)
    if root is None:return None
    if pow((1-z)%q,(q-1)//m,q)!=1:return None
    u=int(root)
    def product(u):
        out=1
        for i in range(m):out=out*pow((1-pow(xi,i,q)*u)%q,i,q)%q
        return out
    E=product(u)
    value=pow(E,(q-1)//m,q)
    log=next(i for i in range(m) if pow(xi,i,q)==value)
    # The central conjugacy invariant must be independent of the root u.
    assert all(pow(product(u*pow(xi,j,q)%q),(q-1)//m,q)==value for j in range(m))
    # Exact shift identity from the displayed algebraic cover.
    assert product(xi*u%q)*pow(E,-1,q)%q==pow((1-u)%q,m,q)*pow((1-z)%q,-1,q)%q
    return {'u':u,'epsilon':E,'character_value':value,'central_coordinate':log}

records=[]
for r in [1,2,3,4]:
    m=3**r;found=[]
    for j in range(1,100000):
        q=3*m*j+1
        if not sp.isprime(q):continue
        g=int(sp.primitive_root(q));zeta=pow(g,(q-1)//3,q)
        z1=zeta*zeta%q;z2=pow((1-z1)%q,-1,q)
        if pow((1-z1)%q,(q-1)//m,q)!=1:continue
        a=central(q,m,z1,g);b=central(q,m,z2,g)
        assert a is not None and b is not None
        # The six-term Bloch orbit gives this equality on the common
        # zero-abelian Frobenius locus; it is checked, not assumed.
        assert a['central_coordinate']==b['central_coordinate']
        xi=pow(g,(q-1)//m,q)
        cinfinity=pow(-1,m*(m-1)//2,q)*pow(xi,sum(i*i for i in range(m)),q)%q
        assert cinfinity==pow(-1,(m-1)//2,q)*z1%q
        endpoint1=zeta*pow(3,-1,q)%q
        endpoint2=-pow(3,-1,q)%q
        assert all(pow(x,(q-1)//m,q)==1 for x in [cinfinity,endpoint1,endpoint2])
        if a['central_coordinate']==0:continue
        rec={'r':r,'m':m,'prime':q,'primitive_root':g,'zeta3':zeta,
             'z1':z1,'z2':z2,'probe1':a,'probe2':b,
             'all_m_root_choices_checked':True}
        rec['tangent_leading_scalars']=[endpoint1,endpoint2]
        rec['infinity_product_leading_constant']=cinfinity
        rec['actual_relative_cusp_deck_coordinates']=[(-a['central_coordinate'])%m,(-b['central_coordinate'])%m]
        rec['actual_relative_cusp_intrinsic_Hall_coordinates']=[a['central_coordinate'],b['central_coordinate']]
        rec['lower_level_coordinates']=[]
        for rr in range(1,r):
            mm=3**rr;aa=central(q,mm,z1,g);bb=central(q,mm,z2,g)
            assert aa['central_coordinate']==a['central_coordinate']%mm
            assert bb['central_coordinate']==b['central_coordinate']%mm
            rec['lower_level_coordinates'].append([mm,aa['central_coordinate']])
        found.append(rec);print(json.dumps(rec),flush=True)
        if len(found)==2:break
    assert len(found)==2
    records.extend(found)
Path('deliverable/code/b_dilog_frobenius.json').write_text(json.dumps({
 'cover':'u^m=t, v^m=1-t, w^m=product_(i=0)^(m-1)(1-zeta_m^i*u)^i',
 'status':'executed exact finite central Frobenius values',
 'arithmetic_lift_composition_checks':arithmetic_checks,
 'marking':'h=[b_deck,a_deck] multiplies w by xi; intrinsic c=[R_b,R_a]=h^-1. Point Frobenius is h^k, relative cusp is h^-k=c^k.',
 'scope':'These are actual finite point-fibre and marked cusp-origin projections. Raw values are nonabelian affine data, not the missing linear action coordinates. Their full quadratic comparison with a specified original-lattice reference remains uncomputed.',
 'records':records},indent=2)+'\n')

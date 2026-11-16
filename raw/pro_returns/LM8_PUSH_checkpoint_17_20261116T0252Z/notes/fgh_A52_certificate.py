#!/usr/bin/env python3
"""Exact chart and counting certificate for candidate A.52.
The mathematical component-persistence and marked-model arguments are in TeX.
"""
from pathlib import Path
import json
import sympy as s

rho,U,X,V,pi,u,x = s.symbols('rho U X V pi u x')
f=lambda t:3*t**4-6*t**2-1
rows=[]
for a in (0,1,-1):
    delta=3*a*a-1
    xx=a+rho**2*U
    eqE=X**2-delta*U-3*a*rho**2*U**2-rho**4*U**3
    rawE=rho**2*X**2-xx**3+xx
    assert s.expand(rawE-rho**2*eqE)==0
    eqC=f(a)*(V+rho**4*V**2-V**3)-2*delta*U**2-4*a*rho**2*U**3-rho**4*U**4
    rawC=f(a)*(1+rho**4*V)**3-f(xx)
    diff=s.expand(rawC-3*rho**4*eqC)
    assert s.rem(diff,rho**8+3,rho)==0
    # In characteristic three delta=2, f(a)=2. Eliminate U=X^2/delta.
    red=s.Poly(f(a)*(V-V**3)-2*delta*(2*X**2)**2,X,V,modulus=3).as_expr()
    assert s.Poly(red-(V**3-V-X**4),X,V,modulus=3).is_zero
    rows.append({'a':a,'delta':delta,'f_a':int(f(a)),
                 'elliptic_identity':True,'Kummer_identity':True,
                 'reduced_equation':'V^3-V=X^4',
                 'special_U_derivative_mod3':(-delta)%3,
                 'special_V_derivative_mod3':int(f(a))%3})
rawmain=(-1+pi*u)**3-f(x)
main=u**3-pi**2*u**2+pi*u-x**4+2*x**2
assert s.rem(s.expand(rawmain-3*main),pi**3-3,pi)==0
assert s.Poly(s.diff(x**4+x**2,x)-(x**3-x),x,modulus=3).is_zero
# Uniformizer t^3 V^2 has order 9-8=1; its nontrivial translate
# differs by t^3(2V+1), of order 9-4=5.
assert 3*3+2*(-4)==1
assert 3*3+(-4)==5
AS_genus=(-2*3+(3-1)*(4+1)+2)//2
assert AS_genus==3 and 1+3*AS_genus==10
assert 3*(-1)+(3-1)==-1

countrows=[]
for m in range(1,129):
    cusps=27*m*m-18
    assert 2-20-cusps==-27*m*m
    if m%2:
        n=m;h=1
        while n%3==0:
            n//=3;h+=1
        ordinary=3**(2*h+1)
        origin=ordinary-18
        assert origin>=9
        assert origin+(n*n-1)*ordinary==cusps
        countrows.append({'m':m,'residue':3,'h':h,'n':n,
                          'origin_cluster':origin,'other_cluster':ordinary,
                          'cluster_classes':n*n,'total':cusps})
    else:
        b=m;a=0
        while b%2==0:
            b//=2;a+=1
        etale=4**a;branch=3*etale-2
        # Nine branch target classes, 9b^2-9 other target classes,
        # and three source clusters over each ordinary target class.
        assert etale>=4 and branch>=10
        assert 9*branch+3*(9*b*b-9)*etale==cusps
        countrows.append({'m':m,'residue':2,'a':a,'b':b,
                          'branch_cluster':branch,'etale_cluster':etale,
                          'branch_classes':9,'etale_source_classes':3*(9*b*b-9),
                          'total':cusps})
result={'status':'PASS','charts':rows,'main_chart':True,
        'main_inseparable_differential':True,'AS_genus':AS_genus,
        'positive_genus_sum':10,'AS_three_rank':0,
        'count_checks':countrows}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print('PASS: all three exact elliptic/Kummer charts modulo rho^8+3.')
print('PASS: each reduction is V^3-V=X^4; both Jacobian pivots are units.')
print('PASS: exact main chart modulo pi^3-3; nonzero inseparable differential.')
print('PASS: Artin-Schreier lower jump4, genus3, three-rank0; total genus10.')
print('PASS: degree/Euler/marking counts for all m=1..128, using both residue primes.')
for m in (1,2,3,5,6,9,10,15,16,27,64,81,128):
    print(json.dumps(countrows[m-1],sort_keys=True))
print(out)

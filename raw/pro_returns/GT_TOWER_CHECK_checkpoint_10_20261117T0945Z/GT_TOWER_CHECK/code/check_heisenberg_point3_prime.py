#!/usr/bin/env python3
"""Small finite-field certificate; its q is NOT the factorial recursion's q0."""
from sympy import isprime, primitive_root, nthroot_mod

for k in range(1, 1_000_001):
    q=600*k+1
    if not isprime(q):
        continue
    if pow(q-2,(q-1)//120,q)!=1 or pow(3,(q-1)//5,q)!=1:
        continue
    zeta=pow(int(primitive_root(q)),(q-1)//5,q)
    x=int(nthroot_mod(3,5,q))
    theta=1
    for i in range(5):
        theta=theta*pow((1-pow(zeta,i,q)*x)%q,i,q)%q
    symbol=pow(theta,(q-1)//5,q)
    if symbol==1:
        continue
    y=int(nthroot_mod(q-2,120,q))
    assert pow(y,120,q)==q-2 and pow(x,5,q)==3
    assert zeta!=1 and pow(zeta,5,q)==1
    assert q%600==1 and symbol!=1 and pow(symbol,5,q)==1
    print('Small test prime q =',q,'(not the recursively defined q0)')
    print('zeta5 =',zeta,'; x =',x,'; (-2)^(1/120) =',y)
    print('theta =',theta,'; theta^((q-1)/5) =',symbol)
    print('PASS: q=1 mod600; both required radical classes split; central Frobenius nonzero')
    for lam in range(1,5):
        for j in range(5):
            zz=pow(zeta,lam,q)
            xx=x*pow(zeta,j,q)%q
            value=1
            for i in range(5):
                value=value*pow((1-pow(zz,i,q)*xx)%q,i,q)%q
            assert pow(value,(q-1)//5,q)!=1
    print('PASS: the nonzero test is independent of all20 choices of zeta and x')
    break
else:
    raise AssertionError('No witness found in the explicitly bounded test range')

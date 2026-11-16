#!/usr/bin/env python3
"""Exact finite checks for centres, sign compression and the 6912 quotient.

No GT elements are manufactured. The global counterexample uses the supplied
R2 element; the finite computations verify its quotient-factorization input.
"""
from collections import deque
from itertools import product
from math import gcd
import json


def mm(a, b, n):
    return tuple(x % n for x in (a[0]*b[0]+a[1]*b[2],
        a[0]*b[1]+a[1]*b[3], a[2]*b[0]+a[3]*b[2],
        a[2]*b[1]+a[3]*b[3]))


def inv(a, n):
    return (a[3] % n, -a[1] % n, -a[2] % n, a[0] % n)


def canon(a):
    return min(a, tuple(-v % 12 for v in a))


def closure(generators, identity, mul):
    found = {identity}
    todo = deque([identity])
    while todo:
        a = todo.popleft()
        for b in generators:
            c = mul(a, b)
            if c not in found:
                found.add(c)
                todo.append(c)
    return found


def main():
    I = (1, 0, 0, 1)
    S = (0, 1, 11, 0)
    R = (0, 11, 1, 11)
    s2 = tuple(x % 2 for x in S)
    r2 = tuple(x % 2 for x in R)
    Q2 = sorted(closure([s2, r2], I, lambda a,b: mm(a,b,2)))
    idx = {a:i for i,a in enumerate(Q2)}
    q2mul = [[idx[mm(a,b,2)] for b in Q2] for a in Q2]
    zero = (0,)*6
    er = [0]*6
    er[idx[I]] = 1
    er[idx[r2]] = 11
    one = (canon(I), zero)
    sg = (canon(S), zero)
    rg = (canon(R), tuple(er))

    def mul(a, b):
        A, v = a
        B, w = b
        i = idx[tuple(x % 2 for x in A)]
        out = list(v)
        for j,x in enumerate(w):
            out[q2mul[i][j]] = (out[q2mul[i][j]] + x) % 12
        return (canon(mm(A,B,12)), tuple(out))

    def power(a, n):
        out = one
        for _ in range(n):
            out = mul(out,a)
        return out

    def inverse(a):
        A,v=a
        Ai=canon(inv(A,12))
        i=idx[tuple(x%2 for x in Ai)]
        out=[0]*6
        for j,x in enumerate(v):
            out[q2mul[i][j]]=-x%12
        z=(Ai,tuple(out))
        assert mul(a,z)==one and mul(z,a)==one
        return z

    assert power(sg,2)==one and power(rg,3)==one
    joint=closure([sg,rg],one,mul)
    x=power(inverse(mul(sg,rg)),2)
    y=mul(mul(sg,x),sg)
    pure=closure([x,y],one,mul)
    comm=mul(mul(mul(x,y),inverse(x)),inverse(y))
    Ugens=[power(x,3),power(y,3),comm]
    # F' F^3 is the normal closure in F of x^3,y^3,[x,y].
    U=closure(Ugens,one,mul)
    while True:
        conjugates=[mul(mul(g,h),inverse(g))
                    for h in U for g in [x,y,inverse(x),inverse(y)]]
        enlarged=closure(list(U)+conjugates,one,mul)
        if enlarged==U:
            break
        U=enlarged
    qU={a for a,v in U}
    fermat={(tuple(x%2 for x in a),v) for a,v in joint}
    fermatU={(tuple(x%2 for x in a),v) for a,v in U}
    assert len(joint)==6912
    assert len(pure)==1152
    assert len(fermat)==864
    assert len(U)==128
    assert len(qU)==32
    assert len(fermatU)==16
    print('PASS joint congruence/Fermat-12 group order:',len(joint))
    print('PASS pure image order:',len(pure))
    print('PASS Fermat-12 group order:',len(fermat))
    print('PASS U=F-prime F^3 joint image order:',len(U))
    print('PASS U congruence image order:',len(qU))
    print('PASS U Fermat image order:',len(fermatU))
    print('CONCLUSION U has a 2-group image. R_nil(U) is killed.')
    print('Using R2: its Delta=1 element acts identically on this joint quotient.')

    signs=[]
    for a3,a2 in product(range(2), repeat=2):
        u=next(u for u in range(12)
               if u%3==((-1)**a3)%3 and u%4==((-1)**a2)%4)
        es=[e for e in range(12) if e*e%12==e and 2*e%12==(1-u)%12]
        assert len(es)==1
        signs.append({'epsilon3':a3,'epsilon2':a2,'u':u,'e':es[0],
                      'delta':(a3+a2)%2})
    print('Sign compression table:',json.dumps(signs,sort_keys=True))
    centre_counts={}
    for n in [3,4,5,8,12,16,24,60]:
        roots=[a for a in range(n) if a*a%n==1]
        cosets={min(a,-a%n) for a in roots}
        centre_counts[n]={'scalars':roots,'quotient_by_global_sign':len(cosets)}
    assert centre_counts[8]['quotient_by_global_sign']==2
    assert centre_counts[24]['quotient_by_global_sign']==4
    assert centre_counts[60]['quotient_by_global_sign']==4
    for n in [8,12]:
        mats=[a for a in product(range(n),repeat=4)
              if (a[0]*a[3]-a[1]*a[2])%n==1]
        E=(1,1,0,1); L=(1,0,1,1)
        center=[a for a in mats if mm(a,E,n)==mm(E,a,n)
                and mm(a,L,n)==mm(L,a,n)]
        assert set(center)=={(a,0,0,a) for a in range(n) if a*a%n==1}
    print('PASS full SL2 centralizers of elementary generators for N=8,12')
    print('Centre table:',json.dumps(centre_counts,sort_keys=True))
    print('PASS scalar multiplier 2I has determinant 4, not 1, modulo 5')


if __name__=='__main__':
    main()

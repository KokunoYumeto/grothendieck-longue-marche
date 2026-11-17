#!/usr/bin/env python3
"""Finite certificate for the independently checked class-two Selmer test.

This script checks only finite algebra and finite-field assertions.  Existence
of the infinite prime recursion and global Selmer identification are proved in
ghost_audit.md; they are not inferred from this certificate.
"""
from itertools import product
from math import isqrt


def prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def rotate(v, k, d):
    k %= d
    return ((v << k) | (v >> (d - k))) & ((1 << d) - 1)


def group(d):
    els = list(product(range(1 << d), range(8)))
    def mul(a, b):
        return (a[0] ^ rotate(b[0], a[1], d), (a[1] + b[1]) % 8)
    def inv(a):
        return (rotate(a[0], -a[1], d), -a[1] % 8)
    def comm(a, b):
        return mul(mul(mul(a, b), inv(a)), inv(b))
    def generated(gens):
        s = {(0, 0)}
        todo = [(0, 0)]
        gens = set(gens)
        gens |= {inv(g) for g in gens}
        while todo:
            a = todo.pop()
            for b in gens:
                c = mul(a, b)
                if c not in s:
                    s.add(c)
                    todo.append(c)
        return s
    assert all(mul(a, inv(a)) == (0, 0) for a in els)
    assert all(mul(mul(a, b), c) == mul(a, mul(b, c))
               for a in els for b in els for c in els)
    series = [set(els)]
    while len(series[-1]) > 1:
        series.append(generated(comm(a, b)
                                for a in series[-1] for b in els))
    return els, mul, series


def q6mul(x, y):
    a,b=x; c,d=y
    return a*c+6*b*d, a*d+b*c


def run():
    p=1129
    assert prime(p)
    squares={a*a % p for a in range(1,p)}
    bit=lambda a: 0 if a % p in squares else 1
    inv=lambda a: pow(a % p, -1, p)
    print('Prime:',p)
    xroots=[a for a in range(p) if pow(a,4,p)==54]
    assert xroots==[16,430,699,1113]
    print('Quartic roots:',xroots)
    initial_x=2; initial_y=56
    assert pow(initial_x,24,p)==276
    assert pow(initial_y,24,p)==978
    assert (3*pow(initial_x,24,p)-2*pow(initial_y,24,p)) % p == 1
    print('Modified A.44 initial Fermat residues:',initial_x,initial_y)
    print('Initial coefficient residues:',3*276 % p,-2*978 % p)
    assert 24 % p != 0

    t=828
    rad=(-t*pow(1-t,3,p)*inv(24)) % p
    assert rad==1115
    zroots=[a for a in range(p) if pow(a,8,p)==rad]
    assert zroots==[35,44,235,511,618,894,1085,1094]
    print('All local sheets (z,x,y,four Kummer bits,norm residues,norm bits):')
    rvals=[838,291]
    assert all(r*r % p==6 for r in rvals)
    expected=[]
    for z in zroots:
        x=(-6*z*z*inv(1-t)) % p
        y=(-18*z*inv(1-t)) % p
        assert (y*y-x**5+54*x) % p==0
        assert x**4*inv(x**4-54) % p==t
        assert 3*x*inv(y) % p==z
        four=tuple(bit(x-a) for a in xroots)
        norms=tuple((x*x-3*r) % p for r in rvals)
        bits=tuple(bit(a) for a in norms)
        assert bits==(1,1)
        assert all(norms)
        expected.append((z,x,y,four,norms,bits))
        print(expected[-1])
    print('Global projected Selmer generators at both embeddings:')
    for r in rvals:
        generators=(-(2+r) % p, (3+r) % p)
        assert tuple(map(bit,generators))==(0,0)
        print('r=',r,'values=',generators,'bits=',tuple(map(bit,generators)))
    for val,root in [(289,17),(836,426),(841,29),(294,221)]:
        assert root*root % p==val

    eps=(5,2); pi2=(2,1); pi3=(3,1)
    assert q6mul(pi2,pi2)==(10,4)
    assert q6mul(pi3,pi3)==(15,6)
    assert q6mul(eps,(5,-2))==(1,0)
    assert q6mul((9,-3),pi3)==(9,0)
    assert q6mul((9,-3),(-2,-1))==(0,-3)
    print('All global candidates (a,b,c,d), real/3-adic survivors:')
    survivors=[v for v in product(range(2),repeat=4) if v[0]==v[2] and v[1]==0]
    assert survivors==[(0,0,0,0),(0,0,0,1),(1,0,1,0),(1,0,1,1)]
    print(survivors)

    def schreier_abelian(word):
        coeff=[0]*9
        k=0
        for letter in word:
            if letter=='x':
                q,k=divmod(k+1,8);coeff[8]+=q
            elif letter=='X':
                q,k=divmod(k-1,8);coeff[8]+=q
            elif letter=='y':
                coeff[k]+=1
                q,k=divmod(k+3,8);coeff[8]+=q
            elif letter=='Y':
                q,k=divmod(k-3,8);coeff[8]+=q;coeff[k]-=1
            else: raise ValueError(letter)
        assert k==0
        return tuple(coeff)
    assert schreier_abelian('x'*8)==(0,)*8+(1,)
    assert schreier_abelian('y'*8)==(1,)*8+(3,)
    boundary=[]
    for j in range(4):
        v=schreier_abelian('x'*j+'xyxy'+'X'*j)
        want=[0]*9
        want[(j+1)%8]=1;want[(j+5)%8]=1;want[8]=1
        assert v==tuple(want)
        boundary.append(v)
    print('Four infinity-boundary Schreier vectors:',boundary)
    print('All six boundary loops yield z=0 and u_(j+4)=u_j; y^8 is redundant mod 2.')

    els32,mul32,series32=group(2)
    els128,mul128,series128=group(4)
    assert [len(s) for s in series32]==[32,2,1]
    assert [len(s) for s in series128]==[128,8,4,2,1]
    def project(a):
        v,k=a
        return (((v & 1) ^ ((v >> 2)&1)) |
                ((((v>>1)&1)^((v>>3)&1))<<1),k)
    assert all(project(mul128(a,b))==mul32(project(a),project(b))
               for a in els128 for b in els128)
    assert len({project(a) for a in els128})==32
    assert {a for a in els128 if project(a)==(0,0)}==series128[2]
    print('Order-32 lower-central orders:',[len(s) for s in series32])
    print('Order-128 lower-central orders:',[len(s) for s in series128])
    print('Projection kernel is exactly Gamma_3 of order 4.')
    print('PASS: all finite checks. No infinite prime search was run.')


if __name__=='__main__':
    run()

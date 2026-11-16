#!/usr/bin/env python3
"""Exact inverse-nome, local logarithm and common-multiplier checks for A.84."""

from math import comb


def vp(n,p):
    if n == 0:
        return float('inf')
    r = 0
    while n % p == 0:
        r += 1
        n //= p
    return r


def mul(a,b,degree):
    c = [0]*(degree+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j <= degree:
                c[i+j] += x*y
    return c


def inv(a,degree):
    b = [1]+[0]*degree
    assert a[0] == 1
    for k in range(1,degree+1):
        b[k] = -sum(a[i]*b[k-i] for i in range(1,k+1))
    return b


def evaluate(a,x,mod):
    v = 0
    for c in reversed(a):
        v = (v*x+c) % mod
    return v


def log_unit(u,p,precision):
    mod = p**precision
    z = (pow(u,p-1,mod)-1) % mod
    if z == 0:
        return 0
    depth = vp(z,p)
    result = 0
    for n in range(1,p*precision+5):
        denominator_depth = vp(n,p)
        if n*depth-denominator_depth >= precision:
            continue
        term = (z**n // p**denominator_depth)*pow(n//p**denominator_depth,-1,mod)
        result = (result + (-1)**(n+1)*term) % mod
    return result*pow(p-1,-1,mod) % mod


def unit_ratio(a,b,p,precision):
    d = vp(a,p)
    assert d == vp(b,p)
    mod = p**(precision-d)
    return (a//p**d)*pow(b//p**d,-1,mod) % mod, mod


degree = 12
e4 = [1]+[240*sum(d**3 for d in range(1,n+1) if n%d == 0)
           for n in range(1,degree+1)]
delta = [1]+[0]*degree
for n in range(1,degree+1):
    term = [0]*(degree+1)
    for k in range(min(24,degree//n)+1):
        term[n*k] = (-1)**k*comb(24,k)
    delta = mul(delta,term,degree)
phi = mul(mul(mul(e4,e4,degree),e4,degree),inv(delta,degree),degree)
assert phi[:5] == [1,744,196884,21493760,864299970]

precision = 7
data = {}
for p,w in ((17,-34),(5,35)):
    assert vp(w,p) == 1
    mod = p**(precision+2)
    numerator = 256*(w*w-w+1)**3
    denominator = w*w*(1-w)**2
    q = 0
    for _ in range(precision+4):
        q = denominator*evaluate(phi,q,mod)*pow(numerator,-1,mod) % mod
    assert (numerator*q-denominator*evaluate(phi,q,mod)) % mod == 0
    assert vp(q,p) == 2
    unit_mod = p**precision
    unit_q = q//(p*p)
    F = 256*unit_q*pow((w//p)**2,-1,unit_mod) % unit_mod
    log_F = log_unit(F,p,precision)
    assert F % (p*p) == (1+w) % (p*p)
    assert log_F % (p*p) == w % (p*p)
    data[p] = (q,F,log_unit(unit_q,p,precision),log_F)

log17_2 = log_unit(2,17,precision)
assert (log17_2//17) % 17 == 4
alpha17,mod17 = unit_ratio((-6*log17_2) % 17**precision,data[17][2],17,precision)
assert (data[17][2]//17) % 17 == 8
assert alpha17 % 17 == 14
assert pow(alpha17 % 17,8,17) == 16

L2 = log_unit(2,5,precision)
L17 = log_unit(17,5,precision)
L7 = log_unit(7,5,precision)
assert (L2 % 25,L17 % 25,L7 % 25) == (10,5,0)
assert data[5][2] % 25 == 5
alpha5,mod5 = unit_ratio((-L2) % 5**precision,L17,5,precision)
assert alpha5 % 5 == 3
tate_solutions = [(b,g) for b in range(1,5) for g in range(1,5)
                  if (b*data[5][2]-2*g*L7+8*L2) % 25 == 0]
assert tate_solutions == [(4,1),(4,2),(4,3),(4,4)]
assert alpha5*pow(4,-1,5) % 5 == 2
assert pow(2,2,5) == 4

# The simpler regular-coordinate quadratic form really has a unit solution.
L5_17 = log_unit(5,17,precision)
L7_17 = log_unit(7,17,precision)
ratio,root_mod = unit_ratio((-L5_17) % 17**precision,L7_17,17,precision)
assert ratio % 17 == 13
root = 8
for _ in range(precision+1):
    root = (root+ratio*pow(root,-1,root_mod))*pow(2,-1,root_mod) % root_mod
assert root % 17 == 8 and (root*root-ratio) % root_mod == 0
assert (L5_17+L7_17*root*root) % 17**precision == 0

# Exact dyadic branch excluded by the full mod-two unit classes.
assert 35 % 8 == 3
assert all((1-8*u) % 8 == 1 for u in (1,3,5,7))
assert {u*u % 8 for u in (1,3,5,7)} == {1}

print('A.84 exact arithmetic certificate: all checks passed.')
for p,w in ((17,-34),(5,35)):
    q,F,Lq,LF = data[p]
    print(f'p={p}, w={w}: q modulo p^9={q}; F modulo p^7={F}; log(q/p^2) modulo p^7={Lq}.')
    print(f'  log F modulo p^2={LF % (p*p)} equals w modulo p^2.')
print(f'alpha17 modulo17^6={alpha17}, residue14 is a nonsquare.')
print(f'alpha5 modulo5^6={alpha5}, residue3.')
print('At coefficient5, log(2),log(17),log(7) modulo25 are10,5,0; log(q5/25)=5 modulo25.')
print('All residue solutions of the coefficient5 Tate equation(beta5,gamma5):',tate_solutions)
print('Every solution has beta5=4; alpha5/beta5=2 modulo5 is a nonsquare.')
print(f'The regular-coordinate form at17 nevertheless has the unit solution(1,z) modulo17^7, z={root} modulo17^6, z=8 modulo17.')
print('The full mod-two unit class excludes the dyadic valuation3 branch.')
print('The proof uses full Tate extensions and one global multiplier; no finite calculation alone asserts a section.')

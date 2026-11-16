"""Arithmetic certificate for AP-D.12, rechecked for SECTIONS_OVER_Q.
The infinite ultrafilter argument is proved in the notes, not certified here.
"""
from math import factorial

def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5)+1))

def valuation(n, p):
    assert n
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v

def crt(congruences):
    x, m = 0, 1
    for b, n in congruences:
        x += m * ((b-x)*pow(m,-1,n) % n)
        m *= n
        x %= m
    return x

def local_residue(n):
    m=3**n
    residue=1
    r=1
    while factorial(r)<n:
        residue += 3**factorial(r)
        r += 1
    return residue%m

xs=[]
qs=[]
print('Certificate for the first 12 terms of the AP-D.12 sequence.')
for n in range(1,13):
    q=2
    while q==3 or not prime(q) or any(x%q==0 for x in xs):
        q+=1
    conditions=[(local_residue(n),3**n),(q,q*q)]+[(1,p) for p in qs]
    x=crt(conditions)
    assert x>=2
    assert x%(3**n)==local_residue(n)
    xs.append(x);qs.append(q)
    print(f'n={n:2d}, q_n={q}, x_n={x}')
print('Valuation matrix (rows q_i, columns x_j):')
for i,p in enumerate(qs):
    row=[valuation(x,p) for x in xs]
    assert row==[int(i==j) for j in range(len(xs))]
    print(' '.join(map(str,row)))
print('All 144 exact valuation checks and all 12 p-adic approximation congruences passed.')
print('The CRT modulus for x_n is 3^n q_n^2 times the product of previous q_i.')

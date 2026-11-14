#!/usr/bin/env python3
"""Independent normalized count for the quintic reflection test.

This verifier imports no code from the candidate experiment. It constructs
F4096 from a full multiplicative cycle, derives all elliptic additions and
Miller lines afresh, and evaluates local leading terms factor by factor.
It checks the Frobenius polynomial and its cyclotomic root-ratio obstruction.
It does not claim a point-section theorem for the resulting genus-two curve.
"""
from pathlib import Path
import json
import math
import sympy as sp

N = 4096
MODULUS = 0x1009

def raw_product(a, b):
    answer = 0
    while b:
        if b & 1:
            answer ^= a
        b >>= 1
        a <<= 1
        if a & N:
            a ^= MODULUS
    return answer

def raw_power(a, n):
    answer = 1
    while n:
        if n & 1:
            answer = raw_product(answer, a)
        a = raw_product(a, a)
        n >>= 1
    return answer

generator = next(g for g in range(2, N)
                 if all(raw_power(g, (N-1)//p) != 1 for p in (3, 5, 7, 13)))
exponents = [1]
for _ in range(N-2):
    exponents.append(raw_product(exponents[-1], generator))
assert len(set(exponents)) == N-1
assert raw_product(exponents[-1], generator) == 1
logarithms = {x:i for i,x in enumerate(exponents)}

def mul(a, b):
    return 0 if not a or not b else exponents[(logarithms[a]+logarithms[b])%(N-1)]

def power(a, n):
    if n == 0:
        return 1
    return 0 if a == 0 else exponents[(logarithms[a]*n)%(N-1)]

def div(a, b):
    assert b
    return mul(a, power(b, N-2))

r = 163
assert power(r, 6)^r^1 == 0
def embed(a):
    answer = 0
    for i in range(6):
        if a & (1 << i):
            answer ^= power(r, i)
    return answer

base_elements = {embed(a) for a in range(64)}
assert len(base_elements) == 64
assert all(power(a, 64) == a for a in base_elements)
aa, cc = embed(32), embed(14)
Q = (embed(38), embed(45))

def neg(P):
    return None if P is None else (P[0], P[0]^P[1])

def add(P, R):
    if P is None:
        return R
    if R is None:
        return P
    x,y = P
    u,v = R
    if x == u:
        if y != v or x == 0:
            return None
        slope = x^div(y,x)
    else:
        slope = div(y^v,x^u)
    xx = mul(slope,slope)^slope^aa^x^u
    yy = mul(slope,x^xx)^xx^y
    return xx, yy

def multiple(n,P):
    answer = None
    for _ in range(n):
        answer = add(answer,P)
    return answer

assert multiple(25,Q) is None and multiple(5,Q) is not None
A = neg(multiple(5,Q))
assert multiple(5,A) is None and A is not None
Q2, Q4 = multiple(2,Q), multiple(4,Q)

def line(P,R):
    x,y = P
    u,v = R
    slope = (x^div(y,x)) if P == R else div(y^v,x^u)
    return slope, y^mul(slope,x)

lines = (line(Q,Q),line(Q2,Q2),line(Q4,Q))
norm_line = line(Q,add(A,neg(Q)))

as_roots = {}
for z in range(N):
    as_roots.setdefault(mul(z,z)^z,[]).append(z)
points = [None,(0,power(cc,N//2))]
for x in range(1,N):
    rhs = x^aa^div(cc,mul(x,x))
    points.extend((x,mul(x,z)) for z in as_roots.get(rhs,[]))
assert len(set(points)) == len(points)
assert all(P is None or
           mul(P[1],P[1])^mul(P[0],P[1])^power(P[0],3)^mul(aa,power(P[0],2))^cc == 0
           for P in points)

def line_leading(L,P):
    x,y = P
    slope,constant = L
    first = y^mul(slope,x)^constant
    if first:
        return 0,first
    assert x
    coeffs = [y]
    for n in range(1,10):
        rhs = mul(x,x) if n == 1 else (x^aa) if n == 2 else 1 if n == 3 else 0
        rhs ^= coeffs[n-1]
        if n % 2 == 0:
            rhs ^= mul(coeffs[n//2],coeffs[n//2])
        yn = div(rhs,x)
        coeffs.append(yn)
        value = yn^slope if n == 1 else yn
        if value:
            return n,value
    raise AssertionError('No leading coefficient found')

def f_leading(P):
    data = [line_leading(L,P) for L in lines]
    valuation = 2*data[0][0]+data[1][0]+data[2][0]
    unit = mul(mul(power(data[0][1],2),data[1][1]),data[2][1])
    for other, exponent in ((Q2,2),(Q4,1)):
        value = P[0]^other[0]
        if value:
            unit = div(unit,power(value,exponent))
        else:
            valuation -= exponent
    return valuation,unit

def h(P):
    return div(P[1]^mul(norm_line[0],P[0])^norm_line[1],P[0]^A[0])

fifth_roots = {}
for z in range(N):
    fifth_roots.setdefault(power(z,5),[]).append(z)

count_T2 = 2
normalization = []
for P in points:
    if P is None or P == A:
        continue
    valuation,unit = f_leading(P)
    assert valuation == (5 if P == Q else 0)
    count_T2 += len(fifth_roots.get(unit,[]))
    if valuation or P[0] in (Q2[0],Q4[0]):
        normalization.append({'P':P,'valuation':valuation,'leading_unit':unit})

twisted_base = 0
twisted_total = 0
norm_equations = 0
for P in points:
    if P is None:
        continue
    frob = (power(P[0],64),power(P[1],64))
    if add(P,frob) != A:
        continue
    twisted_base += 1
    valuation,unit = f_leading(P)
    assert valuation == 0
    roots = fifth_roots.get(unit,[])
    for z in roots:
        assert power(z,65) == h(P)
        norm_equations += 1
    twisted_total += len(roots)

count_E1 = sum(P is None or all(a in base_elements for a in P) for P in points)
count_E2 = len(points)
assert twisted_base == 130-count_E1
count_T1 = count_E1  # fifth power is bijective on F64, including local units
assert (count_T1+twisted_total)%2 == 0
count_H1 = (count_T1+twisted_total)//2
twisted_T2 = 2*(N+1)-count_E2  # inversion on every five-point torsor has one fixed point
assert (count_T2+twisted_T2)%2 == 0
count_H2 = (count_T2+twisted_T2)//2
trace1, trace2 = 65-count_H1, N+1-count_H2
assert (trace1**2-trace2)%2 == 0
b = (trace1**2-trace2)//2
polynomial_coefficients = [1,-trace1,b,-64*trace1,64**2]

x,z = sp.symbols('x z')
P = sum(c*x**(4-i) for i,c in enumerate(polynomial_coefficients))
assert sp.Poly(P,x,modulus=7).is_irreducible
resultant = sp.Poly(sp.resultant(P,sp.expand(z**4*P.subs(x,x/z)),x),z)
residual = sp.div(resultant,sp.Poly((z-1)**4,z))[0]
assert sp.div(resultant,sp.Poly((z-1)**4,z))[1].is_zero
squarefree = sp.Poly(residual.sqf_part(),z).monic()
assert squarefree.degree() <= 8
# phi(n)<=8 forces every prime divisor <=7; the resulting finite list is exact.
orders = [1,2,3,4,5,6,7,8,9,10,12,14,15,16,18,20,24,30]
assert [n for n in range(1,211) if sp.totient(n)<=8] == orders
cyclotomic_checks = []
for n in orders:
    g = sp.gcd(squarefree,sp.Poly(sp.cyclotomic_poly(n,z),z))
    assert g.degree() == 0
    cyclotomic_checks.append({'order':n,'degree':int(sp.totient(n)),'gcd_degree':0})

result = {
    'status':'independent_exact_verification_passed',
    'field_modulus':MODULUS,'multiplicative_generator':generator,
    'multiplicative_cycle_length':len(set(exponents)),
    'base_generator':r,'Q':Q,'A':A,'miller_lines':lines,'norm_line':norm_line,
    'local_leading_terms':normalization,
    'counts':{'E64':count_E1,'E4096':count_E2,'T64':count_T1,
              'T4096':count_T2,'twisted_E64':twisted_base,
              'twisted_T64':twisted_total,'twisted_T4096':twisted_T2,
              'H64':count_H1,'H4096':count_H2},
    'twisted_norm_equations':norm_equations,
    'weil_polynomial':polynomial_coefficients,
    'ordinary':bool(b%2),'irreducible_mod_7':True,
    'root_ratio_squarefree_coefficients':[str(c) for c in squarefree.all_coeffs()],
    'cyclotomic_checks':cyclotomic_checks,
    'scope':'Checks the explicit genus-two quotient and geometric-simplicity certificate; no universal A1 conclusion.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

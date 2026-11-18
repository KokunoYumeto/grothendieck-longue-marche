#!/usr/bin/env python3
"""Exact truncated free-associative certificate for E.81.

No floating point arithmetic and no finite sample substitution is used.
Scalar variables (a,b,h,d,e) remain formal.  The degree cutoff is four.
The paper supplies the integral-lattice and continuous-cohomology arguments.
"""
from fractions import Fraction as F
from math import factorial, lcm

N = 4
Z = (0, 0, 0, 0, 0)
ONE = {((), Z): F(1)}

def clean(p): return {k: v for k, v in p.items() if v}
def add(*ps):
    r = {}
    for p in ps:
        for k, v in p.items(): r[k] = r.get(k, F(0)) + v
    return clean(r)
def scale(p, a): return clean({k: a*v for k, v in p.items()})
def mul(p, q):
    r = {}
    for (w, a), v in p.items():
        for (u, b), t in q.items():
            if len(w)+len(u) <= N:
                k = (w+u, tuple(x+y for x,y in zip(a,b)))
                r[k] = r.get(k, F(0)) + v*t
    return clean(r)
def exp(p):
    r = ONE.copy(); term = ONE
    for k in range(1, N+1):
        term = mul(term, p)
        r = add(r, scale(term, F(1, factorial(k))))
    return r
def log(p):
    u = add(p, scale(ONE, -1)); r = {}; term = ONE
    for k in range(1, N+1):
        term = mul(term, u)
        r = add(r, scale(term, F((-1)**(k+1), k)))
    return r
def scalar(p, i):
    r = {}
    for (w, a), v in p.items():
        a = list(a); a[i] += 1
        r[(w, tuple(a))] = v
    return r
def inverse(p): return exp(scale(log(p), -1))
def comm(p, q): return mul(mul(mul(p,q),inverse(p)),inverse(q))
def denom(p, degree, predicate=lambda a: True):
    return lcm(*(v.denominator for (w,a),v in p.items()
                 if len(w)==degree and predicate(a)))

X = {((0,),Z): F(1)}; Y = {((1,),Z): F(1)}
x = exp(X); y = exp(Y)
C = comm(x,y); D = comm(x,C); E = comm(y,C)
hall = [('C', C), ('D', D), ('E', E),
        ('[x,D]',comm(x,D)), ('[y,D]',comm(y,D)),
        ('[y,E]',comm(y,E))]
for name,g in hall:
    L = log(g)
    ds = [denom(L,i) for i in range(1,5)]
    print(f'log {name}: denominator lcms in degrees 1..4 = {ds}')
    if name=='C': assert ds[1]==1 and 2%ds[2]==0 and 12%ds[3]==0
    if name in ('D','E'): assert ds[2]==1 and 2%ds[3]==0
    if name not in ('C','D','E'): assert ds[3]==1

G = ONE
for P in [exp(scalar(Y,1)), exp(scalar(X,0)),
          exp(scalar(log(C),2)), exp(scalar(log(D),3)),
          exp(scalar(log(E),4))]: G = mul(G,P)
L = log(G)
print('Formal log(y^b x^a C^h D^d E^e), denominator lcms:',
      [denom(L,i) for i in range(1,5)])
assert 2%denom(L,2)==0 and 12%denom(L,3)==0
assert 24%denom(L,4)==0
linear = lambda a: sum(a)==1
nonlinear = lambda a: sum(a)>=2
assert 12%denom(L,4,lambda a: linear(a) and a[2])==0
assert 2%denom(L,4,lambda a: linear(a) and (a[3] or a[4]))==0
assert all(a[3]+a[4]<=1 for (w,a) in L if len(w)==4 and nonlinear(a))
print('Degree-four linear h terms have denominator dividing12;')
print('linear d/e terms have denominator dividing2;')
print('all nonlinear terms have denominator dividing24 and at most one d/e.')

BCH = log(mul(exp(X),exp(Y)))
print('Universal BCH denominator lcms in degrees1..4:',
      [denom(BCH,i) for i in range(1,5)])
assert all(D0%denom(BCH,i)==0 for i,D0 in enumerate([1,2,12,24],1))
assert log(exp(X))==X and log(exp(Y))==Y
assert log(mul(G,inverse(G)))=={}
print('PASS: all exact polynomial identities and denominator bounds for E.81.')

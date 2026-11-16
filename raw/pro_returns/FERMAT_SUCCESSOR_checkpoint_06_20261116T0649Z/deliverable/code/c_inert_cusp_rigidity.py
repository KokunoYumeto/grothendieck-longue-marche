#!/usr/bin/env python3
"""Exact finite inputs for the full-section cross-prime rigidity proof.

This is not a full-group lifting test. The cohomological proof is in
work/c_two_prime_cusp_colouring.md. Only standard-library arithmetic is used.
"""
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
C = ((1, -1), (0, -1))
R = ((0, -1), (1, -1))
T = ((1, -3), (3, -2))

def mv(A, v, mod=None):
    z = tuple(sum(A[i][j] * v[j] for j in range(2)) for i in range(2))
    return tuple(x % mod for x in z) if mod else z

def mm(A, B, mod):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % mod
                       for j in range(2)) for i in range(2))

def add(v, w, mod=3):
    return tuple((v[i] + w[i]) % mod for i in range(2))

def sub(v, w, mod=3):
    return tuple((v[i] - w[i]) % mod for i in range(2))

def scale(t, v, mod=3):
    return tuple(t*x % mod for x in v)

assert mv(R, (1, 0)) == (0, 1)
assert mv(C, (1, 0)) == (1, 0)
assert sub(mv(T, (1, 0)), (1, 0), 27) == (0, 3)
assert mm(C, C, 27) == ((1, 0), (0, 1))
assert mm(R, R, 27) == ((26, 1), (26, 0))

def prime(q):
    return q >= 2 and all(q % d for d in range(2, int(q**0.5)+1))

def fm(x, y, q):
    # zeta^2 = -1-zeta in F_q[zeta], irreducible for q=2 mod3.
    a,b=x; c,d=y
    return ((a*c-b*d) % q, (a*d+b*c-b*d) % q)

def fp(x, n, q):
    y=(1,0)
    while n:
        if n & 1: y=fm(y,x,q)
        x=fm(x,x,q); n//=2
    return y

def cubic_log(x, q):
    y=fp(x,(q*q-1)//3,q)
    roots=[(1,0),(0,1),((q-1)%q,(q-1)%q)]
    assert y in roots, (q,x,y)
    return roots.index(y)

prime_rows=[]
for q in range(2,1000):
    if not prime(q) or q%3 !=2: continue
    e=((q*q-1)//3)%3
    row=(cubic_log((0,1),q), cubic_log((1,q-1),q))
    assert row==(e,2*e%3)
    # Actual Frobenius rows at7: 2(a+b)=e, 2b=2e.
    matching=[(a,b) for a,b in product(range(3),repeat=2)
              if (2*(a+b)%3,2*b%3)==row]
    assert matching==[(e,e)]
    if q<200:
        cubes={pow(x,3,q) for x in range(q)}
        assert len(cubes)==q
        affine=sum(1 for x in range(q) for y in range(q)
                   if (x*x*x+y*y*y+1)%q==0)
        infinity=sum(1 for x in range(q) if (x*x*x+1)%q==0)
        assert affine+infinity==q+1
    if q%9 in (2,5):
        assert e!=0 and (q+1)%3==0 and (q+1)%9!=0
    else:
        assert q%9==8 and e==0
    prime_rows.append({"q":q,"e":e,"kummer_row":list(row),
                       "frattini_coordinates":[e,e]})

image_c_minus_one={sub(mv(C,v),v) for v in product(range(3),repeat=2)}
kernel_one_plus_c={v for v in product(range(3),repeat=2)
                   if add(v,mv(C,v))==(0,0)}
assert image_c_minus_one==kernel_one_plus_c

matrix_cases=0
cocycle_cases=0
for q in (2,5):
    e=((q*q-1)//3)%3
    for tweaks in product(range(3),repeat=4):
        F=tuple(tuple((C[i][j]+3*tweaks[2*i+j])%9 for j in range(2))
                for i in range(2))
        if mm(F,F,9)!=(((-q)%9,0),(0,(-q)%9)): continue
        if (F[0][0]*F[1][1]-F[0][1]*F[1][0])%9!=q: continue
        matrix_cases+=1
        # The literal Kummer cocycle of R0=e1/3 at rational Frobenius.
        kr=((F[0][0]-1)//3%3,F[1][0]//3%3)
        assert add(kr,mv(C,kr))==((-e)%3,0)
        assert kr not in image_c_minus_one
        for a in product(range(3),repeat=2):
            k=sum(a)%3
            square_value=scale(e,add(a,mv(C,a)))
            assert square_value==((-e*k)%3,0)
            for w in product(range(3),repeat=2):
                if add(w,mv(C,w))!=square_value: continue
                cocycle_cases+=1
                assert sub(w,scale(k,kr)) in image_c_minus_one

result={
    "status":"all exact finite inputs passed",
    "scope":"necessary compact consequence for actual full pro-three sections; no lifting assertion",
    "colour_coordinate":"k=(alpha(tau)_1+alpha(tau)_2) mod3",
    "covered_rational_primes":"q congruent to2 or5 modulo9",
    "inert_primes_checked_below1000":len(prime_rows),
    "all_compatible_frobenius_matrices_mod9_checked":matrix_cases,
    "all_compatible_mod3_cocycle_cases_checked":cocycle_cases,
    "kummer_rows":prime_rows,
}
(ROOT/'c_inert_cusp_rigidity.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
print('inert primes below1000:',len(prime_rows))
print('compatible Frobenius matrices modulo9:',matrix_cases)
print('compatible cocycle cases:',cocycle_cases)
print('common colour: k = a1+a2 modulo3')
print('No claim for split primes or inert primes congruent to8 modulo9.')

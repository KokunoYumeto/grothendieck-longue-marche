#!/usr/bin/env python3
"""Exact norm-zeta search for the mixed Kummer direction 3*17.

Complex cubic roots propose coefficients; only exact Z[zeta] arithmetic
certifies an output. A bounded search with no witness proves no exclusion.
"""
from pathlib import Path
import json
import numpy as np

D = 51
BOUND = 7
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(n,a): return n*a[0],n*a[1]
def mul(a,b):
    u,v=a; c,d=b
    return u*c-v*d,u*d+v*c-v*d
def cube(a): return mul(mul(a,a),a)
def norm(a,b,c):
    return add(add(cube(a),scale(D,cube(b))),
               add(scale(D*D,cube(c)),scale(-3*D,mul(mul(a,b),c))))
def complex_value(a): return a[0]+a[1]*np.exp(2j*np.pi/3)

coeff = [(i,j) for i in range(-BOUND,BOUND+1) for j in range(-BOUND,BOUND+1)]
bb = np.array([complex_value(b) for b in coeff])
BB,CC = np.meshgrid(bb,bb,indexing='ij')
B,C = BB.ravel(),CC.ravel()
witnesses = []
attempts = []
for k in range(6):
    target = (0,3**(3*k))
    pol = np.zeros((len(B),3,3),dtype=np.complex128)
    pol[:,1,0]=1; pol[:,2,1]=1
    pol[:,0,2]=-(D*B**3+D*D*C**3-complex_value(target))
    pol[:,1,2]=3*D*B*C
    roots = np.linalg.eigvals(pol)
    candidates = 0
    for index,rr in enumerate(roots):
        b=coeff[index//len(coeff)]; c=coeff[index%len(coeff)]
        for aa in rr:
            a1=int(round(2*aa.imag/np.sqrt(3)))
            a0=int(round(aa.real+a1/2))
            if abs(aa-complex_value((a0,a1)))>1e-5:
                continue
            candidates += 1
            if norm((a0,a1),b,c)==target:
                row={'denominator':3**k,'a':[a0,a1],'b':list(b),'c':list(c),
                     'norm_numerator':list(target),'identity_verified_exactly':True}
                if row not in witnesses:
                    witnesses.append(row)
    attempt={'denominator':3**k,'coefficient_bound':BOUND,
             'approximate_candidates':candidates,'cumulative_exact_witnesses':len(witnesses)}
    attempts.append(attempt)
    print(json.dumps(attempt),flush=True)
    if witnesses:
        break
out={'radicand':D,'attempts':attempts,'witnesses':witnesses,
     'status':'PASS_EXACT_WITNESS' if witnesses else 'NO_WITNESS_IN_BOUNDED_SEARCH'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
for row in witnesses[:12]:
    print(json.dumps(row),flush=True)
print(out['status'],flush=True)

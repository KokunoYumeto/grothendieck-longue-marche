#!/usr/bin/env python3
"""Exact algebra and finite examples for E192--E194.

The finite examples are not the all-finite-field proof.  That proof uses
the actual pro-ell geometric monodromy and Tate's exact sequence.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp

t = sp.symbols('t')

def invariants(a1, a2, a3, a4, a6):
    b2 = a1*a1+4*a2
    b4 = 2*a4+a1*a3
    b6 = a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4 = sp.expand(b2*b2-24*b4)
    delta = sp.expand(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)
    return tuple(map(sp.expand, (b2,b4,b6,b8,c4,delta)))

three = invariants(3,0,t,0,0)
two = invariants(0,t+1,0,t,0)
assert three == (9,3*t,t*t,0,81-72*t,sp.expand(27*t**3*(1-t)))
assert sp.factor(three[-1]) == -27*t**3*(t-1)
assert sp.factor(two[-1]) == 16*t*t*(t-1)**2
assert sp.expand(two[-2]-16*(t*t-t+1)) == 0

sl2 = [A for A in product(range(3), repeat=4)
       if (A[0]*A[3]-A[1]*A[2]) % 3 == 1]
stab = [A for A in sl2 if (A[0],A[2]) == (1,0)]
assert len(sl2) == 24
assert set(stab) == {(1,b,0,1) for b in range(3)}

def prime(p):
    return p >= 2 and all(p % d for d in range(2,sp.integer_nthroot(p,2)[0]+1))

def valuation(m, ell):
    v = 0
    while m % ell == 0:
        v += 1
        m //= ell
    return v

rows = []
for p in range(3,200):
    if not prime(p):
        continue
    for a in range(2,p):
        if p != 3:
            m = 1+sum((y*y+3*x*y+a*y-x**3) % p == 0
                      for x in range(p) for y in range(p))
            assert m % 3 == 0
            assert 1 <= m <= 2*p+1
            assert (p+1-m)**2 <= 4*p
            n = 1
            while 3**n <= 2*p+1:
                n += 1
            assert m % (3**n) != 0
            rows.append({'ell':3,'q':p,'t':a,'points':m,
                         'trace':p+1-m,'uniform_N':n,
                         'first_trace_N':valuation(m,3)+1})
        m = 1+sum((y*y-x*(x+1)*(x+a)) % p == 0
                  for x in range(p) for y in range(p))
        assert m % 4 == 0
        assert 1 <= m <= 2*p+1
        assert (p+1-m)**2 <= 4*p
        n = 1
        while 2**n <= 2*p+1:
            n += 1
        assert m % (2**n) != 0
        rows.append({'ell':2,'q':p,'t':a,'points':m,
                     'trace':p+1-m,'uniform_N':n,
                     'first_trace_N':valuation(m,2)+1})

# F4=F2[z]/(z²+z+1), encoded as the two binary coefficients.
def f4mul(a,b):
    a0,a1=a&1,a>>1
    b0,b1=b&1,b>>1
    return (a0*b0 ^ a1*b1) | ((a0*b1 ^ a1*b0 ^ a1*b1)<<1)

char_two_rows = []
for a in (2,3):
    m = 1+sum((f4mul(y,y) ^ f4mul(x,y) ^ f4mul(a,y)
               ^ f4mul(f4mul(x,x),x)) == 0
              for x in range(4) for y in range(4))
    assert m % 3 == 0 and 1 <= m <= 9
    char_two_rows.append({'q':4,'t_binary':a,'points':m,'trace':5-m})
    assert m % 27 != 0

result = {'three_invariants':list(map(str,three)),
          'two_invariants':list(map(str,two)),
          'SL2_F3_order':len(sl2),'fixed_vector_stabilizer':stab,
          'point_rows':rows,'characteristic_two_rows':char_two_rows,
          'scope':'Finite algebra/examples only; all-field proof is E192--E194.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact Weierstrass invariants for both families.')
print('PASS: SL2(F3) has order24 and the nonzero-vector stabilizer is C3.')
for ell in (2,3):
    selected=[r for r in rows if r['ell']==ell]
    print(f'PASS: ell={ell}, {len(selected)} smooth prime-field fibres; '
          f'point divisibility, elementary bound, and uniform trace detector checked; '
          f'largest observed first trace modulus exponent={max(r["first_trace_N"] for r in selected)}.')
print('PASS: characteristic-two F4 fibres:',char_two_rows)
print('Every cusp trace is q+1 by the proved Tate sequence; '
      'no finite census is used to infer the universal theorem.')

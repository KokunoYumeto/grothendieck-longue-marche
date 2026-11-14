#!/usr/bin/env python3
"""Exact arithmetic checks for the cyclic theta difference bound."""
from math import isqrt, gcd
from pathlib import Path
import json

def factors(n):
    p=2;out=[]
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out

def phi(n):
    a=n
    for p in factors(n):a=a//p*(p-1)
    return a

def orbit(n):
    out=[];v=1
    while v not in out:
        out.append(v);v=v*2%n
    assert v==1
    return out

def record(n):
    b=(1+isqrt(8*n-7))//2
    assert b*(b-1)<=2*(n-1)<(b+1)*b
    O=orbit(n);nu=len(O);ph=phi(n)
    assert ph%nu==0
    minus=n-1 in O
    hit_bound=b//2 if minus else b
    return {'n':n,'phi':ph,'doubling_order':nu,
      'primitive_orbit_count':ph//nu,'theta_packet_bound':b,
      'minus_one_in_doubling_subgroup':minus,
      'upper_bound_on_hit_primitive_orbits':hit_bound,
      'primitive_rank_lower_bound':max(0,ph-nu*hit_bound)}

examples=[record(127),record(257)]
assert examples[0]['primitive_rank_lower_bound']==14
assert examples[1]['primitive_rank_lower_bound']==80
assert factors(127)==[127] and factors(257)==[257]
rows=[record(n) for n in range(3,1002,2)]
out={'status':'PASS','examples':examples,
     'odd_orders_checked':len(rows),
     'positive_lower_bounds':[r for r in rows if r['primitive_rank_lower_bound']>0],
     'scope':'Exact arithmetic only. The geometric two-difference and primitive character bounds are proved in the candidate.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'examples':examples,
    'odd_orders_checked':len(rows),'positive_bounds':len(out['positive_lower_bounds'])},indent=2))

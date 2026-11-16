#!/usr/bin/env python3
"""Exact local coefficient tests for the unresolved A183 least weight.

P9=(Z/9)[T]/T^3 has the V-action chi*(1+T)^a*theta_chi.
Its reduction is the actual cubic-root permutation module with mu3
coefficients. This checks tame cocycle lift equations only. It does
not compute the global augmentation image or assert a value of o_2.
"""
from itertools import product
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
Id = [[int(i == j) for j in range(3)] for i in range(3)]
B = [[1,1,1],[0,1,2],[0,0,1]]
Bi = [[1,-1,1],[0,1,-2],[0,0,1]]

def mm(a,b,m=9):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))%m
             for j in range(len(b[0]))] for i in range(len(a))]

def mv(a,v,m=9):
    return tuple(sum(x*y for x,y in zip(row,v))%m for row in a)

def add(a,b,m=9):
    return [[(u+v)%m for u,v in zip(x,y)] for x,y in zip(a,b)]

def sub(a,b,m=9):
    return [[(u-v)%m for u,v in zip(x,y)] for x,y in zip(a,b)]

def power(a,n,m=9):
    r=Id
    while n:
        if n&1:r=mm(r,a,m)
        a=mm(a,a,m);n//=2
    return r

def geom(a,n,m=9):
    r=[[0]*3 for _ in range(3)]
    t=Id
    for _ in range(n):
        r=add(r,t,m);t=mm(t,a,m)
    return r

def action(chi,a,m=9):
    # Columns in (1,T,T^2), then actual root basis (1,X,X^2).
    z=[[chi,0,0],
       [chi*a,chi**2,0],
       [chi*a*(a-1)//2,
        chi*(a*chi+chi*(chi-1)//2),chi**3]]
    return mm(mm(Bi,z,m),B,m)

vectors=list(product(range(3),repeat=6))
records=[]
for label,Q,aI,aF in [('q11_quadratic',121,8,4),
                       ('q59_quadratic',3481,8,7),
                       ('two_linear',2,0,0),
                       ('two_quadratic',4,0,1)]:
    I=action(1,aI);F=action(Q,aF)
    assert mm(F,I)==mm(power(I,Q),F)
    Rleft=sub(F,geom(I,Q));Rright=sub(Id,power(I,Q))
    R=[Rleft[i]+Rright[i] for i in range(3)]
    images={}
    for v in vectors:images.setdefault(mv(R,v,3),v)
    rows=[];byclass={}
    for v in vectors:
        if mv(R,v,3)!=(0,0,0):continue
        rv=mv(R,v,9)
        assert all(t%3==0 for t in rv)
        defect=tuple((t//3)%3 for t in rv)
        correction=images.get(tuple((-t)%3 for t in defect))
        lifts=correction is not None
        ct,cf=v[:3],v[3:]
        if aI:
            # H is the actual stabilizer of root zero. Its tame
            # generators are tau^3 and tau*Frob.
            val=mv(geom(I,3,3),ct,3)[0]
            fh=(ct[0]+mv(I,cf,3)[0])%3
            e=(2*aF+1)//3
            assert (2*aF+1)%3==0
            angle=(fh-e*val)%3
            key=(val,angle)
        elif Q==2:
            assert ct[1]==ct[2]
            angle=mv(add(Id,F,3),cf,3)[1]
            key=(ct[0],ct[1],angle)
        else:
            assert len(set(ct))==1
            angle=mv(geom(F,3,3),cf,3)[0]
            key=(ct[0],angle)
        byclass.setdefault(key,set()).add(lifts)
        lift=None
        if lifts:
            lift=[a+3*b for a,b in zip(v,correction)]
            assert mv(R,lift,9)==(0,0,0)
        rows.append({'cocycle':v,'local_class':key,
                     'defect':defect,'lifts':lifts,'one_lift':lift})
    assert all(len(v)==1 for v in byclass.values())
    if aI:
        assert len(byclass)==9 and all(next(iter(v)) for v in byclass.values())
    elif Q==2:
        assert len(byclass)==27
        assert all(next(iter(v))==(key[1]==0) for key,v in byclass.items())
    else:
        assert len(byclass)==9 and all(next(iter(v)) for v in byclass.values())
        # Every lifted inertia vector has augmentation zero modulo9.
        for ct9 in product(range(9),repeat=3):
            if mv(Rleft,ct9,9)==(0,0,0):assert sum(ct9)%9==0
    print('PASS:',label,'cocycles',len(rows),'classes',len(byclass),
          'liftable classes',sum(next(iter(v)) for v in byclass.values()))
    records.append({'label':label,'Q':Q,'inertia_kummer':aI,
                    'frobenius_kummer':aF,'I':I,'F':F,'R':R,
                    'classes':[{'class':k,'lifts':next(iter(v))}
                               for k,v in sorted(byclass.items())],
                    'all_cocycle_checks':rows})

data={'coefficient_module':'P9=(Z/9)[T]/T^3 with the V action',
      'root_basis_change':B,'places':records,
      'scope':'Exact tame local Bockstein equations only; the global augmentation/norm-trivialization comparison is not evaluated.'}
(BASE/'two_inert_weight_two_local_bockstein_data.json').write_text(
    json.dumps(data,indent=2)+'\n')
print('PASS: actual semilinear actions and all local lift equations; no global least-weight assertion')

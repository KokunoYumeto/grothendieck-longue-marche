#!/usr/bin/env python3
"""Exact split-prime compact colour formula for B.42.

Only a necessary condition on a full pro-three section is computed here.
No section ramified at two primes is constructed by this program.
"""
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
R=((0,2),(1,2))
R2=((2,1),(2,0))
C=((1,2),(0,2))
a=(1,2)
e1=(1,0)

def mv(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(2))%3 for i in range(2))

def add(v,w):
    return tuple((v[i]+w[i])%3 for i in range(2))

def scale(t,v):
    return tuple(t*x%3 for x in v)

def prime(q):
    return q>=2 and all(q%d for d in range(2,int(q**0.5)+1))

cases=0
for u,v in product(range(3),repeat=2):
    s=(u+v)%3
    if not s: continue
    D=tuple(tuple((u*R[i][j]+v*R2[i][j])%3 for j in range(2)) for i in range(2))
    assert (D[0][0]*D[1][1]-D[0][1]*D[1][0])%3==s*s%3
    assert mv(D,a)==scale(s,a)
    ratio=(u-v)*pow(s,-1,3)%3
    i,j=2*s%3,2*v%3
    assert ratio==(1+j*pow(i,-1,3))%3
    for b,k in product(range(3),repeat=2):
        w=add(scale(b,a),(0,k))
        cocycle=add(scale(u,w),scale(v,mv(C,w)))
        point=add(scale(k,e1),scale(b*ratio,a))
        assert cocycle==mv(D,point)
        cases+=1

rows=[]
for q in range(2,1000):
    if not prime(q) or q%9 not in (4,7): continue
    roots=[z for z in range(2,q) if (z*z+z+1)%q==0]
    assert len(roots)==2
    local=[]
    for z in roots:
        mu=[1,z,z*z%q]
        i=mu.index(pow(z,(q-1)//3,q))
        j=mu.index(pow((1-z)%q,(q-1)//3,q))
        assert i!=0
        u,v=(2*(i-j))%3,2*j%3
        ratio=(1+j*pow(i,-1,3))%3
        assert ratio==(u-v)*pow((u+v)%3,-1,3)%3
        local.append({"zeta_root":z,"zeta_kummer":i,"lambda_kummer":j,
                      "frattini_coordinates":[u,v],"P_colour_coefficient":ratio})
    assert (local[0]['P_colour_coefficient']+local[1]['P_colour_coefficient'])%3==0
    count=None
    if q<200:
        count=sum((x*x*x+y*y*y+1)%q==0 for x in range(q) for y in range(q))
        count+=sum((x*x*x+1)%q==0 for x in range(q))
        assert count%9==0 and count%27!=0
    rows.append({"q":q,"point_count_if_below200":count,"places":local})

seven=next(x for x in rows if x['q']==7)
sixtyone=next(x for x in rows if x['q']==61)
assert seven['places'][0]['P_colour_coefficient']==1
assert all(x['P_colour_coefficient']==0 for x in sixtyone['places'])

result={"status":"all split compact colour checks passed",
        "scope":"necessary compact condition only; no two-prime ramified section constructed",
        "formula":"centre-O = k R0 + (b mod3) ((u-v)/(u+v)) P; P=(1,2)/3",
        "residue_formula":"(u-v)/(u+v) = 1 + kappa(lambda)(F)/kappa(zeta)(F) modulo3",
        "matrix_and_cocycle_cases":cases,
        "split_primes_checked_below1000":len(rows),
        "conditional_pair":{"q7":"P for beta and the root zeta=2",
                            "q61":"O for beta at either root",
                            "missing":"an actual full section with this compact class and nonzero inertia at both primes"},
        "prime_rows":rows}
(ROOT/'c_split_compact_colours.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
print('matrix and cocycle cases:',cases)
print('split primes below1000:',len(rows))
print('beta compact label at7 (zeta=2): P=(1,2)/3; at61: O')
print('This is a conditional colour constraint, not a two-prime section construction.')

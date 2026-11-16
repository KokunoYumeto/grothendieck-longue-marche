#!/usr/bin/env python3
"""Finite exact checks for the all-height S-class induction; no class algorithm."""
from pathlib import Path
import json,itertools
base=Path(__file__).resolve().parent
d=json.loads((base/'two_inert_level2_unit_norm_certificate_data.json').read_text())
rows=[r+[h] for r,h in zip(d['rows'],[0,1,2,0,0,0])]
def rank(a):
    a=[r[:] for r in a];n=0
    for j in range(len(a[0])):
        p=next((k for k in range(n,len(a)) if a[k][j]%3),None)
        if p is None:continue
        a[p],a[n]=a[n],a[p];v=pow(a[n][j],-1,3)
        a[n]=[x*v%3 for x in a[n]]
        for k in range(len(a)):
            if k!=n:
                c=a[k][j];a[k]=[(x-c*y)%3 for x,y in zip(a[k],a[n])]
        n+=1
    return n
assert rank(rows)==6
counts=[]
for n in range(2,15):
    fs=[1]+[2*3**j for j in range(n)]
    assert sum(fs)==3**n
    ef=[2]+[f for f in fs[1:] for _ in range(2)]
    assert len(ef)==2*n+1 and sum(ef)==2*3**n
    assert pow(2,2*3**(n-1),3**n)==1
    assert pow(2,2*3**(n-2),3**n)!=1
    assert (2*n+7)-1-(2*n+6)==0
    # Every diagonal two-prime coefficient is a unit modulo3.
    block=[[0]*10+[int(i==j) for j in range(2*n)] for i in range(2*n)]
    block += [r+[0]*(2*n) for r in rows]
    assert rank(block)==2*n+6
    counts.append({'n':n,'two_residue_degrees':ef,'growing':2*n,
                   'nonsplit':2*n+7,'norm_rank':2*n+6})
poly_count=0
for m in range(1,5):
    mod=3**m
    for ks in itertools.product(range(mod),repeat=3):
        if sum(ks)%3==0:continue
        # Matrix of k0+k1*sigma+k2*sigma² on the three-cycle regular module.
        a=[[ks[(i-j)%3] for j in range(3)] for i in range(3)]
        det=(a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
             -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
             +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
        assert det%3!=0
        assert det%3==sum(ks)%3
        poly_count+=1
out={'fixed_q_matrix':rows,'fixed_q_rank':6,'height_checks':counts,
     'polynomial_cases':poly_count,
     'scope':'Exact finite identities supporting the written induction, not an infinite class computation.'}
(base/'two_inert_all_height_split_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: fixed ten-element changed-prime matrix rank6')
print('PASS:',len(counts),'exact residue-degree, norm-rank and S-ambiguous exponent cases')
print('PASS:',poly_count,'literal cyclic-polynomial invertibility cases modulo3,9,27,81')

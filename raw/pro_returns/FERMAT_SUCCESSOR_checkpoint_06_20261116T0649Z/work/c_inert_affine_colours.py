#!/usr/bin/env python3
"""Exact affine-image certificate for the stronger inert colour theorem.

Enumerates the entire actual compact affine image mod81 (118098 elements),
checks its translation kernel and all inert elements of determinant valuation
at most3, and records the threshold-four Chebotarev conjugacy-class witness.
No geometric ramification or nonabelian local geometry is inferred.
"""
from collections import deque, Counter
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

def cm_mul(x,y,m):
    a,b=x;c,d=y
    return ((a*c-b*d)%m,(a*d+b*c-b*d)%m)

def bar(x,m):
    a,b=x
    return ((a-b)%m,(-b)%m)

def matrix(u,v,e,m):
    # (u+vR) C^e, R=[[0,-1],[1,-1]], C=[[1,-1],[0,-1]].
    A=((u%m,(-v)%m),(v%m,(u-v)%m))
    if not e:return A
    return ((A[0][0],(-A[0][0]-A[0][1])%m),
            (A[1][0],(-A[1][0]-A[1][1])%m))

def mul(x,y,m):
    z0,z1,u,v,e=x;w0,w1,r,s,f=y
    A=matrix(u,v,e,m)
    z=((z0+A[0][0]*w0+A[0][1]*w1)%m,
       (z1+A[1][0]*w0+A[1][1]*w1)%m)
    if e:r,s=bar((r,s),m)
    a,b=cm_mul((u,v),(r,s),m)
    return (z[0],z[1],a,b,e^f)

def vp3(n):
    if not n:return 100000
    k=0
    while n%3==0:n//=3;k+=1
    return k

def exhaustive(n):
    m=3**n
    identity=(0,0,1,0,0)
    A=(1,2,1,3,0)
    c=(0,0,1,0,1)
    found={identity}; queue=deque([identity])
    while queue:
        x=queue.popleft()
        for g in (A,c):
            y=mul(x,g,m)
            if y not in found:found.add(y);queue.append(y)
    kernel={(z0,z1) for z0,z1,u,v,e in found if (u,v,e)==(1,0,0)}
    claimed={((3*x+27*y)%m,6*x%m) for x in range(m) for y in range(m)}
    assert kernel==claimed
    fixed={(x,y) for x,y in kernel if y==0}
    assert fixed=={(27*z%m,0) for z in range(m)}
    counts=Counter()
    for z0,z1,u,v,e in found:
        if e!=1:continue
        F=matrix(u,v,e,m)
        d00=F[0][0]-1;d01=F[0][1]
        d10=F[1][0];d11=F[1][1]-1
        det=(d00*d11-d01*d10)%m
        valuation=min(vp3(det),n)
        counts[valuation]+=1
        if valuation<=3 and valuation<n:
            # D^{-1}z integral iff adj(D)z is divisible by3^v(detD).
            modulus=3**valuation
            assert (d11*z0-d01*z1)%modulus==0
            assert (-d10*z0+d00*z1)%modulus==0
    return {"modulus":m,"group_order":len(found),
            "translation_kernel_order":len(kernel),
            "c_fixed_translation_kernel_order":len(fixed),
            "inert_elements_by_v3_det_F_minus_1":dict(sorted(counts.items()))}

small=exhaustive(3)
full=exhaustive(4)
assert small['group_order']==2*3**6
assert full['group_order']==2*3**10
assert full['translation_kernel_order']==3**4
assert full['c_fixed_translation_kernel_order']==3

t=7**27
assert vp3(t-1)==4
m=243
q=(-t*t)%m
F=matrix(t,0,1,m)
kappa=((t-1)//3)%m
z=(13*((t-1)//3)*pow(4,-1,m))%m
assert q==161 and t%m==163 and z==kappa==54
assert vp3((q+1)%m)==4
# Full exact rational formula has difference (F-1)*(3e1/4).
assert (3*(t-1)*pow(4,-1,m))%m==0
# Translation (t-1)/3 belongs to the exact c-fixed kernel27Z3 e1.
assert ((t-1)//3)%27==0

result={
 "status":"all exact affine checks passed",
 "scope":"compact necessary conditions; no two-prime full-section counterexample",
 "beta_tau":[1,2],
 "kernel_basis_columns":[[3,6],[27,0]],
 "kernel_c_fixed":"27 Z3 e1",
 "fixed_scalar_lift":"(3(t-1)e1/4,tI)",
 "local_beta_divisibility":27,
 "common_colour_range":"inert q with v3(q+1)<=3+v3(b) for alpha=b beta+k kappa(R)",
 "enumerations":[small,full],
 "threshold_four_witness":{
   "t_definition":"7^27","t_mod243":t%m,"q_mod243":q,
   "affine_translation_mod243":[z,0],"frobenius_matrix_mod243":F,
   "kummer_R_mod243":[kappa,0],"v3_q_plus_one":4,
   "consequence":"positive-density Chebotarev set has beta_local=kappa(R), not guaranteed ramification"},
}
(ROOT/'c_inert_affine_colours.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status'])
for row in result['enumerations']:print(json.dumps(row,sort_keys=True))
print('Exact c-fixed translation kernel:27 Z3 e1')
print('All inert elements of e<=3 give zero local beta class.')
print('Threshold4 witness mod243: translation(54,0), matrix',F,'q=161 mod243.')
print('This witnesses compact sharpness only; no full nonabelian ramification is asserted.')

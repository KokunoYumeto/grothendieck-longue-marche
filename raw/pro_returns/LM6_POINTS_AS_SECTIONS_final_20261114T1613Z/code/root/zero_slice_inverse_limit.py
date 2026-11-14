#!/usr/bin/env python3
"""Integral detector and uniform matrix bound for the zero-abelian cubic slice.

The arithmetic eta identity is proved from actual path cocycles in E.36.
This certificate checks the integral equivariant detector and all 330
Smith pivots of the good-Frobenius matrix used in the Chebotarev construction.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
import numpy as np

here=Path(__file__).parent
data=json.loads((here/'class_three_fibre_output.json').read_text())
FV=np.array(data['A_tau'],dtype=object)
CV=np.array(data['C_V'],dtype=object)
n=10
basis=[(i,j,k) for j in range(n) for i in range(j+1,n) for k in range(j,n)]
idx={x:i for i,x in enumerate(basis)}
def hall(i,j,k):
    if i==j:return {}
    if i<j:return {t:-c for t,c in hall(j,i,k).items()}
    if k>=j:return {(i,j,k):1}
    return {(i,k,j):1,(j,k,i):-1}
def lie3(B):
    out=np.zeros((330,330),dtype=object)
    supports=[[(i,int(B[i,j])) for i in range(n) if B[i,j]] for j in range(n)]
    for col,(i,j,k) in enumerate(basis):
        for (a,aa),(b,bb),(c,cc) in product(supports[i],supports[j],supports[k]):
            for t,z in hall(a,b,c).items():out[idx[t],col]+=aa*bb*cc*z
    return out
T=lie3(FV);J=lie3(CV)
ell=[0,2,0,0,0,3,0,0,0,0]
def det(i,j):return int(i==0 and j==1)-int(i==1 and j==0)
row=np.array([[ell[i]*det(j,k)-ell[j]*det(i,k)-2*ell[k]*det(i,j)
               for i,j,k in basis]],dtype=object)
assert np.any(row)
assert np.array_equal(row@T,49*row)
assert np.array_equal(row@J,row)
assert all(int(x)%3==0 for x in row.flat)
primitive=row//3
assert np.array_equal(primitive@T,49*primitive)
assert np.array_equal(primitive@J,primitive)
assert np.array_equal(FV@(CV@FV@CV),(CV@FV@CV)@FV)
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=np.array([(v,-u) for u,v in coords],dtype=object)
u=np.array([3,0]+list(U[:,0]),dtype=object)
v=np.array([0,3]+list(U[:,1]),dtype=object)
assert sum(ell[i]*u[i] for i in range(10))==sum(ell[i]*v[i] for i in range(10))==0
# Phi([z,[u,v]])=2 det(pu,pv) ell(z)=18 ell(z).
for k in range(10):
    vec=np.zeros((330,1),dtype=object)
    for i,j in product(range(10),repeat=2):
        # [e_k,[u,v]] = -[[u,v],e_k].
        for t,z in hall(i,j,k).items():vec[idx[t],0]-=int(u[i]*v[j])*z
    assert int((row@vec)[0,0])==18*ell[k]

precision=12;modulus=3**precision
FV3=FV@FV@FV
T3=lie3(FV3)
inv343=pow(343,-1,modulus)
M=[[((int(T3[i,j])*inv343)-(i==j))%modulus for j in range(330)]
   for i in range(330)]
assert all(x%3==0 for rr in M for x in rr)
def val(x):
    if not x:return precision
    k=0
    while x%3==0:x//=3;k+=1
    return k
values=[]
for k in range(330):
    best=(precision,None,None)
    for i in range(k,330):
        for j in range(k,330):
            q=val(M[i][j])
            if q<best[0]:best=(q,i,j)
    q,i,j=best
    if i is None:break
    M[k],M[i]=M[i],M[k]
    for rr in M:rr[k],rr[j]=rr[j],rr[k]
    pp=3**q;inverse=pow(M[k][k]//pp,-1,modulus//pp)
    for i in range(k+1,330):
        assert M[i][k]%pp==0
        a=(M[i][k]//pp*inverse)%(modulus//pp)
        if a:M[i]=[(x-a*y)%modulus for x,y in zip(M[i],M[k])]
    values.append(q)
assert len(values)==330

# Independent determinant valuation from the exact CM eigenvalue pairs.
def vp(x):
    x=abs(x);assert x
    z=0
    while x%3==0:x//=3;z+=1
    return z
trace=[2,-1]
for i in range(2,7):trace.append(-trace[-1]-7*trace[-2])
contributions=[
 ('H3',1,vp(7**3-trace[3]+1)),
 ('H2W_CM_squares',8,vp(7**6-trace[6]+1)),
 ('H2W_mixed',16,vp(7**3-1)),
 ('HW2',64,vp(7**9-7**3*trace[3]+1)),
 ('W3',168,vp(7**6-1))]
detval=sum(m*k for _,m,k in contributions)
assert sum(values)==detval
C=max(values)
assert C==6
zeta9=4
assert pow(zeta9,9,19)==1 and pow(zeta9,3,19)!=1
residue=pow(3,2,19)
kummer19=next(i for i in range(9) if pow(zeta9,i,19)==residue)
assert kummer19==4 and (6*kummer19)%9==6
target_rows=[]
for nn in range(1,7):
    mm=nn+8;power=3**(nn+1)
    chi=pow(7,power,6*3**mm)
    kap=(-12+(chi-1)//6)%(3**mm)
    assert vp(chi-1)==nn+2 and vp(kap)==1
    target_rows.append({'n':nn,'precision':mm,'chi_mod_3m':chi%(3**mm),
                        'kappa_mod_3m':kap,'chi_minus_one_valuation':nn+2,
                        'kappa_valuation':1,'beta_coefficient_exponent':nn+C,
                        'primitive_detected_correction_valuation':C})
out={
 'coefficient_module':'A(-1)=Lie3(V)(-1)',
 'ell_f_on_V':ell,
 'integral_detector_nonzero_entries':[
   {'hall_word':list(basis[j]),'coefficient':int(row[0,j])}
   for j in range(330) if row[0,j]],
 'detector_equivariance':'row*T=49row, row*J=row; after twist target Z3(1)',
 'detector_on_bracket':'Phi([z,w])=18 ell_f(z)',
 'primitive_detector_nonzero_entries':[
   {'hall_word':list(basis[j]),'coefficient':int(primitive[0,j])}
   for j in range(330) if primitive[0,j]],
 'primitive_actual_eta_image':'6 kappa3(3), from E.36 and eta(c)=0',
 'prime19_finite_witness':{'zeta9_residue':zeta9,'3_squared_mod19':residue,
   'kappa3_of3_mod9':kummer19,'obstruction_mod9':6*kummer19%9,
   '3_cubic_residue_test':pow(3,6,19)},
 'normalized_actual_eta_image':'18 kappa3(3), from E.36 and eta(c)=0',
 'matrix':'D=(7^(-1) Lie3(A_tau))^3-I',
 'matrix_congruent_zero_mod3':True,
 'dimension':330,'rank':330,
 'Smith_3_valuations':dict(sorted(Counter(values).items())),
 'maximum_Smith_valuation_C':C,
 'determinant_valuation':detval,
 'independent_eigenvalue_contributions':contributions,
 'precision':precision,
 'uniform_bound':'For D_n=(I+D)^(3^n)-I, 3^(n+C) D_n^(-1) is integral',
 'Chebotarev_target':'g_n=[tau,tau_prime] tau^(3^(n+1)), n>=1',
 'target_chi_minus_one_valuation':'n+2',
 'target_kappa3_valuation':1,
 'beta_coefficient_exponent':'n+C',
 'primitive_detected_correction_valuation':C,
 'finite_arithmetic_target_rows':target_rows,
 'prime_values_enumerated':False,
 'checks_passed':True
}
(here/'zero_slice_inverse_limit_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

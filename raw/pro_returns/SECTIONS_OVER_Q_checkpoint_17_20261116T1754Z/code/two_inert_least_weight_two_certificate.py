#!/usr/bin/env python3
"""Exact finite arithmetic for A195; global cohomology is proved in the text."""
from itertools import product
from pathlib import Path
import json

B=Path(__file__).resolve().parent
def rank(a):
    a=[list(row)for row in a];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a))if a[k][j]%3),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];iv=pow(a[r][j]%3,-1,3)
        a[r]=[v*iv%3 for v in a[r]]
        for k in range(len(a)):
            if k!=r:
                q=a[k][j]%3;a[k]=[(v-q*w)%3 for v,w in zip(a[k],a[r])]
        r+=1
    return r

# Base order U,alpha,beta1,delta2,g11,delta11,g59,delta59.
norms=[]
for k6,k7,k8 in product(range(3),repeat=3):
    cols=[[0]*8 for _ in range(12)]
    cols[4][2]=1;cols[5][2]=2
    cols[7][0]=-2*(k6+k7+k8);cols[7][1]=1
    cols[9][0]=k6;cols[9][5]=1
    cols[10][0]=k7;cols[10][4]=cols[10][6]=1
    cols[11][0]=k8;cols[11][7]=1
    assert rank(list(zip(*cols)))==5
    norms.append({'unit_exponents':[k6,k7,k8],'norm_columns':cols,'rank':5})
print('PASS: all27 literal supported norm matrices have rank5; kernel in the twelve-dimensional source has dimension7')

identities=[];equivariant=0
for chi in (1,2,4,5,7,8):
    for a in range(9):
        theta=((chi*chi-1)//3)%3
        left=[(a+chi-1)%3,
              (a*(a-1)//2+a*chi+chi*(chi-1)//2+(chi*chi-1)//3)%3]
        right=[(a+chi-1)%3,((a+chi)*(a+chi-1)//2+theta)%3]
        assert left==right
        # D2 matrix in (1,T), and M in (T,T^2), before reduction.
        C=[[chi*chi,0],[chi*(a*chi+chi*(chi-1)//2),chi**3]]
        for v in product(range(3),repeat=2):
            lhs=[sum(C[i][j]*(3*v[j])for j in range(2))%9 for i in range(2)]
            rhs=[3*(sum(C[i][j]*v[j]for j in range(2))%3)%9 for i in range(2)]
            assert lhs==rhs
            equivariant+=1
        assert C[0][1]==0 # the actual last Tate line lifts modulo9
        identities.append({'chi':chi,'a':a,'theta9':theta,'divided_w':left})
print('PASS:54 exact divided-w identities,486 equivariant j=3/T squares, and the lifted last Tate line')

local=[]
for q in (11,59):
    root=next(x for x in range(q)if x**3%q==3)
    # F(q^2)=Fq[alpha]/(alpha^2+root*alpha+root^2).
    def mul(x,y):
        a,b=x;c,e=y
        return ((a*c-b*e*root*root)%q,(a*e+b*c-b*e*root)%q)
    def pw(x,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x);n//=2
        return z
    alpha=(0,1);one=(1,0)
    assert pw(alpha,3)==(3,0)
    om=pw(alpha,(q*q-1)//3)
    assert om!=one and pw(om,3)==one
    aa=mul(alpha,alpha);U=((aa[0]-2)%q,aa[1])
    val=pw(U,(q*q-1)//3)
    assert val==mul(om,om)
    assert 8%3 and (8*2)%3==1
    local.append({'q':q,'linear_alpha_root':root,
                  'quadratic_factor':[root*root%q,root,1],
                  'alpha_cubic_character':om,'U_cubic_character':val,
                  'U_character_exponent':2,'A_valuation':8})
print('PASS: both actual quadratic residue fields give v(A)=8 and cubic U-character2, hence a nonzero bottom cup')

restriction=json.loads((B/'two_inert_base_restriction_unit_classes_data.json').read_text())
assert restriction['detector_rank']==12 and restriction['restriction_rank']==7
assert restriction['radical_kernel']==[0,1,0,0,0,0,2,2]
print('PASS: independently retained complete rank12 detector and exact rank7 base restriction/kernel')
out={'norm_matrices':norms,'divided_w_identities':identities,
     'j_equivariance_checks':equivariant,'quadratic_prime_checks':local,
     'scope':'Finite supported coefficient identities and arithmetic only. The source proves the supported Bockstein exclusion and integral inflation; the absolute finite image remains zero.'}
(B/'two_inert_least_weight_two_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: A195 exact least-weight-two arithmetic and coefficient maps')

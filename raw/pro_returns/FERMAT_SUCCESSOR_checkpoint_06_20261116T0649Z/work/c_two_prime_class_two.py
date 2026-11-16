#!/usr/bin/env python3
"""Exact B24 denominator certificate for the split7/61 class-two test.

This does not construct a full pro-three section or prove actual local
cusp-packet matching. It verifies the genuine global class-two lifting
criterion for an abelian family with nine-divisible peripheral inertia.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as sp

U=sp.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
R=sp.Matrix([[0,-1],[1,-1]])
wpairs=list(combinations(range(8),2))
pairs=list(combinations(range(10),2))
pivot=wpairs.index((0,2))

def wedge(v,w):
    return sp.Matrix([v[i]*w[j]-v[j]*w[i] for i,j in wpairs])

def wedge_matrix(M):
    return sp.Matrix([[M[a,i]*M[b,j]-M[a,j]*M[b,i]
                       for i,j in pairs] for a,b in pairs])

def v3(r):
    if not r:return 100
    a,b=sp.fraction(r); n=0
    while a%3==0:a//=3;n+=1
    while b%3==0:b//=3;n-=1
    return n

records=[]
for q,A,name in [(7,sp.eye(2)+3*R,'7, zeta=2'),
                 (7,sp.eye(2)+3*R**2,'7, zeta=4'),
                 (61,-5*sp.eye(2)-9*R,'61, zeta=13'),
                 (61,4*sp.eye(2)+9*R,'61, zeta=47')]:
    assert A.det()==q and A.trace()==-1
    V=A.row_join(sp.zeros(2,8)).col_join((U*(A-q*sp.eye(2))/3).row_join(q*sp.eye(8)))
    assert all(x.q==1 for x in V)
    L=wedge_matrix(V)/q-sp.eye(45)
    corrections=[]
    for j in range(44):
        src=sp.zeros(44,1);src[j]=1
        X=sp.Matrix(2,8,list(src[:16]));Y=sp.Matrix(src[16:])
        Z=(A-sp.eye(2)).inv()*X
        X1,X2=X.row(0).T,X.row(1).T
        Z1,Z2=Z.row(0).T,Z.row(1).T
        Ys=(Y-(wedge(U[:,0],X1)+wedge(U[:,1],X2))/3)/(q-1)
        Ys+=(wedge(U[:,0],Z1)+wedge(U[:,1],Z2))/3
        z=Ys[pivot]
        C=sp.Matrix([9*z]).col_join(-Z1+3*z*U[:,1]).col_join(-Z2-3*z*U[:,0])
        C=C.col_join(-Ys+z*wedge(U[:,0],U[:,1]))
        assert C[17+pivot]==0
        D=sp.Matrix([0]).col_join(src)
        assert L*C==-D
        corrections.append(C)
    H=sp.Matrix.hstack(*corrections)
    minimum=min(v3(x) for x in H)
    assert minimum==-2
    assert all(v3(9*x)>=0 for x in H)
    records.append({'place':name,'Frobenius_compact':A.tolist(),
                    'rank':44,'minimum_entry_valuation':minimum,
                    'nine_times_operator_integral_at_three':True,
                    'exact_inverse_identity':'(q^{-1} Lambda2(F)-I) H = -inclusion',
                    'denominators':sorted({int(sp.denom(x)) for x in H if x})})

result={'status':'all exact class-two denominator identities passed',
        'abelian_family':'alpha=alpha0+9(corestr_K^Q(kappa(2-zeta)e_C2)+kappa(61)e_O)',
        'compact_class':'beta',
        'ramification_directions':'9e_C2 at7 and9e_O at61',
        'conclusion':'the actual B24 global class-two lifting criterion holds',
        'not_concluded':'actual local cusp-packet matching; a class-three lift; a full pro-three section',
        'records':records}
Path('work/c_two_prime_class_two.json').write_text(json.dumps(result,indent=2,default=str)+'\n')
print(json.dumps(result,indent=2,default=str))

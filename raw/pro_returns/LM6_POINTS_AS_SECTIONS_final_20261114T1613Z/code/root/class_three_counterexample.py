#!/usr/bin/env python3
"""Recompute the finite prime-19 obstruction and the full class-two lifts.

The older return's programs for this calculation were not supplied.
This program constructs every matrix directly from the stated maps.
"""
from collections import Counter
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json
import sympy as s

coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(2,1),(1,2)]
U=s.Matrix([(v,-u) for u,v in coords]);R=s.Matrix([[0,-1],[1,-1]])
wedges=list(combinations(range(10),2))
def degree_one(a,b,q):
    E=a*s.eye(2)+b*R
    A=s.zeros(10);A[:2,:2]=E;A[2:,:2]=U*(E-q*s.eye(2))/3;A[2:,2:]=q*s.eye(8)
    assert all(x.q==1 for x in A)
    return A
def smithvals(M,precision=8):
    n=len(M);mod=3**precision;M=[[int(x)%mod for x in row] for row in M]
    def val(x):
        if x==0:return precision
        v=0
        while x%3==0:x//=3;v+=1
        return v
    vals=[]
    for k in range(n):
        best=(precision,None,None)
        for i in range(k,n):
            for j in range(k,n):
                v=val(M[i][j])
                if v<best[0]:best=(v,i,j)
                if v==0:break
            if best[0]==0:break
        v,i,j=best;assert i is not None
        M[k],M[i]=M[i],M[k]
        for row in M:row[k],row[j]=row[j],row[k]
        pp=3**v;inverse=pow(M[k][k]//pp,-1,mod//pp)
        for i in range(k+1,n):
            assert M[i][k]%pp==0
            c=(M[i][k]//pp*inverse)%(mod//pp)
            if c:M[i]=[(x-c*y)%mod for x,y in zip(M[i],M[k])]
        vals.append(v)
    return dict(sorted(Counter(vals).items()))
counts=[];matrices=[]
for a,b in [(-2,3),(-5,-3)]:
    A=degree_one(a,b,19)
    B=s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k] for k,l in wedges] for i,j in wedges])-19*s.eye(45)
    M=B.extract([i for i,p in enumerate(wedges) if p!=(0,1)],[i for i,p in enumerate(wedges) if p!=(2,4)])
    count=smithvals(M.tolist());assert count=={0:8,1:6,2:18,3:12}
    assert sum(int(k)*v for k,v in count.items())==78
    counts.append(count);matrices.append([[int(x) for x in row] for row in M.tolist()])

u=s.Symbol('u');T=1+u
def trunc(x):return s.Poly(s.expand(x),u).as_dict()
K=s.Matrix([[s.expand(T**3*(T**19-1)**j-u**j).coeff(u,i) for j in range(1,5)] for i in range(1,5)])
b=s.Matrix([-s.expand(81*(T**3-1)).coeff(u,i) for i in range(1,5)])
expected=s.Matrix([[18,0,0,0],[228,360,0,0],[1539,7581,6858,0],[7315,86640,205770,130320]])
assert K==expected
row=s.Matrix([[1,660,558,162]])
assert all(int(x)%729==0 for x in row*K)
assert int((row*b)[0])%729==486
delta=T**3-1
g1=s.Matrix([int(s.expand(3*delta**3).coeff(u,i))%729 for i in range(1,5)])
g2=s.Matrix([int(s.expand(u*delta**3).coeff(u,i))%729 for i in range(1,5)])
assert list(g1)==[0,0,81,243] and list(g2)==[0,0,0,27]
assert int((row*g1)[0])%729==0 and int((row*g2)[0])%729==0
elements={tuple(int(x)%729 for x in a*g1+b0*g2) for a in range(9) for b0 in range(27)}
assert len(elements)==3**5
g3=tuple(int(s.expand(delta**2*u).coeff(u,i))%729 for i in range(1,5))
assert g3==(0,0,9,18) and g3 not in elements
assert all(int(s.binomial(2187,k))%729==0 for k in range(1,5))
coefficient=Fraction(81)
for j in range(4):coefficient*=Fraction(-1,6)-j;coefficient/=j+1
assert coefficient.denominator%3==0 and coefficient.denominator%9!=0
result={'class_two_Smith_counts_at_two_primes_over19':counts,'class_two_matrices':matrices,
 'local_equation_matrix':K.tolist(),'rhs':list(b),'annihilating_row':list(row),
 'annihilator_rhs_mod729':486,'gamma4_generators':[list(g1),list(g2)],
 'gamma4_order':len(elements),'H6_order_exponent':35,'class3_quotient_order_exponent':30,
 'gamma3_nonzero_image':g3,'formal_U4_coefficient':str(coefficient),'checks_passed':True}
def plain(obj):
    if isinstance(obj,dict):return {str(k):plain(v) for k,v in obj.items()}
    if isinstance(obj,(list,tuple)):return [plain(v) for v in obj]
    if isinstance(obj,s.Integer):return int(obj)
    return obj
result=plain(result)
Path(__file__).with_name('class_three_counterexample_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='class_two_matrices'},indent=2))

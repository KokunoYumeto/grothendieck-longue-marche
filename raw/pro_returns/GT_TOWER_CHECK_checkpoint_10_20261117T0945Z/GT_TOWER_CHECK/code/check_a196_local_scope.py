#!/usr/bin/env python3
"""Check A.196's ordinary local obstruction in O_{Q_3(cuberoot3)}/(alpha^6).

alpha^3=3, alpha^6=9.  The proof handles negative valuations separately;
this exact finite ring certificate handles all integral X_0,X_1.
"""
from itertools import product

M=9
one=(1,0,0)
zero=(0,0,0)
alpha=(0,1,0)

def add(x,y):
    return tuple((a+b)%M for a,b in zip(x,y))

def neg(x):
    return tuple(-a%M for a in x)

def mul(x,y):
    c=[0]*5
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c[i+j]+=a*b
    c[1]+=3*c[4]
    c[0]+=3*c[3]
    return tuple(a%M for a in c[:3])

def power(x,n):
    z=one
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z

def val(x):
    vals=[]
    for i,a in enumerate(x):
        if a:
            n=0
            while a%3==0:
                n+=1;a//=3
            vals.append(3*n+i)
    return min(vals,default=6)

elements=list(product(range(M),repeat=3))
U=(-2%M,0,1)
B=power(U,3)
A=mul((pow(649,8,M),0,0),alpha)
assert val(add(U,neg(one)))==2
assert val(add(B,neg(one)))==5
units_one=[x for x in elements if x[0]%3==1]
assert len(units_one)==243
assert {power(x,9) for x in units_one}=={one}
left={mul(A,power(x,9)) for x in elements}
right={add(one,neg(mul(B,power(x,9)))) for x in elements}
assert left.isdisjoint(right)
assert {val(x) for x in left}=={1,6}
print('Ring: (Z/9)[alpha]/(alpha^3-3), cardinality',len(elements))
print('U=',U,'B=U^3=',B,'A=',A)
print('v_alpha(U-1)=2; v_alpha(B-1)=5 modulo alpha^6.')
print('All',len(units_one),'units congruent to 1 modulo alpha have ninth power 1 modulo alpha^6.')
print('Possible valuations of A X_0^9 modulo alpha^6:',sorted({val(x) for x in left}))
print('No integral solutions of A X_0^9+B X_1^9=1 modulo alpha^6.')
print('PASS. This verifies the local ordinary-point obstruction, not A.196 global lifting assertions.')

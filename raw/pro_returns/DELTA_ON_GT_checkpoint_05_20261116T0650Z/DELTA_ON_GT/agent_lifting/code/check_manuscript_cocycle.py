#!/usr/bin/env python3
"""Exact class-two calculation and mod-3 commutator-quotient certificate."""
from itertools import product
from pathlib import Path
import json
import sympy as S

a,b,lam=S.symbols('a b lam')
left=-a*lam-lam**2
right=-lam*(lam+1)/2+b*lam
difference=S.factor(left-right)
assert S.simplify(difference+lam*(a+b+(lam-1)/2))==0
print('class-two central-coordinate difference:',difference)
print('for unit lambda, equality forces a+b=(1-lambda)/2')
print('scan12 abelianization gives beta=-(a+b)=(lambda-1)/2')

p=3;I=(1,0,0,1)
def mul(A,B):
    a,b,c,d=A;e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)
def inv(A):
    a,b,c,d=A;return (d,-b%p,-c%p,a)
def closure(gens):
    seen={I};queue=[I]
    while queue:
        a=queue.pop()
        for b in gens:
            c=mul(a,b)
            if c not in seen:seen.add(c);queue.append(c)
    return seen
G=[A for A in product(range(p),repeat=4) if (A[0]*A[3]-A[1]*A[2])%p==1]
comm={mul(mul(A,B),mul(inv(A),inv(B))) for A in G for B in G}
D=closure(comm)
U=(1,1,0,1);R=(0,2,1,2);minusI=(2,0,0,2)
assert len(G)==24 and len(D)==8
assert U not in D and R not in D and minusI in D
assert mul(mul(U,U),U)==I and mul(mul(R,R),R)==I
print('SL2(F3) order',len(G),'derived subgroup order',len(D))
print('U and R have nontrivial order-three abelian classes; -I is in the derived subgroup: PASS')
out={'class_two_difference':str(difference),'SL2_F3_order':len(G),
     'derived_subgroup':sorted(D),'U':U,'R':R,'minus_I':minusI}
dest=Path(__file__).resolve().parent.parent/'records'/'manuscript_cocycle.json'
dest.write_text(json.dumps(out,indent=2)+'\n')

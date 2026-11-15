#!/usr/bin/env python3
"""Exact counterexample to the universal finite-cover assertion in Boggi
1804.06322, PDF dated 2021-07-12, Lemma 6.7 (printed pp26-27).
N=ker(pi_1(S_g)->H_1(S_g,F_2)), iota acts -I=I on H_1.
"""
from itertools import product
import json

def add(x,y):return tuple(a^b for a,b in zip(x,y))
def mul(x,y):
    v,e=x;w,f=y
    # (-1)^e*w=w in characteristic two.
    return(add(v,w),e^f)
for g in (2,3):
    V=list(product((0,1),repeat=2*g));G=list(product(V,(0,1)))
    invol=(tuple([0]*(2*g)),1)
    C=[x for x in G if mul(x,invol)==mul(invol,x)]
    assert len(C)==2**(2*g+1) and len(C)>2
    print(json.dumps({'g':g,'degree_surface_cover':2**(2*g),'genus_cover':1+2**(2*g)*(g-1),'group':'(C2)^(2g+1)','centralizer_order':len(C),'claimed_centralizer_order':2,'counterexample_element':G[2]}))
import sympy as s

T1=s.eye(4);T1[0,1]=1
T2=s.eye(4);T2[2,3]=1
P=s.zeros(4)
for i,j in enumerate([2,3,0,1]):P[i,j]=1
M=T1*T2**2
C=P*M*P.inv()
assert C != M
assert C.applyfunc(lambda x:x%3) != M.applyfunc(lambda x:x%3)
print('Unequal-weight multitwist:',M.tolist())
print('Handle-swap conjugate:',C.tolist())
print('Different already on H1 modulo 3: full curve-set stabilizer is not this centralizer.')

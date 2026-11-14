#!/usr/bin/env python3
"""Exact obstruction to importing a once-punctured metabelian action.

P is free pro-three on x,y and N=ker(P->(Z/3)^2).
The cover is [3]: E-E[3] -> E-{0}. We detect a word in P''
which survives in N/gamma_3 N, using an explicit Heisenberg quotient.
"""
from pathlib import Path
from itertools import product
import json

vertices=list(product(range(3),repeat=2))
edges=[(i,j,a) for i,j in vertices for a in [1,2]]
tree={(i,0,1) for i in [0,1]}|{(i,j,2) for i in range(3) for j in [0,1]}
basis=[e for e in edges if e not in tree]
assert len(basis)==10
index={e:i for i,e in enumerate(basis)}
def inverse(w):return [-a for a in w[::-1]]
def rewrite(w):
    v=[0,0];out=[]
    for a in w:
        k=abs(a)-1
        if a>0:
            edge=(v[0],v[1],abs(a));v[k]=(v[k]+1)%3
        else:
            v[k]=(v[k]-1)%3;edge=(v[0],v[1],abs(a))
        if edge in index:out.append((index[edge],1 if a>0 else -1))
    assert v==[0,0]
    return out
def ab(w):
    out=[0]*10
    for i,a in rewrite(w):out[i]+=a
    return out
c=[1,2,-1,-2];cx=[1]+c+[-1]
v,w=ab(c),ab(cx)
choices=[(i,j,v[i]*w[j]-v[j]*w[i]) for i in range(10) for j in range(i+1,10)
         if (v[i]*w[j]-v[j]*w[i])%3]
assert choices
i,j,det=choices[0]
def mul(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
def inv(a):return ((-a[0])%3,(-a[1])%3,(-a[2]+a[0]*a[1])%3)
def image(word):
    out=(0,0,0)
    for k,sign in rewrite(word):
        e=(int(k==i),int(k==j),0)
        out=mul(out,e if sign>0 else inv(e))
    return out
z=c+cx+inverse(c)+inverse(cx)
result=image(z)
assert result==(0,0,det%3)
assert result!=(0,0,0)
out={'basis_edges':basis,'word_c':c,'word_xcx_inverse':cx,
     'abelian_c':v,'abelian_xcx_inverse':w,
     'selected_coordinates':[i,j],'determinant':det,
     'Heisenberg_order':27,'commutator_image':result,
     'word_in_P_second_derived':True,
     'word_not_in_N_third_lower_central':True,'checks_passed':True}
Path(__file__).with_name('elliptic_cover_kernel_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

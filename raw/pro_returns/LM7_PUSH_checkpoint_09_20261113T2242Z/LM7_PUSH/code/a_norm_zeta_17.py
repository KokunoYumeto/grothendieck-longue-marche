#!/usr/bin/env python3
"""Search and exactly certify a norm-zeta element in K(cuberoot17).

Complex eigenvalues only propose Eisenstein integer coefficients; every
reported identity is checked by exact integer-pair arithmetic.  A failed
bounded search is not used as a nonexistence statement.
"""
from pathlib import Path
import json
import numpy as np

def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(n,a):return n*a[0],n*a[1]
def mul(a,b):
    u,v=a;c,d=b
    return u*c-v*d,u*d+v*c-v*d
def cube(a):return mul(mul(a,a),a)
def norm(a,b,c):return add(add(cube(a),scale(17,cube(b))),add(scale(289,cube(c)),scale(-51,mul(mul(a,b),c))))
def complex_(a):return a[0]+a[1]*np.exp(2j*np.pi/3)

bound=7
coeff=[(i,j) for i in range(-bound,bound+1) for j in range(-bound,bound+1)]
bb=np.array([complex_(b) for b in coeff]);cc=bb.copy()
BB,CC=np.meshgrid(bb,cc,indexing='ij');B=BB.reshape(-1);C=CC.reshape(-1)
witnesses=[]
for k in range(5):
    target=(0,3**(3*k))
    pol=np.zeros((len(B),3,3),dtype=np.complex128)
    pol[:,1,0]=1;pol[:,2,1]=1
    pol[:,0,2]=-(17*B**3+289*C**3-complex_(target))
    pol[:,1,2]=51*B*C
    roots=np.linalg.eigvals(pol)
    candidates=0
    for idx,rr in enumerate(roots):
        b=coeff[idx//len(coeff)];c=coeff[idx%len(coeff)]
        for aa in rr:
            a1=int(round(2*aa.imag/np.sqrt(3)));a0=int(round(aa.real+a1/2))
            if abs(aa-complex_((a0,a1)))>1e-5:continue
            candidates+=1
            if norm((a0,a1),b,c)==target:
                row={'denominator':3**k,'a':[a0,a1],'b':list(b),'c':list(c),
                     'norm_numerator':list(target),'identity_verified_exactly':True}
                if row not in witnesses:witnesses.append(row)
    print('Denominator',3**k,'b/c coefficient bound',bound,'approximate candidates',candidates,
          'cumulative exact witnesses',len(witnesses),flush=True)
    if witnesses:break
Path(__file__).with_suffix('.json').write_text(json.dumps(witnesses,indent=2)+'\n')
for row in witnesses[:10]:print(json.dumps(row),flush=True)
print('PASS: every reported norm is exact; bounded failure carries no nonexistence claim.',flush=True)

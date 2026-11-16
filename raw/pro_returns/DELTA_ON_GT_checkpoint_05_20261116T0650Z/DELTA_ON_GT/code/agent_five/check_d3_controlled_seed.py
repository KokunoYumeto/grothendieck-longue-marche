"""All thirty actual cyclic-source seed maps in the reverse-prime target.

Full character permutations are retained, including for S itself.
"""
from itertools import permutations
from math import lcm
import json
import numpy as np
from check_ferrari_d3_fox import *

D=np.load(ROOT/'ferrari_d3_fox.npz');X=list(zip(D['X_permutations'],D['X_blocks']))
GL_EXP=8*lcm(*(4**j-1 for j in range(1,6)))
def perm_order(p):
    used=set();n=1
    for a in range(N):
        if a in used:continue
        b=a;k=0
        while b not in used:used.add(b);k+=1;b=int(p[b])
        n=lcm(n,k)
    return n
def exact_order(g):
    n=perm_order(g[0])*GL_EXP;assert eq(power(g,n),ONE)
    for p in (2,3,5,7,11,17,31):
        while n%p==0 and eq(power(g,n//p),ONE):n//=p
    return n
def primary(g,n,p):
    m=n;q=1
    while m%p==0:m//=p;q*=p
    return power(g,0 if q==1 else m*pow(m,-1,q))
def A(x,y):
    z=inv(mul(x,y));xx,_,_=primary3(x);yy,_,_=primary3(y);zz,_,_=primary3(z)
    return comm(comm(xx,yy),comm(yy,zz))
def S(x,y):
    z=inv(mul(x,y));return prod(A(y,z),A(x,y),A(z,x))

reports=[];sp=[];sm=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    x,y=X[i],X[j];z=inv(mul(x,y));triple=(x,y,z)
    row={'pair':[i+1,j+1],'peripheral_orders':[bounded_order(g) for g in triple],'cores':[]}
    for p in permutations(range(3)):
        s=S(triple[p[0]],triple[p[1]]);n=exact_order(s)
        two=primary(s,n,2);three=primary(s,n,3)
        row['cores'].append({'peripheral_permutation':p,'seed_order':n,
          'seed_character_permutation_order':perm_order(s[0]),
          'moved_characters':int(np.count_nonzero(s[0]!=IP)),
          'nonidentity_chain_blocks':int(np.count_nonzero(np.any(s[1]!=IM,axis=(1,2)))),
          'two_part_centralizes_pair':all(eq(mul(two,g),mul(g,two)) for g in (x,y)),
          'three_part_centralizes_pair':all(eq(mul(three,g),mul(g,three)) for g in (x,y))})
        sp.append(s[0]);sm.append(s[1])
    reports.append(row);print(json.dumps(row),flush=True)
np.savez_compressed(ROOT/'ferrari_d3_controlled_seed.npz',seed_permutations=np.stack(sp),seed_blocks=np.stack(sm))
(ROOT/'ferrari_d3_controlled_seed.json').write_text(json.dumps(reports,indent=2)+'\n')
print('All30 full semilinear source evaluations completed; no lifted finite-shadow assertion.')

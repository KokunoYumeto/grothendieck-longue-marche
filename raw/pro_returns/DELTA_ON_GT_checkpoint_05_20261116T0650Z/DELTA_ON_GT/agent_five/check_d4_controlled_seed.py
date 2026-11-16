"""Controlled actual-source seed in the complete D4 Fox-chain quotient.

This only tests the fixed profinite word S used in the accepted R2 lift;
it never treats a finite surviving assignment as a lift.
"""
from pathlib import Path
from itertools import permutations
from math import lcm
import json
import numpy as np
from check_ferrari_d4_fox import (ONE, IP, IM, characters, mul, inv, prod, power,
                                comm, eq, bounded_order, primary3)

ROOT=Path(__file__).resolve().parent
data=np.load(ROOT/'ferrari_d4_fox.npz')
X=list(zip(data['X_permutations'],data['X_blocks']))
GL_EXP=9*lcm(*(9**j-1 for j in range(1,6)))
PRIMES=(2,3,5,7,11,13,41,61)

def block_order(g):
    assert np.array_equal(g[0],IP),'the controlled seed must fix every character'
    assert eq(power(g,GL_EXP),ONE)
    n=GL_EXP
    for p in PRIMES:
        while n%p==0 and eq(power(g,n//p),ONE):n//=p
    return n

def part(g,n,p):
    q=1;m=n
    while m%p==0:q*=p;m//=p
    return power(g,0 if q==1 else m*pow(m,-1,q))

def A(x,y):
    z=inv(mul(x,y))
    xp,_,_=primary3(x);yp,_,_=primary3(y);zp,_,_=primary3(z)
    return comm(comm(xp,yp),comm(yp,zp))

def S(x,y):
    z=inv(mul(x,y))
    return prod(A(y,z),A(x,y),A(z,x))

reports=[];saved=[]
for i,j in ((2,3),(4,0),(1,2),(3,4),(0,1)):
    x,y=X[i],X[j];z=inv(mul(x,y));triple=(x,y,z)
    row={'pair':[i+1,j+1],'peripheral_orders':[bounded_order(g) for g in triple], 'cores':[]}
    for p in permutations(range(3)):
        s=S(triple[p[0]],triple[p[1]])
        n=block_order(s);s2=part(s,n,2)
        bad=[]
        for k,g in enumerate((x,y)):
            left,right=mul(s2,g),mul(g,s2)
            assert np.array_equal(left[0],right[0])
            ids=np.flatnonzero(np.any(left[1]!=right[1],axis=(1,2)))
            if len(ids):bad.append({'generator':k,'number_of_character_blocks':len(ids),
                                   'first_character_index':int(ids[0]),'first_character':characters[ids[0]].tolist()})
        moved=np.flatnonzero(np.any(s[1]!=IM,axis=(1,2)))
        row['cores'].append({'peripheral_permutation':p,'seed_order':n,
                            'nonidentity_blocks':len(moved),'two_primary_part_central':not bad,
                            'centrality_failure':bad})
        saved.append(s[1])
    reports.append(row)
    print(json.dumps(row),flush=True)
np.savez_compressed(ROOT/'ferrari_d4_controlled_seed.npz',seed_blocks=np.stack(saved))
(ROOT/'ferrari_d4_controlled_seed.json').write_text(json.dumps(reports,indent=2)+'\n')
print('All five pairs and all six exact peripheral markings checked; no finite-shadow lifting assertion.')

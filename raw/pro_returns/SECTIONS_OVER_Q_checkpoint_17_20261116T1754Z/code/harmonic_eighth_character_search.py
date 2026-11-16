#!/usr/bin/env python3
"""Actual order-four fibre-character evaluations on harmonic eighth-power covers."""
from fractions import Fraction as Q
from math import gcd
from itertools import product
from pathlib import Path
import json
from harmonic_tripod_obstruction_search import vu, hilbert, primes

def eighth(a,p):
    if not a:return False
    v,u=vu(a,p,32 if p==2 else p)
    if v%8:return False
    return u==1 if p==2 else pow(u,(p-1)//gcd(8,p-1),p)==1

CHI16={}
for k in range(4):
    for sg in (1,-1):CHI16[sg*pow(5,k,16)%16]=k
assert len(CHI16)==8 and CHI16[9]==2

def evaluation(f,r,p):
    if p==2:
        _,u=vu(f,2,16)
        return (-CHI16[u]+2*hilbert(f,r,p))%4
    v,_=vu(f,p)
    return (v*CHI16[p%16]+2*hilbert(f,r,p))%4

def main():
    data=json.loads(Path('work/code/harmonic_eighth_candidates.json').read_text())
    total=actual=nonzero=0
    for index,row in enumerate(data):
        R,c,r=map(Q,(row['R'],row['c'],row['r']))
        S={2,3}
        for value in (R,R-1,R-Q(1,2),c,c-1,c-Q(1,2),R-c,r):S|=primes(value)
        print('COVER',index,dict(R=str(R),c=str(c),r=str(r)),flush=True)
        for p in sorted(S):
            if p>10000:
                print('Unsearched large bad prime',p,flush=True);continue
            limit=1024 if p==2 else min(2*p+32,1000)
            counts=[0,0,0]
            for e,u in product(range(-3,4),range(1,limit)):
                if u%p==0:continue
                X=Q(p)**e*u
                T=R*X**8
                if T in (0,1,Q(1,2),c):continue
                total+=1;counts[0]+=1
                y8=(T-1)/(R-1);z8=(T-Q(1,2))/(R-Q(1,2))
                if not eighth(y8,p) or not eighth(z8,p):continue
                actual+=1;counts[1]+=1
                f=(T-c)/(R-c);val=evaluation(f,r,p)
                assert val%2==0, (row,p,X,T,f,val)
                if val:
                    nonzero+=1;counts[2]+=1
                    print('NONZERO ORDER-FOUR CHARACTER',dict(p=p,X=str(X),T=str(T),f=str(f),y8=str(y8),z8=str(z8),invariant=f'{val}/4'),flush=True)
                    Path('work/code/harmonic_eighth_witness.json').write_text(json.dumps(dict(row=row,p=p,X=str(X),T=str(T),f=str(f),y8=str(y8),z8=str(z8),val=val),indent=2)+'\n')
                    print('Counts:',total,actual,nonzero,flush=True)
                    return
            print('place',p,'trials/points/nonzero',counts,flush=True)
    print('Counts:',total,actual,nonzero,flush=True)
    print('No general vanishing conclusion is inferred from this finite search.')
if __name__=='__main__':main()


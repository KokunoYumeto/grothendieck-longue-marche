#!/usr/bin/env python3
"""Exploratory exact finite p-primary Smith checks, not an all-depth theorem."""
from pathlib import Path
import json
import numpy as np

def local_smith(A, precision=10):
    modulus=5**precision
    A=np.array(A,dtype=np.int64)%modulus
    n=A.shape[0]
    vals=[]
    for k in range(n):
        B=A[k:,k:]
        nz=B!=0
        if not nz.any():break
        valuation=0
        while True:
            loc=np.argwhere(nz & ((B//(5**valuation))%5!=0))
            if len(loc):break
            valuation+=1
            assert valuation<precision
        i,j=map(int,loc[0]);i+=k;j+=k
        A[[k,i],:]=A[[i,k],:]
        A[:,[k,j]]=A[:,[j,k]]
        power=5**valuation
        inv=pow(int(A[k,k])//power,-1,modulus)
        A[k,k:]=(A[k,k:]*inv)%modulus
        assert A[k,k]==power
        for i in range(k+1,n):
            q=int(A[i,k])//power
            assert int(A[i,k])%power==0
            if q:A[i,k:]=(A[i,k:]-q*A[k,k:])%modulus
            assert A[i,k]==0
        # Actual column subtraction affects only this pivot row now.
        assert all(int(x)%power==0 for x in A[k,k+1:])
        A[k,k+1:]=0
        vals.append(valuation)
    return vals,n-len(vals)

def run():
    rows=[]
    for r,N in [(1,1),(1,2),(2,2),(1,3),(2,3),(3,3)]:
        n=5**N;a=5**r
        A=np.zeros((n,n),dtype=np.int64)
        for j in range(n):
            for shift in (0,a):
                for b,c in enumerate((1,3,3,1)):
                    A[(2*j+shift+b)%n,j]+=c
            A[j,j]-=1
        vals,zero=local_smith(A)
        # Rational rank is proved separately by the actual Fourier cycles.
        assert zero==N-r
        predicted=list(range(N-r+1,N))+[N+1]
        tors=[v for v in vals if v]
        assert tors==predicted,(r,N,tors,predicted)
        rows.append({'r':r,'N':N,'dimension':n,'precision':10,
                     'rational_free_rank':N-r,'zero_pivots':zero,
                     'nonzero_pivots':len(vals),'five_torsion_valuations':tors,
                     'exactness':'all rationally nonzero pivots found below precision; remaining pivots have the proved rational nullity'})
    return {'status':'EXPLORATION_ONLY_NOT_AN_ALL_DEPTH_SMITH_PROOF','rows':rows}

if __name__=='__main__':
    result=run();data=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(data)
    print(data,end='')

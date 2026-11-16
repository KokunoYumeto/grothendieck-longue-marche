#!/usr/bin/env python3
"""Exact finite search on C2 x_E D, distinguishing it from the quartic C4."""
from fractions import Fraction as Q
from math import gcd
from tripod_eighth_search import valuation_unit, hilbert
from harmonic_tripod_candidate_search import fourth

def square(x,p):
    if not x:return False
    v,u=valuation_unit(x,p,8 if p==2 else p)
    return v%2==0 and (u==1 if p==2 else pow(u,(p-1)//2,p)==1)

def main():
    R,c,chi=Q(32,81),Q(25,34),Q(210)
    F=lambda t:t*(t-1)*(t-Q(1,2))
    total=c2=zcount=badc2=badz=0
    first={}
    for p in (2,3,5,7,17,937):
        counts=[0,0,0,0,0]
        for e in range(-4,5):
            for u in range(1,max(512,2*p)):
                if u%p==0:continue
                X=Q(p)**e*u
                T=R*X**2
                if T in (0,1,Q(1,2),c):continue
                counts[0]+=1
                y2=(T-1)/(R-1);z2=(T-Q(1,2))/(R-Q(1,2))
                if not square(y2,p) or not square(z2,p):continue
                counts[1]+=1
                inv=hilbert((T-c)/(R-c),chi,p)
                counts[3]+=inv
                if inv:first.setdefault((p,'C2'),(X,T))
                if not fourth(F(T)/F(R),p):continue
                counts[2]+=1
                counts[4]+=inv
                if inv:first.setdefault((p,'Z'),(X,T))
        total+=counts[0];c2+=counts[1];zcount+=counts[2];badc2+=counts[3];badz+=counts[4]
        print(p,dict(zip(('trials','C2','Z','C2_nonzero','Z_nonzero'),counts)))
    print('Witnesses:',first)
    print('Totals:',total,c2,zcount,badc2,badz)
    print('Finite search only: no inference about constancy if no witness occurs.')
if __name__=='__main__':main()

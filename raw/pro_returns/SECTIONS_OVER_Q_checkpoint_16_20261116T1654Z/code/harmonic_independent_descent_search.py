#!/usr/bin/env python3
"""Exact local tests of twelve independent x-descent directions."""
from fractions import Fraction as F
from itertools import product
from harmonic_tripod_obstruction_search import fourth_roots_units, hilbert, primes, is_square
DATA=[(138,(150,720),(162,1080)),(154,(-98,1176),(350,5880)),(210,(-150,1800),(-90,1800)),(330,(-275,3025),(-150,3600)),(426,(588,9828),(726,15840)),(434,(448,2352),(722,15504)),(546,(-507,4563),(-468,6084)),(651,(-525,8820),(-363,10296)),(658,(1458,49680),(1792,70560)),(1146,(2028,75348),(5202,365976)),(1155,(-605,24200),(-539,23716)),(1254,(-912,25992),(-1058,21896))]
def main():
    trials=points=nonzero=0
    for d,P,Q in DATA:
        for x,y in (P,Q):assert y*y==x**3-d*d*x
        R=(1+F(P[0],d))/2;c=(1-F(Q[0],d))/2;r=abs(F(Q[1],P[1]));char=2*r
        boundary=[(1/(1-R),1/(1-2*R)),(1/R,1/(2*R-1)),(1/(2*R),1/(2*(1-R)))]
        assert not any(is_square(-a) or is_square(-b) or is_square(-a*b) for a,b in boundary)
        print('COVER',dict(d=d,R=R,c=c,r=r,char=char),flush=True)
        S={2,3}
        for val in [R,R-1,R-F(1,2),c,c-1,c-F(1,2),R-c,char]:S|=primes(val)
        for p in sorted(S):
            if p>10000:
                print('Unsearched large bad prime',p,flush=True);continue
            limit=4096 if p==2 else min(p**3,4000)
            candidates=[F(x) for x in range(1,limit+1)]
            candidates += [F(x,p**h) for h in range(1,3) for x in range(1,min(p*p,1000)) if x%p]
            local=bad=0
            for X in candidates:
                T=R*X**4
                if T in (0,F(1,2),1,c):continue
                trials+=1
                Ys=fourth_roots_units((T-1)/(R-1),p)
                if not Ys:continue
                Zs=fourth_roots_units((T-F(1,2))/(R-F(1,2)),p)
                if not Zs:continue
                points+=1;local+=1
                f=(T-c)/(R-c)
                if not hilbert(f,char,p):continue
                nonzero+=1;bad+=1
                print('NONZERO EVALUATION',dict(p=p,X=X,T=T,f=f,Ys=Ys,Zs=Zs),flush=True)
                for Y,Z in product(Ys,Zs):
                    symbols=[[hilbert(W,a,p),hilbert(W,b,p)] for W,(a,b) in zip((X,Y,Z),boundary)]
                    if any(any(row) for row in symbols):continue
                    print('ROOT-SYMBOL-ZERO WITNESS',dict(d=d,R=R,c=c,r=r,p=p,X=X,Y=Y,Z=Z,T=T,f=f,symbols=symbols),flush=True)
                    print('Counts',trials,points,nonzero,flush=True)
                    return
            print('place',p,'actual',local,'nonzero',bad,flush=True)
    print('Counts',trials,points,nonzero,flush=True)
    print('Finite search only; no general vanishing or existence inference.')
if __name__=='__main__':main()

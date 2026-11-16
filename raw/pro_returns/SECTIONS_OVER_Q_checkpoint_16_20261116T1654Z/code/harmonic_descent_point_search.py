#!/usr/bin/env python3
"""Exact rational-point search for independent x-descent directions on E_d."""
from math import isqrt
from fractions import Fraction as Q
from sympy import factorint
from harmonic_tripod_obstruction_search import is_square

LIMIT_D=2000
LIMIT_X=10000

def sf(x):
    s=-1 if x<0 else 1
    for p,e in factorint(abs(x)).items():
        if e%2:s*=int(p)
    return s

def span(vals):
    out={1}
    for a in vals:out|={sf(a*b) for b in tuple(out)}
    return out

def good_R(R):
    rows=[(1/(1-R),1/(1-2*R)),(1/R,1/(2*R-1)),(1/(2*R),1/(2*(1-R)))]
    return not any(is_square(-a) or is_square(-b) or is_square(-a*b) for a,b in rows)

def main():
    trials=points=0
    found=0
    for d in range(2,LIMIT_D+1):
        if sf(d)!=d:continue
        basis=[-1,d]; pts=[]
        candidates=list(range(-d+1,0))+list(range(d+1,LIMIT_X+1))
        for x in candidates:
            rhs=x*(x*x-d*d);trials+=1
            y=isqrt(rhs)
            if not y or y*y!=rhs:continue
            points+=1
            xclass=sf(x)
            if xclass in span(basis):continue
            basis.append(xclass);pts.append((Q(x),Q(y)))
            if len(pts)>=2:
                good=[P for P in pts if good_R((1+P[0]/d)/2)]
                if not good:continue
                P0=good[0];P1=next(P for P in pts if sf(int(P[0])) not in span([-1,d,sf(int(P0[0]))]))
                R=(1+P0[0]/d)/2;c=(1-P1[0]/d)/2;r=abs(P1[1]/P0[1])
                assert (c/R)*((c-1)/(R-1))*((c-Q(1,2))/(R-Q(1,2)))==-r*r
                print('CANDIDATE',dict(d=d,base=P0,source=P1,R=R,c=c,r=r,character=2*r,x_classes=basis),flush=True)
                found+=1
                break
        if found>=12:break
    print('Exact counts:',dict(trials=trials,points=points,candidates=found),flush=True)
    print('No rank assertion: each independence assertion is a literal rational squareclass check.')
if __name__=='__main__':main()

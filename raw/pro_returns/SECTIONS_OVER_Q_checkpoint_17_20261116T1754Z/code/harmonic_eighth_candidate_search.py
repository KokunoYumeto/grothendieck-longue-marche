#!/usr/bin/env python3
"""Exact harmonic eighth-power candidates with a rational negative fourth-power fibre product."""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import json
from sympy import factorint
from harmonic_tripod_obstruction_search import is_square

def sf(x):
    x=Q(x);s=-1 if x<0 else 1
    for p,e in factorint(abs(x.numerator)*x.denominator).items():
        if e%2:s*=int(p)
    return s

def span(vals):
    out={1}
    for a in vals:out|={sf(a*b) for b in tuple(out)}
    return out

def good(R):
    rows=[(1/(1-R),1/(1-2*R)),(1/R,1/(2*R-1)),(1/(2*R),1/(2*(1-R)))]
    return not any(is_square(-a) or is_square(-b) or is_square(-a*b) for a,b in rows)

def main():
    data=[];trials=0;seen=set()
    for d in range(2,2001):
        if sf(d)!=d:continue
        pts=[]
        for x in list(range(-d+1,0))+list(range(d+1,15001)):
            yy=x*(x*x-d*d);trials+=1;y=isqrt(yy)
            if y and y*y==yy:pts.append((x,y))
        for P,Q0 in product(pts,repeat=2):
            if P==Q0:continue
            rho=Q(Q0[1],P[1])
            if not is_square(rho):continue
            R=(1+Q(P[0],d))/2;c=(1-Q(Q0[0],d))/2
            if c in (0,1,Q(1,2),R) or not good(R):continue
            r=Q(isqrt(rho.numerator),isqrt(rho.denominator))
            if sf(Q0[0]) in span([-1,d,sf(P[0])]):continue
            key=(R,c)
            if key in seen:continue
            seen.add(key)
            D=[c/R,(c-1)/(R-1),(c-Q(1,2))/(R-Q(1,2))]
            assert D[0]*D[1]*D[2]==-r**4
            row=dict(d=d,base=P,source=Q0,R=str(R),c=str(c),r=str(r),D=list(map(str,D)))
            data.append(row);print(row,flush=True)
            if len(data)>=24:break
        if len(data)>=24:break
    Path('work/code/harmonic_eighth_candidates.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Integer trials:',trials,'exact candidates:',len(data),flush=True)
    print('All source independence assertions concern literal squareclasses, not Mordell-Weil ranks.')
if __name__=='__main__':main()


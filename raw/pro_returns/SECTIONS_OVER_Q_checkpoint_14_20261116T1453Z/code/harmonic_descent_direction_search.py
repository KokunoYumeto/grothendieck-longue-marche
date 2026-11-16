#!/usr/bin/env python3
"""Exact rational-u search for two x-descent directions beyond -1 and d."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, isqrt
import json
import sympy as sp

limit=500
primes=list(sp.primerange(1,2*limit+1))
pos={p:i for i,p in enumerate(primes)}
sfmask=[0]*(2*limit+1)
for n in range(2,2*limit+1):
    sfmask[n]=sum(1<<pos[p] for p,e in sp.factorint(n).items() if e%2)

def maskvalue(mask):
    ans=1
    while mask:
        bit=mask & -mask
        ans*=primes[bit.bit_length()-1]
        mask-=bit
    return ans

def rank(rows):
    basis={}
    for row in rows:
        while row:
            i=row.bit_length()-1
            if i not in basis:
                basis[i]=row
                break
            row^=basis[i]
    return len(basis)

def square(x):
    x=F(x)
    return x>=0 and isqrt(x.numerator)**2==x.numerator and isqrt(x.denominator)**2==x.denominator

def boundary_ok(R):
    pairs=[(1/(1-R),1/(1-2*R)),(1/R,1/(2*R-1)),(1/(2*R),1/(2*(1-R)))]
    return all(not any(square(-x) for x in (d1,d2,d1*d2)) for d1,d2 in pairs)

curves={}
count=0
for m in range(2,limit+1):
    for n in range(1,m):
        if gcd(m,n)!=1:continue
        dm=sfmask[m]^sfmask[n]^sfmask[m-n]^sfmask[m+n]
        d=maskvalue(dm)
        if d>20000:continue
        xm=dm^sfmask[m]^sfmask[n]
        D=m*n*(m*m-n*n)
        h=isqrt(D//d)
        assert d*h*h==D
        x=F(d*m,n)
        y=F(d*d*h,n*n)
        assert y*y==x*x*x-d*d*x
        data=(m,n,xm,x,y)
        curves.setdefault(d,{'dm':dm,'points':[]})['points'].append(data)
        count+=1

results=[]
for d,entry in sorted(curves.items()):
    dm=entry['dm']
    points=entry['points']
    if rank([dm]+[p[2] for p in points])<3:continue
    found=None
    for base in points:
        if rank([dm,base[2]])!=2:continue
        m,n,_,xb,yb=base
        R=F(m-n,2*m)
        yR=yb*F(n*n,m*m)
        if not boundary_ok(R):continue
        for target in points:
            if rank([dm,base[2],target[2]])!=3:continue
            mt,nt,_,xt,yt=target
            c=F(nt-mt,2*nt)
            r=abs(yt/yR)
            f=lambda t:t*(t-1)*(t-F(1,2))
            assert f(c)/f(R)==-r*r
            found={'d':d,'base_mn':[m,n],'target_mn':[mt,nt],
                   'base_point_before_T0':[str(xb),str(yb)],
                   'base_point_after_T0':[str(-F(d*d,1)/xb),str(yR)],
                   'target_point':[str(xt),str(yt)],
                   'R':str(R),'c':str(c),'r':str(r),'character':str(2*r),
                   'x_direction_rank_including_d':3,'boundary_minus_one_excluded':True}
            break
        if found:break
    if found:results.append(found)
    if len(results)>=15:break

out=Path(__file__).resolve().parent
payload={'parameter_bound':limit,'d_bound':20000,'exact_points':count,'curves':len(curves),'candidates':results}
(out/'harmonic_descent_direction_candidates.json').write_text(json.dumps(payload,indent=2)+'\n')
lines=[f'Exact rational points checked: {count}; distinct positive squarefree d: {len(curves)}.',
       'These are exact F2 squareclass ranks; no Mordell-Weil rank assertion is made.']
for x in results:
    lines.append(f'd={x["d"]}, R={x["R"]}, c={x["c"]}, r={x["r"]}, 2r={x["character"]}; base m,n={x["base_mn"]}; target m,n={x["target_mn"]}.')
text='\n'.join(lines)+'\n'
(out/'harmonic_descent_direction_search_output.txt').write_text(text)
print(text,end='')

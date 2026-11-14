#!/usr/bin/env python3
"""Exploratory exact Hankel minors for 27-torsion on the F4 Raynaud theta.

F4 is F2[a]/(a^2+a+1). Polynomials are pairs of binary coefficient masks.
This file is a candidate calculation, not an integrated theorem certificate.
"""
from pathlib import Path
import json
import time

ZERO=(0,0); ONE=(1,0); X=(2,0); ALPHA=(0,1)

def add(a,b): return (a[0]^b[0],a[1]^b[1])
def deg(a): return max(a[0].bit_length(),a[1].bit_length())-1
def clmul(a,b):
    if a.bit_length()<b.bit_length():a,b=b,a
    r=0
    while b:
        low=b&-b
        r^=a<<(low.bit_length()-1)
        b^=low
    return r
def mul(a,b):
    u=clmul(a[0],b[0]);v=clmul(a[1],b[1])
    w=clmul(a[0]^a[1],b[0]^b[1])^u^v
    return (u^v,w^v)
def scale(a,c):
    if c==0:return ZERO
    if c==1:return a
    if c==2:return(a[1],a[0]^a[1])
    return(a[0]^a[1],a[0])
def shift(a,n):return(a[0]<<n,a[1]<<n)
def leading(a):
    d=deg(a)
    return ((a[0]>>d)&1)+2*((a[1]>>d)&1)
def divmodp(a,b):
    assert b!=ZERO
    db=deg(b);ib={1:1,2:3,3:2}[leading(b)]
    monic=scale(b,ib);q=ZERO;r=a
    while r!=ZERO and deg(r)>=db:
        k=deg(r)-db;c=leading(r)
        r=add(r,shift(scale(monic,c),k))
        q=add(q,shift(scale(ONE,c),k))
    return scale(q,ib),r
def exactdiv(a,b):
    q,r=divmodp(a,b)
    assert r==ZERO,(deg(a),deg(b),r)
    return q
def gcdp(a,b):
    while b!=ZERO:a,b=b,divmodp(a,b)[1]
    return scale(a,{1:1,2:3,3:2}[leading(a)]) if a!=ZERO else ZERO
def power(a,n):
    r=ONE
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n>>=1
    return r
def determinant(M):
    M=[row[:] for row in M];n=len(M);prev=ONE
    for k in range(n-1):
        if M[k][k]==ZERO:
            i=next((i for i in range(k+1,n) if M[i][k]!=ZERO),None)
            if i is None:return ZERO
            M[k],M[i]=M[i],M[k]
        pivot=M[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=exactdiv(add(mul(pivot,M[i][j]),mul(M[i][k],M[k][j])),prev)
            M[i][k]=ZERO
        prev=pivot
    return M[-1][-1]

def main():
    started=time.time();xp1=add(X,ONE);D=mul(X,xp1)
    P={}
    for k in range(1,27):
        v=add(mul(power(X,k-1),power(xp1,2*k)),scale(mul(power(X,2*k),power(xp1,k-1)),2))
        if k==1:v=add(v,power(D,2))
        if k%2==0:v=add(v,mul(P[k//2],P[k//2]))
        P[k]=v
    matrix=[[P[i-j] for j in range(13)] for i in range(13,27)]
    out={"status":"exploratory","matrix_shape":[14,13],"minors":[]}
    G=ZERO
    for omitted in [0,13,1,12,2,11,3,10,4,9,5,8,6,7]:
        det=determinant([row for i,row in enumerate(matrix) if i!=omitted])
        G=gcdp(G,det)
        residual=G
        while residual!=ZERO and divmodp(residual,X)[1]==ZERO:residual=exactdiv(residual,X)
        while residual!=ZERO and divmodp(residual,xp1)[1]==ZERO:residual=exactdiv(residual,xp1)
        row={"omitted_row":omitted,"degree":deg(det),"coefficient_masks":[str(v) for v in det],"gcd_degree":deg(G),"residual_gcd_degree":deg(residual)}
        out["minors"].append(row)
        print(json.dumps({k:v for k,v in row.items() if k!="coefficient_masks"}),flush=True)
        if residual==ONE:
            out["status"]="PASS: no common zero away from x=0,1"
            break
    out["gcd_masks"]=[str(v) for v in G]
    out["residual_gcd_masks"]=[str(v) for v in residual]
    out["runtime_seconds"]=time.time()-started
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!="minors"}),flush=True)

if __name__=='__main__':main()

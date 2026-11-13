#!/usr/bin/env python3
"""Cocycle and cohomology checks for the actual rank-two extension.

All affine coordinates use Fractions. At finite level N, units modulo 6N
retain the halves and thirds in the displayed reference lifts. We check
every pair in (Z/6N)^* x S3, not only the S3 generators.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
from itertools import product
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

OUT=Path(__file__).resolve().parent
R=(0,-1,1,-1); S=(0,1,1,0); I=(1,0,0,1)
def mm(A,B):return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
def mv(A,v):return tuple(sum(A[2*i+k]*v[k] for k in range(2)) for i in range(2))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,v):return tuple(a*x for x in v)
zero=(F(0),F(0)); ts=(F(1,3),F(-1,3)); p=(F(2,3),F(1,3))
group=[]; t={}; b={}; words={}
for i in range(3):
    A=I
    for _ in range(i):A=mm(A,R)
    for j in range(2):
        H=mm(A,S) if j else A; group.append(H); words[H]='r'*i+'s'*j or '1'
        t[H]=mv(A,ts) if j else zero
        b[H]=sub(sub(p,mv(H,p)),t[H])
        assert all(x.denominator==1 for x in b[H])
assert len(set(group))==6
nonid=[g for g in group if g!=I]

def cochain_differential(deg):
    cols=list(product(nonid,repeat=deg))
    rows=list(product(nonid,repeat=deg+1))
    ci={v:i for i,v in enumerate(cols)}
    M=sp.zeros(2*len(rows),2*len(cols))
    def insert(row,key,A,sign):
        if key not in ci:return
        j=ci[key]
        for a in range(2):
            for c in range(2):M[2*row+a,2*j+c]+=sign*A[2*a+c]
    for row,tup in enumerate(rows):
        insert(row,tup[1:],tup[0],1)
        for j in range(deg):
            key=tup[:j]+(mm(tup[j],tup[j+1]),)+tup[j+2:]
            insert(row,key,I,(-1)**(j+1))
        insert(row,tup[:-1],I,(-1)**(deg+1))
    return M

def smith(M):
    d=smith_normal_form(M,domain=sp.ZZ)
    return [abs(int(d[i,i])) for i in range(min(d.shape)) if d[i,i]]
def kernelsize(diag,ncols,N):
    a=N**(ncols-len(diag))
    for z in diag:a*=gcd(z,N)
    return a
def imagesize(diag,N):
    a=1
    for z in diag:a*=N//gcd(z,N)
    return a

def main():
    D0=cochain_differential(0);D1=cochain_differential(1);D2=cochain_differential(2)
    assert D1*D0==sp.zeros(D1.rows,D0.cols) and D2*D1==sp.zeros(D2.rows,D1.cols)
    ds=[smith(D) for D in (D0,D1,D2)]
    print('S3 normalized-cochain Smith diagonals:',ds,flush=True)
    cc=[]
    for g in group:
        row=[]
        for h in group:
            c=sub(add(t[g],mv(g,t[h])),t[mm(g,h)])
            db=sub(add(b[g],mv(g,b[h])),b[mm(g,h)])
            assert all(z.denominator==1 for z in c) and add(c,db)==zero
            row.append([int(z) for z in c])
        cc.append(row)
    records=[]
    print('N |Q_(6N)| checked_pairs |H0(S3,M/N)| |H1| |H2| actual_H2_order 2part 3part',flush=True)
    for N in (1,2,3,4,6,8,12,24):
        L=6*N;units=[a for a in range(L) if gcd(a,L)==1]
        Q=list(product(units,group))
        def ref(a,g):
            nu=F(a-1,2)
            return add((-nu/3,nu/3),scale(a,t[g]))
        def corr(a,g):
            nu=F(a-1,2)
            return add((-nu,-nu),scale(a,b[g]))
        refs={q:ref(*q) for q in Q}; corrs={q:corr(*q) for q in Q}
        for a,g in Q:
            for h,k in Q:
                prod=((a*h)%L,mm(g,k))
                c=sub(add(refs[(a,g)],scale(a,mv(g,refs[(h,k)]))),refs[prod])
                db=sub(add(corrs[(a,g)],scale(a,mv(g,corrs[(h,k)]))),corrs[prod])
                assert all(v.denominator==1 for v in c)
                assert all(v.denominator==1 and int(v)%N==0 for v in add(c,db))
        h0=kernelsize(ds[0],D0.cols,N)
        h1=kernelsize(ds[1],D1.cols,N)//imagesize(ds[0],N)
        h2=kernelsize(ds[2],D2.cols,N)//imagesize(ds[1],N)
        assert h0==h1==1 and h2==gcd(3,N)
        row={'N':N,'unit_modulus':L,'base_order':len(Q),'pairs_checked':len(Q)**2,
             'H0_S3_order':h0,'H1_S3_order':h1,'H2_S3_order':h2,
             'actual_extension_class_order':1,'actual_2_primary_order':1,'actual_3_primary_order':1,
             'splittings':N*N,'conjugacy_classes':1}
        records.append(row)
        print(N,len(Q),len(Q)**2,h0,h1,h2,1,1,1,flush=True)
    data={'S3_order':[words[g] for g in group],'S3_action':[list(g) for g in group],
          'reference_translations':[[str(v) for v in t[g]] for g in group],
          'integral_correction_cochain':[[int(v) for v in b[g]] for g in group],
          'reference_cocycle':cc,'smith_diagonals':ds,'finite_levels':records,
          'scalar_correction':'s(mu)=(-nu,-nu)u_mu; nu=(mu-1)/2',
          'fixed_point':['2/3','1/3']}
    (OUT/'b_splitting.json').write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':main()

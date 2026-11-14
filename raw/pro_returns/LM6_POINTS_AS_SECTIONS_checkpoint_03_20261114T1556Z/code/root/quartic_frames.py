#!/usr/bin/env python3
"""Independent exact Q(zeta_8) computation of all framed quartic cusp paths.

No floating-point field arithmetic and no imported LM7 program is used.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

def elt(x):
    return tuple(Q(a) for a in x) if isinstance(x,(list,tuple)) else (Q(x),Q(0),Q(0),Q(0))
zero=elt(0);one=elt(1);z=elt([0,1,0,0])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    out=[Q(0)]*7
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    for k in range(6,3,-1):out[k-4]-=out[k]
    return tuple(out[:4])
def inv(a):
    cols=[mul(a,elt([int(i==j) for i in range(4)])) for j in range(4)]
    M=[[cols[j][i] for j in range(4)]+[Q(i==0)] for i in range(4)]
    for j in range(4):
        k=next(k for k in range(j,4) if M[k][j])
        M[j],M[k]=M[k],M[j]
        d=M[j][j];M[j]=[x/d for x in M[j]]
        for k in range(4):
            if k!=j:
                d=M[k][j];M[k]=[x-d*y for x,y in zip(M[k],M[j])]
    return tuple(row[-1] for row in M)
def div(a,b):return mul(a,inv(b))
def power(a,n):
    if n<0:return power(inv(a),-n)
    out=one
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
sqrt2=sub(z,power(z,3));assert mul(sqrt2,sqrt2)==elt(2)
alpha=[power(z,1+2*i) for i in range(4)]
cusps={}
for i,a in enumerate(alpha):
    cusps['A'+str(i)]=(zero,a,one)
    cusps['B'+str(i)]=(a,zero,one)
    cusps['C'+str(i)]=(a,one,zero)
def line(d,pt):
    typ=d[0];a=alpha[int(d[1])];x,y,w=pt
    return sub(y,mul(a,w)) if typ=='A' else sub(x,mul(a,w if typ=='B' else y))
O='B0';order=[*['A'+str(i) for i in range(4)],'B1','B2','B3',*['C'+str(i) for i in range(4)]]
lookup={mul(power(z,k),power(sqrt2,n)):(k,n) for n in range(-16,5) for k in range(8)}
K=[];N=[];coeffs=[]
for q in order:
    kr=[];nr=[];cr=[]
    for d in order:
        atO=div(mul(elt(4),line(d,cusps[O])),alpha[0])
        atq=div(alpha[int(d[1])],mul(elt(4),line(O,cusps[q]))) if q==d else div(line(d,cusps[q]),line(O,cusps[q]))
        value=div(atq,atO)
        k,n=lookup[value];kr.append(k);nr.append(n);cr.append([str(x) for x in value])
    K.append(kr);N.append(nr);coeffs.append(cr)
expected=[[-8,-3,-2,-3,-5,-6,-5,-4,-4,-4,-4],[-3,-8,-3,-2,-5,-6,-5,-4,-4,-4,-4],[-2,-3,-8,-3,-5,-6,-5,-4,-4,-4,-4],[-3,-2,-3,-8,-5,-6,-5,-4,-4,-4,-4],[-5,-5,-5,-5,-10,-6,-4,-5,-5,-5,-5],[-6,-6,-6,-6,-6,-12,-6,-6,-6,-6,-6],[-5,-5,-5,-5,-4,-6,-10,-5,-5,-5,-5],[-4,-4,-4,-4,-5,-6,-5,-8,-3,-2,-3],[-4,-4,-4,-4,-5,-6,-5,-3,-8,-3,-2],[-4,-4,-4,-4,-5,-6,-5,-2,-3,-8,-3],[-4,-4,-4,-4,-5,-6,-5,-3,-2,-3,-8]]
assert N==expected
origin=[sum(row[4:7],Q(0))/32 for row in N]
assert origin==[Q(-1,2)]*4+[Q(-5,8),Q(-3,4),Q(-5,8)]+[Q(-1,2)]*4
result={'field':'Q[z]/(z^4+1)','cusp_order':order,'entries_verified':121,'N':N,'K':K,'exact_coefficients':coeffs,'coset_origin_vector':[str(x) for x in origin],'checks_passed':True}
path=Path(__file__).with_name('quartic_frames_output.json');path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='exact_coefficients'},indent=2))

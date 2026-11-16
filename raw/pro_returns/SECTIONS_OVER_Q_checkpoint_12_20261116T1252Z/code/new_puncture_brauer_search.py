#!/usr/bin/env python3
"""Search actual local fourth-power points for a new-puncture Brauer obstruction."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json

def v2(a):
    a=F(a)
    if not a:return None
    n,d=a.numerator,a.denominator;e=0
    while n%2==0:n//=2;e+=1
    while d%2==0:d//=2;e-=1
    return e

def unit_mod(a,m):
    a=F(a);e=v2(a);u=a/F(2)**e
    return (u.numerator*pow(u.denominator,-1,m))%m

def fourth_q2(a):
    if not a:return True
    return v2(a)%4==0 and unit_mod(a,16)==1

def hilbert_2(a):
    u=unit_mod(a,8)
    return 1 if u in (1,7) else -1

out=[];tested=0;soluble=0
for k in range(2,41):
    for h in range(1,k):
        if gcd(h,k)!=1:continue
        u=k*(k+h);v=h*(k-h);w=k*k+h*h
        R=F(u,w);c=F(k*(k-h),w)
        assert c*(c-1)==-R*(R-1)
        baseline=hilbert_2(R-c)
        for e in range(-4,5):
            for z in range(1,128,2):
                x=F(z)*F(2)**e
                y4=F(u*x**4-w,v);tested+=1
                if not y4 or not fourth_q2(y4):continue
                soluble+=1
                a=R*x**4-c
                if not a:continue
                symbol=hilbert_2(a)
                if symbol!=baseline:
                    out.append({'h':h,'k':k,'u':u,'v':v,'w':w,'R':str(R),'c':str(c),'x':str(x),'y4':str(y4),'alpha':str(a),'alpha_v2':v2(a),'alpha_unit_mod8':unit_mod(a,8),'baseline':baseline,'local_symbol':symbol})
                    break
            if out and out[-1]['h']==h and out[-1]['k']==k:break
        if len(out)>=12:break
    if len(out)>=12:break
result={'trials':tested,'soluble':soluble,'examples':out,'note':'For every reported point y4 has valuation divisible by4 and odd unit1 modulo16, hence admits an actual Q2 fourth root. No general assertion inferred from absent examples.'}
text=json.dumps(result,indent=2)+'\n'
Path(__file__).with_name('new_puncture_brauer_search_output.txt').write_text(text)
print(text,end='')

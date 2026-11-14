#!/usr/bin/env python3
"""Exploratory exact theta torsion and orbit saturation on remaining F4 classes.
Uses general Cantor composition on Y^2+uY=uF, genus two, with origin Winfty.
No theorem is promoted by this experiment alone.
"""
from pathlib import Path
import json,time
from A_theta_F4_moduli_witnesses import Base,Tower,trim,padd,pscale,pmul,pdiv,peval

class Table:
    def __init__(self,source,q):
        self.q=q;self.mt=[[source.mul(a,b) for b in range(q)] for a in range(q)]
        self.iv=[0]+[next(b for b in range(1,q) if self.mt[a][b]==1) for a in range(1,q)]
    def mul(self,a,b):return self.mt[a][b]
    def inv(self,a):assert a;return self.iv[a]
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r

class Jacobian:
    def __init__(self,F,abc):
        self.F=F;self.abc=abc;self.h=[0,1,1];a,b,c=abc;self.f=pmul(self.h,[b,b^c,a,a],F);self.zero=([1],[]);self.T=(self.h,[]);self.add_count=0
    def exdiv(self,a,b):
        q,r=pdiv(a,b,self.F);assert not r;return q
    def xgcd(self,a,b):
        F=self.F;r0,r1=a,b;s0,s1=[1],[];t0,t1=[],[1]
        while r1:
            q,r=pdiv(r0,r1,F);r0,r1=r1,r;s0,s1=s1,padd(s0,pmul(q,s1,F));t0,t1=t1,padd(t0,pmul(q,t1,F))
        iv=F.inv(r0[-1]);return pscale(r0,iv,F),pscale(s0,iv,F),pscale(t0,iv,F)
    def check(self,D):
        u,v=D;F=self.F
        assert u[-1]==1 and len(v)<len(u)
        assert not pdiv(padd(padd(pmul(v,v,F),pmul(self.h,v,F)),self.f),u,F)[1]
        return D
    def reduce(self,u,v):
        F=self.F;u=pscale(u,F.inv(u[-1]),F);v=pdiv(v,u,F)[1]
        self.check((u,v))
        while len(u)>3:
            newu=self.exdiv(padd(padd(pmul(v,v,F),pmul(self.h,v,F)),self.f),u)
            newu=pscale(newu,F.inv(newu[-1]),F);v=pdiv(padd(v,self.h),newu,F)[1];u=newu
            self.check((u,v))
        if u==[1]:v=[]
        return self.check((u,v))
    def add(self,L,R):
        F=self.F;u1,v1=L;u2,v2=R;d1,a,b=self.xgcd(u1,u2);d,e,c=self.xgcd(d1,padd(padd(v1,v2),self.h));a=pmul(e,a,F);b=pmul(e,b,F)
        u=self.exdiv(pmul(u1,u2,F),pmul(d,d,F))
        numerator=padd(padd(pmul(pmul(a,u1,F),v2,F),pmul(pmul(b,u2,F),v1,F)),pmul(c,padd(pmul(v1,v2,F),self.f),F))
        self.add_count+=1;return self.reduce(u,self.exdiv(numerator,d))
    def neg(self,D):return D[0],pdiv(padd(D[1],self.h),D[0],self.F)[1]
    def times(self,D,n):
        r=self.zero
        while n:
            if n&1:r=self.add(r,D)
            D=self.add(D,D);n>>=1
        return r
    def theta(self,D):return len(self.add(D,self.T)[0])<=2
    def theta_point(self,x,y):
        Y=self.F.mul(self.F.mul(x,x^1),y)
        return self.add(self.check(([x,1],[Y] if Y else [])),self.T)

def orbits(n):
    from math import gcd
    remaining={i for i in range(1,n) if gcd(i,n)==1};out=[]
    while remaining:
        a=min(remaining);orb=[];i=a
        while i not in orb:orb.append(i);i=2*i%n
        remaining.difference_update(orb);out.append(orb)
    return out

def main():
    started=time.time();base=Base(4,19);F=Table(Tower(base,[8,1,1]),256);records=[]
    for key,abc in [('203',[1,9,14]),('302',[1,11,13])]:
        J=Jacobian(F,abc);assert J.add(J.T,J.T)==J.zero
        roots={}
        for y in range(256):roots.setdefault(F.mul(y,y)^y,[]).append(y)
        candidates=[];pointcount=3
        for x in range(2,256):
            a,b,c=abc;phi=F.mul(a,x)^F.mul(b,F.inv(x))^F.mul(c,F.inv(x^1))
            ys=roots.get(phi,[]);pointcount+=len(ys)
            if not ys:continue
            eta=J.theta_point(x,ys[0]);assert J.theta(eta);assert J.add(eta,J.neg(eta))==J.zero
            assert J.times(eta,65408)==J.zero
            if J.times(eta,511)!=J.zero:continue
            n=511
            for p in [7,73]:
                if J.times(eta,n//p)==J.zero:n//=p
            assert n>1 and J.times(eta,n)==J.zero
            hits=[];cur=J.zero
            for i in range(n):
                if J.theta(cur):hits.append(i)
                cur=J.add(cur,eta)
            assert cur==J.zero
            O=orbits(n);missing=[o for o in O if not set(o).intersection(hits)]
            entry={'x':x,'y':ys[0],'eta':eta,'order':n,'theta_multiples':hits,'primitive_doubling_orbits':O,'missing_orbits':missing,'criterion_satisfied':not missing}
            candidates.append(entry)
            print(json.dumps({'key':key,'x':x,'n':n,'theta_hits':hits,'missing':len(missing)}),flush=True)
        assert pointcount==255
        records.append({'key':key,'curve_coefficients':abc,'pointcount_F256':pointcount,'odd_theta_coordinate_count':len(candidates),'candidates':candidates,'cantor_operations':J.add_count})
    out={'status':'EXPLORATORY complete F256 theta-odd subgroup enumeration','field':'F16=F2[w]/(w4+w+1); F256=F16[z]/(z2+z+8); four-bit blocks','curves':records,'runtime_seconds':time.time()-started}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'done':True,'seconds':out['runtime_seconds']}),flush=True)
if __name__=='__main__':main()

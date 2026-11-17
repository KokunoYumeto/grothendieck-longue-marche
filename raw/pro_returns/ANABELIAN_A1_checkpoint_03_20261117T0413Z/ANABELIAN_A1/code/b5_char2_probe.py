#!/usr/bin/env python3
"""Exact B5 probes for C/F2: y^2+y=x^3+1/x.

Equivalently Y^2+X^2*Y=X^5+X, with canonical base point infinity.
For each field and each prime occurring to exponent one in #J, enumerate
all curve points, project their classes to the cyclic prime subgroup,
and record the complete character-sum coefficient of the twisted L-function.
All characters of that cyclic quotient are covered by conjugacy.

The generic binary-field and Cantor implementation below is copied from
isolating_lang_covers.py; it is run here on the stated new curve and checked
at every group operation. No main script from that file is executed.
"""
from pathlib import Path
from collections import Counter
import json
import sympy as sp
class BinaryField:
    def __init__(self,n,mod):
        self.n,self.mod,self.q=n,mod,1<<n
        self.mul=[[self.raw_mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv=[0]+[self.pow(a,self.q-2) for a in range(1,self.q)]
    def raw_mul(self,a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&self.q:a^=self.mod
        return z
    def pow(self,a,n):
        z=1
        while n:
            if n&1:z=self.mul[z][a]
            a=self.mul[a][a];n>>=1
        return z
    def root4(self):
        return min(a for a in range(2,self.q) if self.mul[a][a]^a^1==0)

def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return tuple(a)

class Jacobian:
    def __init__(self,K,alpha):
        self.K,self.alpha=K,alpha
        self.h=(alpha,1,1)
        self.f=(1,1,0,alpha,0,1)
        self.O=((1,),())
    def addp(self,a,b):
        return trim((a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0)
                    for i in range(max(len(a),len(b))))
    def mulp(self,a,b):
        if not a or not b:return ()
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]^=self.K.mul[x][y]
        return trim(c)
    def scale(self,a,c):
        return trim(self.K.mul[x][c] for x in a)
    def divp(self,a,b):
        assert b
        a=list(a);q=[0]*max(0,len(a)-len(b)+1)
        while len(a)>=len(b):
            d=len(a)-len(b);c=self.K.mul[a[-1]][self.K.inv[b[-1]]]
            q[d]=c
            for i,x in enumerate(b):a[d+i]^=self.K.mul[c][x]
            while a and not a[-1]:a.pop()
        return trim(q),tuple(a)
    def exact(self,a,b):
        q,r=self.divp(a,b);assert not r
        return q
    def modp(self,a,b):return self.divp(a,b)[1]
    def xgcd(self,a,b):
        s,t,ss,tt=(1,),(),(),(1,)
        while b:
            q,r=self.divp(a,b)
            a,b=b,r
            s,ss=ss,self.addp(s,self.mulp(q,ss))
            t,tt=tt,self.addp(t,self.mulp(q,tt))
        c=self.K.inv[a[-1]]
        return self.scale(a,c),self.scale(s,c),self.scale(t,c)
    def check(self,D):
        u,v=D
        assert u and u[-1]==1 and len(u)<=3 and len(v)<len(u)
        assert not self.modp(self.addp(self.addp(self.mulp(v,v),self.mulp(self.h,v)),self.f),u)
    def add(self,D,E):
        u1,v1=D;u2,v2=E
        d1,e1,e2=self.xgcd(u1,u2)
        d,c1,c2=self.xgcd(d1,self.addp(self.addp(v1,v2),self.h))
        s1,s2,s3=self.mulp(c1,e1),self.mulp(c1,e2),c2
        u=self.exact(self.mulp(u1,u2),self.mulp(d,d))
        v=self.addp(self.addp(self.mulp(self.mulp(s1,u1),v2),
                             self.mulp(self.mulp(s2,u2),v1)),
                    self.mulp(s3,self.addp(self.mulp(v1,v2),self.f)))
        v=self.modp(self.exact(v,d),u)
        while len(u)>3:
            u2=self.exact(self.addp(self.addp(self.f,self.mulp(v,v)),self.mulp(self.h,v)),u)
            u2=self.scale(u2,self.K.inv[u2[-1]])
            v=self.modp(self.addp(self.h,v),u2);u=u2
        result=(u,v);self.check(result)
        return result
    def neg(self,D):
        return D[0],self.modp(self.addp(self.h,D[1]),D[0])
    def multiple(self,D,n):
        z=self.O
        while n:
            if n&1:z=self.add(z,D)
            D=self.add(D,D);n>>=1
        return z
    def evalp(self,f,x):
        y=0
        for c in reversed(f):y=self.K.mul[y][x]^c
        return y
    def points(self,subset=None):
        subset=list(range(self.K.q)) if subset is None else subset
        result=[None]
        for x in subset:
            h,f=self.evalp(self.h,x),self.evalp(self.f,x)
            for y in subset:
                if self.K.mul[y][y]^self.K.mul[h][y]^f==0:result.append((x,y))
        return result
    def pointclass(self,P):
        return self.O if P is None else ((P[0],1),(P[1],) if P[1] else ())

def probe():
    T=sp.symbols("T")
    polynomial=T**4+T**3+2*T+4
    companion=sp.Matrix([[0,0,0,-4],[1,0,0,-2],[0,1,0,0],[0,0,1,-1]])
    mods={1:3,2:7,3:11,4:19,5:37,6:67,7:131,8:285,9:529,10:1033}
    records=[]
    for m in range(1,11):
        K=BinaryField(m,mods[m]);J=Jacobian(K,0)
        J.h=(0,0,1);J.f=(0,1,0,0,0,1)
        points=J.points()
        expected=K.q+1-int(sp.trace(companion**m))
        assert len(points)==expected
        order=int((sp.eye(4)-companion**m).det())
        factors=sp.factorint(order)
        for ell,valuation in factors.items():
            ell=int(ell)
            if ell==2 or valuation!=1:continue
            projected=[J.multiple(J.pointclass(P),order//ell) for P in points]
            assert all(J.multiple(D,ell)==J.O for D in projected)
            generator=next(D for D in projected if D!=J.O)
            table={};D=J.O
            for i in range(ell):
                assert D not in table
                table[D]=i;D=J.add(D,generator)
            assert D==J.O and len(table)==ell
            counts=Counter(table[D] for D in projected)
            # L_chi(T)=1+(sum count[j]*zeta^j)*T+q*T^2, modulo Phi_ell.
            coeff=[counts.get(j,0)-counts.get(ell-1,0) for j in range(ell-1)]
            divisor=2**((m+1)//2)
            supersingular=all(c%divisor==0 for c in coeff)
            # Necessary and sufficient for *all* conjugate 2-adic valuations
            # of the degree-two coefficient to be at least m/2.
            record={"field_degree":m,"field_modulus":mods[m],"q":K.q,
                    "jacobian_order":order,"ell":ell,"curve_points":len(points),
                    "coefficient_count_map":dict(sorted(counts.items())),
                    "supersingular_all_primitive":supersingular,
                    "required_divisibility":divisor,
                    "violating_coefficient":next((c for c in coeff if c%divisor),None)}
            records.append(record)
            print(json.dumps(record),flush=True)
    output={"curve":"Y^2+X^2*Y=X^5+X", "frobenius_polynomial":str(polynomial),
            "checks":"All points counted; every Mumford operation verified; all nontrivial characters of each exponent-one prime quotient represented.",
            "records":records}
    Path(__file__).with_suffix(".json").write_text(json.dumps(output,indent=2)+"\n")
if __name__=="__main__":probe()

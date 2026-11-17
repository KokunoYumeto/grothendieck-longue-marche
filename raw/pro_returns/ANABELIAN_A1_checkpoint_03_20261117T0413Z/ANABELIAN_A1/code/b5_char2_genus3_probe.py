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
        assert u and u[-1]==1 and len(u)<=4 and len(v)<len(u)
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
        while len(u)>4:
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


def probe3():
    K=BinaryField(8,285);J=Jacobian(K,0)
    J.h=(1,);J.f=(0,0,0,0,0,0,0,1)
    sols={}
    for y in range(K.q):sols.setdefault(K.mul[y][y]^y,[]).append(y)
    pts=[None]+[(x,y) for x in range(K.q) for y in sols.get(K.pow(x,7),[])]
    T=sp.symbols("T");H=T**6-2*T**3+8
    F=sp.zeros(6)
    for i in range(5):F[i+1,i]=1
    F[0,5]=-8;F[3,5]=2
    order=int((sp.eye(6)-F**8).det())
    print("order",order,sp.factorint(order),"points",len(pts),flush=True)
    cofactor=order//9
    projected=[J.multiple(J.pointclass(P),cofactor) for P in pts]
    assert all(J.multiple(D,3)==J.O for D in projected)
    G=next(D for D in projected if D!=J.O)
    line={J.multiple(G,i) for i in range(3)}
    B=next(D for D in projected if D not in line)
    table={J.add(J.multiple(G,i),J.multiple(B,j)):(i,j) for i in range(3) for j in range(3)}
    assert len(table)==9 and all(D in table for D in projected)
    reps=[(1,0),(0,1),(1,1),(1,2)]
    records=[]
    for a,b in reps:
        counts=Counter((a*table[D][0]+b*table[D][1])%3 for D in projected)
        assert counts[1]==counts[2]
        records.append(dict(character=[a,b],counts=dict(counts),S1=counts[0]-counts[1]))
    output=dict(curve="y^2+y=x^7",field_modulus=285,order=order,G=G,B=B,records=records)
    print(json.dumps(output),flush=True)
    Path(__file__).with_suffix(".json").write_text(json.dumps(output,indent=2)+"\n")
if __name__=="__main__":probe3()

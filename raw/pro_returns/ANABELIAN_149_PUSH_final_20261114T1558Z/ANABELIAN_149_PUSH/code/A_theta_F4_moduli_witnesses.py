#!/usr/bin/env python3
"""Construct small, direct norm certificates for positive F4-moduli theta scans.

This does not import the mask/Hankel determinant engine. It uses ordinary
coefficient lists, selects a certified irreducible factor, solves the local
jet equations over that finite field, and verifies the entire norm identity.
The output contains the field, coordinate, polynomial A and polynomial B.
"""
from pathlib import Path
import json,time

class Base:
    def __init__(self,e,mod):
        self.e=e;self.mod=mod;self.q=1<<e
        self.mt=[[self.rawmul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inverses=[0]+[next(b for b in range(1,self.q) if self.mt[a][b]==1) for a in range(1,self.q)]
    def rawmul(self,a,b):
        r=0
        while b:
            if b&1:r^=a
            a<<=1
            if a&self.q:a^=self.mod
            b>>=1
        return r
    def mul(self,a,b):return self.mt[a][b]
    def inv(self,a):assert a;return self.inverses[a]
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r

def trim(a):
    a=list(a)
    while a and a[-1]==0:a.pop()
    return a

def padd(a,b):
    c=list(a)+[0]*max(0,len(b)-len(a))
    for i,v in enumerate(b):c[i]^=v
    return trim(c)

def pscale(a,c,F):return trim([F.mul(x,c) for x in a])
def pmul(a,b,F):
    if not a or not b:return []
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]^=F.mul(x,y)
    return trim(c)

def pdiv(a,b,F):
    a=trim(a);b=trim(b);assert b
    q=[0]*max(0,len(a)-len(b)+1);ib=F.inv(b[-1])
    while a and len(a)>=len(b):
        i=len(a)-len(b);c=F.mul(a[-1],ib);q[i]^=c
        for j,y in enumerate(b):a[i+j]^=F.mul(c,y)
        a=trim(a)
    return trim(q),a

def pgcd(a,b,F):
    while b:a,b=b,pdiv(a,b,F)[1]
    return pscale(a,F.inv(a[-1]),F) if a else []

def ppowmod(a,n,f,F):
    r=[1]
    while n:
        if n&1:r=pdiv(pmul(r,a,F),f,F)[1]
        a=pdiv(pmul(a,a,F),f,F)[1];n>>=1
    return r

def peval(a,t,F):
    r=0
    for c in reversed(a):r=F.mul(r,t)^c
    return r

def irreducible_factor(f,F):
    f=pscale(f,F.inv(f[-1]),F)
    for a in range(F.q):
        if peval(f,a,F)==0:return [a,1]
    x=[0,1];h=x
    for d in range(1,len(f)):
        h=ppowmod(h,F.q,f,F)
        g=pgcd(f,padd(h,x),F)
        if len(g)<=1:continue
        # This is the first nonzero distinct-degree block, hence all factors
        # have degree d. Split using the absolute trace to F2.
        while len(g)-1>d:
            split=None
            for j in range(len(g)-1):
                for c in [1<<i for i in range(F.e)]:
                    a=[0]*j+[c];tr=[];z=a
                    for _ in range(F.e*d):
                        tr=padd(tr,z);z=ppowmod(z,2,g,F)
                    w=pgcd(g,tr,F)
                    if 1<len(w)<len(g):
                        other,rem=pdiv(g,w,F);assert not rem
                        split=w if len(w)<=len(other) else other
                        break
                if split is not None:break
            assert split is not None,'trace splitting failed'
            g=split
        assert len(g)-1==d and not pdiv(f,g,F)[1]
        assert ppowmod(x,F.q**d,g,F)==pdiv(x,g,F)[1]
        for k in range(1,d):assert len(pgcd(g,padd(ppowmod(x,F.q**k,g,F),x),F))==1
        return g
    raise AssertionError('no factor')

class Tower:
    def __init__(self,base,f):
        self.base=base;self.f=f;self.d=len(f)-1;self.bits=base.e;self.mask=(1<<self.bits)-1
        self.t=f[0] if self.d==1 else 1<<self.bits
    def unpack(self,x):
        a=[]
        for _ in range(self.d):a.append(x&self.mask);x>>=self.bits
        assert x==0
        return trim(a)
    def pack(self,a):
        assert len(a)<=self.d
        return sum(v<<(self.bits*i) for i,v in enumerate(a))
    def mul(self,a,b):
        if not a or not b:return 0
        if a==1:return b
        if b==1:return a
        c=pmul(self.unpack(a),self.unpack(b),self.base)
        if len(c)>self.d:c=pdiv(c,self.f,self.base)[1]
        return self.pack(c)
    def inv(self,a):
        assert a
        r0=self.f;r1=self.unpack(a);s0=[];s1=[1]
        while r1:
            q,r=pdiv(r0,r1,self.base);r0,r1=r1,r;s0,s1=s1,padd(s0,pmul(q,s1,self.base))
        assert len(r0)==1
        return self.pack(pdiv(pscale(s0,self.base.inv(r0[0]),self.base),self.f,self.base)[1])
    def pow(self,a,n):
        r=1
        while n:
            if n&1:r=self.mul(r,a)
            a=self.mul(a,a);n>>=1
        return r

def nullvector(M,F):
    M=[row[:] for row in M];r=0;pivots=[];cols=len(M[0])
    for j in range(cols):
        i=next((i for i in range(r,len(M)) if M[i][j]),None)
        if i is None:continue
        M[r],M[i]=M[i],M[r];iv=F.inv(M[r][j]);M[r]=[F.mul(v,iv) for v in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][j]:
                c=M[i][j];M[i]=[x^F.mul(c,y) for x,y in zip(M[i],M[r])]
        pivots.append(j);r+=1
    free=[i for i in range(cols) if i not in pivots];assert free
    v=[0]*cols;v[free[0]]=1
    for i,j in enumerate(pivots):v[j]=M[i][free[0]]
    return v,r

def translate(a,t,F):
    out=[0]*len(a)
    for i,c in enumerate(a):
        for j in range(i+1):
            if (j&i)==j:out[j]^=F.mul(c,F.pow(t,i-j))
    return trim(out)

def witness(row,positive,fields):
    started=time.time();base=fields[row['field_degree']];n=positive['n'];d=(n-3)//2
    factor=irreducible_factor(positive['coordinate_polynomial_coefficients'],base)
    F=Tower(base,factor);t=F.t;a,b,c=row['coefficients']
    assert t not in [0,1]
    it=F.inv(t);is1=F.inv(t^1)
    delta=F.mul(a,t)^F.mul(b,it)^F.mul(c,is1)
    ys=[0]
    for i in range(1,n):
        y=(a if i==1 else 0)^F.mul(b,F.pow(it,i+1))^F.mul(c,F.pow(is1,i+1))
        if i%2==0:y^=F.mul(ys[i//2],ys[i//2])
        ys.append(y)
    matrix=[[ys[i-j] for j in range(d+1)] for i in range(d+1,n)]
    Bshift,rank=nullvector(matrix,F)
    Ashift=[]
    for i in range(d+1):
        v=0
        for j in range(i+1):v^=F.mul(Bshift[j],ys[i-j])
        Ashift.append(v)
    A=translate(Ashift,t,F);B=translate(Bshift,t,F);assert len(B)==d+1
    inv=F.inv(B[-1]);A=pscale(A,inv,F);B=pscale(B,inv,F)
    assert peval(A,t,F)==0 and peval(B,t,F)!=0 and B[0]!=0 and peval(B,1,F)!=0
    u=[0,1,1];curveF=[b,b^c,a,a]
    norm=padd(pmul(u,padd(pmul(A,A,F),pmul(A,B,F)),F),pmul(pmul(B,B,F),padd(curveF,pscale(u,delta,F)),F))
    target=[F.mul(a,F.pow(t,n-j)) if (j&n)==j else 0 for j in range(n+1)]
    assert norm==trim(target)
    # Recheck every original jet, including the low jets fixed by A.
    Ash=translate(A,t,F);Bsh=translate(B,t,F)
    for i in range(n):
        v=Ash[i] if i<len(Ash) else 0
        for j in range(min(i,len(Bsh)-1)+1):v^=F.mul(Bsh[j],ys[i-j])
        assert v==0
    return {'moduli_key':row['moduli_key'],'coefficient_field_degree':base.e,'coefficient_field_binary_modulus':base.mod,'curve_coefficients':row['coefficients'],'n':n,'coordinate_minimal_polynomial':factor,'coordinate_field_extension_degree':F.d,'coordinate_t':t,'beta_relation_constant':delta,'A_coefficients':A,'B_coefficients':B,'jet_matrix_shape':[d+2,d+1],'jet_matrix_rank':rank,'norm_identity':'u(A^2+AB)+B^2(F+delta*u)=a(x+t)^n','all_jets_zero':True,'A_at_t':peval(A,t,F),'B_at_t':peval(B,t,F),'B_at_0':B[0],'B_at_1':peval(B,1,F),'norm_verified':True,'runtime_seconds':time.time()-started}

def main():
    started=time.time();scan=json.loads(Path(__file__).with_name('A_theta_F4_moduli_scan.json').read_text())
    fields={e:Base(e,m) for e,m in [(2,7),(4,19),(6,67)]};records=[]
    output=Path(__file__).with_suffix('.json')
    for row in scan['curves']:
        if not row['successful_orders']:continue
        positive=next(t for t in row['tests'] if t['theta_n_exists'])
        w=witness(row,positive,fields);records.append(w)
        output.write_text(json.dumps({'status':'RUNNING','witnesses':records},indent=2)+'\n')
        print(json.dumps({'key':w['moduli_key'],'n':w['n'],'field_degree':w['coefficient_field_degree']*w['coordinate_field_extension_degree'],'factor':w['coordinate_minimal_polynomial'],'seconds':round(w['runtime_seconds'],3)}),flush=True)
    out={'status':'PASS','positive_count':len(records),'all_norms_verified':True,'all_local_jets_verified':True,'encoding':'Each field element is an integer with consecutive base-field coefficient blocks; base field uses the indicated binary modulus. The coordinate field is the base polynomial quotient by coordinate_minimal_polynomial. A and B lists ascend in x. beta satisfies beta^2+beta=beta_relation_constant.','witnesses':records,'runtime_seconds':time.time()-started}
    output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}),flush=True)
if __name__=='__main__':main()

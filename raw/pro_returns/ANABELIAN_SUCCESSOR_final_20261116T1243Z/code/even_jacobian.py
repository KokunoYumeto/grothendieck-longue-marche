"""Genus-two Jacobians with two rational points at infinity.

For Y^2+hY=f, h monic of degree three and deg(f)<=5, denote the
infinities by O+ (Y/x^3=0) and O- (Y/x^3=1). A class is represented
by E-(O++O-), where E is the unique effective divisor of degree two
unless the class is zero. We store E as (u,v,a,b), with a,b the
multiplicities of O+,O-. The group law is an exact Riemann--Roch
calculation in the five-dimensional space <1,x,x^2,x^3,Y>.
"""
from itertools import product
from finite_jacobian import *

def nullspace(F,rows,n):
    A=[list(row) for row in rows if any(row)];piv=[];j=0
    for c in range(n):
        r=next((r for r in range(j,len(A)) if A[r][c]),None)
        if r is None:continue
        A[j],A[r]=A[r],A[j];iv=F.inv(A[j][c]);A[j]=[F.mul(x,iv) for x in A[j]]
        for k in range(len(A)):
            if k!=j and A[k][c]:
                m=A[k][c];A[k]=[x^F.mul(m,y) for x,y in zip(A[k],A[j])]
        piv.append(c);j+=1
        if j==len(A):break
    ans=[]
    for c in range(n):
        if c in piv:continue
        v=[0]*n;v[c]=1
        for row,p in zip(A,piv):v[p]=row[c]
        ans.append(v)
    return ans

class EvenJacobian(Jacobian):
    def __init__(self,F,h,f):
        self.F=F;self.R=PolynomialRing(F);self.h=trim(h);self.f=trim(f);self.g=2
        assert len(self.h)==4 and self.h[-1]==1 and len(self.f)<=6
        self.zero=((1,),(),1,1);self.elements=None
        self.canonical_base_class=((1,),(),0,2)
        H=list(reversed(self.h));FF=[0]*7
        for i,c in enumerate(self.f):FF[6-i]=c
        self.expansions=[]
        for constant in (0,1):
            z=[constant]+[0]*15
            for n in range(1,len(z)):
                a=FF[n] if n<len(FF) else 0
                for j in range(1,min(3,n)+1):a^=F.mul(H[j],z[n-j])
                if n%2==0:a^=F.mul(z[n//2],z[n//2])
                z[n]=a
            self.expansions.append(z)
    def neg(self,D):
        u,v,a,b=D
        return u,self.R.mod(self.R.add(v,self.h),u),b,a
    def compose(self,u1,v1,u2,v2):
        R=self.R
        d1,a0,b0=R.xgcd(u1,u2);d,e,c=R.xgcd(d1,R.add(R.add(v1,v2),self.h))
        a=R.mul(e,a0);b=R.mul(e,b0)
        u=R.monic(R.exact(R.mul(u1,u2),R.sq(d)))
        num=R.add(R.add(R.mul(R.mul(a,u1),v2),R.mul(R.mul(b,u2),v1)),R.mul(c,R.add(R.mul(v1,v2),self.f)))
        v=R.mod(R.exact(num,d),u)
        return u,v,(len(u1)+len(u2)-len(u)-1)//2
    def add(self,D,E):
        if D==self.zero:return E
        if E==self.zero:return D
        R,F=self.R,self.F;u1,v1,a1,b1=D;u2,v2,a2,b2=E
        u,v,r=self.compose(u1,v1,u2,v2);a=a1+a2+r;b=b1+b2+r;d=len(u)-1
        assert d+a+b==4
        if a and b:
            out=(u,v,a-1,b-1);assert self.valid(out);return out
        # A+B Y vanishes on the conjugate of the finite divisor.
        columns=[R.mod(tuple([0]*i+[1]),u) for i in range(4)]+[R.mod(R.add(v,self.h),u)]
        rows=[[col[i] if i<len(col) else 0 for col in columns] for i in range(d)]
        # Its poles at O+ and O- have bounds 3-b and 3-a.
        for z,bound in zip(self.expansions,(3-b,3-a)):
            for e in range(-3,-bound):
                rows.append([1 if e==-i else 0 for i in range(4)]+[z[e+3]])
        basis=nullspace(F,rows,5)
        assert len(basis)==1,(D,E,rows,basis)
        vec=basis[0];assert vec[4]
        vec=[F.div(x,vec[4]) for x in vec];A=trim(vec[:4])
        N=R.add(R.add(R.sq(A),R.mul(A,self.h)),self.f)
        up=R.monic(R.exact(N,u));vp=R.mod(A,up)
        mult=[]
        for z,old in zip(self.expansions,(a,b)):
            series={e:z[e+3] for e in range(-3,len(z)-3)}
            for i,c in enumerate(A):series[-i]=series.get(-i,0)^c
            val=min(e for e,c in series.items() if c)
            mult.append(val+d+old-1)
        out=up,vp,mult[0],mult[1]
        assert self.valid(out),(D,E,out,A,N)
        return out
    def valid(self,D):
        u,v,a,b=D;R=self.R
        return a>=0 and b>=0 and len(u)-1+a+b==2 and u[-1]==1 and len(v)<len(u) and not R.mod(R.add(R.add(R.sq(v),R.mul(self.h,v)),self.f),u)
    def points(self):
        F,R=self.F,self.R
        out=[('infinity_plus',self.zero),('infinity_minus',self.canonical_base_class)]
        for x in range(F.q):
            h=R.eval(self.h,x);f=R.eval(self.f,x)
            ys=[F.sqrt(f)] if not h else [F.mul(h,a) for a in F.artin.get(F.div(f,F.mul(h,h)),[])]
            for y in ys:out.append(((x,y),((x,1),trim((y,)),0,1)))
        return out
    def enumerate(self):
        if self.elements is not None:return self.elements
        F,R=self.F,self.R;out=[]
        pack=lambda a:sum(x<<(F.m*i) for i,x in enumerate(a))
        for d in range(3):
            for coeff in product(range(F.q),repeat=d):
                u=tuple(coeff)+(1,);cols=[]
                for i in range(d*F.m):
                    v=tuple([0]*(i//F.m)+[1<<(i%F.m)])
                    cols.append(pack(R.mod(R.add(R.sq(v),R.mul(self.h,v)),u)))
                for bits in binary_solutions(cols,pack(R.mod(self.f,u))):
                    v=trim([(bits>>(i*F.m))&(F.q-1) for i in range(d)])
                    for a in range(3-d):
                        D=(u,v,a,2-d-a);assert self.valid(D);out.append(D)
        self.elements=sorted(out);return self.elements

def normalize_rational_infinity(F,h,n,c):
    """AS curve y²+y=n/h+c, h irreducible cubic; put a rational point at infinity.

    Return the even model and the isomorphism x_old=x0+1/x_new,
    y_old=y_new+y0, or the identity when c=0. None means no rational point.
    """
    R=PolynomialRing(F)
    if not c:return EvenJacobian(F,h,R.mul(h,n)),{'identity':True}
    xy=None
    for x0 in range(F.q):
        v=F.div(R.eval(n,x0),R.eval(h,x0))^c
        roots=F.artin.get(v,[])
        if roots:xy=x0,roots[0];break
    if xy is None:return None,None
    x0,y0=xy
    def transform(poly):
        out=()
        for i,coef in enumerate(poly):
            term=(1,)
            for _ in range(i):term=R.mul(term,(1,x0))
            term=tuple([0]*(3-i))+term
            out=R.add(out,R.scale(term,coef))
        return out
    ht=transform(h);nt=R.add(transform(n),R.scale(ht,F.mul(y0,y0)^y0^c))
    z=F.inv(ht[-1]);ht=R.scale(ht,z);nt=R.scale(nt,z)
    assert len(nt)<=3
    return EvenJacobian(F,ht,R.mul(ht,nt)),{'x_old':'x0+1/x_new','x0':x0,'y_old':'Y_new/h_new+y0','y0':y0}

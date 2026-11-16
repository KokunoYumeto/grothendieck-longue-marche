"""Exact binary-field arithmetic and odd-degree hyperelliptic Jacobians.

The curve is Y^2+h(x)Y=f(x), deg f=2g+1, deg h<=g.
Reduced Mumford pairs use the unique point at infinity. No CAS is needed.
"""
from itertools import product

class BinaryField:
    def __init__(self, modulus):
        self.modulus=modulus; self.m=modulus.bit_length()-1; self.q=1<<self.m
        def raw(a,b):
            z=0
            while b:
                if b&1:z^=a
                b>>=1;a<<=1
                if a&self.q:a^=modulus
            return z
        for gen in range(1,self.q):
            exp=[];a=1;seen=set()
            while a not in seen:
                seen.add(a);exp.append(a);a=raw(a,gen)
            if len(exp)==self.q-1 and a==1:break
        else:raise ValueError('Modulus is not irreducible')
        self.generator=gen;self.exp=exp+exp;self.log=[-1]*self.q
        for i,a in enumerate(exp):self.log[a]=i
        self.artin={}
        for a in range(self.q):self.artin.setdefault(self.mul(a,a)^a,[]).append(a)
    def mul(self,a,b):return self.exp[self.log[a]+self.log[b]] if a and b else 0
    def inv(self,a):
        assert a
        return self.exp[(self.q-1-self.log[a])%(self.q-1)]
    def div(self,a,b):return self.mul(a,self.inv(b))
    def power(self,a,n):
        if not a:return 1 if n==0 else 0
        return self.exp[(self.log[a]*n)%(self.q-1)]
    def trace(self,a):
        r=0
        for _ in range(self.m):r^=a;a=self.mul(a,a)
        assert r in (0,1)
        return r
    def sqrt(self,a):return self.power(a,1<<(self.m-1))
    def embed_f4(self):return next(a for a in range(2,self.q) if self.mul(a,a)^a^1==0)

def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return tuple(a)

class PolynomialRing:
    def __init__(self,F):self.F=F
    def add(self,a,b):
        return trim([(a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
    def scale(self,a,c):return trim([self.F.mul(x,c) for x in a])
    def mul(self,a,b):
        if not a or not b:return ()
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]^=self.F.mul(x,y)
        return trim(c)
    def sq(self,a):
        if not a:return ()
        c=[0]*(2*len(a)-1)
        for i,x in enumerate(a):c[2*i]=self.F.mul(x,x)
        return trim(c)
    def divmod(self,a,b):
        assert b
        a=list(trim(a));q=[0]*max(0,len(a)-len(b)+1);ib=self.F.inv(b[-1])
        while a and len(a)>=len(b):
            d=len(a)-len(b);c=self.F.mul(a[-1],ib);q[d]=c
            for i,x in enumerate(b):a[i+d]^=self.F.mul(c,x)
            while a and not a[-1]:a.pop()
        return trim(q),tuple(a)
    def mod(self,a,b):return self.divmod(a,b)[1]
    def exact(self,a,b):
        q,r=self.divmod(a,b);assert not r,(a,b,r)
        return q
    def monic(self,a):return self.scale(a,self.F.inv(a[-1])) if a else ()
    def xgcd(self,a,b):
        s,t,ss,tt=(1,),(),(),(1,)
        while b:
            q,r=self.divmod(a,b);a,b=b,r
            s,ss=ss,self.add(s,self.mul(q,ss));t,tt=tt,self.add(t,self.mul(q,tt))
        c=self.F.inv(a[-1]);return self.scale(a,c),self.scale(s,c),self.scale(t,c)
    def eval(self,a,x):
        r=0
        for c in reversed(a):r=self.F.mul(r,x)^c
        return r

def binary_solutions(columns,target):
    """Solve an F2-linear equation in column form, including all kernel translates."""
    piv={};kernel=[]
    for i,col in enumerate(columns):
        v=col;w=1<<i
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=(v,w);break
            a,b=piv[k];v^=a;w^=b
        if not v:kernel.append(w)
    v=target;w=0
    while v:
        k=v.bit_length()-1
        if k not in piv:return []
        a,b=piv[k];v^=a;w^=b
    sol=[w]
    for b in kernel:sol += [x^b for x in sol]
    return sol

class Jacobian:
    def __init__(self,F,h,f,g=2):
        self.F=F;self.R=PolynomialRing(F);self.h=trim(h);self.f=trim(f);self.g=g
        assert len(self.f)==2*g+2 and len(self.h)<=g+1
        self.zero=((1,),())
        self.elements=None
    def neg(self,D):
        u,v=D;return u,self.R.mod(self.R.add(v,self.h),u)
    def add(self,D,E):
        R=self.R;u1,v1=D;u2,v2=E
        d1,a0,b0=R.xgcd(u1,u2)
        d,e,c=R.xgcd(d1,R.add(R.add(v1,v2),self.h))
        a=R.mul(e,a0);b=R.mul(e,b0)
        u=R.exact(R.mul(u1,u2),R.sq(d))
        num=R.add(R.add(R.mul(R.mul(a,u1),v2),R.mul(R.mul(b,u2),v1)),R.mul(c,R.add(R.mul(v1,v2),self.f)))
        v=R.mod(R.exact(num,d),u)
        while len(u)>self.g+1:
            u=R.monic(R.exact(R.add(R.add(R.sq(v),R.mul(self.h,v)),self.f),u))
            v=R.mod(R.add(v,self.h),u)
        return R.monic(u),v
    def scale(self,D,n):
        if n<0:return self.scale(self.neg(D),-n)
        a=self.zero
        while n:
            if n&1:a=self.add(a,D)
            n>>=1
            if n:D=self.add(D,D)
        return a
    def valid(self,D):
        u,v=D;R=self.R
        return bool(u) and u[-1]==1 and len(u)<=self.g+1 and len(v)<len(u) and not R.mod(R.add(R.add(R.sq(v),R.mul(self.h,v)),self.f),u)
    def points(self):
        F,R=self.F,self.R;out=[('infinity',self.zero)]
        for x in range(F.q):
            h=R.eval(self.h,x);f=R.eval(self.f,x)
            ys=[F.sqrt(f)] if not h else [F.mul(h,a) for a in F.artin.get(F.div(f,F.mul(h,h)),[])]
            for y in ys:out.append(((x,y),((x,1),trim((y,)))))
        return out
    def enumerate(self):
        if self.elements is not None:return self.elements
        F,R=self.F,self.R;out=[]
        def pack(a):return sum(x<<(F.m*i) for i,x in enumerate(a))
        for d in range(self.g+1):
            for coeff in product(range(F.q),repeat=d):
                u=tuple(coeff)+(1,)
                cols=[]
                for i in range(d*F.m):
                    v=tuple([0]*(i//F.m)+[1<<(i%F.m)])
                    cols.append(pack(R.mod(R.add(R.sq(v),R.mul(self.h,v)),u)))
                target=pack(R.mod(self.f,u))
                for bits in binary_solutions(cols,target):
                    v=trim([(bits>>(i*F.m))&(F.q-1) for i in range(d)])
                    D=(u,v);assert self.valid(D);out.append(D)
        self.elements=sorted(out);return self.elements
    def quotient(self,ell):
        """Return all coordinates for J/ell J, with a deterministic F_ell basis."""
        elts=self.enumerate();H=sorted({self.scale(D,ell) for D in elts})
        coords={h:() for h in H};basis=[]
        while len(coords)<len(elts):
            b=next(x for x in elts if x not in coords);basis.append(b)
            old=coords;coords={};shift=self.zero
            for j in range(ell):
                for x,c in old.items():
                    y=self.add(x,shift);assert y not in coords
                    coords[y]=c+(j,)
                shift=self.add(shift,b)
        assert len(elts)==len(H)*ell**len(basis)
        return coords,basis,H

def prime_factors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

def genus2_characters(J,exact_norm=True):
    """Every prime cyclic quotient over the current field and every rational basepoint.

    Characters differing by a nonzero scalar define the same cover; one vector
    from each such orbit is returned. The cyclotomic coefficients give all of
    its twisted L-polynomials by replacing zeta by zeta^j.
    """
    import sympy as s
    F=J.F;order=len(J.enumerate());pts=J.points();x=s.Symbol('x');rows=[]
    for ell in prime_factors(order):
        if ell==2:continue
        coords,basis,H=J.quotient(ell);r=len(basis)
        phi=s.Poly(sum(x**i for i in range(ell)),x)
        for v in product(range(ell),repeat=r):
            if not any(v) or next(a for a in v if a)!=1:continue
            chi=lambda D:sum(a*b for a,b in zip(v,coords[D]))%ell
            for name,P in pts:
                cP=chi(P);counts=[0]*ell
                for _,D in pts:counts[(chi(D)-cP)%ell]+=1
                kappa=(chi(getattr(J,'canonical_base_class',J.zero))-2*cP)%ell
                expr=1+sum(n*x**i for i,n in enumerate(counts))+F.q*x**kappa
                val=s.rem(s.Poly(expr,x),phi)
                gcd=s.gcd(s.Poly(val,x,modulus=2),s.Poly(phi,x,modulus=2))
                norm=int(s.resultant(phi,val)) if exact_norm and ell<=257 else None
                rows.append({'q':F.q,'modulus':F.modulus,'group_order':order,'point':name,'point_Mumford':P,'ell':ell,'character_basis':basis,'character_vector':v,'kernel_order':len(H)*ell**(r-1),'point_counts':counts,'L_coefficients_cyclotomic':[{'0':1},{str(i):n for i,n in enumerate(counts) if n},{str(kappa):F.q}],'L_value_reduced':str(val.as_expr()),'relative_class_number':norm,'mod2_gcd_degree':gcd.degree(),'L1_passes':gcd.degree()==0})
    return rows

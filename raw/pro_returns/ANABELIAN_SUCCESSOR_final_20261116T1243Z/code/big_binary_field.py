"""Exact GF(2^n) for n up to256, with a reproducible optional C++ helper."""
import ctypes,random,subprocess
from pathlib import Path
from finite_jacobian import BinaryField

HERE=Path(__file__).parent
def pmod(a,b):
    n=b.bit_length()
    while a.bit_length()>=n:a^=b<<(a.bit_length()-n)
    return a
def pgcd(a,b):
    while b:a,b=b,pmod(a,b)
    return a
SPREAD=[sum(((x>>j)&1)<<(2*j) for j in range(8)) for x in range(256)]
def psquare(a):
    z=0;j=0
    while a:z|=SPREAD[a&255]<<j;a>>=8;j+=16
    return z
def irreducible(f):
    n=f.bit_length()-1;pr=[];m=n;d=2
    while d*d<=m:
        if m%d==0:
            pr.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1:pr.append(m)
    tests={n//d for d in pr};x=2
    for i in range(1,n+1):
        x=pmod(psquare(x),f)
        if i in tests and pgcd(x^2,f)!=1:return False
    return x==2
def find_modulus(n):
    # Deterministic sparse search, then deterministic random search.
    for k in range(1,min(n,40)):
        f=(1<<n)|(1<<k)|1
        if irreducible(f):return f
    for k in range(3,min(n,40)):
        for j in range(2,k):
            f=(1<<n)|(1<<k)|(1<<j)|3
            if irreducible(f):return f
    rng=random.Random(26061116+n)
    while True:
        f=(1<<n)|rng.getrandbits(n)|1
        if irreducible(f):return f

class BigBinaryField:
    def __init__(self,modulus,check=True):
        self.modulus=modulus;self.m=modulus.bit_length()-1;self.q=1<<self.m
        assert self.m<=256 and (not check or irreducible(modulus))
        so=HERE/'binary_field_fast.so'
        if not so.exists() or so.stat().st_mtime<(HERE/'binary_field_fast.cpp').stat().st_mtime:
            subprocess.run(['g++','-O3','-std=c++17','-shared','-fPIC',str(HERE/'binary_field_fast.cpp'),'-o',str(so)],check=True)
        self.lib=ctypes.CDLL(str(so));self.Arr=ctypes.c_uint64*4
        ptr=ctypes.POINTER(ctypes.c_uint64)
        self.lib.gf_mul.argtypes=[ptr,ptr,ptr,ctypes.c_int,ptr]
        self.lib.gf_square.argtypes=[ptr,ptr,ctypes.c_int,ptr]
        self.low=self.pack(modulus^self.q);self.as_piv=None
    def pack(self,x):return self.Arr(*( (x>>(64*j))&((1<<64)-1) for j in range(4)))
    @staticmethod
    def unpack(x):return sum(int(x[j])<<(64*j) for j in range(4))
    def mul(self,a,b):
        if not a or not b:return 0
        if a==1:return b
        if b==1:return a
        z=self.Arr();self.lib.gf_mul(self.pack(a),self.pack(b),z,self.m,self.low);return self.unpack(z)
    def sq(self,a):
        z=self.Arr();self.lib.gf_square(self.pack(a),z,self.m,self.low);return self.unpack(z)
    def inv(self,a):
        assert a;u,v=a,self.modulus;g,h=1,0
        while u!=1:
            j=u.bit_length()-v.bit_length()
            if j<0:u,v=v,u;g,h=h,g;j=-j
            u^=v<<j;g^=h<<j
        return pmod(g,self.modulus)
    def div(self,a,b):return self.mul(a,self.inv(b))
    def power(self,a,n):
        if n<0:return self.power(self.inv(a),-n)
        z=1
        while n:
            if n&1:z=self.mul(z,a)
            n>>=1
            if n:a=self.sq(a)
        return z
    def frob(self,a,r):
        for _ in range(r):a=self.sq(a)
        return a
    def trace(self,a):
        z=0
        for _ in range(self.m):z^=a;a=self.sq(a)
        assert z in (0,1);return z
    def sqrt(self,a):return self.frob(a,self.m-1)
    def as_root(self,a):
        if self.as_piv is None:
            piv={}
            for j in range(self.m):
                b=self.sq(1<<j)^(1<<j);x=1<<j
                while b:
                    k=b.bit_length()-1
                    if k not in piv:piv[k]=(b,x);break
                    c,d=piv[k];b^=c;x^=d
            assert len(piv)==self.m-1;self.as_piv=piv
        x=0
        while a:
            k=a.bit_length()-1
            if k not in self.as_piv:return None
            b,c=self.as_piv[k];a^=b;x^=c
        return x
    def embed_f4(self):
        x=self.as_root(1);assert x is not None and x not in(0,1);return x

def selfcheck():
    rng=random.Random(12345)
    for modulus in [7,19,67,283]:
        A=BinaryField(modulus);B=BigBinaryField(modulus)
        for _ in range(1000):
            a=rng.randrange(A.q);b=rng.randrange(A.q)
            assert A.mul(a,b)==B.mul(a,b)
            assert B.sq(a)==A.mul(a,a)
            if a:assert B.inv(a)==A.inv(a)
            r=B.as_root(a)
            assert (r is None)==(a not in A.artin)
            if r is not None:assert B.sq(r)^r==a
    print('Small-field cross-checks passed:4000 exact multiplication/square/inverse/AS tests')
if __name__=='__main__':selfcheck()

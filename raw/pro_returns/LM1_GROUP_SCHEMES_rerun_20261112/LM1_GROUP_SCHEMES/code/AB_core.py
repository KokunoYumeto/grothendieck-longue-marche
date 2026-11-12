"""Exact 2 by 2 matrix arithmetic used by the A/B verification programs."""
from itertools import product
from math import gcd

def mul(a,b,n):
    x,y,z,w=a; p,q,r,s=b
    return ((x*p+y*r)%n,(x*q+y*s)%n,(z*p+w*r)%n,(z*q+w*s)%n)

def det(a,n):
    x,y,z,w=a
    return (x*w-y*z)%n

def inv(a,n):
    x,y,z,w=a
    d=pow(det(a,n),-1,n)
    return (d*w%n,-d*y%n,-d*z%n,d*x%n)

def scale(k,a,n): return tuple(k*x%n for x in a)
def sub(a,b,n): return tuple((x-y)%n for x,y in zip(a,b))
def tr(a,n): return (a[0]+a[3])%n
def ident(n): return (1%n,0,0,1%n)
def conj(a,b,n): return mul(mul(a,b,n),inv(a,n),n)
def comm(a,b,n): return mul(conj(a,b,n),inv(b,n),n)
def gl(n): return [a for a in product(range(n),repeat=4) if gcd(det(a,n),n)==1]
def sl(n): return [a for a in product(range(n),repeat=4) if det(a,n)==1]
def primes(n):
    p=2; result=[]
    while p*p<=n:
        if n%p==0:
            result.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1: result.append(n)
    return result

def regular(a,n):
    return all(a[1]%p or a[2]%p or (a[0]-a[3])%p for p in primes(n))

def transverse_unipotent(e,s,n):
    N=sub(e,ident(n),n)
    if mul(N,N,n)!=(0,0,0,0) or not regular(e,n):return False
    for p in primes(n):
        Np=tuple(v%p for v in N)
        v=(Np[0],Np[2]) if Np[0] or Np[2] else (Np[1],Np[3])
        q=inv(tuple(v%p for v in s),p)
        w=((q[0]*v[0]+q[1]*v[1])%p,(q[2]*v[0]+q[3]*v[1])%p)
        if (v[0]*w[1]-v[1]*w[0])%p==0:return False
    return True

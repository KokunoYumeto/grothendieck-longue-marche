#!/usr/bin/env python3
"""Exact dictionaries used in the harmonic-square proof, without sampling f."""
from collections import deque

def fp_mul(a,b):
    out=list(a)
    for factor,e in b:
        modulus=2 if factor=='s' else 3
        if out and out[-1][0]==factor:
            e=(out.pop()[1]+e)%modulus
        if e: out.append((factor,e))
    return tuple(out)
def fp_inv(a):
    return tuple((g,(-e)%(2 if g=='s' else 3)) for g,e in a[::-1])
def fp_pow(a,n):
    if n<0: return fp_pow(fp_inv(a),-n)
    ans=()
    for _ in range(n): ans=fp_mul(ans,a)
    return ans
def fp_conj(g,a): return fp_mul(fp_mul(g,a),fp_inv(g))
s=(('s',1),);r=(('r',1),);tau=fp_mul(s,r)
x=fp_pow(tau,-2);y=fp_conj(s,x);z=fp_inv(fp_mul(x,y))
d=fp_mul(fp_inv(x),s)
assert fp_conj(tau,x)==x
assert fp_conj(tau,y)==fp_mul(fp_inv(x),fp_inv(y))
assert fp_conj(x,fp_conj(tau,y))==z
assert fp_pow(d,2)==fp_conj(fp_inv(x),z)
assert fp_mul(x,d)==s
print('C2*C3 exact reduced words: Ad_tau(x)=x, Ad_tau(y)=x^-1 y^-1.')
print('Ad_x Ad_tau(y)=z; j(d)^2=x^-1 z x; j(vd)=s.')

# F4 elements are a+b*w, encoded a+2*b, w^2+w+1=0.
def fm(a,b):
    a0,a1=a&1,a>>1;b0,b1=b&1,b>>1
    return ((a0*b0+a1*b1)%2)+2*((a0*b1+a1*b0+a1*b1)%2)
def fp(a,n):
    ans=1
    for _ in range(n):ans=fm(ans,a)
    return ans
def am(g,h):return (g[0]^fm(g[1],h[0]),fm(g[1],h[1]))
def ap(g,n):
    if n<0:
        ui=fp(g[1],2)
        return ap((fm(ui,g[0]),ui),-n)
    ans=(0,1)
    for _ in range(n):ans=am(ans,g)
    return ans
w=2;c=2
assert fm(1^w,c)==1
S=(c,1);R=(c,w);T=am(S,R);X=ap(T,-2);Y=am(am(S,X),S)
assert ap(S,2)==(0,1) and S!=(0,1)
assert ap(R,3)==(0,1) and R!=(0,1)
assert T==(0,w) and X==(0,w) and Y==(1,w)
seen={(0,1)};queue=deque(seen)
while queue:
    a=queue.popleft()
    for b in (S,R):
        g=am(a,b)
        if g not in seen:seen.add(g);queue.append(g)
assert len(seen)==12
print('Affine quotient order 12; orders of s,r,tau,x,y are 2,3,3,3,3.')
print('Exact affine images: s=(w,1), r=(w,w), tau=x=(0,w), y=(1,w).')

def mob(M,t):
    a,b,c_,d_=M
    if t is None:
        return None if c_%3==0 else a*pow(c_%3,-1,3)%3
    denominator=(c_*t+d_)%3
    return None if denominator==0 else (a*t+b)*pow(denominator,-1,3)%3
dictionary={None:0,0:w,1:1,2:3}
for matrix,affine in (((0,-1,1,0),S),((0,-1,1,-1),R)):
    for point,value in dictionary.items():
        assert dictionary[mob(matrix,point)]==affine[0]^fm(affine[1],value)
print('P1(F3) dictionary verified at every point for S and R0: infinity->0, 0->w, 1->1, 2->w^2.')
for rho in range(9):
    V=ap(ap(T,-1),8*rho)
    assert V==(0,fp(w,rho%3))
    assert am((0,fp(w,(-rho)%3)),V)==(0,1)
print('All rho mod9: V=U^(8rho)=(0,w^rho); inverse harmonic linear part cancels it.')
assert {g for g in seen if am(g,S)==am(S,g)}=={(a,1) for a in range(4)}
# The signed SL2(F3) centralizer is cyclic order four; its projective
# image is exactly {1,S}, smaller than the projective centralizer.
def mm(A,B):return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2))%3 for i in range(2) for j in range(2))
SL={ (a,b,c_,d_) for a in range(3) for b in range(3) for c_ in range(3) for d_ in range(3) if (a*d_-b*c_)%3==1 }
SM=(0,2,1,0)
central={M for M in SL if mm(M,SM)==mm(SM,M)}
assert len(central)==4
projective=lambda M:min(M,tuple(-v%3 for v in M))
assert {projective(M) for M in central}=={projective((1,0,0,1)),projective(SM)}
print('Signed centralizer has order 4 and projective image exactly {identity,s}.')
print('ALL CHECKS PASSED')

#!/usr/bin/env python3
"""Exact finite certificate for A.54 at lambda=33 and its matrix identity."""
from fractions import Fraction
import sympy as sp
from pathlib import Path
out=[]
def valuation(x,p):
    x=Fraction(x);a=b=0
    n,d=x.numerator,x.denominator
    while n%p==0:n//=p;a+=1
    while d%p==0:d//=p;b+=1
    return a-b
m=5
lam=1+2**m
j=Fraction(256*(lam*lam-lam+1)**3,lam*lam*(1-lam)**2)
assert lam==33 and sp.factorint(lam)=={3:1,11:1}
assert valuation(j,2)==8-2*m==-2
ratio=Fraction(-8,2*m-8)
assert ratio==-4
out.append(f"lambda={lam}; j={j}; v2(j)={valuation(j,2)}; Tate valuation ratio={ratio}")
for p in [3,11]:
    for k in [1,2]:
        mod=p**k
        squares=sorted({a*a%mod for a in range(mod) if a%p})
        assert (-4)%mod not in squares
        out.append(f"p={p}, modulus={mod}: -4 mod modulus={(-4)%mod}; unit squares={squares}; excluded")
a,b,d,ch,c0,cs=sp.symbols('a b d chi c0 cs')
g=sp.Matrix([[a,b],[0,d]])
r0=sp.Matrix([[ch,c0],[0,1]])
rs=sp.Matrix([[ch,cs],[0,1]])
diff=g*r0-rs*g
assert (diff-sp.Matrix([[0,a*c0+(1-ch)*b-d*cs],[0,0]])).applyfunc(sp.expand)==sp.zeros(2)
assert sp.simplify((a/d).subs(d,1/a)-a*a)==0
out.append("Exact matrix identity: g*rho0-rhos*g has sole entry a*c0+(1-chi)*b-d*cs; ad=1 implies a/d=a^2.")
T=sp.symbols('T')
J=256*(T*T-T+1)**3/(T*T*(1-T)**2)
assert sp.limit((1/J)/(T*T),T,0)==sp.Rational(1,256)
assert sp.limit((1/J)/((1-T)**2),T,1)==sp.Rational(1,256)
out.append("Both cusps have leading coefficient 1/256 in 1/j, hence in the formal inverse Tate parameter.")
text="\n".join(out)+"\n"
Path(__file__).with_name('legendre_dyadic_certificate_output.txt').write_text(text)
print(text,end='')

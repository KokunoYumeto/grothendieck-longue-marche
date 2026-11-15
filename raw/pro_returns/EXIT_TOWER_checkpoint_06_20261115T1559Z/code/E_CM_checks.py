"""Independent finite checks for the supplied E58 CM witness.
No return code or saved word data are imported.  The existence of the
profinite witness is a separate lifting assertion, not a finite test.
"""
import json
from itertools import product
from pathlib import Path
import sympy as sp

def mul(a,b,n):
    A,B,C,D=a; E,F,G,H=b
    return ((A*E+B*G)%n,(A*F+B*H)%n,(C*E+D*G)%n,(C*F+D*H)%n)
def inv(a,n):
    A,B,C,D=a
    return (D%n,-B%n,-C%n,A%n)
def power(a,k,n):
    if k<0:return power(inv(a,n),-k,n)
    r=(1,0,0,1)
    while k:
        if k&1:r=mul(r,a,n)
        a=mul(a,a,n);k//=2
    return r
def generated(gens,n):
    I=(1,0,0,1);seen={I};todo=[I]
    while todo:
        a=todo.pop()
        for b in gens:
            c=mul(a,b,n)
            if c not in seen:seen.add(c);todo.append(c)
    return seen
def red(a,n):return tuple(t%n for t in a)
def neg(a,n):return tuple(-t%n for t in a)
def central(G,a,n):return {g for g in G if mul(g,a,n)==mul(a,g,n)}
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,11,1)
S=mul(mul(U,L,12),U,12);R=neg(mul(U,L,12),12)
x=power(U,2,12);y=power(L,2,12)
H=generated([x,y],12)
assert len(H)==96 and neg(I,12) not in H
V4={red(g,4) for g in H}; assert len(V4)==4
comm=mul(mul(mul(x,y,12),inv(x,12),12),inv(y,12),12)
z=power(comm,2,12);assert z==(5,0,0,5)
Cr=central(H,R,12);Cs=central(H,S,12)
assert len(Cr)==6 and len(Cs)==8
w=(1,2)
def eps3(a):
    a=red(a,3);v=((a[0]*w[0]+a[1]*w[1])%3,(a[2]*w[0]+a[3]*w[1])%3)
    assert v in (w,tuple(-t%3 for t in w))
    return int(v!=w)
def eps2(a):
    a=red(a,3); assert a in {power(red(S,3),j,3) for j in range(4)}
    return int(a not in {I,neg(I,3)})
counts={0:0,1:0}
for a,b in product(Cr,Cs):counts[eps3(inv(a,12))^eps2(inv(b,12))]+=1
assert counts=={0:24,1:24}
assert eps3(z)==1 and eps2(I)==0
SL3={a for a in product(range(3),repeat=4) if (a[0]*a[3]-a[1]*a[2])%3==1}
assert len(SL3)==24
assert len(central(SL3,red(R,3),3))==6
assert len(central(SL3,red(S,3),3))==4
# Symbolic CM comparisons used in the Galois-vanishing argument.
t=sp.symbols('t');sqrt3=sp.sqrt(3);rho=(1+sp.I*sqrt3)/2
legendre=sp.expand((t+(1+rho)/3)*(t+(1+rho)/3-1)*(t+(1+rho)/3-rho))
c=-(2*rho-1)/3
assert sp.simplify(legendre-(t**3+c**3))==0
assert sp.expand(64*((t+2)/4)*((t+2)/4-1)*((t+2)/4-sp.Rational(1,2)))==t**3-4*t
r0sq=sqrt3/2
assert sp.simplify(3*(sqrt3-1)**2*r0sq-((-1+sqrt3)**3+1))==0
assert sp.expand((3*t**4-6*t**2-1).subs(t**2,1+2/sqrt3))==0
assert sp.expand((3*t**4-6*t**2-1).subs(t**2,1-2/sqrt3))==0
result={
 'signed_image_order':len(H),'signed_image_mod4_order':len(V4),
 'centralizer_r_order':len(Cr),'centralizer_s_order':len(Cs),
 'frame_pairs_by_delta':counts,'commutator_square_mod12':z,
 'E58_frames':{'T':z,'W':I,'epsilon3':eps3(z),'epsilon2':eps2(I),'Delta':1},
 'CM_symbolic_identities':'all passed',
 'scope':'Finite certificate and CM identities only; no finite test certifies the profinite peripheral lifting theorem.'}
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')

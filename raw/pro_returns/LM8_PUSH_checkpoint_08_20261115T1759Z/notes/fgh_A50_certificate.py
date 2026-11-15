#!/usr/bin/env python3
"""Exact algebra, Heisenberg representation, and finite-field certificate for A.50."""
from pathlib import Path
import json
import sympy as s

x,q,y,w,T=s.symbols('x q y w T')
psiq=3*q**4-6*q*q-1
f=3*x**4-6*x*x-1
X=2*(x**3-x+q**3-q)/(x-q)**2-x-4*q
A=9-30*q*q;B=42*q-70*q**3
Yfactor=s.diff(X,x)
def remq(z):
    n,d=s.fraction(s.cancel(z))
    return s.rem(s.Poly(n,q),s.Poly(psiq,q)).as_expr()
assert remq(f-3*(x-q)**3*(X+3*q))==0
assert remq((x**3-x)*Yfactor**2-X**3-A*X-B)==0
u=s.symbols('u')
G=u**9/s.Integer(27)-q*u**6+(3-q*q)*u**3+15*q-7*q**3
assert s.expand((u**3/3-3*q)**3+A*(u**3/3-3*q)+B-G)==0
assert s.expand(3*(x*x-1)**2-f-4)==0
# Rational group-algebra Fourier intertwiner over Q(omega).
def red(z): return s.rem(s.Poly(s.expand(z),w),s.Poly(w*w+w+1,w)).as_expr()
def matred(M): return M.applyfunc(red)
U=s.diag(1,w,w*w);V=s.zeros(3)
for j in range(3):V[(j+1)%3,j]=1
U=matred(U)
M=s.Matrix(3,3,lambda j,k:red(w**((-j*k)%3)))
Fourier=matred(M*(1+2*w)/3)
assert matred(Fourier**4)==s.eye(3)
assert s.expand(Fourier.trace())==1
assert matred(Fourier*U-Fourier*0-V*Fourier)==s.zeros(3)
assert matred(Fourier*V-U**2*Fourier)==s.zeros(3)
char=red(Fourier.charpoly(T).as_expr())
assert s.expand(char-(T-1)*(T*T+1))==0
assert matred(U*V-w*V*U)==s.zeros(3)
# A noncentral order-three subgroup has one invariant in the 3D representation.
projector=matred((s.eye(3)+U+U**2)/3)
assert projector==s.diag(1,0,0)

def leg(a,p):
    a%=p
    return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)

def count(p,k):
    roots=[a for a in range(p) if (3*a**4-6*a*a-1)%p==0]
    assert len(roots)==4 and all(leg(a**3-a,p)==1 for a in roots)
    assert p%12==1 and k in roots
    c=[pow(27,-1,p),-k,3-k*k,15*k-7*k**3]
    def g(v):return (c[0]*pow(v,9,p)+c[1]*pow(v,6,p)+c[2]*pow(v,3,p)+c[3])%p
    polynomial=s.Poly(sum(c[i]*u**(9-3*i) for i in range(4)),u,modulus=p)
    assert s.gcd(polynomial,polynomial.diff()).degree()==0
    N1=1+sum(1+leg(g(v),p) for v in range(p))
    aE=-sum(leg(v**3-v,p) for v in range(p))
    a0=-sum(leg(v**3+108,p) for v in range(p))
    d=next(i for i in range(2,p) if leg(i,p)==-1)
    def mul(a,b):return ((a[0]*b[0]+d*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
    def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    def scale(a,n):return (a[0]*n%p,a[1]*n%p)
    def pw(a,n):
        z=(1,0)
        while n:
            if n&1:z=mul(z,a)
            a=mul(a,a);n//=2
        return z
    def leg2(a):
        if a==(0,0):return 0
        z=pw(a,(p*p-1)//2)
        assert z in [(1,0),(p-1,0)]
        return 1 if z==(1,0) else -1
    N2=1
    for aa in range(p):
        for bb in range(p):
            v3=pw((aa,bb),3);v6=mul(v3,v3);v9=mul(v3,v6)
            val=add(add(scale(v9,c[0]),scale(v6,c[1])),add(scale(v3,c[2]),(c[3]%p,0)))
            N2+=1+leg2(val)
    s1=p+1-N1-aE-a0
    s2=p*p+1-N2-(aE*aE-2*p)-(a0*a0-2*p)
    e2=(s1*s1-s2)//2
    assert (s1*s1-s2)%2==0
    a=-s1
    assert e2==a*a-p and a==11 and a%p!=0
    P=T**4+a*T**3+(a*a-p)*T*T+p*a*T+p*p
    W=T*T-a*T+p
    disc=a*a-4*p
    # Formal identity for the third-power Frobenius polynomial.
    Z=s.symbols('Z')
    resultant=s.resultant(P,Z-T**3,T)
    expected=(Z*Z-(a**3-3*p*a)*Z+p**3)**2
    assert s.expand(resultant-expected)==0
    return {'prime':p,'kernel_x':k,'all_nonzero_three_torsion_x':roots,'quadratic_extension_nonsquare':d,'N1_genus_four':N1,'N2_genus_four':N2,'trace_original_elliptic':aE,'trace_j0_elliptic':a0,'surface_polynomial_coefficients':s.Poly(P,T).all_coeffs(),'elliptic_cubic_root_trace':a,'ordinary_imaginary_quadratic_discriminant':disc,'third_power_elliptic_trace':a**3-3*p*a,'curve_polynomial_separable':True}
rows=[count(61,4),count(313,26)]
assert rows[0]['ordinary_imaginary_quadratic_discriminant']==-123
assert rows[1]['ordinary_imaginary_quadratic_discriminant']==-1131
assert s.Rational(123,1131)==s.Rational(41,377)
assert not s.sqrt(s.Rational(41,377)).is_Rational
res={'status':'PASS','scope':'Exact identities and finite certificate supporting the unbounded arithmetic proof; no count is used alone to assert non-CM.','degree':27,'genus':10,'cusps':9,'CM_quotient_degree':4,'punctured_CM_map_degree':12,'division_polynomial_lift_identity':True,'Velu_isogeny_identity':True,'genus_four_quotient_identity':True,'Fourier_intertwiner_characteristic_polynomial':str(char),'Fourier_intertwiner':[[str(v) for v in Fourier.row(i)] for i in range(3)],'noncentral_projector_rank':1,'counts':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2,default=int)+'\n')
print('PASS: actual division-polynomial cover and quotient identities, Heisenberg Fourier matrix, two full quadratic-extension point counts, and Frobenius power identities.')
for row in rows: print(json.dumps(row,default=int),flush=True)
print('The ordinary fields Q(sqrt(-123)) and Q(sqrt(-1131)) differ and persist under every positive Frobenius power.')

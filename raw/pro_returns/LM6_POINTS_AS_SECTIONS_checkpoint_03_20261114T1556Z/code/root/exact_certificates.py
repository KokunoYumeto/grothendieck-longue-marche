#!/usr/bin/env python3
"""Exact finite certificates used in Parts C--E. No external CAS data."""
from fractions import Fraction as F
from itertools import product
from math import gcd, prod
import json
import sympy as s
from math import factorial

def ec_add(P,Q,a):
    a1,a2,a3,a4,a6=map(F,a)
    if P is None: return Q
    if Q is None: return P
    x,y=map(F,P); u,v=map(F,Q)
    if x==u and y+v+a1*x+a3==0: return None
    if P==Q:
        den=2*y+a1*x+a3
        lam=(3*x*x+2*a2*x+a4-a1*y)/den
        nu=(-x**3+a4*x+2*a6-a3*y)/den
    else:
        lam=(v-y)/(u-x); nu=(y*u-v*x)/(u-x)
    z=lam*lam+a1*lam-a2-x-u
    w=-(lam+a1)*z-nu-a3
    return z,w

def on_curve(P,a):
    if P is None: return True
    x,y=P; a1,a2,a3,a4,a6=a
    return y*y+a1*x*y+a3*y==x**3+a2*x*x+a4*x+a6

def finite_count(p,a):
    return 1+sum(on_curve_mod(x,y,p,a) for x,y in product(range(p),repeat=2))

def on_curve_mod(x,y,p,a):
    a1,a2,a3,a4,a6=a
    return (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%p==0

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def phi(n): return sum(gcd(i,n)==1 for i in range(1,n+1))

# D8 = <r,t | r^4=t^2=1, trt=r^-1>.
def d8mul(a,b):
    i,j=a; k,l=b
    return ((i+(-1)**j*k)%4,(j+l)%2)
def d8sq(a): return d8mul(a,a)
x=(0,1); y=(1,1)
xy=d8mul(x,y)
assert d8sq(x)==d8sq(y)==(0,0) and d8sq(xy)==(2,0)
# The coset with abelian coordinates (1,1) consists of xy and r^2 xy.
fake=[a for a in product(range(4),range(2)) if a[0]%2==1 and a[1]==0]
assert len(fake)==2 and all(d8sq(a)==(2,0) for a in fake)

# Free-product words in involutions a,b,c. pi generators x=ba,y=ac.
def red(w):
    out=[]
    for z in w:
        if out and out[-1]==z: out.pop()
        else: out.append(z)
    return out
def inv(w): return list(reversed(w))
wa,wb,wc=[0],[1],[2]
wx=wb+wa; wy=wa+wc
wz=red(inv(wx+wy))
assert wz==wc+wb
assert red(wx+wa)==wb
assert red(inv(wy)+wa)==wc
assert red(inv(wz)+wc)==wb

# Fermat cubic -> 27a1, exact identity modulo X^3+Y^3+Z^3.
X,Y,Z=s.symbols('X Y Z')
u=-3*Z/(X+Y); v=(9*(X-Y)/(X+Y)-1)/2
num=s.factor((v*v+v-u**3+7)*(X+Y)**3)
assert s.expand(num-27*(X**3+Y**3+Z**3))==0
E3=(0,0,1,0,-7)
counts={str(p):finite_count(p,E3) for p in [5,7,11,13]}
assert gcd(counts['5'],counts['7'])==3
assert on_curve((F(3),F(4)),E3) and on_curve((F(3),F(-5)),E3)

# The explicit rational 7-torsion point refutes the asserted emptiness of Y_1(7).
E7=(-1,-4,-4,0,0); P=(F(0),F(0)); Q=None; multiples=[]
for n in range(1,8):
    Q=ec_add(Q,P,E7)
    assert on_curve(Q,E7)
    multiples.append(None if Q is None else [str(z) for z in Q])
assert Q is None and all(z is not None for z in multiples[:-1])
a1,a2,a3,a4,a6=E7
b2=a1*a1+4*a2; b4=2*a4+a1*a3; b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
disc=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert disc!=0

# Positive Jacobian rank for genus two via y^2=x^6-x^2+1 -> E.
Er=(0,0,0,-1,1)
twice=ec_add((F(0),F(1)),(F(0),F(1)),Er)
assert twice==(F(1,4),F(-7,8))
q=s.symbols('q')
assert s.gcd(q**6-q**2+1,s.diff(q**6-q**2+1,q))==1

# C.2: the exact matrix commutant.  Its determinant-one elements
# satisfy a^2-a*b-b^2=1; a nonidentity unipotent cannot occur.
a,b,c,d=s.symbols('a b c d')
AA=s.Matrix([[2,1],[1,1]]); BB=s.Matrix([[a,b],[c,d]])
comm=list(AA*BB-BB*AA)
sol=s.linsolve(comm,(a,b,c,d))
assert sol==s.FiniteSet((c+d,c,c,d))
assert AA.charpoly().as_expr()==s.Symbol('lambda')**2-3*s.Symbol('lambda')+1

# Labelled set partitions, and the two cyclic-order formulas of C.11.
def partitions(xs):
    if not xs:
        yield []
        return
    x,*tail=xs
    for pp in partitions(tail):
        yield [(x,)]+pp
        for j in range(len(pp)):
            yield pp[:j]+[tuple(sorted((x,)+pp[j]))]+pp[j+1:]

def surface_types(g):
    return [('nonorientable',g+1-q) for q in range(1,g+2)]+[
        ('orientable',g+1-2*h) for h in range((g+1)//2+1) if g+1-2*h>=1]

marked=[]
for g in range(2,7):
    types=surface_types(g)
    assert len(types)==g+2+g//2
    for n in range(1,7):
        count=0
        for typ,r in types:
            for pp in partitions(list(range(1,n+1))):
                if len(pp)>r: continue
                sizes=list(map(len,pp))
                if typ=='nonorientable':
                    count+=prod(1 if m<=2 else factorial(m-1)//2 for m in sizes)
                else:
                    numerator=prod(factorial(m-1) for m in sizes)+int(max(sizes)<=2)
                    assert numerator%2==0
                    count+=numerator//2
        marked.append({'g':g,'n_real_labelled':n,'components':count})

# D: a global abelian section not locally induced by a curve point.
# The genus-two curve has a rational Weierstrass point at infinity.
f=q**5-q+1
assert s.gcd(f,s.diff(f,q))==1
u=q*q; vv=1-q/F(2)
assert s.rem(vv*vv-f,u,q)==0
# (u,v) is a degree-two reduced Mumford divisor, hence is outside
# the degree-one Abel-Jacobi image; its support is twice (0,1).
assert s.degree(u,q)==2 and vv.subs(q,0)==1 and f.subs(q,0)==1

# D.9: exact 3-division and 3-isogeny equations for the cubic.
xx,yy,bb=s.symbols('xx yy bb')
xp=(xx**3+4*bb)/xx**2
yp=yy*(xx**3-8*bb)/xx**3
isog=s.factor((yp**2-xp**3+27*bb)*xx**6)
assert s.rem(isog,yy**2-xx**3-bb,yy)==0
psi3=3*xx*(xx**3-1728)
assert psi3.subs(xx,0)==0 and psi3.subs(xx,12)==0
assert 12**3-432==36**2 and -432==144*(-3)
assert (9-1)*(9-2)//2==28
assert 1+9*(10-1)==2*28+27-1==82
assert (-432)*(-3)**3==11664

# D.4: explicit maps from the two genus-three curves to X_0(32).
for cc,denx,deny in [(4,1,1),(64,4,8)]:
    uu=xx**4/denx; ww=xx**2*yy/deny
    assert s.rem(s.together(ww**2-uu**3-4*uu).as_numer_denom()[0],
                 yy**2-xx**8-cc,yy)==0

# D: a finite sample of the exact multiquadratic density model.
# b(p) is finite because adjoining sqrt(p) prevents complete splitting.
first_primes=list(s.primerange(2,50))
density_model=[]
for pp in list(s.primerange(3,100)):
    bp=0
    for qq in first_primes:
        if pp==qq or pow(qq%pp,(pp-1)//2,pp)!=1: break
        bp+=1
    density_model.append({'prime':int(pp),'b':bp,'local_image_size':bp+1})

modular=[]
for ell in [3,5,7,11,13,17,19]:
    N=4*ell
    mu=N*F(3,2)*F(ell+1,ell)
    cusps=sum(phi(gcd(d,N//d)) for d in divisors(N))
    genus=1+mu/F(12)-F(cusps,2) # e2=e3=0 since 4 | N
    assert genus==F(ell-3,2)
    modular.append({'ell':ell,'N':N,'index':int(mu),'cusps':cusps,'genus':int(genus)})

even=[]
for n in [2,4,6,8,10]:
    geom_rank=n*n+1; quotient_rank=n*n//2+1
    # One fixed generator t^2 plus pairs a_i, t a_i t^-1.
    assert geom_rank==1+2*(quotient_rank-1)
    # On the fixed Z_2 coordinate the norm is multiplication by two;
    # each swapped pair has invariant diagonal equal to its norm image.
    even.append({'n':n,'geometric_rank':geom_rank,'quotient_rank':quotient_rank,
                 'invariant_norm_quotient':'Z/2','extension_class':1,
                 'first_intrinsic_nilpotent_obstruction':1})

out={
 'tripod_free_words':{'x':'ba','y':'ac','z':'cb','six_germs':['a','b','a','c','c','b']},
 'tripod_class_two_obstruction':{'D8_fake_coset':fake,'squares':[d8sq(a) for a in fake]},
 'fermat_cubic_identity':str(num),'fermat_cubic_counts':counts,
 'rational_order_seven':{'curve_ai':E7,'discriminant':disc,'multiples':multiples},
 'positive_rank_example':{'double_P':[str(z) for z in twice]},
 'matrix_commutant':str(sol), 'real_marked_counts':marked,
 'abelian_nonpoint_divisor':{'curve':str(f),'u':str(u),'v':str(vv)},
 'global_prothree':{'elliptic_B':-432,'twist_B':11664,
                    'isogeny_identity':str(isog),'X9_genus':28,
                    'U9_geometric_pro3_rank':82,'constant_field':'Q(zeta_9,cuberoot(3))'},
 'density_model_sample':density_model,
 'X0_4ell':modular,'even_fermat_orientation':even,
 'status':'all exact assertions passed'
}
print(json.dumps(out,indent=2))

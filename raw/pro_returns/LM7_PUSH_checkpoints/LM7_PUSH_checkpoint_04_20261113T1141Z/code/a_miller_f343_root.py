#!/usr/bin/env python3
"""Exact 9-torsion and Miller functions at 7 for the Fermat cubic.

Arithmetic input to the active finite-cover investigation. This program
does not infer a central Galois cochain from abelian or divisor data.
All fields, group operations, and function identities are exact.
"""
from itertools import product
from pathlib import Path
import json
import sympy as sp


class F:
    __slots__ = ('v',)

    def __init__(self, v=0):
        self.v = v.v if isinstance(v, F) else ((v % 7, 0, 0)
                   if isinstance(v, int) else tuple(int(a) % 7 for a in v))

    def __add__(self, other):
        other = F(other)
        return F(tuple(a+b for a,b in zip(self.v, other.v)))

    __radd__ = __add__

    def __neg__(self):
        return F(tuple(-a for a in self.v))

    def __sub__(self, other):
        return self + -F(other)

    def __rsub__(self, other):
        return F(other) + -self

    def __mul__(self, other):
        other = F(other)
        c = [0]*5
        for i,a in enumerate(self.v):
            for j,b in enumerate(other.v):
                c[i+j] += a*b
        # theta^3=2, irreducible over F_7.
        c[1] += 2*c[4]
        c[0] += 2*c[3]
        return F(c[:3])

    __rmul__ = __mul__

    def __pow__(self, n):
        if n < 0:
            assert self
            return self**((343-1)-((-n) % (343-1)))
        out, a = F(1), self
        while n:
            if n & 1:
                out *= a
            a *= a
            n >>= 1
        return out

    def __truediv__(self, other):
        other = F(other)
        assert other
        return self*(other**341)

    def __rtruediv__(self, other):
        return F(other)/self

    def __bool__(self):
        return any(self.v)

    def __eq__(self, other):
        return self.v == F(other).v

    def __hash__(self):
        return hash(self.v)

    def __repr__(self):
        return str(self.v)


Z, ONE, THETA = F(0), F(1), F((0,1,0))
assert THETA**3 == 2
assert all(F(a)**3 != 2 for a in range(7))
FIELD = [F(v) for v in product(range(7), repeat=3)]
assert all(a**343 == a for a in FIELD)

# Minimal model y^2+y=x^3-7. Its reduction at 7 is y^2+y=x^3.
A6 = F(-7)

def neg(P):
    return None if P is None else (P[0], -P[1]-1)

def add(P,Q):
    if P is None:
        return Q
    if Q is None:
        return P
    x,y = P
    u,v = Q
    if x == u and y+v == -1:
        return None
    lam = (3*x*x)/(2*y+1) if P == Q else (v-y)/(u-x)
    nu = y-lam*x
    xx = lam*lam-x-u
    return xx, -lam*xx-nu-1

def times(n,P):
    if n < 0:
        return times(-n,neg(P))
    ans = None
    while n:
        if n & 1:
            ans = add(ans,P)
        P=add(P,P)
        n >>= 1
    return ans

def frob(P):
    return None if P is None else tuple(a**7 for a in P)

ys = {}
for y in FIELD:
    ys.setdefault(y*y+y,[]).append(y)
points=[None]+[(x,y) for x in FIELD for y in ys.get(x**3+A6,[])]
assert len(points) == 324
E9=[P for P in points if times(9,P) is None]
E3=[P for P in E9 if times(3,P) is None]
assert len(E9) == 81 and len(E3) == 9
assert all(frob(P)==P for P in E3)
assert all(frob(frob(frob(P)))==P for P in E9)
assert all(times(3, add(frob(P),neg(P))) is None for P in E9)
QC = F(3),F(4)
PC = F(3),F(-5)
assert times(3,QC) is None and PC == neg(QC)
roots=[(name,D,P) for name,D in [('P',PC),('Qc',QC)]
       for P in E9 if times(3,P)==D]
assert len(roots)==18 and all(frob(P)!=P for _,_,P in roots)

# Polynomial arithmetic over the exact field, in ascending degree.
def clean(a):
    a=list(map(F,a))
    while len(a)>1 and not a[-1]:
        a.pop()
    return tuple(a)

PZERO=(Z,)
PONE=(ONE,)
PX=(Z,ONE)

def padd(a,b):
    return clean([(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z)
                  for i in range(max(len(a),len(b)))])

def pneg(a):
    return tuple(-x for x in a)

def pmul(a,b):
    c=[Z]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return clean(c)

def ppow(a,n):
    ans=PONE
    for _ in range(n):
        ans=pmul(ans,a)
    return ans

def vertical(P):
    assert P is not None
    return (-P[0], ONE)

# A function numerator is A(x)+B(x)y; y^2=x^3-7-y.
CURVE=(A6,Z,Z,ONE)
FUNONE=(PONE,PZERO)

def nmul(a,b):
    A,B=a
    C,D=b
    BD=pmul(B,D)
    return (padd(pmul(A,C),pmul(BD,CURVE)),
            padd(padd(pmul(A,D),pmul(B,C)),pneg(BD)))

def nscale(a,p):
    return pmul(a[0],p),pmul(a[1],p)

def npow(a,n):
    ans=FUNONE
    for _ in range(n):
        ans=nmul(ans,a)
    return ans

def line(P,Q):
    assert P is not None and Q is not None and P!=neg(Q)
    x,y=P
    u,v=Q
    lam=(3*x*x)/(2*y+1) if P==Q else (v-y)/(u-x)
    nu=y-lam*x
    return ((-nu,-lam),PONE),lam,nu

def miller3(Q):
    Q2=times(2,Q)
    D=times(3,Q)
    L1,lam1,nu1=line(Q,Q)
    L2,lam2,nu2=line(Q2,Q)
    return (nmul(L1,L2),pmul(vertical(Q2),vertical(D))), (lam1,nu1,lam2,nu2)

def conjugate_numerator(a):
    A,B=a
    return padd(A,pneg(B)),pneg(B)

def normline(L):
    n=nmul(L,conjugate_numerator(L))
    assert n[1]==PZERO
    return n[0]

def fmul(f,g):
    return nmul(f[0],g[0]),pmul(f[1],g[1])

def feq(f,g):
    return nscale(f[0],g[1]) == nscale(g[0],f[1])

def encP(P):
    return None if P is None else [list(a.v) for a in P]

records=[]
for label,target,Q in roots:
    Q2=times(2,Q)
    (num,den),coeff=miller3(Q)
    L1,_,_=line(Q,Q)
    L2,_,_=line(Q2,Q)
    # Exact line intersection polynomials; these certify the divisor.
    assert normline(L1)==pneg(pmul(ppow(vertical(Q),2),vertical(Q2)))
    assert normline(L2)==pneg(pmul(pmul(vertical(Q),vertical(Q2)),vertical(target)))
    involution_norm=nmul(num,conjugate_numerator(num))
    assert involution_norm[1]==PZERO
    assert pmul(involution_norm[0],vertical(target))==pmul(ppow(vertical(Q),3),ppow(den,2))
    orbit=[Q,frob(Q),frob(frob(Q))]
    D=add(add(orbit[0],orbit[1]),orbit[2])
    assert D==target
    Q01=add(orbit[0],orbit[1])
    l01,_,_=line(orbit[0],orbit[1])
    l012,_,_=line(Q01,orbit[2])
    g=(nmul(l01,l012),pmul(vertical(Q01),vertical(target)))
    normf=(FUNONE,PONE)
    for R in orbit:
        normf=fmul(normf,miller3(R)[0])
    gcube=(npow(g[0],3),ppow(g[1],3))
    assert feq(normf,gcube)
    # g is defined over F_7, as its divisor and t-leading coefficient predict.
    g7=(tuple(tuple(a**7 for a in p) for p in g[0]),
        tuple(a**7 for a in g[1]))
    assert feq(g,g7)
    records.append({'target_cusp':label,'Q':encP(Q),'twice_Q':encP(Q2),'three_Q':encP(target),
                    'frobenius_orbit':[encP(R) for R in orbit],
                    'frobenius_translation':encP(add(frob(Q),neg(Q))),
                    'miller_line_coefficients':[list(a.v) for a in coeff],
                    'line_divisor_identities_verified':True,
                    'elliptic_involution_norm_verified':True,
                    'frobenius_norm_is_exact_cube':True,
                    'norm_cube_root_defined_over_F7':True})

# Characteristic-zero tangent constants are retained before reduction.
# x_min=-3*s/(1+y_F), y_min=(4-5*y_F)/(1+y_F),
# y_F=-(1+s^3)^(1/3). Hence x_min~9/s^2, y_min~-27/s^3,
# t_min=-x_min/y_min~s/3 and f_(3,Q)~t_min^-2.
# The isomorphic large model is X=4*x_min,Y=8*y_min+4.
s,eta=sp.symbols('s eta')
xmin=-3*s/(1+eta)
ymin=(4-5*eta)/(1+eta)
identity=sp.cancel((ymin**2+ymin-xmin**3+7)*(1+eta)**3)
assert sp.expand(identity-27*(1+eta**3+s**3))==0
eta_series=-1-s**3/3+s**6/9
assert sp.limit(s**2*xmin.subs(eta,eta_series),s,0)==9
assert sp.limit(s**3*ymin.subs(eta,eta_series),s,0)==-27
assert sp.limit((-xmin/ymin/s).subs(eta,eta_series),s,0)==sp.Rational(1,3)
# The two small geometric unit detectors, in the selected embedding zeta=2.
zeta=F(2)
assert zeta**3==1 and zeta!=1
assert F(9)**2==zeta**2 and F(36)**2==1
unit_x_values=[F(3),3*zeta**2]
unit_zeros=[]
for xx in unit_x_values:
    zeros=[P for P in E3 if P is not None and P[0]==xx]
    assert len(zeros)==2 and zeros[0]==neg(zeros[1])
    unit_zeros.append([encP(P) for P in zeros])
out={'field':'F7[theta]/(theta^3-2)',
     'minimal_model_over_Q':'y^2+y=x^3-7',
     'large_model_over_Q':'Y^2=X^3-432, X=4x, Y=8y+4',
     'fermat_map':{'x_min':'-3*z/(x_F+y_F)',
                   'y_min':'(4*x_F-5*y_F)/(x_F+y_F)'},
     'point_counts':{'E_F343':324,'E9':81,'E3':9,
                     'preimages_P_under_3':9,'preimages_Qc_under_3':9},
     'minimal_model_cusps':{'P':[3,-5],'Qc':[3,4]},
     'miller_divisor':'3(Q)-([3]Q)-2(O)',
     'tangent_constants_over_Q':{'f_min_times_s_squared':9,
                                 'f_large_times_s_squared':36,
                                 'f_large_over_f_min':4},
     'tangent_constants_mod7':{'minimal':2,'large':1},
     'tangent_cubic_residue_mod7':{'embedding_zeta':2,
                                 'minimal_constant9':4,
                                 'large_constant36':1},
     'unit_detectors':{'embedding_zeta_mod7':2,
                       'functions_minimal':['x-3','x-3*zeta^2'],
                       'zero_divisors_mod7':unit_zeros,
                       'regularized_at_Fermat_O_over_Q':9},
     'records':records,
     'scope':'Exact finite-field torsion, Miller-divisor and Frobenius norm identities. No intrinsic central Galois cochain or Heisenberg descent is inferred.',
     'status':'PASS'}
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

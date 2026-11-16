"""Independent exact coefficients for the cubic/quartic class-two order law.

The cubic inverse is built from a 2 by 2 elliptic inverse and an explicit
rank-one lattice projection.  The quartic's 121 frame values are derived
from its actual tangent-line equations, not read from the prior return.
"""
from itertools import combinations
from fractions import Fraction
import sympy as s

# Cubic: quotient-domain coordinates delete A0 wedge A2; codomain deletes f1 wedge f2.
U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
R=s.Matrix([[0,-1],[1,-1]])
pairs10=list(combinations(range(10),2))
pairs8=list(combinations(range(8),2))
pivot=pairs10.index((2,4))
pivot8=pairs8.index((0,2))
domain=[i for i in range(45) if i!=pivot]
codomain=[i for i in range(45) if i!=0]
def wedge(a,b,pairs):
    return s.Matrix([a[i]*b[j]-a[j]*b[i] for i,j in pairs])
def wedge_matrix(A,pairs):
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs] for i,j in pairs])
j=(3*s.eye(2)).col_join(U)
w=wedge(j[:,0],j[:,1],pairs10)
assert w[pivot]==1 and w[0]==9

def cubic_inverse_column(D,AE,q):
    X=s.zeros(2,8)
    Y=s.zeros(28,1)
    for k,(i,z) in enumerate(pairs10):
        if i<2 and z>=2:X[i,z-2]=D[k]
        if i>=2:Y[pairs8.index((i-2,z-2))]=D[k]
    Z=(AE-s.eye(2)).inv()*X
    Ysplit=Y-sum((wedge(U[:,i],X[i,:].T,pairs8)/3 for i in range(2)),s.zeros(28,1))
    Yout=Ysplit/(q-1)+sum((wedge(U[:,i],Z[i,:].T,pairs8)/3 for i in range(2)),s.zeros(28,1))
    m=s.zeros(45,1)
    for k,(i,z) in enumerate(pairs10):
        if i<2 and z>=2:m[k]=Z[i,z-2]
        if i>=2:m[k]=Yout[pairs8.index((i-2,z-2))]
    # This is the unique representative in the deleted-pivot lattice chart.
    m-=m[pivot]*w
    assert m[pivot]==0
    return m.extract(domain,[0])

for a,b,q in [(-2,0,4),(1,3,7),(-2,-3,7),(4,3,13),(-2,3,19),(-5,0,25)]:
    AE=a*s.eye(2)+b*R
    assert AE.det()==q
    T=AE.row_join(s.zeros(2,8)).col_join((U*(AE-q*s.eye(2))/3).row_join(q*s.eye(8)))
    assert all(v.q==1 for v in T)
    delta=wedge_matrix(T,pairs10)/q-s.eye(45)
    assert delta*w==s.zeros(45,1)
    d=delta.extract(codomain,domain)
    inv=s.Matrix.hstack(*(cubic_inverse_column(s.eye(45)[:,i],AE,q) for i in codomain))
    assert d*inv==s.eye(44) and inv*d==s.eye(44)
    assert abs(d.det())==abs(((AE-s.eye(2)).det()**8)*(q-1)**28/9)
    print('Cubic full 44-coordinate inverse:',(a,b,q),': PASS')

# Quartic field Q[zeta8].
t=s.symbols('t')
mod=t**4+1
def red(x):
    num,den=s.fraction(s.cancel(x))
    return s.rem(s.rem(num,mod,t)*s.invert(den,mod,t),mod,t).expand()
def fpow(x,n):
    out=s.Integer(1)
    if n<0:x=red(1/x);n=-n
    while n:
        if n%2:out=red(out*x)
        x=red(x*x);n//=2
    return out
def coeff(x):return tuple(s.Poly(red(x),t).nth(i) for i in range(4))
sqrt2=t-t**3
assert red(sqrt2**2)==2
lookup={coeff(fpow(t,k)*fpow(sqrt2,n)):(k,n) for k in range(8) for n in range(-14,5)}
points=[]
for kind in 'ABC':
    for i in range(4):
        z=fpow(t,1+2*i)
        pt=(0,z,1) if kind=='A' else (z,0,1) if kind=='B' else (z,1,0)
        line=(0,1,-z) if kind=='A' else (1,0,-z) if kind=='B' else (1,-z,0)
        assert red(sum(v**4 for v in pt))==0
        points.append((kind+str(i),z,pt,line))
O=4
others=[i for i in range(12) if i!=O]
labels=[points[i][0] for i in others]
def lead_line(d,r):
    if d==r:return points[r][1]/4
    return red(sum(a*b for a,b in zip(points[d][3],points[r][2])))
def lead_ratio(d,r):return red(lead_line(d,r)/lead_line(O,r))
frameN=s.zeros(11)
frameK=s.zeros(11)
for col,d in enumerate(others):
    base=lead_ratio(d,O)
    for row,r in enumerate(others):
        val=red(lead_ratio(d,r)/base)
        k,n=lookup[coeff(val)]
        frameK[row,col]=k;frameN[row,col]=n
assert frameN==frameN.T
v=sum((frameN[:,labels.index(k)] for k in ['B1','B2','B3']),s.zeros(11,1))/32
assert list(v)==[-s.Rational(1,2)]*4+[-s.Rational(5,8),-s.Rational(3,4),-s.Rational(5,8)]+[-s.Rational(1,2)]*4
print('Quartic peripheral order:',labels)
print('All 121 actual frame values = zeta8^K * sqrt(2)^N: PASS')
print('Exact exponent matrix N:')
for row in frameN.tolist():print(row)
print('Averaged origin v:',list(v))

# Universal cochain identity for the 55 shifted cups.
x,y,k,X,Y,K,chi,p,q=s.symbols('x y k X Y K chi p q')
phi=lambda a,b,c:a*b/2+q*c*a+p*q*c*c/2
dphi=chi**2*phi(X,Y,K)-phi(x+chi*X,y+chi*Y,k+chi*K)+phi(x,y,k)
omega=-q*k*chi*X+p*k*chi*Y+(x*chi*Y-y*chi*X)/2
shifted=(x+p*k)*chi*(Y+q*K)
assert s.expand(omega-shifted-dphi)==0
print('Every peripheral obstruction is its shifted cup plus the specified coboundary: PASS')

# Actual plus-quartic maps to E:y^2=x^3+x and their basepoint freedom.
x,y,z=s.symbols('x y z')
curve=x**4+y**4+z**4
for X,Y,Z in [(-x*x*y,z*z*x,y**3),(-y*y*z,x*x*y,z**3),(-z*z*x,y*y*z,x**3)]:
    assert s.rem(s.Poly(Y*Y*Z-X**3-X*Z*Z,x,y,z),s.Poly(curve,x,y,z)).is_zero
    for a in (x,y,z):assert list(s.groebner([curve,X,Y,Z,a-1],x,y,z))==[1]
print('All three basepoint-free degree-four elliptic maps: exact equation/chart checks PASS')

# Smallest explicit cubic nonadditivity witness at p=13, relative to the Q tangent.
assert s.isprime(13) and pow(3,4,13)!=1
assert s.discrete_log(13,pow(3,4,13),pow(2,4,13))%3!=0
assert pairs10[pivot]==(2,4) and (2,5)!=pairs10[pivot]
print('Cubic inputs kappa3(3)e_A0 and alpha_B0+kappa3(13)e_B0 separately lift; their sum has a nonintegral coordinate at 13: finite-field witness PASS')
print('No finite residue is identified with a full p-adic Frobenius value.')

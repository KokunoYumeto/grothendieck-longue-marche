"""Exact coefficient normalization for the Ross cup-edge comparison.

Construct the 54 Fermat automorphisms using projective sixth-root
exponents, average their action on H tensor wedge^2 W, and verify
the contraction matrix and its rank.  Also check the rational
isomorphism used in Ito's Theorem 3.3 and its inverse.
"""
from itertools import permutations,combinations
import sympy as s

def normalize(v):
    offset=next(t for t in v if t is not None)
    return tuple(None if t is None else (t-offset)%6 for t in v)
pts=[]
for i in range(3):pts.append(normalize((None,3+2*i,0)))
for i in range(3):pts.append(normalize((3+2*i,None,0)))
for i in range(3):pts.append(normalize((3+2*i,0,None)))
assert len(set(pts))==9
R=s.Matrix([[0,-1],[1,-1]])
pairs=list(combinations(range(8),2))
def wedge2(W):
    return s.Matrix([[W[i,k]*W[j,l]-W[i,l]*W[j,k]
                      for k,l in pairs] for i,j in pairs])
total=s.zeros(56)
images=set()
for p in permutations(range(3)):
    sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    subtotal=s.zeros(56)
    for a in range(3):
        for b in range(3):
            d=(2*a,2*b,0)
            perm=[]
            for v in pts:
                out=normalize(tuple(None if v[p[i]] is None else v[p[i]]+d[i] for i in range(3)))
                perm.append(pts.index(out))
            images.add(tuple(perm))
            W=s.zeros(8)
            for j in range(8):
                if perm[j]==8:
                    for i in range(8):W[i,j]=-1
                else:W[perm[j],j]=1
            H=sign*R**(a+b)
            subtotal+=s.kronecker_product(H,wedge2(W))
    total+=subtotal
assert len(images)==54
assert total*total==54*total
assert s.trace(total)==108
projector=total/54
f=[0,0,0,3,0,0,-1,-1]
h=[3,0,0,0,0,0,-1,-1]
b=s.Matrix([[f[i]*h[j]-f[j]*h[i] for i,j in pairs]])
contract=s.diag(b,b)
seeds=[pairs.index((0,3)),pairs.index((0,4))]
columns=projector[:,seeds]
answer=contract*columns
assert answer==s.Matrix([[-s.Rational(1,3),s.Rational(1,3)],[0,s.Rational(1,3)]])
assert answer.det()==-s.Rational(1,9)
assert projector.rank()==2
assert columns.rank()==2
integral_lift=18*columns*answer.inv()
assert all(t.q==1 for t in integral_lift)
assert contract*integral_lift==18*s.eye(2)
print('Automorphisms:',len(images),'; invariant H tensor wedge^2 W rank:',projector.rank())
print('Contraction matrix on averaged A0^B0, A0^B1 seeds:',answer.tolist())
print('Exact determinant:',answer.det())
print('Integral numerator identity Pnum^2=54 Pnum: PASS')
print('Integral inverse scaling: contraction composed with i = 18 I2: PASS')

CE=s.Matrix([[1,-1],[0,-1]])
AE=s.eye(2)+3*R
MT=7*AE
MC=-CE
fixed=s.Matrix([1,2])
assert MC*fixed==fixed
relation=(MT-s.eye(2))*fixed
assert relation==s.Matrix([-36,-9])
assert (s.Matrix([[1,-4]])*relation)[0]==0
comm=CE*AE*CE*AE.inv()-s.eye(2)
inverse9=s.Matrix([[-5,1],[-1,-4]])
assert comm*inverse9==9*s.eye(2)
assert comm.det()==s.Rational(27,7)
print('H1(Gamma,H(1)) relation:',list(relation),'= -9*(4,1); detector (1,-4).')
print('[c,tau]-1 on H(1):',comm.tolist())
print('9*([c,tau]-1)^-1:',inverse9.tolist())
print('Every equivariant image in a cyclotomic-action module is killed by 9: PASS.')

u,v,x,y=s.symbols('u v x y')
fx=3*v/(1-u)
fy=9*(1+u)/(2*(1-u))
num=s.factor(s.together(fy**2-fx**3+s.Rational(27,4)))
assert s.cancel(num/(u**3+v**3-1)-27/(u-1)**3)==0
iu=(2*y-9)/(2*y+9)
iv=6*x/(2*y+9)
assert s.cancel(iu.subs(y,fy)-u)==0
assert s.cancel(iv.subs({x:fx,y:fy},simultaneous=True)-v)==0
assert s.cancel(fx.subs({u:iu,v:iv},simultaneous=True)-x)==0
assert s.cancel(fy.subs(u,iu)-y)==0
print('Ito curve map: (u,v) -> (3v/(1-u),9(1+u)/(2(1-u)))')
print('Inverse: (x,y) -> ((2y-9)/(2y+9),6x/(2y+9))')
print('Curve identity and both rational inverse compositions: PASS')
print('Theorem 3.3 Hodge coordinate: r_D(phi_*{1-u,1-v}) = -3/2 times the stated L-value basis.')
print('No numerical 3-adic Frobenius value or finite torsion coordinate is inferred.')

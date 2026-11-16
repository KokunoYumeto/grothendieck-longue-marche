"""An explicit 44-coordinate phantom and the 24=23+1 fibre comparison.

All prime conditions are elementary finite conditions.  Their existence
for every j is proved by Chebotarev in the manuscript.  The displayed
correction is a rational 3-adic unit in the local prolongations explicitly
normalized in the proof. A finite-field discrete logarithm determines only
the residue class of an arbitrary Frobenius value. Conjugating its
prolongation by a prescribed element of ker(chi3) makes the selected integer
the exact value. No rational reconstruction of a 3-adic value is used.
"""
from fractions import Fraction
from itertools import combinations
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

def v3(n):
    n=abs(int(n));v=0
    assert n
    while n%3==0:n//=3;v+=1
    return v

names=['f1','f2','A0','A1','A2','B0','B1','B2','C1','C2']
pairs=list(combinations(range(10),2))
pivot=pairs.index((2,4))
quotient_pairs=[z for z in pairs if z!=(2,4)]
coordinate=quotient_pairs.index((2,5))
assert coordinate==18
print('44-coordinate order:')
print(', '.join(f'{i+1}:{names[a]}^{names[b]}' for i,(a,b) in enumerate(quotient_pairs)))
print('Only coordinate',coordinate+1,'(A0 wedge B0) is nonzero.')
print(' j      p_j     u_j=(p_j-1)/3^j   least primitive root     b_j    correction=-b_j/u_j')
used=set()
for j in range(1,11):
    power=3**j
    p=1+power
    while not (s.isprime(p) and p not in used and pow(3,(p-1)//3,p)!=1):
        p+=3*power
    used.add(p)
    assert v3(p-1)==j
    u=(p-1)//power
    g=int(s.primitive_root(p))
    zeta=pow(g,u,p)
    b=int(s.discrete_log(p,pow(3,u,p),zeta))
    assert 0<=b<power and b%3!=0 and u%3!=0
    c=-Fraction(b,u)
    assert power*b+(p-1)*c==0
    print(f'{j:2} {p:10} {u:20} {g:22} {b:9} {str(c):>20}')
print('All listed corrections are integral 3-adic units: no decay, despite a_j=3^j -> 0.')

U=s.Matrix([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]])
R=s.Matrix([[0,-1],[1,-1]])
AE=s.eye(2)+3*R
At=AE.row_join(s.zeros(2,8)).col_join((U*(AE-7*s.eye(2))/3).row_join(7*s.eye(8)))
CE=s.Matrix([[1,-1],[0,-1]])
perm=[0,2,1,3,5,4,7,6]
CT=s.zeros(8)
for j,i in enumerate(perm):CT[i,j]=-1
C=CE.row_join(s.zeros(2,8)).col_join(((U*CE-CT*U)/3).row_join(CT))
assert C*C==s.eye(10)
assert all(x.q==1 for x in C)
def wedge2(A):
    return s.Matrix([[A[i,k]*A[j,l]-A[i,l]*A[j,k]
                      for k,l in pairs] for i,j in pairs])
B=wedge2(At);J=wedge2(C)
idx=[i for i,z in enumerate(pairs) if z!=(0,1)]
assert all(B[0,i]==J[0,i]==0 for i in idx)
B0=B.extract(idx,idx);J0=J.extract(idx,idx)
for label,T,Q in [('M=Lambda2 V',B,J),('M0=kernel of compact determinant',B0,J0)]:
    rel=(T-s.eye(T.rows))*(s.eye(T.rows)+Q)
    diag=smith_normal_form(rel,domain=s.ZZ)
    nonzero=[abs(int(diag[i,i])) for i in range(diag.rows) if diag[i,i]]
    vals=[v3(x) for x in nonzero]
    hist={e:vals.count(e) for e in sorted(set(vals))}
    free=T.rows-len(nonzero)
    print(label,': free rank',free,'; 3-adic Smith valuation multiplicities',hist)
    assert free==(24 if T.rows==45 else 23)
    assert hist=={0:7,1:9,2:5}
print('Exact integral cohomology comparison: same finite torsion, free ranks 24=23+1: PASS.')

# Independent framed P-row check for the LM7_PUSH A.4 comparison.
z=s.symbols('z')
mod=z*z+z+1
def reduce_field(x):
    num,den=s.fraction(s.cancel(x))
    return s.rem(s.rem(num,mod,z)*s.invert(den,mod,z),mod,z).expand()
lam=1-z
cusps=[(0,-z,1),(0,-z*z,1),(-z,0,1),(-z*z,0,1),(1,-z,0),(1,-z*z,0)]
framed=[s.Rational(1,9),s.Rational(-1,3)]
for x,y,t in cusps:
    framed.append(reduce_field((y+t)/(3*(x+y))))
expected=[s.Rational(1,9),s.Rational(-1,3),
          1/lam,1/(1-z*z),1/lam**2,1/(1-z*z)**2,
          z*z/lam**3,z/(1-z*z)**3]
assert all(reduce_field(a-b)==0 for a,b in zip(framed,expected))
print('LM7_PUSH A.4 framed cube 3z_P, all eight entries:',framed)
print('Exact regularized tangent-line comparison: PASS')

# LM6 E.39 compares abelian path modules, not the degree-three action lattice.
jmap=s.eye(2).row_join(s.zeros(2,8)).col_join((-U).row_join(3*s.eye(8)))
targetT=s.diag(AE,7*s.eye(8))
targetC=s.diag(CE,CT)
assert jmap*At==targetT*jmap
assert jmap*C==targetC*jmap
jsmith=smith_normal_form(jmap,domain=s.ZZ)
jorders=[abs(int(jsmith[i,i])) for i in range(10)]
assert jorders==[1,1]+[3]*8
fixedQ=[]
for a,b in [(1,2),(4,5),(6,7)]:
    e=s.zeros(8,1);e[a]=1;e[b]=-1
    assert CT*e==e
    fixedQ.append(e)
assert s.Matrix.hstack(*fixedQ).rank()==3
print('Abelian path comparison j Smith orders:',jorders)
print('Its quotient has K-invariants F3^8 and Q-invariants F3^3; the latter are three conjugate-cusp differences.')

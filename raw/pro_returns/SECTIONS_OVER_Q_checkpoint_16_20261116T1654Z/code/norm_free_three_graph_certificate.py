"""Exact coefficient and residue checks for A.119."""
from itertools import product
from math import comb, gcd
import sympy as sp

N,d=9,3
def mod(A):
    return A.applyfunc(lambda v:int(v)%3)

def power_z(k):
    return sp.Matrix([comb(k,i)*(-1)**(k-i) if i<=k else 0
                      for i in range(N)])

basis=sp.Matrix.hstack(*[power_z(k) for k in range(d,N)])
Wstar=sp.zeros(N)
for h in range(d):
    Wstar[h,h+d]=1
    Wstar[h+d,h]=-1
Bstar=mod(basis.T*Wstar*basis)
assert int(Bstar.det())%3 != 0
F=sp.zeros(6)
F[4,0]=F[5,0]=F[5,1]=1
B0=mod(Bstar*F)
assert B0[0,1] == 1 and B0[1,0] == 2
assert B0[2:,:] == sp.zeros(4,6)
assert B0[:,2:] == sp.zeros(6,4)
one=sp.zeros(6,1); one[5]=1
assert mod(basis*one) == sp.ones(9,1)
assert B0*one == sp.zeros(6,1)

def z_coordinates(v):
    coeff=[sum(int(v[i])*comb(i,k) for i in range(k,N))%3
           for k in range(N)]
    assert coeff[:d] == [0]*d
    return sp.Matrix(coeff[d:])

def action(translation,unit):
    cols=[]
    for j in range(6):
        moved=[0]*N
        for i in range(N):
            moved[(translation+unit*i)%N] += unit*int(basis[i,j])
        cols.append(z_coordinates(moved))
    return sp.Matrix.hstack(*cols)

equivariance=0
for translation in range(N):
    for unit in range(N):
        if gcd(unit,N)!=1: continue
        A=action(translation,unit)
        assert mod(A.T*Bstar*A-unit*Bstar) == sp.zeros(6)
        assert mod(A*F-F*A) == sp.zeros(6)
        assert mod(A.T*B0*A-unit*B0) == sp.zeros(6)
        equivariance+=1
At=action(1,1)[:2,:2]
Ae=action(0,-1)[:2,:2]
assert At == sp.Matrix([[1,0],[1,1]])
assert Ae == sp.diag(1,2)
assert mod(F[:,1]) == one

graph_checks=0
for coords in product(range(3),repeat=6):
    t=sp.Matrix(coords)
    for z,w in product(range(3),repeat=2):
        c=z*t+w*one
        assert int((t.T*B0*c)[0])%3 == 0
        graph_checks+=1

isotropic_checks=0
for a,b,c in product(range(3),repeat=3):
    G=sp.Matrix([[a,b],[b,c]])
    if int(G.det())%3==0: continue
    for v in product(range(3),repeat=2):
        if v==(0,0):continue
        V=sp.Matrix(v)
        if int((V.T*G*V)[0])%3:continue
        perp={w for w in product(range(3),repeat=2)
              if int((sp.Matrix(w).T*G*V)[0])%3==0}
        span={tuple(int(z*x)%3 for x in V) for z in range(3)}
        assert perp==span
        assert all(int((sp.Matrix(w).T*G*sp.Matrix(w))[0])%3==0
                   for w in perp)
        isotropic_checks+=1

q,g=321193,5
theta,a0,z0=2827,146470,100461
assert sp.isprime(q)
assert sp.n_order(g,q)==q-1
assert q%216==1
assert pow(theta,27,q)==3
assert pow(theta,3,q)==a0
assert pow(a0,9,q)==3
assert sp.n_order(z0,q)==9
assert pow(-2,(q-1)//72,q)==1
omega=pow(g,(q-1)//3,q)
assert omega!=1
chars={1:0,omega:1,pow(omega,2,q):2}
roots=[a0*pow(z0,i,q)%q for i in range(9)]
old=[chars[pow((1-a)%q,(q-1)//3,q)] for a in roots]
v=[0,1,2,2,2,1,1,2,0]
assert old==[2,2,0,0,1,0,2,2,0]
assert all((old[i]+v[(i+1)%9]-v[i])%3==0 for i in range(9))
tgeom=sp.Matrix([-1,0,0,1,0,0,0,0,0])
cgeom=sp.Matrix([1,-1,0,-1,1,0,0,0,0])
assert mod(tgeom-basis[:,0])==sp.zeros(9,1)
assert mod(cgeom-basis[:,1])==sp.zeros(9,1)
for h in range(d):
    assert sum(int(tgeom[h+j*d]) for j in range(3))==0
    assert sum(int(cgeom[h+j*d]) for j in range(3))==0

print("A119 ACTUAL RELATIVE COEFFICIENT MAPS")
print("Bstar Gram:",Bstar.tolist())
print("B0 Gram:",B0.tolist())
print("F image columns:",F[:,0].T.tolist(),F[:,1].T.tolist())
print("actual arithmetic equivariance checks:",equivariance)
print("rank-two translation:",At.tolist())
print("rank-two involution:",Ae.tolist())
print("scalar-shift graph checks:",graph_checks)
print("nonzero isotropic line equals its orthogonal checks:",isotropic_checks)
print("t geometric:",list(tgeom))
print("c geometric:",list(cgeom))
print("B0(t,c)=1; B0(one,-)=0")
print("A119 SPLITTING AND UNIT DATA")
print("q=",q,"primitive unit=",g,"cube character=",omega)
print("27th root=",theta,"ninth root=",a0,"primitive ninth unity=",z0)
print("beta0 unit characters:",old)
print("beta_pre correction exponents:",v)
print("all beta_pre unit characters vanish; b is a 72nd power")
print("ALL CHECKS PASSED")

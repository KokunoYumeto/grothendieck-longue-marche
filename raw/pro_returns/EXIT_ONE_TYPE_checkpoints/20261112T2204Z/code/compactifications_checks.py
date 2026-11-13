"""Exact finite checks for EXIT_ONE_TYPE Parts 2, 3 and the cusp example.
The conceptual proofs in the paper do not infer arbitrary cases from these tests.
"""
from itertools import combinations
from math import gcd
import sympy as s
from sympy.combinatorics.free_groups import free_group
from sympy.combinatorics.fp_groups import FpGroup

print('LOCAL BLOW-UP LATTICES')
for r in range(1,7):
    eye=s.eye(r)
    exceptional=s.ones(r,1)
    bad=eye.row_join(exceptional)
    ker=tuple(bad.nullspace()[0])
    assert ker == tuple([-1]*r+[1])
    print(f'non-toroidal s={r}: rank {bad.rank()} of {r+1}; primitive kernel {ker}')
    if r>=2:
        dets=[]
        for omitted in range(r):
            mat=s.Matrix.hstack(*[eye[:,j] for j in range(r) if j!=omitted],exceptional)
            dets.append(int(mat.det()))
        assert all(abs(d)==1 for d in dets)
        print(f'toroidal s={r}: maximal-chart determinants {dets}')

print('\nCUSP RESOLUTION CHARTS')
u,v,w,x,y=s.symbols('u v w x y')
f=y*y-x*x*x
f1=s.expand(f.subs(y,x*v))
f2=s.expand(f1.subs(x,u*v))
f3=s.expand(f2.subs(v,u*w))
assert s.expand(f1-x*x*(v*v-x))==0
assert s.expand(f2-u*u*v**3*(v-u))==0
assert s.expand(f3-u**6*w**3*(w-1))==0
print('first chart:',s.factor(f1))
print('second chart:',s.factor(f2))
print('third chart:',s.factor(f3))
print('final multiplicities: strict=1, E2=2, E3=3, E6=6')
A=s.Matrix([[0,-1],[1,0]])
B=s.Matrix([[0,-1],[1,1]])
Z=A**2
M=A*B.inv()
assert A**2==B**3==-s.eye(2)
assert (M-s.eye(2))**2==s.zeros(2) and M!=s.eye(2)
print('a matrix:',list(A)); print('b matrix:',list(B))
print('a^2=b^3:',list(Z)); print('meridian a b^-1:',list(M))
print('m=I+N, N^2=0, N!=0: infinite order; degree(a,b,z,m)=(3,2,6,1)')
for row in ([6,2],[6,3]):
    mat=s.Matrix([row]); q=mat.nullspace()[0]
    q=q*s.ilcm(*[z.q for z in q])
    if q[0]<0:q=-q
    print('node exponents',row,'primitive kernel',tuple(q))
    assert mat*q==s.zeros(1,1)
for n0,n1 in ((1,1),(2,3),(5,7),(6,6)):
    row=s.Matrix([[2*n0,6*n1]])
    q=row.nullspace()[0]*s.ilcm(*[z.q for z in row.nullspace()[0]])
    assert q!=s.zeros(2,1)
    print('rooted bad node indices',n0,n1,'nonzero kernel',tuple(q))

print('\nFINITE COMPLEMENT GROUPS')
F,a,b=free_group('a,b')
conic=FpGroup(F,[a*a,b])
nodal=FpGroup(F,[a*b**-1,a*b*a**-1*b**-1,a**3])
print('conic presentation order:',conic.order()); assert conic.order()==2
print('nodal cubic van Kampen presentation order:',nodal.order()); assert nodal.order()==3

print('\nMINIMAL TORIC SURFACE FANS')
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def fan_check(name,rays):
    n=len(rays)
    ds=[det(rays[i],rays[(i+1)%n]) for i in range(n)]
    assert ds==[1]*n
    weights=[-det(rays[i-1],rays[(i+1)%n]) for i in range(n)]
    print(name, 'rays=',rays,'self-intersections=',weights,'corner-minimal=',-1 not in weights)
    return weights
fan_check('P2',[(1,0),(0,1),(-1,-1)])
for n in range(0,7):
    weights=fan_check(f'F{n}',[(1,0),(0,1),(-1,n),(0,-1)])
    assert ((-1 not in weights)==(n!=1))

print('\nRATIONAL-TWIG REDUCTION CHECK')
# Starting with a toric triangle: an outer blow-up and a blow-up of the new
# edge produce a (-2)-tip joined by a (-1)-curve. Both must disappear.
vertices={'A':1,'B':1,'C':1}
edges={frozenset(e) for e in [('A','B'),('B','C'),('C','A')]}
def outer(a,e):
    vertices[a]-=1;vertices[e]=-1;edges.add(frozenset((a,e)))
def inner(a,b,e):
    edges.remove(frozenset((a,b)));vertices[a]-=1;vertices[b]-=1;vertices[e]=-1
    edges.add(frozenset((a,e)));edges.add(frozenset((b,e)))
def core():
    keep=set(vertices)
    while True:
        drop={v for v in keep if sum(v in e and e<=keep for e in edges)<=1}
        if not drop:return keep
        keep-=drop
def contract(v):
    ns=[next(iter(e-{v})) for e in edges if v in e]
    assert vertices[v]==-1 and len(ns)<=2
    for e in list(edges):
        if v in e:edges.remove(e)
    del vertices[v]
    for x in ns:vertices[x]+=1
    if len(ns)==2:edges.add(frozenset(ns))
outer('A','E');inner('A','E','F')
print('before:',vertices,'core:',sorted(core()))
assert core()=={'A','B','C'}
contract('F');contract('E')
assert vertices=={'A':1,'B':1,'C':1}
print('after:',vertices,'core:',sorted(core()))
print('\nALL EXACT CHECKS PASSED')

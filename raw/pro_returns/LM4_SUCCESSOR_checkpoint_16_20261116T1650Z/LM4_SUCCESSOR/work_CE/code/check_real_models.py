"""Finite verifications supporting E.3, E.4 and E.7; not CSP tests."""
from itertools import permutations, product
import sympy as sp

# D_8 = {(i,e): r^i t^e}; t r t = r^-1.
def mul(a,b):
    i,e=a; j,f=b
    return ((i+(-1)**e*j)%4,(e+f)%2)
def inv(a):
    return next(b for b in D if mul(a,b)==(0,0) and mul(b,a)==(0,0))
def conj(a,b): return mul(mul(a,b),inv(a))
D=list(product(range(4),range(2)))
r,t=(1,0),(0,1)
K=[(0,0),(2,0)]
assert conj(t,r)==inv(r)
assert all(mul(k,conj(t,k))==(0,0) for k in K)
assert [mul(mul(r,k),inv(conj(t,r))) for k in K]==K[::-1]
assert [g for g in [(i,0) for i in range(4)] if conj(g,t)==t]==K
print('E.3: D8 has two K-cocycle classes; Q=C2 interchanges them; C_P(t)=K. PASS')

# Orientation-double-cover graph of the N4 pants decomposition.
V=('P+','P-','Q+','Q-')
edges={'a+':('P+','Q+'),'a-':('P-','Q-'),
       'b+':('P+','Q+'),'b-':('P-','Q-'),
       'c+':('P+','Q-'),'c-':('P-','Q+')}
seen={V[0]}
while True:
    new=seen|{b for a,b in edges.values() if a in seen}|{a for a,b in edges.values() if b in seen}
    if new==seen:break
    seen=new
assert seen==set(V)
inc={v:frozenset(k for k,e in edges.items() if v in e) for v in V}
assert len(set(inc.values()))==4
autom=[]
for p in permutations(V):
    f=dict(zip(V,p))
    if all({f[a],f[b]}=={a,b} for a,b in edges.values()):autom.append(p)
assert autom==[V]
names=list(edges)
vectors=[tuple((1 if n==z+'+' else -1 if n==z+'-' else 0) for n in names) for z in 'abc']
fix=[]
for p in permutations(range(6)):
    if all(tuple(w[p[i]] for i in range(6))==w for w in vectors):fix.append(p)
assert fix==[tuple(range(6))]
print('E.7: connected four-vertex cover; all incident edge sets distinct; edge-fixing graph group trivial. PASS')
print('E.7: simultaneous stabilizer of three signed twist vectors in S6 is trivial. PASS')

# These checks certify smoothness and real branch-point counts. The dividing
# assertions in E.4 are proved topologically in the paper, not inferred here.
x=sp.symbols('x')
polys=[(-(x**8+1),0),((x*x-1)*(x**6+1),2),
       ((x*x-1)*(x*x-4)*(x**4+1),4),
       ((x*x-1)*(x*x-4)*(x*x-9)*(x*x+1),6),
       (x**8+1,0),(sp.prod(x*x-j*j for j in range(1,5)),8)]
for f,n in polys:
    p=sp.Poly(f,x)
    assert p.degree()==8 and sp.gcd(p,p.diff()).degree()==0
    assert p.count_roots(-sp.oo,sp.oo)==n
print('E.4: all six degree-eight models square-free; real branch counts 0,2,4,6,0,8. PASS')

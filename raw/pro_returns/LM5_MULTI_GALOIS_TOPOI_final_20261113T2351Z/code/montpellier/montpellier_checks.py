"""Exact finite audits for LM5 Part F. No mathematical assertion is inferred
from a sample alone: the paper proves the general statements separately.
"""
from itertools import combinations, product
from collections import deque
import sympy as sp


def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a: out.pop()
        else: out.append(a)
    while len(out)>1 and out[0]==-out[-1]: out=out[1:-1]
    return out

def inverse(w): return [-a for a in w[::-1]]
def pi1_poset(n,cutoff):
    vertices=[frozenset(c) for r in range(1,cutoff+1) for c in combinations(range(n),r)]
    edges=[(a,b) for a,b in combinations(range(len(vertices)),2) if vertices[a]<vertices[b]]
    adjacency={v:[] for v in range(len(vertices))}
    for e,(a,b) in enumerate(edges): adjacency[a].append((b,e)); adjacency[b].append((a,e))
    seen={0}; tree=set(); q=deque([0])
    while q:
        a=q.popleft()
        for b,e in adjacency[a]:
            if b not in seen: seen.add(b);tree.add(e);q.append(b)
    edgegen={e:i+1 for i,e in enumerate(e for e in range(len(edges)) if e not in tree)}
    edgeid={pair:e for e,pair in enumerate(edges)}
    def ew(a,b):
        e=edgeid[(a,b)]
        return [] if e in tree else [edgegen[e]]
    triangles=[]; rel=[]
    for a,b,c in combinations(range(len(vertices)),3):
        if vertices[a]<vertices[b]<vertices[c]:
            triangles.append((a,b,c)); rel.append(reduce_word(ew(a,b)+ew(b,c)+inverse(ew(a,c))))
    gens=set(edgegen.values());eliminations=[]
    while True:
        chosen=None
        for r in rel:
            for g in gens:
                if sum(abs(a)==g for a in r)==1:chosen=(r,g);break
            if chosen:break
        if not chosen:break
        r,g=chosen; j=next(j for j,a in enumerate(r) if abs(a)==g)
        # u g^sign v =1 implies g^sign =u^-1 v^-1
        rhs=inverse(r[:j])+inverse(r[j+1:])
        if r[j]<0: rhs=inverse(rhs)
        new=[]
        for s in rel:
            if s is r:continue
            expanded=[]
            for a in s: expanded += rhs if a==g else inverse(rhs) if a==-g else [a]
            rr=reduce_word(expanded)
            if rr:new.append(rr)
        rel=new;gens.remove(g);eliminations.append(g)
    return len(vertices),len(edges),len(triangles),len(gens),rel,len(eliminations)

print('F.15 bicategorical constant-groupoid flag colimit')
for cutoff in (2,3):
    V,E,F,ng,rels,nel=pi1_poset(3,cutoff)
    assert not rels
    print(f'  depth <= {cutoff}: vertices={V}, edges={E}, triangles={F}; free index generators={ng}; Tietze eliminations={nel}; total group=Z^{3+ng}')
assert pi1_poset(3,2)[3]==1 and pi1_poset(3,3)[3]==0

print('F.16 sharpness: reduced homology of simplex boundaries')
for n in range(2,7):
    faces={r:list(combinations(range(n),r+1)) for r in range(n-1)}
    ranks={0:1}
    for r in range(1,n-1):
        prev={f:i for i,f in enumerate(faces[r-1])}
        M=sp.zeros(len(prev),len(faces[r]))
        for col,f in enumerate(faces[r]):
            for j in range(r+1): M[prev[f[:j]+f[j+1:]],col]=(-1)**j
        ranks[r]=M.rank()
    betti=[]
    for r in range(n-1):
        betti.append(len(faces[r])-ranks[r]-ranks.get(r+1,0))
    assert betti==[0]*(n-2)+[1]
    print(f'  boundary of {(n-1)}-simplex: reduced Betti={betti}')

print('F.11 Boolean coslices do not force thinness')
objects=('x','y','z'); ranks={'x':2,'y':1,'z':0}
arrows={'ix':('x','x'),'iy':('y','y'),'iz':('z','z'),'a':('x','y'),'b':('x','y'),'c':('y','z'),'d':('x','z')}
ids={'x':'ix','y':'iy','z':'iz'}
def compose(g,f):
    assert arrows[f][1]==arrows[g][0]
    if f==ids[arrows[f][0]]: return g
    if g==ids[arrows[g][0]]: return f
    assert (g,f) in [('c','a'),('c','b')]
    return 'd'
for f,g,h in product(arrows,repeat=3):
    if arrows[f][1]==arrows[g][0] and arrows[g][1]==arrows[h][0]:
        assert compose(h,compose(g,f))==compose(compose(h,g),f)
for x in objects:
    outgoing=[f for f in arrows if arrows[f][0]==x]
    rel=[(f,g) for f,g in product(outgoing,repeat=2) if any(arrows[h][0]==arrows[f][1] and arrows[h][1]==arrows[g][1] and compose(h,f)==g for h in arrows)]
    assert len(outgoing)==2**ranks[x]
    print(f'  {x}: arrows={outgoing}, factorization relation={rel}')
assert arrows['a']==arrows['b'] and 'a'!='b'
print('  all composition triples associative; parallel a,b distinct')

print('F.6 elliptic j-invariant')
j=sp.symbols('j');a=-3*j/(j-1728);b=-2*j/(j-1728)
computed=sp.factor(1728*4*a**3/(4*a**3+27*b**2))
assert computed==j
print('  j(E_j)=',computed)
print('  discriminant=',sp.factor(-16*(4*a**3+27*b**2)))

print('F.20 transvection obstruction')
M=sp.Matrix([[1,1],[0,1]]);v=sp.Matrix(sp.symbols('a b'))
print('  (M-I)v=',list((M-sp.eye(2))*v))
assert list((M-sp.eye(2))*v)==[v[1],0]
print('  every fixed vector has normal coordinate b=0; no equivariant splitting')

print('F.22 finite root-stack kernel')
for n in (2,3,5):
    mod=30*n
    kernel=[a for a in range(mod) if a%n==0]
    assert kernel==list(range(0,mod,n))
    print(f'  Z/{mod} -> Z/{n}: kernel generated by {n}, cardinality {len(kernel)}')

# Normal-crossing compactification of M_0,5 as Bl_{(0,0),(1,1),(inf,inf)}(P1 x P1).
from itertools import combinations
from math import gcd
vec = {
 'x0':(1,0,0,0,0), 'x1':(0,1,0,0,0), 'xi':(-1,-1,0,0,-1),
 'y0':(0,0,1,0,0), 'y1':(0,0,0,1,0), 'yi':(0,0,-1,-1,-1),
 'diag':(0,0,0,0,1), 'E0':(1,0,1,0,1),
 'E1':(0,1,0,1,1), 'Ei':(-1,-1,-1,-1,-1)}
edges = [('x'+h,'y'+k) for h in ('0','1','i') for k in ('0','1','i') if h!=k]
edges += [('E'+h,t) for h in ('0','1','i') for t in ('x'+h,'y'+h,'diag')]
print('F.43 M_0,5 boundary meridian independence')
for u,v in edges:
    minors=[vec[u][i]*vec[v][j]-vec[u][j]*vec[v][i] for i,j in combinations(range(5),2)]
    g=0
    for d in minors: g=gcd(g,abs(d))
    assert g==1
    print(' ',u,v,'Smith rank=2, elementary divisors=(1,1)')
assert len(edges)==15
assert all(sum(t in e for e in edges)==3 for t in vec)
print('  all 15 compatible meridian pairs split inject into Z^5; boundary graph has 10 vertices and degree 3')

print('F.25 free involution: Segal map on connected components fails')
perm={1:2,2:1,3:4,4:3}
def transform(flag): return tuple(frozenset(perm[x] for x in v) for v in flag)
def orbit(flag):
    f=tuple(frozenset(v) for v in flag)
    return frozenset((f,transform(f)))
B={1,2}
upper1=({1,2,3},B); upper2=({1,2,4},B)
lower1=(B,{1}); lower2=(B,{2})
full1=({1,2,3},B,{1}); full2=({1,2,3},B,{2})
assert orbit(upper1)==orbit(upper2)
assert orbit(lower1)==orbit(lower2)
assert orbit(full1)!=orbit(full2)
assert orbit(({1,2,3},{1}))!=orbit(({1,2,3},{2}))
print('  upper pairs same orbit; lower pairs same orbit; full flags distinct; composites distinct')
print('ALL CHECKS PASSED')

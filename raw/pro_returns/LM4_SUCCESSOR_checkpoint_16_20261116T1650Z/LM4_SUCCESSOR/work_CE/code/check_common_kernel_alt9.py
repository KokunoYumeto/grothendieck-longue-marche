"""Exact finite certificates for B.57.

Pure Python enumeration; no random search or black-box group-order result.
Conventions: permutations act on the left and compose(p,q)=p after q.
The Schur multiplier of A9 is a cited primary ATLAS input, not a numerical
claim inferred by this program. All universal-cover and profinite lifting
arguments are supplied in the proof.
"""
from collections import deque, Counter
from itertools import permutations

def identity(n): return tuple(range(n))
def compose(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inverse(p): return tuple(p.index(i) for i in range(len(p)))
def cycle(n, *xs):
    p=list(range(n))
    for a,b in zip(xs,xs[1:]+xs[:1]): p[a]=b
    return tuple(p)
def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def cycle_type(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; k=0
        while j not in seen:
            seen.add(j); k+=1; j=p[j]
        out.append(k)
    return sorted(out)
def closure(gens):
    one=identity(len(gens[0])); seen={one}; todo=deque([one])
    while todo:
        a=todo.popleft()
        for g in gens:
            b=compose(a,g)
            if b not in seen: seen.add(b); todo.append(b)
    return seen
def conjugate(a,g): return compose(compose(a,g),inverse(a))

# The specified quotient of the tripod.
X=cycle(9,0,1,2,3,4,5,6)
Y=cycle(9,0,1,4,3,2,7,8)
Z=inverse(compose(X,Y))
S=closure([X,Y])
assert len(S)==181440 and all(sign(g)==1 for g in S)
assert all(cycle_type(g)==[1,1,7] for g in (X,Y,Z))
print('A9 generation by the specified X,Y: exactly',len(S),'even permutations: PASS')
print('X,Y,Z=(XY)^(-1) cycle types:',[cycle_type(g) for g in (X,Y,Z)])
print('Z permutation in zero-based image notation:',Z)
t=cycle(9,0,1)
for name,g in [('X',X),('Y',Y),('Z',Z)]:
    fixed=[i for i in range(9) if g[i]==i]
    c=cycle(9,*fixed)
    u=compose(t,c)
    assert sign(u)==1 and conjugate(t,g)==conjugate(u,g)
    print('Even conjugator for outer transposition on',name,':',u)
# C_S9(X) consists exactly of the seven powers of X times the swap
# of its two fixed points. Test all fourteen against Y.
fixed=[i for i in range(9) if X[i]==i]
swap=cycle(9,*fixed)
centralizers=[]; p=identity(9)
for _ in range(7):
    for q in (p,compose(p,swap)):
        if compose(q,Y)==compose(Y,q): centralizers.append(q)
    p=compose(p,X)
assert centralizers==[identity(9)]
print('C_S9(<X,Y>)=1 by all14 candidates in C_S9(X): PASS')
print('Thus conjugation by t is outer on A9; its three peripheral classes are preserved.')

# A5 on twelve cosets of C5, with the six antipodal pairs.
A5=[p for p in permutations(range(5)) if sign(p)==1]
rot=cycle(5,0,1,2,3,4)
C5=closure([rot])
normalizer=[g for g in A5 if conjugate(g,rot) in C5]
flip=next(g for g in normalizer if g not in C5)
cosets=sorted({frozenset(compose(g,h) for h in C5) for g in A5},key=min)
ci={c:i for i,c in enumerate(cosets)}
reps=[min(c) for c in cosets]
def act(g,i): return ci[frozenset(compose(g,a) for a in cosets[i])]
pairs={frozenset((i,ci[frozenset(compose(compose(g,flip),h) for h in C5)]))
       for i,g in enumerate(reps)}
pair=min(pairs,key=lambda x:tuple(sorted(x)))
third=next(i for i in range(12) if i not in pair)
T=pair|{third}
orbit={frozenset(act(g,i) for i in T) for g in A5}
stabilizer=[g for g in A5 if frozenset(act(g,i) for i in T)==T]
assert len(pairs)==6 and len(orbit)==60 and len(stabilizer)==1
assert all(sum(pair2<=triple for pair2 in pairs)==1 for triple in orbit)
print('Retained triple:',sorted(T),'with antipodal pair',sorted(pair))
print('A5 orbit size60; stabilizer1; every triple has one antipodal pair: PASS')
assert len({tuple(int(i in triple) for i in range(12)) for triple in orbit})==60
print('The60 simple quotient kernels have distinct nonzero cusp-support patterns: PASS')

# The three factor images in A4 and their normal closures.
a2=compose(cycle(4,0,1),cycle(4,2,3))
a3=cycle(4,0,1,2)
b3=inverse(compose(a2,a3))
A4=closure([a2,a3])
assert len(A4)==12 and cycle_type(b3)==[1,3]
for name,g,wanted in [('order2',a2,4),('order3first',a3,12),('order3second',b3,12)]:
    normal=closure([conjugate(a,g) for a in A4])
    assert len(normal)==wanted
    print('A4 normal closure of',name,': order',len(normal))
print('Thus cone3 fillings send K onto C2*C3; cone2 filling leaves quotientC3.')
print('All finite checks PASS. Profinite central lifting and q(V)=socle are proved in B.57.')


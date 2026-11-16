"""Certificates for B.54's actual pro-7 insertion/averaging construction.

The code checks finite Kummer, Lie, and permutation calculations.  The
infinite fixed-point lift and R2 lift are proved in the accompanying text.
"""
from itertools import permutations, combinations, product
from collections import Counter

# Literal degree-three Soulé Kummer seed.
r, zeta = 29, 16
assert pow(zeta, 7, r) == 1 and zeta != 1
epsilon = 1
for a in range(1, 7):
    epsilon = epsilon * pow((1-pow(zeta, a, r)) % r, a*a, r) % r
assert epsilon == 21 and pow(epsilon, 4, r) == 7 != 1
for b in range(1, 7):
    # After zeta -> zeta^b, exponent of (1-zeta^a) is (a/b)^2.
    for a in range(1, 7):
        assert ((a*pow(b, -1, 7))**2 - pow(b, -2, 7)*a*a) % 7 == 0
assert pow(3, 3, 7) == 6
assert (2*(7*7-1)) % 7 != 0
print('Kummer seed: zeta7 ->16 mod29, epsilon ->21, epsilon^4 ->7: PASS')
print('Kummer line character b^(-2), conjugation on C7 by b^3: PASS')
print('Degree-three coefficient denominator 2(7^2-1) is a7-adic unit: PASS')

# Free Lie algebra in degree at most four over F7, represented associatively.
P = 7
def clean(a): return {w:c%P for w,c in a.items() if c%P}
def add(a,b):
    out=dict(a)
    for w,c in b.items():out[w]=out.get(w,0)+c
    return clean(out)
def scale(a,c):return clean({w:c*v for w,v in a.items()})
def mul(a,b):
    out={}
    for u,c in a.items():
        for v,d in b.items():
            if len(u+v)<=4:out[u+v]=out.get(u+v,0)+c*d
    return clean(out)
def br(a,b):return add(mul(a,b),scale(mul(b,a),-1))
X,Y={(0,):1},{(1,):1}
Z=scale(add(X,Y),-1)
C=br(X,Y);A=br(X,C);B=br(Y,C)
U,V,W=br(X,A),br(Y,A),br(Y,B)
assert V==br(X,B)
d12=(scale(V,-1),V)
d13=(scale(br(X,br(Z,br(X,Z))),-1),{})
d23=({},scale(br(Y,br(Z,br(Y,Z))),-1))
for d,h in [(d13,A),(d23,scale(B,-1))]:
    assert add(d[0],scale(d12[0],-1))==br(h,X)
    assert add(d[1],scale(d12[1],-1))==br(h,Y)
assert all((br(add(scale(A,a),scale(B,b)),X),
            br(add(scale(A,a),scale(B,b)),Y))!=d12
           for a,b in product(range(7),repeat=2))
print('Three pair insertions have the same nonzero outer degree-three class: PASS')

# A5 on its twelve cosets of a C5; antipodal pairs are the six D5/C5 blocks.
ident=tuple(range(5))
def compose(a,b):return tuple(a[b[i]] for i in range(5))
def inverse(a):return tuple(a.index(i) for i in range(5))
def sign(a):return (-1)**sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))
G=[a for a in permutations(range(5)) if sign(a)==1]
rot=(1,2,3,4,0)
H={ident};a=ident
for _ in range(4):a=compose(a,rot);H.add(a)
N=[g for g in G if compose(compose(g,rot),inverse(g)) in H]
flip=next(g for g in N if g not in H)
cosets=sorted({frozenset(compose(g,h) for h in H) for g in G},
              key=lambda c:min(c))
index={c:i for i,c in enumerate(cosets)}
reps=[min(c) for c in cosets]
def act(g,i):return index[frozenset(compose(g,a) for a in cosets[i])]
opposite={frozenset((i,index[frozenset(compose(compose(g,flip),h)
                                      for h in H)]))
          for i,g in enumerate(reps)}
assert len(G)==60 and len(H)==5 and len(N)==10 and len(cosets)==12
assert len(opposite)==6 and all(len(p)==2 for p in opposite)
seed=next(iter(opposite))
orbit_counts=Counter(frozenset(act(g,i) for i in seed) for g in G)
assert set(orbit_counts)==opposite and set(orbit_counts.values())=={10}
triple_counts=Counter()
for t in combinations(range(12),3):
    count=sum(n for pair,n in orbit_counts.items() if pair<=set(t))
    triple_counts[count]+=1
assert triple_counts=={0:160,10:60}
assert 10%7!=0 and 60%7!=0
print('A5/C5 vertices:',len(cosets),'; antipodal pairs:',len(opposite))
print('Each pair occurs10 times in the60-element trace: PASS')
print('Tripod coefficients before reduction:',dict(sorted(triple_counts.items())))
print('Thus160 tripod shadows vanish and60 equal10 times the nonzero seed: PASS')
print('Fixed-point lifting and full R2 lifting are supplied by proof, not inferred from these checks.')

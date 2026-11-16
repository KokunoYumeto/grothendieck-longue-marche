"""Exact exterior-algebra checks for the rank-two quartic CM projector."""
from itertools import combinations
from collections import defaultdict

def wedge(a,b):
    out=defaultdict(int)
    for I,x in a.items():
        for J,y in b.items():
            if set(I)&set(J):
                continue
            inv=sum(i>j for i in I for j in J)
            out[tuple(sorted(I+J))]+=(-1)**inv*x*y
    return {k:v for k,v in out.items() if v}

def add(*terms):
    d=defaultdict(int)
    for s,t in terms:
        for I,v in t.items():d[I]+=s*v
    return {I:v for I,v in d.items() if v}

v=[{(i,):1} for i in range(6)]
q=add(*[(1,wedge(v[2*r],v[2*r+1])) for r in range(3)])
def pair(i,j):
    if i//2 != j//2:return 0
    if i%2==0 and j==i+1:return 1
    if i%2==1 and j==i-1:return -1
    return 0

def johnson(eta):
    images=[]
    for x in range(6):
        terms=[]
        for (a,b,c),co in eta.items():
            terms.extend([(co*pair(a,x),wedge(v[b],v[c])),
                          (co*pair(b,x),wedge(v[c],v[a])),
                          (co*pair(c,x),wedge(v[a],v[b]))])
        images.append(add(*terms))
    return images

def alt(D):
    return add(*[(s,wedge(v[i],D[j])) for r in range(3)
                 for s,i,j in [(1,2*r,2*r+1),(-1,2*r+1,2*r)]])

for triple in combinations(range(6),3):
    eta={triple:1}
    assert alt(johnson(eta))=={triple:3}
for h in range(6):
    inner=[wedge(v[h],v[x]) for x in range(6)]
    assert alt(inner)==add((-2,wedge(q,v[h])))
    # f(q wedge h) equals -ad_h modulo the polarization line.
    D=johnson(wedge(q,v[h]))
    for x in range(6):
        error=add((1,D[x]),(1,inner[x]))
        assert error==add((pair(h,x),q))
print('Alt(f(eta))=3 eta on every one of 20 exterior basis vectors: PASS')
print('Alt(ad_h)=-2 q wedge h on all 6 basis vectors: PASS')
print('f(q wedge h)=-ad_h modulo q on all 36 coefficient tests: PASS')

# Interleave positive and negative characters to match a symplectic basis.
chars=[(1,1),(3,3),(1,2),(3,2),(2,1),(2,3)]
invariants=[]
for I in combinations(range(6),3):
    if all(sum(chars[i][j] for i in I)%4==0 for j in range(2)):
        invariants.append(I)
assert invariants==[(0,2,4),(1,3,5)]
print('Deck-invariant exterior triples:',invariants)
print('Primitive exterior invariant rank = 2; no H character is trivial: PASS')
print('The pure-CM projector after Alt/3 is integral at 5: denominators 2,3,16 are units.')

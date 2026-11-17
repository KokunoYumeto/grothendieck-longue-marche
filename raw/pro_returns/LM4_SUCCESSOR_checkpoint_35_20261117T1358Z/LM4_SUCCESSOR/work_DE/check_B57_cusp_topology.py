"""Independent finite cusp/topology checks for the B.57 peer review.

This uses the original B=C2*C3 quotient generators of B.53/B.55.
It does not certify the central-extension/lifting argument of B.57.
The free-product identities below use exact reduced normal forms.
"""
from collections import Counter, deque
from itertools import permutations
from pathlib import Path
import json

def mul(p,q): return tuple(p[q[i]] for i in range(len(p)))
def inv(p): return tuple(p.index(i) for i in range(len(p)))
def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def closure(gs):
    one=tuple(range(len(gs[0]))); seen={one}; todo=deque([one])
    while todo:
        x=todo.popleft()
        for g in gs:
            y=mul(x,g)
            if y not in seen: seen.add(y); todo.append(y)
    return seen
def conj(g,x): return mul(mul(g,x),inv(g))
def order(x):
    one=tuple(range(len(x))); y=x; n=1
    while y!=one: y=mul(y,x); n+=1
    return n

s=(1,0,3,2,4)
r=(2,1,4,3,0)
tau=mul(s,r)
A5=closure([s,r]); I=tuple(range(5))
assert len(A5)==60 and all(sign(g)==1 for g in A5)
assert (order(s),order(r),order(tau))==(2,3,5)
D=closure([tau])
cusps=sorted({frozenset(mul(g,h) for h in D) for g in A5},key=min)
cusp_index={c:i for i,c in enumerate(cusps)}
assert len(cusps)==12
def cusp(g): return cusp_index[frozenset(mul(g,h) for h in D)]
def act(g,i): return cusp(mul(g,min(cusps[i])))
print('Original modular quotient: |<s,r>|=60; orders(s,r,sr)=(2,3,5): PASS')
print('K cusp set A5/<sr>: twelve cosets, each base cusp width five: PASS')

all_blocks=[]
for fixed in range(5):
    T={g for g in A5 if g[fixed]==fixed}
    assert len(T)==12 and len(T&D)==1
    # The J_i cusp has width five, and all K -> J_i cusp widths are one.
    assert {cusp(g) for g in T}==set(range(12))
    assert len({tuple(act(g,i) for i in range(12)) for g in T})==12
    V={g for g in T if order(g) in (1,2)}
    assert len(V)==4 and closure(list(V))==V
    assert all(conj(g,h) in V for g in T for h in V)
    blocks=sorted({tuple(sorted(act(v,i) for v in V)) for i in range(12)})
    assert len(blocks)==3 and all(len(b)==4 for b in blocks)
    assert sorted(i for b in blocks for i in b)==list(range(12))
    # Each cone-3 factor normally generates T; the cone-2 normal closure is V.
    for a in T:
        if order(a)==3:
            assert closure([conj(g,a) for g in T])==T
        elif order(a)==2:
            assert closure([conj(g,a) for g in T])==V
    all_blocks.append(blocks)
    print('Point stabilizer',fixed,': K->J has12 width-one cusps; C2-filling colors',blocks)
print('All five cone-2 fillings: exactly three colors of four cusps; cone-3 images are full targets: PASS')

# Verify the regular tripod orbit in the ORIGINAL cusp labelling.
normalizer={g for g in A5 if {conj(g,h) for h in D}==D}
assert len(normalizer)==10
flip=next(g for g in normalizer if g not in D)
pairs={frozenset((cusp(g),cusp(mul(g,flip)))) for g in A5}
assert len(pairs)==6 and all(len(p)==2 for p in pairs)
assert Counter(i for p in pairs for i in p)==Counter({i:1 for i in range(12)})
pair=min(pairs,key=lambda p:tuple(sorted(p)))
third=next(i for i in range(12) if i not in pair)
triple=frozenset(set(pair)|{third})
orbit={frozenset(act(g,i) for i in triple) for g in A5}
assert len(orbit)==60
assert sum(frozenset(act(g,i) for i in triple)==triple for g in A5)==1
assert all(sum(p<=t for p in pairs)==1 for t in orbit)
assert all(len(set(b)-t)>=1 for t in orbit for blocks in all_blocks for b in blocks)
assert len({tuple(int(i in t) for i in range(12)) for t in orbit})==60
print('Original cusp labels: chosen antipodal tripod',sorted(triple),'has regular orbit60: PASS')
print('Every color block in every conjugate filling contains a killed cusp, for every orbit tripod: PASS')
print('All60 nonzero cusp-support patterns are distinct, hence the60 simple quotient kernels are distinct: PASS')

# Normal forms in C3*C3; syllables are (factor, exponent modulo3).
def word(*pieces):
    out=[]
    for piece in pieces:
        for f,e in piece:
            e%=3
            if not e: continue
            if out and out[-1][0]==f:
                e=(out.pop()[1]+e)%3
                if e: out.append((f,e))
            else: out.append((f,e))
    return tuple(out)
def winv(w): return tuple((f,(-e)%3) for f,e in reversed(w))
a=((0,1),); b=((1,1),); c=word(a,b)
c0=c
c1=word(a,c,winv(a))
c2=word(a,a,c,winv(word(a,a)))
assert c0==((0,1),(1,1))
assert c1==((0,2),(1,1),(0,2))
assert c2==((1,1),(0,1))
assert word(c2,c1,c0)==()
assert c1==word(winv(c2),winv(c0))
def mod3(w): return sum((1 if f==0 else -1)*e for f,e in w)%3
assert all(mod3(w)==0 for w in (c0,c1,c2))
print('C3*C3 index-three cusp representatives: c0=ab, c1=a^2ba^2, c2=ba: PASS')
print('Exact free-product identity c2*c1*c0=1; each is a first-power conjugate of ab: PASS')
print('All independent finite and normal-form checks PASS. Rank/genus and continuity are proved in the review.')

out={'generators':{'s':s,'r':r,'tau':tau},
     'cusp_representatives':[min(c) for c in cusps],
     'five_color_partitions':all_blocks,
     'antipodal_pairs':[sorted(p) for p in sorted(pairs,key=lambda p:tuple(sorted(p)))],
     'tripod':sorted(triple), 'tripod_orbit':[sorted(t) for t in sorted(orbit,key=lambda t:tuple(sorted(t)))],
     'cusp_normal_forms':{'c0':c0,'c1':c1,'c2':c2}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

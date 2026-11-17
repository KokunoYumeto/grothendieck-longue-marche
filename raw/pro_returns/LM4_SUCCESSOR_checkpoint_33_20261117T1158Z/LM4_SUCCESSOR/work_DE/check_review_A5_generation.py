"""Independent S5/permutation audit of the proposed all-A5 argument.

No code or data is imported from the proposed proof's finite certificate.
The separate final SL2(F5) check verifies exactly the central-cover fact
used to exclude the plus case, not arbitrary profinite word existence.
"""
from itertools import permutations, product
from collections import Counter, defaultdict

S=list(permutations(range(5))); identity=tuple(range(5))
def parity(a): return sum(a[i]>a[j] for i in range(5) for j in range(i+1,5))%2
A=[a for a in S if not parity(a)]; idx={a:i for i,a in enumerate(A)}; e=idx[identity]
def compose(a,b): return tuple(a[b[i]] for i in range(5))
def inverse(a): return tuple(a.index(i) for i in range(5))
mul=[[idx[compose(a,b)] for b in A] for a in A]
inv=[idx[inverse(a)] for a in A]
autom=[tuple(idx[compose(compose(s,a),inverse(s))] for a in A) for s in S]
assert len(set(autom))==120
inner=[autom[i] for i,s in enumerate(S) if not parity(s)]
def subgroup(a,b):
    result={e}; queue=[e]
    while queue:
        x=queue.pop()
        for y in (a,b):
            z=mul[x][y]
            if z not in result: result.add(z);queue.append(z)
    return frozenset(result)
def order(a):
    z=e
    for n in range(1,61):
        z=mul[z][a]
        if z==e:return n
orders=[order(a) for a in range(60)]
classes=[frozenset(h[a] for h in inner) for a in range(60)]
assert all(classes[a]==classes[inv[a]] for a in range(60))
pairs={(a,b):subgroup(a,b) for a in range(60) for b in range(60)}
generating={p for p,g in pairs.items() if len(g)==60}
orbits=[]; orbit_id={}
for a,b in sorted(generating):
    if (a,b) in orbit_id:continue
    orbit={(h[a],h[b]) for h in autom}; j=len(orbits)
    assert len(orbit)==120 and orbit<=generating
    orbits.append((a,b,orbit))
    orbit_id.update({p:j for p in orbit})
assert len(generating)==2280 and len(orbits)==19
print('PASS 2280 generating pairs in19 free Aut(A5) orbits of size120')

def passport(a,b):return (orders[a],orders[b],orders[mul[a][b]])
hist=Counter(); critical=[]
for j,(a,b,orb) in enumerate(orbits):
    p=passport(a,b)
    if set(p[:2])=={3,5}:case='mixed3/5'
    elif 2 in p[:2]:case='one2'
    elif p[:2]==(3,3):case='3/3'
    elif p[:2]==(5,5):case='5/5'
    else:raise AssertionError(p)
    hist[case]+=1
    same=classes[a]==classes[b] if p[:2]==(5,5) else None
    swaps=[i for i,h in enumerate(autom) if h[a]==b and h[b]==a]
    if p[0]==p[1]:
        assert len(swaps)==1 and orbit_id[b,a]==j
        expected_inner=(p[0]==3 or same)
        assert (parity(S[swaps[0]])==0)==expected_inner
    else:assert not swaps
    if case=='one2' or case=='3/3' or (case=='5/5' and same):critical.append((j,a,b))
    print('orbit',j,'passport',p,'same5class',same,'swap',('inner' if swaps and not parity(S[swaps[0]]) else 'outer') if swaps else 'different kernel')
assert hist=={'mixed3/5':8,'one2':6,'3/3':1,'5/5':4} and len(critical)==9
diff=[passport(a,b) for j,(a,b,orb) in enumerate(orbits) if orders[a]==orders[b]==5 and classes[a]!=classes[b]]
assert sorted(diff)==[(5,5,2),(5,5,3)]
print('PASS8 mixed,6 one2,1 three/three,4 five/five; nine critical negative kernels')

# For the negative action x->x^-1, y->F^-1 y^-1 F, impose the
# actual third-peripheral conjugacy class and test every F in A5.
for j,a,b in critical:
    found=0
    for f in range(60):
        aa=inv[a];bb=mul[mul[inv[f]][inv[b]]][f]
        if mul[aa][bb] not in classes[inv[mul[a][b]]]:continue
        assert len(pairs[aa,bb])==60
        assert orbit_id[aa,bb]==j
        which=[i for i,h in enumerate(autom) if h[a]==aa and h[b]==bb]
        assert len(which)==1 and parity(S[which[0]])==0
        found+=1
    assert found
    print('PASS critical orbit',j,'all',found,'negative peripheral candidates preserve kernel and are inner')

all_subgroups=set(pairs.values())
assert len(all_subgroups)==59
proper=[h for h in all_subgroups if len(h)<60]
maximal=[h for h in proper if not any(h<k for k in proper)]
assert Counter(map(len,maximal))=={6:10,10:6,12:5}
for h in maximal:
    normalizer={g for g in range(60) if frozenset(mul[mul[g][x]][inv[g]] for x in h)==h}
    assert normalizer==h
    if len(h)==12:
        assert all(mul[mul[g][x]][inv[g]]!=inv[x] for g in h for x in h if orders[x]==3)
for x in range(60):
    if orders[x] not in (3,5):continue
    cp=subgroup(x,e)
    centralizer={g for g in range(60) if mul[g][x]==mul[x][g]}
    normalizer={g for g in range(60) if frozenset(mul[mul[g][y]][inv[g]] for y in cp)==cp}
    assert centralizer==cp and len(normalizer)==2*orders[x]
    reflections={g for g in normalizer if orders[g]==2}
    assert len(reflections)==orders[x]
    assert all((mul[g][h]==mul[h][g])==(g==h) for g in reflections for h in reflections)
print('PASS all59 subgroups, maximal self-normalizers, no A4 inversion, and odd-dihedral commuting reflections')

def det(m):return (m[0]*m[3]-m[1]*m[2])%5
def mm(a,b):return ((a[0]*b[0]+a[1]*b[2])%5,(a[0]*b[1]+a[1]*b[3])%5,(a[2]*b[0]+a[3]*b[2])%5,(a[2]*b[1]+a[3]*b[3])%5)
I=(1,0,0,1);minusI=(4,0,0,4)
sl=[m for m in product(range(5),repeat=4) if det(m)==1]
assert len(sl)==120 and [m for m in sl if m!=I and mm(m,m)==I]==[minusI]
projective_involution_lifts=[m for m in sl if m not in (I,minusI) and mm(m,m) in (I,minusI)]
assert len(projective_involution_lifts)==30 and all(mm(m,m)==minusI for m in projective_involution_lifts)
print('PASS SL2(F5) unique involution is-I; all30 noncentral projective-involution lifts square to-I')
print('ALL INDEPENDENT FINITE CHECKS PASS; no profinite-word existence inferred.')

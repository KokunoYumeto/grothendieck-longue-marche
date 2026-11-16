"""Independent direct 12-dimensional odd-subgroup check for A.49.

This constructs the paired action from permutations, then computes all
66 exterior-square coinvariant coordinates at once. It does not import
the author's affine/Clifford verification programs.
"""
from collections import deque
from itertools import combinations

identity = tuple(range(7))
def compose(a,b): return tuple(a[b[i]] for i in range(7))
def inverse(a): return tuple(a.index(i) for i in range(7))
def pair_product(a,b): return tuple(compose(x,y) for x,y in zip(a,b))
def generated(gens):
    seen = {(identity,identity)}
    queue = deque(seen)
    while queue:
        a = queue.popleft()
        for b in gens:
            c = pair_product(a,b)
            if c not in seen: seen.add(c); queue.append(c)
    return seen
def rank(columns):
    pivots = {}
    for v in columns:
        while v:
            k = v.bit_length()-1
            if k in pivots: v ^= pivots[k]
            else: pivots[k]=v; break
    return len(pivots)
def permute(p,v):
    return sum(1 << p[i] for i in range(7) if (v >> i)&1)

s = tuple(-i % 7 for i in range(7))
r = tuple((2*i+1) % 7 for i in range(7))
rm = compose(compose(s,inverse(r)),s)
t = tuple((i+1) % 7 for i in range(7))
hs,hr = (s,s),(r,rm)
jgens = [(t,identity),(identity,t),hr]
head = generated([hs,hr])
odd = generated(jgens)
assert len(head)==294 and len(odd)==147 and odd <= head
assert all(pair_product(pair_product(hs,x),hs) in odd for x in odd)
print('PASS exact paired head order294; normal odd subgroup order147')

basis = [(1<<i)^(1<<6) for i in range(6)]
pairs = list(combinations(range(12),2))
def action_columns(g):
    return [permute(g[0],v)&63 for v in basis] + [((permute(g[1],v)&63)<<6) for v in basis]
def wedge(u,v):
    value=0
    for k,(i,j) in enumerate(pairs):
        if (((u>>i)&1)*((v>>j)&1)) ^ (((u>>j)&1)*((v>>i)&1)):
            value ^= 1<<k
    return value
relations=[]
for g in jgens:
    cols=action_columns(g)
    relations += [wedge(cols[i],cols[j])^(1<<k) for k,(i,j) in enumerate(pairs)]
assert len(pairs)==66 and rank(relations)==64
print('PASS direct full exterior-square rank64 of66; odd coinvariant dimension2')

vectors=[v for v in range(128) if v.bit_count()%2==0]
for rr in (r,rm):
    fixed_s=[v for v in vectors if permute(s,v)==v]
    norm_r=[v for v in vectors if v^permute(rr,v)^permute(compose(rr,rr),v)==0]
    coboundaries={(v^permute(s,v),v^permute(rr,v)) for v in vectors}
    assert len(fixed_s)==8 and len(norm_r)==16 and len(coboundaries)==64
    assert all((a,b) in {(x,y) for x in fixed_s for y in norm_r} for a,b in coboundaries)
print('PASS both H1(Pi,V) calculations: cocycles128, coboundaries64, dimension1')
assert rank([(permute(t,v)^v)&63 for v in basis])==6
print('PASS translation minus identity invertible on each augmentation module')
print('All independent A49 linear/odd-subgroup checks PASS; no full involution claim.')

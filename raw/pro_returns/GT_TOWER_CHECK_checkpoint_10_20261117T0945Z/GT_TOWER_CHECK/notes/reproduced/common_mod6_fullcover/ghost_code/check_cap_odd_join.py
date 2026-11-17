#!/usr/bin/env python3
"""Small exact cap216 checks needed for the odd-kernel joint source."""
from pathlib import Path
from hashlib import sha256
import json
import numpy as np
HERE=Path(__file__).resolve().parent
path=HERE/'check_main_mixed_capping.npz'
edges=np.load(path)['capped_edges']
assert edges.shape==(216,2)
words={0:()};states=[0]
for a in states:
    for j in range(2):
        b=int(edges[a,j])
        if b not in words:words[b]=words[a]+(j+1,);states.append(b)
assert len(states)==216
table=np.empty((216,216),dtype=np.int16)
for a in range(216):
    for b in range(216):
        c=a
        for j in words[b]:c=int(edges[c,j-1])
        table[a,b]=c
inverse=np.array([int(np.flatnonzero(table[a]==0)[0]) for a in range(216)])
def mul(a,b):return int(table[a,b])
def power(a,n):
    b=0
    for _ in range(n):b=mul(b,a)
    return b
def order(a):
    b=0
    for n in range(1,217):
        b=mul(b,a)
        if b==0:return n
    raise AssertionError(a)
D,V=map(int,edges[0]);assert (D,V)==(1,2)
c=mul(mul(mul(D,V),inverse[D]),inverse[V])
ng={mul(mul(a,c),inverse[a]) for a in range(216)}
derived={0};todo=[0]
for a in todo:
    for b in ng:
        z=mul(a,b)
        if z not in derived:derived.add(z);todo.append(z)
assert len(derived)==27
assert all(power(a,3)==0 for a in derived)
assert all(power(a,4) in derived for a in range(216))
assert all(power(a,12)==0 for a in range(216))
print('PASS cap216 derived subgroup has order27 and exponent3',flush=True)
print('PASS cap216 abelian quotient has exponent dividing4; entire group exponent12',flush=True)

def invword(w):return tuple(-j for j in reversed(w))
def subst(w,images):return tuple(j for z in w for j in
    (images[z-1] if z>0 else invword(images[-z-1])))
def compose(a,b):return tuple(subst(w,a) for w in b)
S=((2,),(1,));R=((2,),(-2,-1));Id=((1,),(2,))
deck=[Id,S,R,compose(R,R),compose(S,R),compose(S,compose(R,R))]
pairs=[(D,power(V,2)),(V,power(D,2))]
def evalword(w,images):
    a=0
    for z in w:a=mul(a,images[z-1] if z>0 else int(inverse[images[-z-1]]))
    return a
records=[]
for i,pair in enumerate(pairs):
    for j,aut in enumerate(deck):
        values=[evalword(w,pair) for w in aut]
        oo=[order(a) for a in values]
        assert all(12%n==0 for n in oo)
        records.append({'pair':i+1,'deck':j,'values':values,'orders':oo})
print('PASS all24 named cap/deck generator values have orders dividing12',flush=True)
out={'scope':'Exact finite cap-coordinate facts for the actual odd-kernel join',
     'input_sha256':sha256(path.read_bytes()).hexdigest(),
     'cap_order':216,'derived_order':27,'derived_exponent':3,
     'abelian_quotient_exponent_divides':4,'group_exponent':12,
     'derived_elements':sorted(derived),'deck_generator_records':records,
     'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact derived and generator certificates saved',flush=True)

#!/usr/bin/env python3
"""Independent direct-permutation review of A.28, without the word engine.

The three substitutions are transcribed directly from the displayed table in
the paper, checked against Bardakov--Bellingeri Proposition 4, printed p.5.
This verifies a finite certificate, not the topological comparison theorem.
"""
from itertools import permutations
from pathlib import Path
import json

identity = tuple(range(4))
def mul(*terms):
    result = identity
    for term in terms:
        result = tuple(result[term[i]] for i in range(4))
    return result
def inv(term):
    return tuple(term.index(i) for i in range(4))
def comm(a,b):
    return mul(inv(a),inv(b),a,b)
def conj(a,b):
    return mul(a,b,inv(a))
def cycle(s):
    out=list(identity)
    entries=[int(x)-1 for x in s]
    for i,x in enumerate(entries):out[x]=entries[(i+1)%len(entries)]
    return tuple(out)
def peripheral(T):
    a,b,d,e=T
    return inv(mul(comm(inv(a),b),comm(inv(d),e)))
def alpha(T):
    a,b,d,e=T;r=peripheral(T);q=comm(r,a)
    return conj(inv(r),a),mul(inv(r),b,comm(a,r)),conj(q,d),conj(q,e)
def beta(T):
    a,b,d,e=T;r=peripheral(T)
    return a,b,mul(d,r),conj(inv(r),e)
def gamma(T):
    a,b,d,e=T;r=peripheral(T)
    return a,b,conj(inv(r),d),mul(inv(r),e,comm(d,r))
def orbit_tuple(T):return gamma(beta(alpha(T)))

tuples=[tuple(map(cycle,row)) for row in [
    ['34','234','134','143'],['34','234','123','234'],
    ['34','234','123','143'],['34','123','234','123'],
    ['34','234','134','124']]]
hs=list(map(cycle,['24','13','234','243','13']))
group=list(permutations(range(4)))
transitions=[]
for i,T in enumerate(tuples):
    computed=tuple(conj(hs[i],x) for x in orbit_tuple(T))
    assert computed==tuples[(i+1)%5]
    transitions.append({'from':i,'to':(i+1)%5,'verified':True})
distinct=[]
for i in range(5):
    for j in range(i):
        assert all(tuple(conj(h,x) for x in tuples[i])!=tuples[j] for h in group)
        distinct.append([j,i])
assert peripheral(tuples[0])==cycle('234')
out={'status':'passed','method':'direct permutation substitutions, independent of free-word engine',
     'transitions':transitions,'pairwise_nonconjugate':distinct,'peripheral_image':'(234)',
     'group_order':len(group),'cycle_length':5,'prime':5,
     'conclusion':'The displayed five-cycle certificate is correct; topology and specialization are separately reviewed in the paper.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

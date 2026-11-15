#!/usr/bin/env python3
"""Exact finite quotient detecting two components of an unpinned flag.

G0 has genera (0,1), loops at each vertex, and a bridge.
Contracting the bridge gives G1 with genus 1 and two loops.
Its half-edge automorphisms form (C2 x C2) semidirect S2.
Both specified incidences have trivial loop-permutation image.
"""
from itertools import permutations
from pathlib import Path
import json

loops = {frozenset((0,1)),frozenset((2,3))}
group = [p for p in permutations(range(4))
         if {frozenset(p[x] for x in loop) for loop in loops} == loops]
kernel = [p for p in group if frozenset((p[0],p[1]))==frozenset((0,1))]
def mul(p,q):
    return tuple(p[q[i]] for i in range(4))
cosets=[]
unseen=set(group)
while unseen:
    x=min(unseen)
    dc={mul(mul(h,x),k) for h in kernel for k in kernel}
    cosets.append(sorted(dc))
    unseen-=dc
assert len(group)==8 and len(kernel)==4 and len(cosets)==2
assert all(mul(p,q) in kernel for p in kernel for q in kernel)
output={"type":[3,0],"G0_vertex_genera":[0,1],
        "G0_edges":[[0,0],[1,1],[0,1]],
        "G1_vertex_genera":[1],"G1_edges":[[0,0],[0,0]],
        "G2_vertex_genera":[2],"G2_edges":[[0,0]],
        "Aut_G1_order":len(group),"loop_fixing_order":len(kernel),
        "double_coset_count":len(cosets),"double_cosets":cosets}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))

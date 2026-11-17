#!/usr/bin/env python3
"""Exact graph and arithmetic checks for the modular homology detector.

This computes the entire projective SL2(Z/12) deck group, its actual
Bass--Serre quotient graph, a rank-97 integral cycle basis, and the two
deck matrices in that basis. It is not a pentagon-shadow enumeration.
"""
from collections import deque, Counter
from pathlib import Path
import json
import numpy as np

MOD=12
I=(1,0,0,1)
def canon(a):
    a=tuple(x%MOD for x in a)
    return min(a,tuple((-x)%MOD for x in a))
def mul(a,b):
    return canon(tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%MOD
                       for i in range(2) for j in range(2)))
def inv(a):return canon((a[3],-a[1],-a[2],a[0]))
S=canon((0,1,-1,0));R=canon((0,-1,1,-1));I=canon(I)
elts=[I]; idx={I:0}
for a in elts:
    for b in (S,R):
        c=mul(a,b)
        if c not in idx:idx[c]=len(elts);elts.append(c)
assert len(elts)==576
def cyclic(g):
    out=[I];x=g
    while x!=I:out.append(x);x=mul(x,g)
    return tuple(out)
H2=cyclic(S);H3=cyclic(R)
assert len(H2)==2 and len(H3)==3
def cosets(H):
    which={};classes=[]
    for a in elts:
        if a in which:continue
        c=tuple(sorted(mul(a,h) for h in H))
        k=len(classes);classes.append(c)
        for b in c:which[b]=k
    return classes,which
C2,c2=cosets(H2);C3,c3=cosets(H3)
assert (len(C2),len(C3))==(288,192)
edges=[(c2[a],288+c3[a]) for a in elts]
adj=[[] for _ in range(480)]
for e,(u,v) in enumerate(edges):
    adj[u].append((v,e,1));adj[v].append((u,e,-1))
parent=[None]*480; parent[0]=(-1,-1,0); order=[0]; tree=set()
for u in order:
    for v,e,sgn in adj[u]:
        if parent[v] is None:
            parent[v]=(u,e,sgn);order.append(v);tree.add(e)
assert len(order)==480 and len(tree)==479
chords=[e for e in range(576) if e not in tree]
assert len(chords)==97
def root_path(v):
    d={}
    while v:
        u,e,sgn=parent[v];d[e]=sgn;v=u
    return d
cycles=[]
for e in chords:
    u,v=edges[e]
    # chord u->v, then v->root->u.
    d={e:1}
    for f,c in root_path(u).items():d[f]=d.get(f,0)+c
    for f,c in root_path(v).items():d[f]=d.get(f,0)-c
    d={f:c for f,c in d.items() if c}
    boundary=Counter()
    for f,c in d.items():
        a,b=edges[f];boundary[a]-=c;boundary[b]+=c
    assert all(c==0 for c in boundary.values())
    assert [d.get(f,0) for f in chords]==[int(e==f) for f in chords]
    cycles.append(d)
def matrix(g):
    gi=inv(g)
    # Coefficients on non-tree edges are cycle coordinates.
    return np.array([[d.get(idx[mul(gi,elts[e])],0) for d in cycles]
                     for e in chords],dtype=np.int64)
MS=matrix(S);MR=matrix(R);eye=np.eye(97,dtype=np.int64)
assert np.array_equal(MS@MS,eye)
assert np.array_equal(MR@MR@MR,eye)
traces={}
for g in elts:
    gi=inv(g)
    tr=sum(d.get(idx[mul(gi,elts[e])],0) for e,d in zip(chords,cycles))
    fixed2=sum(c2[mul(g,C[0])]==j for j,C in enumerate(C2))
    fixed3=sum(c3[mul(g,C[0])]==j for j,C in enumerate(C3))
    expected=(576 if g==I else 0)-fixed2-fixed3+1
    assert tr==expected
    if g!=I:assert 96<=97-tr<=384<576
    traces[g]=tr

# The actual tau^12 cusp in the oriented Bass--Serre quotient graph.
# A word syllable g->g*s or g->g*r crosses the two corresponding
# edge midpoints through a vertex of the appropriate type. Combining
# the two half-edge contributions gives an integral closed 1-cycle.
tau=mul(S,R);g=I;half=Counter()
for _ in range(12):
    gs=mul(g,S);half[idx[g]]-=1;half[idx[gs]]+=1
    gr=mul(gs,R);half[idx[gs]]+=1;half[idx[gr]]-=1
    g=gr
assert g==I and all(c%2==0 for c in half.values())
cusp={e:c//2 for e,c in half.items() if c}
bd=Counter()
for e,c in cusp.items():
    u,v=edges[e];bd[u]-=c;bd[v]+=c
assert all(c==0 for c in bd.values())
cusp_coordinates=[cusp.get(e,0) for e in chords]
assert set(cusp_coordinates)<={-1,0,1}
assert any(cusp_coordinates)
recon=Counter()
for a,d in zip(cusp_coordinates,cycles):
    for e,c in d.items():recon[e]+=a*c
assert {e:c for e,c in recon.items() if c}==cusp

def val(n,p):
    z=0
    while n%p==0:z+=1;n//=p
    return z
d=97
cross2=sum(val(3**i-1,2) for i in range(1,d+1))
cross3=sum(val(2**i-1,3) for i in range(1,d+1))
v2=5*d*d+d*(d-1)//2+cross2
v3=d*d+d*(d-1)//2+cross3
assert (cross2,cross3,v2,v3)==(239,70,51940,14135)
a2,a3=v2+2,v3+1
assert (6+d*a2,2+d*a3)==(5038380,1371194)
out={
 "deck_group_order":len(elts),"vertices":[len(C2),len(C3)],"edges":len(edges),
 "cycle_rank":len(chords),"chords":chords,
 "S":S,"R0":R,"deck_S":MS.tolist(),"deck_R0":MR.tolist(),
 "trace_histogram":dict(sorted(Counter(traces.values()).items())),
 "cusp_tau12":cusp_coordinates,
 "detector_modulus_prime_exponents":{"2":a2,"3":a3},
 "quotient_order_prime_exponents":{"2":6+d*a2,"3":2+d*a3},
 "scope":"Source homology detector only; no pentagon-shadow enumeration."
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print("Projective SL2(Z/12) order:",len(elts))
print("Bass--Serre graph vertices/edges:",len(C2)+len(C3),len(edges))
print("Integral cycle rank:",len(chords))
print("Exact deck orders S^2=R0^3=I: PASS")
print("All 576 integral deck traces:",dict(sorted(Counter(traces.values()).items())))
print("Deck faithfulness mod 576 by nonzero trace differences: PASS")
print("tau^12 cusp cycle primitive: PASS")
print("GL97(Z/576) cross valuations:",cross2,cross3)
print("GL97(Z/576) valuations at 2,3:",v2,v3)
print("Full multiplier modulus: 2^%d * 3^%d"%(a2,a3))
print("Underlying quotient order: 2^%d * 3^%d"%(6+d*a2,2+d*a3))
print("Certificate:",path.name)
print("No pentagon-shadow enumeration is claimed.")

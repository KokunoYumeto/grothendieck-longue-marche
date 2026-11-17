#!/usr/bin/env python3
"""Compute evaluation-pair derived subgroups in the actual F3 homology cover.

The calculation uses exact affine extension coordinates coming from the
Reidemeister--Schreier cellular complex. It decides whether the second
derived image of each pair is nilpotent; this is the criterion needed
for the already constructed relative-nilpotent gentle witness.
"""
import test_fivepoint_cm_level as T
import numpy as np
from pathlib import Path
import json

p=3;P=T.projections[p];dim=P.shape[1];Q=T.Q;tab=T.table
zero=np.zeros(dim,dtype=np.int16)
gpaths={0:()}
for q in T.C.order[1:]:
    prev,j=T.C.parent[q];gpaths[q]=gpaths[prev]+(j+1,)
unitrows=[]
for j in range(dim):
    e=np.zeros(dim,dtype=np.int16);e[j]=1
    unitrows.append(next(k for k in range(len(P)) if np.array_equal(P[k],e)))
gloops=[]
for k in unitrows:
    q,j=T.C.chords[k];h=int(tab[q,T.C.ig[j]])
    gloops.append(gpaths[q]+(j+1,)+T.inverse(gpaths[h]))
action_cache={0:np.eye(dim,dtype=np.int16)}
cocycle_cache={}
def action(q):
    if q not in action_cache:
        rows=[]
        for w in gloops:
            end,v=T.chain(q,w);assert end==q;rows.append(v@P%p)
        action_cache[q]=np.array(rows,dtype=np.int16)
    return action_cache[q]
def cocycle(q,h):
    key=(q,h)
    if key not in cocycle_cache:
        end,v=T.chain(q,gpaths[h]);assert end==int(tab[q,h])
        cocycle_cache[key]=v@P%p
    return cocycle_cache[key]
def mul(g,h):
    q,v=g;r,w=h
    return int(tab[q,r]),(v+w@action(q)+cocycle(q,r))%p
def inv(g):
    q,v=g;r=T.C.inverses[q]
    return r,(-(v+cocycle(q,r))@action(r))%p
def conj(g,h):return mul(mul(g,h),inv(g))
def comm(g,h):return mul(mul(mul(g,h),inv(g)),inv(h))
def evaluate(w):
    q,v=T.chain(0,w);return q,v@P%p

class Span:
    def __init__(self,rows=()):
        self.rows={}
        for row in rows:self.add(row)
    def add(self,row):
        v=np.array(row,dtype=np.int16)%p
        for j in sorted(self.rows):
            if v[j]:v=(v-int(v[j])*self.rows[j])%p
        nz=np.flatnonzero(v)
        if not len(nz):return False
        j=int(nz[0]);v=v*pow(int(v[j]),-1,p)%p
        self.rows[j]=v;return True
    def basis(self):return [self.rows[j] for j in sorted(self.rows)]
    def contains(self,row):
        v=np.array(row,dtype=np.int16)%p
        for j in sorted(self.rows):
            if v[j]:v=(v-int(v[j])*self.rows[j])%p
        return not np.any(v)

def subgroup(generators,extra=()):
    gens=[]
    seen=set()
    for q,v in generators:
        key=(q,tuple(int(a) for a in v))
        if key not in seen:seen.add(key);gens.append((q,v))
    lifts={0:zero.copy()};order=[0]
    for q in order:
        for g in gens:
            h,v=mul((q,lifts[q]),g)
            if h not in lifts:lifts[h]=v;order.append(h)
    U=Span()
    for q in order:
        for g in gens:
            h,v=mul((q,lifts[q]),g);U.add(v-lifts[h])
        for v in extra:U.add(v@action(q))
    # The Schreier vectors generate the complete kernel, and the following
    # closure check independently verifies invariance under the base image.
    for q in order:
        for v in U.basis():assert U.contains(v@action(q))
    # Choose a small generating set of the finite base and its actual lifts.
    H={0};basegens=[]
    for q in order:
        if q in H:continue
        basegens.append((q,lifts[q]))
        H={0};todo=[0]
        for h in todo:
            for k,v in basegens:
                n=int(tab[h,k])
                if n not in H:H.add(n);todo.append(n)
    assert H==set(order)
    return {"base":order,"lifts":lifts,"U":U,"basegens":basegens}

def derived(G):
    U=G["U"];gs=G["basegens"];H=G["base"];lifts=G["lifts"]
    M=Span()
    for q,v in gs:
        for u in U.basis():
            d=u@action(q)-u
            for h in H:M.add(d@action(h))
    cs=[]
    for i,g in enumerate(gs):
        for h in gs[:i]:
            c=comm(g,h)
            for q in H:cs.append(conj((q,lifts[q]),c))
    # Kernel commutators have zero base. Include them as actual generators.
    cs.extend((0,v) for v in M.basis())
    return subgroup(cs)

records=[]
for i,pair in enumerate(T.pairwords[:5],1):
    G=subgroup([evaluate(w) for w in pair]);D=derived(G);DD=derived(D)
    U2=DD["U"];moves=0
    for q in DD["base"]:
        for v in U2.basis():
            if np.any((v@action(q)-v)%p):moves+=1
    nilpotent=(len(DD["base"])==1 or
               (len(DD["base"])&(len(DD["base"])-1)==0 and moves==0))
    record={"pair":i,
            "base_orders":[len(X["base"]) for X in (G,D,DD)],
            "kernel_dimensions":[len(X["U"].rows) for X in (G,D,DD)],
            "second_derived_action_nonfixed_basis_pairs":moves,
            "second_derived_nilpotent_certified":nilpotent}
    records.append(record);print(record,flush=True)
out={"scope":"Exact second-derived evaluation images in the characteristic-three homology factor.",
     "records":records}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")

#!/usr/bin/env python3
"""Exact lower-central computation for the geometric A137 quotient.

No enumeration of the group of order 2^136 is used.  The actual covering
graph has 128 vertices and 256 directed generator edges.  Its cycle module
is represented by Python integer bitsets.  Each retained basis vector is
an unreduced original generator, so its commutator provenance is literal.
"""
from itertools import product
from pathlib import Path
import json


def encode(a,b,k):
    return (a%4)+4*(b%4)+16*(k%8)


def decode(g):
    return g%4,(g//4)%4,g//16


def pmul(g,h):
    a,b,k=decode(g)
    c,d,l=decode(h)
    if k%2:
        c,d=d,c
    return encode(a+c,b+d,k+l)


P=tuple(range(128))
ONE=0
PX=encode(1,0,0)
PY=encode(0,0,1)
PMUL=tuple(tuple(pmul(g,h) for h in P) for g in P)
PINV=tuple(next(h for h in P if PMUL[g][h]==ONE and PMUL[h][g]==ONE)
           for g in P)
PERM=tuple(tuple(2*PMUL[g][h]+e for h in P for e in range(2)) for g in P)


def act(g,v):
    ans=0
    perm=PERM[g]
    while v:
        low=v & -v
        ans ^= 1 << perm[low.bit_length()-1]
        v ^= low
    return ans


def boundary(v):
    ans=0
    while v:
        low=v & -v
        e=low.bit_length()-1
        g,label=divmod(e,2)
        h=PMUL[g][PX if label==0 else PY]
        ans ^= (1<<g) ^ (1<<h)
        v ^= low
    return ans


def qmul(a,b):
    v,g=a
    w,h=b
    return v ^ act(g,w),PMUL[g][h]


def qinv(a):
    v,g=a
    return act(PINV[g],v),PINV[g]


def comm(a,b):
    """The convention [a,b]=a b a^{-1} b^{-1}."""
    return qmul(qmul(qmul(a,b),qinv(a)),qinv(b))


X=(1,PX)
Y=(2,PY)
E=(0,ONE)


def qpow(a,n):
    if n<0:
        return qpow(qinv(a),-n)
    ans=E
    for _ in range(n):
        ans=qmul(ans,a)
    return ans


def lift(g):
    a,b,k=decode(g)
    B=qmul(qmul(Y,X),qinv(Y))
    return qmul(qmul(qpow(X,a),qpow(B,b)),qpow(Y,k))


def independent_originals(candidates):
    pivots={}
    originals=[]
    for v,meta in candidates:
        w=v
        while w:
            p=w.bit_length()-1
            if p in pivots:
                w ^= pivots[p]
            else:
                pivots[p]=w
                originals.append((v,meta))
                break
    return originals


def in_span(v,basis):
    pivots={}
    for w,_ in basis:
        while w:
            p=w.bit_length()-1
            if p in pivots:
                w ^= pivots[p]
            else:
                pivots[p]=w
                break
    while v:
        p=v.bit_length()-1
        if p not in pivots:
            return False
        v ^= pivots[p]
    return True


def main():
    # All P products and the exact deck action are checked.
    assert all(PMUL[PMUL[a][b]][c]==PMUL[a][PMUL[b][c]]
               for a,b,c in product(P,repeat=3))
    assert all(PMUL[PINV[g]][g]==ONE for g in P)
    assert all(len(set(perm))==256 for perm in PERM)
    assert all(boundary(act(g,1<<e)) ==
               ((1<<PMUL[g][e//2]) ^
                (1<<PMUL[g][PMUL[e//2][PX if e%2==0 else PY]]))
               for g in P for e in range(256))
    assert qpow(X,4)[1]==ONE and qpow(Y,8)[1]==ONE
    assert qmul(lift(PX),lift(PY))[1]==PMUL[PX][PY]
    assert all(lift(g)[1]==g and
               boundary(lift(g)[0])==((1<<ONE)^(1<<g)) for g in P)
    print("PASS: all 2,097,152 associative P products, all deck-edge boundaries, "
          "and canonical actual word lifts.",flush=True)

    c=comm(X,Y)
    assert c[1]!=ONE
    gamma3=[comm(c,Z) for Z in (X,Y)]
    assert any(z[1]!=ONE for z in gamma3)
    seeds=[comm(z,Z) for z in gamma3 for Z in (X,Y)]
    assert all(g==ONE and boundary(v)==0 for v,g in seeds)
    print("Weight-four seeds XX,XY,YX,YY edge supports:",
          [v.bit_count() for v,g in seeds],flush=True)
    print("P has class3, with literal third and fourth commutator tests.",flush=True)

    candidates=[]
    for seed_index,(v,_) in enumerate(seeds):
        for g in P:
            w=act(g,v)
            actual=qmul(qmul(lift(g),seeds[seed_index]),qinv(lift(g)))
            assert actual==(w,ONE)
            candidates.append((w,dict(seed=seed_index,translate=g,tail="")))
    basis=independent_originals(candidates)
    dims=[]
    layers=[]
    k=4
    previous=None
    while True:
        dims.append((k,len(basis)))
        assert all(boundary(v)==0 for v,_ in basis)
        assert all(in_span(act(g,v),basis) for v,_ in basis for g in (PX,PY))
        print(f"dim_F2 Gamma_{k}(Q) = {len(basis)}",flush=True)
        layers.append(dict(weight=k,dimension=len(basis),
                           basis=[dict(vector_hex=hex(v),**meta)
                                  for v,meta in basis]))
        if not basis:
            break
        previous=(k,basis)
        candidates=[]
        for v,meta in basis:
            for label,g,Z in (("X",PX,X),("Y",PY,Y)):
                w=v ^ act(g,v)
                assert comm((v,ONE),Z)==(w,ONE)
                candidates.append((w,dict(meta,tail=meta["tail"]+label)))
        basis=independent_originals(candidates)
        k+=1
        assert k<=40

    deepest_weight,deep_basis=previous
    v,meta=deep_basis[0]
    w=seeds[meta["seed"]]
    pword=lift(meta["translate"])
    w=qmul(qmul(pword,w),qinv(pword))
    for label in meta["tail"]:
        w=comm(w,X if label=="X" else Y)
    assert w==(v,ONE) and v
    assert comm(w,X)==E and comm(w,Y)==E
    edges=[i for i in range(256) if (v>>i)&1]
    witness=dict(weight=deepest_weight,seed=["XX","XY","YX","YY"][meta["seed"]],
                 conjugating_P=decode(meta["translate"]),tail=meta["tail"],
                 vector_hex=hex(v),directed_edges=edges,
                 edge_vertices_labels=[dict(vertex=decode(i//2),
                                            label="X" if i%2==0 else "Y")
                                       for i in edges])
    assert len(edges)==v.bit_count()
    assert edges==list(range(0,256,2))
    print("DEEPEST NONZERO ACTUAL COMMUTATOR",json.dumps(
        {**{k:witness[k] for k in ("weight","seed","conjugating_P","tail","vector_hex")},
         "support_size":len(edges),"support":"all 128 X-edges"},
        sort_keys=True),flush=True)
    print("Exact nilpotency class:",deepest_weight,flush=True)
    print("NEXT LAYER IS ZERO; every previous nonzero vector has literal commutator provenance.",
          flush=True)
    Path(__file__).with_name("harmonic_quotient_class_data.json").write_text(
        json.dumps(dict(group_order_log2=136,cycle_rank=129,
                        commutator_convention="aba^-1b^-1",
                        dimensions=dims,witness=witness,layers=layers),indent=2)+"\n")
    print("ALL COVER-GRAPH LOWER-CENTRAL CERTIFICATES PASSED.",flush=True)


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Exploratory exact integral scaled-log model for the class-three pro-3 group.

Coordinates (v,Z,T) mean log=(v,Z/2,T/12) in the free class-three Lie
algebra on ten generators, with the 330 ordinary degree-three Lyndon
brackets.  All multiplication and based action matrices are integral.
The actual pro-3 group is the lattice T-T0(v,Z) in 3 Z3^330;
the omitted factor four is a unit.  This congruence is retained.
This file is separate from all accepted checkpoint05/E44 programs.
"""
from pathlib import Path
from itertools import product,combinations
import json,time
import numpy as np
import de_fermat_schreier as f
import bc_fermat_class_two_integral_model as old
import bc_fermat_class_three_burnside as finite

HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(10),2));PI,PJ=np.array(PAIRS).T

def lyndon(w):return all(w<w[i:]+w[:i] for i in range(1,len(w)))
def tensor_bracket(a,b):
    out={}
    for u,x in a.items():
        for v,y in b.items():
            out[u+v]=out.get(u+v,0)+x*y
            out[v+u]=out.get(v+u,0)-x*y
    return {w:a for w,a in out.items() if a}
def lyndon_expansion(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return tensor_bracket(lyndon_expansion(w[:i]),lyndon_expansion(w[i:]))

WORDS=[w for w in product(range(10),repeat=3) if lyndon(w)]
assert len(WORDS)==330
TENSOR_WORDS=list(product(range(10),repeat=3));TENSOR_INDEX={w:i for i,w in enumerate(TENSOR_WORDS)}
EXPANSIONS=[lyndon_expansion(w) for w in WORDS]
assert all(min(e)==w and e[w]==1 for w,e in zip(WORDS,EXPANSIONS))
LIE_TENSOR=np.zeros((1000,330),dtype=np.int64)
for j,expansion in enumerate(EXPANSIONS):
    for word,a in expansion.items():LIE_TENSOR[TENSOR_INDEX[word],j]=a

BRACKET_TENSOR=np.zeros((1000,450),dtype=np.int64)
for i in range(10):
    for p,(j,k) in enumerate(PAIRS):
        expansion=tensor_bracket({(i,):1},tensor_bracket({(j,):1},{(k,):1}))
        for word,a in expansion.items():BRACKET_TENSOR[TENSOR_INDEX[word],45*i+p]=a
residual=BRACKET_TENSOR.copy();BRACKET=np.zeros((330,450),dtype=np.int64)
for i,(word,expansion) in enumerate(zip(WORDS,EXPANSIONS)):
    coefficient=residual[TENSOR_INDEX[word]].copy();BRACKET[i]=coefficient
    for w,a in expansion.items():residual[TENSOR_INDEX[w]]-=a*coefficient
assert not np.any(residual)
assert np.array_equal(LIE_TENSOR@BRACKET,BRACKET_TENSOR)
BRACKET_BY_GENERATOR=BRACKET.reshape(330,10,45)
DIM=385
ZERO=np.zeros(DIM,dtype=np.int64)
GENERATORS=np.eye(DIM,dtype=np.int64)[:10]

def wedge(v,w):return v[PI]*w[PJ]-v[PJ]*w[PI]
def bracket(v,z):return BRACKET@np.outer(v,z).ravel()
def multiply(g,h):
    v,Z,T=g[:10],g[10:55],g[55:]
    w,W,U=h[:10],h[10:55],h[55:]
    vw=wedge(v,w)
    return np.r_[v+w,Z+W+vw,T+U+3*(bracket(v,W)-bracket(w,Z))+bracket(v-w,vw)]
def inverse(g):return -g
def commutator(g,h):return multiply(multiply(multiply(g,h),-g),-h)
def collect_signed(word):
    out=ZERO.copy()
    for letter in word:
        generator=GENERATORS[abs(letter)-1]*(1 if letter>0 else -1)
        out=multiply(out,generator)
    return out
def literal(word):return collect_signed(f.schreier(word))

COMMUTATOR_THIRD=np.stack([
    BRACKET_BY_GENERATOR[:,i,p]+BRACKET_BY_GENERATOR[:,j,p]
    for p,(i,j) in enumerate(PAIRS)],axis=1)

def canonical(v,Z):
    base=ZERO.copy()
    for i,a in enumerate(v):
        if a:base=multiply(base,int(a)*GENERATORS[i])
    difference=Z-base[10:55]
    T=base[55:]+3*COMMUTATOR_THIRD@difference+3*bracket(v,difference)
    return np.r_[v,Z,T]

def in_group_lattice(g):return not np.any((g[55:]-canonical(g[:10],g[10:55])[55:])%3)

PROJECTION=np.stack([finite.tensor_projection({w:a%3 for w,a in expansion.items()})
                     for expansion in EXPANSIONS],axis=1)

def projection_exp3(g):
    base=canonical(g[:10],g[10:55]);difference=g[55:]-base[55:]
    assert not np.any(difference%3)
    central=(difference//3)%3 # 12/3=4 is one modulo three.
    v=g[:10]%3;z=2*g[10:55]%3
    t=(finite.canonical_triple(v,z)+PROJECTION@central)%3
    return np.r_[v,z,t]

def degree_three_action(a):
    columns=[]
    for word in WORDS:
        i=next(i for i in range(1,3) if lyndon(word[i:]))
        x,y,z=word
        if i==1:columns.append(bracket(a[:,x],wedge(a[:,y],a[:,z])))
        else:columns.append(-bracket(a[:,z],wedge(a[:,x],a[:,y])))
    return np.stack(columns,axis=1)

def action(images):
    columns=np.stack([literal(old.substitute(w,images)) for w in f.NWORDS],axis=1)
    A=columns[:10];J=columns[10:55]
    out=np.zeros((DIM,DIM),dtype=np.int64)
    out[:,:10]=columns
    out[10:55,10:55]=old.exterior(A)
    out[55:,10:55]=np.stack([3*(bracket(A[:,i],J[:,j])-bracket(A[:,j],J[:,i]))
                             for i,j in PAIRS],axis=1)
    out[55:,55:]=degree_three_action(A)
    return out

S=action(([2],[1]));R=action(([2],[-2,-1]))

def norm_errors(g):
    first=multiply(S@g,g)
    second=multiply(multiply(-g,R@(-g)),R@R@(-g))
    return np.r_[first,second]

def main():
    start=time.time();rng=np.random.default_rng(2026111344)
    assert np.array_equal(S@S,np.eye(DIM,dtype=np.int64))
    assert np.array_equal(R@R@R,np.eye(DIM,dtype=np.int64))
    assert np.array_equal(S[:55,:55],old.S) and np.array_equal(R[:55,:55],old.R)
    for i,j in PAIRS:
        c=commutator(GENERATORS[i],GENERATORS[j]);p=PAIRS.index((i,j))
        assert not np.any(c[:10])
        expected=np.zeros(45,dtype=np.int64);expected[p]=2
        assert np.array_equal(c[10:55],expected)
        assert np.array_equal(c[55:],6*COMMUTATOR_THIRD[:,p])
    for _ in range(20):
        states=[]
        for __ in range(3):
            v=rng.integers(-2,3,size=10);Z=rng.integers(-2,3,size=45)
            g=canonical(v,Z);g[55:]+=12*rng.integers(-2,3,size=330);states.append(g)
            assert in_group_lattice(g)
        a,b,c=states
        assert np.array_equal(multiply(multiply(a,b),c),multiply(a,multiply(b,c)))
        assert in_group_lattice(multiply(a,b))
        assert np.array_equal(multiply(a,b)[:55],old.multiply(a[:55],b[:55]))
        assert np.array_equal(projection_exp3(multiply(a,b)),finite.multiply(projection_exp3(a),projection_exp3(b)))
        for act,act3 in ((S,finite.S),(R,finite.R)):
            assert np.array_equal(act@multiply(a,b),multiply(act@a,act@b))
            assert in_group_lattice(act@a)
            assert np.array_equal(projection_exp3(act@a),act3(projection_exp3(a)))
    for _ in range(20):
        word=rng.choice(np.r_[np.arange(1,11),-np.arange(1,11)],size=30).tolist()
        g=collect_signed(word)
        assert in_group_lattice(g)
        assert np.array_equal(projection_exp3(g),finite.collect_signed(word))
    triple_norm=np.vstack((np.eye(330,dtype=np.int64)+S[55:,55:],
         -np.eye(330,dtype=np.int64)-R[55:,55:]-R[55:,55:]@R[55:,55:]))
    assert not np.any(S[55:,10:55]%3) and not np.any(R[55:,10:55]%3)
    result={"status":"exploratory integral representation; no full lifting claim yet",
        "coordinates":"log=(v,Z/2,T/12) in the ordinary free class-three Lie algebra",
        "dimensions":[10,45,330],"exact_group_lattice":"T-T0(v,Z) in 3 Z3^330",
        "all_product_and_based_action_matrices_integral":True,
        "ordinary_Lyndon_basis_and_exact_tensor_comparison":True,
        "exact_projection_to_E37_and_E44":True,
        "S_squared_R_cubed_identity_over_Z":True,
        "triple_norm_shape":list(triple_norm.shape),
        "elapsed_seconds":round(time.time()-start,3)}
    (HERE/"bc_fermat_class_three_integral.json").write_text(json.dumps(result,indent=2)+"\n")
    np.savez_compressed(HERE/"bc_fermat_class_three_integral.npz",S=S,R=R,
        bracket=BRACKET,lie_tensor=LIE_TENSOR,lyndon_words=np.array(WORDS),
        projection_exp3_central=PROJECTION,triple_norm=triple_norm,
        commutator_third=COMMUTATOR_THIRD)
    print(json.dumps(result,indent=2))
    print("PASS: exact integral scaled-log class-three group lattice and based action.")

if __name__=="__main__":main()

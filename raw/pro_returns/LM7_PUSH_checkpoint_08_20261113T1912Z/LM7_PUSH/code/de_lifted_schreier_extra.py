#!/usr/bin/env python3
"""Exact elementary-abelian kernel above a faithful permutation quotient.

At each stabilizer-chain level all Schreier generators are rewritten
through the next levels.  Their actual lifted discrepancies generate
the kernel normally.  The saved word DAG is in the original generators.
"""
import time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation
from de_ferrari_two_core import Span2

def lifted_kernel(H,generators,permutations,vector,element,width,known_order=None,
                  extra_lifts=(),normalizers=()):
    start=time.time();G=PermutationGroup(permutations);G.schreier_sims();order=int(G.order())
    if known_order is not None:assert order==known_order
    print('permutation base order',order,'base length',len(G.base),'strong generators',len(G.strong_gens),flush=True)
    allgenerators=list(generators)+[g for p,g in extra_lifts]+list(normalizers)
    nodes=[{'identity':True}]+[{'generator':i} for i in range(len(allgenerators))]
    normal_generators=list(generators)+list(normalizers)
    normal_nodes=list(range(1,len(generators)+1))+list(range(1+len(generators)+len(extra_lifts),1+len(allgenerators)))
    inverse_nodes={0:0}
    def invnode(i):
        if i not in inverse_nodes:
            j=len(nodes);nodes.append({'inverse':i});inverse_nodes[i]=j;inverse_nodes[j]=i
        return inverse_nodes[i]
    def prodnode(factors):
        factors=[i for i in factors if i]
        if not factors:return 0
        if len(factors)==1:return factors[0]
        i=len(nodes);nodes.append({'product':factors});return i
    identity=Permutation(list(range(permutations[0].size)))
    lifts={identity:(H.one,0)}
    for i,(p,g) in enumerate(zip(permutations,generators)):
        if p in lifts:assert np.array_equal(vector(H.mul(g,H.inv(lifts[p][0]))),np.zeros(width,dtype=np.int64))
        lifts[p]=(g,i+1);lifts[p**-1]=(H.inv(g),invnode(i+1))
    def liftstrong(p):
        if p in lifts:return lifts[p]
        if p**-1 in lifts:
            g,node=lifts[p**-1];lifts[p]=(H.inv(g),invnode(node));return lifts[p]
        if p in G._strong_gens_slp:
            parts=list(reversed(G._strong_gens_slp[p]))
            assert parts!=[p]
            out=H.one;check=identity;ns=[]
            for f in parts:
                g,node=liftstrong(f);out=H.mul(out,g);check=check*f;ns.append(node)
            assert check==p;lifts[p]=(out,prodnode(ns));return lifts[p]
        assert p**-1 in G._strong_gens_slp
        g,node=liftstrong(p**-1);lifts[p]=(H.inv(g),invnode(node));return lifts[p]
    for p in G.strong_gens:liftstrong(p)
    trans=[]
    for i,tr in enumerate(G.basic_transversals):
        layer={}
        for q,p in tr.items():
            parts=[G.strong_gens[j] for j in reversed(G._transversal_slp[i][q])]
            out=H.one;check=identity;ns=[]
            for f in parts:
                g,node=liftstrong(f);out=H.mul(out,g);check=check*f;ns.append(node)
            assert check==p;layer[q]=(out,prodnode(ns))
        trans.append(layer)
    def canonical(p):
        indices=G.coset_factor(p,True);assert len(indices)==len(G.base)
        out=H.one;ns=[];check=identity
        for i in reversed(range(len(indices))):
            q=indices[i]
            if q==G.base[i]:continue
            g,node=trans[i][q];out=H.mul(out,g);ns.append(node);check=check*G.basic_transversals[i][q]
        assert check==p
        return out,ns
    S=Span2(width);relation_count=0;normal_additions=0
    def normal_close():
        nonlocal normal_additions
        at=0
        while at<len(S.basis):
            v=S.basis[at];g=element(v);node=S.words[at]
            for a,anode in zip(normal_generators,normal_nodes):
                w=vector(H.conj(a,g))
                if np.any(S.reduce(w)[0]):
                    n=prodnode([anode,node,invnode(anode)]);S.add(w,n);normal_additions+=1
            at+=1
    for extra_index,(p,g) in enumerate(extra_lifts):
        canon,canonical_nodes=canonical(p)
        v=vector(H.mul(g,H.inv(canon)));relation_count+=1
        if np.any(S.reduce(v)[0]):
            node=prodnode([1+len(generators)+extra_index]+[invnode(j) for j in reversed(canonical_nodes)])
            S.add(v,node);normal_close()
    print('extra lift relations',len(extra_lifts),'initial kernel rank',len(S.basis),flush=True)
    for i,basepoint in enumerate(G.base):
        sg=[s for s in G.strong_gens if all(s(b)==b for b in G.base[:i])]
        before=len(S.basis)
        for q,uq in G.basic_transversals[i].items():
            gu,nu=trans[i][q]
            for s in sg:
                target=s(q);ut=G.basic_transversals[i][target];gt,nt=trans[i][target]
                gs,ns=liftstrong(s);p=uq*s*(ut**-1)
                assert all(p(b)==b for b in G.base[:i+1])
                canonical_value,canonical_nodes=canonical(p)
                residual=H.mul(H.mul(H.mul(gu,gs),H.inv(gt)),H.inv(canonical_value))
                v=vector(residual);relation_count+=1
                if np.any(S.reduce(v)[0]):
                    node=prodnode([nu,ns,invnode(nt)]+[invnode(j) for j in reversed(canonical_nodes)])
                    S.add(v,node);normal_close()
        print('Schreier level',i,'orbit',len(G.basic_orbits[i]),'relations',relation_count,
              'kernel rank',len(S.basis),'new rank',len(S.basis)-before,flush=True)
    # The stored module is normal and consists of actual lifted relators.
    normal_close()
    for v in S.basis:
        for g in normal_generators:S.coordinates(vector(H.conj(g,element(v))))
    # Re-evaluate every saved word-DAG node independently of the lift cache.
    values=[]
    for node in nodes:
        if 'identity' in node:values.append(H.one)
        elif 'generator' in node:values.append(allgenerators[node['generator']])
        elif 'inverse' in node:values.append(H.inv(values[node['inverse']]))
        else:
            out=H.one
            for j in node['product']:out=H.mul(out,values[j])
            values.append(out)
    for v,node in zip(S.basis,S.words):assert np.array_equal(vector(values[node]),v)
    return G,S,{'base_order':order,'base_length':len(G.base),
        'strong_generator_count':len(G.strong_gens),'Schreier_relation_count':relation_count,
        'complete_kernel_dimension':len(S.basis),'normal_closure_additions':normal_additions,
        'extra_lift_relations':len(extra_lifts),'additional_normalizers':len(normalizers),
        'lifted_group_order':order*2**len(S.basis),'literal_word_DAG':nodes,
        'kernel_basis_word_nodes':S.words,'all_saved_relator_words_independently_replayed':True,
        'seconds':round(time.time()-start,3)}

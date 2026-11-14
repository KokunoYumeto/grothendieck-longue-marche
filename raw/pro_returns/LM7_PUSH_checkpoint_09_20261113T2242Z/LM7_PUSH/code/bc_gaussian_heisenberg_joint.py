#!/usr/bin/env python3
"""All 3456 actual E66/E68/Gaussian-central-layer word preimages.

The accepted E68 source and certificates are read only. Six exact words
with trivial retained E66 value are lifted through its saved Schreier
certificate. Their three commutators supply the entire new central
kernel, and extend each of the 1152 old words in all three possible ways.
"""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from de_a6_schreier_certificate import read_certificate,verify_words
from a_cm_distribution_orbifold import OrbifoldExport
from bc_gaussian_heisenberg_structure import Evaluations,gaussian_graph,graph_vector

HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic();E=Evaluations();export=OrbifoldExport()
    upper=read_certificate(HERE/'a_cm_distribution_orbifold_N_derived.bin')
    lower=read_certificate(HERE/'a_cm_distribution_orbifold_projected.bin')
    verify_words(upper);verify_words(lower)
    old=np.load(HERE/'a_cm_distribution_orbifold_witnesses.npz')
    joint=np.load(HERE/'a_cm_distribution_orbifold.npz')
    assert upper['derived'] and not lower['derived']
    points=joint['retained_projection_points'];n=len(points);fulln=upper['degree']
    assert (n,fulln)==(4957,5331)
    inverse=np.full(fulln,-1,dtype=np.int64);inverse[points]=np.arange(n)
    assert np.array_equal(inverse[upper['strong'][:,points]],lower['original'])
    nodes=[tuple(map(int,row)) for row in old['word_DAG']]
    assert nodes[:len(upper['nodes'])]==[tuple(map(int,row)) for row in upper['nodes']]

    def make(op,a,b=0):
        if op==2:
            if not a:return b
            if not b:return a
        nodes.append((op,int(a),int(b)));return len(nodes)-1

    mapping=[]
    for op,a,b in lower['nodes']:
        op,a,b=map(int,(op,a,b))
        if op==0:v=0
        elif op==1:v=int(upper['words'][a])
        else:v=make(op,mapping[a],mapping[b] if op in (2,4,5) else 0)
        mapping.append(v)
    strongnodes=[mapping[int(i)] for i in lower['words']]
    one=np.arange(n,dtype=np.uint16);levels=[]
    for lev,base in enumerate(lower['base']):
        gens=[(g,node) for g,node,depth in zip(lower['strong'],strongnodes,lower['depths'])
              if depth>=lev]
        orbit=[int(base)];trans=[one];words=[0];at={int(base):0}
        for k,v in enumerate(orbit):
            for g,gnode in gens:
                w=int(g[v])
                if w not in at:
                    at[w]=len(orbit);orbit.append(w);trans.append(g[trans[k]])
                    words.append(make(2,words[k],gnode))
        levels.append((int(base),{v:(np.argsort(t).astype(np.uint16),w)
                                  for v,t,w in zip(orbit,trans,words)}))

    def preimage(p):
        h=p;answer=0
        for base,trans in levels:
            v=int(h[base])
            if v==base:continue
            ti,w=trans[v];h=ti[h];answer=make(2,w,answer)
        assert np.array_equal(h,one)
        return answer

    # Prescribe six horizontal basis vectors and zero Mordell/E66 values.
    horizontal=[];desired=[]
    for i in range(6):
        coords=[0]*9;coords[3*(i//2)+i%2]=1
        gs=[tuple(coords[3*j:3*j+3])+(0,) for j in range(3)]
        v=graph_vector(0,0,0,*gs)
        oldv=list(v[:12])+[v[12+3*j+k] for j in range(6) for k in range(2)]
        p=np.r_[np.arange(4849,dtype=np.uint16),4849+export.translations(oldv)]
        horizontal.append(preimage(p));desired.append(p)
    central=[make(4,horizontal[2*j],horizontal[2*j+1]) for j in range(3)]

    # Replay these six lifts and their commutators in the original full
    # 5331-point source. The claim needed here is its actual E66 projection.
    wanted=set(horizontal+central);ancestors=set(wanted);todo=list(wanted)
    while todo:
        op,a,b=nodes[todo.pop()]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if j not in ancestors:ancestors.add(j);todo.append(j)
    values={};fullone=np.arange(fulln,dtype=np.uint16)
    for i in sorted(ancestors):
        op,a,b=nodes[i]
        if op==0:v=fullone
        elif op==1:v=upper['original'][a]
        elif op==2:v=values[b][values[a]]
        elif op==3:v=np.argsort(values[a]).astype(np.uint16)
        elif op==4:v=np.argsort(values[b])[np.argsort(values[a])[values[b][values[a]]]]
        elif op==5:v=np.argsort(values[a])[values[b][values[a]]]
        else:raise AssertionError(op)
        values[i]=v
    for node,p in zip(horizontal,desired):assert np.array_equal(inverse[values[node][points]],p)
    for node in central:assert np.array_equal(inverse[values[node][points]],one)
    full_old_central_identity=[bool(np.array_equal(values[node][:5223],fullone[:5223])) for node in central]
    del values

    nwords=json.loads((HERE/'bc_cm_literal_words.json').read_text())['N_B_basis_in_F']
    indices=list(map(int,old['original_N_indices']))
    metadata=json.loads((HERE/'a_cm_distribution_orbifold_witnesses.json').read_text())
    assert [nwords[j] for j in indices]==metadata['original_N_words_in_F']
    nv=[E.word(nwords[j]) for j in indices]

    def evaluate_nodes(wanted):
        ancestors=set(wanted);todo=list(wanted)
        while todo:
            op,a,b=nodes[todo.pop()]
            for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
                if j not in ancestors:ancestors.add(j);todo.append(j)
        vals={}
        for i in sorted(ancestors):
            op,a,b=nodes[i]
            if op==0:v=E.one
            elif op==1:v=nv[a]
            elif op==2:v=E.mul(vals[a],vals[b])
            elif op==3:v=E.inv(vals[a])
            elif op==4:v=E.comm(vals[a],vals[b])
            elif op==5:v=E.conj(vals[a],vals[b])
            else:raise AssertionError(op)
            vals[i]=v
        return vals,len(ancestors)

    previous=list(map(int,old['witness_nodes']))
    vals,oldanc=evaluate_nodes(set(previous+horizontal+central))
    expected_central=[]
    for j,node in enumerate(central):
        h=[E.G.one]*3;h[j]=E.G.C
        v=graph_vector(0,0,0,*h);expected_central.append(v)
        assert E.vector(vals[node])==v
    # These are the three exact central basis preimages. They kill Psi
    # and every old orbifold coordinate, rather than merely their norms.
    model=json.loads((HERE/'bc_gaussian_heisenberg_model.json').read_text())
    source=json.loads((HERE/'bc_gaussian_heisenberg_source.json').read_text())
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    fvalues=[E.word(r['actual_commutator_word_f']) for r in origins]
    final=[];parameters=[];expected=[];byold=[]
    for oi,(oldnode,param) in enumerate(zip(previous,old['witness_parameters'])):
        index,fi,ti=map(int,param[:3]);exp=export.meta['families']['E17_E62_actual'][index]
        target=exp['complete_four_finite_norm_values'][ti]
        oldabsolute=target['absolute_twelve_translation_target']
        complete=E.mul(fvalues[index],vals[oldnode]);cv=E.vector(complete)
        assert list(cv[:12])+[cv[12+3*j+k] for j in range(6) for k in range(2)]==oldabsolute
        choices=[]
        for allowed in source['records'][index]['allowed']:
            gi=allowed['Gaussian_framed_target_index'];gr=model['records'][gi]
            gs=tuple(tuple(g) for g in gr['six_absolute_values'])
            if [c for g in gs for c in g[:2]]!=oldabsolute[12:]:continue
            absolute=tuple((tuple(oldabsolute[2*j:2*j+2]),0) for j in range(6))+gs
            delta=E.vector(E.mul(E.inv(complete),absolute))
            coeff=[delta[14],delta[17],delta[20]]
            check=tuple(sum(c*v[k] for c,v in zip(coeff,expected_central))%3 for k in range(30))
            assert delta==check
            node=oldnode
            for c,cn in zip(coeff,central):
                if c==1:node=make(2,node,cn)
                elif c==2:node=make(2,node,make(3,cn))
            final.append(node);parameters.append([int(x) for x in param]+[gi])
            expected.append(absolute);choices.append(gi)
        assert len(choices)==3;byold.append(choices)
    assert len(final)==3456
    finalvals,finalanc=evaluate_nodes(final)
    for node,pa,target in zip(final,parameters,expected):
        assert E.mul(fvalues[pa[0]],finalvals[node])==target
    # Central correction identity in the retained old source, together
    # with E68's exact predecessor replay, proves all old values at once.
    out={'status':'PASS_ALL_3456_LITERAL_E66_GAUSSIAN_CENTRAL_LAYER_WORDS',
         'previous_actual_E68_words':1152,'new_words':len(final),
         'new_framed_lifts_per_previous_value':3,
         'finite_correction_image_order':356241767399424*3**12,
         'exact_common_quotient_order':1,
         'common_quotient_proof':'Every nontrivial finite 3-group quotient has a C3 quotient. '
             'The actual L to E67 projection is L_ab, whose product with Psi is E68.',
         'six_horizontal_basis_nodes':horizontal,'three_central_basis_nodes':central,
         'three_central_basis_vectors':expected_central,
         'full_source_ancestors_for_six_generic_lifts':len(ancestors),
         'central_basis_has_identity_retained_E66_and_E67_value':True,
         'central_basis_has_identity_all_5223_old_induced_points':full_old_central_identity,
         'new_twelve_group_ancestors_replayed':finalanc,
         'parameter_columns':metadata['parameter_columns']+['Gaussian_central_framed_target'],
         'original_N_indices':indices,
         'original_N_words_in_F':[nwords[j] for j in indices],
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{f:hashlib.sha256((HERE/f).read_bytes()).hexdigest() for f in
            ['bc_gaussian_heisenberg_structure.py','bc_gaussian_heisenberg_structure.json',
             'bc_gaussian_heisenberg_model.json','bc_gaussian_heisenberg_source.json',
             'bc_orbifold_CM_export.json','bc_orbifold_CM_export.npz',
             'a_cm_distribution_orbifold_N_derived.bin','a_cm_distribution_orbifold_projected.bin',
             'a_cm_distribution_orbifold.npz','a_cm_distribution_orbifold_witnesses.npz',
             'a_cm_distribution_orbifold_witnesses.json','de_ferrari_fibres.json']},
         'scope':'Exact common retained finite maps and full word-kernel cosets in f_i Nprime. '
                 'No larger-source generation or full-GT lift is assigned.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'bc_gaussian_heisenberg_joint.npz',
                       word_DAG=np.array(nodes,dtype=np.uint32),
                       witness_nodes=np.array(final,dtype=np.uint32),
                       witness_parameters=np.array(parameters,dtype=np.int64),
                       original_N_indices=np.array(indices,dtype=np.uint32),
                       central_nodes=np.array(central,dtype=np.uint32),
                       central_vectors=np.array(expected_central,dtype=np.uint8),
                       successful_targets=np.array([E.vector(a) for a in expected],dtype=np.uint8),
                       predecessor_word_nodes=old['witness_nodes'])
    (HERE/'bc_gaussian_heisenberg_joint.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
                     ['input_sha256','original_N_words_in_F','three_central_basis_vectors']},indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Actual N_B-prime preimages for every simultaneous E66/E62/E67 value."""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

from de_a6_schreier_certificate import read_certificate,verify_words
from de_ferrari_a6_source_data import load_data


HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic()
    upper=read_certificate(HERE/'a_cm_distribution_orbifold_N_derived.bin')
    lower=read_certificate(HERE/'a_cm_distribution_orbifold_projected.bin')
    verify_words(upper);verify_words(lower)
    assert upper['derived'] and not lower['derived']
    data=np.load(HERE/'a_cm_distribution_orbifold.npz')
    points=data['retained_projection_points']
    expected=data['successful_membership_values']
    parameters=data['successful_membership_parameters']
    fulln=upper['degree'];n=len(points)
    inverse=np.full(fulln,-1,dtype=np.int64)
    inverse[points]=np.arange(n)
    assert fulln==5331 and n==4957
    assert np.array_equal(inverse[upper['strong'][:,points]],lower['original'])
    nodes=[tuple(map(int,row)) for row in upper['nodes']]

    def product(a,b):
        if not a:return b
        if not b:return a
        nodes.append((2,a,b));return len(nodes)-1

    mapping=[]
    for op,a,b in lower['nodes']:
        op,a,b=map(int,(op,a,b))
        if op==0:v=0
        elif op==1:v=int(upper['words'][a])
        else:
            nodes.append((op,mapping[a],mapping[b] if op in (2,4,5) else 0))
            v=len(nodes)-1
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
                    at[w]=len(orbit);orbit.append(w)
                    trans.append(g[trans[k]])
                    words.append(product(words[k],gnode))
        levels.append((int(base),{v:(np.argsort(t).astype(np.uint16),w)
                                  for v,t,w in zip(orbit,trans,words)}))

    def preimage(p):
        h=p;answer=0
        for base,trans in levels:
            v=int(h[base])
            if v==base:continue
            ti,w=trans[v]
            h=ti[h]
            answer=product(w,answer)
        assert np.array_equal(h,one)
        return answer

    wanted=[preimage(p) for p in expected]
    ancestors=set(wanted);todo=list(wanted)
    while todo:
        i=todo.pop();op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            assert 0<=j<i
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
    for node,p in zip(wanted,expected):
        assert np.array_equal(inverse[values[node][points]],p)
    result=json.loads((HERE/'a_cm_distribution_orbifold.json').read_text())
    indices=result['common_N_source']['selected_original_indices']
    source=load_data()
    assert np.array_equal(upper['original'],data['common_N'][indices])
    assert len(wanted)==1152 and result['exact_common_quotient_order']==1
    out={'status':'PASS_ALL_1152_LITERAL_E66_E67_COMMON_WORDS',
         'witness_count':len(wanted),'full_source_degree':fulln,
         'projected_degree':n,'original_N_indices':indices,
         'original_N_words_in_F':[list(source['fword'](source['Nwords'][j])) for j in indices],
         'word_DAG_nodes':len(nodes),'full_source_ancestors_replayed':len(ancestors),
         'all_words_lie_in_actual_N_derived_subgroup':True,
         'parameter_columns':['E17_origin','E62_final_index','E67_target_index',
                              'c2','c3','c4','c6','c12'],
         'all_exact_E62_distribution_and_orbifold_values_replayed':True,
         'input_sha256':{name:sha256((HERE/name).read_bytes()).hexdigest() for name in
                         ['a_cm_distribution_orbifold.json','a_cm_distribution_orbifold.npz',
                          'a_cm_distribution_orbifold_N_derived.bin',
                          'a_cm_distribution_orbifold_projected.bin']},
         'scope':'Actual common-word finite witnesses. No additional arithmetic or full-GT '
                 'condition is assigned to these words.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_distribution_orbifold_witnesses.npz',
                        word_DAG=np.array(nodes,dtype=np.uint32),
                        witness_nodes=np.array(wanted,dtype=np.uint32),
                        witness_parameters=parameters,original_N_indices=indices,
                        full_original_N_values=upper['original'])
    (HERE/'a_cm_distribution_orbifold_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='original_N_words_in_F'},indent=2))


if __name__=='__main__':main()

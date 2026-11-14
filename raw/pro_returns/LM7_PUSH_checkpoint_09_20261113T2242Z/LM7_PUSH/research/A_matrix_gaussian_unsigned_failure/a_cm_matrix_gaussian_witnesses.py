#!/usr/bin/env python3
"""All 55296 actual E71/E69 common word preimages, with exact old maps."""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np

from a_cm_kn23_witnesses import Words
from bc_gaussian_heisenberg_structure import Evaluations

HERE=Path(__file__).resolve().parent


def ancestors_of(nodes,wanted):
    ancestors=set(wanted);todo=list(ancestors)
    while todo:
        op,a,b=nodes[todo.pop()]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if j not in ancestors:ancestors.add(j);todo.append(j)
    return ancestors


def main():
    start=time.monotonic();old=np.load(HERE/'a_cm_kn23_witnesses.npz')
    predecessor=np.load(HERE/'a_cm_kn23_fibres.npz')
    central=np.load(HERE/'a_cm_matrix_gaussian_join.npz')
    centralmeta=json.loads((HERE/'a_cm_matrix_gaussian_join.json').read_text())
    assert centralmeta['full_E71_E69_central_kernel_obtained']
    W=Words();W.nodes=[tuple(map(int,row)) for row in old['word_DAG']]
    W.cache={row:i for i,row in enumerate(W.nodes)}
    assert [W.nodes[i+1] for i in range(97)]==[(1,i,0) for i in range(97)]
    incoming=[tuple(map(int,row)) for row in central['word_DAG']]
    incoming_needed=ancestors_of(incoming,map(int,central['new_central_word_nodes']))
    mapping={};indices=list(map(int,central['original_N_indices']))
    for i in sorted(incoming_needed):
        op,a,b=incoming[i]
        if op==0:node=0
        elif op==1:node=indices[a]+1
        else:node=W.make(op,mapping[a],mapping[b] if op in (2,4,5) else 0)
        mapping[i]=node
    centers=[mapping[int(i)] for i in central['new_central_word_nodes']]
    nodes=list(map(int,old['witness_nodes']));assert len(nodes)==18432
    meta=json.loads((HERE/'a_cm_kn23_model.json').read_text());nwords=meta['source_basis_words_in_F']
    E=Evaluations();original=[E.word(w) for w in nwords]
    needed=ancestors_of(W.nodes,nodes+centers);refs={i:0 for i in needed}
    for i in needed:
        op,a,b=W.nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    checks={}
    for j,node in enumerate(nodes):checks.setdefault(node,[]).append(j)
    values={};saved=np.empty((len(nodes),30),dtype=np.uint8);central_values={};peak=0
    for step,i in enumerate(sorted(needed)):
        op,a,b=W.nodes[i]
        if op==0:v=E.one
        elif op==1:v=original[a]
        elif op==2:v=E.mul(values[a],values[b])
        elif op==3:v=E.inv(values[a])
        elif op==4:v=E.comm(values[a],values[b])
        elif op==5:v=E.conj(values[a],values[b])
        else:raise AssertionError(op)
        values[i]=v
        for j in checks.get(i,[]):saved[j]=E.vector(v)
        if i in centers:central_values[i]=v
        peak=max(peak,len(values))
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j)
        if refs[i]==0:values.pop(i)
        if step and step%50000==0:print('Replayed exact Gaussian ancestor',step,flush=True)
    central_vectors=[]
    for j,node in enumerate(centers):
        v=E.vector(central_values[node]);central_vectors.append(v)
        assert np.array_equal(v,central['exact_Gaussian_central_values'][j])

    # Independently replay the substituted three powered words in the
    # original E71 source, instead of assuming their identity from order.
    full=np.load(HERE/'a_cm_kn23_model.npz')['common_N']
    fullone=np.arange(full.shape[1],dtype=np.uint16)
    def pinv(p):
        q=np.empty_like(p);q[p]=fullone;return q
    cv={};central_needed=ancestors_of(W.nodes,centers)
    for i in sorted(central_needed):
        op,a,b=W.nodes[i]
        if op==0:p=fullone
        elif op==1:p=full[a]
        elif op==2:p=cv[b][cv[a]]
        elif op==3:p=pinv(cv[a])
        elif op==4:p=pinv(cv[b])[pinv(cv[a])[cv[b][cv[a]]]]
        elif op==5:p=pinv(cv[a])[cv[b][cv[a]]]
        else:raise AssertionError(op)
        cv[i]=p
    assert all(np.array_equal(cv[node],fullone) for node in centers)
    del cv
    products={}
    for coeff in product(range(3),repeat=3):
        node=0;value=E.one
        for c,cn in zip(coeff,centers):
            node=W.product(node,W.power(cn,c))
            for _ in range(c):value=E.mul(value,central_values[cn])
        products[coeff]=(node,value)

    export=json.loads((HERE/'bc_orbifold_CM_export.json').read_text())
    targetmeta=json.loads((HERE/'bc_gaussian_heisenberg_model.json').read_text())
    sourcemeta=json.loads((HERE/'bc_gaussian_heisenberg_source.json').read_text())
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    fvalues=[E.word(r['actual_commutator_word_f']) for r in origins]
    final_nodes=[];parameters=[];target_values=[];byold=[]
    for wi,((row,a24,b24),oldnode,wvec) in enumerate(zip(old['witness_parameters'],nodes,saved)):
        oldpar=list(map(int,old['old_parameters'][int(row)]));index,fi,ti=oldpar[:3]
        ext=export['families']['E17_E62_actual'][index]
        oldtarget=ext['complete_four_finite_norm_values'][ti]['absolute_twelve_translation_target']
        current=E.mul(fvalues[index],E.element(wvec));currentvec=E.vector(current)
        assert list(currentvec[:12])+[currentvec[12+3*j+k] for j in range(6) for k in range(2)]==oldtarget
        count=0
        for allowed in sourcemeta['records'][index]['allowed']:
            gi=allowed['Gaussian_framed_target_index'];record=targetmeta['records'][gi]
            gs=tuple(tuple(g) for g in record['six_absolute_values'])
            if [c for g in gs for c in g[:2]]!=oldtarget[12:]:continue
            target=tuple((tuple(oldtarget[2*j:2*j+2]),0) for j in range(6))+gs
            delta=E.vector(E.mul(E.inv(current),target))
            coeff=tuple(delta[k] for k in (14,17,20))
            assert delta==tuple(sum(c*v[k] for c,v in zip(coeff,central_vectors))%3
                                for k in range(30))
            product_node,product_value=products[coeff]
            node=W.product(oldnode,product_node)
            actual_value=E.mul(E.element(wvec),product_value)
            assert E.mul(fvalues[index],actual_value)==target
            final_nodes.append(node);parameters.append([wi,*oldpar,int(a24),int(b24),gi])
            target_values.append(E.vector(target));count+=1
        assert count==3;byold.append(count)
    assert len(final_nodes)==55296
    out={'status':'PASS_ALL_55296_LITERAL_E71_E69_COMMON_WORDS',
         'preceding_E71_values':18432,'Gaussian_lifts_per_value':3,
         'joint_finite_value_count':len(final_nodes),
         'exact_common_image':'P_E71 times_(E67_image) L_E69',
         'new_pure_central_kernel_order':27,
         'new_word_DAG_nodes':len(W.nodes),'exact_Gaussian_ancestors_replayed':len(needed),
         'peak_retained_Gaussian_values':peak,
         'all_three_powered_words_independently_replayed_on_11691_points':True,
         'all_original_E71_values_retained':True,
         'all_55296_actual_Gaussian_targets_replayed':True,
         'whole_domain':'K6 intersect F-prime',
         'parameter_columns':['E71_value_index','E17_origin','E62_final','E67_target',
                              'c2_mod6','c3_mod6','c4_mod6','c6_mod6','c12_mod6',
                              'c2_mod24','c3_mod24','Gaussian_central_framed_target'],
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in
                         ['a_cm_kn23_witnesses.npz','a_cm_kn23_fibres.npz',
                          'a_cm_kn23_model.json','a_cm_kn23_model.npz',
                          'a_cm_matrix_gaussian_join.json','a_cm_matrix_gaussian_join.npz',
                          'bc_orbifold_CM_export.json','bc_gaussian_heisenberg_model.json',
                          'bc_gaussian_heisenberg_source.json','de_ferrari_fibres.json']},
         'scope':'Exact common-source finite word fibres. The additional full Gaussian pro-three Frattini characters of E70 are not assigned by this calculation.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_matrix_gaussian_witnesses.npz',
                        word_DAG=np.array(W.nodes,dtype=np.uint32),
                        witness_nodes=np.array(final_nodes,dtype=np.uint32),
                        witness_parameters=np.array(parameters,dtype=np.int64),
                        full_source_identity_central_nodes=np.array(centers,dtype=np.uint32),
                        Gaussian_targets=np.array(target_values,dtype=np.uint8),
                        preceding_E71_Gaussian_values=saved)
    (HERE/'a_cm_matrix_gaussian_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()

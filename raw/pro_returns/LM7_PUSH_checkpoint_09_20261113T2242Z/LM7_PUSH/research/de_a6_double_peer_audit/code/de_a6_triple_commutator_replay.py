#!/usr/bin/env python3
"""Independent replay of the exact C-preimage normal-form queries."""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_ferrari_mod9_lift import rref,solve

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_a6_triple_commutator_queries.json','de_a6_triple_commutator_prepare.npz',
           'de_a6_triple_commutator_prepare.json','de_a6_triple_kernel_replay.npz',
           'de_a6_triple_central_replay.npz','de_a6_gl_central_prepare.npz',
           'de_a6_triple_query_core.hpp','de_a6_triple_central.cpp']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    source=(HERE/names[-1]).read_text()
    body=source[source.index('constexpr unsigned NG='):source.index('int main(int argc')]
    assert (HERE/names[-2]).read_text().endswith(body)
    raw=json.loads((HERE/names[0]).read_text());prep=np.load(HERE/names[1])
    labels=json.loads((HERE/names[2]).read_text())['query_labels']
    assert raw['status']=='PASS_EXACT_C_PREIMAGE_NORMAL_FORM_QUERIES'
    assert raw['query_count']==len(labels)==len(raw['records'])==60
    kernel=np.load(HERE/names[3]);central=np.load(HERE/names[4]);old=np.load(HERE/names[5])
    H=FerrariA6Triple();d=load_data();W=InducedCombined(H,d)
    f=[W.word(d['xword']),W.word(d['yword'])]
    queries,qcount=selected_group(prep['literal_F_word_DAG'],prep['query_word_nodes'],W,f)
    qp=evaluate(prep['literal_F_word_DAG'],old['original_F_source_permutations'],prep['query_word_nodes'])
    targets=sorted(set(j for rec in raw['records'] for j in rec['normal_form_nodes']))
    c=[(W.id,v) for v in kernel['C_source_values']]
    values,ccount=selected_group(raw['normal_form_word_DAG'],targets,W,c)
    cp=evaluate(raw['normal_form_word_DAG'],old['C_original_source_permutations'],targets)
    # Ordinary exponent sums in the ten actual C generators.
    ex=[]
    for op,a,b in raw['normal_form_word_DAG']:
        if op==0:v=np.zeros(10,dtype=np.int64)
        elif op==1:v=np.eye(10,dtype=np.int64)[a]
        elif op==2:v=(ex[a]+ex[b])%3
        elif op==3:v=-ex[a]%3
        elif op==4:v=np.zeros(10,dtype=np.int64)
        elif op==5:v=ex[b]
        else:raise AssertionError(op)
        ex.append(v)
    B=kernel['kernel_basis'];piv=np.array(rref(B.T)[1])
    inverse=np.column_stack([solve(B[piv],np.eye(79,dtype=np.int64)[:,i])[0] for i in range(79)])
    L=central['kernel_to_preimage_abelianization'];hom=central['C_lift_abelianization_values']
    coords=[]
    for i,(qn,rec) in enumerate(zip(prep['query_word_nodes'],raw['records'])):
        qn=int(qn);v=queries[qn];p=qp[qn];e=np.zeros(10,dtype=np.int64)
        assert np.array_equal(v[0],W.id)
        assert np.array_equal(v[1],prep['query_source_values'][i])
        assert np.array_equal(p,prep['query_A6_permutations'][i])
        for j in rec['normal_form_nodes']:
            v=W.mul(v,W.inv(values[j]));p=np.argsort(cp[j])[p];e=(e+ex[j])%3
        assert np.array_equal(p,np.arange(9462)) and np.array_equal(v[0],W.id)
        actual=H.relative_kernel_vector(v[1]).ravel();expected=np.zeros(5724,dtype=np.int64)
        for at,x in rec['kernel_residue']:
            assert not expected[at] and x in (1,2);expected[at]=x
        assert np.array_equal(actual,expected)
        k=inverse@actual[piv]%3;assert np.array_equal(B@k%3,actual)
        assert np.array_equal(e,rec['C_generator_exponents'])
        value=(L@k+hom@e)%3;assert np.array_equal(value,rec['coordinate'])
        coords.append(value)
    coords=np.array(coords,dtype=np.int64).T
    pair=np.zeros((3,9,9),dtype=np.int64)
    for value,label in zip(coords.T,labels):
        if label[0]=='module_commutator':
            _,i,j=label;pair[:,i,j]=value;pair[:,j,i]=-value%3
    V=prep['stable_module_coordinates']
    for value,label in zip(coords.T,labels):
        if label[0]=='stable_commutator':
            _,i,j=label
            expected=np.array([V[:,i]@a@V[:,j] for a in pair])%3
            assert np.array_equal(value,expected)
    matrices={kind:np.array([v for v,l in zip(coords.T,labels) if l[0]==kind]).T
              for kind in ['module_cube','module_commutator','stable_commutator']}
    out={'status':'PASS_INDEPENDENT_LITERAL_C_PREIMAGE_QUERY_REPLAY',
         'query_count':60,'query_literal_F_ancestors_replayed':qcount,
         'C_normal_form_ancestors_replayed':ccount,
         'all_normal_form_nodes_replayed_in_both_maps':True,
         'all_actual_kernel_residues_and_abelian_coordinates_replayed':True,
         'stable_pairing_matches_full_module_alternating_pairing':True,
         'image_ranks':{k:len(rref(v)[1]) for k,v in matrices.items()},
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_triple_commutator_replay.npz',
                        query_coordinates=coords,alternating_pairing=pair,**matrices)
    (HERE/'de_a6_triple_commutator_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

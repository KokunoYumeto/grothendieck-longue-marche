#!/usr/bin/env python3
"""Actual common N_B-prime word DAG witnesses for every E6/E62 fibre."""
from pathlib import Path
import json,time
import numpy as np
from a_cm_distribution_e62 import Distribution
from a_cm_gl23_pc import ClassTwoCoordinates
from de_a6_schreier_certificate import read_certificate,verify_words
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent


def main():
    start=time.monotonic();P=ClassTwoCoordinates('joint');D=Distribution()
    upper=read_certificate(HERE/'a_cm_distribution_e62_N_derived.bin')
    projected=read_certificate(HERE/'a_cm_distribution_e62_projected.bin')
    verify_words(upper);verify_words(projected)
    assert upper['derived'] and not projected['derived']
    retained=np.load(HERE/'a_cm_distribution_e62.npz')
    points=retained['retained_projection_points'];fulln=upper['degree'];n=len(points)
    invpoints=np.full(fulln,-1,dtype=np.int64);invpoints[points]=np.arange(n)
    assert np.array_equal(invpoints[upper['strong'][:,points]],projected['original'])
    nodes=[tuple(map(int,row)) for row in upper['nodes']]
    def product(a,b):
        if not a:return b
        if not b:return a
        nodes.append((2,a,b));return len(nodes)-1
    mapping=[]
    for op,a,b in projected['nodes']:
        op,a,b=map(int,(op,a,b))
        if op==0:v=0
        elif op==1:v=int(upper['words'][a])
        else:
            nodes.append((op,mapping[a],mapping[b] if op in (2,4,5) else 0));v=len(nodes)-1
        mapping.append(v)
    strongnodes=[mapping[int(i)] for i in projected['words']]
    one=np.arange(n,dtype=np.uint16);levels=[]
    for lev,base in enumerate(projected['base']):
        gens=[(g,node) for g,node,depth in zip(projected['strong'],strongnodes,projected['depths']) if depth>=lev]
        orbit=[int(base)];trans=[one];words=[0];at={int(base):0}
        for k,v in enumerate(orbit):
            for g,gnode in gens:
                w=int(g[v])
                if w not in at:
                    at[w]=len(orbit);orbit.append(w)
                    trans.append(g[trans[k]]);words.append(product(words[k],gnode))
        levels.append((int(base),{v:(np.argsort(t).astype(np.uint16),w)
                                  for v,t,w in zip(orbit,trans,words)}))
    def preimage(p):
        h=p;ans=0
        for base,trans in levels:
            v=int(h[base])
            if v==base:continue
            ti,w=trans[v];h=ti[h];ans=product(w,ans)
        assert np.array_equal(h,one)
        return ans
    results=json.loads((HERE/'a_cm_distribution_e62.json').read_text())
    originals=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    records=[];expected=[];wanted=[]
    for row,base in zip(results['records'],originals):
        f=base['actual_commutator_word_f'];qf=D.ordinary(f)
        original=[D.word(f,k)[1][0] for k in D.sources]
        for final in row['actual_single_source_correction_fibres']:
            c=final['E62_actual_PC_coordinate']
            for coeff in final['admissible_distribution_coefficient_tuples']:
                target=[]
                for a,k in zip(original,coeff):
                    hc=D.hm[D.apower((D.y[0],0),k)[0]][qf]
                    target.append(D.am(D.ai(a),(hc,k)))
                p=np.r_[P.element(c),P.n+D.projected(target)]
                node=preimage(p);wanted.append(node);expected.append(p)
                records.append({'point':row['index'],'E62_coordinate':c,'coefficients':coeff,'actual_N_small_word_node':node})
    # Independently replay all ancestors using the original 13 actual N
    # permutations, with the full 459-point distribution core retained.
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
    for node,p in zip(wanted,expected):assert np.array_equal(invpoints[values[node][points]],p)
    original_indices=results['common_N_source']['selected_original_indices']
    data=load_data()
    out={'status':'PASS_ALL_LITERAL_COMMON_CORRECTION_WORDS',
         'witness_count':len(records),'original_N_indices':original_indices,
         'original_N_words_in_F':[list(data['fword'](data['Nwords'][j])) for j in original_indices],
         'all_words_are_combinations_of_actual_N_derived_generators':True,
         'full_induced_source_ancestors_replayed':len(ancestors),
         'actual_word_DAG_nodes':len(nodes),'records':records,
         'scope':'All 288 witnesses preserve the exact E62 correction and attain the entire five-equation E6 tuple simultaneously.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_distribution_witnesses.npz',word_DAG=np.array(nodes,dtype=np.uint32),
                        witness_nodes=wanted,expected_projected_values=np.array(expected),
                        original_N_indices=original_indices,full_original_N_values=upper['original'])
    (HERE/'a_cm_distribution_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {'records','original_N_words_in_F'}},indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Actual C_A6 generators lifted to the three specified SL2(F5) factors.

All nested mixture records are expanded into one literal F-word DAG.
The ten final original permutations are independently replayed before
exporting the tiny central-extension coefficient model.
"""
from pathlib import Path
from hashlib import sha256
import json,struct,time
import numpy as np
from de_a6_schreier_certificate import read_certificate
from de_a6_gl_common_quotient import evaluate_selected
from de_ferrari_sl2_5_model import FerrariSL2Five

HERE=Path(__file__).resolve().parent


def main():
    started=time.time()
    names=['de_a6_schreier_Fprime.bin','de_a6_schreier_Fprimecompact_input.json',
           'de_a6_module.json','de_a6_schreier_Fprimeprime.bin',
           'de_a6_schreier_residual_input.json','de_a6_schreier_residual.bin',
           'de_a6_schreier_residual_derived_input.json','de_a6_schreier_residual_derived.bin',
           'de_ferrari_a6_residual_certificate.json','de_a6_gl_common_quotient.json',
           'de_ferrari_sl2_5_model.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    E=read_certificate(HERE/names[0]);E1=read_certificate(HERE/names[3])
    C=read_certificate(HERE/names[5]);C2=read_certificate(HERE/names[7])
    assert all(d['derived'] for d in (E,E1,C,C2))
    assert len(E['original'])==2 and len(E1['original'])==9
    assert len(C['original'])==len(C2['original'])==10
    nodes=[[0,0,0],[1,0,0],[1,1,0]]
    def append(op,a,b=0):
        if op==2 and not a:return b
        if op==2 and not b:return a
        if op==3 and not a:return 0
        nodes.append([op,int(a),int(b)]);return len(nodes)-1
    def substitute(local,original):
        mapping=[]
        for op,a,b in local:
            op,a,b=map(int,(op,a,b))
            if op==0:w=0
            elif op==1:w=original[a]
            elif op==3:w=append(op,mapping[a])
            else:w=append(op,mapping[a],mapping[b])
            mapping.append(w)
        return mapping
    emap=substitute(E['nodes'],[1,2])
    compact=json.loads((HERE/names[1]).read_text())
    chosen=json.loads((HERE/names[2]).read_text())['selected_original_indices']
    indices=[compact['source_indices'][j] for j in chosen]
    assert np.array_equal(E['strong'][indices],E1['original'])
    e1original=[emap[int(E['words'][j])] for j in indices]
    e1map=substitute(E1['nodes'],e1original)
    def mixtures(cert,mapping,name,target):
        raw=json.loads((HERE/name).read_text())
        words=raw['one_based_signed_strong_generator_words']
        assert len(words)==len(target['original'])
        answer=[]
        for w in words:
            node=0
            for j in w:
                v=mapping[int(cert['words'][abs(j)-1])]
                if j<0:v=append(3,v)
                node=append(2,node,v)
            answer.append(node)
        return answer
    coriginal=mixtures(E1,e1map,names[4],C)
    cmap=substitute(C['nodes'],coriginal)
    originals=mixtures(C,cmap,names[6],C2)
    # This is a fresh evaluation of the ten complete nested F words in
    # the full 9462-point A6 source, independent of the small SL2 tables.
    values,count=evaluate_selected(nodes,set(originals),E['original'])
    assert all(np.array_equal(values[node],C2['original'][i]) for i,node in enumerate(originals))
    H=FerrariSL2Five();shared=[4,12,18]
    fvalues=[H.lifts[shared,0],H.lifts[shared,1]]
    sv=[];av=[];fab=[]
    for op,a,b in nodes:
        if op==0:v=np.full(3,H.sid,dtype=np.int64);z=np.zeros(3,dtype=np.int64);ab=(0,0)
        elif op==1:
            v=fvalues[a].copy();z=H.old.generating_pairs
            z=np.array(z,dtype=np.int64)[shared,a];ab=(int(a==0),int(a==1))
        elif op==2:v=H.sm[sv[a],sv[b]];z=H.old.sm[av[a],av[b]];ab=tuple(x+y for x,y in zip(fab[a],fab[b]))
        elif op==3:v=H.si[sv[a]];z=H.old.si[av[a]];ab=tuple(-x for x in fab[a])
        elif op==4:
            v=H.sm[H.sm[H.sm[sv[a],sv[b]],H.si[sv[a]]],H.si[sv[b]]]
            z=H.old.sm[H.old.sm[H.old.sm[av[a],av[b]],H.old.si[av[a]]],H.old.si[av[b]]];ab=(0,0)
        elif op==5:
            v=H.sm[H.sm[sv[a],sv[b]],H.si[sv[a]]]
            z=H.old.sm[H.old.sm[av[a],av[b]],H.old.si[av[a]]];ab=fab[b]
        else:raise AssertionError(op)
        assert np.array_equal(H.qsl[v],z)
        sv.append(v);av.append(z);fab.append(ab)
    lifted=np.array([sv[j] for j in originals]);projected=np.array([av[j] for j in originals])
    assert all(fab[j]==(0,0) for j in originals)
    # The final ten originals generate the certified perfect C: their
    # derived image has the same proved order as C, and all are in C.
    residual=json.loads((HERE/names[8]).read_text())
    assert residual['C_is_perfect_by_derived_word_inclusion_and_equal_order']
    with (HERE/'de_a6_gl_central_model.bin').open('wb') as f:
        f.write(struct.pack('<6I',0xA6C6CE13,1,int(H.sid),int(H.z),10,C2['degree']))
        f.write(np.asarray(H.sm,dtype=np.uint8).tobytes());f.write(np.asarray(H.si,dtype=np.uint8).tobytes())
        f.write(np.asarray(lifted,dtype=np.uint8).tobytes());f.write(np.asarray(C2['original'],dtype='<u2').tobytes())
    np.savez_compressed(HERE/'de_a6_gl_central_prepare.npz',literal_F_word_DAG=np.array(nodes,dtype=np.int64),
        C_original_word_nodes=np.array(originals),C_original_SL2_values=lifted,
        C_original_A5_values=projected,source_F_SL2_values=np.array(fvalues),
        original_F_source_permutations=E['original'],C_original_source_permutations=C2['original'])
    out={'status':'PASS_LITERAL_CENTRAL_PULLBACK_INPUT',
         'specified_A5_epikernels':shared,'C_generator_count':10,
         'actual_C_generator_SL2_values':lifted.tolist(),'actual_C_generator_A5_values':projected.tolist(),
         'literal_F_word_DAG_nodes':len(nodes),'actual_F_ancestors_replayed_in_full_A6_source':count,
         'all_nested_source_words_match_final_originals':True,
         'all_C_generator_ordinary_F_abelianizations_zero':True,
         'all_projective_values_match_specified_A5_epikernels':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_gl_central_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()

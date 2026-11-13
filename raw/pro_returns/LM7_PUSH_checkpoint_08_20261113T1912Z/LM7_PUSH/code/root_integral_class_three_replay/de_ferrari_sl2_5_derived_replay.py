#!/usr/bin/env python3
"""Replay the complete derived-image certificates without generator search.

The supplied directory contains immutable expected certificates.  Every
chosen generator is rebuilt from its nested literal B-word description,
then compared with both the saved actual component image and the saved
faithful base permutation.  The full lifted presentation, all original
commutators, all module commutators, all conjugation residuals, and the
entire normal closure are recomputed.  Only discovery of a small base
generating set is skipped.

Run in an isolated copied code directory, for example:
  python de_ferrari_sl2_5_derived_replay.py --expected-dir ORIGINAL_CODE
The output directory defaults to this script's directory.  Its model,
source, and N inputs come from that directory, so independently rerun
upstream certificates are used.  Expected and output directories must
be distinct.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_sl2_5_source import Source
from de_lifted_schreier_extra import lifted_kernel
from de_ferrari_two_core import Span2

here=Path(__file__).resolve().parent

def expression_evaluator(W):
    cache={}
    def evaluate(description):
        key=json.dumps(description,sort_keys=True,separators=(',',':'))
        if key in cache:return cache[key]
        if set(description)=={'literal_B_word'}:
            word=description['literal_B_word']
            assert all(t in (-1,0,1) for t in word)
            result=W.word(word),len(word)
        elif set(description)=={'commutator'}:
            a,na=evaluate(description['commutator'][0])
            b,nb=evaluate(description['commutator'][1])
            result=W.comm(a,b),2*(na+nb)
        elif set(description)=={'conjugate'}:
            a,na=evaluate(description['conjugate'][0])
            b,nb=evaluate(description['conjugate'][1])
            result=W.conj(a,b),2*na+nb
        else:raise AssertionError(('unsupported chosen word description',description))
        cache[key]=result
        return result
    return evaluate

def replay_stage(model,main,perms,kernel,expected_base_order,stem,
                 descriptions,kernel_description,expected_dir,output_dir):
    W=model.W
    expected=json.loads((expected_dir/(stem+'.json')).read_text())
    cert=np.load(expected_dir/(stem+'.npz'))
    chosen_descriptions=expected['chosen_base_derived_generator_descriptions']
    evaluate=expression_evaluator(W)
    actual=[];selected=[];lengths=[]
    assert len(chosen_descriptions)==len(cert['chosen_component_images'])
    for i,description in enumerate(chosen_descriptions):
        g,length=evaluate(description)
        assert np.array_equal(g[0],W.id)
        assert np.array_equal(g[1],cert['chosen_component_images'][i])
        p=model.permutation(g)
        assert np.array_equal(np.array(p.array_form),cert['chosen_base_permutations'][i])
        actual.append(g);selected.append(p);lengths.append(length)
    print(stem,'reconstructed actual nested source words',len(actual),
          'unreduced lengths',min(lengths),max(lengths),flush=True)
    identity=Permutation(list(range(perms[0].size)));extra=[]
    for i,a in enumerate(main):
        for j,b in enumerate(main[:i]):
            p=perms[i]*perms[j]*(perms[i]**-1)*(perms[j]**-1)
            extra.append((p,W.comm(a,b),{'commutator':[descriptions[i],descriptions[j]]}))
    for i,n in enumerate(main):
        for p,g,description in zip(selected,actual,chosen_descriptions):
            extra.append((perms[i]*p*(perms[i]**-1),W.conj(n,g),
                          {'conjugate':[descriptions[i],description]}))
    for j,v in enumerate(kernel.T):
        k=model.element(v);kd={'kernel_basis':j,**kernel_description}
        for i,n in enumerate(main):
            extra.append((identity,W.comm(k,n),{'commutator':[kd,descriptions[i]]}))
    # known_order is checked against a freshly computed full BSGS, not
    # against the saved generating-set size or a saved order alone.
    G,S,info=lifted_kernel(W,actual,selected,model.vector,model.element,36*57,
        known_order=expected_base_order,extra_lifts=[(p,g) for p,g,de in extra],normalizers=main)
    saved=Span2(36*57)
    for i,v in enumerate(cert['kernel_basis'].T):saved.add(v,i)
    assert len(S.basis)==len(saved.basis)==expected['complete_kernel_dimension']
    for v in S.basis:saved.coordinates(v)
    for v in saved.basis:S.coordinates(v)
    assert info['lifted_group_order']==expected['lifted_group_order']
    assert info['Schreier_relation_count']==expected['Schreier_relation_count']
    assert info['extra_lift_relations']==expected['extra_lift_relations']
    out={**info,'construction':'complete derived replay from reconstructed literal source expressions',
         'chosen_base_derived_generator_descriptions':chosen_descriptions,
         'chosen_unreduced_literal_B_word_lengths':lengths,
         'all_input_word_descriptions':chosen_descriptions+[de for p,g,de in extra]+descriptions,
         'all_kernel_commutators_retained':kernel.shape[1]*len(main),
         'all_base_generator_conjugations_retained':len(actual)*len(main),
         'discovery_only_skipped':True,
         'all_chosen_component_and_permutation_arrays_verified':True,
         'complete_kernel_equals_supplied_certificate_in_both_directions':True}
    (output_dir/(stem+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(output_dir/(stem+'.npz'),kernel_basis=S.matrix(),
        chosen_component_images=np.array([g[1] for g in actual]),
        chosen_base_permutations=np.array([p.array_form for p in selected]),
        base_strong_generators=np.array([p.array_form for p in G.strong_gens]))
    print(stem,'COMPLETE',json.dumps({k:v for k,v in out.items() if k not in
        ('literal_word_DAG','kernel_basis_word_nodes','all_input_word_descriptions',
         'chosen_base_derived_generator_descriptions')}),flush=True)
    return actual,selected,S,out

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--expected-dir',type=Path,required=True)
    parser.add_argument('--output-dir',type=Path,default=here)
    args=parser.parse_args();expected_dir=args.expected_dir.resolve();output_dir=args.output_dir.resolve()
    assert expected_dir!=output_dir,'Expected certificates must remain in a separate immutable directory.'
    assert expected_dir.is_dir();output_dir.mkdir(parents=True,exist_ok=True)
    start=time.time();model=Source();W,d=model.W,model.d
    old=json.loads((here/'de_ferrari_a5_corrections.json').read_text())
    ndata=json.loads((here/'de_ferrari_sl2_5_N.json').read_text())
    ncert=np.load(here/'de_ferrari_sl2_5_N.npz')
    N=[(W.id,x) for x in ncert['N_component_images']]
    oldperms=np.load(here/'de_ferrari_a5_corrections.npz')['N_images']
    indices=ndata['selected_original_N_indices']
    normal=[N[i] for i in indices]
    descriptions=[{'literal_B_word':d['Nwords'][i]} for i in indices]
    for g,description in zip(normal,descriptions):
        rebuilt=W.word(description['literal_B_word'])
        assert np.array_equal(rebuilt[0],g[0]) and np.array_equal(rebuilt[1],g[1])
    perms=[Permutation(oldperms[i].tolist()+list(range(1980,2124))) for i in indices]
    for g,p in zip(normal,perms):assert model.permutation(g)==p
    VN=ncert['N_kernel_basis']
    cmain,cperms,C,cinfo=replay_stage(model,normal,perms,VN,old['N_derived_image_order'],
        'de_ferrari_sl2_5_Nprime',descriptions,{'source_certificate':'de_ferrari_sl2_5_N.json'},
        expected_dir,output_dir)
    _,_,CC,ccinfo=replay_stage(model,cmain,cperms,C.matrix(),old['N_derived_image_order'],
        'de_ferrari_sl2_5_Nprimeprime',cinfo['chosen_base_derived_generator_descriptions'],
        {'source_certificate':'de_ferrari_sl2_5_Nprime.json'},expected_dir,output_dir)
    assert len(CC.basis)==len(C.basis)
    for v in C.basis:CC.coordinates(v)
    full=np.load(here/'de_ferrari_sl2_5_source.npz')['full_kernel_basis']
    fm=[W.word(d['xword']),W.word(d['yword'])];fp=[model.permutation(g) for g in fm]
    oldcompare=json.loads((here/'de_ferrari_a5_compare.json').read_text())
    _,_,E,einfo=replay_stage(model,fm,fp,full,oldcompare['F_derived_image_order'],
        'de_ferrari_sl2_5_Fprime',[{'literal_B_word':d['xword']},{'literal_B_word':d['yword']}],
        {'source_certificate':'de_ferrari_sl2_5_source.json'},expected_dir,output_dir)
    for v in C.basis:E.coordinates(v)
    source=json.loads((here/'de_ferrari_sl2_5_source.json').read_text())
    orderC=cinfo['lifted_group_order']
    out={'N_kernel_dimension':VN.shape[1],'Nprime_kernel_dimension':len(C.basis),
         'Nprimeprime_kernel_dimension':len(CC.basis),'Fprime_kernel_dimension':len(E.basis),
         'Nprime_is_perfect':True,
         'N_abelianization_order':ndata['lifted_group_order']//orderC,
         'Fprime_mod_Nprime_order':einfo['lifted_group_order']//orderC,
         'source_mod_N_order':source['lifted_group_order']//ndata['lifted_group_order'],
         'source_mod_Nprime_order':source['lifted_group_order']//orderC,
         'all_stages_reconstructed_and_completely_replayed':True,
         'seconds':round(time.time()-start,3)}
    (output_dir/'de_ferrari_sl2_5_derived_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

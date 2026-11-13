#!/usr/bin/env python3
"""Exact derived images, retaining every elementary-kernel commutator.

For G=<g_i,V>, with V an elementary abelian normal subgroup, Gprime
is the normal closure of [g_i,g_j] and [V,g_i].  We retain all such
kernel commutators, every conjugation correction of the chosen base
derived generators, and the complete lifted base presentation.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_sl2_5_source import Source
from de_lifted_schreier_extra import lifted_kernel
from de_ferrari_two_core import Span2

here=Path(__file__).resolve().parent

def derived_stage(model,main,perms,kernel,expected_base_order,stem,descriptions,kernel_description):
    W=model.W;identity=Permutation(list(range(perms[0].size)));selected=[];actual=[];desc=[]
    base=PermutationGroup([identity]);baseorder=1
    seeds=[]
    for i,a in enumerate(main):
        for j,b in enumerate(main[:i]):
            p=perms[i]*perms[j]*(perms[i]**-1)*(perms[j]**-1)
            g=W.comm(a,b);description={'commutator':[descriptions[i],descriptions[j]]}
            seeds.append((p,g,description))
    def add(p,g,description):
        nonlocal base,baseorder
        if not base.contains(p):
            selected.append(p);actual.append(g);desc.append(description);base=PermutationGroup(selected)
            baseorder=int(base.order())
            print(stem,'base derived generators',len(selected),'order',baseorder,flush=True)
    for p,g,de in seeds:
        if baseorder==expected_base_order:break
        add(p,g,de)
    at=0
    while baseorder!=expected_base_order and at<len(selected):
        for i,n in enumerate(main):
            p=perms[i]*selected[at]*(perms[i]**-1)
            g=W.conj(n,actual[at]);de={'conjugate':[descriptions[i],desc[at]]}
            add(p,g,de)
            if baseorder==expected_base_order:break
        at+=1
    assert baseorder==expected_base_order
    extra=list(seeds)
    # These residuals make the lifted base-derived subgroup normal under
    # all original generators, including every lift above the same base.
    for i,n in enumerate(main):
        for p,g,de in zip(selected,actual,desc):
            extra.append((perms[i]*p*(perms[i]**-1),W.conj(n,g),{'conjugate':[descriptions[i],de]}))
    for j,v in enumerate(kernel.T):
        k=model.element(v);kd={'kernel_basis':j,**kernel_description}
        for i,n in enumerate(main):
            extra.append((identity,W.comm(k,n),{'commutator':[kd,descriptions[i]]}))
    G,S,info=lifted_kernel(W,actual,selected,model.vector,model.element,36*57,
        known_order=expected_base_order,extra_lifts=[(p,g) for p,g,de in extra],normalizers=main)
    out={**info,'construction':'complete normal derived subgroup with all original module commutators',
         'chosen_base_derived_generator_descriptions':desc,
         'all_input_word_descriptions':desc+[de for p,g,de in extra]+descriptions,
         'all_kernel_commutators_retained':kernel.shape[1]*len(main),
         'all_base_generator_conjugations_retained':len(actual)*len(main)}
    here.joinpath(stem+'.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/(stem+'.npz'),kernel_basis=S.matrix(),
                        chosen_component_images=np.array([g[1] for g in actual]),
                        chosen_base_permutations=np.array([p.array_form for p in selected]),
                        base_strong_generators=np.array([p.array_form for p in G.strong_gens]))
    print(stem,'COMPLETE',json.dumps({k:v for k,v in info.items() if k not in ('literal_word_DAG','kernel_basis_word_nodes')}),flush=True)
    return actual,selected,S,out

def main():
    start=time.time();model=Source();H,W,d=model.H,model.W,model.d
    old=json.loads((here/'de_ferrari_a5_corrections.json').read_text())
    ndata=json.loads((here/'de_ferrari_sl2_5_N.json').read_text())
    ncert=np.load(here/'de_ferrari_sl2_5_N.npz');N=[(W.id,x) for x in ncert['N_component_images']]
    oldperms=np.load(here/'de_ferrari_a5_corrections.npz')['N_images']
    indices=ndata['selected_original_N_indices']
    normal=[N[i] for i in indices]
    perms=[Permutation(oldperms[i].tolist()+list(range(1980,2124))) for i in indices]
    VN=ncert['N_kernel_basis']
    descriptions=[{'literal_B_word':d['Nwords'][i]} for i in indices]
    cmain,cperms,C,cinfo=derived_stage(model,normal,perms,VN,old['N_derived_image_order'],
        'de_ferrari_sl2_5_Nprime',descriptions,{'source_certificate':'de_ferrari_sl2_5_N.json'})
    _,_,CC,ccinfo=derived_stage(model,cmain,cperms,C.matrix(),old['N_derived_image_order'],
        'de_ferrari_sl2_5_Nprimeprime',cinfo['chosen_base_derived_generator_descriptions'],
        {'source_certificate':'de_ferrari_sl2_5_Nprime.json'})
    assert len(CC.basis)==len(C.basis)
    for v in C.basis:CC.coordinates(v)
    full=np.load(here/'de_ferrari_sl2_5_source.npz')['full_kernel_basis']
    fm=[W.word(d['xword']),W.word(d['yword'])];fp=[model.permutation(g) for g in fm]
    oldcompare=json.loads((here/'de_ferrari_a5_compare.json').read_text())
    _,_,E,einfo=derived_stage(model,fm,fp,full,oldcompare['F_derived_image_order'],
        'de_ferrari_sl2_5_Fprime',[{'literal_B_word':d['xword']},{'literal_B_word':d['yword']}],
        {'source_certificate':'de_ferrari_sl2_5_source.json'})
    for v in C.basis:E.coordinates(v)
    orderN=ndata['lifted_group_order'];orderC=cinfo['lifted_group_order'];orderE=einfo['lifted_group_order']
    source=json.loads((here/'de_ferrari_sl2_5_source.json').read_text())
    out={'N_kernel_dimension':VN.shape[1],'Nprime_kernel_dimension':len(C.basis),
         'Nprimeprime_kernel_dimension':len(CC.basis),'Fprime_kernel_dimension':len(E.basis),
         'Nprime_is_perfect':True,'N_abelianization_order':orderN//orderC,
         'Fprime_mod_Nprime_order':orderE//orderC,
         'source_mod_N_order':source['lifted_group_order']//orderN,
         'source_mod_Nprime_order':source['lifted_group_order']//orderC,
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_derived.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

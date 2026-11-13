#!/usr/bin/env python3
"""Extract an actual six-word basis of the certified order64 quotient."""
from pathlib import Path
import json
import numpy as np
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent

def main():
    q=json.loads((HERE/'de_a6_residual_quotient.json').read_text())
    assert q['status']=='PASS' and q['quotient_order']==64
    gens=np.array(q['generators'],dtype=np.uint8);one=np.arange(64,dtype=np.uint8)
    assert all(np.array_equal(g[g],one) for g in gens)
    assert all(np.array_equal(g[h],h[g]) for i,g in enumerate(gens) for h in gens[:i])
    group={bytes(one):0};images=[one];selected=[]
    for i,g in enumerate(gens):
        if bytes(g) in group:continue
        old=list(images);selected.append(i)
        for h in old:
            p=g[h];assert bytes(p) not in group
            group[bytes(p)]=len(images);images.append(p)
    assert len(images)==64 and len(selected)==6
    # Every original generator is represented in this exact regular action.
    coords=[group[bytes(g)] for g in gens]
    d=read_certificate(HERE/'de_a6_schreier_Fprimeprime.bin');verify_words(d)
    prep=json.loads((HERE/'de_a6_schreier_Fprimeprime_all_input.json').read_text())
    source=np.load(HERE/'de_a6_schreier_Fprimeprime_all_input.npz')['generators']
    assert np.array_equal(source,d['strong'][prep['source_indices']])
    basis=source[selected]
    with (HERE/'de_a6_binary_module_basis.input').open('w') as out:
        out.write(f'{d["degree"]} 6\n')
        for p in basis:out.write(' '.join(map(str,p))+'\n')
    raw=json.loads((HERE/'de_a6_module.json').read_text())
    with (HERE/'de_a6_binary_module_V.input').open('w') as out:
        out.write(' '.join(map(str,np.array(raw['conjugation_matrices']).ravel()))+'\n')
        out.write(' '.join(map(str,raw['commutator_x_y']))+'\n')
    data={'status':'PASS','quotient':'E1/C=(F2)^6',
          'all315_quotient_generators_have_square_one':True,
          'all_quotient_generator_pairs_commute':True,
          'selected_sorted_strong_indices':selected,
          'selected_source_strong_indices':[prep['source_indices'][j] for j in selected],
          'selected_source_word_nodes':[int(d['words'][prep['source_indices'][j]]) for j in selected],
          'all_sorted_strong_generator_binary_coordinates':coords,
          'complete_quotient_order':len(images)}
    (HERE/'de_a6_binary_module_basis.json').write_text(json.dumps(data,indent=2)+'\n')
    np.savez_compressed(HERE/'de_a6_binary_module_basis.npz',basis=basis,regular_basis=gens[selected])
    print(json.dumps({k:v for k,v in data.items() if k!='all_sorted_strong_generator_binary_coordinates'},indent=2))

if __name__=='__main__':main()

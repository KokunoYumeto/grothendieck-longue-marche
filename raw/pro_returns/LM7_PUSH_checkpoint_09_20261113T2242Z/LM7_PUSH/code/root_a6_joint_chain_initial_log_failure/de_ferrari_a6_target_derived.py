#!/usr/bin/env python3
"""Connect the full Nielsen derived certificates to the actual target.

The free kernel A6^53 is perfect.  The verified derived and second
derived Nielsen images coincide; their index is two.  Their inverse
image in the Ferrari semidirect product is therefore the perfect
derived group of the full target, with the specified braid-sign map.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy import factorint
from de_ferrari_a6_model import FerrariA6
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent
def last(name):return json.loads((HERE/name).read_text().splitlines()[-1])

def main():
    start=time.time();H=FerrariA6()
    original=np.array([H.permutation(g,True).array_form for g in (H.a,H.b)])
    first=read_certificate(HERE/'de_a6_schreier_Nielsenprime.bin')
    assert first['derived'] and np.array_equal(first['original'],original);verify_words(first)
    prep=json.loads((HERE/'de_a6_schreier_Nielsencompact_input.json').read_text())
    compact=read_certificate(HERE/'de_a6_schreier_Nielsencompact.bin')
    assert np.array_equal(compact['original'],first['strong'][prep['source_indices']]);verify_words(compact)
    compact_log=last('de_a6_schreier_Nielsencompact.out')
    second=read_certificate(HERE/'de_a6_schreier_Nielsenprimeprime.bin')
    assert second['derived']
    assert np.array_equal(second['original'],compact['original'][compact_log['selected_original_indices']])
    verify_words(second)
    orders=[]
    for stem in ('Nielsenprime','Nielsencompact','Nielsenprimeprime'):
        discovery=last('de_a6_schreier_'+stem+'.out')
        replay=last('de_a6_schreier_'+stem+'_replay.out')
        for key in ('order','base','orbit_lengths','complete_final_Schreier_relations'):
            assert discovery[key]==replay[key]
        orders.append(int(replay['order']))
    assert len(set(orders))==1
    model=json.loads((HERE/'de_ferrari_a6_model.json').read_text())
    assert model['Nielsen_image_order']==2*orders[0]
    T=model['four_strand_target_order'];derived=360**53*orders[0];assert T==2*derived
    z4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    omega=H.power(H.mul(H.a,H.b),3)
    zorder=int(H.permutation(z4).order());omega_order=int(H.permutation(omega).order())
    assert zorder==20 and omega_order==40
    for g in (H.a,H.b,H.c):assert np.array_equal(H.mul(z4,g),H.mul(g,z4))
    out={'status':'PASS','Nielsen_order':model['Nielsen_image_order'],
         'Nielsen_derived_order':orders[0],'Nielsen_second_derived_order':orders[2],
         'Nielsen_derived_is_perfect':True,'Nielsen_abelianization_order':2,
         'full_target_order':T,'full_target_derived_order':derived,
         'full_target_derived_factorization':factorint(derived),
         'full_target_derived_is_perfect':True,
         'maximal_solvable_quotient':'C2, the actual braid exponent modulo2',
         'central_full_twist_order':zorder,'three_strand_full_twist_order':omega_order,
         'all_nested_input_word_certificates_linked':True,
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_target_derived.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'de_ferrari_a6_target_derived.npz',full_twist=z4,three_strand_twist=omega)
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

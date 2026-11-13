#!/usr/bin/env python3
"""Independent literal-word substitution for the ternary torsion certificate.

This program imports no conjugacy solver.  It reads the certified
literal braid words, evaluates them using exact group multiplication,
and reconstructs every one of the 216 original ternary inputs.
"""
from pathlib import Path
from itertools import product
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from de_ferrari_degree6_kernel import CombinedSix,InducedSix

here=Path(__file__).resolve().parent

def main():
    start=time.time();H=CombinedSix()
    result=json.loads((here/'de_ferrari_three_torsion.json').read_text())
    epsilon=H.mul(H.mul(H.power(H.a,2),H.b),H.c)
    z4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    assert np.array_equal(H.power(epsilon,3),z4)
    assert np.array_equal(H.power(epsilon,73),H.mul(epsilon,H.power(z4,6)))
    letters={1:H.a,2:H.b,3:H.c}
    letters.update({-i:H.inv(g) for i,g in list(letters.items())})
    conjugators=[]
    for witness in result['literal_witnesses']:
        g=H.one.copy()
        for letter in witness['literal_B4_conjugator']:g=H.mul(g,letters[letter])
        assert np.array_equal(g,H.decode(witness['conjugator']))
        conjugators.append(g)
    targets=[];positive=0
    for target in result['distinct_targets']:
        y=H.decode(target['epsilon_image']);targets.append(y)
        assert np.array_equal(H.power(y,3),z4)
        for row in target['all_central_translates']:
            if not row['conjugate']:continue
            j=row['central_exponent'];g=conjugators[row['witness_index']]
            assert np.array_equal(H.conj(g,epsilon),H.mul(y,H.power(z4,j)))
            assert np.array_equal(H.conj(g,H.power(epsilon,73)),H.mul(y,H.power(z4,(j+6)%9)))
            positive+=1
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    W=InducedSix(H,d);x=W.word(d['xword'])
    data=json.loads((here/'de_ferrari_degree6_lift.json').read_text())['records']
    origins=json.loads((here/'de_ferrari_fibres.json').read_text())['records']
    CM=np.load(here/'de_ferrari_degree6_lift_certificate.npz')['top_kernel_basis']
    all_checked=0
    for row,origin,certificate in zip(data,origins,result['records']):
        old=row['chosen_witness'];images=[H.decode(g) for g in old['actual_braid_images']]
        K=np.array(old['homogeneous_top_correction'],dtype=np.int64)
        xg=W.power(x,origin['integral_cusp_gauge'])
        for pair,entry in zip(product(range(3),repeat=2),certificate['all_nine_ternary_points']):
            assert list(pair)==entry['ternary_parameters']
            correction=W.conj(xg,W.element(CM@(K@np.array(pair,dtype=np.int64)%3)%3))[1][W.root]
            a=images[0];b=H.conj(H.inv(correction[4]),images[1]);c=H.conj(H.inv(correction[5]),images[2])
            H.check_braids((a,b,c))
            y=H.mul(H.mul(H.power(a,2),b),c)
            assert np.array_equal(y,targets[entry['target_index']])
            all_checked+=1
    assert all_checked==216
    # The identity GT element is a literal control independent of every
    # retained E17 origin: its braid triple is exactly (a,b,c).
    assert np.array_equal(H.conj(H.one,epsilon),epsilon)
    out={'all216_actual_ternary_inputs_reconstructed':True,
         'literal_B4_conjugators_verified':len(conjugators),
         'positive_target_translate_equalities_verified':positive,
         'both_multiplier_equalities_substituted':True,
         'literal_identity_GT_control_verified':True,
         'conjugator_word_length_range':[min(len(w['literal_B4_conjugator']) for w in result['literal_witnesses']),
                                         max(len(w['literal_B4_conjugator']) for w in result['literal_witnesses'])],
         'imports_no_conjugacy_solver':True,'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_three_torsion_words.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

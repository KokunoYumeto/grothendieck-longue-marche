#!/usr/bin/env python3
"""Independent literal B4 conjugator certificates for every E24 input."""
from pathlib import Path
from itertools import groupby
import json,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_generation import Collector

def main():
    start=time.time();here=Path(__file__).resolve().parent;H=FerrariTwo(6)
    generation=json.loads((here/'de_ferrari_two_generation.json').read_text())
    data=json.loads((here/'de_ferrari_two_torsion.json').read_text())
    images={1:H.a,2:H.b,3:H.c,-1:H.inv(H.a),-2:H.inv(H.b),-3:H.inv(H.c)}
    def inverse_word(w):return [-t for t in w[::-1]]
    def evaluate(w):
        out=H.one.copy()
        for t,letters in groupby(w):out=H.mul(out,H.power(images[t],sum(1 for _ in letters)))
        return out
    basis_words=[];C=Collector(H)
    for i,(dag,encoding) in enumerate(zip(generation['literal_source_expression_DAG'],generation['actual_polycyclic_basis'])):
        expression=dag['start']
        if 'literal_B4_word' in expression:w=list(expression['literal_B4_word'])
        elif 'square_of_basis' in expression:w=basis_words[expression['square_of_basis']]*2
        else:
            a,b=expression['commutator_of_basis'];wa,wb=basis_words[a],basis_words[b]
            w=wa+wb+inverse_word(wa)+inverse_word(wb)
        for j in dag['right_inverse_factors']:w+=inverse_word(basis_words[j])
        g=evaluate(w);assert np.array_equal(g,H.decode(encoding))
        assert C.add(g,{'literal_B4_word':w})
        assert np.array_equal(C.basis[i],g);basis_words.append(w)
    assert len(C.basis)==40;C.verify()
    x=H.power(H.mul(H.mul(H.a,H.b),H.c),2)
    unique={};witnesses=[];records=[]
    for row in data['records']:
        witness=next(w for w in row['witnesses'] if w['central_exponent']==0)
        g=H.decode(witness['conjugator']);key=tuple(g)
        if key not in unique:
            U=H.decode(witness['U_factor']);residual,coeff=C.reduce(U)
            assert np.array_equal(residual,H.one)
            word=[]
            for j in coeff[::-1]:word+=basis_words[j]
            word+=witness['outer_word']
            assert np.array_equal(evaluate(word),g)
            value=H.conj(g,x);assert np.array_equal(value,H.decode(row['image_delta_squared']))
            unique[key]=len(witnesses)
            witnesses.append({'literal_B4_conjugator_word':word,'word_length':len(word),
                              'conjugator':H.encode(g),'target_delta_squared':H.encode(value)})
        wi=unique[key];value=H.decode(witnesses[wi]['target_delta_squared'])
        assert np.array_equal(value,H.decode(row['image_delta_squared']))
        records.append({'certificate_index':row['certificate_index'],'lambda_residue':row['lambda_residue'],
                        'binary_parameter':row['binary_parameter'],'literal_witness_index':wi})
    out={'all_96_inputs_verified':len(records),'distinct_literal_conjugators':len(witnesses),
         'literal_word_lengths':[w['word_length'] for w in witnesses],
         'all40_polycyclic_basis_words_rebuilt_from_original_braid_generators':True,
         'no_conjugacy_solver_imported_or_run':True,'witnesses':witnesses,'records':records,
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_two_torsion_words.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('witnesses','records')},indent=2),flush=True)

if __name__=='__main__':main()

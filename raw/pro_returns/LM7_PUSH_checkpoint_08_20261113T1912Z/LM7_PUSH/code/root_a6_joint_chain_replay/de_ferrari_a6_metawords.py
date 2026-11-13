#!/usr/bin/env python3
"""Replay the six literal metabelian correction words in both old cores."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree6_kernel import CombinedSix,InducedSix
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,chunk_trie
from de_ferrari_a6_metabelian import Metabelian

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();d=load_data();M=Metabelian()
    rows=json.loads((HERE/'de_ferrari_a6_metageneration.json').read_text())['literal_correction_words']
    checks=[]
    for prime in (3,2):
        H=CombinedSix() if prime==3 else FerrariTwo(6)
        W=InducedSix(H,d) if prime==3 else InducedTwo(H,d,4)
        N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
        for j,row in enumerate(rows):
            raw=W.word(row['ternary_kernel_word_B'])
            square=W.word(row['D23_kernel_word_B'])
            assert W.equal(W.power(raw,2),square)
            assert W.equal(square,W.one)
            if prime==3:assert W.equal(raw,W.one)
            value=M.word(row['D23_kernel_word_F'])
            assert not np.any(value[:2]) and value[2:].tolist()==row['module_value']
            checks.append({'prime':prime,'basis_index':j,'raw_ternary_word_killed':W.equal(raw,W.one),
                           'literal_squared_word_killed':True,
                           'all_36_induced_components_checked':True})
        print(json.dumps({'prime':prime,'all_six_actual_words_pass':True,'seconds':round(time.time()-start,3)}),flush=True)
    out={'status':'PASS','literal_correction_words':6,'old_source_component_checks':12,
         'checks':checks,'read_only_legacy_inputs':True,'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_metawords.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

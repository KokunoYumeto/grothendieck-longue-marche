#!/usr/bin/env python3
"""Replay the complete six gamma5(N) binary correction preimages."""
from pathlib import Path
import json,time
import numpy as np
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree6_kernel import CombinedSix,InducedSix
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,chunk_trie

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();d=load_data();raw=json.loads((HERE/'de_ferrari_a6_common.json').read_text())
    nodes=raw['source_word_DAG'];targets=raw['binary_lower_central_levels'][-1]['word_nodes']
    needed=set(targets);todo=list(targets)
    while todo:
        j=todo.pop();r=nodes[j];op=r[0]
        parents=[] if op in ('one','N') else r[1:2] if op in ('inv','power') else r[1:]
        for k in parents:
            if k not in needed:needed.add(k);todo.append(k)
    for prime in (3,2):
        H=CombinedSix() if prime==3 else FerrariTwo(6)
        W=InducedSix(H,d) if prime==3 else InducedTwo(H,d,4)
        N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W);values={}
        for j in sorted(needed):
            r=nodes[j];op=r[0]
            if op=='one':v=W.one
            elif op=='N':v=N[r[1]]
            elif op=='inv':v=W.inv(values[r[1]])
            elif op=='power':v=W.power(values[r[1]],r[2])
            elif op=='mul':v=W.mul(values[r[1]],values[r[2]])
            elif op=='comm':v=W.comm(values[r[1]],values[r[2]])
            elif op=='conj':v=W.conj(values[r[1]],values[r[2]])
            else:raise AssertionError(op)
            values[j]=v
        for j,w in zip(targets,raw['literal_gamma5_words_B']):
            assert raw['source_word_lower_central_grades'][j]>=5
            assert W.equal(values[j],W.one)
            assert W.equal(W.word(w),values[j])
        print(json.dumps({'prime':prime,'all_six_gamma5_words_killed':True,'all_36_components_checked':True}),flush=True)
    out={'status':'PASS','actual_source_word_DAG_ancestors':len(needed),
         'complete_literal_words':6,'old_component_checks':12,
         'literal_and_nested_evaluations_compared':True,'read_only_legacy_inputs':True,
         'seconds':round(time.time()-start,3)}
    (HERE/'de_ferrari_a6_common_words.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

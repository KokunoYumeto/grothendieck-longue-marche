#!/usr/bin/env python3
"""Literal varied-support word inputs with the exact small-quotient gate.

These remain search inputs, never a generation assertion about their
large parent. The subsequent complete derived certificate and exact
quotient/order bounds supply the mathematical conclusion.
"""
from pathlib import Path
from hashlib import sha256
import argparse,json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_a6_schreier_certificate import read_certificate,verify_words
from de_a6_triple_base_prepare import evaluate

HERE=Path(__file__).resolve().parent

def products(words,original):
    inverse=np.argsort(original,axis=1).astype(np.uint16);out=[]
    for w in words:
        p=np.arange(original.shape[1],dtype=np.uint16)
        for j in w:p=(original[j-1] if j>0 else inverse[-j-1])[p]
        out.append(p)
    return np.array(out,dtype=np.uint16)

def order(a):return int(PermutationGroup([Permutation(g.tolist()) for g in a]).order())

def main():
    parser=argparse.ArgumentParser();parser.add_argument('parent');parser.add_argument('prefix')
    parser.add_argument('--quotient-input',required=True);parser.add_argument('--quotient-key',default='quotient_generators')
    parser.add_argument('--count',type=int,default=16);args=parser.parse_args();started=time.time()
    parent=Path(args.parent);prefix=Path(args.prefix);qfile=Path(args.quotient_input)
    hashes={str(p):sha256(p.read_bytes()).hexdigest() for p in [parent,qfile]}
    cert=read_certificate(parent);verify_words(cert);assert cert['derived']
    qo=np.load(qfile)[args.quotient_key].astype(np.uint16)
    assert len(qo)==len(cert['original'])
    qdict=evaluate(cert['nodes'],qo,cert['words']);qs=np.array([qdict[int(i)] for i in cert['words']],dtype=np.uint16)
    target=order(qs);rng=np.random.default_rng(606273+len(cert['strong']))
    for attempt in range(100):
        words=[]
        for _ in range(args.count):
            indices=rng.permutation(len(cert['strong']));coeff=rng.integers(-1,2,len(indices));word=[]
            for i,a in zip(indices,coeff):
                if a:word.append((int(i)+1)*int(a))
            words.append(word)
        qvalues=products(words,qs);actual=order(qvalues)
        if actual==target:break
    else:raise AssertionError('small quotient generation gate did not pass')
    values=products(words,cert['strong'])
    with Path(str(prefix)+'.input').open('w') as f:
        f.write(f'{cert["degree"]} {len(values)}\n')
        for p in values:f.write(' '.join(map(str,p))+'\n')
    np.savez_compressed(str(prefix)+'_input.npz',generators=values,
                        quotient_generators=qvalues,parent_quotient_strong_values=qs)
    out={'status':'PASS_LITERAL_VARIED_SUPPORT_INPUTS_AND_SMALL_QUOTIENT_GATE',
         'source_certificate':str(parent),'source_certificate_is_derived':True,
         'one_based_signed_strong_generator_words':words,
         'source_word_nodes':cert['words'].tolist(),'degree':cert['degree'],
         'small_quotient_parent_order':target,'small_quotient_word_image_order':actual,
         'deterministic_search_attempts':attempt+1,
         'all_parent_strong_words_independently_replayed':True,
         'large_parent_generation_not_asserted':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    Path(str(prefix)+'_input.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in
        ['one_based_signed_strong_generator_words','source_word_nodes']},indent=2),flush=True)

if __name__=='__main__':main()

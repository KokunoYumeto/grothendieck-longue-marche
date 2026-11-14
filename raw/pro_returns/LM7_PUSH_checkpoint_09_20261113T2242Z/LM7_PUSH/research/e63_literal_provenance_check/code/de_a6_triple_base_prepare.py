#!/usr/bin/env python3
"""Exact A6/affine-three joint base and saved nonfactor witness."""
from pathlib import Path
from hashlib import sha256
import json,struct,time
import numpy as np
from sympy.combinatorics import Permutation
from de_a6_schreier_certificate import read_certificate,verify_words

HERE=Path(__file__).resolve().parent


def evaluate(nodes,original,wanted):
    needed=set(map(int,wanted));stack=list(needed)
    while stack:
        i=stack.pop();op,a,b=map(int,nodes[i])
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            assert j<i
            if j not in needed:needed.add(j);stack.append(j)
    refs={i:0 for i in needed}
    for i in needed:
        op,a,b=map(int,nodes[i])
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    targets=set(map(int,wanted));saved={};values={};identity=np.arange(original.shape[1],dtype=np.uint16)
    def mul(x,y):return y[x]
    def inv(x):return np.argsort(x).astype(np.uint16)
    for i in sorted(needed):
        op,a,b=map(int,nodes[i])
        if op==0:v=identity
        elif op==1:v=original[a]
        elif op==2:v=mul(values[a],values[b])
        elif op==3:v=inv(values[a])
        elif op==4:v=mul(mul(mul(values[a],values[b]),inv(values[a])),inv(values[b]))
        elif op==5:v=mul(mul(values[a],values[b]),inv(values[a]))
        else:raise AssertionError(op)
        values[i]=v
        if i in targets:saved[i]=v.copy()
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j)
        if refs[i]==0:values.pop(i)
    return saved


def main():
    started=time.time();files=['de_a6_triple_affine_source.npz','de_a6_triple_affine_factor.json',
                              'de_a6_schreier_full_ordered.bin']
    hashes={p:sha256((HERE/p).read_bytes()).hexdigest() for p in files}
    raw=np.load(HERE/files[0]);affine=np.array([raw['s'],raw['r']],dtype=np.uint16)
    old=read_certificate(HERE/files[2]);verify_words(old)
    assert np.array_equal(old['original'],np.array([raw['old_s'],raw['old_r']]))
    nonfactor=json.loads((HERE/files[1]).read_text());node=nonfactor['rejection_word_node']
    assert not nonfactor['affine_source_factors'] and node>=0
    oldword=evaluate(nonfactor['literal_word_DAG'],old['original'],[node])[node]
    affineword=evaluate(nonfactor['literal_word_DAG'],affine,[node])[node]
    assert np.array_equal(oldword,np.arange(old['degree']))
    assert not np.array_equal(affineword,np.arange(324))
    values=evaluate(old['nodes'],affine,old['words'])
    oldn=old['degree'];n=oldn+324
    original=np.column_stack((old['original'],oldn+affine)).astype(np.uint16)
    strong=np.column_stack((old['strong'],oldn+np.array([values[int(w)] for w in old['words']]))).astype(np.uint16)
    lifted={**old,'degree':n,'original':original,'strong':strong}
    verify_words(lifted)
    path=HERE/'de_a6_triple_base_seed.bin'
    with path.open('wb') as f:
        def integer(v):f.write(struct.pack('<I',int(v)))
        integer(0x41365354);integer(n);integer(0);integer(2);f.write(original.astype('<u2').tobytes())
        integer(len(old['base']))
        for b in old['base']:integer(b)
        integer(len(strong))
        for w,d,p in zip(old['words'],old['depths'],strong):
            integer(w);integer(d);f.write(p.astype('<u2').tobytes())
        integer(len(old['nodes']));f.write(np.asarray(old['nodes'],dtype='<u4').tobytes())
    np.savez_compressed(HERE/'de_a6_triple_base_generators.npz',s=original[0],r=original[1],
                        nonfactor_affine_word=affineword,seed_original_word_nodes=old['words'])
    out={'status':'PASS_LITERAL_JOINT_BASE_PREPARATION','joint_degree':n,'old_degree':oldn,
         'affine_degree':324,'old_source_nonfactor_word_independently_replayed':True,
         'nonfactor_word_node':node,'nonfactor_affine_image_order':int(Permutation(affineword.tolist()).order()),
         'nonfactor_affine_support_size':int(np.count_nonzero(affineword!=np.arange(324))),
         'all_seed_strong_generator_words_independently_replayed':True,
         'seed_strong_count':len(strong),'seed_word_DAG_size':len(old['nodes']),
         'seed_is_not_a_complete_joint_certificate':True,'input_sha256':hashes,
         'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_base_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/p).read_bytes()).hexdigest()==v for p,v in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()

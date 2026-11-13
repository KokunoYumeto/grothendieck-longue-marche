#!/usr/bin/env python3
"""Faithful complete SL2(F3) Ferrari source with literal subgroup maps.

Every discarded transitive component is equipped with an actual intertwiner
of the original s/r actions.  H is the literal kernel F -> (Z/3)^2, not a
kernel in the Ferrari free group.  This file only writes new a_cm artifacts.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from a_cm_sl23_model import FerrariSL23
from de_ferrari_a6_source_data import load_data
from de_ferrari_a6_kernel_source import compress
from de_ferrari_degree4_lift import InducedCombined

HERE=Path(__file__).resolve().parent

def inverse_word(w):return [-a for a in w[::-1]]
def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:out.pop()
        else:out.append(a)
    return out

def main():
    started=time.time();H=FerrariSL23();d=load_data();W=InducedCombined(H,d)
    hd=24*H.n
    def permutation(e):
        return np.concatenate([hd*(6*int(e[0][q])+i)+
            np.asarray(H.permutation(e[1][q,i]).array_form,dtype=np.int64)
            for q in range(6) for i in range(6)])
    s,r=permutation(W.letters[0]),permutation(W.letters[1]);identity=np.arange(len(s))
    assert np.array_equal(s[s],identity) and np.array_equal(r[r[r]],identity)
    for a in (W.letters[0],W.letters[1],W.letters[-1]):
        for b in (W.letters[0],W.letters[1],W.letters[-1]):
            assert np.array_equal(permutation(W.mul(a,b)),permutation(b)[permutation(a)])
    new,metadata=compress(s,r)
    points=np.concatenate(metadata['retained_original_canonical_orders'])
    assert len(points)==len(new[0])
    inverse=np.full(len(s),-1,dtype=np.int64);inverse[points]=np.arange(len(points))
    for original,compressed in zip((s,r),new):
        assert np.array_equal(inverse[original[points]],compressed)
    n=len(points);one=np.arange(n);letters={0:new[0],1:new[1],-1:new[1][new[1]]}
    def evaluate(w):
        out=one.copy()
        for a in w:out=letters[a][out]
        return out
    section={(a,b):[1]*a+[2]*b for a in range(3) for b in range(3)}
    hwords=[]
    for (a,b),path in section.items():
        for letter,delta in ((1,(1,0)),(2,(0,1))):
            nxt=((a+delta[0])%3,(b+delta[1])%3)
            word=reduce_word(path+[letter]+inverse_word(section[nxt]))
            if word:hwords.append(word)
    assert len(hwords)==10 and len({tuple(w) for w in hwords})==10
    assert all(sum((a==j)-(a==-j) for a in w)%3==0 for w in hwords for j in (1,2))
    Hwords=[d['to_B'](w) for w in hwords]
    groups={'B':[[],[]],'F':[d['xword'],d['yword']],
            'H':Hwords,'N':d['Nwords']}
    images={'B':new}
    for name,words in groups.items():
        if name=='B':continue
        images[name]=np.array([evaluate(w) for w in words])
        for word,p in zip(words,images[name]):
            original=permutation(W.word(word))
            assert np.array_equal(inverse[original[points]],p)
    for name,perms in images.items():
        with (HERE/('a_cm_sl23_'+name+'_source.input')).open('w') as f:
            f.write(f'{n} {len(perms)}\n')
            for p in perms:f.write(' '.join(map(str,p))+'\n')
    np.savez_compressed(HERE/'a_cm_sl23_induced.npz',
        original_s=s,original_r=r,compressed_s=new[0],compressed_r=new[1],
        retained_original_points=points,H_generators=images['H'],
        N_generators=images['N'],F_generators=images['F'])
    out={**metadata,'status':'PASS_EXACT_COMPLETE_INDUCED_SL23_SOURCE',
         'H_free_basis_words':hwords,'H_basis_words_in_B':Hwords,
         'H_index_in_F':9,'H_free_rank':10,
         'H_exact_definition':'ker(F -> (Z/3)^2) = F-prime F^3',
         'all_nine_generator_product_comparisons':True,
         'every_H_and_N_word_compared_in_original_and_compressed_actions':True,
         'seconds':round(time.time()-started,3)}
    (HERE/'a_cm_sl23_induced.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in
        ('retained_original_canonical_orders','orbit_correspondences')},indent=2),flush=True)

if __name__=='__main__':main()

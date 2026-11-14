#!/usr/bin/env python3
"""Deterministic replay of the pure A96 generating certificate.

No search, probabilistic order procedure or generic stabilizer chain is
used. The certificate gives words in the four squared braid generators.
"""
from pathlib import Path
import json,math
import numpy as np
from e_hurwitz_five_a5_order_root import cycles,power

HERE=Path(__file__).resolve().parent

def verify(sig):
    rec=json.loads((HERE/'e_hurwitz_five_a5_order_pure_root.json').read_text())
    expected=np.load(HERE/'e_hurwitz_five_a5_order_pure_root.npz')['sigma']
    assert np.array_equal(sig,expected)
    n=len(sig[0]);one=np.arange(n)
    assert n==96 and rec['conjugators_are_words_in_signed_squares']
    assert all(sum(len(c)-1 for c in cycles(g))%2==0 for g in sig)
    letters={i+1:g[g] for i,g in enumerate(sig)}
    letters.update({-i:np.argsort(g) for i,g in list(letters.items())})
    w=one.copy()
    for t in rec['three_cycle_word_in_signed_squares']:w=letters[t][w]
    c=power(w,rec['isolating_power'])
    nontrivial=[v for v in cycles(c) if len(v)>1]
    assert nontrivial==[rec['three_cycle']]
    reached=set()
    for r in rec['conjugate_records']:
        g=one.copy()
        for t in r['conjugator_word']:g=letters[t][g]
        v=g[c[np.argsort(g)]]
        nontrivial=[t for t in cycles(v) if len(t)>1]
        assert nontrivial==[r['three_cycle']]
        support=set(nontrivial[0]);assert sorted(support)==r['support']
        assert len(support)==3
        assert not reached or (reached&support and support-reached)
        reached|=support
    assert reached==set(range(n))
    assert rec['pure_target_order']==rec['full_target_order']==math.factorial(n)//2
    return math.factorial(n)//2

if __name__=='__main__':
    sig=np.load(HERE/'e_hurwitz_five_a5_probe_root.npz')['sigma']
    print(json.dumps({'pure_and_full_order':verify(sig),'degree':len(sig[0]),
                      'all_pure_three_cycles_replayed':True},indent=2))
    print('PASS: constructive certificate independently replayed without search')

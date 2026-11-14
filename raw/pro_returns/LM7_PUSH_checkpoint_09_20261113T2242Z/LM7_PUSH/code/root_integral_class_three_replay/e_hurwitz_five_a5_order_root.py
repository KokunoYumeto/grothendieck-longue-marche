#!/usr/bin/env python3
"""A constructive alternating-group certificate for the 96-point action.

A literal pure-braid word is powered to a single 3-cycle. Its explicitly
recorded conjugates have a connected support hypergraph. Three-cycles
whose supports form a connected hypergraph generate the alternating
group on that support; the short induction proof is recorded separately.
This avoids the slow generic stabilizer-chain attempt and proves both
the full and pure images exactly, with no probable-order assertion.
"""
from pathlib import Path
import json,math,time
import numpy as np

HERE=Path(__file__).resolve().parent

def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen:continue
        cyc=[];v=i
        while v not in seen:seen.add(v);cyc.append(v);v=int(p[v])
        out.append(cyc)
    return out

def power(p,k):
    out=np.arange(len(p));g=p.copy()
    while k:
        if k&1:out=g[out]
        g=g[g];k//=2
    return out

def main():
    at=time.time();sig=np.load(HERE/'e_hurwitz_five_a5_probe_root.npz')['sigma']
    n=len(sig[0]);assert n==96
    one=np.arange(n);letters={i+1:g for i,g in enumerate(sig)}
    letters.update({-i:np.argsort(g) for i,g in list(letters.items())})
    assert all(sum(len(c)-1 for c in cycles(g))%2==0 for g in sig)
    pure={i:g[g] for i,g in letters.items()}
    rng=np.random.default_rng(202611131)
    options=[1,-1,2,-2,3,-3,4,-4]
    found=None
    for trial in range(1,2001):
        word=[int(x) for x in rng.choice(options,size=120)]
        w=one.copy()
        for i in word:w=pure[i][w]
        cc=cycles(w);triples=[c for c in cc if len(c)==3]
        if len(triples)!=1 or any(len(c)%3==0 for c in cc if c is not triples[0]):continue
        exponent=math.lcm(*(len(c) for c in cc if len(c)!=3))
        c=power(w,exponent)
        assert sorted(len(v) for v in cycles(c) if len(v)>1)==[3]
        found=(word,exponent,c,trial);break
    assert found is not None,'bounded search found no isolating word'
    word,exponent,c,trial=found
    print('Single pure three-cycle found at trial',trial,'power',exponent,flush=True)
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:parent[v]=parent[parent[v]];v=parent[v]
        return v
    def join(triple):
        a=root(triple[0])
        for b in triple[1:]:parent[root(b)]=a
    supp=tuple(sorted(np.flatnonzero(c!=one).tolist()))
    queue=[(c,[])];seen={supp};records=[];all_support=set()
    for v,cword in queue:
        support=sorted(np.flatnonzero(v!=one).tolist());assert len(support)==3
        join(support);all_support.update(support)
        records.append({'support':support,'conjugator_word':cword,
                        'three_cycle':next(cc for cc in cycles(v) if len(cc)==3)})
        if len(all_support)==n and len({root(i) for i in range(n)})==1:break
        for t in options:
            g=letters[t];nxt=g[v[np.argsort(g)]]
            ns=tuple(sorted(np.flatnonzero(nxt!=one).tolist()))
            if ns not in seen:seen.add(ns);queue.append((nxt,cword+[t]))
    assert len(all_support)==n and len({root(i) for i in range(n)})==1
    # Order the certificate into a union-building sequence. At every step
    # a retained triple meets the union and adds one or two new vertices.
    remaining=list(range(len(records)));ordered=[remaining.pop(0)]
    reached=set(records[ordered[0]]['support'])
    while len(reached)<n:
        i=next(i for i in remaining if set(records[i]['support'])&reached
               and set(records[i]['support'])-reached)
        remaining.remove(i);ordered.append(i);reached.update(records[i]['support'])
    assert reached==set(range(n))
    # Replay every retained conjugator from the original four arrays.
    for i in ordered:
        rec=records[i];g=one.copy()
        for t in rec['conjugator_word']:g=letters[t][g]
        v=g[c[np.argsort(g)]]
        assert sorted(np.flatnonzero(v!=one).tolist())==rec['support']
        assert next(cc for cc in cycles(v) if len(cc)==3)==rec['three_cycle']
    out={'degree':n,'full_target_order':math.factorial(n)//2,
         'pure_target_order':math.factorial(n)//2,
         'image_is_alternating_group':True,'all_original_generators_even':True,
         'three_cycle_word_in_signed_squares':word,'isolating_power':exponent,
         'isolating_word_trial':trial,'three_cycle':next(cc for cc in cycles(c) if len(cc)==3),
         'conjugate_records':[records[i] for i in ordered],
         'connected_support_vertices':n,'retained_conjugate_count':len(ordered),
         'all_conjugates_replayed':True,'seconds':round(time.time()-at,3)}
    (HERE/'e_hurwitz_five_a5_order_root.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/'e_hurwitz_five_a5_order_root.npz',sigma=sig,
                       pure_three_cycle=c,initial_pure_word_value=w)
    print(json.dumps({k:v for k,v in out.items() if k not in
         ('three_cycle_word_in_signed_squares','conjugate_records')},indent=2),flush=True)
    print('PASS: exact full and pure A96 images by connected three-cycle certificate',flush=True)

if __name__=='__main__':main()

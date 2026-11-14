#!/usr/bin/env python3
"""Portable reader and independent NumPy replay of the exact word DAG.

The C++ replay separately enumerates and sifts all final Schreier relations.
This program checks every saved strong generator's membership in the original
group, and in its derived subgroup for a derived certificate, using independent
array arithmetic.  The certificate format stores no executable instructions.
"""
from pathlib import Path
import argparse,json,struct,time
import numpy as np

def read_certificate(path):
    raw=Path(path).read_bytes();at=0
    def integer():
        nonlocal at
        ans=struct.unpack_from('<I',raw,at)[0];at+=4;return ans
    def points(n):
        nonlocal at
        ans=np.frombuffer(raw,dtype='<u2',count=n,offset=at);at+=2*n;return ans
    magic=integer();assert magic in (0x41365353,0x41365354)
    n=integer();derived=bool(integer()) if magic==0x41365354 else False
    m=integer();original=points(n*m).reshape(m,n)
    b=integer();base=np.array([integer() for _ in range(b)],dtype=np.int64)
    k=integer();words=[];depths=[];strong=[]
    for _ in range(k):
        words.append(integer());depths.append(integer());strong.append(points(n))
    nn=integer();nodes=np.frombuffer(raw,dtype='<u4',count=3*nn,offset=at).reshape(nn,3);at+=12*nn
    assert at==len(raw)
    return {'degree':n,'derived':derived,'original':original,'base':base,
            'strong':np.array(strong,dtype=np.uint16).reshape(k,n),
            'words':np.array(words,dtype=np.int64),'depths':np.array(depths,dtype=np.int64),'nodes':nodes}

def verify_words(d):
    n=d['degree'];id=np.arange(n,dtype=np.uint16);nodes=d['nodes'];refs=np.zeros(len(nodes),dtype=np.int64)
    checks={}
    for j,w in enumerate(d['words']):checks.setdefault(int(w),[]).append(j)
    for i,(op,a,b) in enumerate(nodes):
        if op in (2,3,4,5):assert a<i;refs[a]+=1
        if op in (2,4,5):assert b<i;refs[b]+=1
    values={};derived=np.zeros(len(nodes),dtype=bool)
    def mul(x,y):return y[x]
    def inv(x):return np.argsort(x).astype(np.uint16)
    for i,(op,a,b) in enumerate(nodes):
        if op==0:assert i==0;p=id;derived[i]=True
        elif op==1:p=d['original'][a]
        elif op==2:p=mul(values[a],values[b]);derived[i]=derived[a] and derived[b]
        elif op==3:p=inv(values[a]);derived[i]=derived[a]
        elif op==4:
            p=mul(mul(mul(values[a],values[b]),inv(values[a])),inv(values[b]));derived[i]=True
        elif op==5:p=mul(mul(values[a],values[b]),inv(values[a]));derived[i]=derived[b]
        else:raise AssertionError('unknown word operation')
        for j in checks.get(i,[]):
            assert np.array_equal(p,d['strong'][j])
            if d['derived']:assert derived[i]
        values[i]=p
        if op in (2,3,4,5):
            refs[a]-=1
            if refs[a]==0:values.pop(a)
        if op in (2,4,5):
            refs[b]-=1
            if refs[b]==0:values.pop(b)
        if refs[i]==0:values.pop(i)
    for p,depth in zip(d['strong'],d['depths']):
        assert np.array_equal(np.sort(p),id)
        assert np.array_equal(p[d['base'][:depth]],d['base'][:depth])
        assert p[d['base'][depth]]!=d['base'][depth]
    for p in d['original']:assert np.array_equal(np.sort(p),id)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('certificate');parser.add_argument('--output-prefix')
    args=parser.parse_args();start=time.time();d=read_certificate(args.certificate);verify_words(d)
    prefix=Path(args.output_prefix) if args.output_prefix else Path(args.certificate).with_suffix('')
    np.savez_compressed(str(prefix)+'_certificate.npz',original_generators=d['original'],
        strong_generators=d['strong'],base=d['base'],strong_word_nodes=d['words'],
        strong_depths=d['depths'],word_DAG=d['nodes'])
    out={'status':'PASS','degree':d['degree'],'derived_mode':d['derived'],
         'original_generator_count':len(d['original']),'strong_generator_count':len(d['strong']),
         'word_DAG_node_count':len(d['nodes']),
         'all_strong_generator_words_independently_evaluated':True,
         'all_required_derived_source_memberships_verified':True,
         'all_actual_strong_stabilizer_depths_verified':True,'seconds':round(time.time()-start,3)}
    Path(str(prefix)+'_word_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()

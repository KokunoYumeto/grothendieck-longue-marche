#!/usr/bin/env python3
"""Literal commutator generation of the 115248-element B4 image."""
from pathlib import Path
from hashlib import sha256
from collections import deque
import json,time
import numpy as np

HERE=Path(__file__).resolve().parent
def key(a):return np.asarray(a,dtype=np.uint8).tobytes()
def mul(a,b):return b@a%7
def inv(a):
    a=a.copy()%7;b=np.eye(4,dtype=np.int64)
    for j in range(4):
        k=j+int(np.flatnonzero(a[j:,j])[0]);a[[j,k]]=a[[k,j]];b[[j,k]]=b[[k,j]]
        t=pow(int(a[j,j]),-1,7);a[j]=t*a[j]%7;b[j]=t*b[j]%7
        c=a[:,j].copy();c[j]=0;a=(a-c[:,None]*a[j][None,:])%7;b=(b-c[:,None]*b[j][None,:])%7
    assert np.array_equal(a,np.eye(4,dtype=np.int64));return b
def invword(w):return [-x for x in reversed(w)]
def evaluate(w,letters):
    a=np.eye(4,dtype=np.int64)
    for t in w:a=mul(a,letters[t])
    return a
def closure(gs,limit=115248):
    one=np.eye(4,dtype=np.int64);vals=[one];seen={key(one)}
    for a in vals:
        for b in gs:
            c=mul(a,b);k=key(c)
            if k not in seen:seen.add(k);vals.append(c);assert len(vals)<=limit
    return vals,seen
def main():
    started=time.time();names=['bc_symplectic_five_p7_model.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    A=np.load(HERE/names[0])['matrices'][:3];letters={i+1:a for i,a in enumerate(A)}
    letters.update({-i-1:inv(a) for i,a in enumerate(A)})
    full,fullkeys=closure(A);assert len(full)==115248
    words=[[1,2,-1,-2],[2,3,-2,-3]];gs=[evaluate(w,letters) for w in words]
    vals,seen=closure(gs);progress=[len(vals)]
    at=0
    while at<len(gs):
        g,w=gs[at],words[at]
        for j in (1,2,3):
            v=[j]+w+[-j];h=evaluate(v,letters)
            if key(h) not in seen:
                gs.append(h);words.append(v);vals,seen=closure(gs);progress.append(len(vals))
        at+=1
    assert len(vals)==115248 and seen==fullkeys
    assert all(key(evaluate([j]+w+[-j],letters)) in seen for w in words for j in (1,2,3))
    out={'status':'PASS_LITERAL_P7_B4_PERFECTNESS','group_order':115248,
         'normal_commutator_closure_orders':progress,'derived_group_order':len(vals),
         'literal_commutator_and_conjugate_generators':words,
         'right_permutation_matrix_product':'mul(A,B)=B A',
         'all_group_elements_and_conjugation_closure_checked':True,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    p=HERE/'bc_symplectic_five_p7_target_perfect'
    p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(p.with_suffix('.npz'),all_elements=np.stack(full),derived_generators=np.stack(gs))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'},indent=2),flush=True)
if __name__=='__main__':main()

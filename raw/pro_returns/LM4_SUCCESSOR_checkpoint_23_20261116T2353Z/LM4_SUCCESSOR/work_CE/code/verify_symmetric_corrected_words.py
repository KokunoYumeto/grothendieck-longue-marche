#!/usr/bin/env python3
"""Independent sequential geometric-word audit of corrected based data.
No crossing producer or its art() routine is imported. Each elementary
geometric push is applied directly to a free word in chronological order.
"""
from pathlib import Path
import json, hashlib, time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_node_words_pullback_corrected.json',
       'symmetric_old_base_words_pullback_corrected.json',
       'symmetric_source_bridge_pullback_corrected.json']
raw={n:(P/n).read_bytes() for n in names};nodes,old,bridge=[json.loads(raw[n]) for n in names]
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def loc(x,g):
    i=abs(g);j=abs(x)
    if g>0:v=(i,i+1,-i) if j==i else (i,) if j==i+1 else (j,)
    else:v=(i+1,) if j==i else (-i-1,i,i+1) if j==i+1 else (j,)
    return v if x>0 else inv(v)
def push_word(w,word):
    for g in w:word=red(y for x in word for y in loc(x,g))
    return word
def back_word(w,word):return push_word(tuple(-g for g in reversed(w)),word)
def maps(d):return {int(i):tuple(w) for i,w in d.items()}
def inner_word(E):
    c={}
    for j,e in E.items():
        left,right=0,len(e)
        while right-left>1 and e[left]==-e[right-1]:left+=1;right-=1
        assert e[left:right]==(j,);c[j]=e[:left]
    v=red(inv(c[1])+c[2]);n=0;k=0
    while k<len(v) and abs(v[k])==1:n+=v[k];k+=1
    assert not v[k:] or all(x==v[k] and abs(x)==2 for x in v[k:])
    g=red(c[1]+((1,)*n if n>=0 else (-1,)*(-n)))
    assert all(E[j]==red(g+(j,)+inv(g)) for j in range(1,22))
    return g
start=time.monotonic();rows=[];F=maps(bridge['nodal_involution_images'])
for row in nodes['loops']:
    W=row['whisker'];w=row['word'];A=maps(row['geometric_push_images']);Ai=maps(row['based_pullback_images'])
    for j in range(1,22):
        assert push_word(w,(j,))==A[j] and back_word(w,(j,))==Ai[j]
    for node in row['nodes']:
        u,v=[back_word(W,(j,)) for j in node['local_positions']]
        assert [list(u),list(v)]==node['meridians']
        assert red(u+v+inv(u)+inv(v))==tuple(node['commutator'])
    # This geometric consistency test failed in the superseded convention.
    comm={j:sub(sub(sub(Ai[j],F),A),F) for j in range(1,22)}
    k=inner_word(comm);assert red(sub(k,F)+k)==()
    rows.append({'index':row['index'],'basis_images':42,
                 'node_count':len(row['nodes']),'F_commutator_inner_word':k})
    print('PASS independent corrected node',row['index'],'and all21 F compatibility images; inner length',len(k),flush=True)
for row in old['loops']:
    A=maps(row['geometric_push_images']);Ai=maps(row['based_pullback_images'])
    for j in range(1,22):assert push_word(row['word'],(j,))==A[j] and back_word(row['word'],(j,))==Ai[j]
print('PASS all6 corrected old actions by direct chronological local substitution.',flush=True)
W=bridge['nodal_base_to_pairing_base_braid'];A=maps(bridge['nodal_generators_in_endpoint_base']);Ai=maps(bridge['endpoint_generators_in_nodal_base'])
for j in range(1,22):assert push_word(W,(j,))==A[j] and back_word(W,(j,))==Ai[j]
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in raw.items()},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'node_checks':rows,'old_basis_images_checked':252,'bridge_images_checked':42,
 'elapsed_seconds':time.monotonic()-start,
 'claims_excluded':['full relation-module closure','syzygy vanishing','source image equality']}
(P/'symmetric_corrected_words_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS corrected geometric package; elapsed',round(out['elapsed_seconds'],3),flush=True)

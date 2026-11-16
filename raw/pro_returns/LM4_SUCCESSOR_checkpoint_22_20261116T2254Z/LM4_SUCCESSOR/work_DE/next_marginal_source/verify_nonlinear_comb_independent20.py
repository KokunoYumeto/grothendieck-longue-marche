#!/usr/bin/env python3
"""Independent complete replay of the existing nonlinear comb certificate.

No producer imports, orbit search, or expansion of large comb generators.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
P=ROOT/'work_CE/next_symmetric_nodes'
started=time.monotonic()
paths={k:P/v for k,v in {
 'comb':'nonlinear_comb_rewrite.json',
 'full':'actual_full21_Fox.json',
 'finite':'finite_even_boundary32.json',
 'factored':'geometric_stabilizer_factored_chain.json'}.items()}
D={k:json.loads(p.read_text()) for k,p in paths.items()}
C=D['comb']; T=C['retained_word_DAG']; R=C['R_word_DAG']

def audit_dag(nodes):
    assert nodes[0]==[0,0,0]
    edges={}
    for i,(p,x,n) in enumerate(nodes[1:],1):
        assert 0<=p<i and x and n==nodes[p][2]+1
        assert not p or nodes[p][1]!=-x
        assert (p,x) not in edges
        edges[p,x]=i
    return edges

TE=audit_dag(T); RE=audit_dag(R)
def step(nodes,edges,p,x):
    return nodes[p][0] if p and nodes[p][1]==-x else edges[p,x]
@lru_cache(None)
def readT(p):
    return readT(T[p][0])+(T[p][1],) if p else ()
@lru_cache(None)
def readR(p):
    return readR(R[p][0])+(R[p][1],) if p else ()
def inv(w): return tuple(-x for x in reversed(w))
def push(w,x):
    if w and w[-1]==-x:w.pop()
    else:w.append(x)
def reduced(w):
    r=[]
    for x in w:push(r,x)
    return r
def abelian(w):
    q=Counter()
    for x in w:q[abs(x)]+=1 if x>0 else -1
    return {k:v for k,v in q.items() if v}

rgens=C['common_R_generators']; rid={tuple(v):i for i,v in enumerate(rgens[1:],1)}
ngens=C['N_free_generators']; nid={tuple(v):i for i,v in enumerate(ngens[1:],1)}
assert len(rid)==len(rgens)-1 and len(nid)==len(ngens)-1
for a,b,x in ngens[1:]:assert 0<a<len(R) and 0<=b<len(R) and 0<x<len(rgens)
old={j:i+1 for i,j in enumerate(D['full']['retained_paired_indices'])}
beta={int(k):v[0] for k,v in D['full']['retained_involution'].items()}
nodewords={(f['sheet'],tuple(f['node_index'])):f['literal_F21_word']
           for f in D['finite']['faces'] if f['type']=='node'}
assert len(nodewords)==128

for rec in C['records']:
    w=rec['literal_F21_word']
    if 'sheet' in rec:assert w==nodewords[rec['sheet'],tuple(rec['node_index'])]
    else:assert w==D['factored']['circuits'][1]['literal_F21_word']
    a=b=t=bt=0; actual=[]; schwarz=[]
    for letter in w:
        j=abs(letter);sgn=1 if letter>0 else -1
        if j in old:
            k=old[j];t=step(T,TE,t,sgn*k);bt=step(T,TE,bt,sgn*beta[k])
        elif j<12:
            x=rid[t,j];a=step(R,RE,a,sgn*x);push(schwarz,sgn*(2*x-1))
        else:
            x=rid[bt,j-10];newb=step(R,RE,b,sgn*x)
            if a:push(actual,sgn*nid[a,b if sgn>0 else newb,x])
            b=newb;push(schwarz,sgn*2*x)
    assert (a,b,t,bt)==(0,0,0,0)
    assert actual==rec['nonlinear_N_word']
    assert abelian(actual)==dict(rec['abelianization'])
    if 'sheet' in rec:
        expanded=[]
        for letter in actual:
            av,bv,x=ngens[abs(letter)]
            aw=tuple((1 if z>0 else -1)*(2*abs(z)-1) for z in readR(av))
            bw=tuple(2*z for z in readR(bv))
            cw=bw+aw+(2*x,)+inv(aw)+(-2*x,)+inv(bw)
            for z in (cw if letter>0 else inv(cw)):push(expanded,z)
        assert expanded==schwarz
        witness=rec['single_occurrence_primitive_witness']; x=witness['basis_generator']
        assert sum(abs(z)==x for z in actual)==1
        pos=witness['position'];assert actual[pos]==witness['sign']*x

# Reconstruct both full prior root-path dictionaries, including the large
# one, directly in the same semantic word labels. No N generator expands.
B=D['factored']
def oldread(nodes,p):
    out=[]
    while p:p,x,n=nodes[p];out.append(x)
    return tuple(reversed(out))
tids={readT(i):i for i in range(len(T))}
oldgens={i:rid[tids[oldread(B['retained_word_DAG'],t)],slot]
         for i,(t,slot) in enumerate(B['common_R_generators'][1:],1)}
def translateR(p):
    out=0
    for x in oldread(B['R_word_DAG'],p):
        out=step(R,RE,out,(1 if x>0 else -1)*oldgens[abs(x)])
    return out
small=next(r for r in C['records'] if r.get('sheet')==0 and r.get('node_index')==[8,0])
for rec,circuit in [(small,B['circuits'][0]),(C['records'][-1],B['circuits'][1])]:
    target={nid[translateR(c['A_endpoint']),translateR(c['B_edge_start']),oldgens[c['B_generator']]]:c['coefficient']
            for c in circuit['rectangles']}
    assert abelian(rec['nonlinear_N_word'])==target

out={'result':'PASS','input_sha256':{k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in paths.items()},
 'entire_literal_prefix_replays':129,'entire_short_free_product_expansions':128,
 'individual_primitive_witnesses':128,'both_complete_root_path_abelianizations':True,
 'counts':C['counts'],'no_producer_imports':True,'no_large_generator_expansion':True,
 'scope':'Exact complete words and individual primitives only; no simultaneous-basis or quotient-freeness claim.',
 'elapsed_seconds':time.monotonic()-started}
(OUT/'nonlinear_comb_independent_review20.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all129 exact comb rewrites; all128 full short expansions and primitive witnesses')
print('PASS both complete root-path abelianizations; no large generator expansion')
print(json.dumps(out['counts'],sort_keys=True));print('elapsed',out['elapsed_seconds'])

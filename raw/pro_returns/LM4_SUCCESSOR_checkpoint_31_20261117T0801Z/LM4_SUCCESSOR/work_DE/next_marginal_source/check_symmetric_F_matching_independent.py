#!/usr/bin/env python3
"""Independent verification of the actual finite F/node matching certificate.

No producer is imported. Literal F21 identities are substituted directly.
Each recorded two-chain is checked by its full product-tree edge boundary;
the product of two Cayley trees has injective two-boundary. Retained deck
words and E coefficients are checked separately.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
DIR=ROOT/'work_CE/next_symmetric_nodes'
paths=[DIR/'symmetric_paired_fox_data.json',DIR/'symmetric_F_node_matching.json']
raw=[p.read_bytes() for p in paths]
P,D=map(json.loads,raw)
start=time.monotonic()

def reduce(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x:ans.pop()
        else:ans.append(int(x))
    return tuple(ans)
def inverse(w):return tuple(-x for x in reversed(w))
def substitute(w,images):
    return reduce(y for x in w for y in (images[abs(x)] if x>0 else inverse(images[abs(x)])))
def add(out,key,value):
    out[key]+=value
    if out[key]==0:del out[key]

F={int(j):tuple(w) for j,w in P['paired_involution'].items()}
old=list(P['retained_paired_indices'])
old_index={j:k+1 for k,j in enumerate(old)}
beta={int(j):tuple(w) for j,w in P['retained_involution'].items()}
meta={int(j):(tuple(v['retained_word']),v['paired_slot']) for j,v in D['common_R_basis'].items()}
lookup={v:j for j,v in meta.items()}
assert len(meta)==len(lookup)

def fill(w):return reduce(x for x in w if abs(x) in old_index)
def fill5(w):return reduce((1 if x>0 else -1)*old_index[abs(x)] for x in w if abs(x) in old_index)
def schreier(w):
    head=();word=[]
    for x in w:
        j=abs(x);sign=1 if x>0 else -1
        if j in old_index:
            head=reduce(head+(sign*old_index[j],))
        else:
            side=0 if j<12 else 1
            key=(head if side==0 else substitute(head,beta),j if side==0 else j-10)
            number=lookup[key]
            word.append(sign*(2*number-1+side))
    assert head==()
    return reduce(word)
def project(word,side):
    return reduce((1 if x>0 else -1)*((abs(x)+1)//2) for x in word if (abs(x)%2==1)==(side==0))
def decode(rows):
    out={}
    for r in rows:
        key=(tuple(r['A_vertex']),tuple(r['B_vertex']),r['A_generator'],r['B_generator'])
        assert key not in out and r['coefficient']
        out[key]=r['coefficient']
    return out
def boundary(chain):
    out=defaultdict(int)
    for (a,b,i,j),c in chain.items():
        add(out,(0,a,b,i),c)
        add(out,(0,a,reduce(b+(j,)),i),-c)
        add(out,(1,reduce(a+(i,)),b,j),c)
        add(out,(1,a,b,j),-c)
    return dict(out)
def edge_walk(word):
    position=[(),()];out=defaultdict(int)
    for x in word:
        side=0 if abs(x)%2 else 1
        letter=(1 if x>0 else -1)*((abs(x)+1)//2)
        destination=reduce(position[side]+(letter,))
        endpoint=list(position)
        if x<0:endpoint[side]=destination
        add(out,(side,endpoint[0],endpoint[1],abs(letter)),1 if x>0 else -1)
        position[side]=destination
    assert position==[(),()]
    return dict(out)

node={(r['loop_index'],r['local_node_index']):r for r in P['node_columns']}
def normalized(r):
    w=tuple(r['paired_relator'])
    return w if r['physical_labels'][0]<11 else inverse(w)
checked=[];empty_deck=0;fixed=0
for row in D['rows']:
    key=tuple(row['node_index']);matekey=tuple(row['physical_F_mate_index'])
    source=node[key];mate=node[matekey]
    assert key[0]==matekey[0]
    assert {i+8 if i<11 else i-8 for i in source['physical_labels']}==set(mate['physical_labels'])
    r=normalized(source);m=normalized(mate)
    fr=substitute(r,F);g=tuple(row['conjugator_F21'])
    assert fr==reduce(g+inverse(m)+inverse(g))==tuple(row['F_normalized_relator'])
    assert substitute(fr,F)==r
    t=fill(g);n=reduce(g+inverse(t))
    assert t==tuple(row['retained_deck_F21'])
    assert fill5(t)==tuple(row['retained_deck_F5'])
    assert n==tuple(row['kernel_part_F21']) and not fill(n)
    nk=schreier(n)
    a,b=project(nk,0),project(nk,1)
    assert a==tuple(row['E_coefficient']['A_word'])
    assert b==tuple(row['E_coefficient']['B_word'])
    left=decode(row['F_normalized_column'])
    deckchain=decode(row['deck_mate_normalized_column'])
    assert boundary(left)==edge_walk(schreier(fr))
    assert boundary(deckchain)==edge_walk(schreier(reduce(t+m+inverse(t))))
    right={(reduce(a+u),reduce(b+v),i,j):-c for (u,v,i,j),c in deckchain.items()}
    assert left==right
    original=decode(source['fox_cells']);orientation=1 if source['physical_labels'][0]<11 else -1
    assert left=={(v,u,j,i):-orientation*c for (u,v,i,j),c in original.items()}
    empty_deck+=not t;fixed+=key==matekey
    checked.append({'node':key,'mate':matekey,'deck_F5':fill5(t),'conjugator_length':len(g),'left_cells':len(left),'right_cells':len(deckchain)})

assert len(checked)==64 and empty_deck==12 and fixed==8
out={'input_sha256':{p.name:hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
     'checks':checked,'full_word_identities':64,'full_two_chain_boundary_checks':128,
     'literal_chain_identities':64,'empty_deck_count':empty_deck,'fixed_physical_nodes':fixed,
     'scope':'actual finite F/node word and full-chain matches only; no full equivariant presentation-kernel identification, kappa value or source equality',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'symmetric_F_matching_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:64 literal F21 physical-mate conjugacies and128 full product-tree boundary checks.')
print('PASS:64 complete chain identities, with F5 deck and E coefficient independently separated.')
print('PASS:12 empty-deck matches,8 fixed physical nodes; no presentation-kernel identification inferred.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))

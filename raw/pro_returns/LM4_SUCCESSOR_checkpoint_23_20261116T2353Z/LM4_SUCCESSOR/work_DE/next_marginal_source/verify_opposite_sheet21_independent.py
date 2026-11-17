#!/usr/bin/env python3
"""Independent semantic replay of the other64 actual L8 node boundaries."""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

H=Path(__file__).resolve().parent;ROOT=H.parents[1]
P=ROOT/'work_CE/next_symmetric_nodes'
fp=P/'full21_opposite_sheet_nodes.json'
d=json.loads(fp.read_text());paired=json.loads((P/'symmetric_paired_fox_data.json').read_text())
odd=json.loads((H/'odd_G_overlap.json').read_text());started=time.monotonic()

def red(w):
    ans=[]
    for s,x in w:
        if ans and ans[-1]==(-s,x):ans.pop()
        else:ans.append((s,x))
    return tuple(ans)
def fret(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x:ans.pop()
        else:ans.append(x)
    return tuple(ans)
def inv(w):return tuple(-x for x in w[::-1])
def sub(w,A):return fret(y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x])))
def add(c,k,n):
    c[k]+=n
    if not c[k]:del c[k]
ret={j:i+1 for i,j in enumerate(paired['retained_paired_indices'])}
beta={int(k):tuple(v) for k,v in paired['retained_involution'].items()}
def bet(t):return sub(t,beta)
one=((),(),())
def step(g,x):
    a,b,t=g;j=abs(x);s=1 if x>0 else -1
    if j in ret:return a,b,fret((*t,s*ret[j]))
    if j<12:return red((*a,(s,(t,j)))),b,t
    return a,red((*b,(s,(bet(t),j-10)))),t
def fox(w):
    c=defaultdict(int);g=one
    for x in w:
        new=step(g,x)
        add(c,(abs(x),g if x>0 else new),1 if x>0 else -1);g=new
    return dict(c),g
def boundary(c):
    out=defaultdict(int)
    for (row,g),n in c.items():add(out,step(g,row),n);add(out,g,-n)
    return dict(out)

def decode_R(w,D):
    ans=[]
    for x in w:
        r=D[str(abs(x))];head=tuple(r['retained_word']);slot=r['paired_slot']
        assert fret(head)==head and slot in (2,3,5,6,7,8,10,11)
        ans.append((1 if x>0 else -1,(head,slot)))
    assert red(ans)==tuple(ans)
    return tuple(ans)
def decode_g(x,D):
    t=tuple(x['retained_word']);assert fret(t)==t
    return decode_R(x['A_word'],D),decode_R(x['B_word'],D),t
def decode_rows(rows):
    c={}
    for r in rows:
        key=(r['row'],decode_g(r['G_coefficient'],d['common_R_basis']))
        assert key not in c and isinstance(r['coefficient'],int) and r['coefficient']
        c[key]=r['coefficient']
    return c

for name,h in d['input_sha256'].items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
pull={int(k):tuple(v) for k,v in next(x for x in paired['old_actions'] if x['index']==1)['based_pullback_paired'].items()}
nodes={(x['loop_index'],x['local_node_index']):x for x in paired['node_columns']}
oldcols={tuple(x['node']):x for x in odd['columns'] if x['layer']==1}
checks=[]
for col in d['columns']:
    ix=tuple(col['node_index']);word=sub(nodes[ix]['paired_relator'],pull)
    assert word==tuple(col['literal_F21_word'])==tuple(oldcols[ix]['paired_relator'])
    chain,end=fox(word);assert end==one and boundary(chain)=={}
    assert chain==decode_rows(col['full21_cycle'])
    drop={k:v for k,v in chain.items() if k[0] not in ret}
    assert drop==decode_rows(col['collapsed16_cycle'])
    # Reconstruct the entire audited2-chain boundary in semantic labels.
    want=defaultdict(int)
    for term in oldcols[ix]['terms']:
        row=term['row'];i=row['A_slot'];j=row['B_slot'];z=tuple(row['relative_retained_word'])
        a,b,t=decode_g(term['G_coefficient'],odd['common_R_basis']);n=term['coefficient']
        A=(t,i);B=(fret((*bet(t),*z)),j);tb=fret((*t,*bet(z)))
        add(want,(i,(a,b,t)),n)
        add(want,(i,(a,red((*b,(1,B))),t)),-n)
        add(want,(j+10,(red((*a,(1,A))),b,tb)),n)
        add(want,(j+10,(a,b,tb)),-n)
    assert drop==dict(want)
    checks.append({'node_index':ix,'letters':len(word),'full21_terms':len(chain),'collapsed16_terms':len(drop),
                   'literal_old1_pull':True,'all_boundary_coefficients':True,'entire_square_boundary':True})
assert len(checks)==len(nodes)==64
counts={'nodes':len(checks),'letters':sum(x['letters'] for x in checks),
        'full21_terms':sum(x['full21_terms'] for x in checks),'collapsed16_terms':sum(x['collapsed16_terms'] for x in checks)}
assert counts=={'nodes':64,'letters':11254,'full21_terms':7560,'collapsed16_terms':5788}
out={'input_sha256':hashlib.sha256(fp.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'method':'Semantic free-word letters (retained head,slot), without importing the producer or its numeric R indices.',
     'checks':checks,'counts':counts,'total_actual_L8_node_columns':128,
     'scope':'The audited old1-pull opposite sheet, not an added orbit sample. No kernel or kappa decision.',
     'elapsed_seconds':time.monotonic()-started}
(H/'opposite_sheet21_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS independent all64 literal odd pullbacks, all7560 full21 coefficients, all5788 forest projections and full square boundaries')
print('COUNTS',counts,'elapsed',round(out['elapsed_seconds'],3))

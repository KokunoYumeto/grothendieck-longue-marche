#!/usr/bin/env python3
"""The64 audited opposite-sheet node cycles in the full21 edge model.

This is the existing L8 second sheet, not an additional old-orbit sample.
Each literal word is rederived using the actual old1 pull and compared
with DE's audited full-G2-chain boundary before the certificate is saved.
"""
from pathlib import Path
from collections import defaultdict
import json, hashlib, time

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
DATA=P/'symmetric_paired_fox_data.json'
ODD=ROOT/'work_DE/next_marginal_source/odd_G_overlap.json'
data=json.loads(DATA.read_text());odd=json.loads(ODD.read_text())
retained={j:i+1 for i,j in enumerate(data['retained_paired_indices'])}
beta={int(k):v[0] for k,v in data['retained_involution'].items()}


def reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)


def inv(w):return tuple(-x for x in reversed(w))
def mul(a,b):return reduce((*a,*b))
def bet(w):return tuple((1 if x>0 else -1)*beta[abs(x)] for x in w)
def add(c,k,n):
    c[k]+=n
    if not c[k]:del c[k]


generators=[None];gen_index={}
def generator(head,slot):
    k=(tuple(head),slot)
    if k not in gen_index:
        gen_index[k]=len(generators);generators.append(k)
    return gen_index[k]


def right(g,letter):
    a,b,t=g;j=abs(letter);s=1 if letter>0 else -1
    if j in retained:return(a,b,mul(t,(s*retained[j],)))
    if j<12:return(mul(a,(s*generator(t,j),)),b,t)
    return(a,mul(b,(s*generator(bet(t),j-10),)),t)


def fox(w):
    one=((),(),());g=one;c=defaultdict(int)
    for x in w:
        if x>0:add(c,(x,g),1);g=right(g,x)
        else:g=right(g,x);add(c,(-x,g),-1)
    boundary=defaultdict(int)
    for (row,h),n in c.items():add(boundary,right(h,row),n);add(boundary,h,-n)
    want=defaultdict(int);add(want,g,1);add(want,one,-1)
    assert dict(boundary)==dict(want)
    return g,c


def substitute(w,images):
    out=[]
    for x in w:
        z=images[str(abs(x))]
        if x<0:z=inv(z)
        for y in z:
            if out and out[-1]==-y:out.pop()
            else:out.append(y)
    return tuple(out)


def packed(c):
    return [{'row':row,'G_coefficient':{'A_word':a,'B_word':b,'retained_word':t},
             'coefficient':n} for (row,(a,b,t)),n in sorted(c.items())]


started=time.monotonic()
DE_gens={int(k):generator(v['retained_word'],v['paired_slot'])
         for k,v in odd['common_R_basis'].items()}
def convert(w):return tuple((1 if x>0 else -1)*DE_gens[abs(x)] for x in w)


def square_boundary(terms):
    c=defaultdict(int)
    for term in terms:
        n=term['coefficient'];row=term['row'];h=term['G_coefficient']
        a,b,t=convert(h['A_word']),convert(h['B_word']),tuple(h['retained_word'])
        i,j,z=row['A_slot'],row['B_slot'],tuple(row['relative_retained_word'])
        agen=generator(t,i)
        bhead=mul(bet(t),z);bgen=generator(bhead,j)
        add(c,(i,(a,b,t)),n)
        add(c,(i,(a,mul(b,(bgen,)),t)),-n)
        bt=mul(t,bet(z))
        add(c,(j+10,(mul(a,(agen,)),b,bt)),n)
        add(c,(j+10,(a,b,bt)),-n)
    return c


pull=next(x for x in data['old_actions'] if x['index']==1)['based_pullback_paired']
odd_by_node={tuple(x['node']):x for x in odd['columns'] if x['layer']==1}
columns=[]
for node in data['node_columns']:
    idx=(node['loop_index'],node['local_node_index'])
    word=substitute(node['paired_relator'],pull)
    expected=odd_by_node[idx]
    assert word==tuple(expected['paired_relator']),('literal second-sheet word',idx)
    endpoint,chain=fox(word);assert endpoint==((),(),())
    collapsed={k:v for k,v in chain.items() if k[0] not in retained}
    assert collapsed==dict(square_boundary(expected['terms'])),('entire2-boundary',idx)
    columns.append({'node_index':idx,'sheet':1,'literal_F21_word':word,
                    'full21_cycle':packed(chain),'collapsed16_cycle':packed(collapsed),
                    'literal_old1_pull_verified':True,'full_boundary_zero':True,
                    'independent_full_G_square_boundary_equal':True})
assert len(columns)==64
out={'scope':__doc__,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in(DATA,ODD)},
 'sheet0_companion':'work_CE/next_symmetric_nodes/actual_full21_Fox.json:node_cycles',
 'operator':'actual old1 based pullback alpha_b^-1; chronological orientation unchanged',
 'common_R_basis':{str(i):{'retained_word':g,'paired_slot':j} for i,(g,j) in enumerate(generators[1:],1)},
 'columns':columns,'counts':{'opposite_sheet_columns':64,'total_block_columns':128,
 'input_letters':sum(len(x['literal_F21_word']) for x in columns),
 'full21_terms':sum(len(x['full21_cycle']) for x in columns),
 'collapsed16_terms':sum(len(x['collapsed16_cycle']) for x in columns)},
 'claims_excluded':['new orbit-depth sample','whole-orbit overlap or kappa decision'],
 'elapsed_seconds':time.monotonic()-started}
(P/'full21_opposite_sheet_nodes.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('PASS all64 literal actual old1-pull words, full21 boundaries, complete audited full-G2-chain boundaries')
print('COUNTS',out['counts']);print('DONE elapsed',round(out['elapsed_seconds'],3))

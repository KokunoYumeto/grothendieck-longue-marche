#!/usr/bin/env python3
"""Bounded exact F-image matching for all64 actual common node relators.

Each relator is normalized with its A-meridian first. Its physical mate
is fixed by the actual Mobius permutation, not by a word search. A
successful free conjugacy is refined to a full product-tree chain
identity with separate retained-F5 deck index and E coefficient.
Failure of a single-conjugate match implies no module nonmembership.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
path=P/'symmetric_paired_fox_data.json';raw=path.read_bytes();D=json.loads(raw)
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
def add(d,k,n):
    d[k]+=n
    if not d[k]:del d[k]
def peel(w):
    c=[];w=tuple(w)
    while len(w)>1 and w[0]==-w[-1]:c.append(w[0]);w=w[1:-1]
    return tuple(c),w
def conjugator(w,v):
    a,c=peel(w);b,d=peel(v)
    if len(c)!=len(d):return None
    for k in range(len(c)):
        if c[k:]+c[:k]==d:
            g=red(a+c[:k]+inv(b))
            assert red(g+tuple(v)+inv(g))==tuple(w)
            return g
    return None
F=mp(D['paired_involution']);beta=mp(D['retained_involution'])
ret=D['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
fill={j:((j,) if j in hm else ()) for j in range(1,22)}
fill5={j:((hm[j],) if j in hm else ()) for j in range(1,22)}
meta={int(i):dict(r,retained_word=tuple(r['retained_word'])) for i,r in D['finite_used_common_R_basis'].items()}
idx={(r['retained_word'],r['paired_slot']):i for i,r in meta.items()}
def bid(g,i):
    if (g,i) not in idx:
        j=max(meta,default=0)+1;idx[g,i]=j;meta[j]={'retained_word':g,'paired_slot':i}
    return idx[g,i]
def rw(w):
    g=();r=[]
    for x in w:
        i=abs(x);sgn=1 if x>0 else -1
        if i in hm:g=red(g+(sgn*hm[i],))
        else:
            a=i<12;n=bid(g if a else sub(g,beta),i if a else i-10)
            r.append(sgn*(2*n-1 if a else 2*n))
    assert not g
    return red(r)
def isA(x):return abs(x)%2==1
def rid(x):return (abs(x)+1)//2
def proj(w,a):return red((1 if x>0 else -1)*rid(x) for x in w if isA(x)==a)
def chain(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x)
        if isA(x):
            aa=red(a+(y,));av=a if y>0 else aa;bp=()
            for z in b:
                bn=red(bp+(z,));bv=bp if z>0 else bn
                add(out,(av,bv,abs(y),abs(z)),-(1 if y>0 else -1)*(1 if z>0 else -1));bp=bn
            a=aa
        else:b=red(b+(y,))
    assert not a and not b
    return dict(out)
def edge_cycle(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x);sgn=1 if y>0 else -1
        if isA(x):
            aa=red(a+(y,));add(out,('A',a if y>0 else aa,b,abs(y)),sgn);a=aa
        else:
            bb=red(b+(y,));add(out,('B',a,b if y>0 else bb,abs(y)),sgn);b=bb
    assert not a and not b
    return dict(out)
def boundary(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        add(out,('A',a,b,i),n);add(out,('A',a,red(b+(j,)),i),-n)
        add(out,('B',red(a+(i,)),b,j),n);add(out,('B',a,b,j),-n)
    return dict(out)
def enc(c):return [{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':n} for (a,b,i,j),n in sorted(c.items())]
def dec(c):return {(tuple(r['A_vertex']),tuple(r['B_vertex']),r['A_generator'],r['B_generator']):r['coefficient'] for r in c}
def physicalF(i):
    assert 3<=i<=18
    return i+8 if i<11 else i-8
def key(r):return r['loop_index'],r['local_node_index']
def orientation(r):return 1 if r['physical_labels'][0]<11 else -1
def arelator(r):
    w=tuple(r['paired_relator']);return w if orientation(r)>0 else inv(w)
lookup={(r['loop_index'],frozenset(r['physical_labels'])):r for r in D['node_columns']}
rows=[];started=time.monotonic()
for node in D['node_columns']:
    mate=lookup[node['loop_index'],frozenset(physicalF(i) for i in node['physical_labels'])]
    r=arelator(node);m=arelator(mate);fr=sub(r,F)
    g=conjugator(fr,inv(m))
    lc=chain(rw(fr));assert boundary(lc)==edge_cycle(rw(fr))
    sc=dec(node['fox_cells']);eps=orientation(node)
    assert lc=={(b,a,j,i):-eps*n for (a,b,i,j),n in sc.items()}
    rec={'node_index':key(node),'physical_labels':node['physical_labels'],
         'physical_F_mate_index':key(mate),'physical_F_mate_labels':mate['physical_labels'],
         'A_first_orientation_signs':[orientation(node),orientation(mate)],
         'exact_single_conjugate_match':g is not None,
         'F_normalized_relator':fr,'F_normalized_column':enc(lc)}
    if g is not None:
        deck=sub(g,fill);n=red(g+inv(deck));assert not sub(n,fill5)
        nk=rw(n);a,b=proj(nk,True),proj(nk,False)
        dm=red(deck+m+inv(deck));mc=chain(rw(dm))
        assert boundary(mc)==edge_cycle(rw(dm))
        rhs={(red(a+u),red(b+v),i,j):-coef for (u,v,i,j),coef in mc.items()}
        assert lc==rhs
        rec.update({'conjugator_F21':g,'retained_deck_F21':deck,
            'retained_deck_F5':sub(deck,fill5),'kernel_part_F21':n,
            'E_coefficient':{'A_word':a,'B_word':b},
            'deck_mate_normalized_column':enc(mc),
            'word_identity':'F(r_A_nu)=g*r_A_mate^-1*g^-1',
            'chain_identity':'F(C_A_nu)=-(A_word,B_word)*C_A_(retained_deck.mate)',
            'fixed_physical_node':key(node)==key(mate),
            'pure_E_coefficient':not deck})
    rows.append(rec)
    print('PASS F-image/chain',key(node),'mate',key(mate),'single-conjugate',g is not None,
          'deck',rec.get('retained_deck_F5'),'g length',len(g) if g is not None else None,flush=True)
out={'scope':__doc__,'input_sha256':hashlib.sha256(raw).hexdigest(),
    'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'common_R_basis':meta,'rows':rows,
    'matched_count':sum(r['exact_single_conjugate_match'] for r in rows),
    'pure_E_count':sum(r.get('pure_E_coefficient',False) for r in rows),
    'fixed_physical_count':sum(key(n)==key(lookup[n['loop_index'],frozenset(physicalF(i) for i in n['physical_labels'])]) for n in D['node_columns']),
    'claims_excluded':['nonmembership from failed single-conjugate matches','equivariant kernel identification without full index comparison','nonzero kappa','I=R'],
    'elapsed_seconds':time.monotonic()-started}
(P/'symmetric_F_node_matching.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all64 exact F chains;',out['matched_count'],'literal physical-mate conjugacies;',out['pure_E_count'],'with zero retained deck; elapsed',round(out['elapsed_seconds'],3),flush=True)

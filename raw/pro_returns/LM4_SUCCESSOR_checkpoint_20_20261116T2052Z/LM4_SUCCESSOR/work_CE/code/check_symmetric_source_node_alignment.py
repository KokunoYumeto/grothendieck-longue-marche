#!/usr/bin/env python3
"""Eight actual source diagonals, Tate defects and exact node conjugacies."""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_full_source_data.json',P/'symmetric_paired_fox_data.json']
raw=[p.read_bytes() for p in paths];source,paired=[json.loads(r) for r in raw]
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
F=mp(paired['paired_involution']);beta=mp(paired['retained_involution'])
ret=paired['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
meta={int(i):dict(r,retained_word=tuple(r['retained_word'])) for i,r in paired['finite_used_common_R_basis'].items()}
idx={(r['retained_word'],r['paired_slot']):i for i,r in meta.items()}
def bid(g,i):
    key=(g,i)
    if key not in idx:
        j=max(meta,default=0)+1;idx[key]=j;meta[j]={'retained_word':g,'paired_slot':i}
    return idx[key]
def rw(w):
    g=();out=[]
    for x in w:
        i=abs(x);sgn=1 if x>0 else -1
        if i in hm:g=red(g+(sgn*hm[i],))
        else:
            isA=i<12;j=i if isA else i-10
            n=bid(g if isA else sub(g,beta),j)
            out.append(sgn*(2*n-1 if isA else 2*n))
    assert not g
    return red(out)
def isA(x):return abs(x)%2==1
def rid(x):return (abs(x)+1)//2
def proj(w,A):return red((1 if x>0 else -1)*rid(x) for x in w if isA(x)==A)
def cells(w):
    a=b=();out=defaultdict(int)
    for x in w:
        y=(1 if x>0 else -1)*rid(x)
        if isA(x):
            an=red(a+(y,));av=a if y>0 else an;bp=()
            for z in b:
                bn=red(bp+(z,));bv=bp if z>0 else bn
                add(out,(av,bv,abs(y),abs(z)),-(1 if y>0 else -1)*(1 if z>0 else -1));bp=bn
            a=an
        else:b=red(b+(y,))
    assert not a and not b
    return dict(out)
def tensor(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        ai=red(a+(i,));bj=red(b+(j,))
        for u,v,coef in [(ai,bj,n),(ai,b,-n),(a,bj,-n),(a,b,n)]:
            if u and v:add(out,(u,v),coef)
    return dict(out)
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
old_b_inv=mp(paired['old_actions'][1]['based_pullback_paired'])
rows=[];started=time.monotonic()
for seed in source['source_peripheral_generators']:
    h=tuple(seed['positive_source_word_F21']);r=rw(h)
    a,b=proj(r,True),proj(r,False);assert a==b and a
    delta=red(inv(h)+sub(h,F));dr=rw(delta)
    assert not proj(dr,True) and not proj(dr,False)
    c=cells(dr);t=tensor(c)
    assert t=={(v,u):n for (u,v),n in t.items()}
    diag={u:n%2 for (u,v),n in t.items() if u==v and n%2}
    assert diag=={inv(a):1},('wrong right-defect Tate value',seed['sheet'],seed['critical_index'],diag,a)
    k=red(sub(h,F)+inv(h));matches=[]
    for node in paired['node_columns']:
        if node['loop_index']!=seed['critical_index']:continue
        v=tuple(node['paired_relator'])
        if seed['sheet']:v=sub(v,old_b_inv)
        for sign in (1,-1):
            vv=v if sign==1 else inv(v);g=conjugator(k,vv)
            if g is not None:matches.append({'original_node_index':[node['loop_index'],node['local_node_index']],
                'actual_Q_translate':[2] if seed['sheet'] else [],'translation_operator':'geometric pullback',
                'node_sign':sign,'conjugator_F21':g,'exact_equation':'k=g*(translated_node_relator)^sign*g^-1'})
    rows.append({'sheet':seed['sheet'],'critical_index':seed['critical_index'],
        'actual_source_word_R':a,'right_defect_F21':delta,
        'right_defect_kernel_word':dr,
        'fox_cells':[{'A_vertex':u,'B_vertex':v,'A_generator':i,'B_generator':j,'coefficient':n}
                     for (u,v,i,j),n in sorted(c.items())],
        'tate_diagonal_word':inv(a),'tate_value':'r^-1-1',
        'exact_matched_node_conjugacies':matches})
    print('PASS actual source diagonal/Tate defect',seed['sheet'],seed['critical_index'],'R length',len(a),'exact local node matches',len(matches),flush=True)
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'common_R_basis':meta,'source_rows':rows,'elapsed_seconds':time.monotonic()-started,
 'claims_excluded':['full translated relation submodule','syzygy vanishing','I=R']}
(P/'symmetric_source_node_alignment.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all8 exact source diagonals and right-defect Tate identities; elapsed',round(out['elapsed_seconds'],3),flush=True)

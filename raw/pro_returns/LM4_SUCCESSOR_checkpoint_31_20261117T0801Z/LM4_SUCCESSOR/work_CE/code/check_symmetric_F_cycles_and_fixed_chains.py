#!/usr/bin/env python3
"""Exact double-F cycles and four intrinsic fixed-cell anti-chains.

This checks the finite common-marking coefficient/index data directly.
It does not identify infinite relation-kernel presentations. The four
anti-chains are evaluated intrinsically in the actual submodule Lbar.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'symmetric_F_node_matching.json',P/'symmetric_paired_fox_data.json',P/'symmetric_source_node_alignment.json']
raw=[p.read_bytes() for p in paths];match,paired,source=[json.loads(r) for r in raw]
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
fill5={j:((hm[j],) if j in hm else ()) for j in range(1,22)}
meta={int(i):dict(r,retained_word=tuple(r['retained_word'])) for i,r in match['common_R_basis'].items()}
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
def proj(w,a):return red((1 if x>0 else -1)*((abs(x)+1)//2) for x in w if (abs(x)%2==1)==a)
def dec(c):return {(tuple(r['A_vertex']),tuple(r['B_vertex']),r['A_generator'],r['B_generator']):r['coefficient'] for r in c}
def enc(c):return [{'A_vertex':a,'B_vertex':b,'A_generator':i,'B_generator':j,'coefficient':n} for (a,b,i,j),n in sorted(c.items())]
def diagonal(c):
    out=defaultdict(int)
    for (a,b,i,j),n in c.items():
        if a==b and i==j:
            add(out,red(a+(i,)),n);add(out,a,-n)
    return {w:n%2 for w,n in out.items() if n%2}
srcmeta={int(i):(tuple(r['retained_word']),r['paired_slot']) for i,r in source['common_R_basis'].items()}
def source_word(w):return red((1 if x>0 else -1)*bid(*srcmeta[abs(x)]) for x in w)
seeds=[dict(r,R=source_word(r['actual_source_word_R'])) for r in source['source_rows']]
lookup={tuple(r['node_index']):r for r in match['rows']}
nodes={(r['loop_index'],r['local_node_index']):r for r in paired['node_columns']}
cycles=[];fixed=[];started=time.monotonic()
for r in match['rows']:
    key=tuple(r['node_index']);mu=lookup[tuple(r['physical_F_mate_index'])]
    g=tuple(r['conjugator_F21']);gm=tuple(mu['conjugator_F21'])
    z=red(sub(g,F)+gm)
    nr=nodes[key];rr=tuple(nr['paired_relator'])
    if r['A_first_orientation_signs'][0]<0:rr=inv(rr)
    assert red(z+rr+inv(z))==rr
    assert not sub(z,fill5)
    zw=rw(z);assert not proj(zw,True) and not proj(zw,False)
    t=tuple(r['retained_deck_F5']);tm=tuple(mu['retained_deck_F5'])
    assert not red(sub(t,beta)+tm)
    cycles.append({'node_index':key,'mate_index':r['physical_F_mate_index'],
        'double_F_conjugator':z,'retained_head_zero':True,'E_projection_identity':True,
        'exact_commutator_kernel_word':zw,
        'claim':'The finite common-cell head and E coefficient return to identity under double F.'})
    if r['fixed_physical_node'] and r['pure_E_coefficient']:
        a=tuple(r['E_coefficient']['A_word']);b=tuple(r['E_coefficient']['B_word'])
        assert b==inv(a)
        # e=(1,a^-1) satisfies F(e)*coefficient=e.
        original=dec(nr['fox_cells']);eps=r['A_first_orientation_signs'][0]
        c={(u,red(inv(a)+v),i,j):eps*n for (u,v,i,j),n in original.items()}
        assert c=={(v,u,j,i):n for (u,v,i,j),n in c.items()}
        psi=diagonal(c);witnesses=[]
        for s in seeds:
            for sign in (1,-1):
                u=s['R'] if sign>0 else inv(s['R'])
                expected={():1,u:1} if u else {}
                if psi==expected:witnesses.append({'source_sheet':s['sheet'],'critical_index':s['critical_index'],
                    'source_word_R':s['R'],'power':sign,'left_coefficient_R':[],
                    'exact_identity':'psi=source_word^power-1'})
        assert witnesses,('anti-chain diagonal lacks actual source certificate',key,psi)
        fixed.append({'node_index':key,'E_half_translation':{'A_word':[],'B_word':inv(a)},
            'actual_anti_chain':enc(c),
            'diagonal_group_ring':[{'word':w,'coefficient_F2':n} for w,n in sorted(psi.items())],
            'source_left_ideal_zero_witnesses':witnesses})
        print('PASS intrinsic fixed-cell anti-chain',key,'cells',len(c),'source witnesses',[(w['source_sheet'],w['critical_index'],w['power']) for w in witnesses],flush=True)
assert len(cycles)==64 and len(fixed)==4
out={'scope':__doc__,'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(r).hexdigest() for p,r in zip(paths,raw)},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'common_R_basis':meta,'double_F_cycles':cycles,'fixed_cell_anti_chains':fixed,
 'claims_excluded':['full equivariant kernel identification','exhaustion of intrinsic anti-chains','nonzero kappa','I=R'],
 'elapsed_seconds':time.monotonic()-started}
(P/'symmetric_F_cycles_and_fixed_chains.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all64 exact double-F cycles and four actual E-weighted anti-chains, all zero modulo the witnessed source ideal; elapsed',round(out['elapsed_seconds'],3),flush=True)

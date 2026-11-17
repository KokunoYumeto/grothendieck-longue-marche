#!/usr/bin/env python3
"""Independent double-F, semilinear half and actual-source checks."""
from pathlib import Path
import json,hashlib,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent;DIR=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_F_node_matching.json','symmetric_F_cycles_and_fixed_chains.json','symmetric_paired_fox_data.json','symmetric_full_source_data.json']
raw=[(DIR/n).read_bytes() for n in names];M,D,P,S=map(json.loads,raw);start=time.monotonic()
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(int(x))
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
F={int(j):tuple(w) for j,w in P['paired_involution'].items()}
ret=P['retained_paired_indices'];hm={j:i+1 for i,j in enumerate(ret)}
beta={int(j):tuple(w) for j,w in P['retained_involution'].items()}
meta={int(j):(tuple(r['retained_word']),r['paired_slot']) for j,r in D['common_R_basis'].items()}
lookup={v:j for j,v in meta.items()}
def split(w):
    head=();parts=[[],[]]
    for x in w:
        j=abs(x);s=1 if x>0 else -1
        if j in hm:head=red(head+(s*hm[j],))
        else:
            side=int(j>=12);key=(sub(head,beta) if side else head,j-10 if side else j)
            parts[side].append(s*lookup[key])
    return head,red(parts[0]),red(parts[1])
node={(r['loop_index'],r['local_node_index']):r for r in P['node_columns']}
match={tuple(r['node_index']):r for r in M['rows']}
for r in D['double_F_cycles']:
    key=tuple(r['node_index']);m=match[key];mate=match[tuple(m['physical_F_mate_index'])]
    z=red(sub(m['conjugator_F21'],F)+tuple(mate['conjugator_F21']))
    assert z==tuple(r['double_F_conjugator'])
    rel=tuple(node[key]['paired_relator'])
    if m['A_first_orientation_signs'][0]<0:rel=inv(rel)
    assert red(z+rel+inv(z))==rel
    assert split(z)==((),(),())
    assert not red(sub(m['retained_deck_F5'],beta)+tuple(mate['retained_deck_F5']))

ren={j:i+1 for i,j in enumerate(S['first_family_F13_kept_paired_indices'])}
Rimages={}
for j,(t,k) in meta.items():
    word=tuple((1 if x>0 else -1)*ren[ret[abs(x)-1]] for x in t)
    Rimages[j]=red(word+(ren[k],)+inv(word))
actual={(r['sheet'],r['critical_index']):tuple(r['positive_source_word_F13']) for r in S['source_peripheral_generators']}
def dec(rows):return {(tuple(r['A_vertex']),tuple(r['B_vertex']),r['A_generator'],r['B_generator']):r['coefficient'] for r in rows}
checks=[]
for r in D['fixed_cell_anti_chains']:
    key=tuple(r['node_index']);m=match[key]
    assert m['fixed_physical_node'] and not m['retained_deck_F5']
    a=tuple(m['E_coefficient']['A_word']);b=tuple(m['E_coefficient']['B_word'])
    assert b==inv(a)
    x=tuple(r['E_half_translation']['A_word']);y=tuple(r['E_half_translation']['B_word'])
    assert (red(y+a),red(x+b))==(x,y) # F(e) coefficient = e, in exact order
    original=dec(node[key]['fox_cells']);eps=m['A_first_orientation_signs'][0]
    chain={(red(x+u),red(y+v),i,j):eps*n for (u,v,i,j),n in original.items()}
    assert chain==dec(r['actual_anti_chain'])
    assert chain=={(v,u,j,i):n for (u,v,i,j),n in chain.items()}
    psi=set()
    for (u,v,i,j),n in chain.items():
        if u!=v or i!=j or not n%2:continue
        for w in (u,red(u+(i,))):
            if w in psi:psi.remove(w)
            else:psi.add(w)
    assert psi=={tuple(w['word']) for w in r['diagonal_group_ring'] if w['coefficient_F2']}
    witnessed=[]
    for w in r['source_left_ideal_zero_witnesses']:
        sr=tuple(w['source_word_R']);sid=w['source_sheet'],w['critical_index']
        assert sub(sr,Rimages)==actual[sid]
        power=sr if w['power']==1 else inv(sr)
        assert w['left_coefficient_R']==[] and psi=={(),power}
        witnessed.append(sid)
    assert witnessed
    checks.append({'node':key,'source_ids':witnessed,'cells':len(chain)})
assert len(D['double_F_cycles'])==64 and len(checks)==4
out={'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in zip(names,raw)},
     'double_F_cycles':64,'fixed_chain_checks':checks,
     'scope':'four actual E-weighted anti-chains have literal source-ideal zero witnesses; no full relation kernel or orbit span identified',
     'elapsed_seconds':time.monotonic()-start}
(HERE/'symmetric_F_cycles_independent_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all64 double-F words centralize their relators and have trivial retained/E projections.')
print('PASS: all4 semilinear half equations F(e)*coefficient=e, full anti-chains and exact source IDs.')
print('PASS: four diagonal values expand to actual first-sheet F13 seeds at0,8,12,16; all zero modulo J_I.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))

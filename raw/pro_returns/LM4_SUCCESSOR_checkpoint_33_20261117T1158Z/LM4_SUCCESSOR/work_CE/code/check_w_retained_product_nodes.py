#!/usr/bin/env python3
"""Actual companion nodes remove the two diagonal-triple source corrections."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
A=json.loads((P/'w_source_adapted_basis.json').read_text())
D=json.loads((P/'w_positive_negative_transport.json').read_text())
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def inv(w):return[-x for x in w[::-1]]
def sub(w,a):return red(y for x in w for y in(a[str(abs(x))] if x>0 else inv(a[str(abs(x))])))
def cj(h,w):return red(h+w+inv(h))
def comm(x,y):return red(x+y+inv(x)+inv(y))
rows=[]
for action_index,source_index,triple_index in [(2,17,1),(3,19,2)]:
    p=A['all_source_words_in_new'][str(source_index)]
    gamma=A['actions_in_new'][str(action_index)]
    inverse=A['inverse_actions_in_new'][str(action_index)]
    h=[10]+inv(p)
    for w in ([10],p):
        assert sub(w,gamma)==cj(h,w)
        assert sub(w,inverse)==cj(inv(h),w)
    assert sub(p,gamma)==cj([10],p)
    v=comm([10],inv(p))
    assert v==red(sub(inv(p),gamma)+p)
    triple=next(r for r in D['positive_triples'] if r['index']==triple_index)
    K=triple['boundary_word']
    assert v==triple['correction_before_boundary']
    for w in triple['normalized_triple'].values():
        assert cj(inv(v),sub(w,gamma))==cj(K,w)
        assert sub(cj(v,w),inverse)==cj(inv(K),w)
    rows.append({'action_index':action_index,'source_product_index':source_index,
                 'product':p,'companion_pair_inner':h,'correction':v,
                 'corrected_source_lift':'pminus^-1 g_i pminus',
                 'triple_boundary':K,'normalized_triple':triple['normalized_triple']})
first=rows[0]['normalized_triple']
assert first['6']==[11]
assert first['2']==cj([12],[-2])
assert first['9']==inv(A['all_source_words_in_new']['19'])
print('PASS both actual companion nodes and inverses on a and pminus.')
print('PASS corrections [a,pminus^-1]=gamma(pminus^-1)*pminus are literal source commutators.')
print('PASS both corrected triple actions and inverses; source lift is pminus^-1 g_i pminus.')
print('PASS positive1 deleted core is b c1^-1 b^-1 and retained core is inverse source19.')
print('Scope: positive1 gives a whole mixed d/product deleted-kernel image in J_c.')
print('No membership of b c2^-1 b^-1 in J_c is inferred for positive2.')
(ROOT/'work_CE/w_retained_product_nodes_certificate.json').write_text(json.dumps(
    {'description':__doc__,'status':'PASS','rows':rows},indent=2)+'\n')

#!/usr/bin/env python3
"""Exact retained-node inputs for the whole four-product diagonal kernel."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
A=json.loads((P/'w_source_adapted_basis.json').read_text())
N=json.loads((P/'w_positive_negative_transport.json').read_text())
L=json.loads((P/'w_local_markings.json').read_text())
def red(w):
    o=[]
    for x in w:
        if o and o[-1]==-x:o.pop()
        else:o.append(x)
    return o
def inv(w):return[-x for x in w[::-1]]
def sub(w,a):return red(y for x in w for y in(a[str(abs(x))] if x>0 else inv(a[str(abs(x))])))
def cj(h,w):return red(h+w+inv(h))
def comm(x,y):return red(x+y+inv(x)+inv(y))
def peel(w):
    h=[]
    while len(w)>1:
        assert w[0]==-w[-1]
        h.append(w[0]);w=w[1:-1]
    return h,w

b=[12];a=[10];d=[11];C=cj(b,[-2])
products=[A['all_source_words_in_new'][str(i)] for i in (17,19,21,23)]
Q4=cj([-10],products[3])
gamma5=A['actions_in_new']['5']
gamma5inv=A['inverse_actions_in_new']['5']
h=inv(products[3])+a
for w in (a,products[3]):
    assert sub(w,gamma5)==cj(h,w)
    assert sub(w,gamma5inv)==cj(inv(h),w)
assert sub(products[3],gamma5inv)==Q4

# Reconstruct the three filled-node relations directly from their common
# transported actual peripherals, not merely the simplified relation table.
expected={3:inv(products[0]),4:cj(C,inv(products[2])),2:inv(Q4)}
checks=[]
for index,q in expected.items():
    row=next(r for r in L['all_local_markings'] if r['name']==f'filled_negative_{index}')
    per={int(k):sub(w,A['initial_basis_in_new'])
         for k,w in row['transported_peripheral_words_by_label'].items()}
    hd,core=peel(per[6]);assert core==d
    product_label=7+(2*index)%5
    actual_q=cj(inv(hd),per[product_label])
    assert actual_q==q
    actual_rel=comm(per[6],per[product_label])
    assert actual_rel==cj(hd,comm(d,q))
    stored=next(r for r in N['negative_nodes'] if r['index']==index)
    assert stored['simplified_commuting_word']==q
    checks.append({'filled_index':index,'actual_conjugator':hd,
                   'commuting_word':q,'relation':comm(d,q)})

# The positive1 triple and both corrected actions provide the whole
# initial deleted and retained kernels; repeat its exact word identities.
triple=next(r for r in N['positive_triples'] if r['index']==1)
assert triple['normalized_triple']['6']==d
assert triple['normalized_triple']['2']==C
assert triple['normalized_triple']['9']==inv(products[1])
v=comm(a,inv(products[0]))
K=triple['boundary_word']
gamma2=A['actions_in_new']['2'];gamma2inv=A['inverse_actions_in_new']['2']
for w in triple['normalized_triple'].values():
    assert cj(inv(v),sub(w,gamma2))==cj(K,w)
    assert sub(cj(v,w),gamma2inv)==cj(inv(K),w)
assert v==red(sub(inv(products[0]),gamma2)+products[0])

print('PASS actual positive4 companion pair and inverse; Q4=gamma5^-1(P4) is a source word.')
print('PASS all3 filled-node commuting relations reconstructed from actual transported peripherals.')
print('PASS positive1 corrected source triple and inverse on d,C,P2^-1.')
print('Whole-kernel consequence uses the separately written exponent-kernel lemma, not sampled conjugates.')
print('Scope: normal closure of C in <d,C,P1,P2,P3,Q4> lies in J_c; no whole-J_c normality.')
(ROOT/'work_CE/w_coupled_diagonal_products_certificate.json').write_text(json.dumps({
    'description':__doc__,'status':'PASS','C':C,'products':products,'Q4':Q4,
    'actual_filled_node_checks':checks,'positive1_boundary':K,
    'positive1_source_correction':v},indent=2)+'\n')

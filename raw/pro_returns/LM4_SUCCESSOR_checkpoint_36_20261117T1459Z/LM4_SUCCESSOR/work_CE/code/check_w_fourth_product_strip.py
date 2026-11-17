#!/usr/bin/env python3
"""Independent literal verification of the fourth corrected actual b-node."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
P = ROOT/'work_DE/next_marginal_source'
A = json.loads((P/'w_source_adapted_basis.json').read_text())
D = json.loads((P/'w_fourth_strip_correction.json').read_text())

def red(word):
    out=[]
    for x in word:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out
def inv(word): return [-x for x in word[::-1]]
def sub(word, action):
    return red(y for x in word for y in
               (action[str(abs(x))] if x>0 else inv(action[str(abs(x))])))
def cj(h, word): return red(h+word+inv(h))

# Reconstruct every returned source generator from the independent data;
# do not import the weighted-fold producer or its evaluator.
rows=[]
source_rows=[]
for r in D['source_generators']:
    j=r['source_index']
    w=A['all_source_words_in_new'][str(j)]
    sw=[j-10]                 # thirteen extra source meridians: 1,...,13
    if r['operator'] is not None:
        i,kind=r['operator']
        w=sub(w,A[kind][str(i)])
        g=14+i               # six actual old source lifts: 14,...,19
        if kind=='inverse_actions_in_new':g=-g
        sw=[g]+sw+[-g]
    assert w==r['word']
    rows.append(w)
    source_rows.append(sw)
word=D['exact_source_expression']
v=sub(word,{str(i+1):w for i,w in enumerate(rows)})
assert v==D['correction']
source_expression=sub(word,{str(i+1):w for i,w in enumerate(source_rows)})
filled=red(x for x in source_expression if abs(x) not in {2,3,4,5,16,17,18,19})
assert filled==[]

C=D['normalized_deleted_core']
b=[12]
T=[12,10,11,12]
h=[-5,-4,-1]
assert C==cj(h+T,[-3])
inside=sub([-7,-3,7],A['inverse_actions_in_new']['1'])
assert inside==cj(T,[-3])
assert C==cj(h,inside)
K=red(C+b)
assert K==D['local_pair_boundary']
gamma=A['actions_in_new']['4']
gamma_inv=A['inverse_actions_in_new']['4']
for w in (b,C):
    assert sub(w,gamma)==cj(v+K,w)
    assert cj(inv(v),sub(w,gamma))==cj(K,w)
    assert sub(cj(v,w),gamma_inv)==cj(inv(K),w)

# Literal Nielsen replacement c2 -> hT c2^-1 (hT)^-1.
assert 3 not in [abs(x) for x in h+T]
phi={str(i):[i] for i in range(1,13)}
phi['3']=C
psi={str(i):[i] for i in range(1,13)}
psi['3']=cj(inv(h+T),[-3])
for i in range(1,13):
    assert sub(phi[str(i)],psi)==[i]
    assert sub(psi[str(i)],phi)==[i]

print('PASS all169 listed actual source generators independently reconstructed.')
print('PASS exact16-factor correction expression; its full source word dies under both-family filling.')
print('PASS c2star is an explicit source conjugate of the inverse actual w1 image of p2^-1 c2^-1 p2.')
print('PASS corrected positive3 action and inverse restrict to Inn(c2star b) and its inverse.')
print('PASS all24 compositions for the deleted-generator Nielsen replacement.')
print('Conclusion: the whole b-strip of c2star lies in actual J_c; c2 itself is not substituted silently.')
out={'description':__doc__,'status':'PASS','correction':v,
     'source_expression_19_basis':source_expression,'both_family_fill':filled,
     'c2star':C,'source_kernel_witness_inside':inside,'normalizing_source_word':h,
     'corrected_pair_inner':K,'replacement_inverse':psi['3'],
     'input_sha256':{name:hashlib.sha256((P/name).read_bytes()).hexdigest()
                     for name in ['w_source_adapted_basis.json','w_fourth_strip_correction.json']},
     'scope':'Four deleted Nielsen generators have whole b-kernels. No whole-J_c normality inferred.'}
(ROOT/'work_CE/w_fourth_product_strip_certificate.json').write_text(json.dumps(out,indent=2)+'\n')

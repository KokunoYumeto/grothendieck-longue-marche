#!/usr/bin/env python3
"""Two actual product-one strips and exact limits of proposed propagation."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
A=json.loads((P/'w_source_adapted_basis.json').read_text())
L=json.loads((P/'w_local_markings.json').read_text())
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return r
def inv(w):return[-x for x in w[::-1]]
def sub(w,a):return red(y for x in w for y in(a[abs(x)] if x>0 else inv(a[abs(x)])))
def conj(a,w):return red(a+w+inv(a))
def mp(a):return{int(i):w for i,w in a.items()}
def peel(w):
    h=[]
    while len(w)>1 and w[0]==-w[-1]:h.append(w[0]);w=w[1:-1]
    return h,w
def ab(w):
    v=[0]*12
    for x in w:v[abs(x)-1]+=1 if x>0 else -1
    return v

# Adapted coordinates: z,c1,c2,c3,c4,p1,p2,p3,p4,a,d,b.
alpha1=mp(A['actions_in_new']['5'])
alpha4=mp(A['actions_in_new']['2'])
for i in (2,12):assert alpha1[i]==conj([12,-2],[i])
for i in (5,12):assert alpha4[i]==conj([-5,12],[i])
print('PASS actual positive4 restricts on<b,c1> to Inn(b c1^-1).')
print('PASS actual positive1 restricts on<b,c4> to Inn(c4^-1 b).')
table=[
 ('actions_in_new','1',[]),('inverse_actions_in_new','1',[]),
 ('actions_in_new','2',[-5]),('inverse_actions_in_new','2',[-12,5,12]),
 ('actions_in_new','5',[12,-2,-12]),('inverse_actions_in_new','5',[2])]
for kind,index,k in table:
    assert A[kind][index]['12']==conj(k,[12])
    assert all(abs(x) in (2,5,12) for x in k) and sum((1 if x>0 else -1) for x in k if abs(x)==12)==0
print('PASS all6 actual b-conjugator entries, including inverses, lie in the initial b-kernel on<c1,c4,b>.')

# The full w=-1 retained node, without unbased simplification.
row=next(x for x in L['all_local_markings'] if x['name']=='filled_negative_0')
to_new=mp(A['initial_basis_in_new'])
d=sub(row['transported_peripheral_words_by_label']['6'],to_new)
b=sub(row['transported_peripheral_words_by_label']['7'],to_new)
hd,cd=peel(d);hb,cb=peel(b)
assert cd==[11] and cb==[12]
h=red(inv(hd)+hb)
assert h==[-11,-10,-12,1,4,5]
M=[1,4,5]
q0=conj([-10,-12]+M,[12])
assert conj(h,[12])==conj([-11],q0)
print('PASS actual negative1 node gives [d,q0]=1, q0=(ba)^-1(z c3 c4)b(z c3 c4)^-1(ba), not[d,b].')

zero=mp(A['actions_in_new']['0'])
h0,core=peel(zero[12]);assert core==[12]
assert h0==[12,2,3,-12,-11,-10,-12,1,4,5]
for w in A['all_source_words_in_new'].values():assert ab(w)[9:]==[0,0,0]
checks=0
for typ in ('actions_in_new','inverse_actions_in_new'):
    for action in A[typ].values():
        for i,w in mp(action).items():
            v=[0]*12;v[i-1]=1;assert ab(w)==v;checks+=1
assert ab(h0)[9:]==[-1,-1,-1]
print('PASS all source crossings have zero a,d,b characters; all264 action images preserve fiber abelianization.')
print('PASS h0 has a,d,b coordinates(-1,-1,-1); no h0 b^n can be a source-image element.')

out={'description':__doc__,'first_strip_action_index':5,'first_strip_conjugator':[12,-2],
 'fourth_strip_action_index':2,'fourth_strip_conjugator':[-5,12],
 'valid_stage_conjugator_table':table,
 'negative_one_relative_conjugator':h,'negative_one_q0':q0,
 'zero_b_conjugator':h0,'zero_b_conjugator_abelianization':ab(h0),
 'abelian_action_checks':checks,
 'scope':'Actual two-generator kernel images only. No whole-J b-normality. The source-membership obstruction is a character test for a specific proposed conjugator, not a finite separator of the ambient kernel.'}
(ROOT/'work_CE/w_normalizer_limitations_certificate.json').write_text(json.dumps(out,indent=2)+'\n')

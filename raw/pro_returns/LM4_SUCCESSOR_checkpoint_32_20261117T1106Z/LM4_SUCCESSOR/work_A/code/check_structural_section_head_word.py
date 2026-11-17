#!/usr/bin/env python3
"""Independent actual [6,2,-6,-2] section-head certificate.

Uses both the head cocycle and literal F21 substitutions. It retains the
returned source operator and correction. No full Fox2-chain is expanded.
"""
from pathlib import Path
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/symmetric_paired_fox_data.json',
       ROOT/'work_CE/next_symmetric_nodes/symmetric_full_source_data.json',
       ROOT/'work_A/old_base_augmented_row_action.json',
       ROOT/'records/old0_retained_incidence18.json']
raw=[p.read_bytes() for p in paths];D,S,H,I=map(json.loads,raw)
started=time.monotonic()
def red(w):
    a=[]
    for x in w:
        if a and a[-1]==-x:a.pop()
        else:a.append(int(x))
    return tuple(a)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in(A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(k):tuple(v) for k,v in d.items()}
old=tuple(D['retained_paired_indices']);oi={j:i+1 for i,j in enumerate(old)}
F=mp(D['paired_involution']);beta=mp(D['retained_involution'])
def fill(w):return red((1 if x>0 else -1)*oi[abs(x)] for x in w if abs(x) in oi)
def peel(w,j):
    w=red(w);p=[]
    while len(w)>1 and w[0]==-w[-1]:p.append(w[0]);w=w[1:-1]
    assert w==(j,)
    p=tuple(p);return p
slots=(2,3,5,6,7,8,10,11)
word=(6,2,-6,-2)
phis={j:(j,) for j in range(1,6)}
HA={i:() for i in slots};HB={i:() for i in slots}
A={j:(j,) for j in range(1,22)};steps=[]
for letter in word:
    j=abs(letter)-1;op=D['old_actions'][j];heads=H['old_generators'][j]
    if letter>0:
        f=mp(op['geometric_push_paired']);phi=mp(op['retained_push'])
        ha={i:tuple(heads['A_heads'][str(i)]) for i in slots}
        hb={i:tuple(heads['B_heads'][str(i)]) for i in slots}
    else:
        f=mp(op['based_pullback_paired']);phi=mp(op['retained_pullback'])
        ha={i:sub(inv(tuple(heads['A_heads'][str(i)])),phi) for i in slots}
        hb={i:sub(inv(tuple(heads['B_heads'][str(i)])),phi) for i in slots}
    A={j:sub(A[j],f) for j in range(1,22)}
    phis={j:sub(phis[j],phi) for j in range(1,6)}
    HA={i:red(sub(HA[i],phi)+ha[i]) for i in slots}
    HB={i:red(sub(HB[i],phi)+hb[i]) for i in slots}
    assert all(fill(A[old[j-1]])==phis[j] for j in range(1,6))
    steps.append({'geometric_letter':letter,'A6_head':HA[6],'B6_head':HB[6],
                  'retained_action':phis})
assert phis=={j:(j,) for j in range(1,6)}
literal=[]
for i in slots:
    ka=peel(A[i],i);kb=peel(A[i+10],i+10)
    assert red(ka+(i,)+inv(ka))==A[i]
    assert red(kb+(i+10,)+inv(kb))==A[i+10]
    assert fill(ka)==HA[i] and fill(kb)==HB[i]
    literal.append({'slot':i,'A_head':HA[i],'B_head':HB[i],
                    'A_conjugator_F21':ka,'B_conjugator_F21':kb})
assert HA[6]==HB[6]==()
node=next(x for x in D['node_columns'] if(x['loop_index'],x['local_node_index'])==(8,0))
assert node['physical_labels']==[4,12]
row=next(x['seed_row'] for x in I['rows'] if x['node_index']==[8,0])
assert row==[6,6,[1]]
z=tuple(row[2]);got=red(inv(sub(HA[6],beta))+sub(sub(sub(z,beta),phis),beta)+sub(HB[6],beta))
assert got==z

# Actual source lift of geometric word a*(b*a*b^-1)^-1.
sa=next(x for x in S['old_source_generators'] if x['name']=='old_5')
so=next(x for x in S['old_source_generators'] if x['name']=='other_sheet_old_5')
assert sa['far_base_word']==[6] and so['far_base_word']==[2,6,-2]
assert red(tuple(sa['far_base_word'])+inv(tuple(so['far_base_word'])))==word
Sp=mp(sa['source_push_F21']);Oi=mp(so['source_pullback_F21'])
Sw={j:sub(Sp[j],Oi) for j in range(1,22)}
ha=tuple(sa['h_paired']);ho=tuple(so['h_paired'])
hw=sub(red(inv(ho)+ha),Oi)
assert all(Sw[j]==red(inv(hw)+A[j]+hw) for j in range(1,22))
assert all(sub(F[j],Sw)==sub(Sw[j],F) for j in range(1,22))
assert fill(hw)==()
assert all(fill(Sw[old[j-1]])==(j,) for j in range(1,6))
assert fill(peel(Sw[6],6))==fill(peel(Sw[16],16))==()

out={'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(x).hexdigest() for p,x in zip(paths,raw)},
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'geometric_word':word,'composition':'alpha_uv=alpha_v alpha_u; chronological letters applied successively',
     'constant_section':'v=zeta^2, confirmed by independent geometric transport',
     'physical_node':[8,0],'physical_labels':[4,12],'paired_slot':6,
     'seed_row':row,'transported_row':[6,6,got],
     'head_composition_steps':steps,'actual_retained_action':phis,
     'all_eight_literal_peripheral_head_checks':literal,
     'actual_far_push_F21':A,
     'source_schreier_word':['old_5','other_sheet_old_5^-1'],
     'source_correction_h_F21':hw,'source_correction_retained_head':fill(hw),
     'actual_source_push_F21':Sw,'all21_source_normalization_and_F_commutation':True,
     'related_geometry_record':'work_CE/research_retained_section_stabilizer_node_18h.txt',
     'claims_excluded':['full G-column expansion','group-unit column relation','whole overlap','kappa value'],
     'elapsed_seconds':time.monotonic()-started}
(ROOT/'work_A/structural_section_head_word19.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:actual geometric word[6,2,-6,-2] evaluated with anti-homomorphic push order.')
print('PASS:retained phi is literally identity; all16 actual peripheral heads agree with the cocycle computation.')
print('PASS:physical node(8,0),constant v=zeta^2,paired slot6 has A6=B6 heads0 and fixed row(6,6,y1).')
print('PASS:actual returned source operator is old_5*(other_sheet_old_5)^-1;all21 normalization and F-commutation identities.')
print('Source correction length',len(hw),'retained head',list(fill(hw)))
print('No full2-chain,full-column relation or whole-overlap conclusion is computed.')
print('Elapsed seconds',round(out['elapsed_seconds'],3))

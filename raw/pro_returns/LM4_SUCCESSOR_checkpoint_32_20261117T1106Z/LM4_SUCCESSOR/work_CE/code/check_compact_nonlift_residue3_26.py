#!/usr/bin/env python3
"""Finite marked verification of the continuous residue-three nonlift target.

The all-source-word argument is structural: this checks every signed operator
color/level rule, all node types and all three possible common deck residues.
No source orbit is truncated or enumerated.
"""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'family_kernel_schreier25.json',P/'two_operator_filling25.json',
       P/'annular_two_operator25.json']
K,Q,D=[json.loads(p.read_text()) for p in paths]
FAMILY=tuple(K['family_indices_F11'])
POS={i:n for n,i in enumerate(FAMILY)}
MATE={i:i+5 if i<5 else i-5 for i in FAMILY}

def red(w):
    a=[]
    for j in w:
        if a and a[-1]==-j:a.pop()
        else:a.append(j)
    return tuple(a)
def inv(w):return tuple(-j for j in reversed(w))
def sub(w,A):return red(j for i in w for j in (A[abs(i)] if i>0 else inv(A[-i])))
def chi(w):return sum((i==3)-(i==-3) for i in w)
def letter(i,r):return 3*POS[i]+r%3+1
def decode(j):return FAMILY[(j-1)//3],(j-1)%3
def shift(w,r):
    return tuple((1 if j>0 else -1)*letter(decode(abs(j))[0],decode(abs(j))[1]+r) for j in w)
def mul(a,b):return red((*a[0],*shift(b[0],a[1]))),(a[1]+b[1])%3
def inverse(a):return shift(inv(a[0]),-a[1]),(-a[1])%3

# F11 -> F24 semidirect C3. f,g vanish; x is the cyclic shift.
def phi(w):
    word=[];residue=0
    for j in w:
        if abs(j) in POS:
            word.append((1 if j>0 else -1)*letter(abs(j),residue))
        elif abs(j)==11:
            residue=(residue+(1 if j>0 else -1))%3
        else:
            assert abs(j) in (5,10)
    return red(word),residue

dfiber={j:(letter(MATE[decode(j)[0]],1-decode(j)[1]),) for j in range(1,25)}
def delta_target(a):return sub(a[0],dfiber),(-a[1])%3
for j in range(1,25):
    assert sub(dfiber[j],dfiber)==(j,)
    assert sub(shift((j,),1),dfiber)==shift(dfiber[j],-1)
shift_element=((),1)
for j in range(1,25):
    lhs=delta_target(mul(mul(shift_element,((j,),0)),inverse(shift_element)))
    ds=delta_target(shift_element)
    rhs=mul(mul(ds,delta_target(((j,),0))),inverse(ds))
    assert lhs==rhs

delta={int(i):tuple(w) for i,w in D['selected_plus_involution'].items()}
for i in range(1,12):
    assert phi(delta[i])==delta_target(phi((i,)))

keep={letter(1,1):(1,),letter(6,0):(2,)}
rho={j:keep.get(j,()) for j in range(1,25)}
swap={1:(2,),2:(1,)}
for j in range(1,25):assert sub(dfiber[j],rho)==sub(rho[j],swap)
A=(11,1,-11);B=(6,)
assert phi(A)==((letter(1,1),),0) and phi(B)==((letter(6,0),),0)
assert sub(phi(A)[0],rho)==(1,) and sub(phi(B)[0],rho)==(2,)
assert sub(A,delta)==B and sub(B,delta)==A

for name,action in Q['coarse_source_actions'].items():
    for i,w in action.items():assert chi(w)==(int(i)==3),(name,i)
for name,action in K['all_four_signed_source_operators'].items():
    for i,r in action['family_images'].items():
        assert r['signed_core']==int(i) and chi(r['retained_head'])==0

relevant=[];residue_checks=[]
for row in K['all40_node_factor_pairs']:
    u,v=row['first_factor'],row['second_factor']
    i,j=abs(u['signed_core']),abs(v['signed_core'])
    if i in (1,6) and j in (1,6):
        assert {i,j}=={1,6}
        a,b=(u,v) if i==1 else (v,u)
        difference=chi(a['retained_head'])-chi(b['retained_head'])
        assert difference in (0,-1)
        relevant.append({'side':row['side'],'name':row['name'],'sheet':row['sheet'],
                         'difference':difference})
    for r in range(3):
        # Check the exact core criterion for each common deck residue.
        uj=letter(i,chi(u['retained_head'])+r)
        vj=letter(j,chi(v['retained_head'])+r)
        assert not rho[uj] or not rho[vj]
        # Also evaluate the entire original commutator, with all connectors.
        uw=tuple(u['word_F11']);vw=tuple(v['word_F11'])
        comm=red((*uw,*vw,*inv(uw),*inv(vw)))
        image=mul(mul(((),r),phi(comm)),((),-r%3))
        assert image[1]==0 and not sub(image[0],rho)
        residue_checks.append((row['side'],row['name'],row['sheet'],r))
assert len(relevant)==4 and len(residue_checks)==120

out={'status':'PASS_CONTINUOUS_RESIDUE3_TARGET_FULL_DELTA_AND_ALL_NODE_TYPES',
     'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths],
     'free24_basis':[{'id':j,'family':decode(j)[0],'residue':decode(j)[1]} for j in range(1,25)],
     'cyclic_action':{j:shift((j,),1) for j in range(1,25)},
     'delta_on_free24':dfiber,'delta_on_shift':'inverse',
     'rho_free24_to_free2':rho,'actual_free2_section_F11':{'A':A,'B':B},
     'all_relevant_color_pairs':relevant,'all120_literal_node_residue_checks':residue_checks,
     'counts':{'delta_basis_squares':24,'shift_compatibilities':24,'F11_equivariance':11,
               'rho_equivariance':24,'signed_peripheral_rules':32,'signed_retained_rules':12,
               'full_node_residue_words':120},
     'scope':'The uniform level proof kills every signed source/deck translate. The continuous map is restricted to the actual closed family kernel, never identified with its abstract completion. HR1985 supplies the separate profinite free-swap fixed-group theorem.'}
target=P/'compact_nonlift_residue3_26.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print('PASS all24 free-fiber involution squares and all24 cyclic-shift compatibilities')
print('PASS all11 original-generator equivariance and all24 coordinate-projection equivariance checks')
print('PASS literal actual A,B free-two section and its involution swap')
print('PASS all32 signed peripheral color/zero-level rules and all12 retained level rules')
print('PASS all40 node types in all3 common deck residues, including every nonlinear connector (120 words)')
print('OUTPUT',target.relative_to(ROOT))
print('SCOPE the all-source-word conclusion is the uniform invariant-level proof, not a finite orbit test')

#!/usr/bin/env python3
"""One actual index-two free-ten quotient retaining the a-contact.

No finite group or period sweep. The whole nodal family is killed by the
same uniform chi_sum difference argument, checked on the complete inputs.
"""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
sp=ROOT/'work_CE/next_symmetric_nodes/annular_two_operator25.json'
fp=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
S=json.loads(sp.read_text());F=json.loads(fp.read_text())
def red(w):
    s=[]
    for a in w:
        if s and s[-1]==-a:s.pop()
        else:s.append(a)
    return s
def inv(w):return [-a for a in w[::-1]]
def mul(*ws):return red(a for w in ws for a in w)
def sub(w,mp):return mul(*(mp[abs(a)] if a>0 else inv(mp[-a]) for a in w))
def sum3(w):return sum(1 if a>0 else -1 for a in w if abs(a) in (1,2))
selected={1:0,2:0,3:0,4:0,6:1}
node_checks=[]
for row in F['all40_node_factor_pairs']:
    a,b=row['first_factor'],row['second_factor']
    i,j=abs(a['signed_core']),abs(b['signed_core'])
    if i in (6,7,8,9):a,b=b,a;i,j=j,i
    assert i in (1,2,3,4) and j in (6,7,8,9)
    delta=sum3(a['retained_head'])-sum3(b['retained_head'])
    if i in selected and j in selected:
        assert delta%2!=(selected[i]-selected[j])%2
    node_checks.append({'side':row['side'],'name':row['name'],'sheet':row['sheet'],'colors':[i,j],'sum_difference':delta})
for name,op in F['all_four_signed_source_operators'].items():
    heads={sum3(r['retained_head']) for r in op['family_images'].values()}
    assert heads=={{'m':0,'m_inverse':0,'v':-1,'v_inverse':1}[name]}
    for i,r in op['family_images'].items():assert r['signed_core']==int(i)
    for i,r in op['retained_images'].items():assert sum3(r['retained_head'])==(0 if int(i)==11 else 1)

# Target basis a,B,d,e,A_odd,t,u,w,x,y.
lookup={(0,1):1,(0,2):2,(0,3):3,(0,4):4,(1,6):5,
        (1,5):6,(0,10):7,(1,10):8,(0,11):9,(1,11):10}
def scan(w):
    e=0;out=[]
    for a in w:
        j=abs(a);ep=e^(j in (5,10))
        z=lookup.get((e,j),0) if a>0 else -lookup.get((ep,j),0)
        if z:out.append(z)
        e=ep
    assert e==0
    return red(out)
basis=[[1],[2],[3],[4],[5,6,-5],[5,5],[10,-5],[5,10],[11],[5,11,-5]]
assert [scan(w) for w in basis]==[[i] for i in range(1,11)]
rs=[]
for e in (0,1):
    for i in range(1,12):
        ep=e^(i in (5,10));w=mul([5]*e,[i],[-5]*ep)
        if w:rs.append(w)
assert len(rs)==21
actions={}
for name in ('m','m_inverse'):
    mp={int(k):w for k,w in S['source_ordinary_actions'][name].items()}
    actions[name]={i:scan(sub(w,mp)) for i,w in enumerate(basis,1)}
    for w in rs:assert scan(sub(w,mp))==sub(scan(w),actions[name])
for i in range(1,11):
    assert sub(actions['m'][i],actions['m_inverse'])==[i]
    assert sub(actions['m_inverse'][i],actions['m'])==[i]
raw=[r['fiber11'] for r in S['actual_six_source_normal_forms'][:4]]
images=[scan(w) for w in raw]
As=mul(raw[0],inv(raw[3]),inv(raw[0]))
Bs=mul(inv(As),inv(raw[0]),As)
Ds=mul(raw[1],raw[0],inv(raw[2]),inv(raw[0]),inv(raw[1]))
Es=inv(raw[1])
contact_basis={name:scan(w) for name,w in zip(('A_s','B_s','D_s','E_s'),(As,Bs,Ds,Es))}
assert contact_basis['A_s']==[1]
defects={name:mul(sub(contact_basis['D_s'],a),inv(contact_basis['D_s'])) for name,a in actions.items()}
out={'status':'PASS_EXACT_FREE_TEN_ACTUAL_QUOTIENT','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (sp,fp)},
 'target_basis':['a','B','d','e','f bar_a f^-1','f^2','g f^-1','f g','x','f x f^-1'],
 'basis_F11':basis,'selected_family_cosets':selected,'all40_node_checks':node_checks,
 'all21_RS_basis':rs,'actual_signed_m_actions':actions,'raw_four_contact_images':images,
 'transformed_contact_basis':contact_basis,'actual_D_defects':defects,
 'scope':'One actual index-two free quotient, killing the entire N by uniform character/color separation. Exact m quotient diagrams and full words; no source subgroup presentation or centralizer claim yet.'}
(ROOT/'work_A/even_sum_a_source_quotient27.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all40 node omissions and all signed color/character invariants.')
print('PASS all42 actual Schreier quotient diagrams and20 inverse compositions.')
for k,w in contact_basis.items():print(k,len(w),w)
for k,w in defects.items():print('D defect',k,len(w),w)
print('Signed m actions:',actions)

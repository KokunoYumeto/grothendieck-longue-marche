"""Independent literal replay of CE's complete family-kernel data.
No producer imports, no source orbit generation, and no quotient oracle.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,datetime
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
cp=ROOT/'work_CE/next_symmetric_nodes/family_kernel_schreier25.json'
c=json.loads(cp.read_text());ip=ROOT/c['input']['path'];d=json.loads(ip.read_text())
assert hashlib.sha256(ip.read_bytes()).hexdigest()==c['input']['sha256']
fam={1,2,3,4,6,7,8,9};ret={5:1,10:2,11:3};back={1:5,2:10,3:11}
def normal(w,cones=()):
    st=[]
    for q in w:
        q=abs(q) if abs(q) in cones else q
        if st and (st[-1]==-q or q in cones and st[-1]==q):st.pop()
        else:st.append(q)
    return tuple(st)
def inverse(w):return tuple(-q for q in w[::-1])
def product(*ws):return normal(q for w in ws for q in w)
def evaluate(w,im,cones=()):
    return normal((z for q in w for z in (im[abs(q)] if q>0 else inverse(im[-q]))),cones)
def conjugate(u,v):return product(u,v,inverse(u))
def commutator(u,v):return product(u,v,inverse(u),inverse(v))
def lift(t):return tuple((1 if q>0 else -1)*back[abs(q)] for q in t)
def fill(w):return normal((1 if q>0 else -1)*ret[abs(q)] for q in w if abs(q) in ret)
def unpack(k,head=()):
    z=[]
    for sign,t,i in k:z.extend(conjugate(lift(t),(sign*i,)))
    z.extend(lift(head));return normal(z)
def k_normal(k):
    st=[]
    for sign,t,i in k:
        q=(int(sign),tuple(t),int(i))
        if st and st[-1]==(-q[0],q[1],q[2]):st.pop()
        else:st.append(q)
    return tuple(st)
def k_inverse(k):return tuple((-s,t,i) for s,t,i in reversed(k_normal(k)))
def rec(r):
    w=tuple(r['word_F11']);v=tuple(r['conjugator_F11']);q=r['signed_core']
    assert abs(q) in fam and conjugate(v,(q,))==w
    assert fill(v)==tuple(r['retained_head'])
    assert unpack(r['kernel_conjugator'],r['retained_head'])==v
    assert unpack(r['kernel_word'])==w and fill(w)==()
    expected=k_normal([*r['kernel_conjugator'],(1 if q>0 else -1,r['retained_head'],abs(q)),*k_inverse(r['kernel_conjugator'])])
    assert k_normal(r['kernel_word'])==expected
    return w

def ordinary(w):
    state=0;res=[]
    for q in normal(w,(6,7)):
        if q==6:state=1-state
        elif q==7:res.append(11 if state==0 else -11);state=1-state
        else:res.append((abs(q)+5*state)*(1 if q>0 else -1))
    assert not state;return normal(res)
lookup={(r['side'],r['name']):r for r in d['all20_orbifold_node_relations']}
local={f'diagonal_{n}':((i,),(6,i,6)) for n,i in [('a',1),('b',2),('d',3),('e',4)]}
local.update({'pair_ab':((1,),(2,)),'pair_bara_d':((6,1,6),(3,)),'pair_bara_e':((6,1,6),(4,)),
 'pair_d_bare':((3,),(6,4,6)),'pair_b_hdh':((2,),(5,3,-5)),'pair_b_heh':((2,),(5,4,-5))})
seen=set()
for row in c['all40_node_factor_pairs']:
    key=(row['side'],row['name'],row['sheet']);assert key not in seen;seen.add(key)
    src=lookup[key[:2]];maps={int(i):tuple(w) for i,w in d[key[0]+'_local_to_global'].items()}
    lu,lv=local[key[1]];u=evaluate(lu,maps,(6,7));v=evaluate(lv,maps,(6,7))
    orb=normal((*u,*v,*inverse(u),*inverse(v)),(6,7));assert orb==tuple(src['orbifold_fiber7'])
    collar=(6,) if key[2] else ()
    uu=ordinary((*collar,*u,*collar));vv=ordinary((*collar,*v,*collar))
    assert rec(row['first_factor'])==uu and rec(row['second_factor'])==vv
    rel=commutator(uu,vv);assert rel==tuple(src['ordinary_two_sheets'][key[2]])
    assert unpack(row['kernel_relator'])==rel
    ab=Counter()
    for sign,t,i in row['kernel_relator']:ab[(tuple(t),i)]+=sign
    assert all(v==0 for v in ab.values())
assert len(seen)==40
for name,op in c['all_four_signed_source_operators'].items():
    actual={int(i):tuple(w) for i,w in d['source_ordinary_actions'][name].items()}
    assert set(map(int,op['family_images']))==fam
    for si,r in op['family_images'].items():
        i=int(si);assert rec(r)==actual[i];assert r['signed_core']==i
    for si,r in op['retained_images'].items():
        i=int(si);assert i in ret and tuple(r['word_F11'])==actual[i]
        assert fill(actual[i])==tuple(r['retained_head'])
        assert unpack(r['kernel_correction'],r['retained_head'])==actual[i]
delta={int(i):tuple(w) for i,w in d['selected_plus_involution'].items()}
beta={int(i):tuple(w) for i,w in c['retained_cone_action'].items()}
for i in range(1,12):
    assert evaluate(delta[i],delta)==(i,)
    if i in fam:
        mate=i+5 if i<5 else i-5
        assert delta[i]==(11,mate,-11)
    else:
        assert delta[i]==lift(beta[ret[i]])
for i in range(1,4):assert evaluate(beta[i],beta)==(i,)
assert beta[3]==(-3,)
r={'status':'PASS','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
 'full_node_relators':40,'peripheral_factor_replays':80,'same_positive_signed_source_cores':32,'full_retained_corrections':12,
 'full_basis_delta_squared':11,'retained_beta_squared':3,'all_node_abelianizations_zero':True,
 'method':'Independent word/label evaluator reading only stable JSON; no producer import or source orbit generation.',
 'scope':'Complete finite input replay; all-orbit N <= [L,L] and exact paired J_ab follow from the separate uniform proof.'}
(OUT/'family_kernel_schreier_independent25.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS all40 actual node relators, all80 factors and full nonlinear Schreier expansions.')
print('PASS all32 same-positive family operator cores and all12 retained correction words.')
print('PASS entire free-basis involution and retained action, with all node abelianizations zero.')

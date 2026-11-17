#!/usr/bin/env python3
"""Actual 19-generator source and its eleven kernel operators.

The source double cover of the punctured q-base has parity only at q=1.
Its47 Schreier generators comprise11 old generators and36 nodal lifts.
After the28 regular-source nodal lifts are filled, the abstract source
has the stated19-generator free basis. Its image is not asserted free.
All source loops are normalized by the unique free-product cocycle
solution, in the actual corrected common marking.
"""
from pathlib import Path
from collections import Counter
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
names=['symmetric_paired_fox_data.json','symmetric_node_words_pullback_corrected.json',
       'symmetric_source_lasso_corrections.json']
raw={n:(P/n).read_bytes() for n in names};paired,nodes,previous=[json.loads(raw[n]) for n in names]
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(y for x in w for y in (A[abs(x)] if x>0 else inv(A[abs(x)])))
def mp(d):return {int(i):tuple(w) for i,w in d.items()}
F=mp(paired['paired_involution']);cut=mp(paired['paired_basis_forward_in_nodal_cut_basis'])
pair=mp(paired['nodal_cut_basis_in_paired_basis']);Id={j:(j,) for j in range(1,22)}
gens={};invs={}
for r in paired['old_actions']:
    gens[r['index']+1]=mp(r['geometric_push_paired']);invs[r['index']+1]=mp(r['based_pullback_paired'])
for r in nodes['loops']:
    a=mp(r['geometric_push_images']);ai=mp(r['based_pullback_images'])
    gens[r['index']+7]={j:sub(sub(cut[j],a),pair) for j in Id}
    invs[r['index']+7]={j:sub(sub(cut[j],ai),pair) for j in Id}
def action(w):
    A=Id
    for x in w:
        e=gens[x] if x>0 else invs[-x]
        A={j:sub(A[j],e) for j in Id}
    return A
def inner(E):
    c={}
    for j,e in E.items():
        l,r=0,len(e)
        while r-l>1 and e[l]==-e[r-1]:l+=1;r-=1
        assert e[l:r]==(j,);c[j]=e[:l]
    v=red(inv(c[1])+c[2]);n=0;j=0
    while j<len(v) and abs(v[j])==1:n+=v[j];j+=1
    assert not v[j:] or all(x==v[j] and abs(x)==2 for x in v[j:])
    k=red(c[1]+((1,)*n if n>=0 else (-1,)*(-n)))
    assert all(E[i]==red(k+(i,)+inv(k)) for i in Id)
    return k
TAU,TAU1=101,102
def il(x):return x if x in (TAU,TAU1) else -x
def er(w):
    r=[]
    for x in w:
        if r and r[-1]==il(x):r.pop()
        else:r.append(x)
    return tuple(r)
def ei(w):return tuple(il(x) for x in reversed(w))
def eimage(w):
    r=[]
    for x in w:
        j=abs(x);v=(TAU1,TAU) if j==1 else (j,) if j<=11 else (TAU,j-10,TAU)
        r.extend(v if x>0 else ei(v))
    return er(r)
def sch(w):
    parity=0;r=[]
    for x in w:
        if x==TAU:parity^=1
        elif x==TAU1:r.append(1 if parity==0 else -1);parity^=1
        else:r.append((1 if x>0 else -1)*(abs(x)+(10 if parity else 0)))
    assert parity==0
    return red(r)
def solve(k,required=TAU):
    t=er((TAU,)+eimage(k));assert not er(t+t)
    g=[];core=t
    while len(core)>1 and core[0]==il(core[-1]):g.append(core[0]);core=core[1:-1]
    assert core==(required,),('wrong returned fixed branch',core,required)
    if required!=TAU:return None
    if sum(x in (TAU,TAU1) for x in g)%2:g=er(tuple(g)+(TAU,))
    h=sch(g);assert eimage(h)==tuple(g)
    assert red(sub(h,F)+inv(h))==k
    return h
def correction(w,required=TAU):
    A=action(w);Ai=action(inv(w))
    for j in Id:assert sub(A[j],Ai)==(j,)==sub(Ai[j],A)
    k=inner({j:sub(sub(sub(Ai[j],F),A),F) for j in Id})
    assert not red(sub(k,F)+k)
    h=solve(k,required)
    if h is None:return k,None,None,None
    source={j:red(inv(h)+A[j]+h) for j in Id}
    sourcei={j:sub(red(h+(j,)+inv(h)),Ai) for j in Id}
    for j in Id:
        assert sub(source[j],F)==sub(F[j],source)
        assert sub(source[j],sourcei)==(j,)==sub(sourcei[j],source)
    return k,h,source,sourcei

retained=paired['retained_paired_indices'];right=paired['deleted_right_slots']
kept=[i for i in range(1,22) if i in retained or i in right]
assert len(kept)==13
ren={j:i+1 for i,j in enumerate(kept)}
fill13={j:((ren[j],) if j in ren else ()) for j in Id}
ren5={j:i+1 for i,j in enumerate(retained)}
fill5={j:((ren5[j],) if j in ren5 else ()) for j in Id}
fill13to5={ren[j]:((ren5[j],) if j in ren5 else ()) for j in kept}
def restrict(A,Ai,kept,fill):
    r={i+1:sub(A[j],fill) for i,j in enumerate(kept)}
    ri={i+1:sub(Ai[j],fill) for i,j in enumerate(kept)}
    for j in Id:
        if j not in kept:assert not sub(A[j],fill) and not sub(Ai[j],fill)
    for i in r:assert sub(r[i],ri)==(i,)==sub(ri[i],r)
    return r,ri
start=time.monotonic();b=2
# The odd old loop exchanges the two old reflection classes.
k,_,_,_=correction((b,),TAU1)
print('PASS actual q=1 old loop exchanges the two fixed branches.',flush=True)
oldrows=[]
oldspec=[('old_'+str(i-1),(i,)) for i in range(1,7) if i!=b]
oldspec += [('other_sheet_old_'+str(i-1),(b,i,-b)) for i in range(1,7) if i!=b]
oldspec += [('branch_square',(b,b))]
for name,w in oldspec:
    k,h,A,Ai=correction(w)
    A13,A13i=restrict(A,Ai,kept,fill13)
    A5,A5i=restrict(A,Ai,retained,fill5)
    oldrows.append({'name':name,'far_base_word':w,'k_paired':k,'h_paired':h,
        'actual_source_loop':'g_far*h','source_push_F21':A,'source_pullback_F21':Ai,
        'source_push_F13':A13,'source_pullback_F13':A13i,
        'source_push_F5':A5,'source_pullback_F5':A5i,
        'source_fiber_correction_F13':sub(h,fill13),'source_fiber_correction_F5':sub(h,fill5)})
    print('PASS returned old source generator',name,'h length',len(h),'all F21/F13/F5 actions.',flush=True)

nodal=[];seeds=[]
for sheet in (0,1):
    for row,prev in zip(nodes['loops'],previous['loops']):
        i=row['index']+7;w=(i,) if sheet==0 else (b,i,-b)
        k,h,A,Ai=correction(w)
        if sheet==0:assert h==tuple(prev['h_in_paired_basis'])
        h13=sub(h,fill13);h5=sub(h,fill5)
        assert not h5
        fixed=prev['has_fixed_source_nodes']
        hc=sub(h,cut);ab=Counter()
        for x in hc:ab[nodes['initial_order'][abs(x)-1]]+=1 if x>0 else -1
        ab={j:n for j,n in sorted(ab.items()) if n}
        if fixed:
            assert len(ab)==2 and set(ab.values())=={1}
            tags=[nodes['labels'][j] for j in ab]
            assert {x['kind'] for x in tags}=={'A','B'}
            assert tags[0]['index']==tags[1]['index']
            assert {x['branch'] for x in tags}==({'w'} if sheet==0 else {'v'})
            v=h13;c=[]
            while len(v)>1 and v[0]==-v[-1]:c.append(v[0]);v=v[1:-1]
            assert len(v)==1 and v[0]>0 and not fill13to5[v[0]]
            seed={'sheet':sheet,'critical_index':row['index'],'far_base_word':w,
                'positive_source_word_F21':h,'positive_source_word_F13':h13,
                'F13_conjugator':c,'F13_positive_core':v[0],
                'physical_abelianization':ab}
            seeds.append(seed)
        else:
            assert not h13,('regular source loop fails first-family filling',sheet,row['index'])
        nodal.append({'sheet':sheet,'critical_index':row['index'],
            'far_base_word':w,'is_source_puncture':fixed,'h_F21':h,
            'h_F13':h13,'physical_abelianization':ab,
            'after_critical_filling':'source puncture' if fixed else 'trivial by regular-source extension'})
    print('PASS all18 nodal lifts on source sheet',sheet,flush=True)
assert len(oldrows)==11 and len(seeds)==8 and len(nodal)==36
assert sum(not r['is_source_puncture'] for r in nodal)==28
out={'scope':__doc__,'input_sha256':{n:hashlib.sha256(r).hexdigest() for n,r in raw.items()},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'base_letter_convention':'1..6 are old0,1,zeta,zeta^2,zeta^3,zeta^4;7..24 are node indices0..17; b=2',
 'source_cover_parity':'only b (q=1) has odd parity',
 'first_family_F13_kept_paired_indices':kept,'F13_to_retained_F5':fill13to5,
 'old_source_generators':oldrows,'source_peripheral_generators':seeds,
 'all36_returned_nodal_lifts':nodal,
 'actual_source_rank':19,'filled_source_rank':11,
 'kernel_image_description':'I is generated by the orbits of these eight F13 source meridians under all eleven source F13 actions and their inverses. This is a subgroup-generation statement from the source free-factor filling, not an ambient normal-closure assertion.',
 'claims_excluded':['injectivity of the source map','I=R','kappa=0','nonlinear fixed lifting'],
 'elapsed_seconds':time.monotonic()-start}
(P/'symmetric_full_source_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact actual19 source generators,11 source operators,8 positive meridians; elapsed',round(out['elapsed_seconds'],3),flush=True)

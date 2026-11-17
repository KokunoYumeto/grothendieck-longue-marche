#!/usr/bin/env python3
"""Exact ordinary cover and actual both-family quotient, without a word oracle.

All marked9/36 inputs are retained. Cone-square and cross-relation Tietze
eliminations are explicit; no graph-kernel or post-cross injection is inferred.
"""
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / 'work_CE/next_symmetric_nodes'
input_path = P / 'annular_neck_presentation23.json'
G = json.loads(input_path.read_text())

def red(w, cones=()):
    s = []
    for x in w:
        if abs(x) in cones:
            x = abs(x)
        if s and (s[-1] == -x or x in cones and s[-1] == x):
            s.pop()
        else:
            s.append(x)
    return tuple(s)

def inv(w, cones=()):
    return red((-x for x in reversed(w)), cones)

def sub(w, D, cones=()):
    return red((x for j in w for x in
                (D[abs(j)] if j > 0 else inv(D[-j], cones))), cones)

def cat(*ws, cones=()):
    return red((x for w in ws for x in w), cones)

def comm(u,v):
    return cat(u,v,inv(u),inv(v))

cones=(6,7)
eta={int(j):tuple(w) for j,w in G['eta_in_common_K'].items()}
# New cone6=c=actual selected minus gap, cone7=d=actual plus gap.
# The entire common K basis stays fixed; these are not individual peripheral
# conjugations followed by an unrecorded marking reset.
old_new={j:(j,) for j in range(1,10)}
old_new[6]=(-1,6,1)
old_new[7]=cat(inv(eta[1]),(7,),eta[1],cones=cones)
new_old={j:(j,) for j in range(1,10)}
new_old[6]=tuple(G['actual_gap_cones']['minus'])
new_old[7]=tuple(G['actual_gap_cones']['plus'])
for j in range(1,10):
    assert sub(old_new[j],new_old,cones)==(j,)
    assert sub(new_old[j],old_new,cones)==(j,)

# Universal ordinary kernel in F7*C2(c)*C2(d) is freeF15.
#1..5=K,6..10=cKc,11=kminus,12=kplus,13=x=dc,
#14=c kminus c,15=c kplus c.
pos={**{j:j for j in range(1,6)},8:11,9:12}
bar={**{j:j+5 for j in range(1,6)},8:14,9:15}
delta15={j:(j+5,) for j in range(1,6)}
delta15.update({j+5:(j,) for j in range(1,6)})
delta15.update({11:(14,),14:(11,),12:(15,),15:(12,),13:(-13,)})
back15={j:(j,) for j in range(1,6)}
back15.update({j+5:(6,j,6) for j in range(1,6)})
back15.update({11:(8,),12:(9,),13:(7,6),14:(6,8,6),15:(6,9,6)})

def rewrite(w,start=0):
    state=start;out=[]
    for x in red(w,cones):
        j=abs(x)
        if j==6:
            state^=1
        elif j==7:
            out.append(13 if state==0 else -13);state^=1
        else:
            out.append((pos[j] if state==0 else bar[j])*(1 if x>0 else -1))
    return red(out),state

for j in range(1,16):
    assert rewrite(back15[j])==((j,),0)
    assert sub(delta15[j],back15,cones)==cat((6,),back15[j],(6,),cones=cones)
    assert sub(delta15[j],delta15)==(j,)

# The two actual cross relations eliminate precisely the two barred bases.
elim={j:(j,) for j in range(1,16)}
elim[14]=(-13,11,13)
elim[15]=(12,)
delta={j:sub(delta15[j],elim) for j in range(1,14)}
for j in range(1,16):
    assert sub(delta15[j],elim)==sub(elim[j],delta)
for j in range(1,14):
    assert sub(delta[j],delta)==(j,)
# Conjugation by the ACTUAL selected plus cone d=x c.
delta_plus={j:cat((13,),delta[j],(-13,)) for j in range(1,14)}
for j in range(1,14):
    assert sub(delta_plus[j],delta_plus)==(j,)

regional=[];cross=[]
for row in G['regional_relators']+G['cross_relators']:
    old=tuple(row['word']);new=sub(old,old_new,cones)
    records=[]
    for state in (0,1):
        rs,end=rewrite(new,state)
        assert end==state
        expected=cat((6,) if state else (),new,(6,) if state else (),cones=cones)
        assert sub(rs,back15,cones)==expected
        small=sub(rs,elim)
        records.append({'state':state,'free15':rs,'free13':small})
    assert records[1]['free13']==sub(records[0]['free13'],delta)
    rec={'name':row['name'],'side':row.get('side'),'original9':old,
         'selected_cone9':new,'ordinary_rewrites':records}
    if row in G['cross_relators']:
        assert all(not r['free13'] for r in records)
        cross.append(rec)
    else:regional.append(rec)
assert len(regional)==32 and len(cross)==2
assert cross[0]['selected_cone9']==red(comm((7,),(8,)),cones)
assert cross[1]['selected_cone9']==red(comm((6,),(9,)),cones)

back13={j:sub(back15[j],new_old,cones) for j in range(1,14)}
for j in range(1,14):
    w=sub(back13[j],old_new,cones);rs,end=rewrite(w)
    assert end==0 and sub(rs,elim)==(j,)
sources=[]
for row in G['actual_six_source_words']:
    w=sub(row['word'],old_new,cones);rs,end=rewrite(w)
    assert end==0
    sources.append({'name':row['name'],'actual_original9':row['word'],
                    'ordinary13':sub(rs,elim)})

# Fill exactly the eight A/B family generators. Fiber basis(f,g=cfc,x=dc),
# base letters(m=kminus,p=kplus). No retained generator is filled.
fill={j:() for j in range(1,14)}
fill.update({5:(1,),10:(2,),13:(3,),11:(4,),12:(5,)})
coarse=[]
for row in regional:
    for rr in row['ordinary_rewrites']:
        w=sub(rr['free13'],fill)
        if w:coarse.append({'side':row['side'],'name':row['name'],
                            'state':rr['state'],'word':w})
assert len(coarse)==8
am={1:(-1,2,1),2:(1,),3:(3,-2,1)}
ami={1:(2,),2:(2,1,-2),3:(3,1,-2)}
ap={1:(1,3,2,-3,-1),2:(2,-3,1,3,-2),3:(1,3,-2)}
api={1:(3,2,-3),2:(-3,1,3),3:(3,-2,-3,1,3)}
for A,Ai in ((am,ami),(ap,api)):
    for j in range(1,4):
        assert sub(A[j],Ai)==sub(Ai[j],A)==(j,)
actions={4:am,-4:ami,5:ap,-5:api}
def acted(w,head):
    for j in reversed(head):w=sub(w,actions[j])
    return w
def normal(w):
    v=();head=()
    for j in w:
        if abs(j)<=3:v=cat(v,acted((j,),head))
        else:head=cat(head,(j,))
    return v,head
for row in coarse:assert normal(row['word'])==((),()),row
mapping=[]
for k,A in ((4,am),(5,ap)):
    for j in range(1,4):
        r=cat((k,j,-k),inv(A[j]));assert normal(r)==((),())
        mapping.append({'base':k,'fiber':j,'word':r})
# Exact free changes exposing the converse presentation comparison:
# m fixes u=x f and v=g x^-1; p fixes y=f x and v=g x^-1.
assert sub((3,1),am)==(3,1)
assert sub((2,-3),am)==(2,-3)
assert sub((1,3),ap)==(1,3)
assert sub((2,-3),ap)==(2,-3)

out={'status':'PASS_COMPLETE_ORDINARY13_AND_COARSE_ACTIONS',
 'input':{'path':str(input_path.relative_to(ROOT)),
          'sha256':hashlib.sha256(input_path.read_bytes()).hexdigest()},
 'selected_cone_old_to_new':old_new,'selected_cone_new_to_old':new_old,
 'universal_free15_to_selected9':back15,'cross_elimination':{14:elim[14],15:elim[15]},
 'all_cross_rewrites':cross,'all32_regional_two_sheet_rewrites':regional,
 'ordinary13_generators':['a','B','d','e','f','c a c','c B c','c d c','c e c','c f c','kminus','kplus','x=dcone ccone'],
 'ordinary13_to_actual9':back13,'selected_minus_cone_action':delta,
 'selected_plus_cone_action':delta_plus,'actual_six_source_words':sources,
 'actual_family_filling':fill,'all_eight_nonempty_coarse_relators':coarse,
 'coarse_positive_actions':{'kminus':am,'kplus':ap},
 'coarse_negative_actions':{'kminus':ami,'kplus':api},
 'coarse_mapping_relators':mapping,
 'scope':'Exact ordinary index-two presentation with64 regional relators after both cross eliminations. Coarse quotient is the actual eight-family normal filling; automorphism/converse presentation proof is recorded separately. No splitting back into the family-unfilled group or final source-centralizer assertion.'}
(P/'annular_ordinary13_24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS both selected-cone gauge maps on all9 original generators')
print('PASS universal free15 kernel and all68 complete two-sheet relator rewrites')
print('PASS exact two cross eliminations; complete ordinary13 presentation with64 regional relators')
print('PASS both actual selected-cone involutions on all13 generators')
print('PASS all13 actual generator round trips and six complete source words')
print('PASS exact filling of8 family generators leaves the following8 nonempty relators:')
for row in coarse:print(row['side'],row['name'],row['state'],row['word'])
print('PASS both coarse free3 actions/inverses and all actual relators in F3 semidirect F2')
print('SCOPE converse coarse presentation is proved in the companion note; no unfilled splitting or centralizer conclusion')

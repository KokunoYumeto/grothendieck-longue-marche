#!/usr/bin/env python3
"""Independent complete replay of the actual annular source detector.

No DE or CE producer is imported.  Contact source words are reconstructed
from the original positive Artin actions, with their unique even cone
conjugator, before comparing the saved detector certificate.
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
paths={
 'raw':ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
 'adapted':ROOT/'work_CE/next_symmetric_nodes/inner_q0_adapted_basis22.json',
 'source':ROOT/'work_DE/next_marginal_source/inner_q0_source22.json',
 'detector':ROOT/'work_DE/next_marginal_source/annular_source_retraction22.json'}
raw,D,S,DE=(json.loads(paths[k].read_text()) for k in ('raw','adapted','source','detector'))
def reduce(w,cone=None):
    stack=[]
    for letter in w:
        letter=int(letter)
        if cone is not None and abs(letter)==cone:letter=cone
        if stack and (letter==-stack[-1] or (cone is not None and letter==stack[-1]==cone)):
            stack.pop()
        else:stack.append(letter)
    return tuple(stack)
def inverse(w):return tuple(-x for x in reversed(w))
def product(*ww,cone=None):return reduce((x for w in ww for x in w),cone)
def subst(w,A,cone=None):
    return product(*(A[abs(x)] if x>0 else inverse(A[-x]) for x in w),cone=cone)
def conj(g,w,cone=None):return product(g,w,inverse(g),cone=cone)
def peel_involution(word,cone):
    w=list(reduce(word,cone));left=[]
    while len(w)>1:
        assert w[-1]==-w[0] or abs(w[-1])==abs(w[0])==cone
        left.append(w.pop(0));w.pop()
    assert w==[cone]
    if sum(abs(x)==cone for x in left)%2:left.append(cone)
    left=reduce(left,cone)
    assert conj(left,(cone,),cone)==reduce(word,cone)
    assert sum(abs(x)==cone for x in left)%2==0
    return left
J={int(i):tuple(w) for i,w in D['Y_in_old'].items()}
Ji={int(i):tuple(w) for i,w in D['old_in_Y'].items()}
for i in range(1,7):
    assert subst(J[i],Ji)==(i,)
    assert subst(Ji[i],J)==(i,)
K=(-3,1)
contact=[]
for name in ('beta_11','beta_22','beta_33','beta_44'):
    loop=next(row for row in raw['loops'] if row['name']==name)
    v=peel_involution(loop['positive_push']['2'],2)
    old_word=conj(K,v,2)
    Yword=subst(old_word,Ji,3)
    assert subst(Yword,J,2)==old_word
    saved=next(row for row in S['four_contact_source_words_in_common_q0_marking'] if row['name']==name)
    assert Yword==tuple(saved['source_word_in_q0_adapted_Y_basis'])
    contact.append({'name':name,'raw_even_conjugator':v,'C_based_old_word':old_word,'Y_word':Yword})

# Reconstruct the local source action from a positive full twist, rather
# than assuming the previously stored corrected arrays.
phi={i:(i,) for i in range(1,7)};phi[3]=(3,4,-3);phi[4]=(3,)
phiinv={i:(i,) for i in range(1,7)};phiinv[3]=(4,);phiinv[4]=(-4,3,4)
L={i:subst(phi[i],phi) for i in range(1,7)}
Linv={i:subst(phiinv[i],phiinv) for i in range(1,7)}
v=(3,4,3)
sigma={i:conj(inverse(v),L[i],3) for i in range(1,7)}
sigmainv={i:subst(conj(v,(i,),3),Linv,3) for i in range(1,7)}
for i in range(1,7):
    assert sigma[i]==tuple(D['source_h_action'][str(i)])
    assert sigmainv[i]==tuple(D['source_h_inverse_action'][str(i)])
    assert subst(sigma[i],sigmainv,3)==(i,)
    assert subst(sigmainv[i],sigma,3)==(i,)

# Ordinary-kernel letters are indexed by the raw ordinary peripheral and
# its sheet.  First Schreier rewrite, then apply a separate free map.
ordinary=(1,2,4,5,6)
def schreier(w):
    parity=0;letters=[]
    for x in w:
        if abs(x)==3:parity^=1
        else:
            assert abs(x) in ordinary
            letters.append(((abs(x),parity),1 if x>0 else -1))
    assert parity==0
    return letters
map10={(1,0):(1,),(1,1):(),(2,0):(),(2,1):(2,),
       (4,0):(5,),(4,1):(5,),(5,0):(3,),(5,1):(),(6,0):(4,),(6,1):()}
def detector(w):
    return product(*(map10[g] if s>0 else inverse(map10[g]) for g,s in schreier(w)))
mapping=[]
for i in ordinary:
    for side in (0,1):
        w=(i,) if side==0 else (3,i,3)
        target=detector(w)
        for direction,A,head in (('positive',sigma,(-5,)),('negative',sigmainv,(5,))):
            actual=detector(subst(w,A,3))
            expected=conj(head,target)
            assert actual==expected
            mapping.append({'generator':w,'direction':direction,'image':actual})
nodes=[]
for row in D['all_ten_relations']:
    word=tuple(row['new_relation'])
    for side in (0,1):
        tested=word if side==0 else (3,)+word+(3,)
        assert detector(tested)==()
        nodes.append({'name':row['name'],'physical_labels':row['physical_labels'],'sheet':side})
for row in contact:row['target_word']=detector(row['Y_word'])
images={1:(2,),2:(2,5,3,4,-3,-5,-2),3:(3,),4:(1,),5:(5,)}
assert [row['target_word'] for row in contact]==[images[i] for i in range(1,5)]
back={1:(4,),2:(1,),3:(3,),4:(-3,-5,-1,2,1,5,3),5:(5,)}
for i in range(1,6):
    assert subst(images[i],back)==(i,)
    assert subst(back[i],images)==(i,)
assert {int(k):tuple(v) for k,v in DE['source_to_target_free_basis'].items()}==images
assert {int(k):tuple(v) for k,v in DE['target_to_source_inverse_basis'].items()}==back
out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths.values()},
 'source_reconstructed_from_original_positive_push':contact,
 'twenty_signed_generic_mapping_checks':mapping,'twenty_full_node_checks':nodes,
 'source_images':images,'inverse_source_basis':back,
 'both_free5_inverse_compositions':10,
 'scope':'Actual annular source embeds as a retract of the ordinary group and has its full topology. Centralizer equality requires the separate complete graph proof.'}
dest=ROOT/'work_CE/next_symmetric_nodes/annular_source_detector_independent23.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print('PASS all four actual source words reconstructed from original positive actions')
print('PASS all six source actions/inverses reconstructed from the local full twist')
print('PASS all ten ordinary generators in both signed mapping relations')
print('PASS all twenty complete node words')
print('PASS actual five source images and both five-generator inverse bases')
print('PASS no producer imported; complete actual source-retraction replay')

#!/usr/bin/env python3
"""Exact mirror-fold Tietze input; no quotient solver or group census."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
src = ROOT / 'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
D = json.loads(src.read_text())

def reduce(w, cones):
    out = []
    for x in w:
        if abs(x) in cones:
            x = abs(x)
        if out and (out[-1] == -x or x in cones and out[-1] == x):
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def inverse(w, cones):
    return reduce((-x for x in reversed(w)), cones)

def product(*words, cones):
    return reduce((x for w in words for x in w), cones)

def substitute(w, images, cones):
    return reduce((z for x in w for z in
                   (images[abs(x)] if x > 0 else inverse(images[-x], cones))), cones)

# Fold labels 1..6 are r0..r5; 7 is Cminus, 8 is kminus.
FCONES = set(range(1, 8))
GCONES = {6, 7}
rf = lambda w: reduce(w, FCONES)
pf = lambda *ws: product(*ws, cones=FCONES)
j = (1,)
O = {i: (i, i+1) for i in range(1, 6)}
K_to_O = {1: (2,), 2: (-2,1,2), 3: (4,),
          4: (-5,-4,3,4,5), 5: (4,5,-4)}
K = {i: substitute(K_to_O[i], O, FCONES) for i in range(1, 6)}
assert K == {1:(2,3), 2:(3,2,1,3), 3:(4,5),
             4:(6,4,3,6), 5:(4,6,5,4)}
global_to_fold = dict(K)
global_to_fold.update({6:(7,), 7:(1,7,1), 8:(8,), 9:(1,8,1), 10:j})
eta = {int(i):tuple(w) for i,w in D['eta_in_common_K'].items()}
for i in range(1, 6):
    assert substitute(eta[i], K, FCONES) == pf(j,K[i],j)

# Inverse words in the old group with the actual external mirror j=10.
O_global = {1:(1,2,-1), 2:(1,), 3:(5,3,4,-3,-5),
            4:(3,), 5:(-3,5,3)}
prefix = ()
fold_to_extended = {1:(10,), 7:(6,), 8:(8,)}
for i in range(1, 6):
    prefix = product(prefix,O_global[i],cones=GCONES)
    fold_to_extended[i+1] = (10,)+prefix

# Exact normal form in the pre-relator semidirect product. The mirror
# acts by eta on K and swaps the two C and k generators.
mirror = dict(eta)
mirror.update({6:(7,),7:(6,),8:(9,),9:(8,)})
for i in range(1, 10):
    assert substitute(mirror[i],mirror,GCONES) == (i,)

def extended_normal(w):
    word, parity = (), 0
    for x in w:
        if abs(x) == 10:
            parity ^= 1
            continue
        step = (x,)
        if parity:
            step = substitute(step,mirror,GCONES)
        word = product(word,step,cones=GCONES)
    return word,parity

for i in range(1, 9):
    assert substitute(fold_to_extended[i],global_to_fold,FCONES) == (i,)
for i in range(1, 11):
    expanded = tuple(z for x in global_to_fold[i] for z in
                     (fold_to_extended[abs(x)] if x>0
                      else inverse(fold_to_extended[-x],GCONES|{10})))
    assert extended_normal(expanded) == extended_normal((i,))

minus,plus = {},{}
for row in D['regional_relators']:
    (minus if row['side']=='minus' else plus)[row['name']] = \
        substitute(row['word'],global_to_fold,FCONES)
assert len(minus)==len(plus)==16
for name in minus:
    assert plus[name] == pf(j,minus[name],j)

cross = [substitute(row['word'],global_to_fold,FCONES)
         for row in D['cross_relators']]
assert cross[1] == pf(j,cross[0],j)
assert cross[0] == (1,2,3,7,3,2,1,8,1,2,3,7,3,2,1,-8)
for w in D['cone_squares']:
    assert substitute(w,global_to_fold,FCONES) == ()

relators = [{'name':f'{i}_square','word':(i,i)} for i in range(1,8)]
relators += [{'name':name,'word':w} for name,w in minus.items()]
relators.append({'name':'single_folded_cross','word':cross[0]})
assert len(relators)==24

sources=[]
for row in D['actual_six_source_words']:
    word=substitute(row['word'],global_to_fold,FCONES)
    assert sum(abs(x)==7 for x in word)%2==0
    assert sum(abs(x)<=6 for x in word)%2==0
    sources.append({'name':row['name'],'word':word,
                    'geometric_base_F2_image':row['base_F2_image'],
                    'original_height':row['unfolding_height']})

result = {
    'status':'PASS_ACTUAL_FOLDED_PRESENTATION',
    'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
    'input_path':str(src.relative_to(ROOT)),
    'generators':{str(i):('r'+str(i-1) if i<=6 else 'Cminus' if i==7 else 'kminus')
                  for i in range(1,9)},
    'free_product_before_relators':'C2(r0)*...*C2(r5)*C2(Cminus)*Z(kminus)',
    'common_O_basis_in_fold':O,
    'common_adapted_K_in_fold':K,
    'global_to_fold':global_to_fold,
    'fold_to_extended_global':fold_to_extended,
    'inverse_checks':{'folded_generators':8,'extended_global_generators':10},
    'outer_relator_j_conjugacy_checks':16,
    'second_cross_is_j_conjugate':True,
    'relators':relators,
    'total_generator_count':8,
    'total_free_group_relator_count':24,
    'actual_selected_cones':{side:substitute(w,global_to_fold,FCONES)
                             for side,w in D['actual_gap_cones'].items()},
    'actual_six_source_words':sources,
    'source_word_lengths':[len(row['word']) for row in sources],
    'scope':'Exact actual mirror extension of G_ann. The original G_ann is the mirror-parity kernel. This is an invertible marked presentation change, not a quotient normal-form or source-injectivity result.',
}
dest=ROOT/'work_A/annular_mirror_fold23.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print('PASS actual prefix-reflection edge map and 18 generator inverse checks')
print('PASS all16 outer relations are literal j-conjugates; second cross likewise')
print('PASS exact 8-generator/24-relator mirror-extension presentation')
print('PASS all6 actual source words and both parity checks; lengths',result['source_word_lengths'])

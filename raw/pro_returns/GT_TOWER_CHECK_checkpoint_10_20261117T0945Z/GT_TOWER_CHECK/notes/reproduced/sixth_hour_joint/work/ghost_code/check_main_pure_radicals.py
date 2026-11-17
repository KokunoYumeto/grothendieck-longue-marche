#!/usr/bin/env python3
"""Literal pure source words for both complete orthogonal radicals."""
from pathlib import Path
import json
import runpy
import numpy as np

here = Path(__file__).resolve().parent
b = runpy.run_path(str(here/'check_main_orthogonal_generation.py'))
D = b['D']
data = json.loads((D/'translation_quaternion_homology.json').read_text())
cover = json.loads((D/'translation_cover_basis.json').read_text())
labels = [tuple(x) for x in cover['standard_peripheral_labels']]
labels.append(tuple(cover['last_peripheral_label']))
assert len(set(labels)) == 9
label_index = {x:i for i,x in enumerate(labels)}
identity = tuple(range(9))
permutations = [identity]*4
for k in range(7):
    p = list(identity)
    p[k], p[k+1] = p[k+1], p[k]
    permutations.append(tuple(p))
for dx,dy in ((1,0),(0,1)):
    permutations.append(tuple(label_index[((x+dx)%3,(y+dy)%3)] for x,y in labels))
permutations += [identity,identity]
assert len(permutations) == 15


def compose(a,c): return tuple(a[c[i]] for i in range(9))
def inverse_perm(a): return tuple(a.index(i) for i in range(9))
def inverse_word(w): return tuple(-x for x in w[::-1])


def word_perm(w):
    p=identity
    for j in w:
        q=permutations[abs(j)-1]
        p=compose(p,q if j>0 else inverse_perm(q))
    return p


def expanded(w):
    result=[]
    for j in w:
        a=tuple(data['kernel_generator_words'][abs(j)-1])
        result.extend(a if j>0 else inverse_word(a))
    return tuple(result)


def evaluate360(w):
    a=b['I'].copy()
    for j in w:
        g=b['generators'][abs(j)-1]
        a=a@(g if j>0 else b['inverse'](g))%3
    return a


certificate=b['certificate']
root_index=certificate['root_generator_index']
root_word=tuple(data['kernel_generator_words'][root_index])
assert root_word==(3,5,-3)
root_perm=word_perm(root_word)
assert sum(a!=i for i,a in enumerate(root_perm))==2
assert compose(root_perm,root_perm)==identity
e=b['e'];parameters=b['parameters'];pure_words=[];pure_matrices=[]
for v,w0 in zip(parameters,certificate['conjugating_words_in_360_generators']):
    w=tuple(w0)+(root_index+1,)+inverse_word(tuple(w0))
    source=expanded(w)
    p=word_perm(source)
    assert sum(a!=i for i,a in enumerate(p))==2
    assert word_perm(source+source)==identity
    matrix=evaluate360(w+w)
    assert np.array_equal(matrix,b['radical'](e,2*v%3))
    pure_words.append(source+source);pure_matrices.append(matrix)
assert b['rank'](np.vstack((e,2*parameters%3)))==17
opposite_index=certificate['opposite_generator_index']
opposite_word=tuple(data['kernel_generator_words'][opposite_index])
opposite=b['generators'][opposite_index]
opposite_words=[]
for word,matrix,v in zip(pure_words,pure_matrices,parameters):
    word2=opposite_word+word+inverse_word(opposite_word)
    assert word_perm(word2)==identity
    conjugate=opposite@matrix%3@b['inverse'](opposite)%3
    assert np.array_equal(conjugate,b['radical'](opposite@e%3,2*opposite@v%3))
    opposite_words.append(word2)
assert e@b['F']@(opposite@e)%3 != 0
print('NEW PASS all16 squared root words are literally pure and generate the full first radical')
print('NEW PASS all16 conjugated squared words are literally pure and generate the opposite radical')

word15=tuple(data['kernel_generator_words'][15])
assert word15==(1,1,-13)
p=word_perm(word15)
assert p!=identity and compose(compose(p,p),p)==identity
assert word_perm(word15*3)==identity
assert certificate['all_generator_spinor_norms'][15]==2
g=b['generators'][15]
g3=g@g%3@g%3
assert b['determinant'](g3)==1 and np.array_equal(g3.T@b['F']@g3%3,b['F'])
print('NEW PASS source15 cubed is pure with nonsquare spinor; the pure image is the full SO18^-(3)')

Path(__file__).with_suffix('.json').write_text(json.dumps({
    'scope':'Actual pure quaternion-kernel words for the two complete orthogonal radicals and nonsquare spinor',
    'root_word15':root_word,'root_permutation':root_perm,
    'pure_first_radical_words15':pure_words,
    'opposite_word15':opposite_word,'pure_opposite_radical_words15':opposite_words,
    'pure_nonsquare_word15':word15*3,'nonsquare_spinor':2,
    'puncture_labels':labels,'source_generator_permutations':permutations,
},indent=2)+'\n')

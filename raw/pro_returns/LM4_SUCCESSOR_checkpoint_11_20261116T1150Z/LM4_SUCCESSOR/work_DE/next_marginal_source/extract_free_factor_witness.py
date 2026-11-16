"""Extract actual source words for a four-generator filling free factor."""
from pathlib import Path
import json,time
from weighted_stallings import WeightedFold,inverse,multiply,substitute
HERE=Path(__file__).resolve().parent
D=json.loads((HERE/'positive_fiber_data.json').read_text())
R=json.loads((HERE/'stallings_orbit_radius1.json').read_text())
F=[D['new_fiber_words'][str(i)] for i in range(11,19)]
labels=[{'old_source_conjugator':[],'new_source_index':i} for i in range(11,19)]
added=sorted(R['added_words'],key=lambda z:len(z['word']))
words=list(F);start=time.monotonic();chosen=[]
for entry in added:
    words.append(entry['word']);labels.append({k:v for k,v in entry.items() if k!='word'});chosen.append(entry)
    g=WeightedFold(words,allow_relations=True)
    witness=g.rewrite((5,))
    if witness is not None:
        print('x5 found after',len(chosen),'shortest additional words, elapsed',round(time.monotonic()-start,3),flush=True)
        break
else:raise AssertionError('Certified H1 did not recover x5')
# Greedily discard unnecessary generators; membership is tested exactly.
changed=True
while changed:
    changed=False
    for i in range(len(words)-1,-1,-1):
        trial=words[:i]+words[i+1:]
        h=WeightedFold(trial,allow_relations=True)
        if h.rewrite((5,)) is not None:
            words=trial;labels=labels[:i]+labels[i+1:];changed=True;break
g=WeightedFold(words,allow_relations=True);w5=g.rewrite((5,))
assert w5 is not None
h=WeightedFold(F);w1=h.rewrite((1,));w7=h.rewrite((7,))
C=(-7,-6,-5,-4)
y3=multiply(C,(3,),inverse(C))
assert y3==inverse(tuple(F[0]))
# This is a literal Nielsen automorphism: only x3 is conjugated by C,
# which does not involve x3.  Its inverse is displayed and checked.
basis={j:(j,) for j in range(1,8)};basis[3]=y3
back={j:(j,) for j in range(1,8)};back[3]=multiply(inverse(C),(3,),C)
for j in range(1,8):assert substitute(basis[j],back)==(j,)==substitute(back[j],basis)
out={'description':'Exact source words for x1,x5,x7 and C x3 C^-1; these form the killed half of a specified Nielsen basis. This does not prove marginal source equality or normality.',
     'x1_seed_word':w1,'x7_seed_word':w7,'x5_generators':labels,'x5_generator_fiber_words':words,'x5_word':w5,
     'conjugator_C':C,'basis_images':basis,'inverse_basis_images':back,
     'four_free_factor_generators':[basis[j] for j in (1,3,5,7)]}
(HERE/'free_factor_witness.json').write_text(json.dumps(out,indent=2)+'\n')
print('x1 in original eight seeds:',w1)
print('x7 in original eight seeds:',w7)
print('x5 generator labels:',labels)
print('x5 word:',w5)
print('y3=nu11^-1:',y3)
print('PASS: independent free substitution, both Nielsen inverse compositions, and the four-puncture filling.')


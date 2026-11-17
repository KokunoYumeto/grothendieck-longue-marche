"""Exact marked index-two rewriting of the proposed actual neck/base subgroup.

The structural proof identifies L=<h,k,V_1,...,V_4 | [h^2,k], [k,V_i]>.
This producer checks the complete Reidemeister--Schreier presentation and
the actual free-neck branch word. It does not replace that structural
identification by a finite test.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-letter for letter in reversed(word))


def commutator(left, right):
    return reduce_word(left + right + inverse(left) + inverse(right))


def substitute(word, images):
    return reduce_word(letter for old in word
                       for letter in (images[old] if old > 0 else inverse(images[-old])))


# Old generators: h=1,k=2,V_i=i+2 for1<=i<=4.
# New generators: t=1,k0=2,k1=3,V0_i=i+3,V1_i=i+7.
new_names = ['t', 'k0', 'k1'] + ['V0_' + str(i) for i in range(1,5)] + ['V1_' + str(i) for i in range(1,5)]
back = {1:(1,1), 2:(2,), 3:(1,2,-1)}
for i in range(1,5):
    back[i+3] = (i+2,)
    back[i+7] = (1,i+2,-1)


def schreier(word, start=0):
    state = start
    result = []
    for letter in word:
        generator = abs(letter)
        next_state = state ^ int(generator == 1)
        positive_state = state if letter > 0 else next_state
        if generator == 1:
            output = () if positive_state == 0 else (1,)
        elif generator == 2:
            output = (2 if positive_state == 0 else 3,)
        else:
            i = generator - 2
            output = (i+3 if positive_state == 0 else i+7,)
        result.extend(output if letter > 0 else inverse(output))
        state = next_state
    return reduce_word(result), state


old_relators = [commutator((1,1),(2,))] + [commutator((2,),(i+2,)) for i in range(1,5)]
expected_edges = [(1,2),(1,3)] + [(2,i+3) for i in range(1,5)] + [(3,i+7) for i in range(1,5)]
expected_relators = {commutator((a,),(b,)) for a,b in expected_edges}
actual_relators = []
checks = []
for number, relator in enumerate(old_relators):
    for start in (0,1):
        rewritten, end = schreier(relator,start)
        assert end == start
        assert rewritten in expected_relators
        old_conjugate = reduce_word(((1,) if start else ()) + relator + ((-1,) if start else ()))
        assert substitute(rewritten,back) == old_conjugate
        actual_relators.append(rewritten)
        checks.append({'old_relator_index':number,'transversal':start,
                       'old_word':relator,'rewritten_word':rewritten,
                       'inverse_substitution_is_exact_free_word':True})
assert set(actual_relators) == expected_relators and len(actual_relators) == 10

for generator in range(1,12):
    rewritten,end = schreier(back[generator])
    assert end == 0 and rewritten == (generator,)

# The graph really is a tree, using only its explicit ten edges.
adjacency = {i:set() for i in range(1,12)}
for a,b in expected_edges:
    adjacency[a].add(b)
    adjacency[b].add(a)
seen={1}; pending=[1]
while pending:
    for other in adjacency[pending.pop()]:
        if other not in seen:
            seen.add(other);pending.append(other)
assert len(seen)==11 and len(expected_edges)==10

# Actual f=h k^-1. Its square is k1^-1 t k0^-1, literally.
f=(1,-2)
branch,end=schreier(f+f)
assert end==0 and branch==(-3,1,-2)
assert substitute(branch,back)==f+f
leaf_checks=[]
for i in range(1,5):
    word=reduce_word(f+(i+2,)+inverse(f))
    rewritten,end=schreier(word)
    assert end==0 and rewritten==(-3,i+7,3)
    assert (3,i+7) in expected_edges
    leaf_checks.append({'i':i,'actual_f_conjugate':word,
                        'schreier_word':rewritten,'equals_V1_by_exact_edge':[3,i+7]})

# The retraction of L2 to the actual K2 kills k0,k1, sends t to F,
# and keeps all eight leaves. Every RAAG edge maps to the identity.
# K2 labels: F=1 and the eight leaf labels remain4,...,11.
retract={1:(1,),2:(),3:(),**{i:(i,) for i in range(4,12)}}
assert all(substitute(w,retract)==() for w in actual_relators)
assert substitute(branch,retract)==(1,)
assert all(substitute((i,),retract)==(i,) for i in range(4,12))

out={'status':'PASS_EXACT_INDEX_TWO_SCHREIER_PRESENTATION_AND_MARKING',
     'recorded_at':datetime.now(timezone.utc).isoformat(),
     'old_generators':['h','k','V1','V2','V3','V4'],
     'old_complete_relators':old_relators,
     'new_generators':new_names,
     'new_to_old_words':back,
     'all_relator_and_transversal_checks':checks,
     'graph_vertices':11,'graph_edges':expected_edges,'connected_tree':True,
     'actual_retained_branch_f_squared':branch,
     'actual_branch_formula':'f^2=k1^-1 t k0^-1, not t',
     'all_four_f_conjugate_leaf_checks':leaf_checks,
     'retraction_to_actual_free_nine_neck':'PASS all10 relators and all9 section generators',
     'structural_scope':'The exact subgroup identification L=<K,k> in the actual R is supplied by the invariant-color proof; this computation independently checks its complete finite-index rewriting and the actual marking.',
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'records/neck_base_schreier24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all10 relator/transversal rewrites and inverse exact free-word substitutions')
print('PASS all11 Schreier generators and the connected eleven-vertex ten-edge tree')
print('PASS f^2=k1^-1 t k0^-1 and all four actual f-conjugated leaf words')
print('PASS retraction to the actual free-nine neck: all10 relations and all9 section generators')

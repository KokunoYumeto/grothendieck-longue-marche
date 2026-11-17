#!/usr/bin/env python3
"""Independent beta33 conjugacy proof using one cone relator, not a word oracle."""
from pathlib import Path
import json
import hashlib

ROOT = Path(__file__).resolve().parents[2]
paths = [ROOT / 'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
         ROOT / 'records/inner_bad_normalized22.json',
         ROOT / 'records/inner_bad_hnn22.json']
D, N, H = [json.loads(p.read_text()) for p in paths]

def red(word):
    out = []
    for x in word:
        x = 2 if abs(x) == 2 else int(x)
        if out and (out[-1] == -x or out[-1] == x == 2):
            out.pop()
        else:
            out.append(x)
    return tuple(out)

def inv(word): return red(-x for x in reversed(word))
def mul(*words): return red(x for word in words for x in word)
def sub(word, images):
    return mul(*(images[abs(x)] if x > 0 else inv(images[-x]) for x in word))
def comm(x, y): return mul(x, y, inv(x), inv(y))

q0 = D['loops'][0]
assert q0['name'] == 'q0'
loop = next(l for l in D['loops'] if l['name'] == 'beta_33')
assert len(loop['nodes']) == 1
operator = {int(k): tuple(v) for k, v in q0['negative_pull'].items()}
first = {int(k): tuple(v) for k, v in N['old_in_new'].items()}
second = {j: (j,) for j in range(1, 7)}
second[6] = tuple(H['branch_f_in_new_generators'])
image = sub(sub(sub(loop['nodes'][0]['relation'], operator), first), second)

a, c, b, e, w, p = [(j,) for j in (1, 2, 3, 5, 6, 7)]
block = (1, 2, 1, 2, -1, 2, -1)
cone_relator = comm(a, mul(c, a, c))
assert mul(block, c) == cone_relator

def displayed(v):
    return mul(a, inv(b), e, e,
               w, v, inv(w), e,
               w, v, inv(w), inv(e),
               w, v, inv(w), inv(e),
               w, v, inv(w), inv(e), b, inv(a))

assert image == displayed(block)
after_one_cone_relation = displayed(c)
substitute_e = {j: (j,) for j in range(1, 9)}
substitute_e[5] = mul(w, p, inv(w))
expanded = sub(after_one_cone_relation, substitute_e)
bar_p = mul(c, p, c)
conjugator = mul(a, inv(b), w, p)
target = mul(conjugator, comm(p, bar_p), inv(conjugator))
assert expanded == target

vertices = {tuple(v) for v in H['base_vertices']}
edges = {frozenset(map(tuple, edge)) for edge in H['base_edges']}
assert (7, 0) in vertices and (7, 1) in vertices
assert frozenset(((7, 0), (7, 1))) not in edges
kept = {(7, 0), (7, 1)}
assert all(not kept.issubset(edge) for edge in edges)

out = {
    'status': 'PASS',
    'inputs_sha256': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in paths},
    'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'actual_negative_q0_image_beta33': image,
    'repeated_block': block,
    'literal_identity_block_times_c': cone_relator,
    'after_using_only_a_cone_relation': after_one_cone_relation,
    'edge_identity_used': 'e=w p w^-1',
    'conjugator': conjugator,
    'commutator': comm(p, bar_p),
    'literal_conjugate_after_edge_substitution': target,
    'separating_retraction': 'Gamma -> F(p,bar p), kill every other vertex',
    'nontrivial_free_word': ['p', 'bar p', 'p^-1', 'bar p^-1'],
    'conclusion': 'The actual annular filling kills a nontrivial conjugate of [p,bar p] from the slit group.',
    'scope': 'One exact obstruction to the slit-to-annulus injection; no claim about the full annular centralizer.'
}
(ROOT / 'work_A/review_q0_beta33_witness22.json').write_text(json.dumps(out, indent=2) + '\n')
print('PASS actual negative beta33 word has the four printed repeated blocks.')
print('PASS each repeated block equals c using precisely [a,cac]=1.')
print('PASS e=w p w^-1 gives literal conjugacy by a b^-1 w p to [p,cpc].')
print('PASS p and bar p are nonadjacent: coordinate retraction onto their free group.')
print('CONCLUSION [p,bar p] is nontrivial in the HNN base and killed by the annular map.')

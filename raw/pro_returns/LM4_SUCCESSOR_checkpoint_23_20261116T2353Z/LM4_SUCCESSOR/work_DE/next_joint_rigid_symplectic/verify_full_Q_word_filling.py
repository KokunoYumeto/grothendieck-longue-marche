"""Exact finite certificate for B68, independently of the Whitehead search.

Recompute the braid from the original common-base eleven-strand words;
verify the Birman fiber word and the six specified free automorphisms;
verify connectivity after deleting each Whitehead vertex.  The geometric
implication is stated separately in B_Q_filling.tex, using the published
separable-set cut-vertex lemma and Kra's point-pushing theorem.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent

def red(w):
    z = []
    for a in w:
        if z and z[-1] == -a:
            z.pop()
        else:
            z.append(a)
    return tuple(z)

def inv(w):
    return tuple(-a for a in reversed(w))

def mul(*words):
    return red(a for w in words for a in w)

def sub(w, images):
    return mul(*(images[a] if a > 0 else inv(images[-a]) for a in w))

def artin(w, n):
    result = [(i,) for i in range(1, n + 1)]
    for a in w:
        k = abs(a) - 1
        x, y = result[k:k+2]
        if a > 0:
            result[k:k+2] = [mul(x, y, inv(x)), x]
        else:
            result[k:k+2] = [y, mul(inv(y), x, y)]
    return tuple(result)

def delete(w, labels, retained):
    labels = list(labels)
    result = []
    for a in w:
        k = abs(a) - 1
        if labels[k] in retained and labels[k+1] in retained:
            b = 1 + sum(x in retained for x in labels[:k])
            result.append(b if a > 0 else -b)
        labels[k], labels[k+1] = labels[k+1], labels[k]
    return red(result), labels

def cyclic(w):
    w = red(w)
    while len(w) > 1 and w[0] == -w[-1]:
        w = w[1:-1]
    return w

def last_conjugator(w, n):
    v = list(artin(w, n)[-1])
    q = []
    while len(v) > 1:
        assert v[0] == -v[-1]
        q.append(v.pop(0))
        v.pop()
    assert v == [n]
    return red(a for a in q if abs(a) != n)

source = (-5,-1,6,1,5,3,-5,-1,-6,1,5,-3)
data = json.loads((HERE.parent/'next_B59_image/common_base_braid_words.json').read_text())
order = data['initial_order_labels']
retained = {1,4,5,6,10,11}
old = [a for a in order if a in retained]
assert old == [4,11,5,1,10,6]
images = {}
for i, b in data['C5'].items():
    images[int(i)+1], end = delete(b, order, retained)
    assert end == order
braid = sub(source, images)
assert len(braid) == 166
five, end = delete(braid, old, retained-{5})
assert end == old and artin(five, 5) == tuple((i,) for i in range(1,6))
tau = (3,4,5)
last_braid = mul(inv(tau), braid, tau)
new = [4,11,1,10,6,5]
last_deleted, end = delete(last_braid, new, retained-{5})
assert end == new and artin(last_deleted,5) == tuple((i,) for i in range(1,6))
p = last_conjugator(last_braid,6)
saved = json.loads((HERE/'full_Q_word_Whitehead_certificate.json').read_text())
assert p == tuple(saved['fiber_word']) and len(p) == 144
assert len(cyclic(p)) == 142
print('Original common-base words -> PB6 length 166 -> last-strand Birman kernel: PASS')
print('Recomputed fiber conjugator length 144; cyclic length 142: PASS')

# The standard A_(i,6) form a free basis of the Birman kernel.  Their
# extracted words have a triangular free-basis change, and extraction
# reverses multiplication.  This checks the conventions on actual braids.
standard = {}
standard_push = {}
for i in range(1,6):
    tail = tuple(range(5,i,-1))
    standard[i] = mul(tail,(i,i),inv(tail))
    standard_push[i] = last_conjugator(standard[i],6)
    u = tuple(range(i+1,6))
    assert standard_push[i] == mul(inv(u),(i,),u)
for i in range(1,6):
    for j in range(1,6):
        assert last_conjugator(mul(standard[i],standard[j]),6) == mul(standard_push[j],standard_push[i])
print('All five canonical fiber meridians have the triangular basis images; 25 antihomomorphism checks: PASS')

steps = [(3,[-5,-4,3,4,5]), (2,[-5,-4,2,4,5]), (1,[-4,1]),
         (5,[-3,-2,2,3,5]), (4,[-3,-2,2,4]), (5,[-2,5])]
expected_lengths = [98,62,48,34,26,24]

def whitehead(a, A):
    A = set(A)
    assert a in A and -a not in A
    return {x: (x,) if x == abs(a) else
            ((-a,) if -x in A else ())+(x,)+((a,) if x in A else ())
            for x in range(1,6)}

v = cyclic(p)
records = []
for k, ((a,A), expected) in enumerate(zip(steps,expected_lengths),1):
    phi = whitehead(a,A)
    psi = whitehead(-a,(set(A)-{a})|{-a})
    for x in range(1,6):
        assert sub(phi[x],psi) == (x,) and sub(psi[x],phi) == (x,)
    v = cyclic(sub(v,phi))
    assert len(v) == expected
    assert v == tuple(saved['Whitehead_reductions'][k-1]['word'])
    records.append({'multiplier':a,'set':A,'images':phi,'inverse_images':psi,
                    'cyclic_word':v})
    print('Whitehead step',k,': both inverse compositions verified; cyclic length',len(v))

expected_final = (4,-1,-4,-3,5,-2,4,2,5,-2,-4,2,-5,3,1,-3,-2,5,4,-5,-4,-5,2,3)
assert v == expected_final
vertices = set(range(-5,0))|set(range(1,6))
# This is the global sign reversal of Heusener--Weidmann's convention.
edges = sorted(set(tuple(sorted((-a,b))) for a,b in zip(v,v[1:]+v[:1])))
assert all(a != b for a,b in edges)

def tree_without(removed):
    todo_vertices = vertices - ({removed} if removed else set())
    start = min(todo_vertices)
    reached = {start}
    queue = [start]
    tree = []
    while queue:
        x = queue.pop(0)
        for a,b in edges:
            y = b if a == x else a if b == x else None
            if y in todo_vertices and y not in reached:
                reached.add(y)
                queue.append(y)
                tree.append((x,y))
    assert reached == todo_vertices
    return tree

trees = {str(x):tree_without(x) for x in [0]+sorted(vertices)}
assert len(trees['0']) == 9 and all(len(trees[str(x)]) == 8 for x in vertices)
print('Whitehead graph: 10 vertices,',len(edges),'edges; connected and connected after each of 10 vertex deletions: PASS')
print('Final cyclic word:',v)
print('PASS finite algebraic certificate; filling/pseudo-Anosov implication uses the separately cited theorems')
(HERE/'full_Q_word_filling_verification.json').write_text(json.dumps({
    'source_word':source,'old_order':old,'new_order':new,'transport':tau,
    'six_strand_braid':braid,'last_strand_braid':last_braid,'fiber_word':p,
    'homomorphic_fiber_word':inv(p),'canonical_fiber_braids':standard,
    'canonical_extracted_words':standard_push,'Whitehead_steps':records,
    'final_word':v,'Whitehead_edges':edges,'connectivity_spanning_trees':trees,
    'graph_convention':'Edges (-x_i,x_(i+1)), globally sign-reversed from Heusener--Weidmann',
    'proof_scope':'Exact algebraic certificate; topological inference is separately justified in B_Q_filling.tex'
},indent=2)+'\n')

#!/usr/bin/env python3
"""Check the marked index-nine Bass--Serre graph used in D45 transport.

The infinite torsion-conjugacy assertion is proved in the paper using
Herfort--Ribes A'; this program checks its actual finite graph and marking.
"""
from collections import deque
from itertools import permutations
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
one = ((0, 1, 2), 0)
s = ((1, 0, 2), 0)
r = ((1, 2, 0), 1)

def mul(a, b):
    return (tuple(a[0][b[0][i]] for i in range(3)), (a[1] + b[1]) % 3)

def inv(a):
    p = tuple(a[0].index(i) for i in range(3))
    return (p, -a[1] % 3)

group = set((p, j) for p in permutations(range(3)) for j in range(3))
words = {one: []}
queue = deque([one])
while queue:
    g = queue.popleft()
    for letter, image in [(0, s), (1, r)]:
        h = mul(g, image)
        if h not in words:
            words[h] = words[g] + [letter]
            queue.append(h)
assert set(words) == group
assert mul(s, s) == one and mul(mul(r, r), r) == one
H = {one, s}
cosets = sorted({frozenset(mul(h, q) for h in H) for q in group}, key=lambda c: sorted(c))
index = {q: i for i, c in enumerate(cosets) for q in c}
transversals = [min(c, key=lambda q: (len(words[q]), words[q])) for c in cosets]
actions = [[index[mul(q, g)] for q in transversals] for g in [s, r]]

def cycles(p):
    unseen = set(range(len(p)))
    result = []
    while unseen:
        start = min(unseen)
        cycle, q = [], start
        while q in unseen:
            unseen.remove(q)
            cycle.append(q)
            q = p[q]
        assert q == start
        result.append(cycle)
    return result

sc, rc = map(cycles, actions)
fixed_s = [c[0] for c in sc if len(c) == 1]
fixed_r = [c[0] for c in rc if len(c) == 1]
assert len(cosets) == 9
assert sorted(map(len, sc)) == [1, 1, 1, 2, 2, 2]
assert sorted(map(len, rc)) == [3, 3, 3]
assert len(cosets) - len(sc) - len(rc) + 1 == 1
factor_markings = []
for i in fixed_s:
    q = transversals[i]
    assert mul(mul(q, s), inv(q)) == s
    word = words[q]
    inverse_word = [0 if a == 0 else 2 for a in reversed(word)]
    factor_markings.append({"coset": i, "conjugator_B_word": word,
                            "factor_generator_B_word": word + [0] + inverse_word,
                            "Q0_image": s})

data = {"status": "PASS", "marked_Q0_order": len(group),
        "subgroup_order": len(H), "cosets": [sorted(c) for c in cosets],
        "s_action": actions[0], "r_action": actions[1],
        "s_cycles": sc, "r_cycles": rc,
        "s_fixed_cosets": fixed_s, "r_fixed_cosets": fixed_r,
        "Bass_Serre_edges": 9, "s_vertices": len(sc), "r_vertices": len(rc),
        "graph_free_rank": 1, "order_two_vertex_factors": factor_markings,
        "discrete_preimage": "C2 * C2 * C2 * Z",
        "K_index_in_preimage": 2,
        "scope": "Finite marked coset graph only; the pro2 comparison and torsion transport are proved in D45 supplement."}
(OUT / 'verify_torsion_bridge.json').write_text(json.dumps(data, indent=2) + '\n')
print(json.dumps({k: data[k] for k in ['status', 'marked_Q0_order', 'subgroup_order',
      's_cycles', 'r_cycles', 'graph_free_rank', 'discrete_preimage', 'K_index_in_preimage']}, indent=2))

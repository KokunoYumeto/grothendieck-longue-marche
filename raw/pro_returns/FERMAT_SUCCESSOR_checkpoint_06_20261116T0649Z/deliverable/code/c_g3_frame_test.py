"""First relative homology tests for the E.58 and D.46 frames.

Build the actual Q576 Bass--Serre graph directly from modular matrices.
For G_p = B/[N,N]N^p, a lift a of a quotient element centralizing c
can be corrected to centralize c iff [a,c] lies in (c-1) H_1(N,F_p).
All cosets are tested, not a choice of convenient frame representatives.
"""
from collections import deque
import json
from pathlib import Path


def canon(a):
    a = tuple(z % 12 for z in a)
    return min(a, tuple(-z % 12 for z in a))


def multiply(a, b):
    return canon(tuple(sum(a[2*i+k] * b[2*k+j] for k in range(2)) for i in range(2) for j in range(2)))


identity = (1, 0, 0, 1)
s0 = canon((0, 1, -1, 0))
r0 = canon((0, -1, 1, -1))
words = {identity: ()}
queue = deque([identity])
while queue:
    q = queue.popleft()
    for letter, generator in ((0, s0), (1, r0)):
        t = multiply(q, generator)
        if t not in words:
            words[t] = words[q] + (letter,)
            queue.append(t)
qgroup = sorted(words)
assert len(qgroup) == 576
index = {q: j for j, q in enumerate(qgroup)}
table = [[index[multiply(a, b)] for b in qgroup] for a in qgroup]
e, s, r = map(index.__getitem__, (identity, s0, r0))
rs = [table[q][s] for q in range(576)]
rr = [table[q][r] for q in range(576)]
rr2 = [rr[rr[q]] for q in range(576)]
v2 = [(0, min(q, rs[q])) for q in range(576)]
v3 = [(1, min(q, rr[q], rr2[q])) for q in range(576)]
adj = {v: [] for v in set(v2 + v3)}
for q in range(576):
    adj[v2[q]].append((v3[q], q, 1))
    adj[v3[q]].append((v2[q], q, -1))
paths = {v2[e]: {}}
queue = deque([v2[e]])
tree = set()
while queue:
    v = queue.popleft()
    for w, edge, sign in adj[v]:
        if w not in paths:
            path = dict(paths[v])
            path[edge] = path.get(edge, 0) + sign
            paths[w] = path
            tree.add(edge)
            queue.append(w)
chords = [q for q in range(576) if q not in tree]
assert len(chords) == 97
chord_index = {q: j for j, q in enumerate(chords)}
cycles = []
for edge in chords:
    cycle = dict(paths[v2[edge]])
    cycle[edge] = cycle.get(edge, 0) + 1
    for q, weight in paths[v3[edge]].items():
        cycle[q] = cycle.get(q, 0) - weight
    cycles.append({q: weight for q, weight in cycle.items() if weight})
for j, cycle in enumerate(cycles):
    assert [cycle.get(edge, 0) for edge in chords] == [int(j == k) for k in range(97)]


def inverse_word(word):
    return tuple(0 if letter == 0 else 3-letter for letter in reversed(word))


def evaluate(word, prime):
    q = e
    vector = [0] * 97
    for letter in word:
        if letter == 0:
            q = rs[q]
        else:
            nxt = rr[q] if letter == 1 else rr2[q]
            if q in chord_index:
                j = chord_index[q]
                vector[j] = (vector[j] + 1) % prime
            if nxt in chord_index:
                j = chord_index[nxt]
                vector[j] = (vector[j] - 1) % prime
            q = nxt
    return q, vector


def action(q, prime):
    columns = []
    for cycle in cycles:
        translated = {table[q][edge]: weight for edge, weight in cycle.items()}
        columns.append([translated.get(edge, 0) % prime for edge in chords])
    return columns


def solver(columns, prime):
    pivots = {}
    for vector in columns:
        vector = vector[:]
        for k in range(97):
            if not vector[k]:
                continue
            if k in pivots:
                scale = vector[k]
                vector = [(a-scale*b) % prime for a, b in zip(vector, pivots[k])]
            else:
                scale = pow(vector[k], -1, prime)
                pivots[k] = [scale*a % prime for a in vector]
                break
    def reduce(vector):
        vector = vector[:]
        for k in sorted(pivots):
            if vector[k]:
                scale = vector[k]
                vector = [(a-scale*b) % prime for a, b in zip(vector, pivots[k])]
        return vector
    return pivots, reduce


records = []
for name, c, cword, prime in (("r", r, (1,), 3), ("r", r, (1,), 2), ("s", s, (0,), 2), ("s", s, (0,), 3)):
    columns = action(c, prime)
    difference = [[(value-int(j == k)) % prime for k, value in enumerate(column)] for j, column in enumerate(columns)]
    pivots, reduce = solver(difference, prime)
    centralizer = [q for q in range(576) if table[q][c] == table[c][q]]
    image = []
    failures = {}
    for q in centralizer:
        a = words[qgroup[q]]
        endpoint, defect = evaluate(a + cword + inverse_word(a) + inverse_word(cword), prime)
        assert endpoint == e
        remainder = reduce(defect)
        if not any(remainder):
            image.append(q)
        else:
            failures[str(q)] = remainder
    result = {"peripheral": name, "prime": prime, "correction_rank": len(pivots),
              "quotient_centralizer_order": len(centralizer), "liftable_image_order": len(image),
              "liftable_matrices": [qgroup[q] for q in image], "nonzero_remainders": failures}
    records.append(result)
    print(name, "prime", prime, "centralizer order", len(centralizer),
          "liftable image order", len(image), "correction rank", len(pivots))

z0 = canon((5, 0, 0, 5))
assert z0 in words
by_key = {(row["peripheral"], row["prime"]): row for row in records}
z3 = z0 in by_key[("r", 3)]["liftable_matrices"]
z2 = z0 in by_key[("r", 2)]["liftable_matrices"]
print("E.58 cubic frame 5I centralizes r after a G3 correction:", z3)
print("E.58 cubic frame 5I centralizes r after a G2 correction:", z2)
gaussian = [q for q in qgroup if tuple(z % 4 for z in q) in (identity, (3, 0, 0, 3))
            and tuple(z % 3 for z in q) in ((0, 1, 2, 0), (0, 2, 1, 0))]
assert len(gaussian) == 2
gaussian2 = [q in by_key[("s", 2)]["liftable_matrices"] for q in gaussian]
print("D.46 two possible positive Gaussian [i] frames:", gaussian)
print("G2 centralizing lifts for these frames:", gaussian2)
assert not z3 and z2
assert gaussian2 == [False, False]
summary = {"rank": 97, "E58_G2_identity_compatible": z2,
           "E58_G3_identity_impossible": not z3,
           "D46_G2_identity_impossible": not any(gaussian2),
           "scope": "Necessary relative homology conditions; this does not specify all entries of either full action or prove a Galois comparison."}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps({"summary": summary, "records": records}, indent=2) + "\n")
print(json.dumps(summary, indent=2))

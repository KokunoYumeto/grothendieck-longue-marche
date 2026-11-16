"""Recover the S5 action on the 542 objects of the cote 148 five-point diagram from the coset representatives in
b_diagram.json: find, for each vertex type, the subgroup H and the coset convention under which the given
representatives are canonical; then build the permutation of vertices for any g in S5."""
import json, itertools, collections, pickle
j = json.load(open('src_exit_tower_cp28/code/b_diagram.json', encoding='utf-8'))
V, E = j['vertices'], j['edges']
S5 = list(itertools.permutations(range(5)))
def mul(a, b):  # (a*b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(5))
def inv(a):
    r = [0]*5
    for i, x in enumerate(a): r[x] = i
    return tuple(r)
def closure(gens):
    G = {tuple(range(5))}; frontier = list(G)
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = mul(x, g)
                if y not in G: G.add(y); new.append(y)
        frontier = new
    return frozenset(G)
subs = set()
for a in S5:
    subs.add(closure([a]))
for a, b in itertools.combinations(S5, 2):
    subs.add(closure([a, b]))
bysize = collections.defaultdict(list)
for H in subs: bysize[len(H)].append(H)
print({k: len(v) for k, v in sorted(bysize.items())})
reps = collections.defaultdict(list)
for idx, (t, c) in enumerate(V): reps[t].append((tuple(c), idx))
conventions = {
 'left_min':  lambda s, H: min(mul(s, h) for h in H),
 'right_min': lambda s, H: min(mul(h, s) for h in H),
 'left_min_inv':  lambda s, H: min(inv(mul(s, h)) for h in H),
 'right_min_inv': lambda s, H: min(inv(mul(h, s)) for h in H),
}
found = {}
for t, lst in reps.items():
    R = {c for c, _ in lst}; order = 120 // len(R)
    hits = []
    for H in bysize[order]:
        for name, f in conventions.items():
            if {f(s, H) for s in S5} == R: hits.append((name, sorted(H)))
    print(t, 'size', len(R), '|H|', order, 'matches', len(hits), [h[0] for h in hits][:6])
    found[t] = hits
pickle.dump(found, open('tools/s5_found.pkl', 'wb'))

import json, itertools, collections, pickle
exec(open('tools/s5_action.py').read().split("subs = set()")[0])  # reuse helpers: mul, inv, closure, V, E
found = pickle.load(open('tools/s5_found.pkl', 'rb'))
cands = {t: [frozenset(map(tuple, H)) for name, H in hits if name == 'left_min'] for t, hits in found.items()}
cands = {t: list(dict.fromkeys(v)) for t, v in cands.items()}
print({t: len(v) for t, v in cands.items()})
index = {(t, tuple(c)): i for i, (t, c) in enumerate(V)}
types = [t for t, _ in V]
def act(g, i, H):
    t, c = V[i]
    return index[(t, min(mul(mul(g, tuple(c)), h) for h in H))]
gens = [(1, 0, 2, 3, 4), (1, 2, 3, 4, 0)]
fams = collections.defaultdict(list)
for e in E: fams[e['family']].append((e['source'], e['target']))
ok_pairs = {}
for f, lst in fams.items():
    T1, T2 = types[lst[0][0]], types[lst[0][1]]
    ms = collections.Counter(lst); good = []
    for H1 in cands[T1]:
        for H2 in cands[T2]:
            if T1 == T2 and H1 != H2: continue
            if all(collections.Counter((act(g, s, H1), act(g, t, H2)) for s, t in lst) == ms for g in gens):
                good.append((cands[T1].index(H1), cands[T2].index(H2)))
    ok_pairs[f] = (T1, T2, good); print(f, T1, '->', T2, good)
# solve: choose an index per type consistent with all families
ts = sorted(cands)
sols = []
for choice in itertools.product(*[range(len(cands[t])) for t in ts]):
    ch = dict(zip(ts, choice))
    if all((ch[T1], ch[T2]) in good for T1, T2, good in ok_pairs.values()): sols.append(ch)
print('solutions', len(sols), sols[:4])
if sols:
    H = {t: cands[t][sols[0][t]] for t in ts}
    pickle.dump({t: sorted(h) for t, h in H.items()}, open('tools/s5_H.pkl', 'wb'))
    for t in ts: print(t, sorted(H[t]))

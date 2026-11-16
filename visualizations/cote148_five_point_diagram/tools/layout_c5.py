"""D5-symmetric 3D layout of the 542-object diagram: project the lowest eigenspace of the graph Laplacian in which no
object type collapses (a 5-dimensional S5-irreducible) onto the fixed line and the 72-degree rotation plane of the
5-cycle i -> i+1. Writes layout_c5.json (positions, types, edges with families)."""
import json, itertools, collections, pickle, numpy as np
exec(open('tools/s5_action.py').read().split("subs = set()")[0])
Hs = {t: [tuple(h) for h in H] for t, H in pickle.load(open('tools/s5_H.pkl', 'rb')).items()}
index = {(t, tuple(c)): i for i, (t, c) in enumerate(V)}
n = len(V)
def perm(g):
    return [index[(t, min(mul(mul(g, tuple(c)), h) for h in Hs[t]))] for t, c in V]
# check: the whole S5 acts by automorphisms preserving families
ms = collections.Counter((e['family'], e['source'], e['target']) for e in E)
bad = 0
for g in itertools.permutations(range(5)):
    p = perm(g)
    if collections.Counter((f, p[s], p[t]) for (f, s, t) in ms.elements()) != ms: bad += 1
print('S5 elements failing to preserve the typed edge multiset:', bad)
w = np.load('tools/spec_w.npy'); U = np.load('tools/spec_U.npy')
# eigenspace 2 = indices 5..9 (after 0 and the 4-dim one)
E2 = U[:, 5:10]; print('eigenvalues used', np.round(w[5:10], 6))
g5 = (1, 2, 3, 4, 0); p = perm(g5)
P = np.zeros((n, n)); P[p, range(n)] = 1          # P e_i = e_{p(i)}
R = E2.T @ P @ E2                                  # 5x5 orthogonal
print('R orthogonal err', np.abs(R @ R.T - np.eye(5)).max())
ev, evec = np.linalg.eig(R)
print('eigenvalues of the 5-cycle:', np.round(ev, 4), 'angles(deg):', np.round(np.degrees(np.angle(ev)), 1))
fix = np.real(evec[:, np.argmin(np.abs(ev - 1))]); fix /= np.linalg.norm(fix)
k72 = np.argmin(np.abs(np.angle(ev) - np.radians(72)))
a = np.real(evec[:, k72]); b = np.imag(evec[:, k72]); a /= np.linalg.norm(a); b -= a * (a @ b); b /= np.linalg.norm(b)
k144 = np.argmin(np.abs(np.angle(ev) - np.radians(144)))
c = np.real(evec[:, k144]); d = np.imag(evec[:, k144]); c /= np.linalg.norm(c); d -= c * (c @ d); d /= np.linalg.norm(d)
X = E2 @ np.stack([a, b, fix], 1)       # 3D
X2 = E2 @ np.stack([c, d, fix], 1)      # alternative: 144-degree plane (pentagram view)
X /= np.abs(X).max(); X2 /= np.abs(X2).max()
print('distinct 3D positions', len({tuple(np.round(r, 5)) for r in X}), len({tuple(np.round(r, 5)) for r in X2}))
types = [t for t, _ in V]
for t in sorted(set(types)):
    idx = [i for i in range(n) if types[i] == t]
    print(t, 'mean radius xy %.3f  z range %.3f..%.3f' % (np.mean(np.hypot(X[idx,0], X[idx,1])), X[idx,2].min(), X[idx,2].max()))
out = {'positions_72': X.round(5).tolist(), 'positions_144': X2.round(5).tolist(), 'types': types,
       'cosets': [c for _, c in V],
       'edges': [[e['family'], e['source'], e['target']] for e in E]}
json.dump(out, open('layout_c5.json', 'w'))

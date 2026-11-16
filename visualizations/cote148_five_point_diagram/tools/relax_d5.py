"""D5-equivariant force-directed relaxation (Fruchterman-Reingold in 3D) of the spectral layout; after each step the
positions are averaged over the ten symmetries, so the result keeps exact 5-fold rotational and reflection symmetry."""
import json, itertools, pickle, numpy as np, sys
exec(open('tools/s5_action.py').read().split("subs = set()")[0])
Hs = {t: [tuple(h) for h in H] for t, H in pickle.load(open('tools/s5_H.pkl', 'rb')).items()}
index = {(t, tuple(c)): i for i, (t, c) in enumerate(V)}
n = len(V)
def perm(g): return np.array([index[(t, min(mul(mul(g, tuple(c)), h) for h in Hs[t]))] for t, c in V])
w = np.load('tools/spec_w.npy'); U = np.load('tools/spec_U.npy'); E2 = U[:, 5:10]
L = json.load(open('layout_c5.json')); X = np.array(L['positions_72'])
# D5 = stabilizer of the I10 object with coset identity
D5 = [tuple(h) for h in Hs['I10']]
# 3x3 matrices: least squares M with X[p(i)] = M X[i]
mats = []
for g in D5:
    p = perm(g); M, *_ = np.linalg.lstsq(X, X[p], rcond=None); M = M.T
    err = np.abs(X[p] - X @ M.T).max(); mats.append((p, M)); assert err < 1e-4, err
print('D5 acts on the 3D layout by orthogonal maps; dets', sorted(round(float(np.linalg.det(M)), 3) for _, M in mats))
def symmetrize(X):
    Y = np.zeros_like(X)
    for p, M in mats: Y += X[p] @ M     # M^{-1} = M^T for orthogonal M; X[p] @ M == (M^T X[p]^T)^T
    return Y / len(mats)
edges = np.array([[s, t] for f, s, t in L['edges']])
types = L['types']
rng = np.random.default_rng(1)
X = X * 3.0 + rng.normal(scale=1e-3, size=X.shape); X = symmetrize(X)
k = float(sys.argv[1]) if len(sys.argv) > 1 else 0.12
iters = int(sys.argv[2]) if len(sys.argv) > 2 else 600
T = 0.08
for it in range(iters):
    D = X[:, None, :] - X[None, :, :]; d = np.linalg.norm(D, axis=2) + 1e-9
    F = (D / d[..., None] * (k * k / d)[..., None]).sum(1)                  # repulsion
    ev = X[edges[:, 0]] - X[edges[:, 1]]; de = np.linalg.norm(ev, axis=1) + 1e-9
    fa = ev / de[:, None] * (de * de / k)[:, None]
    np.add.at(F, edges[:, 0], -fa); np.add.at(F, edges[:, 1], fa)       # attraction
    F -= 0.02 * X                                                         # mild gravity
    step = np.linalg.norm(F, axis=1, keepdims=True) + 1e-9
    X = X + F / step * np.minimum(step, T)
    X = symmetrize(X)
    T *= 0.994
mind = np.sort(np.linalg.norm(X[:, None] - X[None], axis=2) + np.eye(n) * 9, axis=1)[:, 0]
print('min pair distance %.4f, median nearest %.4f' % (mind.min(), np.median(mind)))
X -= X.mean(0); X /= np.abs(X).max()
L['positions_relaxed'] = X.round(5).tolist(); json.dump(L, open('layout_c5.json', 'w'))

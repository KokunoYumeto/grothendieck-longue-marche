import json, numpy as np, collections
j = json.load(open('src_exit_tower_cp28/code/b_diagram.json', encoding='utf-8'))
V, E = j['vertices'], j['edges']
n = len(V)
A = np.zeros((n, n))
for e in E:
    s, t = e['source'], e['target']; A[s, t] += 1; A[t, s] += 1
L = np.diag(A.sum(1)) - A
w, U = np.linalg.eigh(L)
# group eigenvalues into eigenspaces
groups = []; i = 0
while i < n:
    k = i
    while k + 1 < n and abs(w[k+1] - w[i]) < 1e-7: k += 1
    groups.append((round(w[i], 6), k - i + 1, i)); i = k + 1
print('connected components:', sum(1 for x in w if abs(x) < 1e-9))
print('first 14 eigenspaces (eigenvalue, multiplicity):', [(g[0], g[1]) for g in groups[:14]])
print('number of distinct eigenvalues', len(groups))
np.save('tools/spec_w.npy', w); np.save('tools/spec_U.npy', U)

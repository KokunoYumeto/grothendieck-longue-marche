import json, sys, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
L = json.load(open(sys.argv[1])); key = sys.argv[2]; out = sys.argv[3]
X = np.array(L[key]); types = L['types']; edges = L['edges']
fams = sorted({e[0] for e in edges}); cmap = plt.get_cmap('tab20')
fc = {f: cmap(i % 20) for i, f in enumerate(fams)}
tcol = {'I10': '#ffd23f', 'I6': '#ff6b6b', 'I4': '#4ecdc4', 'II2': '#c77dff', 'IIp2': '#9d4edd', 'II1': '#7b2cbf',
        'III2': '#90e0ef', 'III1': '#48cae4', 'IIIp2': '#0096c7'}
fig, axs = plt.subplots(1, 2, figsize=(16, 8), facecolor='#0b0d17')
for ax, (i, j, title) in zip(axs, [(0, 1, 'top view (5-fold axis)'), (0, 2, 'side view')]):
    ax.set_facecolor('#0b0d17'); ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title, color='w')
    segs = [[X[s][[i, j]], X[t][[i, j]]] for f, s, t in edges]
    ax.add_collection(LineCollection(segs, colors=[fc[f] for f, s, t in edges], linewidths=0.5, alpha=0.55))
    for t, c in tcol.items():
        idx = [k for k in range(len(types)) if types[k] == t]
        ax.scatter(X[idx, i], X[idx, j], s={'I':28,'II':10,'III':6}[t.rstrip('p0123456789')], c=c, zorder=3, label=t, edgecolors='none')
    ax.autoscale()
axs[0].legend(loc='lower left', fontsize=8, facecolor='#0b0d17', labelcolor='w', frameon=False, ncol=3)
plt.tight_layout(); plt.savefig(out, dpi=90, facecolor=fig.get_facecolor())

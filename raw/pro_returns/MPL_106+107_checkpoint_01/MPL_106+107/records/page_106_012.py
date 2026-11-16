import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{6)}
La difficulté, c'est qu'il n'est pas clair que le foncteur
\[\widetilde C\longrightarrow W^{-1}C\]
précédent soit aussi \uline{fidèle} (ce qui impliquerait que c'est une équivalence des catégories \inserted{et même un iso}). \deleted{Dans ce cas \unsure{le foncteur inverse serait forcément donné par}} \inserted{Il revient au $=$ de dire} que le foncteur can $C\longrightarrow\widetilde C$ (dont le composé avec $\widetilde C\longrightarrow W^{-1}C$ est bien le foncteur can. $C\longrightarrow W^{-1}C$) transforme flèches de $W$ en iso, ou encore que la construction qu'on vient d'\unsure{envisager}, pour \deleted{le cas} \inserted{trouver} un inverse de $[f,i]$ dans $\widetilde C$, est bien valable, \deleted{\unsure{ce que}}
Cela \unsure{entraînerait} d'ailleurs \inserted{semble-t-il,} que, \deleted{le} posant $W_0=W\cap\mathrm{cof}$, le foncteur
\[W_0^{-1}C\longrightarrow W^{-1}C\]
serait une équivalence de catégories, car
\[\widetilde C\longrightarrow W^{-1}C\]
se factorise visiblement par
\diagram{\begin{tikzcd}
\widetilde C \arrow[r] \arrow[d,phantom,"\unsure{\simeq}"] & W_0^{-1}C \arrow[r]& W^{-1}C\\
W^{-1}C&&
\end{tikzcd}}
Mais je doute qu'il suffise d'inverser les équiv. faibles \uline{cofibrantes}, pour que \unsure{ttes} les équiv. faibles deviennent inversibles !

Je rectifie donc le tir, en prenant plutôt la catégorie (notée maintenant par $\widetilde C$) ayant $\unsure{=^{\mathrm{s}}}$ objets que $C$, \deleted{\unsure{et définie ainsi par les flèches de $x\longrightarrow y$}} \inserted{et \unsure{ayant pour} les $\pi_0$ des $\uline{\mathrm{Ch}}_0(x,y)$,} \deleted{\unsure{définie maintenant}} \inserted{cette catégorie} (pour $x,y$ donnés) comme celle des diagrammes
\diagram{\begin{tikzcd}
\deleted{\unsure{x}} \arrow[r,phantom,"\deleted{\unsure{\longrightarrow}}"]&\deleted{\unsure{y}}
\end{tikzcd}}
\diagram{\begin{tikzcd}
x \arrow[dr,"f"']&y\arrow[d,"i"',"\sim"]\\
&\bar y
\end{tikzcd}}
avec $\left\{\begin{array}{l}f\in\mathrm{cof}\\i\in W\end{array}\right.$
\mspage{11}
"""
elements=[('text','upper left','6)'),('text','top','La difficulté, c’est qu’il n’est pas clair'),('display','top','tilde C → W^-1 C'),('text','upper paragraph','précédent soit aussi fidèle'),('text','middle','Cela entraînerait d’ailleurs'),('display','middle','W_0^-1 C → W^-1 C'),('text','middle','serait une équivalence de catégories, car'),('display','middle lower','tilde C → W^-1 C'),('text','middle lower','se factorise visiblement par'),('diagram','lower middle','tilde C → W_0^-1 C → W^-1 C; W^-1 C below'),('text','lower paragraph','Mais je doute qu’il suffise'),('text','bottom paragraph','Je rectifie donc le tir'),('diagram','bottom left of final roof','cancelled x → y'),('diagram','bottom right','x → bar y ← y'),('display','right of final roof','f∈cof; i∈W'),('text','foot','11')]
notes='''Explicit difficulty: “il n’est pas clair” that the comparison is faithful; an inserted “et même un iso” accompanies the equivalence claim. “semble-t-il” qualifies the implication toward W_0^-1 C→W^-1 C for W_0=W∩cof. He explicitly doubts inversion of only weak-equivalence cofibrations: “Mais je doute qu’il suffise d’inverser les équiv. faibles cofibrantes”. He changes the roof convention with “Je rectifie donc le tir”: now the forward f lies in cof and the backward i in W. This is a withdrawn/replaced construction relative to scans006–010, not a silent notation change. He reuses tilde C and Ch_0 for the revised construction. The heavily overwritten final definition has especially low-confidence syntax; preserve it as a reading question rather than derive its wording mathematically.'''
if __name__=='__main__':save(106,12,tex,elements,notes=notes)

import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{5)}
\margin{\uline{NB} On utilise $y\in\mathrm{Cof}$ $\longleftarrow$ ici}
On utilise le weak lifting \unsure{lemme|lemma} pour
\diagram{\begin{tikzcd}
\varnothing \arrow[r] \arrow[d] & x \arrow[d,"f","\sim"'] \arrow[r,dashed,hook,"i","\sim"'] & \bar x \arrow[dl,dashed,"\alpha","\sim"'] \\
y \arrow[r,"1"] & y \arrow[ur,dashed,bend right=45,"g"'] & \deleted{\unsure{\varphi}}
\end{tikzcd}}
donc il existe $i,\alpha$ avec $\alpha i=f$, \deleted{\unsure{et}} $i\in W\cap\mathrm{cof}$, et $\alpha$ admet une section $g$
\[\alpha g=1_y\]
Je dis que $(g,i)$ est l'inverse \inserted{cherché.} \deleted{$\unsure{\alpha g=\operatorname{id}_y}$}
\deleted{Considérons alors}

Pour $(gf,i)\sim\uline{1}_x$, on a envie d'utiliser le diagramme commutatif ci-contre, le seul ennui c'est que, on a $\alpha\in W$ mais pas néc. $\alpha\in\mathrm{cof}$, donc $\alpha i\ (=f)$ pas néc. dans \deleted{\unsure{W}} $\mathrm{cof}$ (alors qu'il est dans $W$).
\diagram{\begin{tikzcd}[column sep=large,row sep=small]
x \arrow[dd,"1_x"'] \arrow[dr,"gf"] \arrow[dddrr,dashed,"f" near end] & & x \arrow[dl,"i","\sim"'] \arrow[ddll,"1_x","\sim"'] \\
&\bar x \arrow[ddr,dashed,"\alpha","\sim"']&\\
x \arrow[drr,dashed,"f"'] & \deleted{\unsure{f}} &\\
&& y
\end{tikzcd}}
Ça marcherait si on pouvait trouver $y\xrightarrow[\sim]{\beta}y'$ \inserted{dans $W$,} tel que le composé $\beta f$ soit non seulement dans $W$, mais de plus, dans $\mathrm{cof}$.

Visiblement, ce n'est pas \unsure{tjs} le cas (prendre le cas où les $\mathrm{cof}$ sont les monos, et où $f$ n'est \uline{pas} un mono !). Ça se présente mal !
\diagram{\begin{tikzcd}
x \arrow[d,"f"'] \arrow[dr] &\\
y \arrow[r,"\beta"']&y'
\end{tikzcd}}
On va donc plutôt définir d'abord le foncteur canonique
\[\widetilde C\longrightarrow W^{-1}C\]
\[\unsure{\Phi|\varphi}:\quad x\longmapsto x\]
\[(f,i)\longmapsto[i]^{-1}[f]\]
il est immédiat que c'est compatible avec les identités et la composition. Donc on a bien foncteur \deleted{\unsure{injectif}} \inserted{bijectif} sur objets. Je dis que c'est surjectif sur les flèches; Il suffit de voir, par composition, que si $f:x\longrightarrow y$ est dans $W$, alors $[f]^{-1}$ provient de $\widetilde C$. On va prendre \deleted{$(y,x)$} $y\longrightarrow x$ dans $\widetilde C$, défini par $(g,i)$, \deleted{\unsure{À priori que}} $[i]^{-1}[g]$, pour prouver que $[i]^{-1}[g]=[f]^{-1}$, il suffit de prouver que $[f][i]^{-1}[g]=[\uline{1}_y]$, or $\alpha i=f$ entraîne $[\alpha][i]=[f]$ donc $[f][i]^{-1}=[\alpha]$, donc le \unsure{produit} est $[\alpha][g]=[\alpha g]=[1_y]$, OK.
\mspage{9}
"""
elements=[('text','top left','5)'),('margin note','top right','NB On utilise y∈Cof ici'),('text','top','On utilise le weak lifting lemme pour'),('diagram','upper left','initial-object square and factorization of f'),('text','upper right','donc il existe i,alpha'),('display','upper right','alpha g=1_y'),('text','under first diagram','Je dis que (g,i) est l’inverse'),('text','middle right','Pour (gf,i)~1_x, on a envie'),('diagram','middle left','x,x,x,bar x,y; gf,i,alpha,f,1_x'),('text','middle','Ça marcherait si on pouvait trouver'),('text','below middle','Visiblement, ce n’est pas tjs le cas'),('diagram','left margin lower middle','x → y → y prime'),('text','lower middle','On va donc plutôt définir'),('display','lower middle','tilde C → W^-1 C'),('display','lower middle','Phi: x ↦ x'),('display','lower middle','(f,i) ↦ [i]^-1[f]'),('text','lower paragraph','il est immédiat que c’est compatible'),('text','foot','9')]
notes='''Own explicit obstruction: “le seul ennui” is that alpha∈W need not lie in cof, so alpha i=f need not lie in cof. The attempted repair by postcomposition beta is rejected: “Visiblement, ce n’est pas tjs le cas”, taking cof to be monomorphisms and f nonmonic; “Ça se présente mal !” The approach to inverses inside pi_0 Ch_0 is thereby abandoned locally, replaced by the canonical functor tilde C→W^-1 C and a proof of surjectivity on arrows. “il est immédiat” asserts identity/composition compatibility without displaying the check. The NB explicitly notes use of y∈Cof in weak lifting. The final alpha i=f calculation is given, not merely promised. Distinguish this proved surjectivity from faithfulness, not proved on this page.'''
if __name__=='__main__':save(106,10,tex,elements,notes=notes)

import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{8})

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
x\vee x\arrow[r,hook,"\unsure{\{f_0\vee f'_0\}}"]\arrow[d,"\nabla_x"']&\bar y\amalg\bar y'\arrow[d,dashed]\arrow[drr,"(\alpha,\alpha')"]\arrow[dl,phantom,"\text{cocart}" description]&&\\
x\arrow[r,hook,dashed,"g"]\arrow[rrr,bend right=25,"f"']&\widetilde y\arrow[rr,dashed,"\varphi"']\arrow[r,hook,"\varphi_0"]&\bar y''\arrow[r,dashed,"\alpha''","\sim"']&y
\end{tikzcd}}

on factorise $\varphi$ en $\unsure{\alpha''}\varphi_0$ avec $\varphi_0\in\operatorname{cof}$, $\unsure{\alpha''}\in W$, et on prend
\[f''_0=\varphi_0 g\]

Mais si $\alpha,\alpha'$ ont des sections (il suffirait que $\alpha$ ou $\alpha'$ en ait), \deleted{\unsure{On en a donc}} \inserted{il est trivial que} \deleted{\unsure{la section de}} $\alpha''$ (qui les reçoit) en a aussi une. Donc on est ramené au cas où on a une flèche
\[u:(f_0,\alpha)\longrightarrow(f'_0,\alpha')\]
dans la catégorie des factorisations de $f$ en $\alpha f_0$. Donc \uline{Si} on choisit la section $\unsure{i''|i'}$ pour $\unsure{\alpha''|\alpha'}$ comme l'image par $u$ de la section $\unsure{i'|i''}$ de $\alpha'$ \deleted{\unsure{et}}\unsure{,} on gagne. Donc il reste à prouver que
\diagram{\begin{tikzcd}
x\arrow[rr,"f"]\arrow[dr,"f'_0"']\arrow[drr,"f''_0" description]&&y\\
&\bar y'\arrow[ur,"\alpha'"]\arrow[r,leftrightarrow,"u"']&\bar y''\arrow[u,"\alpha''"']
\end{tikzcd}}
\deleted{le choix de}
pour une factorisation choisie de $f$ en $\alpha f_0$ comme dessus, $[f_0,i]$ ne dépend pas du choix de la section $i$. Comme
\[[f_0,i]=[\operatorname{id}_{\bar y},i]\circ(f,\operatorname{id}_{\bar y}),\]
On est ramené à ceci :

$(\unsure{*})$ Soit
\diagram{\begin{tikzcd}x\arrow[r,"f","\sim"']&y\end{tikzcd}}
dans $W$, tel que $f$ ait une \deleted{\unsure{(deux $i,i'\in W$)}} section $i$, alors \deleted{\unsure{pour deux telles sections $i,i'$}} \inserted{la classe dans} \deleted{les comp. connexes dans} $\pi_0(\underline{\operatorname{Ch}}_0(x,y))$ \deleted{de} des $(1_x,i)$
\diagram{\begin{tikzcd}
\deleted{\unsure{x}}&x\arrow[dr,"1_x"']&y\arrow[d,"i"]\\
&&x
\end{tikzcd}}
ne dépend pas du choix de la section $i$.

\margin{\diagram{\begin{tikzcd}
x\arrow[r,"f^{\unsure{?}}"]\arrow[dr,"f_0"']&y\arrow[d,bend left=15,"i"]\arrow[d,bend left=45,"i'"]\\
&\bar y\arrow[u,"\alpha","\sim"']
\end{tikzcd}}}

Cette condition est (néc. et) \unsure{suffis\textsuperscript{t}} pour que $\widetilde C\longrightarrow W^{-1}C$ soit fidèle (donc un iso), comme on doit pouvoir vérifier aisément, en construisant bel et bien le foncteur cherché $C\longrightarrow\widetilde C$.

\mspage{15}
"""
elements=[('text','top left','8)'),('diagram','top centre','x vee x, bar y coproduct bar y prime, tilde y, bar y double prime, y'),('text','top right','on factorise phi'),('display','below top diagram','f0 double prime=phi0 g'),('text','upper middle','Mais si alpha alpha prime ont des sections'),('display','middle','u:(f0,alpha) to (f0 prime,alpha prime)'),('text','middle','dans la catégorie des factorisations'),('diagram','middle left','x, y, bar y prime, bar y double prime'),('text','below middle diagram','pour une factorisation choisie'),('display','lower middle','[f0,i]=[id bar y,i] circle (f,id bar y)'),('text','lower middle','On est ramené à ceci'),('text','lower statement','(*) Soit'),('diagram','lower statement first line','x to y; f sim'),('text','lower statement continued','dans W tel que f ait une section'),('display','lower statement component formula','pi0(Ch0(x,y)) des (1x,i)'),('diagram','lower statement left','x to x, y to x; 1x i'),('text','lower statement right','ne dépend pas du choix de la section i'),('diagram','left margin lower half','x,y,bar y; f,f0,alpha,i,i prime'),('text','bottom paragraph','Cette condition est (néc. et) suffis...'),('text','foot','15')]
notes='''Common domination of factorizations is drawn through a coproduct pushout followed by a cofibration/weak-equivalence factorization. The text says a common dominating weak equivalence has a section if either original one has a section, then reduces the choice issue to a marked statement (*): for a weak equivalence f:x→y with section i, the component of (1_x,i) in pi0 Ch0(x,y) is independent of i. The manuscript calls the condition necessary and sufficient for faithfulness (hence isomorphism) of tilde C→W^{-1}C, but qualifies the completion by “comme on doit pouvoir vérifier aisément, en construisant bel et bien le foncteur cherché C→tilde C.” This is a self-flagged expected verification, not a completed proof on this page. In the middle, section primes are overwritten and remain uncertain. The composition formula visibly uses (f,id_bar y), retained without replacing f by f0.'''
if __name__=='__main__':save(106,16,tex,elements,notes=notes)

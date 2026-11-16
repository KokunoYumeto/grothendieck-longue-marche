import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{2}
\diagram{\begin{tikzcd}
\tilde x \arrow[r,"\deleted{\unsure{\varphi}}"] \arrow[d,"\sim"'] \arrow[rr,bend left=22,"\varphi"] & \tilde y \arrow[r,hook,"i","\sim"'] \arrow[d,"\sim"'] \arrow[rrr,bend left=22,"\psi"] & \tilde y' \arrow[dl] & \tilde z \arrow[r,hook,"j","\sim"'] \arrow[d,"\sim"'] & \tilde z' \arrow[dl]\\
x \arrow[r,"f"'] & y \arrow[rr,"g"'] && z &
\end{tikzcd}}
\diagram{\begin{tikzcd}
\unsure{\tilde x} \arrow[dr,bend left=30] & \tilde y \arrow[d,"i"] \arrow[dr,"\psi"] & \tilde z \arrow[d,"j"]\\
&\tilde y'&\tilde z'
\end{tikzcd}}
\diagram{\begin{tikzcd}
\tilde x \arrow[r,"\deleted{\unsure{\tilde f}}"] \arrow[dr,"\tilde f"'] \arrow[ddd,dashed,"\sim"'] & \tilde y \arrow[d,"i_f"] \arrow[dr,"\tilde g"] & \tilde z \arrow[d,"i_g"]\\
& \tilde y' \arrow[dr,no head,"\deleted{\unsure{u}}\ \tilde g'"] \arrow[dd,dashed,"\sim"'] & \tilde z' \arrow[d]\\
&&\tilde z'' \arrow[d,dashed]\\
x \arrow[r,"f"'] & y \arrow[r,"g"'] & z
\end{tikzcd}}

\deleted{\unsure{En}} Montrons que ce foncteur transforme $f\in W$ en iso.
En effet, si $f\in W$, donc $f\alpha_x\in W$, on voit aussitôt qu'on aura $\tilde f\in W$, donc $[\tilde f]$ est un iso.

Considérons les deux composés
\diagram{\begin{tikzcd}
W_{\mathrm{Cof}}^{-1}\mathrm{Cof} \arrow[r,shift left=1ex,"\Psi"] & W^{-1}C \arrow[l,shift left=1ex,"\Phi"]
\end{tikzcd}}
\deleted{\unsure{faire voir}} \inserted{prouvons} qu'ils \deleted{\unsure{donnent}} sont \deleted{\unsure{égaux}} iso aux foncteurs identiques.

Pour $\Phi\Psi$, cela $\unsure{\simeq|=}$ l'identité, si on a pris soin de choisir $\tilde x\xrightarrow{\alpha_x}x$ l'identité, quand $x\in\mathrm{Cof}$.
Pour $\Psi\Phi$, il \deleted{suffit de} \inserted{\unsure{on va}} voir que le foncteur
\[
\deleted{\unsure{\Psi\Phi\overset{\mathrm{def}}{=}}}\ R\overset{\mathrm{def}}{=}\Psi\Phi\mid C
\]
\[
x\longmapsto\tilde x\qquad C\longrightarrow W^{-1}C
\]
est iso \deleted{à l'identité} \inserted{au foncteur can.}, on a
\[
\underset{\parallel\ \tilde x}{R(x)}\xrightarrow{\unsure{[\alpha_x]}}x\quad\text{dans }C\ \unsure{\text{donc}}\ \text{dans }W^{-1}C\quad(\text{soit }[\alpha_x])
\]
qui est un iso, il faut vérifier que c'est fonctoriel
\diagram{\begin{tikzcd}
\tilde x \arrow[d,"\alpha_x"'] \arrow[rr,bend left=20,"\tilde f"] & \tilde y \arrow[r,hook,"i_f"'] \arrow[d,"\alpha_y"] & \tilde y' \arrow[dl,"\beta_f"]\\
x \arrow[r,"f"'] & y &
\end{tikzcd}}
i.e. qu'on a
\[
[\alpha_y]\deleted{\unsure{\alpha}}([i_f]^{-1}\deleted{\unsure{x}}[\tilde f])=[f][\alpha_x].
\]
Mais $\alpha_y=\beta_f i_f$, d'où le premier mb est $[\beta_f\tilde f]=[f\alpha_x]=[f][\alpha_x]$ cqfd.
\mspage{3}
"""
elements=[('text','top left','2'),('diagram','top left','tilde x tilde y tilde y-prime tilde z tilde z-prime / x y z'),('diagram','top right','tilde x tilde y tilde y-prime tilde z tilde z-prime'),('diagram','upper left below','tilde x tilde y tilde z; lifted composition'),('text','upper middle','Montrons que ce foncteur transforme'),('text','middle','En effet si f en W'),('text','middle','Considérons les deux composés'),('diagram','middle','W_Cof^{-1} Cof, W^{-1} C, Psi Phi'),('text','middle below diagram','prouvons qu’ils sont iso aux foncteurs identiques'),('text','lower middle','Pour Phi Psi cela'),('text','lower middle','Pour Psi Phi il'),('display','right lower middle','R def= Psi Phi restricted C'),('display','lower middle','x mapsto tilde x; C -> W^{-1}C'),('text','lower','est iso au foncteur can.'),('display','lower','R(x) -> x; = tilde x'),('text','lower','qui est un iso, il faut vérifier'),('diagram','bottom left','tilde x tilde y tilde y-prime / x y'),('text','bottom right','i.e. qu’on a'),('display','bottom right','[alpha_y]([i_f]^{-1}[tilde f])=[f][alpha_x]'),('text','bottom','Mais alpha_y=beta_f i_f; cqfd.'),('text','foot left','3')]
notes='''The comparison between cofibrant localization and W^{-1}C is continued: images of weak equivalences are asserted invertible, and both composites are compared with identity/canonical functors. “il faut vérifier que c’est fonctoriel” is immediately followed by the square calculation and “cqfd.”, so this is a self-flagged verification discharged on this page, unlike the conditional lemma at 106/002. The sheet carries 2 at its head and 3 at its foot; preserve both without reconciling the two numbering layers.'''
if __name__=='__main__':save(106,4,tex,elements,notes=notes)

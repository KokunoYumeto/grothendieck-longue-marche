import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,158,r'''\scanpage{158}
\margin{\textcircled{\unsure{d|e}}}
\deleted{Cela \unsure{par}}

On a donc trouvé un accouplement (\unsure{donnant} : la \unsure{multiplication} à un \unsure{signe})
\[
\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F_\bullet),\mathrm{pr}_2^!(G_\bullet))\times
\mathrm{R}\mathcal{H}om(\mathrm{pr}_2^*(G_\bullet),\mathrm{pr}_1^!(F_\bullet))
\longrightarrow K_{X\times_S Y}^{\bullet}
\]
\deleted{D'où, pour $\xi^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(\unsure{\backslash})$ et $\eta^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(\unsure{\backslash})$}
\deleted{un élément $\unsure{\xi^0\cup\eta^0}$}
\deleted{$\xi^0\cup\eta^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(K_{X\times_S Y}^{\bullet})$}

Appliquant $\mathrm{R}\Gamma_{X\times_S Y}$, on trouve un accouplement
\diagram{\begin{tikzcd}[column sep=small]
\mathrm{R}\operatorname{Hom}^{\bullet}(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G))\times \arrow[d,phantom,"\simeq" description]
& \mathrm{R}\operatorname{Hom}^{\bullet}(\mathrm{pr}_2^*(G),\mathrm{pr}_1^!(F)) \arrow[r] \arrow[d,phantom,"\simeq" description]
& \mathrm{R}\Gamma_{X\times_S Y}K_{X\times_S Y}^{\bullet}\arrow[d]\\
\mathrm{R}\operatorname{Hom}^{\bullet}(\unsure{\mathrm{R}f_*}(F),\unsure{\mathrm{R}g_*}(G))\times
& \mathrm{R}\operatorname{Hom}^{\bullet}(\unsure{\mathrm{R}g_*}(G),\unsure{\mathrm{R}f_*}(F))\arrow[r]
& \deleted{\unsure{\mathrm{R}}}A_S
\end{tikzcd}}
qui ne doit être autre que l'accouplement déjà connu \unsure{relatif} ; $P_\bullet\simeq\unsure{\mathrm{pr}_{1*}|\mathrm{R}f_*}(F_\bullet)$ et $Q_\bullet\simeq\unsure{\mathrm{pr}_{2*}|\mathrm{R}g_*}(G_\bullet)$.

En particulier, si
\[
\xi^0\in\mathrm{R}^0\operatorname{Hom}^{\bullet}(\mathrm{pr}_1^*(\unsure{P|F}),\mathrm{pr}_2^!(\unsure{Q|G}))
=\mathrm{R}^0\Gamma_{X\times_S Y}\,\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G_\bullet))
\]
\[
\eta^0\in\mathrm{R}^0\operatorname{Hom}^{\bullet}(\mathrm{pr}_2^*(\unsure{Q|G}),\mathrm{pr}_1^!(F))
=\mathrm{R}^0\Gamma_{X\times_S Y}\,\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F),\mathrm{pr}_2^!(G_\bullet))
\]
alors
\[
\xi^0\cup\eta^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(K_{X\times_S Y}^{\bullet})\xrightarrow{\operatorname{Tr}_h} A.
\]
et on aura
\[
\boxed{\operatorname{Tr}(\xi^0\cup\eta^0)=\langle\xi^0,\eta^0\rangle}
\qquad
\left(=\sum_i\operatorname{Tr}(\xi^0)^{(i)}(\eta^0)^{(\unsure{-i|i})}\unsure{(-1)^i}\right)
\]
\margin{si on représente $\unsure{f_*}(P),\unsure{g_*}(Q)$ par des complexes plats de type fini en chaque degré !).}
\margin{157}
''',[
('margin note','upper left','circled d or e'),('deletion','top','Cela par'),('text','top','On a donc trouvé un accouplement'),('display','upper','RHom(pr1*F,pr2!G) times RHom'),('deletion','upper middle',"D'où, pour xi0"),('deletion','upper middle','un élément'),('deletion','upper middle','xi cup eta in R0Gamma'),('text','middle','Appliquant RGamma'),('diagram','middle','RHom pairings, R Gamma K and A_S'),('deletion','diagram lower right','overwritten letter before A_S'),('text','below diagram','qui ne doit être autre'),('text','lower','En particulier, si'),('display','lower','xi0 in R0Hom'),('display','lower','eta0 in R0Hom'),('text','lower','alors'),('display','lower','xi cup eta, Tr_h to A'),('text','bottom','et on aura'),('display','bottom framed','Tr(xi cup eta) equals pairing'),('margin note','bottom right','si on représente'),('margin note','bottom left','157')],remarks='Whole and both halves examined, plus enlarged top, diagram and lower annotation. The prose parenthesis after accouplement and the overwritten direct-image symbols are low-confidence. The RHS of the eta display visibly repeats the pr1,pr2 order, retained. The line giving P,Q is visually closer to pr1*,pr2* than the expected f*,g*, hence explicit alternatives. The lower trace exponent/sign is cramped. No omitted symbol is supplied from expected mathematics.')

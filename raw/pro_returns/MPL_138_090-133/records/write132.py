from records.record_page import save
save(132,r'''
\scanpage{132}
% archive foliation: 131
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw(0,0)ellipse(.85 and 1);\fill(0,.25)circle(.025);\node[above]at(0,.25){$\infty$};\draw(-.45,-.1)..controls(-.1,-.35)and(.2,-.3)..(.45,-.2);\node[left]at(-.45,-.2){$0$};\node[right]at(.4,-.2){$1$};
\end{tikzpicture}}
Opération \inserted{$\Omega$ orientée} définie par une \deleted{\unsure{sous-complexe}}
Carte $(K',S')$ sur $S$, ayant éventuellement
un bout arrondi en le pt $1\in S$.
\inserted{définie à une isotopie constante sur $[0,1]\cup\{\infty\}$}

Considérons les conditions,

a) Pour tte carte holomorphe $(X,K,S)$, il existe
\deleted{\unsure{complexe $K'_X$ sur $X$}}
un représentant $(K'_X,S'_X)$ de $\Omega(C)$ qui est
compatible avec la structure complexe.

b) Pour tte \deleted{\unsure{carte au dessus}} \inserted{carte $(X,K,S)$}, les réalisations
\deleted{complexes} \inserted{holomorphes} canoniques de celle-ci et de
$(\unsure{X'_C|X},K'_C,S'_C)$ \deleted{sont} faites sur des surfaces
\deleted{comp.} holomorphes isomorphes.

\deleted{b') comme b),}
\unsure{c)} Pour tte carte $C=(X,K,S)$, \inserted{et choix de $K'_X$,} il existe
une structure complexe sur $X$
qui est compatible avec $(K,S)$, $(K'_X,S'_X)$ et
avec $\operatorname{Sup}((K,S),(K'_X,S'_X))$)

\margin{a') b') c') comme a) b) c) mais mêmes groupes d'autom. hol.}

d) Il existe une application \uline{holomorphe}
$\varphi:S\longrightarrow S$, \deleted{définie} ``spéciale'' [i.e. un
\deleted{rev.} \inserted{étale} au dessus de $S-\{0,1,\infty\}$,
\deleted{appliquant} ayant ramification \deleted{\unsure{=}}\inserted{$\leq$}$2$
\inserted{en les pts au dessus de $1$ \unsure{(sauf en $1$)}}
\deleted{en $1$}, appliquant $\{0,\infty\}$ dans $\unsure{\{0,\infty\}}$ et
$1$ en $\{0,\infty,1\}$, et telle que \deleted{$\unsure{\varphi(1)\neq1}$} $\varphi(1)=1$
implique que $\varphi$ est étale en $1$) telle que
\[
(K',S')\underset{\unsure{[0,1]\cup\{\infty\}}}{\overset{\text{isotope}}{\simeq}}\varphi^{-1}([0,1],\{0\})
\]
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw(-.8,0)--(1,.3);\draw(-.7,.8)..controls(-.3,-.3)and(.2,-.3)..(.2,.8);\draw(.55,.9)..controls(.4,.2)and(.5,-.4)..(.7,-.6);\fill(-.2,.1)circle(.045);\fill(.5,.22)circle(.04);\fill(1,.3)circle(.05);
\begin{scope}[yshift=-1.3cm]\draw[line width=1.5pt](-.9,0)--(-.05,.1);\draw[line width=1pt](-.5,.04)--(-.58,.45);\draw(.4,0)--(1.3,.2);\draw(.4,0)--(.3,.5);\draw(1.05,.14)--(1.15,.55);\end{scope}
\end{tikzpicture}}}
''', [('drawing','top left','sphere 0,1,∞'),('text','top','Opération définie'),('insertion','top','Ω orientée'),('deletion','top','sous-complexe'),('insertion','upper right','définie à une isotopie constante'),('text','upper','Considérons les conditions'),('text','upper','a) Pour tte carte holomorphe'),('deletion','upper','complexe K′_X sur X'),('text','middle','b) Pour tte carte'),('deletion','middle','carte au dessus'),('insertion','middle','carte (X,K,S)'),('deletion','middle','complexes'),('insertion','middle','holomorphes'),('deletion','middle','sont / comp.'),('deletion','middle','b′) comme b)'),('text','middle lower','c) Pour tte carte'),('insertion','middle lower','et choix de K′_X'),('margin note','lower','a′) b′) c′)'),('text','lower','d) Il existe une application'),('deletion','lower','définie / rev.'),('insertion','lower','étale'),('deletion','lower','appliquant / ='),('insertion','lower','≤'),('insertion','lower','en les pts au dessus de 1'),('deletion','lower','en 1 / φ(1)≠1'),('display','bottom','(K′,S′) isotope φ^{-1}([0,1],{0})'),('drawing','left lower','three local graph sketches')],
doubts=[('top deletion','sous-complexe','crossed text','low'),('a)','complexe K′_X sur X','cancelled line','low'),('b)','X′_C, K′_C,S′_C','first coordinate overwritten, indices possibly X','low'),('c)','c)','label overwritten','low'),('d)','en les pts au dessus de1 (sauf en1)','faint and partially stained insertion','low'),('bottom','{0,∞}; φ(1)≠1; isotope relative[0,1]∪{∞}','formula and cancellation partly obscured physically','low')],
leads='Conditions for operation Ω to preserve holomorphic realizations: existence representative compatible with complex structure; canonical surfaces isomorphic; common complex structure for C,ΩC,Sup; variants same holomorphic automorphism groups; special holomorphic sphere map φ with branch and marked-point conditions. Heavy corrections and stained lower formula require marked reading uncertainty, cannot strengthen equivalence before133.')

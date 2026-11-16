import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{9}
\mspage{7}

(2.2.2), et on ne se bornera pas \deleted{\unsure{et}} à étudier sa restriction à $I$. \deleted{\unsure{Pour}} On verra que \deleted{toute} \inserted{parfois} le fait qu'une représentation de $I$ se prolonge à $\pi$ impose à cette représentation des restrictions draconiennes.

2.3.

2.4. Rappelons la structure de $I$. Soit $p$ l'exposant caractéristique de $k$, \deleted{Alors} et soit $P$ \deleted{\unsure{le}} un \deleted{plus grand} sous-groupe de Silow de $I$ ($P=1$ si $p=1$ i.e. $k$ de car. nulle). Alors $P$ \uline{est invariant}, i.e. on a une suite exacte
\diagram{\begin{tikzcd}
(2.4.1)\quad1\arrow[r,no head]&P\arrow[r]&I\arrow[r]&I_t\arrow[r]&1,
\end{tikzcd}}
où $I_t$ \inserted{(partie ``tame'' du groupe d'inertie $I$)} est un groupe profini premier à $p$, d'autre part on a un isomorphisme canonique
\[
(2.4.2)\qquad I_t\simeq\prod_{\ell\ne p}\mathbf Z_\ell(1)
\]
Le deuxième est obtenu ainsi. Le groupe $P$ est le groupe de Galois \deleted{de}
\[
(2.4.3)\qquad P=\operatorname{Gal}(\bar K/\bar K_t),
\]
où $\bar K_t$ est la plus \deleted{\unsure{grande}} grde sous-extension \uline{modérément ramifiée} de $\bar K/K$ \inserted{(val. : $V$)}, ou encore de $\bar K/\widetilde K$ (val. : $\widetilde V$). Celle-ci s'obtient, \unsure{en termes|en donnant}
\margin{8}
'''
e=[('text','top','(2.2.2) et on ne se bornera pas'),('deletion','first line','et'),('deletion','between top lines','Pour'),('deletion','above que','toute'),('insertion','above le fait','parfois'),('text','upper-middle','2.3.'),('text','middle','2.4 Rappelons la structure de I'),('deletion','after k','Alors'),('deletion','after P','le'),('deletion','before sous-groupe','plus grand'),('diagram','middle','(2.4.1) 1—P→I→I_t→1'),('insertion','below sequence','partie tame du groupe d’inertie I'),('text','middle-lower','où I_t est un groupe profini'),('display','lower','(2.4.2) I_t ≃ product Zℓ(1)'),('text','lower','Le deuxième est obtenu ainsi'),('deletion','before P=Gal','de'),('display','lower','(2.4.3) P=Gal(Kbar/Kbar_t)'),('text','bottom','où Kbar_t est la plus'),('deletion','bottom','grande'),('insertion','after Kbar/K','val.:V'),('margin note','bottom left','8')]
save_page(34,9,tex,e,remarks='The manuscript spelling Silow is retained. The terminal words are faint and tentative. The first exact-sequence segment is a line without an arrowhead. The bare heading 2.3. is an actual otherwise empty item on the sheet.')

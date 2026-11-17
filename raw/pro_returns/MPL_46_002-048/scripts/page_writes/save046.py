import sys
sys.path.insert(0,'/workspace/scratch/0abb0718b9e3/MPL_46_002-048_work/scripts')
from record_page import save
save(46,r'''\scanpage{46}
\mspage{-VI-4-}
\hfill n°383

par des figures, en associant à chaque noeud un point du plan, et en joignant deux points par un arc si les noeuds correspondants sont liés. On saute le laius pontifiant sur la nature non-mathématique des figures.
\figure{\begin{tikzpicture}\draw (0,1.3) .. controls (-0.04,1.2) and (0.04,1.15) .. (0,1.05) .. controls (0.05,0.95) and (-0.04,0.9) .. (0,0.8) .. controls (-0.04,0.7) and (0.05,0.65) .. (0,0.55) -- (0,0);\end{tikzpicture}}

Un graphe $X'$ est un \uline{sous-graphe} de $X$ si $X'\subset X$ et si deux noeuds de $X'$ liés dans $X'$ sont liés dans $X$. On dit que $X'$ est un sous-graphe \uline{plein} si, de plus, deux noeuds de $X'$ qui sont liés dans $X$ sont liés dans $X'$.

Un noeud $a$ d'un graphe $X$ est dit une \uline{extrémité} de $X$ si $a$ est lié à au plus un noeud distinct de $a$.

On dit qu'un graphe $X$ est \uline{connexe} s'il n'existe aucune partition $X=X'\cup X''$ de $X$ telle qu'aucun élément de $X'$ ne soit lié à aucun élément de $X''$.

Un graphe fini $X$ s'appelle un \uline{circuit} s'il a au moins $3$ noeuds, et si ces noeuds peuvent être indexés $a_1,\ldots,a_n$ $(n\geqslant3)$ de sorte que les simplexes de $X$ soient $(a_1,a_2)$, $(a_2,a_3)$,\ldots,$(a_{n-1},a_n)$,$(a_n,a_1)$ ; un circuit n'admet aucune extrémité. Un graphe dont aucun sous-graphe n'est un circuit s'appelle une \uline{forêt}. Une forêt connexe s'appelle un \uline{arbre}.

LEMME 6.- \uline{Toute forêt finie non vide} $X$ \uline{admet une extrémité}.

Prenons $a_1\in X$. Construisons, par récurrence, une suite $(a_1,\ldots,a_i,\ldots)$ d'éléments de $X$ telle que $a_i$ soit lié à $a_{i-1}$ et $a_{i+1}$ et que $a_{i+1}$ soit distinct de $a_{i-1}$ (pour $i\geqslant2$). Les $a_i$ sont distincts car, \inserted{sinon,} $X$ contiendrait un circuit. La suite $(a_i)$ est donc finie. Son dernier terme est évidemment une extrémité de $X$.

LEMME 7.- \uline{Soit} $X$ \uline{une forêt finie ayant au moins deux noeuds}. \uline{Il existe une partition} $X=X_1\cup X_2$ \uline{telle que deux noeuds distincts appartenant à un même} $X_i$ \uline{soient non-liés}.

On raisonne par récurrence sur $\operatorname{card}(X)$, le cas $\operatorname{card}(X)=2$ étant trivial. Soit $a$ une extrémité de $X$ (lemme 6), et $X'$ le complémentaire de $a$, muni de la structure de sous-graphe plein de $X$. Alors $X'$ est une forêt ; d'après l'hypothèse de récurrence on a une partition $X'=X'_1\cup X'_2$ telle que deux noeuds appartenant à un même $X'_i$ soient
\mspage{45}''',[
('text','header','-VI-4- ; n°383'),('text','top continuation','par des figures'),('drawing','left of initial paragraph','short wavy vertical stroke'),('text','second paragraph','Un graphe X′ est un sous-graphe'),('text','third paragraph','Un noeud a d’un graphe X'),('text','fourth paragraph','On dit qu’un graphe X est connexe'),('text','fifth paragraph','Un graphe fini X s’appelle un circuit'),('text','LEMME 6','Toute forêt finie non vide'),('text','proof of LEMME 6','Prenons a₁∈X'),('insertion','proof, above X contiendrait','sinon,'),('text','LEMME 7','Soit X une forêt finie'),('text','last paragraph, unfinished','On raisonne par récurrence'),('text','opposite orientation foliation','45')],sheet_kind='reused_typed',observation='Reused typescript was additionally read in rotated halves. A handwritten “sinon,” with insertion caret is preserved in the proof of lemma 6, as is the marginal wavy stroke. This typescript’s continuation occurs on scan 044, not the next physical scan.')

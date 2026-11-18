import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{59}
% archive foliation: 61
\uline{Th. 4} Équivalence de catégories entre

a) Cat. des couples $(X,K,S)$ $X$ surface conforme
à bord compacte, $(K,S)$ complexe top. \deleted{\unsure{cpt}}\inserted{cpt} avec
\[
\delta X\subset K\subset X,\qquad K\text{ assez régulier}\quad\text{(rectifiable suffit)}
\]

\margin{\uline{NB} On ne suppose pas les \unsure{compos. conn.}
de $K\setminus S$ des intervalles
(il peut y avoir des cercles).}

b) Cat des systèmes $(\widetilde X,\widetilde S,\sigma)$, où
$\widetilde X$ est une surface conforme à bord \inserted{compacte},
$\widetilde S$ une partie finie de $\delta\widetilde X$, $\sigma$ une
involution de $\operatorname{Déc}(\delta\widetilde X/\widetilde S)$, $\sigma$ assez
\unsure{régulière|régulier} (rectifiable suffit).

Le foncteur a) $\longrightarrow$ b) résulte du th. $\unsure{3|2}$,
avec un complément qui explicite les
propriétés de régularité de la fonction-recollement
dont il a été question dans
le lemme 2. Pour le foncteur en sens
inverse, il est connu topologiquement, et
comme faisceau structural conforme
(large) sur $X$ \inserted{$=\widetilde X/R$}, on prend les fonctions
continues qui sont conformes dans $X\setminus K\simeq\operatorname{Int}\widetilde X$.
"""
save(59,tex,[('text','heading','Th. 4 Équivalence de catégories entre'),('text','a)','Cat. des couples (X,K,S)'),('deletion','a) second line','cpt'),('insertion','a) second line','cpt'),('display','a)','δX⊂K⊂X; K assez régulier (rectifiable suffit)'),('margin note','upper left diagonal','NB On ne suppose pas'),('text','b)','Cat des systèmes (X-tilde,S-tilde,σ)'),('insertion','b) after bord','compacte'),('text','lower half','Le foncteur a)→b) résulte du th.'),('insertion','penultimate two lines','X=X-tilde/R')],
 doubts=[('margin','compos. conn.','compressed abbreviation; means connected components','medium'),('b)','régulière','régulier; ending uncertain','medium'),('lower paragraph','th. 3','2 possible, overwritten digit','medium')],
 notations=[('Cut boundary at finite marked set',r'\operatorname{Déc}(\delta\widetilde X/\widetilde S)','Scan 59; slash, not set difference'),('Gluing involution',r'\sigma','Scan 59'),('Topological quotient',r'\widetilde X/R','Scan 59; plain R')],
 abbreviations=[('cpt','compact'),('compos. conn.','composantes connexes'),('Déc','découpe')],
 leads=['Th. 4 proposes cutting/gluing equivalence between triples (called couples in the text) and bordered surfaces with finite boundary marking and an involution of the cut boundary. Morphisms and sufficient regularity are not fully specified here.','Rectifiable suffit appears without question marks here, despite the earlier explicit questions. Do not treat that change alone as a proof.','Boundary components without marked vertices are explicitly allowed (circles in K minus S).','Construction of the large sheaf on the quotient is given; showing it defines a conformal structure is the analytic step.'])

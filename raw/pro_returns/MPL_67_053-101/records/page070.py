import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{70}
\mspage{9}
% archive foliation: 72
métriques euclidiennes \uline{canoniques} sur
les $T_{X,a_i}$, \unsure{décrivant|dérivant} leur structure
conforme. Dans le cas $g\geq2$ et même
encore pour $g=1$, cela ne semble pas
inquiétant, puisqu'on a une
métrique canonique sur $X$. Par
contre dans le cas $g=0$, cela semble
étrange, puisque dans ce cas on n'a
\uline{pas} de métrique canonique sur $X$.

\uline{12.1.}

5. \uline{Retour sur le principe de chirurgie conforme}

La formulation des lemmes \inserted{locaux} $2$ et $3$, qui
sont l'ingrédient technique essentiel pour le
th. $4$ (et lui sont équivalents), est un peu
alambiquée. Il est plus élégant de se
réduire à des lemmes globaux du type
uniformisation par le disque $D$. Cela
donne le
"""
save(70,tex,[('text','upper half','métriques euclidiennes canoniques'),('text','middle','12.1.'),('text','middle lower heading','5. Retour sur le principe de chirurgie conforme'),('text','lower half','La formulation des lemmes'),('insertion','lower first line','locaux')],
 doubts=[('second line','décrivant','dérivant; middle strokes compressed','medium')],
 leads=['Author flags genus-zero tension: canonical Euclidean tangent metrics would seem strange because X has no canonical metric; distinguish marked from unmarked surface.','Dated 12.1, section 5 returns to surgery principle and proposes replacing local lemmas 2 and 3 by global disc-uniformization lemmas, claimed equivalent to theorem 4.'])

import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{68}
\mspage{8}
% archive foliation: 70
par bouchage des trous correspondants reste
la même (à isom. can. près). Il faudrait,
pour le voir clairement, voir la
relation entre la sphère \inserted{\unsure{bd}} $S(I)$ triponctuée,
associée à la sphère à bord $\Sigma^*$, et ses
paramètres $\ell_i$ $(i\in I)$ comme \unsure{déduite}
\deleted{(\unsure{obtenue}}
de $S(I)$ en enlevant des disques \deleted{que}
$\unsure{D}(\ell_i)$ \inserted{de centre $s_i$ ?}\deleted{qui} dont chacun ne dépend que
des $\ell_i$ correspondants, pas des autres
$\ell_j$.
\margin{?}

Ce point étant supposé acquis, ou quelque
variante, il semble donc bien que
\inserted{(du moins dans le cas hyperbolique orienté)}
pour une surface conforme ponctuée
donnée, \inserted{de type $(g,\nu)$} les familles \inserted{\unsure{admiss.} $(D_i)$} des disques autour
des $a_i$ forment un espace homéom.
à $\mathbb R^\nu$ (où $\nu=\operatorname{card} I$), i.e. à celui
des systèmes d'ombres possibles ! Il
est donc très tentant de faire la

\uline{Conjecture} Pour tt \unsure{surface} conforme
ponctuée (ou \deleted{tout} au moins dans le cas
hyperbolique), l'application \deleted{que}
\[
(D_i)\longmapsto(o(D_i))
\]
"""
save(68,tex,[('text','top','par bouchage des trous correspondants'),('insertion','upper','bd'),('deletion','upper middle','(obtenue'),('deletion','upper middle','que'),('insertion','middle','de centre s_i ?'),('deletion','middle','qui'),('margin note','left middle','?'),('text','middle lower','Ce point étant supposé acquis'),('insertion','middle lower','du moins dans le cas hyperbolique orienté'),('insertion','middle lower','de type (g,ν)'),('insertion','middle lower','admiss. (D_i)'),('text','lower','Il est donc très tentant'),('text','bottom','Conjecture Pour tt surface conforme'),('deletion','bottom','tout'),('deletion','bottom','que'),('display','bottom','(D_i)↦(o(D_i))')],
 doubts=[('above sphère','bd','small abbreviation insertion uncertain','low'),('after comme','déduite','ending compressed','medium'),('cancelled parenthesis','obtenue','several superposed letters','low'),('before families of discs','admiss.','inserted abbreviation squeezed','medium'),('conjecture object','surface','overwritten word possibly earlier système; only final surface readable','medium')],
 notations=[('Bordered sphere',r'\Sigma^*','capital Sigma and star'),('Boundary length parameter',r'\ell_i','looped lower-case ell'),('Tripunctured sphere',r'S(I)','plain capital S')],
 abbreviations=[('can.','canonique'),('homéom.','homéomorphe'),('admiss.','admissibles'),('bd','bord, uncertain insertion')],
 leads=['Unverified independence claim: each removed disc on the tripunctured sphere should depend only on its corresponding boundary length and not on the other lengths; marked by a large marginal question mark and Il faudrait.','Conditional reasoning Ce point étant supposé acquis yields an R^ν-space of admissible disc systems for a fixed punctured surface.','Begins explicit conjecture about map from admissible disc systems to shadow systems, at least in the hyperbolic case; continuation on scan 69.'])

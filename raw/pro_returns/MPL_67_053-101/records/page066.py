import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{66}
\mspage{7}
% archive foliation: 68
coïncident. Cela signifie donc que
$X$ est déduit de $X^*$ par ``bouchage
de trous \unsure{par disques} canoniques'' (utilisant
les structures toriques sur les
comp. conn. de $\delta X^*$). \deleted{La question}\inserted{Disons alors}
qu'un système de disques $(D_i)_{i\in I}$ dans $X$
\deleted{\unsure{qui n}} autour des $a_i$ est ``admissible''.

\uline{\unsure{Questions|Question :}} Comment cette condition
d'admissibilité se reflète-t-elle en
termes de la géométrie interne de $X$ ?
Par exemple, \deleted{quand} quand $X$ est muni
d'une métrique de \unsure{Bergmann|Bergman} canonique
(cas où $X\not\simeq\mathbb P^1_{\mathbb C}$), quelle est la
relation de cette condition avec celle
que les \deleted{$\unsure{\delta}$}$D_i$ soient des ``disques
géodésiques'' (\inserted{définis} par la condition que
\[
\operatorname{dist.\ géod}(x,a_i)\leq r_i
\]
) ?

\margin{supposons hyperbolique i.e. $(g,\nu)\neq(0,1),(0,2)$}
Fixons une \deleted{$X_0$} surface top. \inserted{orientée}
à bord de référence $X_0$, de type $g,\nu$
"""
save(66,tex,[('text','top','coïncident. Cela signifie donc que'),('deletion','upper middle','La question'),('insertion','upper middle','Disons alors'),('deletion','upper middle','qui n'),('text','middle','Questions Comment cette condition'),('text','middle lower','Par exemple quand X est muni'),('deletion','middle lower','quand'),('deletion','lower','δ before D_i'),('insertion','lower','définis'),('display','lower','dist. géod(x,a_i)≤r_i'),('margin note','bottom left','supposons hyperbolique'),('text','bottom','Fixons une surface top.'),('deletion','bottom','X_0'),('insertion','bottom','orientée')],
 doubts=[('top third line','par disques','very compressed joining strokes','medium'),('heading','Questions','could be Question followed by colon','medium'),('metric name','Bergmann','one or two final n not resolved','medium'),('before D_i','δ','deleted symbol overwritten','low')],
 abbreviations=[('top.','topologique'),('géod','géodésique')],
 leads=['Admissible disc systems defined by matching toric boundary structures; capping with canonical discs recovers X.','Explicit question about intrinsic geometry of admissibility; comparison with geodesic discs for the canonical Bergmann/Bergman metric on X not isomorphic to the complex projective line.','Fixes an oriented hyperbolic topological bordered reference surface, excluding (g,ν)=(0,1),(0,2).'])

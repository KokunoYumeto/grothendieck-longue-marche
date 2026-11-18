import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(40,r'''\mspage{14}
% archive foliation: 42
\uline{Cas des surfaces conformes à bord} (pas néc. cptes)

On utilise l'équivalence de catégories
\diagram{\begin{array}{c@{\quad\simeq\quad}l}
\text{surfaces conformes à bord}&\text{surfaces holomorphes sans bord,}\\
&\text{munies d'une anti-involution.}
\end{array}}
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
X \arrow[r,mapsto] & (X'=X^{or},\sigma)\\
X=X'/\sigma & (X',\sigma) \arrow[l,mapsto]
\end{tikzcd}}

On dit que $X$ est hyperbolique ssi $X^{or}$ est hyperbolique \inserted{(i.e. ses comp. connexes les 2 ou 1)}. Quand $X$ est sans bord, on a $\widetilde X\simeq\widetilde{X^{or}}$ (car $X^{or}$ est un rev. étale de $X$) donc $X$ est hyperbolique au sens des réflexions précédentes, ssi il l'est en ce nouveau sens.

Si $X$ est compact, \inserted{donc $X^{or}$ aussi,} comme on a
\[
\chi(X^{or})=2\chi(X),
\]
et que $\chi(X^{or})<0\Longleftrightarrow X^{or}$ hyperbolique, on trouve
\[
X\text{ hyperbolique}\Longleftrightarrow\chi(X)<0.
\]
P.ex. si $X$ est holomorphe 0-connexe, de type $g,\nu$, cela signifie que
\[
2g\unsure{-|+}2+\nu\geq1\qquad\text{i.e}\quad2g+\nu\geq3.
\]
Mais on se gardera de confondre cette condition avec celle que $\mathrm{Int}\,X$ soit hyperbolique, ce qui est tjrs vrai sauf si $\nu=0$, $g\in\{0,1\}$\ldots
''',[
('text','top title','Cas des surfaces conformes à bord (pas néc. cptes)'),
('text','upper','On utilise l’équivalence de catégories'),
('diagram','upper','surfaces conformes à bord ≃ surfaces holomorphes sans bord'),
('diagram','middle upper','X ↦ (X′=X^{or},σ); X=X′/σ ↤ (X′,σ)'),
('text','middle','On dit que X est hyperbolique'),
('insertion','middle right','i.e. ses comp. connexes les 2 ou 1'),
('text','lower middle','Si X est compact'),
('insertion','lower middle','donc X^{or} aussi'),
('display','lower middle','χ(X^{or})=2χ(X)'),
('display','lower','X hyperbolique ⇔ χ(X)<0'),
('text','lower','P.ex. si X est holomorphe 0-connexe'),
('display','lower','2g−2+ν≥1; 2g+ν≥3'),
('text','bottom','Mais on se gardera de confondre ... Int X')],leads='Hyperbolicity of a conformal surface with boundary is defined through its double X^{or}, compared with hyperbolicity of Int X; exact maps X↦(X^{or},sigma), quotient back. Compact Euler formula chi(Xor)=2chi(X). Final warning explicitly compares two conditions. Need search context doubling, bord, hyperbolique, type (g,nu). Arithmetic sign in 2g?2+nu is kept doubtful from heavy ink.')

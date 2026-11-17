import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(42,r'''
\scanpage{42}
% archive foliation: 41
\[
\delta=\rho^N\delta\qquad\forall N\in\mathbf N
\]
d'où, prenant $N$ grand d'où $\rho^N=0$ :
\[
\delta=0\qquad\text{cqfd.}
\]
\uline{Extension aux tenseurs}
\[
\begin{aligned}
u&\in\operatorname{End}_K(M)\\
v&\in\operatorname{End}_K(N)
\end{aligned}
\]
Alors $M$ $(N)$ $\overline G_a$-Module par $\bar e_u$ $(\bar e_v)$, et on a $M\otimes N$ $\overline G_a$-Module par $\bar e_u\otimes\bar e_v$ --- et
\[
\bar e_u\otimes\bar e_v=\bar e_{u\otimes\operatorname{id}_N+\operatorname{id}_M\otimes v}
\]
De \unsure{même}, si $u,v$ nilpotents
\[
e_u\otimes e_v=e_{u\otimes\operatorname{id}_N+\operatorname{id}_M\otimes v}
\]
Extension : $\displaystyle\bigotimes_{i\in I}M_i$ ($I$ ens d'indices fini, de cardinal $\geq2$)

\uline{Corollaire} Soit $M$ muni d'une structure d'alg. (pas néc. assoc. ni unitaire, encore moins comm.) sur $K$, $u\in\operatorname{End}_{K\text{-mod}}(M)$, donc $\overline G_a$ (Resp. $G_a$ si $u$ nilpotent) opère sur le $K$-module $M$. Pour que cette opération soit une op. \unsure{d'endom|d'autom.} d'algèbre, il f et s. que $u$ soit une \uline{dérivation}.
''',[
('display','top','delta=rho^N delta forall N in N'),
('text','upper','dou prenant N grand dou rho^N=0'),
('display','upper','delta=0 cqfd.'),
('text','upper title','Extension aux tenseurs'),
('display','upper middle','u in End_K(M); v in End_K(N)'),
('text','middle','Alors M (N) bar G_a-Module'),
('display','middle','bar e_u tensor bar e_v = bar e_(u tensor id+id tensor v)'),
('text','fold','De même si u,v nilpotents'),
('display','below fold','e_u tensor e_v = e_(u tensor id+id tensor v)'),
('text','lower middle','Extension: tensor_i M_i; I ens dindices fini'),
('text','lower','Corollaire Soit M muni dune structure dalg.')
],[
('before unbarred tensor identity','même','word abbreviated by horizontal strokes','medium'),
('corollary final condition','dendom','dautom.; faint middle letters, not resolved by mathematical expectation','low')])

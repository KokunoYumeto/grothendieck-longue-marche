import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(41,r'''
\scanpage{41}
% archive foliation: 40
\uline{Dém} On a déjà vu l'équivalence de $(1)$ à $(3)$, et \deleted{\unsure{(3)}} \inserted{\unsure{ce|que}} implique $4$ (i.e. $e_v(\unsure{1|0})f=fe_u(\unsure{1|0})$). Prouvons $(4)\longrightarrow(3)$. Or $(4)$ s'écrit
\[
\begin{gathered}
\underbrace{(\exp v)\circ f-f\circ\exp u}_{\text{''}}=0\\
\sum_{n\geq1}\frac1{n!}\underbrace{(v^nf-fu^n)}_{\delta_n\ \mathrm{déf}}
\end{gathered}
\]
Or on a (réc. sur $n$)
\[
\delta_n=\unsure{v}^{n-1}\delta+v^{n-2}\delta u+\cdots+v\delta u^{n-2}+\delta u^{n-1}
\]
donc $(4)$ signifie
\[
\delta+\frac12(v\delta+\delta u)+\frac1{3!}(v^2\delta+v\delta u+\delta u^2)+\cdots=0
\]
\margin{(somme \uline{finie})}
On peut l'écrire
\[
\delta=\sum_{i+j\geq1}c_{ij}v^i\delta u^j
\qquad\begin{array}{c}(c_{ij}\in K)\\\text{''}\\\dfrac1{(i+j)!}\end{array}
\]
On met $U=\operatorname{End}_K(M)$
\[
\Theta,\Theta':U\longrightarrow U\qquad K\text{-endom}
\]
\[
\Theta(x)=vx,\qquad\Theta'(x)=xu
\]
Donc $\Theta,\Theta'$ sont nilpotents ($v,u$ l'étant) et commutent, et on aura
\[
\delta=\sum_{i+j\geq1}c_{ij}\Theta^i\Theta'{}^j\delta=\rho\delta
\]
\[
\rho=\sum_{i+j\geq1}c_{ij}\Theta^i\Theta'{}^j\in\operatorname{End}_K(U)
\]
Or $\rho$ est \uline{nilpotent} ($\Theta,\Theta'$ l'étant et commutant).

Or $\delta=\rho\delta$ implique par récurrence
''',[
('text','top','Dém On a déjà vu léquivalence'),
('deletion','top right after et','(3)'),
('insertion','above top-right cancellation','ce / que'),
('display','upper','exp v circle f - f circle exp u =0; sum delta_n/n!'),
('text','upper-middle','Or on a (réc. sur n)'),
('display','middle','delta_n=v^(n-1)delta + ...'),
('text','middle','donc (4) signifie'),
('display','fold','delta+1/2(v delta+delta u)+1/3!(...)=0'),
('margin note','right below fold','somme finie'),
('text','lower-middle','On peut lécrire'),
('display','lower-middle','delta=sum_i+j>=1 c_ij v^i delta u^j'),
('margin note','right of c_ij formula','c_ij in K; ditto; 1/(i+j)!'),
('text','lower-middle','On met U=End_K(M)'),
('display','lower','Theta, Theta prime: U to U K-endom'),
('display','lower','Theta(x)=vx; Theta prime(x)=xu'),
('text','lower','Donc Theta,Theta prime sont nilpotents'),
('display','lower','delta=sum c_ij Theta^i Theta prime^j delta=rho delta'),
('display','near bottom','rho=sum c_ij Theta^i Theta prime^j in End_K(U)'),
('text','bottom','Or rho est nilpotent; Or delta=rho delta implique')
],[
('top-right deletion and insertion','(3) deleted; ce inserted','que; small letters obscured at page edge','low'),
('evaluation in opening parenthesis','1','0; numeral retraced','medium'),
('first base in delta_n identity','v','heavily retraced, resembles u','medium'),
('Greek endomorphism letters throughout','Theta, Theta prime','lower-case theta possible; large circular crossed form retained','medium')])

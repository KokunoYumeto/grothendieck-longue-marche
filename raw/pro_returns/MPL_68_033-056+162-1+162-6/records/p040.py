import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(40,r'''
\scanpage{40}
% archive foliation: 39
\uline{Prop} Soient $M,N$ deux $K$-modules, $u$ $(v)$ un endom de $M$ $(N)$, $f:M\longrightarrow N$ un $K$-hom. Considérons $M,N$ comme $\overline G_{aK}$-modules par $\lambda\in\overline G_{aK}(K')$ opérant par $\exp(\lambda u)$ resp. $\exp(\lambda v)$. Pour que $f$ soit un $G_{aK}$-morphisme, il f. et s. que l'on ait $vf=fu$ i.e. $vf-fu=0$

\uline{Cor} Si $u,v$ \deleted{\unsure{c}} sont nilpotents, c'est aussi la cond. néc. et suff. pour que $f$ soit un $G_a$-\unsure{morphisme}.

\uline{Dém} Il faut écrire
\[
\sum_{n\geq0}\lambda^n\frac{v^n}{n!}f=\sum_{n\geq0}\lambda^n f\frac{u^n}{n!}
\]
\margin{\unsure{univ.} en $\lambda$ nilp.}
i.e.
\[
\sum_{n\geq1}\frac1{n!}(v^nf-fu^n)\lambda^n=0
\]
\unsure{univ.} en $\lambda$ nilp., ce qui équivaut à
\[
v^nf-fu^n=0\qquad\forall n\geq1
\]
Pour $n=1$, c'est la commutation $vf=fu$, qui implique par récurrence $v^nf=fu^n$ $(\forall n\geq1)$.

\uline{Proposition} Soient \deleted{\unsure{u,v}} $u\in N(\operatorname{End}_K(M))$, $v\in N\operatorname{End}_K(N)$, $f\in\operatorname{Hom}_K(M,N)$. Conditions équivalentes :

1) $f$ est un $\overline G_{aK}$-hom (pour \inserted{$\overline G_a$ opérant sur $M,N$ par} $\bar e_u$ et $\bar e_v$)

2) $f$ est un $G_{aK}$-hom ($\ldots$)

3) $fu=vf\deleted{\unsure{0}}$ i.e. $\delta\overset{\mathrm{déf}}=vf-fu=0$

4) $f\circ\exp(u)=\exp(v)\circ f$
''',[
('text','top','Prop Soient M,N deux K-modules'),
('text','upper middle','Cor Si u,v sont nilpotents'),
('deletion','above after u,v','c (tiny cancelled mark)'),
('text','middle','Dém Il faut écrire'),
('display','middle','sum lambda^n v^n/n! f = sum lambda^n f u^n/n!'),
('margin note','right of sum','univ. en lambda nilp.'),
('text','middle left','i.e.'),
('display','above fold','sum_n>=1 1/n! (v^n f-fu^n)lambda^n=0'),
('text','below fold','univ. en lambda nilp., ce qui équivaut à'),
('display','below fold','v^n f-fu^n=0 forall n>=1'),
('text','lower middle','Pour n=1, cest la commutation'),
('text','lower','Proposition Soient u in N(End_K(M))'),
('deletion','after Soient','u,v'),
('text','bottom condition 1','f est un bar G_aK-hom'),
('insertion','condition 1 above e_u et e_v','bar G_a opérant sur M,N par'),
('text','bottom condition 2','f est un G_aK-hom'),
('display','bottom condition 3','fu=vf i.e. delta defined vf-fu=0'),
('deletion','condition 3 after vf','0 (small overwritten symbol)'),
('display','bottom condition 4','f circle exp(u)=exp(v) circle f')
],[
('corollary after u,v','deleted c','tiny overwritten mark may be an abandoned letter','low'),
('corollary right edge','morphisme','end of word faint and crowded at edge','medium'),
('margin and below fold','univ.','universal abbreviation; first letters compressed','medium'),
('second proposition deletion','u,v','two short overwritten symbols','low'),
('condition 3 trailing cancellation','0','small overtraced symbol','low')])

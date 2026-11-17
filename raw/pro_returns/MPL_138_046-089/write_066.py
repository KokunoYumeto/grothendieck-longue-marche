from workflow import save_page
save_page(66,r'''
\scanpage{66}
% archive foliation: 65
\margin{Cas galoisien $d_{ij}=\deleted{\unsure{N}}d_i=N/\nu_i$}
\[
2-2g'=N(2-2g)\unsure{-}\underbrace{(N\nu\unsure{-|+}\nu')}_{\sum_{i,j}(d_{ij}-1)}
=N(2-2g)-\sum_i\underbrace{\nu_i(N/\nu_i-1)}_{N-\nu_i=N(1-\frac{\nu_i}{N})}
\]
\margin{\deleted{$\unsure{-g'}$}\quad\deleted{\unsure{ici}}}
\[
\boxed{2-2g'=N\left[(2-2g)-\sum_i\left(1-\frac1{d_i}\right)\right]}
\]
Si $g'=0$, on trouve $g=0$ et
\[
\boxed{\frac2N=2-\sum_i\left(1-\frac1{d_i}\right)>0}
\]
d'où
\[
\sum_i\left(1-\frac1{d_i}\right)<2
\]
\uline{Obs} Tous les $d_i\geq2$ \deleted{car} \unsure{ici} $I$ est \uline{\unsure{tout|tjrs}} l'ens de ramification

1) $\operatorname{Card}I=0$\qquad $\dfrac2N=2$, $N=1$ : \deleted{\unsure{par}} $G=1$

2) $\operatorname{Card}I=1$
\[
\frac2N=2-\left(1-\frac1d\right)=1+\frac1d\qquad
2=N+\frac Nd=N+\nu
\]
\margin{or $N\geq1$, $\nu\geq1$\quad donc $N=1$, $\nu=1$\quad $I=\varnothing$}
\uline{impossible}

3) $\operatorname{Card}I=2$
\[
\frac2N=\frac1{d_1}+\frac1{d_2}\qquad
2=\frac N{d_1}+\frac N{d_2}=\nu_1+\nu_2\qquad
\nu_1,\nu_2\geq1\qquad\nu_1=\nu_2=1
\]
\[
d_1=d_2=N\qquad\uline{N\text{ quelconque}}
\]
4) $\operatorname{Card}I=3$
\[
\deleted{\unsure{\frac2N=2}}\qquad
\frac1{\unsure{p|d_1}}+\frac1{\unsure{q|d_2}}+\frac1{\unsure{r|d_3}}>1
\qquad\left(\frac2N=\left(\frac1p+\frac1q+\frac1r-1\right)\right)
\]
OPS\qquad $p\geq q\geq r$

a) $\unsure{r|p}=2$\qquad $\dfrac1p+\dfrac1q>\dfrac12$\qquad i.e. pour $p=\alpha+2$, $q=\beta+2$\quad $(\alpha\geq\beta\geq0$
\margin{$\unsure{\alpha}$}
\[
2p+2q-pq>0\qquad\deleted{\unsure{2(\alpha+\beta)+8-}}
\]
\[
\underbrace{2(\alpha+2)+2(\beta+2)-(\alpha+2)(\beta+2)}_{4-\alpha\beta>0}>0
\]
\[
\alpha\beta<4\qquad
\begin{array}{l}
\beta=0,\ \alpha\text{ quelc.}\\
\beta=1,\ \alpha=1,2,3\\
\deleted{\unsure{\beta=2,\alpha}}
\end{array}
\]
\diagram{\left\{\begin{array}{lll}
(2,2,p)&p\geq2\text{ quelc.}&N=2p\\
(2,3,3)&&N=12\\
(2,3,4)&&N=24\\
(2,3,5)&&N=60
\end{array}\right.}
b) $r\geq3$\qquad $\dfrac1p+\dfrac1q>1-\dfrac1r\geq\dfrac23$\quad\uline{impossible} car $\dfrac1p,\dfrac1q\leq\dfrac13$

5) $\operatorname{Card}I\geq4$\qquad $\deleted{\unsure{\sum}}\quad\dfrac1p+\dfrac1q+\dfrac1r+\dfrac1s>2$\qquad $\deleted{\unsure{si}}\ p\geq q\geq r\ \deleted{\unsure{ou}}\geq s$

Faisons d'abord $\operatorname{Card}I=4$
\[
\deleted{\frac1p+\frac1q+\frac1r>2-\frac1s=1+\left(1-\frac1s\right)\geq1+\left(1-\frac1p\right)>1}
\]
''',[
('margin note','top','Cas galoisien d_ij=d_i=N/nu_i'),
('deletion','top marginal formula','N'),
('display','top','2-2g prime=N(2-2g)-(Nnu-nu prime) and summation'),
('deletion','beneath first formula left','-g prime; ici'),
('display','boxed upper third','2-2g prime=N[(2-2g)-sum(1-1/d_i)]'),
('text','upper third','Si g prime=0, on trouve g=0 et; d’où'),
('display','second boxed formula','2/N=2-sum(1-1/d_i)>0'),
('display','beneath second box','sum(1-1/d_i)<2'),
('text','upper middle','Obs Tous les d_i greater or equal 2'),
('deletion','Obs sentence','car'),
('text','middle','1) Card I=0; 2) Card I=1; impossible'),
('deletion','case 1 before G=1','par'),
('display','case 2','2/N=2-(1-1/d)=1+1/d; 2=N+N/d=N+nu'),
('margin note','right of case 2','or N and nu greater or equal 1; donc N=nu=1; I empty'),
('text','middle','3) Card I=2'),
('display','case 3','2/N=1/d_1+1/d_2; nu_1=nu_2=1; d_1=d_2=N quelconque'),
('text','lower middle','4) Card I=3; OPS; a); i.e. pour p alpha+2, q beta+2'),
('display','case 4','1/p+1/q+1/r>1; 2/N; p greater or equal q greater or equal r'),
('deletion','case 4 before inequality','2/N=2'),
('margin note','right of alpha beta condition','alpha'),
('display','case 4a','2p+2q-pq>0; substituted expression; alpha beta<4; beta cases'),
('deletion','above substituted expression','2(alpha+beta)+8-'),
('deletion','beneath beta=1','beta=2,alpha'),
('diagram','lower third','four triples (2,2,p),(2,3,3),(2,3,4),(2,3,5) and N'),
('text','near bottom','b) r greater or equal 3; impossible car'),
('display','case 4b','1/p+1/q>1-1/r greater or equal 2/3; 1/p,1/q less or equal 1/3'),
('text','bottom','5) Card I greater or equal 4; Faisons d’abord Card I=4'),
('display','case 5','1/p+1/q+1/r+1/s>2; p greater or equal q greater or equal r greater or equal s'),
('deletion','case 5','sum; si; ou'),
('deletion','last displayed line','1/p+1/q+1/r>2-1/s=1+(1-1/s) ... >1')])

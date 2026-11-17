from record import save
save(16,r'''\scanpage{16}
\begin{center}-- 47 --\end{center}
\margin{$\mathrm{n}^{\mathrm{o}}\ 387$}

f) Soient $M$, $N$ deux $A$-modules ; pour tout homomorphisme $u:M\longrightarrow N$, on note ${}^tu$ l'homomorphisme $\operatorname{Hom}(u,1_{K/A})$ de $N^*$ dans $M^*$, tel que $({}^tu(w))(x)=w(u(x))$ pour tout $x\in M$ et tout $w\in N^*$ ; ${}^tu$ est continu pour les topologies $\sigma(N^*,N)$ et $\sigma(M^*,M)$. Si $u$ est l'endomorphisme $x\longrightarrow\pi x$ de $M$, ${}^tu$ est l'endomorphisme $w\longrightarrow\pi w$ de $M^*$. Pour tout sous-module $P$ de $M$, on a $(u(P))^\circ={}^tu^{-1}(P^\circ)$.

10) Les hypothèses et notations sont celles de l'exerc. 9.

a) Si $M$ est un $A$-module \uline{topologique} discret, montrer que $M$ est un module de torsion. Si de plus $M$ est linéairement compact, montrer que $M$ est artinien (si $N$ est le noyau de l'endomorphisme $x\longrightarrow\pi x$, observer que $N$ est linéairement compact et discret, et peut être considéré comme $(A/\pi A)$-espace vectoriel ; utiliser alors l'exerc. 20 d) du chap. II, \S 2).

b) Déduire de a) que tout $A$-module topologique linéairement compact est strictement linéairement compact (chap. II, \S 2, exerc. 19).

c) On appelle \uline{dual torique topologique} d'un $A$-module topologique $M$ le sous-module $M'$ du dual torique algébrique $M^*$, formé des homomorphismes continus de $M$ dans $K/A$ (ce dernier étant muni de la topologie discrète). Si la topologie de $M$ est linéaire (chap. II, \S 2, exerc. 14) et si $N$ est un sous-module fermé de $M$, montrer que le dual torique topologique de $M/N$ s'identifie à $N^\circ\cap M'$ et celui de $N$ à $M'/(N^\circ\cap M')$ (pour déterminer le dual de $N$, remarquer que pour tout homomorphisme continu $u$ de $N$ dans $K/A$, il existe un sous-module ouvert $U$ de $M$ tel que $u(x)=0$ dans $N\cap U$, puis utiliser l'exerc. 9).

d) Pour un $A$-module topologique $M$ de rang fini, le dual torique topologique $M'$ est égal au dual torique algébrique $M^*$ (se ramener au cas des modules de rang un).

e) Soit $M$ un $A$-module topologique séparé dont la topologie est linéaire ; montrer que pour tout $x\ne0$ dans $M$, il existe un $u\in M'$ tel que $u(x)\ne0$ (remarquer qu'il existe un sous-module ouvert $U$ de $M$ tel que $x\in U$) ; autrement dit, l'application canonique $M\longrightarrow(M')^*$ est injective. En déduire que si $N$ est un sous-module fermé de $M$, $N^\circ\cap M'$ est dense dans $N^\circ$ pour la topologie $\sigma(M^*,M)$ (utiliser d)), et par suite on a $N=M\cap(N^\circ\cap M')^\circ$ dans $M^{**}$. Montrer que $M$ est dense dans $(M')^*$ pour la topologie $\sigma((M')^*,M')$.
\mspage{15}
''',[
('text','top centre','-- 47 --'),('margin note','top right','n° 387'),
('text','first block','f) Soient M, N deux A-modules'),
('text','above a)','10) Les hypothèses et notations'),
('text','upper middle','a) Si M est un A-module topologique discret'),
('text','middle','b) Déduire de a)'),
('text','middle-lower','c) On appelle dual torique topologique'),
('text','lower','d) Pour un A-module topologique M de rang fini'),
('text','bottom block','e) Soit M un A-module topologique séparé'),
('margin note','bottom left','15')
],[('e), parenthesis after u(x)≠0','x∈U','The visible membership sign has no confident negation stroke; retained despite the surrounding argument.','high')],['The reused typescript’s 10e visibly says x∈U where separation may suggest x∉U; retained for research reading question.'],sheet_kind='reused_typed')

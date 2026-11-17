from record_page import record
record(3,r'''
\scanpage{3}
% archive foliation: 2
\uline{Cor} Conditions équivalentes

 a) $C=C_\infty$ i.e. pour $\forall x\in C$, l'ens des longueurs des parties partant de $x$ est fini.

 b) $\exists\ C\xrightarrow{l}\mathbb N$ tel que si $y\in R(x)$, on ait $l(y)<l(x)$

[Alors $\forall x\in C$, si $l=l(x)$, on a $x\in C_l$]

\deleted{\unsure{Impl.}}

\uline{NB} Ces conditions impliquent que $\nexists$ partie infinie.
\deleted{Mais} Si $C$ est \deleted{\unsure{in}}fini, \deleted{\unsure{l'inverse est vrai}}\inserted{la réciproque est vraie} : en effet, tte partie \deleted{\unsure{est finie}}\inserted{a alors une longueur} \unsure{au plus} $(\operatorname{card}C)-1=N-1$, i.e. $C=C_{N-1}$

\deleted{\uline{Prop} Si $C$}

\textcircled{3} \uline{Stratégie pour $j\in J$}
\[
\Sigma\subset(C(j)\times C)\cap R\quad\text{tel que}
\]
\[
\forall x\in C(j),\quad\text{on a}\quad(R(x)\ne\varnothing\ (\text{i.e. }x\notin C_0)\Longrightarrow\Sigma(x)\ne\varnothing)
\]
Partie $\underline x=(x_0,\ldots,x_n)$ \uline{compatible} avec stratégie $\Sigma$ pour $j$ :
\[
\forall\,0\leq i\leq n-1\quad\text{tel que }x_i\in C(j),\quad\text{on a }x_{i+1}\in\Sigma(x_i)
\]
\margin{Idem pour parties \unsure{infinies}}

\uline{Stratégie gagnante} \inserted{(pour $j$)} pour $x$ $(\in C)$ :

 a) Toute partie partant de $x$, compatible avec $\Sigma$, est finie

(i.e. $\nexists$ partie infinie partant de $x$, comp. avec $\Sigma$)

 b) \inserted{pour} Toute partie terminée, partant de $x$, \inserted{$(x_0=x,x_1,\ldots,x_n)$} compatible avec $\Sigma$, on a $x_n\in G_0(j)$.

On dit que $x\in C$ est \uline{gagnante} \uline{pour} $j$ si $\exists$ stratégie \deleted{gagnante}\inserted{pour $j$} gagnante pour $x$.
L'ens des ces $x$ est noté $G(j)$

\uline{NB} $G(j)\cap C_0=G_0(j)$

Posons $\overline C(j)=C\setminus C(j)$, $\overline G(j)=C\setminus G(j)$\ldots
''',[
('text','top','Cor Conditions équivalentes'),('text','upper a','C=C_infty i.e. pour forall x in C'),('display','upper b','exists C ->^l N; l(y)<l(x)'),('text','upper bracket','Alors forall x in C; l=l(x); x in C_l'),
('deletion','upper-middle','Impl.'),('text','upper-middle','NB Ces conditions impliquent que no partie infinie'),('text','upper-middle','Si C est fini; en effet tte partie ...'),('deletion','upper-middle','Mais; in; l’inverse est vrai; est finie'),('insertion','above previous paragraph','la réciproque est vraie; a alors une longueur'),('display','upper-middle end','(card C)-1=N-1; C=C_(N-1)'),('deletion','middle-left','Prop Si C'),
('text','middle','3 Stratégie pour j in J'),('display','middle','Sigma subset (C(j) x C) cap R'),('display','middle','forall x in C(j); R(x) nonempty implies Sigma(x) nonempty'),('text','middle-lower','Partie x=(x_0,...,x_n) compatible'),('display','middle-lower','forall 0<=i<=n-1; x_(i+1) in Sigma(x_i)'),('margin note','middle-right','Idem pour parties infinies'),('text','lower','Stratégie gagnante pour x'),('insertion','above gagnante','pour j'),('text','lower a','Toute partie partant de x ... est finie'),('text','lower a parenthesis','i.e. no partie infinie ... comp. avec Sigma'),('text','lower b','Toute partie terminée ... x_n in G_0(j)'),('insertion','above b','pour; (x_0=x,x_1,...,x_n)'),('text','bottom','On dit que x in C est gagnante pour j'),('deletion','bottom','gagnante'),('insertion','bottom','pour j'),('text','bottom','L’ens des ces x est noté G(j)'),('display','bottom','NB G(j) cap C_0=G_0(j)'),('text','bottom edge','Posons Cbar(j)=C\\C(j), Gbar(j)=C\\G(j)...')
],'''C=C_infty is equated to a strictly decreasing N-valued length function. Finite C allows the converse from no infinite play and gives C=C_(N-1), N=card C. Strategies are relations, not necessarily deterministic maps; winning requires both termination and a winning terminal endpoint. Terminal compatibility condition is explicitly present even after initiative was restricted on scan 002. The upper correction around “a alors une longueur” is hard to read and retained with doubt.''')

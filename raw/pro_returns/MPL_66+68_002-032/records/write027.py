from record_page import record
record(27,r'''\scanpage{27}
C'est une $j$-stratégie, \deleted{prouvons} \inserted{Prouvons} qu'elle est gagnante pour $x_0$. \deleted{\unsure{ou}} Une partie maximale jouée suivant $\Sigma_0$ \unsure{commence} avec $(x_0,x_1)$, soit $(x_0,x_1,\ldots,x_m,\ldots)$ \deleted{les $x_i$ $(i\geq1)$ sont \unsure{gagnants} pour $\Sigma_1$}, prouvons qu'elle est gagnée par $j$. Prouvons que tous les $x_i$ $(i\geq1)$ sont $\ne x_0$. Sinon, \deleted{si $i$ est le} plus petit indice $i\geq1$ tel que $x_i=x_0$, \deleted{pour un $\unsure{i>1|j>1}$}, alors \deleted{par la prop. \unsure{il s'ensuivrait}} \inserted{$(x_1,\ldots,x_i=x_0)$ serait compatible avec $(\Sigma_1)$,} on aurait que $\deleted{x_i}\inserted{{}=x_0}$ est gagnant pour $\Sigma_1$, contrairement à la supposition que $x_0$ non gagnant pour $\Sigma_1$.

Comme les $x_i$ $(i\geq1)$ sont $\ne x_0$, la partie $(x_1,x_2,\deleted{\unsure{x_0}}\inserted{\ldots})$ est une $\Sigma_1$-partie, donc elle est gagnante pour $j$, donc $(x_0,x_1,\ldots)$ aussi; cqfd.

b) On suppose $x_0\in\bar C(j)$.

1) $\subset$. Supposons $x_0\in G(j)$, prouvons $R(x)\subset G(j)$, Soit $x_1\in R(x)$, prouvons $x_1\in G(j)$. En effet, \inserted{si $\Sigma_0$ est une $j$-stratégie $x_0$-gagn.}, $(x_0,x_1)$ est une \inserted{$\Sigma_0$-}partie, donc par la prop., $x_1$ est gagnant pour $\Sigma_0$, donc $x_1\in G(j)$.

2) $\supset$. Supposons $R(x_0)\subset G(j)$, prouvons $x_0\in G(j)$. $\forall x_1\in R(x_0)$, soit $\Sigma_{x_1}$ une $j$-stratégie $x_1$-gagnante. Choisissons un \uline{bon ordre} sur $R(x_0)$. On va définir une $j$-stratégie $\Sigma_0$ $x_0$-gagnante ainsi :

$\forall x\in C$, soit
\[
E(x)=\{x_1\in R(x_0)\mid\exists\ \Sigma_{x_1}\text{-partie de }\unsure{x_1|x_0}\text{ à }x\}
\]
% archive foliation: 26
''',[
('text','top','C’est une j-stratégie ...'),
('deletion','top','prouvons; ou'),
('insertion','top','Prouvons'),
('text','upper','Une partie maximale ... commence avec (x_0,x_1) ...'),
('deletion','upper','les x_i (i≥1) sont gagnants pour Σ_1'),
('text','upper middle','Prouvons que tous les x_i ...'),
('deletion','upper middle','si i est le; pour un i>1; par la prop. il s’ensuivrait'),
('insertion','middle','(x_1,...,x_i=x_0) serait compatible avec (Σ_1)'),
('deletion','middle','x_i'),
('insertion','middle',' =x_0'),
('text','middle','Comme les x_i ... la partie (x_1,x_2,...) ... cqfd'),
('deletion','middle','x_0 in tuple'),
('insertion','middle','ellipsis in tuple'),
('text','lower','b) On suppose x_0∈bar C(j). 1) ⊂ ...'),
('insertion','lower right','si Σ_0 est une j-stratégie x_0-gagn.'),
('insertion','lower','Σ_0-'),
('text','bottom','2) ⊃ Supposons R(x_0)⊂G(j) ... bon ordre ...'),
('text','bottom','∀x∈C, soit'),
('display','bottom edge','E(x)={x_1∈R(x_0)|∃Σ_{x_1}-partie de x_1 à x}')
],'''The first half completes the nonreturn argument for the modified strategy. In the universal-predecessor converse the author now explicitly well-orders R(x_0), chooses individual strategies Σ_{x_1}, and defines reachable-source sets E(x). This is a substantive revision of the cancelled well-order attempt in scan 7, so the next page must be checked for actual stabilization and termination, rather than presuming the earlier shortcut has been repaired. The source index in the final E(x) definition is overwritten and remains marked uncertain.''')

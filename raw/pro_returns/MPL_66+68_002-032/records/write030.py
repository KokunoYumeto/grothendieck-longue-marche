from record_page import record
record(30,r'''\scanpage{30}
\[
\Sigma'(x)=\begin{cases}
R(x)&\text{si }x\in C(j)\cup G(j)\\
R(x)\cap\complement G(j)&\text{si }x\in\bar C(j)\cap\complement G(j)
\end{cases}
\]
(C'est une stratégie contre $j$, par [b) $\supset$]. Alors Pour $x\in C$, les conditions suivantes sont équivalentes

a) $x_0\notin G(j)$

b) $x_0$ est admissible contre $j$

c) $x_0$ est admissible pour $\Sigma'$ contre $j$.

\uline{Dém}\quad c) $\Longrightarrow$ b) trivial, b) $\Longrightarrow$ a) par le lemme, Prouvons a) $\Longrightarrow$ c). \unsure{Si on a} une partie $(x_0,x_1,\ldots)$ d'origine $x_0$ jouée en accord avec $\Sigma'$, alors par définition de $\Sigma$, on voit de proche en proche que $x_i\in\complement G(j)$ $\forall i$, donc la partie ne peut être gagnée par $j$ !

\uline{Corollaire}\quad Supposons $J=\{j,j'\}$, $j\ne j'$, et
\margin{$\big|$}
\[
G_0(j)\cap G_0(j')=\varnothing.
\]
Soit \deleted{$\unsure{N}$}
\[
N=\{x\in C\mid x\text{ admissible contre }j,\text{ et contre }j'\}.
\]
\margin{$\big|$}
Alors $C$ est réunion disjointe de $G(j)$, $G(j')$ et $N$.
% archive foliation: 29
''',[
('display','top','Σ′(x)=R(x) if ... / R(x)∩complement G(j) if ...'),
('text','upper','C’est une stratégie contre j ... conditions suivantes ...'),
('text','middle','a) x_0∉G(j); b) x_0 est admissible contre j; c) ... Σ′ ...'),
('text','middle lower','Dém c)⇒b) trivial ... a)⇒c) ...'),
('text','lower','Corollaire Supposons J={j,j′}, j≠j′, et'),
('margin note','lower left','vertical emphasis mark'),
('display','lower','G_0(j)∩G_0(j′)=∅'),
('text','lower','Soit'),
('deletion','lower','N'),
('display','bottom','N={x∈C|x admissible contre j, et contre j′}'),
('margin note','bottom left','vertical emphasis mark'),
('text','bottom','Alors C est réunion disjointe de G(j), G(j′) et N')
],'''The fixed coalition strategy keeps a play outside G(j), proving the equivalence between not winning and admitting an anti-j avoidance strategy. Infinite play is permitted, so this is a reachability-versus-safety conclusion, not a claim that all positions are won by one player. The two-player corollary needs only disjoint terminal winning sets, not that they exhaust C_0; it partitions C into the two winning regions and a residual N. “par définition de Σ” is unprimed in the proof, although the displayed strategy is Σ′; retained literally.''')

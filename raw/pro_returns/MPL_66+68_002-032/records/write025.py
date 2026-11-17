from record_page import record
record(25,r'''\scanpage{25}
\[
\Sigma(x)\subset R(x),\qquad\Sigma(x)\ne\varnothing.
\]
Cette notion ne dépend que de $C,R,C(j)\subset C\setminus C_0$.

\inserted{\uline{NB} On pose $\Sigma(x)=R(x)$ si $x\in\bar C(j)$. Donc on peut interpréter $\Sigma$ comme une application $C\setminus C_0\longrightarrow\mathcal P^*(C)$, $\Sigma(x)\subset R(x)$ et $\Sigma(x)\ne\varnothing$ $\forall x\in C\setminus C_0$, et $\Sigma(x)=R(x)$ si $x\in\bar C(j)$.}
\deleted{\uline{Stratégie \unsure{pour $j$} gagnante pour $x_0\in C$}}

\uline{Partie jouée en accord avec une Stratégie $\Sigma$} (ou \uline{compatible} avec $\Sigma$, ou $\Sigma$-partie) : cette notion est stable par composition. (On prend une sous-catégorie ayant mêmes objets, mais a priori moins de flèches)

\inserted{\uline{Lemme} Soit \deleted{\unsure{une stratégie}} $J'\subset J$, $\forall j\in J'$ soit $\Sigma_j$ une $j$-stratégie. Soit $x_0\in C$. Alors $\exists$ partie maximale d'origine $x_0$, comp. avec les $\Sigma_j$ $(j\in J')$.}

\uline{Stratégie $\Sigma$ (pour $j$) gagnante pour $x_0\in C$} (ou \uline{position} $x_0$ \uline{gagnante} pour une Stratégie $\Sigma$) : toute partie maximale commençant en $x_0$, et jouée suivant $\Sigma$, est gagnée par $j$ (i.e. est finie, et son extrémité $x_n\in C_0$ est $\in G_0(j)$).
\margin{ne dépend que de $C,R,C(j),G_0(j)$}

\uline{Position \inserted{$x_0\in C$} gagnante pour $j$} : telle qu'il existe une $j$-Stratégie qui soit gagnante pour $x_0$. Soit
\[
G(j)
\]
l'ens de ces positions. On a
\[
G(j)\cap C_0=G_0(j).
\]

[\uline{Proposition} Soit $J'\subset J$. Si $\bigcap_{j\in J'}G(j)\ne\varnothing$, alors $\bigcap_{j\in\unsure{J|J'}}G_0(j)\ne\varnothing$. En d'autres termes, si $\bigcap_{j\in J'}G_0(j)=\varnothing$, alors $\bigcap_{j\in J'}G(j)=\varnothing$ i.e. un $x_0\in C$ ne peut être gagnant pour tous les $j\in J'$.

Immédiat par le lemme.]
% archive foliation: 24
''',[
('display','top','Σ(x)⊂R(x), Σ(x)≠∅'),
('text','upper','Cette notion ne dépend que de C,R,C(j)⊂C minus C_0'),
('insertion','upper','NB On pose Σ(x)=R(x) si x∈bar C(j) ...'),
('deletion','upper','Stratégie pour j gagnante pour x_0∈C'),
('text','upper middle','Partie jouée en accord avec une Stratégie Σ ... sous-catégorie ...'),
('insertion','middle','Lemme Soit J′⊂J ... partie maximale ...'),
('deletion','inside lemma','une stratégie'),
('text','middle lower','Stratégie Σ (pour j) gagnante pour x_0∈C ...'),
('margin note','left','ne dépend que de C,R,C(j),G_0(j)'),
('text','lower','Position gagnante pour j ...'),
('insertion','lower','x_0∈C'),
('display','lower','G(j)'),
('text','lower','l’ens de ces positions. On a'),
('display','lower','G(j)∩C_0=G_0(j)'),
('text','bottom','[Proposition Soit J′⊂J ... intersections ...'),
('text','bottom edge','Immédiat par le lemme.]')
],'''A lemma asserts existence of a maximal play simultaneously compatible with one strategy for every player in an arbitrary coalition J′. It underlies the bracketed proposition that nonempty intersection of winning regions implies nonempty intersection of terminal winning regions; this does not assume exclusive winners. The second intersection index looks unprimed J and is marked uncertain rather than repaired. The compatibility lemma has no proof here; choice and maximal-play conventions could matter for infinite positions/coalitions. The inserted strategy extension to all nonterminal positions is explicit.''')

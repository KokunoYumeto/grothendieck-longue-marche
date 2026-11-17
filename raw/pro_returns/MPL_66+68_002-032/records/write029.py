from record_page import record
record(29,r'''\scanpage{29}
et comp. avec $\Sigma_0$
\[
(x_0,x_1,x_2,\ldots)
\]
Par le lemme, on voit de proche en proche \deleted{cette partie est} \inserted{(puisque $x_1\in C'$)} que \deleted{$x_1\in G(j)$, $x$} les $x_i$ $(i\geq1)$ sont $\in C'\deleted{\cap G(j)}$ donc $j$-gagnants. Pour montrer que la partie est gagnée par $j$, il suffit de prouver qu'elle est finie. \deleted{Or} \inserted{Supposons le contraire.} Les $\varepsilon(x_i)$ $(i\geq1)$ forment une suite décroissante d'éléments de $R(x_0)$, donc stationnaire. Soit $n$ tel que $\varepsilon(x_m)=\varepsilon(x_n)\inserted{(=\unsure{\xi|\zeta})}$ pour $m\geq n$.

Alors par définition de $\Sigma_0$, la partie $(x_n,x_{n+1},\ldots,\ )$ est une partie comp. avec $\Sigma_{\unsure{\xi|\zeta}}$. Comme $x_n$ est gagnant pour $\Sigma_{\unsure{\xi|\zeta}}$ (par le lemme), cette partie est finie, absurde.

Stratégie \uline{contre $j$} (\unsure{stratégie relative à} $\bar C(j)$, i.e. $\Sigma'$ telle que $\Sigma'(x)=R(x)$ si $x\in C(j)$ (et $\Sigma'(x)\subset R(x)$, $\Sigma'(x)\ne\varnothing$ si $x\in\bar C(j)$) admissible pour $x_0$ (tte partie maximale d'origine $x_0$ jouée suivant $\unsure{x_0|\Sigma'}$ est \uline{non gagnée} par $j$, i.e. est ou bien infinie, ou bien a une position terminale $\notin\unsure{C_0|G_0}(j)$).

\deleted{\uline{Corollaire}} \inserted{Théorème} Soit $\Sigma'$ la stratégie contre $j$ définie par
% archive foliation: 28
''',[
('text','top','et comp. avec Σ_0'),
('display','top','(x_0,x_1,x_2,...)'),
('text','upper','Par le lemme, on voit de proche en proche ...'),
('deletion','upper','cette partie est; x_1∈G(j), x; ∩G(j)'),
('insertion','upper','puisque x_1∈C′'),
('text','middle','Pour montrer ... il suffit de prouver qu’elle est finie ...'),
('deletion','middle','Or'),
('insertion','middle','Supposons le contraire.'),
('text','middle','Les ε(x_i) ... suite décroissante ... stationnaire'),
('insertion','middle lower','(=ξ)'),
('text','lower middle','Alors par définition de Σ_0 ... finie, absurde'),
('text','lower','Stratégie contre j ... admissible pour x_0 ...'),
('deletion','bottom','Corollaire'),
('insertion','bottom','Théorème'),
('text','bottom edge','Soit Σ′ la stratégie contre j définie par')
],'''The infinite-play contradiction is completed: the weakly decreasing least-source sequence is eventually constant in a well-order, after which the tail follows one fixed winning strategy. This is stronger than the first draft’s explicit admission of finiteness on scan 6 and must be compared under the same arbitrary/infinite-game hypotheses. The following definition switches the earlier word “acceptable” to “admissible” for a coalition strategy preventing j’s terminal win, allowing infinite plays. The apparent x_0 after “suivant” and C_0(j) after the terminal condition remain doubtful literal readings, not repaired to Σ′ and G_0(j).''')

from record_page import record
record(28,r'''\scanpage{28}
Soit
\[
C'=\{x\in C\mid E(x)\ne\varnothing\}
\]
et pour $x\in C'$, posons
\[
\varepsilon(x)=\text{plus petit élément de }E(x)
\]
(donc $\varepsilon:C'\longrightarrow R(x_0)$). Posons
\[
\Sigma_0(x)=\begin{cases}
R(x)&\text{si }\deleted{\unsure{\forall}}x\in\bar C(j)\cup\complement C'\\
\Sigma_{\varepsilon(x)}(x)&\text{si }x\in C(j)\cap C'
\end{cases}
\]
Donc $\Sigma_0$ est une $j$-Stratégie. On va prouver qu'elle est gagnante pour $x_0$.

\uline{Lemme}\quad \deleted{On a} \inserted{Si $x\in C'$, $x$ est gagnant pour $\Sigma_{\varepsilon(x)}$ (donc gagnant pour $j$ --- donc $C'\subset G(j)$) et} \deleted{$C'\subset G(j)$, et si $x\in C'$, $y\in\Sigma_0(x)$,} alors \deleted{$\Sigma_0(x)\subset C'$ et} pour tout $y\in\Sigma_0(x)$, on a
\[
E(y)\ni\unsure{\varepsilon(x)|E(x)}
\]
(donc $E(y)\ne\varnothing$ donc $y\in C'$, donc $\Sigma_0(x)\subset C'\inserted{\subset G(j)}$) et par suite
\[
\varepsilon(y)\leq\varepsilon(x).
\]

\uline{Dém}\deleted{\unsure{cq}}
Soit $x\in C'$ donc $E(x)\ne\varnothing$, alors si $x_1\in E(x)$ $\exists$ \deleted{partie} $\Sigma_{x_1}$-partie de $x_1$ à $x$, donc par la prop. (comme $\Sigma_{x_1}$ est $x_1$-gagnante), $x$ est $\Sigma_{x_1}$-gagnante, donc à fortiori $x\in G(j)$.

Soit $y\in\Sigma_0(x)=\Sigma_{\varepsilon(x)}(x)$
\[
(\underset{\substack{\Vert\\\varepsilon(x)}}{x_1},x_2,\ldots,x_m=x,x_{\unsure{m+1|m-1}}=y)
\]
est une $\Sigma_{\varepsilon(x)}$-partie, donc \deleted{$\unsure{\varepsilon_0}$} $\varepsilon(x)\in E(y)$, OK.

Prouvons que $\Sigma_0$ est gagnante pour $x_0$.
Soit une partie maximale commençant par $x_0$
% archive foliation: 27
''',[
('text','top','Soit'),
('display','top','C′={x∈C|E(x)≠∅}'),
('text','upper','et pour x∈C′, posons'),
('display','upper','ε(x)=plus petit élément de E(x)'),
('text','upper middle','donc ε:C′→R(x_0). Posons'),
('display','middle','Σ_0(x)=R(x) if ... / Σ_{ε(x)}(x) if ...'),
('deletion','inside definition','∀'),
('text','middle','Donc Σ_0 est une j-Stratégie ...'),
('text','middle lower','Lemme ... alors pour tout y∈Σ_0(x) ...'),
('deletion','middle lower','On a; C′⊂G(j), et si x∈C′, y∈Σ_0(x); Σ_0(x)⊂C′ et'),
('insertion','middle lower','Si x∈C′ x est gagnant pour Σ_{ε(x)} ...'),
('display','lower','E(y)∋ε(x)'),
('text','lower','donc E(y)≠∅ ... et par suite'),
('insertion','lower','⊂G(j)'),
('display','lower','ε(y)≤ε(x)'),
('text','lower','Dém Soit x∈C′ ...'),
('deletion','lower','cq; partie'),
('text','bottom','Soit y∈Σ_0(x)=Σ_{ε(x)}(x)'),
('display','bottom','(x_1=ε(x),x_2,...,x_m=x,x_{m+1}=y)'),
('text','bottom','est une Σ_{ε(x)}-partie, donc ... OK'),
('deletion','bottom','ε_0'),
('text','bottom edge','Prouvons que Σ_0 est gagnante pour x_0. Soit une partie ...')
],'''The chosen least reachable source ε(x) yields a piecewise positional strategy, the invariant C′, and the inequality ε(y)≤ε(x) along its moves. The lemma’s membership sign is drawn as ∋, not an inclusion of all E(x); this distinction is important to the proposed stitching argument. Its proof invokes the earlier propagation proposition. A stabilization argument is still needed on scan 29; one should not claim that the weakly decreasing selector itself is a strictly decreasing termination rank.''')

from record_page import save
save(15,219,'manuscript',r'''
\mspage{218}
$X$ \deleted{schéma} préschéma de type fini \inserted{normal} irréductible sur corps $k$

$v,w$ deux places archimédiennes de \deleted{\unsure{le}} $X$, d'où
foncteurs fibres $\xi_v^{\mathbb Z},\xi_w^{\mathbb Z}$. Question : a) \inserted{Quand} sont-ils
isomorphes ? b) \deleted{Est-il vrai que} Quand est-il
vrai que pour tte sous-catégorie \inserted{mult.} de t.f. de
$\mathbb M(X)$, les restrictions de ces foncteurs à
$\mathbb M_\alpha(X)$ sont isomorphes ?

Nous pouvons supposer, quitte à remplacer $k$ par
\deleted{\unsure{Soit déjà les}}
sa clôture alg. dans $k(X)$, que $k$ est alg.
clos dans $k(X)$ [utilise le fait $X$ \uline{normal} !],
donc $X$ est géom\textsuperscript{t} irred. sur $k$. Soit \deleted{$k_0$}
\inserted{$k_0$ la clôture alg. de $\mathbb Q$ dans $k$.}
\deleted{le corps \unsure{de définition} des places (= \unsure{sur $k_0$}).
\uline{induites sur $k_0$}
\illegible{1}
\uline{Contient la clôture alg. $E$ de $\mathbb Q$ dans $k$} (p.ex. $k_0$ alg. fermé dans $k$).
1) $k_0$ est algébriquement fermé dans $k$. Alors}

1°) $v,w$ coïncident sur $k_0$.
\[
\text{a) }\xi_v^{\mathbb Z}|\mathbb M_\alpha(X)\simeq\xi_w^{\mathbb Z}|\mathbb M_\alpha(X)
\quad\text{pour }\forall\alpha.
\]
En effet, $X$ et $\mathbb M_\alpha(X)$ proviennent de
$X_0$, \inserted{$\mathbb M_\alpha(X_0)$}, de type fini sur $A_0$, \inserted{$k_0$}\unsure{-alg.} de
\deleted{$X_0\longrightarrow\operatorname{Spec}A_0$ fid plat \unsure{univers\textsuperscript{t}} connexe, $\operatorname{Spec}A_0\longrightarrow k$ $^{*}$}
type fini de $k_0$ \deleted{$\unsure{E}$}. On est ramené
au cas où $k=k_0$, où on obtient le
résultat voulu grâce au groupoïde fondamental
transcendant. \deleted{\unsure{Alors}}

\margin{\diagram{\begin{tikzcd}[row sep=small,column sep=small]
&X_0\arrow[r,no head]\arrow[d,no head]&X\arrow[d,no head]\\
k_0\arrow[r,no head]&A_0\arrow[r,no head]&k
\end{tikzcd}}}

\margin{\deleted{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node (E) at (0,1) {$E$};\node (k0) at (1.1,1) {$k_0$};
\node (A0a) at (2.1,1) {$\unsure{A_0}$};\node (k) at (3.2,1) {$k$};
\node (X0a) at (2,2.4) {$\unsure{X_0}$};\node (X0) at (1.7,2) {$X_0$};\node (X) at (3.2,2.4) {$X$};
\node (A0) at (1.9,.25) {$A_0$};\node (Q) at (1,-.2) {$\mathbb Q$};\node (Eb) at (2.9,-.2) {$E$};
\draw (E)--(k0)--(A0a)--(k);\draw (X0a)--(X)--(k);\draw (X0)--(A0a);\draw (Q)--(k0)--(X0);
\draw[->] (E)--(A0);\draw (Q)--(Eb);\draw (A0)--(X0a);
\foreach \x in {1.2,1.4,1.6,1.8,2,2.2,2.4}{\draw (\x,.6)--(\x+.6,2);}
\draw (.1,.9) .. controls (.4,-.8) and (3.9,-.4) .. (3.1,1.8);
\draw (1,-.4) .. controls (3.8,-.5) and (4,.4) .. (2.4,.5);
\end{tikzpicture}}}}

b) Si \deleted{$\unsure{k=k_0}$}\inserted{$v$ et $w$ coïncident sur $k$}, cet argument montre que
$\xi_v^{\mathbb Z}\simeq\xi_w^{\mathbb Z}$.
\inserted{Sinon,} \unsure{mais rien ne prouve qu'on ait}
\deleted{Si $k\ne k_0$, \unsure{je pense que} $\xi_v^{\mathbb Z}\ne\xi_w^{\mathbb Z}$ ; \illegible{2}}

\margin{$^{*}$ on peut supposer $X_0\longrightarrow\operatorname{Spec}A_0$ fid plat \unsure{univers\textsuperscript{t} connexe}, et
$\operatorname{Spec}(A_0)\mathrel{\text{---}}k_0$ \unsure{géom. connexe}, donc $X_0\mathrel{\text{---}}\operatorname{Spec}k_0$ \unsure{géom. connexe}.}
''',[
('text','top','X préschéma de type fini normal irréductible sur corps k'),
('text','upper','v,w deux places archimédiennes; Question a), b)'),
('text','middle','Nous pouvons supposer; clôture algébrique dans k(X)'),
('text','middle heavily revised','Soit k_0; clôture algébrique de Q dans k; corps des places'),
('text','middle-lower','1°) v,w coïncident sur k_0'),
('display','middle-lower','a) restrictions xi_v^Z and xi_w^Z to M_alpha(X)'),
('text','lower','En effet, X et M_alpha(X) proviennent de X_0'),
('diagram','left lower margin, upper','X_0--X over k_0--A_0--k'),
('diagram','left lower margin, lower heavily cancelled','E,k_0,A_0,k,X_0,X,Q and cancellation hatching'),
('text','bottom','b) Si v et w coïncident sur k; otherwise revision'),
('text','footnote at bottom edge','on peut supposer X_0 to Spec A_0 fid plat'),
('text','bottom left','218')], 'Dense overlapping deletions inspected at enlarged scale. Some words and deletion/insertion boundaries remain uncertain; cancelled diagram reproduced schematically with visible labels and cancellation strokes.')

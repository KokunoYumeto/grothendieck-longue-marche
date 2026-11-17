from record_page import record
record(17,r'''\scanpage{17}
\[
E_i=[\unsure{-i|i},i]\qquad0\leq i\leq m
\]
\margin{NB $E_m=G$, $E_{\unsure{1|0}}=\varepsilon$}
\[
F_j=[m-j,m+1+j]\qquad0\leq j\leq m-1\qquad F_m=E_m=G
\]
\inserted{\[
E_i\ast E_j=\sum\alpha_{ij}^h E_h\qquad\alpha_{ij}^h\geq0
\]}
\[
F_i\ast F_j=\sum_0^m\beta_{ij}^h E_h\qquad\beta_{ij}^h\geq0
\]
\[
E_i\ast F_j=\sum\gamma_{ij}^h F_h
\]
\margin{$\varepsilon=\varepsilon^{-1}$\quad\deleted{$\unsure{\varepsilon}$}}
\[
\mathcal A(\uline{g,\deleted{\unsure{\delta}}\varepsilon})=
\left\{\begin{array}{ll}
\dfrac g2\ast\mathcal A(0)&\text{si }\varepsilon=+1\\
\dfrac g2\ast\mathcal B(0)&\text{si }\varepsilon=-1
\end{array}\right.
\]
\[
\mathcal A(\tilde g)\ast\mathcal A(\tilde h)\unsure{\subset|\subseteq}\mathcal A(\tilde g\cdot\tilde h)
\]

% The following portion is written in the opposite orientation.
\deleted{$\unsure{G'}\quad G'\text{ groupe}\quad G'\xrightarrow{\lambda}G$}
\[
\tilde G\text{ gr}\qquad\tilde G\xrightarrow{\rho}G\quad\text{hom.}
\]
\[
i:{}_2G\simeq\operatorname{Ker}\rho
\]
\margin{\deleted{\unsure{f}}\quad
$\begin{aligned}
A&=g\ast\unsure{\check A|\tilde A}=\check A\ast g\\
B&=h\ast\check B=\check B\ast h\\
A\ast B&=g\ast\check A\ast h\ast\check B=\unsure{g\ast\check A\ast\check B\ast h}
\end{aligned}$}
\[
\forall\tilde g\in G\qquad\mathcal A(\tilde g)\subset\mathcal P_f(G),
\]
\margin{On pose $C(\tilde g)$ cône des
$\displaystyle\sum_{A\in\mathcal A(\tilde g)}\alpha_A\unsure{A_\ast|A}$, $\alpha_A\geq0$}

a) $\mathcal A(\tilde g)$ \unsure{tot} ordonné

b) $A\in\mathcal A(\tilde g)\Longrightarrow A=\deleted{\unsure{\rho(\tilde g)}}g\ast\check A$ où $g=\rho(\tilde g)$
\margin{$\forall\tilde g\in\tilde G$}

c) $A\in\mathcal A(\tilde g),\ B\in\mathcal B(\tilde h)\Longrightarrow A\ast B\in C(\tilde g\tilde h)$
\margin{$\forall\tilde g,\tilde h\in\tilde G$}

d) Si $u\in{}_2G$, $\tilde g\in G$, \unsure{$\ldots$}

\deleted{d) $\mathcal A(\tilde g\tilde u^2)=\tilde u\ast\mathcal A(\tilde g)\quad\mathcal A(\unsure{\tilde u\tilde g})=$}
$\mathcal A(i(u)\tilde g)=u\ast\mathcal A(\tilde g)$

d) $\forall\tilde g,\tilde h\in\tilde G\quad\exists s\in G$ tel que $\mathcal A(\tilde g)\cup\unsure{\varepsilon_s|s}\mathcal A(\tilde h)$ tot. ordonné

[i.e. $\bigcup\mathcal A_g$
% archive foliation: 16
''',[
('display','top','E_i=[−i,i], 0≤i≤m'),
('margin note','upper right','NB E_m=G, E_1=ε'),
('display','upper','F_j=[m−j,m+1+j]; F_m=E_m=G'),
('insertion','upper left curved arrow','E_i*E_j=ΣαE_h; α≥0, moved ahead of F_i*F_j'),
('display','upper','F_i*F_j=ΣβE_h; β≥0'),
('display','upper middle','E_i*F_j=ΣγF_h'),
('margin note','upper right','ε=ε^{−1}'),
('deletion','upper right','ε'),
('display','upper middle','A(g,ε)=g/2*A(0) or g/2*B(0)'),
('deletion','inside argument of A','δ'),
('display','middle','A(g̃)*A(h̃)⊂A(g̃h̃)'),
('deletion','opposite orientation, first line','G′ groupe; G′→G'),
('display','opposite orientation, top','G̃ gr; G̃→G hom.; i:₂G≃Kerρ'),
('margin note','opposite orientation, upper right','A=g*check A; B=h*check B; A*B=...'),
('deletion','opposite orientation, upper right','f'),
('display','opposite orientation, upper','∀g̃∈G A(g̃)⊂P_f(G)'),
('margin note','opposite orientation, middle right','On pose C(g̃) cône des Σα_A A_*'),
('text','opposite orientation, middle','a) A(g̃) tot ordonné'),
('display','opposite orientation, middle','b) A∈A(g̃)⇒A=g*check A'),
('deletion','within b','ρ(g̃)'),
('margin note','next to b and c','∀g̃∈G̃; ∀g̃,h̃∈G̃'),
('display','opposite orientation, lower','c) A∈A(g̃),B∈B(h̃)⇒A*B∈C(g̃h̃)'),
('text','opposite orientation, lower','d) Si u∈₂G, g̃∈G'),
('deletion','opposite orientation, lower','d) A(g̃ũ²)=ũ*A(g̃); A(ũg̃)='),
('display','opposite orientation, lower','A(i(u)g̃)=u*A(g̃)'),
('text','opposite orientation, bottom','d) ∀g̃,h̃ ... ∃s ... tot. ordonné'),
('display','opposite orientation, bottom','[i.e. ∪ A_g')
],'''The upper half proposes convolution expansions with nonnegative alpha/beta coefficients for intervals E_i,F_j and a signed/half-translate construction of script A. The lower half sketches an extension tilde G→G with kernel identified with 2-torsion, ordered families A(g), positive cones C(g), symmetry A=g*check A, convolution closure, torsion translation, and a common ordering up to translation. Both halves are unfinished calculations; notation A versus B and membership in G versus tilde G must remain literal. The recurring reversed-set accent on A,B is tentatively check, not an unquestioned tilde. No proof is given for the algebraic conditions on this sheet.''')

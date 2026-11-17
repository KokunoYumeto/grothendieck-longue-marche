from record_page import record
record(22,r'''\scanpage{22}
\margin{Si $(K)$ et si les couples $\in S\times S$ sont \unsure{privilégiés|priorisés} $\updownarrow$ id}

d) $\forall A,B\in\mathcal P_f(G)\cap S$, $A'\sim A$, $B'\sim B$, \unsure{$\ldots$}
\[
A'\ast B'\prec A\ast B\qquad\text{i.e.}\quad\uline{(A,B)\text{ bon}}
\]
e) $\forall A,B,C\in\mathcal P_f(G)\cap S$, $A'\sim A$, $B'\sim B$, $C'\sim C$, \unsure{$\ldots$}
\[
\|A'\ast B'\ast C'\|_\infty\leq\|A\ast B\ast C\|_\infty
\]

\deleted{Supposons}

Quitte à \unsure{saturer} $S$, \unsure{on s.} $S$ stable par translation
\[
S_0=S\cap\mathcal P_f(G)\qquad\unsure{\text{NB}}\quad S_0\ne\varnothing
\]
Soit $f\in S$. Alors

a) $\exists t\in G\quad f=\varepsilon_t\ast\unsure{f|\check f}$
\margin{[$(f,f)$ \deleted{bon}\inserted{\uline{pri}}]}

b) les $E_\alpha(f)\in S_0$
\margin{[$(f,A)$ \deleted{bon}\inserted{\uline{pri}} pour $A\in S_0$]}

\deleted{\unsure{Donc} Soit $f\in\mathbb R[G]^+$}

Soit \deleted{$f$} $\tilde S=\{f\in\mathbb R(G)^+\mid\text{satisfait a), b)}\}$

\deleted{$\unsure{f\in S}$} i.e.
\[
\left\{\begin{array}{l}
f=\displaystyle\sum_I\alpha_i A_i\qquad\alpha_i>0\qquad A_i\in S_0\quad(A_i)\text{ tot ord.}\\
\deleted{\unsure{f}}\ \exists s\in G,\quad A_i=\deleted{\unsure{\check A_i}}\varepsilon_s\ast\check A_i\quad\forall i
\end{array}\right.
\]
Soit de même
\[
\left|\begin{array}{l}
g=\displaystyle\sum_J\beta_j B_j\qquad\beta_j>0,\quad B_j\in S_0\quad(B_j)\text{ tot ord.}\\
t\in G,\qquad B_j=\varepsilon_t\ast\check B_j
\end{array}\right.
\]
On a
\[
f\ast g=\sum_{(i,j)\in I\times J}\alpha_i\beta_j A_i\ast B_j
\]

\deleted{Supposons que $\exists(C_{\unsure{n|\alpha}})$}

On a $A_i\ast B_j\in S$, donc
\[
E_\ast(A_i\ast B_j)\subset S_0
\]
\uuline{Supposons}
\[
\bigcup E_\ast(A_i\ast B_j)\quad\uline{\text{tot}}\text{ ordonné}
\]
\unsure{on veut}
\[
\bigcap_{C\in\bigcup_{ij}E_\ast(A_i\ast B_j)}C\ne\varnothing
\]
\diagram{\begin{tikzcd}
0\arrow[r]&{}_2G\arrow[r]&G\arrow[r,"2"]&G
\end{tikzcd}}
% archive foliation: 21
''',[
('margin note','upper left','Si (K) et si les couples ∈S×S sont ... ↕ id'),
('text','top','d) ∀A,B∈P_f(G)∩S, A′∼A,B′∼B'),
('display','top','A′*B′≺A*B i.e. (A,B) bon'),
('text','upper','e) ∀A,B,C∈P_f(G)∩S ...'),
('display','upper','||A′*B′*C′||∞≤||A*B*C||∞'),
('deletion','below dividing line','Supposons'),
('text','middle upper','Quitte à saturer S ... S stable par translation'),
('display','middle upper','S_0=S∩P_f(G); S_0≠∅'),
('text','middle','Soit f∈S. Alors'),
('display','middle','a) ∃t∈G f=ε_t*f'),
('margin note','right of a','[(f,f) bon / pri]'),
('deletion','right of a','bon'),
('insertion','right of a','pri'),
('text','middle','b) les E_α(f)∈S_0'),
('margin note','right of b','[(f,A) bon / pri pour A∈S_0]'),
('deletion','right of b','bon'),
('insertion','right of b','pri'),
('deletion','middle','Donc Soit f∈R[G]^+'),
('text','middle','Soit S̃={f∈R(G)^+ | satisfait a),b)}'),
('deletion','before S̃ and i.e.','f; f∈S'),
('display','middle lower','f=Σα_i A_i; ∃s A_i=ε_s*check A_i'),
('deletion','within second line of f display','f; check A_i'),
('text','middle lower','Soit de même'),
('display','middle lower','g=Σβ_j B_j; t∈G B_j=ε_t*check B_j'),
('text','lower','On a'),
('display','lower','f*g=Σ_(i,j) α_iβ_j A_i*B_j'),
('deletion','lower','Supposons que ∃(C_n)'),
('text','lower','On a A_i*B_j∈S donc'),
('display','lower','E_*(A_i*B_j)⊂S_0'),
('text','bottom','Supposons; on veut'),
('display','bottom','∪E_*(A_i*B_j) tot ordonné; intersection C≠∅'),
('diagram','bottom left','0→₂G→G→²G')
],'''Continuation of Condition K: indicator-pair majorization and indicator triple convolution norm tests. The new sketch enlarges S via symmetry and level-set closure, decomposes f,g into positive combinations of nested indicator sets, and reaches a desired/common-level-set intersection condition. The phrase “Supposons” precedes joint ordering of all convolution level sets, rather than a proof of it. Marginal corrections replace “bon” with the literal abbreviation “pri”. The final sequence uses the multiplication-by-2 map on G, with no terminal zero. This is a distinct group-extension lead, not a completed deduction.''')

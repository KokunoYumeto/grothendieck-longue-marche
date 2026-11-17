from record_page import record
record(13,r'''\scanpage{13}
\deleted{Construction}

5. \uline{Essai de construction récurrente de} $G(j)$

\margin{\uline{NB} $G_{-1}(j)=\varnothing$}
$G_0(j)$ donné
\[
G_1(j)=\deleted{\{x\in C}G_0(j)\cup
\left\{x\in C\ \middle|\ 
\begin{array}{l}
(x\in C(j)\text{ et }\deleted{\unsure{\exists y}}R(x)\cap G_0(j)\ne\varnothing)\ \unsure{\text{ou}}\\
x\in(\bar C(j)\setminus\bar C_0(j))\text{ et }R(x)\subset G_0(j)
\end{array}\right\}
\]
\[
\cdots
\]
\[
G_{\unsure{i|2}}(j)=G_0(j)\cup
\left\{x\in C\ \middle|\ 
\begin{array}{l}
x\in C(j)\text{ et }R(x)\cap G_{i-1}(j)\ne\varnothing\\
x\in(\bar C(j)\setminus\bar C_0(j))\text{ et }R(x)\subset G_{i-1}(j)
\end{array}\right\}
\]
On voit par récurrence que :
\[
G_i(j)\subset G_{i+1}(j)
\]
et aussi
\[
G_i(j)\subset G(j)
\]
(en utilisant la prop.)

Posons
\[
G_\infty(j)=\bigcup G_i(j)\qquad\text{donc}\qquad G_\infty(j)\subset G(j)
\]

? \uline{Th 3} $G_\infty(j)=G(j)$.

\margin{Si $C$ \uline{fini} \unsure{et n'existe de} partie infinie. Plus généralement si $C=\bigcup C_i$. cf § 2.}

\deleted{Il reste à prouver $x\in G(j)\Rightarrow\exists i,\ x\in G_i(j)$.
Soit $\Sigma$ une $j$-stratégie gagnante pour $x$. Donc
$\exists$ partie \inserted{finie} (maximale) \unsure{débutant} par $x$, comp. avec $\Sigma$
\[
X:(x_0=x,x_1,\ldots,x_N)
\]
et $x_N\in G_0(j)$. Je dis que

\unsure{On le}}

On prouve par récurrence sur $i\geq0$
\[
G_\infty(j)\cap C_i=G(j)\cap C_i
\]
en utilisant le Th. 1.
% archive foliation: 12
''',[
('deletion','top','Construction'),
('text','heading','5. Essai de construction récurrente de G(j)'),
('margin note','upper left','NB G_{-1}(j)=∅'),
('text','upper','G_0(j) donné'),
('display','upper','G_1(j)=G_0(j)∪...'),
('deletion','first display','{x∈C; ∃y'),
('display','upper middle','...; G_i(j)=G_0(j)∪...'),
('text','middle','On voit par récurrence que'),
('display','middle','G_i(j)⊂G_{i+1}(j)'),
('text','middle','et aussi'),
('display','middle','G_i(j)⊂G(j)'),
('text','middle','(en utilisant la prop.) Posons'),
('display','middle','G_∞(j)=∪G_i(j), donc G_∞(j)⊂G(j)'),
('text','lower middle','? Th 3 G_∞(j)=G(j)'),
('margin note','left lower middle','Si C fini ... Plus généralement si C=∪C_i. cf §2'),
('deletion','lower','Il reste à prouver ... Je dis que ... On le'),
('insertion','within cancelled argument','finie'),
('display','within cancelled argument','X:(x_0=x,x_1,...,x_N)'),
('text','bottom','On prouve par récurrence sur i≥0'),
('display','bottom','G_∞(j)∩C_i=G(j)∩C_i'),
('text','bottom','en utilisant le Th. 1.')
],'''Theorem 3 explicitly carries a question mark; the left margin adds finiteness/no infinite play and then C=union C_i (cf §2). The deleted attempt uses one finite maximal compatible play to argue finite-stage membership; the live replacement uses induction on the C_i. The recurrence visibly uses barred C_0(j), and omits a written connector between the two conditions in its general line; do not regularize either. The iteration subscript has an overwritten appearance (i/2).''')

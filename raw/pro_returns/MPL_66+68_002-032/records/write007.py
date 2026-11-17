from record_page import record
record(7,r'''
\scanpage{7}
% archive foliation: 6
% Two long diagonal strokes cancel the entire draft below.
\deleted{
Prouvons $\Longleftarrow$, i.e. supposons que $\forall y\in R(x)$, on a $y\in G(j)$, prouvons $x\in G(j)$, i.e. montrons qu'il existe une $j$-stratégie $\Sigma$ $x$-gagnante (sachant que \inserted{$R(x)\ne\varnothing$ et que} $\forall y\in R(x)$, $\exists\Sigma_y$ \deleted{strat.} $j$-stratégie $y$-gagnante, et que $x\in\overline C(j)$).

Considérons un bon ordre sur $R(x)$, et posons \inserted{pour $z\in C(j)$}
\[
\Sigma(z)=\begin{cases}
R(z)\text{ si }\deleted{\unsure{z\ \text{n'est pas conséquent}}}\ z\unsure{\not\succ|\not>}x\quad(z\text{ n'est pas }\unsure{\text{conséquent de}}\ x)\\
\Sigma_{y(z)}(z)\text{ si }\deleted{\unsure{y(z)}}\ z\unsure{\succ|\geq}x,\ \text{donc si }\deleted{z\unsure{\succ|\geq}y}\ \exists y(z)\in R(x),\ \text{avec }z\unsure{\succ|\geq}y(z).
\end{cases}
\]
On prendra $y(z)$ le \uuline{plus petit}.

On vérifie immédiatement que a) $\Sigma$ est une \uline{stratégie} i.e. $R(z)\ne\varnothing\Longrightarrow\Sigma(z)\ne\varnothing$ (car les $\Sigma_y$ sont des stratégies), et \inserted{prouvons} qu'elle est $x$-gagnante.

\deleted{Pour ceci, voyons d'abord que si $z\in G(j)\cap C(j)$, \inserted{et si $z$ est un successeur de $x$,} alors $\Sigma(z)\unsure{\in|\subset}G(j)$}
\deleted{\unsure{donc} $\Sigma$}
Soit $(x_0=x,x_1=\unsure{y},x_2,\ldots,x_n,\ldots)$ une partie partant de $x$, comp. avec $\Sigma$. Alors les $x_i$ $(i\geq1)$ sont $\unsure{\succ|\geq}x$, donc $\forall i\geq1$, $\exists y_i\in R(x)$ \deleted{\unsure{avec qui}\ \unsure{y_i}\ \unsure{\text{est le}}} avec $x_i\unsure{\succ|\geq}y_i$; soit $y_i$ le plus petit de ceux-ci.
Comme $x_{i+1}\unsure{\succ|\geq}x_i\unsure{\succ|\geq}y_i$ donc $x_{i+1}\unsure{\succ|\geq}y_i$, on a $y_{i+1}\leq y_i$, donc les $y_i$ vont en décroissant donc sont stationnaires. Soit $y$ la valeur commune.

Donc pour $n$ assez grand, on a.
}
''',[
('deletion','whole sheet','Entire draft crossed by two long diagonal lines'),('text','top','Prouvons left implication i.e. supposons que'),('display','top inline','forall y in R(x); y in G(j); exists Sigma_y'),('insertion','top parenthesis','R(x) nonempty et que'),('deletion','top parenthesis','strat.'),('text','upper','Considérons un bon ordre sur R(x)'),('insertion','above cases','pour z in C(j)'),('display','upper-middle','Sigma(z)=R(z) or Sigma_y(z)(z)'),('deletion','cases','z n’est pas conséquent; y(z); z succeeds y'),('text','under cases','On prendra y(z) le plus petit'),('text','middle','On vérifie immédiatement que a) Sigma est une stratégie'),('display','middle inline','R(z) nonempty implies Sigma(z) nonempty'),('insertion','middle','prouvons'),('deletion','middle-lower','Pour ceci voyons d’abord que si z in G(j) cap C(j) ...'),('insertion','inside deleted paragraph','et si z est un successeur de x'),('deletion','middle-lower','donc Sigma'),('text','lower','Soit (x_0=x,x_1=y,...) une partie ...'),('display','lower inline','x_i succeeds x; exists y_i; x_i succeeds y_i'),('deletion','lower','avec qui y_i est le'),('text','lower','Comme x_(i+1) succeeds x_i ... sont stationnaires'),('display','lower inline','y_(i+1)<=y_i'),('text','bottom','Donc pour n assez grand, on a.')
],'''Entire sheet is cancelled. It attempts a different universal-successor gluing proof using a well-order on R(x), a least predecessor index y(z), and eventual stabilization of a decreasing sequence y_i. The relation sign and some conditions in the cases are doubtful; do not silently read them as the relation a repaired proof would need. Last sentence ends unfinished. This is an abandoned proof attempt, not an established argument.''',sheet_kind='cancelled_draft')

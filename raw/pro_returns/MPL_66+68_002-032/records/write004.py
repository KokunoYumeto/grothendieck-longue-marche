from record_page import record
record(4,r'''
\scanpage{4}
% archive foliation: 3
\deleted{\uline{Prop}}\inserted{\uline{Th\unsure{m} 1}}
\[
(C(j)\setminus C_0)\cap G(j)=\{x\in C(j)\inserted{\setminus C_0}\mid\deleted{\unsure{x\in G_0(j)}\ \unsure{\text{ou}}}\ \exists y\in R(x),\ \unsure{\text{avec}}\ y\in G(j)\}
\]
\inserted{$R(x)\cap G(j)\ne\varnothing$}
\[
(\overline C(j)\setminus C_0)\cap G(j)=\{x\in\overline C(j)\mid\forall y\in R(x)\ \text{on a }y\in G(j)\ \deleted{\text{et }\unsure{\text{si}}\ R(x)=\varnothing\ (\text{i.e. }x\in C_0)\ \unsure{\text{alors}}\ x\in G_0(j)}\}
\]
\inserted{$R(x)\subset G(j)$}
\margin{Si \unsure{$\nexists$} \unsure{de} partie infinie}

\uline{Dém} \deleted{a) Soit $x\in C(j)$}\inserted{$1^\circ)$} Soit $x\in C(j)$, il faut prouver que
\[
x\in G(j)\Longleftrightarrow\deleted{\unsure{x\in G_0(j)\ \text{ou}}}\ \exists y\in R(x),\ y\in G(j).
\]
\deleted{\unsure{x est terminal}}

\deleted{Si $x\in C_0$, c'est clair (cf NB plus haut)}
Soit $x\in C\setminus C_0$ \inserted{i.e. $R(x)\ne0$. Prouvons $\Longrightarrow$ i.e. supposons $x\in G(j)$, prouvons $\exists y$ \unsure{ch}\ldots}, soit $\Sigma$ stratégie \deleted{pour $j$} $x$-gagnante. Considérons $\Sigma(x)$; \unsure{donc} \deleted{nécessairement} $\Sigma(x)\ne\varnothing$, donc $\exists y\in\Sigma(x)$. Je dis que $y\in G(j)$, i.e.

\uline{Lemme} Si $x\in C(j)\cap G(j)$, $\Sigma$ une $j$-stratégie $x$-gagnante, alors $\forall y\in\Sigma(x)$, \inserted{on a} $y\in G(j)$, \inserted{i.e. $\Sigma(x)\subset G(j)$.} Plus précisément $\Sigma$ est aussi $y$-gagnante.

\deleted{En effet, \unsure{parties pour} $\Sigma$}
Trivial sur définitions.

Inversement, supposons $\exists y\in R(x)$ avec $y\in G(j)$, prouvons que $x\in G(j)$. Soit $\Sigma$ une $j$-stratégie $y$-gagnante. On va \inserted{en gardant} définir une $j$-stratégie \inserted{$\Sigma'$} $x$-gagnante ainsi : Pour $z\in C(j)$, on pose
\[
\Sigma'(z)=\begin{cases}\Sigma(z)\text{ si }z\ne x\\ \{y\}\deleted{\unsure{\text{ou}}}\text{ si }z=x\end{cases}
\]
C'est une $j$-stratégie, car \deleted{si $R(z)\ne\varnothing$ \unsure{-} $R(x)\ne\varnothing$, alors} $\Sigma(z)\ne0$ \deleted{\unsure{pour}} \deleted{(et dans le cas $z\ne x$ pas de pb, mais alors $\Sigma'(z)=\Sigma(z)\ne\varnothing$ par hyp. que $\Sigma$ est stratégie.}

Prouvons que $\Sigma'$ est $x$-gagnante : Soit une partie $(x_0=x,x_1,\ldots,x_n\ldots)$ partant de $x$ et compatible avec $\Sigma'$. On a donc $x_1=y$; \deleted{et}\inserted{prouvons que} la partie $(x_1,x_2,\ldots,x_n\ldots)$ \inserted{$x_1=y$} est compatible avec $\Sigma$, i.e. que
\[
\deleted{\unsure{\forall}}\quad i\geq1,\quad x_i\in C(j)\Longrightarrow x_{i+1}\in\Sigma(x_i).
\]
''',[
('deletion','top-left','Prop'),('insertion','top-left','Thm 1'),('display','top first formula','(C(j)\\C_0) cap G(j) = {... exists y ...}'),('insertion','top first formula','\\C_0; R(x) cap G(j) nonempty'),('deletion','top first formula','x in G_0(j) ou'),('display','top second formula','(Cbar(j)\\C_0) cap G(j) = {... forall y ...}'),('deletion','top second formula','et si R(x)=empty ... x in G_0(j)'),('insertion','under second formula','R(x) subset G(j)'),('margin note','upper-left diagonal','Si no de partie infinie'),
('text','upper proof','Dém Soit x in C(j), il faut prouver que'),('deletion','upper proof opening','a) Soit x in C(j)'),('insertion','upper proof opening','1 degrees'),('display','upper proof','x in G(j) iff exists y in R(x), y in G(j)'),('deletion','proof display and underbrace','x in G_0(j) ou; x est terminal'),('deletion','upper-middle','Si x in C_0 c’est clair (cf NB plus haut)'),('text','middle','Soit x in C\\C_0, soit Sigma stratégie ...'),('insertion','above middle paragraph','i.e. R(x) nonzero; Prouvons implication ...'),('deletion','middle','pour j; nécessairement'),('text','middle','Je dis que y in G(j), i.e.'),('text','middle lemma','Lemme Si x in C(j) cap G(j) ... Plus précisément'),('insertion','lemma','on a; i.e. Sigma(x) subset G(j)'),('deletion','under lemma','En effet, parties pour Sigma'),('text','under lemma','Trivial sur définitions'),('text','lower','Inversement supposons exists y ...'),('insertion','lower','en gardant; Sigma prime'),('display','lower','Sigma prime(z)=cases'),('deletion','cases second line','ou'),('text','lower','C’est une j-stratégie, car; Sigma(z) nonzero'),('deletion','lower three struck lines','si R(z)...; et dans le cas z ne x pas de pb ...'),('text','bottom','Prouvons que Sigma prime est x-gagnante'),('deletion','bottom','et; forall'),('insertion','bottom','prouvons que; x_1=y'),('display','bottom','i>=1; x_i in C(j) implies x_(i+1) in Sigma(x_i)')
],'''Theorem 1 gives local existential/universal characterizations of winning positions; terminal-position corrections and heavy deletions occur in its statement. The proof changes a strategy only at x to choose a winning successor y. At this stage the argument must deal with a later return to x; the proof continues on scan 005. “Trivial sur définitions” is the stated justification for the lemma on successor positions. Upper-left marginal hypothesis is uncertain; do not draw a mathematical conclusion from it until checked.''')

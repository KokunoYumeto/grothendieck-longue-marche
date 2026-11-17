from record_page import record
record(2,r'''
\cotefile{68}
\scanpage{2}
% archive foliation: 1
\textcircled{1.} Jeu (de position)

\textcircled{a} $\left\{\begin{array}{l} C\text{ ensemble des positions }(\unsure{:=}\text{ configurations})\\ R\subset C\times C\quad\text{relation}\end{array}\right.$
$((x,y)\in R$ se lit $y\in R(x)$ ou $y$ \uline{successeur} de $x)$.

\inserted{\uline{Déf} Position $x$ terminale $\Longleftrightarrow R(x)=\varnothing$
\[
C_0=\{x\in C\mid R(x)=\varnothing\}=\text{ens des positions terminales}
\]}
% The blue bracket and long return arrow attach this definition after (a).

\textcircled{b} $\left\{\begin{array}{l}J\text{ ensemble des joueurs}\\ i:\inserted{C\setminus}C_{\inserted{0}}\longrightarrow J\end{array}\right.$
$i(x)\longrightarrow$ le joueur qui a l'initiative dans la position $x$
\[
\inserted{C\setminus}C_{\inserted{0}}=\coprod_{j\in J}C(j)
\]
\margin{\uline{NB} \deleted{$i$ \uline{n'intervient que} \uline{pour $x$ situé sur} $C\setminus C_0$} \deleted{\unsure{J}}}

\textcircled{c} $J\longrightarrow\mathcal P(C_0)\qquad j\longmapsto G_0(j)\subset C_0$
\begin{center}positions terminales \uline{gagnantes} \uline{pour $j$}\end{center}
\margin{\uline{NB} On ne \unsure{suppose pas} $G_0(j)\subset C_0(j)$}

\textcircled{2.} \uline{Parties}.
\deleted{\unsure{2a}} (Ne dépend que de $(C,R)$\ldots)

\uline{Partie} \inserted{(à $n$ coups, $n\in\mathbb N$)}
\[
(x_0,x_1,\ldots,x_n)\in C^{n+1}\qquad \forall\,0\leq i\leq n-1,\quad x_{i+1}\in R(x_i)
\]
\uline{Prolongement} de parties

\uline{Partie terminée} ($\Leftrightarrow$ partie maximale) : telles que $x_n\in C_0$

Partie infinie, partie circulaire. $(x_0,x_1\ldots,x_n)\quad x_n=x_0\quad(n\geq1)$

\uline{Prop} S'il existe une partie circulaire, existe une partie infinie. L'inverse est vrai si $C$ est fini.

\uline{Construction} récurrente
\inserted{\[
C_{-1}=\varnothing\qquad C_0=\{x\in C\mid\forall y\in R(x),\ y\in C_{-1}\}=\{x\in C\mid R(x)=\varnothing\}
\]}
\[
C_1=\{x\in C\mid\forall y\in R(x),\ y\in C_0\}\qquad\text{NB }C_1\supset C_0
\]
\[
\unsure{--}
\]
\[
C_i=\{x\in C\mid\forall y\in R(x),\ y\in C_{i-1}\}
\]
\uline{Prop} $(C_i)$ \unsure{suite} croiss. d'ensembles.
\[
C_i=\{x\in C\mid\text{tte partie }\deleted{\unsure{commençant}}\inserted{\text{issue de}}\ x\text{ est de longueur }\leq i\}
\]
\uline{Cor} Soit $C_\infty=\bigcup C_i$. Alors
\[
C_\infty=\{x\in C\mid\text{l'ens des }\inserted{\uline{longueurs des}}\text{ parties partant de }x\text{ est borné}\}
\]
''',[
('text','top','1. Jeu (de position)'),('text','upper; a','C ensemble des positions'),('display','upper; a','R subset C x C; (x,y) in R'),
('insertion','middle-left returned by blue arrow to a','Déf Position x terminale'),('display','inserted definition','C_0 = {x in C | R(x)=empty}'),
('text','upper-middle; b','J ensemble des joueurs'),('display','upper-middle','i:C\\C_0 -> J; i(x)'),('insertion','domain of i and coproduct','C\\ and subscript 0 in blue'),('display','middle','C\\C_0 = coproduct C(j)'),
('margin note','middle-left','NB i n’intervient que'),('deletion','middle-left','i n’intervient que pour x situé sur C\\C_0; J'),
('display','middle; c','J -> P(C_0); j maps to G_0(j)'),('text','under G_0(j)','positions terminales gagnantes pour j'),('margin note','right of c','NB On ne suppose pas G_0(j) subset C_0(j)'),
('text','middle-lower','2. Parties (Ne dépend que de (C,R)...)'),('deletion','left under 2','2a'),('insertion','above tuple','à n coups, n in N'),('text','lower; definition','Partie; Prolongement de parties'),('display','lower','(x_0,...,x_n) in C^(n+1); forall 0<=i<=n-1'),
('text','lower','Partie terminée (partie maximale)'),('text','lower','Partie infinie, partie circulaire'),('display','lower-right','(x_0,...,x_n); x_n=x_0 (n>=1)'),('text','lower','Prop S’il existe une partie circulaire'),
('text','lower-left','Construction récurrente'),('insertion','above C_1 formula','C_-1=empty; C_0='),('display','lower','C_1={...}; NB C_1 superset C_0'),('display','lower','-- ; C_i={...}'),('text','bottom','Prop (C_i) suite croiss. d’ensembles'),('display','bottom','C_i={x | tte partie ... longueur <= i}'),('deletion','bottom display','commençant'),('insertion','bottom display','issue de'),('text','bottom','Cor Soit C_infty=union C_i. Alors'),('display','bottom','C_infty={x | l’ens des parties ... borné}'),('insertion','bottom-right','longueurs des')
],'''The finite-position converse from infinite play to a circular play is stated as a proposition without proof. The C_i recursion and bounded-length characterization are stated without proof. The blue correction removes terminal positions from the domain of i; the marginal G_0(j) versus C_0(j) inclusion needs later review and remains uncertain. No handwritten manuscript page number confidently identified; lower-left 1 treated as archive foliation. The circled 1 and 2 are section numbers.''')

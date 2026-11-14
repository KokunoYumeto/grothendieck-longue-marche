from record_page import save_page
save_page(120,5,r'''
\mspage{2}
\[
\mathcal M'_n=\mathcal M_n\cup\{\varnothing\}
\]
les $\mathcal M'_n$ satisfont encore les axiomes \ldots

\deleted{\textcircled{4} \unsure{On a} \unsure{NB} \unsure{Si on pose}}

De $\overline{\mathrm m}$, \deleted{$\unsure{M}$} $M1$ implique que si on a, pour \uline{un} $n$, \deleted{$\unsure{M}$} $\mathcal M_n=\{\varnothing\}$, alors c'est vrai aussi pour $\forall n$ -- cas trivial \inserted{(qui satisfait aux axiomes)} que je vais exclure. Donc je suppose aussi
\[
(***)\quad\deleted{\unsure{\exists}}\ \mathcal M_1\ne\{\varnothing\}\quad\text{i.e.}\quad\exists A\in\mathcal M_1,\quad A\ne\varnothing.
\]
Ceci étant, si on pose pour $I\unsure{\ne|=}\varnothing$
\[
\mathcal M_\varnothing=\mathcal P(\underbrace{R^\varnothing}_{\text{espace ponctuel }\{e\}})=\{\varnothing,\{e\}\}
\]
\margin{les propriétés $M'1$ à $M'4$ (cf \textcircled{1}) restent satisfaites sans se borner à \deleted{\unsure{$I,J$}} $I,J\ne\varnothing$}

\textcircled{4} Soit \deleted{$\unsure{x\in R_n}$}
\[
x=(x_1,\ldots,x_n)\in R^n
\]
alors il résulte de $M1$ et $M4$ que
\[
\{x\}\in R^n\Longleftrightarrow\forall i\in[1,n],\text{ on a }\{x_i\}\in\mathcal M_1.
\]
Soit
\[
R_0=\{x\in R\mid\{x\}\in\mathcal M_1\}\qquad\text{donc }R_0\subset R,
\]
alors pour $\forall$ ens fini $I$, on a
\[
R_0^I=\{x\in R^I\mid\{x\}\in\mathcal M_I\}
\]
\inserted{$\widehat R^I$}
Notons que si \deleted{$R_0\ne\varnothing$} \inserted{$\mathrm{Card}\ R_0\ge2$}, alors on conclut de la stabilité \inserted{de $\mathcal M_1$} par intersection que $\varnothing\in\mathcal M_1$, donc on satisfait à \textcircled{3}.

\textcircled{5} Exemples (à part $\mathcal M_n=\varnothing\quad\forall n$, et $\mathcal M_n=\{\varnothing\}\quad\forall n$)
\mspage{4}
''',[
('text','top right page number','2'),('display','top','M prime_n = M_n union {emptyset}'),('text','top continuation','les M prime_n satisfont encore les axiomes ...'),('deletion','upper cancelled line','4; On a; NB; Si on pose'),('text','upper paragraph','De m-bar M1 implique que si on a'),('deletion','upper before M1','M'),('deletion','upper before M_n={emptyset}','M'),('insertion','upper right above que je vais','(qui satisfait aux axiomes)'),('display','upper-middle','(***) M_1 not {emptyset}; exists A nonempty'),('deletion','(***) display before M_1','exists'),('text','middle','Ceci étant, si on pose pour I neq emptyset'),('display','middle','M_emptyset=P(R^emptyset)={emptyset,{e}}'),('insertion','under R^emptyset','espace ponctuel {e}'),('margin note','right middle linked by bracket','les propriétés M prime 1 à M prime 4 restent satisfaites'),('deletion','right middle note','I,J'),('text','middle comment 4','Soit'),('deletion','comment 4 after Soit','x in R_n'),('display','middle','x=(x_1,...,x_n) in R^n'),('text','middle-lower','alors il résulte de M1 et M4'),('display','middle-lower','{x} in R^n iff all {x_i} in M_1'),('text','lower','Soit'),('display','lower','R_0={x in R such that {x} in M_1}; R_0 subset R'),('text','lower','alors pour forall ens fini I'),('display','lower','R_0^I={x in R^I such that {x} in M_I}'),('insertion','below left of last display','R hat^I'),('text','lower','Notons que si ... alors on conclut'),('deletion','Notons que si','R_0 neq emptyset'),('insertion','above deleted condition','Card R_0 >= 2'),('insertion','after stabilité','de M_1'),('text','bottom comment 5','Exemples (à part M_n=emptyset and M_n={emptyset})'),('text','bottom left page number','4')
],observations='The text adjoins the empty set, excludes M_n={emptyset}, extends the notation to an empty index set, and defines the admissible-point set R_0. The singleton equivalence visibly writes {x} in R^n on its left; it is retained without mathematical emendation. The condition R_0 nonempty is crossed out and replaced with Card R_0 >= 2 before the empty-set intersection conclusion. The heavily cancelled line above De m-bar is uncertain; the condition on I before M_emptyset appears neq, although the surrounding formula is indexed by emptyset.')

from record_page import save_page
save_page(120,3,r'''
\mspage{1}
\margin{\textcircled{I}\par\uline{Modèles modérés} \deleted{\unsure{et espaces}}\inserted{ens} \deleted{modérés}}
\[
\forall n\in\mathbb N^*,\qquad\mathcal M_n\subset\mathcal P(R^n)
\]
\textcircled{\scriptsize$M1$} $\forall u:[1,n]\longrightarrow[1,m]$, d'où $u^*:R^m\longrightarrow R^n$, on a
\[
u^*(\mathcal M_m)\subset\mathcal M_n\qquad\text{i.e.}\quad\forall A\in\mathcal M_m,\text{ on a }u^*(A)\in\mathcal M_n.
\]
\textcircled{\scriptsize$M2$} $\forall u:[1,n]\longrightarrow[1,m]$ \uline{surjectif}, d'où $u^*:R^m\hookrightarrow R^n$ injectif, on a
\[
u^{*-1}(\mathcal M_n)\subset\mathcal M_m\qquad\text{i.e.}\quad\forall \unsure{B|A}\in\mathcal M_n,\text{ on a }u^{*-1}(\unsure{B|A})\in\mathcal M_m.
\]
\margin{donc si on a $M1$, \unsure{on trouve}\par $A\in\mathcal M_m\Longleftrightarrow\unsure{u_*|u^*}(A)\in\mathcal M_n$}
\textcircled{\scriptsize$M3$} $\forall u:[1,n]\longrightarrow[1,m]$ d'où $u^*:R^m\longrightarrow R^n$, et pour $A\in\mathcal M_m$, $B\in\mathcal M_n$, on a
\[
u^{*-1}(B)\cap A\in\mathcal M_m
\]
\textcircled{\scriptsize$M4$} $\forall A\in\mathcal M_m$, $B\in\mathcal M_n$, on a (modulo $R^m\times R^n\simeq R^{m+n}$)
\[
A\times B\in\mathcal M_{m+n}.
\]

\uline{Commentaires} \textcircled{1} $M1)$ permet de définir, pour \deleted{tout} $I$ ens fini non vide, $\mathcal M_I\in\mathcal P(R^I)$, et alors on a des propriétés $M'1$ à $M'4$ pour les $\mathcal M_I$ et les $u:I\unsure{\longrightarrow|-}J$.

\textcircled{2} : Pour avoir $M1$, il suffit de le supposer pour les \deleted{trois} cas :

a) $m=n$, $u\in\unsure{\mathfrak S_n}$

b) $m=n+1$, $u$ injectif (``op. face''), donc $u^*$ surjectif

c) $n=m+1$, $u$ surjectif \deleted{\unsure{(``op. dégénérescence'')}} \inserted{(``op dégénérescence'')} donc $u^*$ injectif

\deleted{\unsure{et en} seulement les \unsure{projections} \unsure{dans}}

\margin{ou $\overline{\mathrm m}$ seulement les op. standard\par
$R^n\longrightarrow R^{n+1},\ (x_1,\ldots,x_n)\longmapsto(x_1,\ldots,x_n,x_n)$\par
et\par
$R^{n+1}\unsure{\longrightarrow|-}R^n,\ (x_1,\ldots,x_{n+1})\longmapsto(x_1,\ldots,x_n)$}

Pour avoir $M2$, il suffit de le supposer pour les op${}^{\mathrm{os}}$ de dégénérescences, \inserted{et \unsure{$\overline{\mathrm m}$|m} seulement pour l'application \deleted{\unsure{$R^n\hookrightarrow R^{n+1}$}} \figure{\begin{tikzpicture}[x=.12cm,y=.12cm,baseline=-.5ex]\draw[line width=1.2pt] (0,0)--(.7,3) (.45,1.1)--(1.6,.2)--(.3,.6)--(1.1,1.6);\end{tikzpicture}}}
\margin{\figure{\begin{tikzpicture}[x=.12cm,y=.12cm]\draw[line width=1.2pt] (0,0)--(.7,3) (.45,1.1)--(1.6,.2)--(.3,.6)--(1.1,1.6);\end{tikzpicture}}\par
\fbox{$\begin{gathered}R^n\hookrightarrow R^{n+1}\\(x_1,\ldots,x_n)\deleted{\unsure{x_n}}\\\longmapsto(x_1,\ldots,x_n,x_n)\end{gathered}$}}
Notons que $M1$, $M2$, $M4$ impliquent que les $\unsure{\mathfrak S_n|\mathcal M_n}$ sont stables par intersection de deux
\[
A,B\in\unsure{\mathfrak S_n|\mathcal M_n}\Longrightarrow A\cap B\in\unsure{\mathfrak S_n|\mathcal M_n}
\]
\inserted{(uniquement $M1$, $M2$, $M4$)}
d'où résulte que pour avoir $M3$, il suffit de le prouver pour $u$ \unsure{surjectif|injectif}, et $\overline{\mathrm m}$ seulement pour $u^*$ l'op. standard
\[
R^{n+1}\longrightarrow R^n,\quad(x_1,\ldots,x_{n+1})\longmapsto(x_1,\ldots,x_n).
\]
\mspage{2}
''',[
('text','top right page number','1'),('margin note','upper left oblique heading','I; Modèles modérés'),('deletion','upper left heading','et espaces; modérés'),('insertion','upper left heading','ens'),('display','top','forall n in N*, M_n subset P(R^n)'),('text','upper axiom M1','forall u:[1,n] to [1,m], u*:R^m to R^n'),('display','upper M1','u*(M_m) subset M_n; forall A'),('text','upper axiom M2','u surjectif; u* injectif'),('display','upper M2','u^{*-1}(M_n) subset M_m; forall B'),('margin note','left beside M2','donc si on a M1; A in M_m iff u_*(A) in M_n'),('text','middle axiom M3','forall u; A in M_m, B in M_n'),('display','middle M3','u^{*-1}(B) intersection A in M_m'),('text','middle axiom M4','forall A,B; modulo R^m times R^n simeq R^{m+n}'),('display','middle M4','A times B in M_{m+n}'),('text','below axioms comment 1','Commentaires; M1 permet de définir'),('deletion','comment 1','tout'),('text','lower comment 2','Pour avoir M1, il suffit'),('deletion','comment 2','trois'),('text','comment 2 item a','m=n; u in S_n'),('text','comment 2 item b','m=n+1; u injectif; op. face'),('text','comment 2 item c','n=m+1; u surjectif; op dégénérescence'),('deletion','comment 2 item c','op. dégénérescence'),('insertion','above item c deletion','op dégénérescence'),('deletion','below item c','et en seulement les projections dans'),('margin note','left oblique beside items b,c','ou m-bar seulement les op. standard'),('display','within left note first','R^n to R^{n+1}; duplicate last coordinate'),('display','within left note second','R^{n+1} to R^n; drop last coordinate'),('text','lower paragraph','Pour avoir M2'),('insertion','above lower paragraph continuation','et m-bar seulement pour l’application'),('deletion','end of inserted note','R^n to R^{n+1}'),('drawing','end of insertion and beside left box','matching handwritten reference marks'),('margin note','lower left box','R^n hook to R^{n+1}; coordinate duplication'),('deletion','within lower left box','x_n'),('text','lower','Notons que M1,M2,M4 impliquent'),('display','bottom-middle','A,B in S_n implies A intersection B in S_n'),('insertion','below intersection display','uniquement M1,M2,M4'),('text','bottom paragraph','d’où résulte que pour avoir M3'),('display','bottom','R^{n+1} to R^n; projection coordinates'),('text','bottom left page number','2')
],observations='First axiom sheet, top folio 1 and bottom 2. M1–M4 concern coordinate images, inverse images under coordinate diagonals, relative inverse images, and products; the comments reduce coordinate maps to permutations, face and degeneracy maps. The ornate glyph in the intersection statement resembles the permutation-group glyph in item a rather than the preceding M; it remains marked rather than normalized. The final word surjectif/injectif and several heavily cancelled lower lines are uncertain. The bar over m is retained as an abbreviation, not expanded.')

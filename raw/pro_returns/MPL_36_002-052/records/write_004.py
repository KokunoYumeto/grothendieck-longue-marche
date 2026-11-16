from save_page import save
tex=r'''
\scanpage{4}
\mspage{2}

$\ell-8$\quad pourquoi\quad \uline{donc}\qquad ?

\rule{\linewidth}{0.3pt}

p3\quad $\ell-8,-9$\qquad $B$ ?

\rule{\linewidth}{0.3pt}

p4.\quad 1.3.1.\quad As tu vérifié si l'accouplement d'\unsure{A. M.} coïncide avec le tien ?

$\ell\,4$.\quad \uline{formellement} non ramifié ?

$\ell\,7$.\quad \uline{séparablement} clos ?

$\ell\,14-20$.\quad Est-ce utile à dire, en l'absence de référence à ce que ce peut vouloir dire ?

$\ell-5$\quad Qu'il soit\qquad et\qquad \unsure{signifierait}\qquad plutôt ?

\rule{\linewidth}{0.3pt}

pg5\quad $\ell-2$\quad français :\quad les classes $\unsure{w|\omega}$\qquad \uline{en}\qquad relatifs.

\rule{\linewidth}{0.3pt}

pg6\quad $\ell\,4$\quad français.\quad dire\quad un Module inversible simple\qquad :

\deleted{\illegible{5}}

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.06)--(12,-0.06);\draw (0,-0.12)--(12,-0.12);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {2};\draw (0,0) circle (0.27);\draw (0.01,0.01) ellipse (0.31 and 0.29);\end{tikzpicture}}

pg7\quad français \uline{$\ell-9$}\quad
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {$\unsure{\subset|c}$};\draw (0,0) ellipse (0.21 and 0.26);\end{tikzpicture}}
$L_0$\quad donc
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {c'};\draw (0,0) ellipse (0.23 and 0.26);\end{tikzpicture}}
est

\deleted{$\ell\unsure{-8}$\quad \unsure{si}\quad \illegible{1}\quad \unsure{que}}
\quad $\ell-7$\quad
\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {que};\draw (0,0) ellipse (0.36 and 0.24);\end{tikzpicture}}
(le $2^{\mathrm{e}}$)

\rule{\linewidth}{0.3pt}

pg8\quad français\quad $\ell\,4$\quad par exemple\quad à\inserted{\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=2pt] (t) {pour};\draw (0,0) ellipse (0.34 and 0.20);\node at (0.48,0.03) {?};\end{tikzpicture}}}\quad $\ldots$

$\ell-7$\quad \uline{le} terme

\rule{\linewidth}{0.3pt}

pg14.\quad L'argument est un peu immoral; si $X$ et $Y$ sont extensions d'une VA par un tore et si $\varphi:X\longrightarrow Y$ est donné, alors $\varphi$ est strictement compatible à la filtration par les poids et $\varphi$ est une isogénie si et seulement si $T_\ell(\varphi)$ en est une.

\rule{\linewidth}{0.3pt}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {pg\deleted{\unsure{15|16}}20.};\draw (0,0) ellipse (0.85 and 0.55);\end{tikzpicture}}
Rmq 2.6 a)\quad $S$ est-il un trait dans cette remarque ; sait-on assez sur le passage à la limite et Néron ?

\margin{3}
'''
e=[('text','upper right','2'),('text','top l-8','pourquoi donc ?'),('drawing','under first note','horizontal divider'),('text','upper p3','l-8,-9 B ?'),('drawing','under p3','horizontal divider'),('text','upper p4 1.3.1','As tu vérifié si l’accouplement'),('text','p4 l4','formellement non ramifié ?'),('text','p4 l7','séparablement clos ?'),('text','p4 l14-20','Est-ce utile à dire'),('text','p4 l-5','Qu’il soit et signifierait plutôt ?'),('drawing','under p4','horizontal divider'),('text','middle pg5 l-2','français : les classes w en relatifs'),('drawing','under pg5','horizontal divider'),('text','middle pg6 l4','dire un Module inversible simple'),('deletion','below pg6 text','five heavily obliterated words'),('drawing','under pg6','three horizontal strokes'),('drawing','left section number','double-circled 2'),('text','lower pg7 l-9','français subset L0 donc c’est'),('drawing','pg7 first circled symbol','subset / c'),('drawing','pg7 second circled token','c prime'),('deletion','pg7 below first note','l-8 si ... que (uncertain/illegible)'),('text','pg7 l-7','que (le 2e)'),('drawing','pg7 l-7','que circled'),('drawing','under pg7','horizontal divider'),('text','pg8 l4','par exemple à ...'),('insertion','above à in pg8 l4','pour ?'),('drawing','inside pg8 insertion','oval around pour'),('text','pg8 l-7','le terme'),('drawing','under pg8','horizontal divider'),('text','pg14','L’argument est un peu immoral'),('drawing','under pg14','horizontal divider'),('drawing','bottom left page reference','pg deleted15 20 circled'),('deletion','inside bottom page reference','15 / 16'),('text','bottom Rmq 2.6 a','S est-il un trait'),('margin note','bottom left pencil','3')]
d=[{'line':'p4, 1.3.1','reading':'A. M.','alternatives':'second initial resembles Π','confidence':'medium'},{'line':'p4, l-5','reading':'signifierait','alternatives':'ending compressed','confidence':'medium'},{'line':'pg5, l-2','reading':'w','alternatives':'omega','confidence':'low'},{'line':'pg6, struck line','reading':'illegible, estimated 5 words','alternatives':'ink physically obscured by dense cancellation','confidence':'low'},{'line':'pg7, l-9','reading':'subset','alternatives':'c','confidence':'low'},{'line':'pg7, struck note','reading':'l-8 si [1 illegible word] que','alternatives':'number and surviving fragments uncertain','confidence':'low'},{'line':'pg20, corrected reference','reading':'deleted 15','alternatives':'deleted 16','confidence':'low'}]
save(4,tex,e,d,'Self-flagged verification question: “As tu vérifié si l’accouplement d’A. M. coïncide avec le tien ?”. Notes question formally unramified / separably closed hypotheses and absent references. Unproved assertion pg14: strict compatibility of a morphism of torus-by-abelian extensions with the weight filtration, and detection of isogenies by T_ell. Last question: trait hypothesis, passage to the limit, and Néron. Section number 2 is double circled; manuscript page 2; pencil 3.')

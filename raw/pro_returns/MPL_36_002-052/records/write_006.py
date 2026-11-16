from save_page import save
tex=r'''
\scanpage{6}
\mspage{4}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {\uline{pg41}};\draw[rotate=12] (0,0) ellipse (0.58 and 0.63);\end{tikzpicture}}
$\ell-2$\quad ``fonction de Dirac'' est malheureux (sur un groupe, on ne \unsure{voit|sait} trop si c'est\quad ou
$\left\{\begin{array}{l} f(e)=1,\ 0\ \text{ailleurs}\\ f(e)=\#G,\ 0\ \text{ailleurs}\end{array}\right.$)
\margin{\unsure{guillemets suffisent} ?}

\uline{pg42}\quad début dém. 4.7 : le \unsure{eps|cas} n'est pas clair pour $n=2$, et je n'ai pas confiance en dehors du cas strictement local.

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {5};\draw (0,0) ellipse (0.24 and 0.29);\end{tikzpicture}}

\uline{pg\unsure{45|47}}\quad $\ell\,3$ ss\quad français : beaucoup de ``donc''.

\uline{pg46}\quad Quel est le sens de (5.2.3.1) et de \deleted{\unsure{le}} ``par définition'' qui suit --

S'agit-il de pro-objets, ou de schémas.
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {je le dis !};\draw[rotate=10] (0,0) ellipse (0.90 and 0.31);\end{tikzpicture}}}

\uline{pg48}\quad $\ell-4$\quad Pourquoi as-tu barré connexe ?

\deleted{\uline{pg53}\quad 5.7 est une redite pour $\ell\ne p$, et un peu idiot pour $\ell=p$.}\quad (utilisé en 5.15)

\figure{\begin{tikzpicture}[baseline=(t.base)]\node[inner sep=3pt] (t) {\uline{pg56 bis}\quad 5.15};\node at (-1.23,0.02) {?};\draw (-0.25,0) ellipse (1.52 and 0.56);\end{tikzpicture}}
tu n'a plus besoin ici de $\operatorname{car}(k)\ne\ell$

54 quater -- 5.11.\quad seraient plutôt que seront.

\uline{55 ter}\quad $\ell-10$. Il serait honnête de dire que 6.6 utilise $\operatorname{car}(K)=0$, via Tate
\margin{\figure{\begin{tikzpicture}[baseline=(t.base)]\node[align=left] (t) {C'est dit\\dans les \unsure{hyp}\\de 5.15};\draw (0,0) ellipse (0.82 and 0.57);\end{tikzpicture}}}

\figure{\begin{tikzpicture}\draw (0,0)--(12,0);\draw (0,-0.08)--(12,-0.08);\draw (0,-0.16)--(12,-0.16);\end{tikzpicture}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {6};\draw (0,0) ellipse (0.23 and 0.26);\end{tikzpicture}}

\uline{pg57/58} : tu supposes tantôt $A^0$ $\ell$-divisible $(58,\ell-11)$, tantôt non $(57,\ell\,3)$

\uline{pg58}\quad $\ell-5$\quad
\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {$( {}_{p^\infty}X)^0$};\draw (0.52,0.14) ellipse (0.25 and 0.28);\node at (1.10,0) {?};\draw (1.10,0) ellipse (0.29 and 0.31);\end{tikzpicture}}
\qquad itou plus loin --

\uline{pg59}\quad Je ne comprends rien -- Que fais-tu de la partie discrète ? --
\margin{\uline{CANULAR ?!}}

Je ne crois pas que la plus grande \deleted{\unsure{VA}} sous VA ordinaire puisse se relever (\unsure{$\hat{\mathrm m}$|ni} en cas de bonne réduction).

\uline{ie}\quad \unsure{6.3|63} est faux (déformer de façon générale $E\times F$, $E$ et $F$ elliptiques, $E$ ordinaire, $F$ non ordinaire ; général $\Rightarrow$ générique simple.

\margin{5}
'''
e=[('text','upper right','4'),('drawing','upper left reference','pg41 circled'),('text','top pg41 l-2','fonction de Dirac est malheureux'),('display','top right','f(e)=1; f(e)=#G; 0 ailleurs'),('margin note','upper left pencil','guillemets suffisent ?'),('text','upper pg42','début dém. 4.7'),('drawing','upper divider','three horizontal strokes'),('drawing','middle left section number','circled 5'),('text','middle pg45 l3 ss','beaucoup de donc'),('text','middle pg46','Quel est le sens de (5.2.3.1)'),('deletion','inside pg46 before quotation','le uncertain'),('text','middle pg46 next line','S’agit-il de pro-objets'),('margin note','left beside pg46','je le dis !'),('drawing','margin beside pg46','oval around je le dis !'),('text','middle pg48 l-4','Pourquoi as-tu barré connexe ?'),('deletion','middle pg53 entire remark','5.7 est une redite'),('text','right after deleted pg53','(utilisé en 5.15)'),('drawing','lower middle reference','? pg56 bis 5.15 circled'),('text','pg56 bis 5.15','tu n’a plus besoin ici'),('text','54 quater 5.11','seraient plutôt que seront'),('text','55 ter l-10','Il serait honnête de dire'),('margin note','left beside 55 ter','C’est dit dans les hyp de 5.15'),('drawing','left beside 55 ter','oval around pencil answer'),('drawing','lower divider','three horizontal strokes'),('drawing','lower left section number','circled 6'),('text','lower pg57/58','tu supposes tantôt A^0 ell-divisible'),('text','lower pg58 l-5','(p-infinity X)^0 ? itou plus loin'),('drawing','pg58','oval around 0 and circled question mark'),('text','bottom pg59 first paragraph','Je ne comprends rien'),('margin note','bottom left slanted','CANULAR ?!'),('text','bottom pg59 next paragraph','Je ne crois pas que la plus grande'),('deletion','inside bottom paragraph before sous','VA uncertain'),('text','bottom final paragraph','ie 6.3 est faux'),('margin note','bottom left pencil','5')]
d=[{'line':'pg41 l-2','reading':'voit','alternatives':'sait','confidence':'medium'},{'line':'pg41 pencil','reading':'guillemets suffisent ?','alternatives':'faint final letters','confidence':'medium'},{'line':'pg42 début dém.','reading':'eps','alternatives':'cas','confidence':'low'},{'line':'first reference in section 5','reading':'pg45','alternatives':'pg47; overwritten final digit','confidence':'low'},{'line':'pg46','reading':'deleted le','alternatives':'dense cancellation','confidence':'low'},{'line':'55 ter, pencil answer','reading':'hyp','alternatives':'word overlaps page reference','confidence':'low'},{'line':'pg59 before sous VA','reading':'deleted VA','alternatives':'cancelled two-letter fragment','confidence':'low'},{'line':'pg59 parenthesis','reading':'m with circumflex','alternatives':'ni','confidence':'low'},{'line':'pg59 final paragraph','reading':'6.3','alternatives':'63; separating dot not distinct','confidence':'medium'}]
save(6,tex,e,d,'Several explicit objections: Dirac-function normalization; proof 4.7 unclear for n=2 and not trusted outside strictly local case; pro-objects versus schemes. Crossed-out criticism of 5.7 (redite for ell != p, idiot for ell=p) followed by note “utilisé en 5.15”. Hypothesis car(k)!=ell questioned for 5.15; use of characteristic zero via Tate in 6.6 is requested, answered in pencil as already in hypotheses of 5.15. Inconsistent ell-divisibility and omission of discrete part queried. Strong objection to lifting greatest ordinary sub-VA; “6.3 est faux” with proposed deformation of E x F (E ordinary, F nonordinary elliptic) to a generically simple variety. Marginal CANULAR ?!; distinguish this manuscript’s objection from proof of counterexample.')

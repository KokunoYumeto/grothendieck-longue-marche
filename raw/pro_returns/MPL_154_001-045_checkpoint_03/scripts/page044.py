from workflow import save_page
tex=r'''\scanpage{44}
\margin{43}
\margin{\unsure{31.12.83|31.11.83}}
\uline{Déploiement} d'un syst. de pseudo-droites. $\underline\Sigma=(X,\Sigma)$, $\Sigma=\unsure{(D_i)_{i\in I}}$

surface compacte $\mathcal X=\mathcal X(\underline\Sigma)$, avec deux sous-graphes $K,L$ tels que $K,L$ découpent cellulairement $\mathcal X$.

a) Tous les pts de $K$ sont d'\uline{ordre 4}. (D'où déploiement $\unsure{\widetilde K'|\widehat K'}$ de $K$ qui est une courbe topologique)

\deleted{\unsure{b)}} Tous les pts de $L$ sont d'ordre pair, les quatre arêtes qui en \unsure{sortent} \inserted{sont distinctes (pas de boucle \unsure{topique})}.

b) \deleted{Pour} toute arête de $K$ contient au plus un sommet de $L$.

c) La réunion \inserted{$K_0$} des adh. des arêtes de $K$ qui ne contiennent pas de sommets \inserted{de $L$ (arêtes exceptionnelles de $K$)} est une réunion finie de cercles, \deleted{indexée par $I$}

\deleted{d) Soit $K_1$ la réunion des autres \unsure{composantes} de}

[Il revient au $=$ d'exiger que \unsure{l'arête} de $K$ \unsure{opposée} à une arête exceptionnelle est exceptionnelle, et que \deleted{\unsure{les pts}}\inserted{\unsure{pour}} les sommets de $K$, il existe au moins une arête issue de ce sommet qui \deleted{n'est pas} est ``ordinaire''.

\deleted{\textcircled{d} \unsure{Alors}} Soit $K_1$ la réunion des adh. des arêtes \deleted{\unsure{exceptionnelles}}\inserted{ordinaires} de sorte que \inserted{$\unsure{N}$} $K'_1$ est une \deleted{réunion de} partie ouverte et fermée \inserted{$\unsure{N}$} de $K'$ (i.e réunion de comp. connexes). Alors on \unsure{redonne} une section \deleted{du} fibré des bandes pour l'immersion $K'_1\hookrightarrow\mathcal X$.

\margin{cette donnée résulte en fait des autres, revoir \unsure{position} de e)\quad cf plus bas}

e) Soit $s$ un sommet exceptionnel de $K$ (i.e. sommet incident à une arête exceptionnelle). Alors sur \deleted{\unsure{la}} une arête \inserted{\deleted{\unsure{unique}} non exceptionnelle} \inserted{(pt critique de $K$)} \deleted{iss} incidente à $s$, entre $s$ et le \unsure{1er} sommet de $L$

\figure{\begin{tikzpicture}[x=.65cm,y=.65cm,line cap=round]
\draw[yellow!60!green,line width=3pt](0,1.4)--(0,0)--(2.5,0)--(2.5,1.7);
\draw[green!25!black,line width=4pt](0,0)--(2.5,0);\fill(2.5,0)circle(4pt);
\draw[red!65!orange,line width=2pt](1.8,1.85)--(3.1,1.4);
\draw[red!65!orange,line width=2pt](1.8,1.4)--(3.1,1.85);
\draw[red!65!orange,line width=2pt](2,1.65)--(3.1,1.65);
\draw[red!65!orange,dashed,line width=1.5pt](.8,-.8)--(.8,.8);
\draw[red!65!orange,dashed,line width=1.5pt](1.3,-.8)--(1.3,.8);
\draw[red!65!orange,dashed,line width=1.5pt](1.9,-.8)--(1.9,.8);
\node at(2.15,-1){$L$};
\end{tikzpicture}}

\inserted{multiplicités des arêtes \inserted{ord} issues de $s$ sont les $=$.}

d'autres pts de $L$. De plus, les \inserted{les deux} deux pts critiques en vis à vis,

f) Pour tt $x\in L\cap K$, ttes branches de $L$ en $x$ croisent les branches de $K$ en $x$. Si $x$ est un sommet de $K$, alors $x$ est un pt d'ordre \deleted{4}\inserted{réduit 2} de $L$. et tout secteur angulaire local de $K$ en $x$ \deleted{\unsure{contient exactement un}} \inserted{\unsure{une arête de} $L$} \inserted{\unsure{deux}} contient exactement une arête de $L$ aboutissant à $x$. (Donc trois cas de figure pour un $x\in K\cap L$

f') Un sommet exceptionnel \inserted{$s$} de $K$ n'est pas sommet de $L$, i.e $s\notin L$.

g) \deleted{Un sommet} Pour un sommet \deleted{ordinaire} $s$ de $K$, pour les 4 arêtes \inserted{(ordinaires)} de $K$ qui en sortent, \unsure{le nb} d'\uline{élts de} $L$ (\deleted{\unsure{prè. de}} entre $s$ et l'unique sommet de $L$ sur l'arête \deleted{\unsure{(point qui est}} indépendant de l'arête, soit $\nu(s)$).

\deleted{Soit $\varepsilon(s)=\begin{cases}+1&\text{si }s\in L\\0&\text{si }s\notin L\end{cases}$}

\deleted{Pour ttes arêtes ordinaires, soit $\nu(a)$ la multiplicité réduite de l'unique sommet \unsure{de} $\unsure{\ell}-1$}

h) \deleted{Pour tte arête $a$ de $K$, soit $\nu(a)$ le nb des pts simples de $L$ sur $a$ ($=\nu(s)+\nu(s')$, si $a$ est ordinaire d'extrémités $s,s'$) et}

Soit $n$ l'ordre de $\Sigma$. Alors pour tte face $F$ de $K$, le nb des pts de $L$ sur $\partial F$, chacun compté avec sa multiplicité réduite est $2n$.

\margin{NB \unsure{à} $F$ \unsure{ordinaire}, c'est égal :
\[
\sum_{\substack{s\text{ incident}\\\text{à }F}}(2\nu(s)+\varepsilon(s))
+\sum_{\substack{a\text{ incident}\\\text{à }F}}\nu(a)
\]}

\figure{\begin{tikzpicture}[x=.7cm,y=.7cm,line cap=round]
\begin{scope}[shift={(0,4.4)}]
\draw[yellow!65!green,line width=3pt](-1.5,0)--(1.5,.05);
\draw[yellow!65!green,line width=3pt](-1.6,-.25)--(-1.4,0)--(-1.55,.3);\draw[yellow!65!green,line width=3pt](1.6,-.2)--(1.4,.05)--(1.55,.3);
\draw[red!70!orange,line width=3pt](-.4,1)--(.5,-.9);
\draw[red!70!orange,line width=3pt](.1,1.15)--(-.2,-.95);
\draw[red!70!orange,line width=3pt](.7,1.25)--(-.55,-.7);
\node at(2.3,.2){b)};
\end{scope}
\begin{scope}[shift={(0,2.7)}]
\draw[yellow!65!green,line width=3pt](-1.6,0)--(1.6,.05);
\draw[yellow!65!green,line width=3pt](-1.7,-.25)--(-1.5,0)--(-1.65,.3);\draw[yellow!65!green,line width=3pt](1.7,-.2)--(1.5,.05)--(1.65,.3);
\draw[red!70!orange,line width=3pt](.2,.5)--(-.2,-.6);\node at(2.3,.1){a)};
\end{scope}
\begin{scope}
\draw[yellow!65!green,line width=3pt](-2.5,0)--(.7,.05);\draw[yellow!65!green,line width=3pt](-1,1.3)--(-1,-1.3);
\draw[red!70!orange,line width=3pt](-1.55,.6)--(-.5,-.65);\draw[red!70!orange,line width=3pt](-.5,.65)--(-1.55,-.6);\node at(1.5,.15){c)};
\end{scope}
\end{tikzpicture}}

a) $x$ \deleted{\unsure{un sommet de} $L$}\inserted{$\notin S(L)$}, donc pt d'ordre 2 de $L$, alors $x\notin S(K)$

b) $x\in S(L)\cap\mathrm{C}S(K)$

c) $x\in S(L)\cap S(K)$
'''
e=[('margin note','bottom left','43'),('margin note','top left date','31.12.83'),('text','top heading','Déploiement d’un syst.'),('text','top second paragraph','surface compacte'),('text','left upper a','Tous les pts de K'),('text','left upper parenthesis','D’où déploiement'),('deletion','left upper before Tous','b)'),('text','left upper','Tous les pts de L'),('insertion','left upper','sont distinctes, pas de boucle'),('text','left upper b','toute arête de K'),('deletion','left upper b','Pour'),('text','left c','La réunion'),('insertion','left c','K_0'),('insertion','left c','de L (arêtes exceptionnelles de K)'),('deletion','left c','indexée par I'),('deletion','left center first d','Soit K_1 la réunion'),('text','left center bracket','Il revient au = d’exiger'),('deletion','left center bracket','les pts'),('insertion','left center bracket','pour'),('deletion','left center bracket','n’est pas'),('deletion','left lower repeated d','d Alors'),('text','left lower repeated d','Soit K_1 la réunion'),('deletion','left lower','exceptionnelles'),('insertion','left lower','ordinaires'),('insertion','left lower near K_1 prime','N'),('deletion','left lower','réunion de'),('insertion','left lower near fermée','N'),('text','left lower','Alors on redonne'),('deletion','left lower','du'),('margin note','diagonal left margin','cette donnée résulte'),('text','left e','Soit s un sommet exceptionnel'),('deletion','left e','la'),('deletion','left e insertion','unique'),('insertion','left e','non exceptionnelle'),('insertion','left e','pt critique de K'),('deletion','left e','iss'),('drawing','lower gutter','green angular path, black point, orange rays and dashed crossings, L'),('insertion','lower gutter','multiplicités des arêtes issues de s'),('insertion','lower gutter','ord'),('text','left e continuation','d’autres pts de L'),('insertion','left e continuation','les deux'),('text','left bottom f','Pour tt x dans L inter K'),('deletion','left bottom f','4'),('insertion','left bottom f','réduit 2'),('deletion','left bottom f','contient exactement un'),('insertion','left bottom f','une arête de L'),('insertion','left bottom f','deux'),('text','right top f prime','Un sommet exceptionnel'),('insertion','right top','s'),('text','right upper g','Pour un sommet'),('deletion','right upper g','Un sommet'),('deletion','right upper g','ordinaire'),('insertion','right upper g','ordinaires'),('deletion','right upper g','prè. de'),('deletion','right upper g','point qui est'),('deletion','right middle formula','Soit epsilon(s), cases +1,0'),('deletion','right middle red and black','Pour ttes arêtes ordinaires'),('deletion','right middle h','Pour tte arête a de K'),('text','right lower','Soit n l’ordre de Sigma'),('margin note','right lower NB','NB à F ordinaire'),('display','right lower margin','sum (2 nu(s)+epsilon(s)) + sum nu(a)'),('drawing','right lower top b','green horizontal edge and red six-ray crossing'),('drawing','right lower middle a','green edge and red single transverse segment'),('drawing','right lower bottom c','green cross and red four-ray crossing'),('text','bottom right a','x not in S(L)'),('deletion','bottom right a','un sommet de L'),('insertion','bottom right a','not in S(L)'),('text','bottom right b','x in S(L) inter C S(K)'),('text','bottom right c','x in S(L) inter S(K)')]
d=[('top date','31.12.83 / 31.11.83','Second month digit is a near-vertical stroke; first reading retained with alternative.','low'),('title indexing','(D_i) indexed by i in I','Tiny index and terminal indexing sign.','medium'),('surface notation','mathcal X','Curved upper and lower strokes form calligraphic X; not a separately added hat.','medium'),('a parenthesis','tilde K prime / hat K prime','Heavy upper mark and visible prime.','low'),('after order pair','quatre arêtes qui en sortent; boucle topique','Small compressed inserted text; topique especially doubtful.','low'),('bracket after c','l’arête de K opposée','Tiny writing above canceled d sentence; exact noun and participle uncertain.','low'),('same bracket','pour les sommets','Overwritten preposition above deleted les pts.','low'),('d two inserted letters','N; N','Isolated caret-linked signs around K_1 prime and fermée; retained as N with doubt.','low'),('d','on redonne','Verb in compressed connective line.','medium'),('diagonal margin','position de e)','Rotated handwriting; noun position uncertain.','low'),('e main and insertions','non exceptionnelle; pt critique de K; 1er sommet','Crowded crossing lines and arrows; attachment and numeral uncertain, all text retained.','low'),('f canceled lower line','contient exactement un; une arête de L; deux','Several overwritten alternatives below baseline; wording/attachment least secure.','low'),('g','le nb d’élts; prè. de; point qui est','Crossed/abbreviated clauses left unreconstructed.','low'),('red canceled paragraph','multiplicité réduite de l’unique sommet de ell−1','Final symbol/word and relation uncertain; best literal attempt.','low'),('NB before sum','à F ordinaire','Connecting letters uncertain; the sum itself is clear apart from epsilon shape.','low'),('bottom a cancellation','un sommet de L','Struck phrase replaced by not in S(L).','low')]
save_page(44,tex,e,d,'''Dated heading Déploiement d’un syst. de pseudo-droites (date reading uncertain 31.12.83/31.11.83). Axiomatization via compact surface mathcal X and graphs K,L; degree/crossing requirements, exceptional edge circles, ordinary edge immersion and band section. Many revisions in (c)–(h), especially reduced multiplicities, must be separated in notes. Marginal says band datum follows from others and revoir position de e), cf plus bas—self-flagged verification/reorganization. Weight condition on each face: reduced multiplicities of L on boundary total 2n, with vertex/edge sum expression. Exceptional vertex not in L; ordinary local branches have equal counts. Need reading questions for incomplete (e), repeated d, inserted N signs, and canceled epsilon/nu definitions; do not treat all as a settled axiom system.''')

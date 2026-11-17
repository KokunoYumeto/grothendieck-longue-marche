from workflow import save_page
tex=r'''\scanpage{26}
\mspage{14}
\margin{25}

Dans le cas actuel, il se trouve que cet iso. des \unsure{deux pol.} \deleted{\unsure{définis}} \inserted{\unsure{est au point}} pour induire \unsure{de lui-même} $\operatorname{Pol}^*(D)\longrightarrow\operatorname{Pol}^*(D')$ ayant les propriétés \unsure{signalées}.

Il faudrait examiner à part la situation de spécialisation vers un $\Delta$ supersingulier.

24.12. Finalement, il apparaît que c'est le polygône $\unsure{\operatorname{Pol}^{\wedge}(D)|\operatorname{Pol}^{*}(D)}$ qui est ``le bon'', ou encore mieux, le polygône dual ; \unsure{le passage} \deleted{\unsure{d'un}} au dual revient à passer à la carte \uline{duale} de celle considérée hier --- c'est la carte duale qui est la plus intuitive encore. À partir de positions relatives, on visualise le polygône \unsure{dual} $\operatorname{Pol}(D)$ (\unsure{un nouveau dessin !}) comme \deleted{le bord} associé au pôle $D$, bord d'un petit voisinage tubulaire autour de $D$, ou encore bord du disque $\Delta(D)$ fermé complt de l'intérieur de ce voisinage tubulaire, et la carte qui nous intéresse peut être considérée comme obtenue en recollant les disques $\Delta(D)$, d'une façon naturelle que je viens de \unsure{m'expliquer} --- ou plutôt, \deleted{\unsure{ce}} qu'on déduit de ces disques en prenant \inserted{pour chaque $\Delta(D)$} sur le bord les ``arêtes libres'' (i.e. celles qui ne sont arêtes de spécialisation ni de générisation) \inserted{marquées en vert et bleu ici}, et en les repliant par le milieu, de sorte qu'on trouve un disque \inserted{$\Delta'(D)$} dans lequel les arêtes \inserted{repliées} précédentes apparaissent comme \inserted{autant de} segments allant du bord vers l'intérieur. Si on garde le tracé du \deleted{\unsure{le}} syst. de droites (en rouge) à l'intérieur de $\Delta'(D)$ (cf figure ci-contre, voisinage du bord) \unsure{on dénoue} des points doubles

\figure{\begin{tikzpicture}[x=0.7cm,y=0.7cm,line cap=round,line join=round]
\draw[yellow!65!green,line width=1.6pt] (0,0) ellipse (2.7 and 3.1);
\fill[yellow!80!orange] (-.1,3.2)--(-.5,1.3)--(.12,2.5)--cycle;
\fill[yellow!80!orange] (-2.2,1.9)--(-2,0)--(-1.35,.65)--cycle;
\fill[yellow!80!orange] (-2.9,-.5)--(-1.8,-.75)--(-2.1,-.1)--cycle;
\fill[yellow!80!orange] (-.1,-3.3)--(.3,-1.8)--(-.4,-2.3)--cycle;
\fill[yellow!80!orange] (1.9,-2.5)--(.9,-1.2)--(1.6,-.9)--cycle;
\fill[yellow!80!orange] (2.9,.8)--(1.1,.75)--(1.6,.35)--cycle;
\fill[orange!90!yellow] (-.65,1.3)--(-1.05,1.05)--(-.55,.65)--cycle;
\fill[yellow!85!orange] (.1,.5)--(1.1,.05)--(1.4,.6)--cycle;
\draw[orange!90!yellow,line width=2.8pt] (-2.25,2.15) .. controls (-2.2,-1) and (-1,-1.8) .. (2,-2.65);
\draw[orange!90!yellow,line width=2.8pt] (-1.8,2.65) .. controls (-1.2,.8) and (1.1,-.7) .. (1.7,-2.8);
\draw[orange!90!yellow,line width=2.8pt] (-.35,3.35) .. controls (-.8,1.4) and (-.85,-1.7) .. (-.2,-3.35);
\draw[orange!90!yellow,line width=2.8pt] (-.05,3.3) .. controls (.1,1.4) and (.2,-1.4) .. (-.1,-3.35);
\draw[orange!90!yellow,line width=2.8pt] (-2.95,-.45) .. controls (-1.4,.6) and (1.5,.8) .. (3,.85);
\draw[orange!90!yellow,line width=2.8pt] (-3,-.2) .. controls (-1.8,-1.3) and (1.2,.6) .. (3,1.1);
\draw[orange!90!yellow,line width=2.8pt] (-1.55,-2.8) .. controls (-1,0) and (-1.2,2.7) .. (2.15,2.1);
\draw[orange!90!yellow,line width=2.8pt] (-1.3,-2.9) .. controls (1.7,-2.1) and (1.1,1.3) .. (1.75,2.75);
\draw[blue!65!green,line width=3pt] (-2.65,-.55)--(-2.63,-.2) (-.28,-3.02)--(.02,-3.02) (2.65,.7)--(2.65,.9) (-.23,3.03)--(.02,3.03);
\draw[green!45!black,line width=3pt] (-2.18,1.92)--(-1.96,2.2) (1.72,2.43)--(2.1,2.12) (1.6,-2.63)--(1.84,-2.34);
\node at (-1.35,2.85) {$\unsure{1}$};\node at (-2.05,2.6) {$\unsure{2}$};\node at (-2.85,.8) {$3$};\node at (-2.8,-1.4) {$4$};\node at (-1.55,-3.15) {$5$};\node at (-.95,-3.3) {$6$};\node at (.65,-3.2) {$7$};\node at (2.15,-2.6) {$8$};\node at (2.8,-1.4) {$9$};\node at (2.7,1.5) {$10$};\node at (1.7,2.85) {$\unsure{11}$};\node at (.8,3.15) {$12$};
\begin{scope}[shift={(3.2,-3.4)},scale=.55]
\draw[yellow!65!green,line width=2pt] (0,0) circle (2);
\draw[blue!65!green,line width=4pt] (85:1.9) arc(85:32:1.9) (7:1.9) arc(7:-80:1.9) (-132:1.9) arc(-132:-178:1.9) (165:1.9) arc(165:140:1.9);
\draw[green!40!black,line width=4pt] (136:1.9) arc(136:90:1.9) (30:1.9) arc(30:8:1.9) (-84:1.9) arc(-84:-130:1.9);
\foreach \a in {90,140,178,-132,-84,8,32}{\draw[orange!90!yellow,line width=3pt] (\a:1.9)--({\a-12}:1.25) (\a:1.9)--({\a+12}:1.25);\draw[yellow!65!green,line width=3pt] (\a:1.9)--(\a:1.05);}
\node at (.35,1.15) {$1$};\node at (-.45,1.4) {$2$};\node at (-1.15,1) {$3$};\node at (-1.45,.6) {$4$};\node at (-1.1,.2) {$5$};\node at (-1,-.4) {$6$};\node at (-.4,-.5) {$7$};\node at (.1,-.5) {$8$};\node at (.8,-.7) {$9$};\node at (.75,.15) {$10$};\node at (1,1) {$11$};\node at (.5,1.3) {$\unsure{12}$};
\end{scope}
\end{tikzpicture}} % crop-candidate: scan 26
'''
e=[('text','left top','Dans le cas actuel'),('deletion','left top','définis'),('insertion','left top','est au point'),('display','left top','Pol star(D) → Pol star(D prime)'),('text','left upper','Il faudrait examiner à part'),('text','left middle','24.12. Finalement'),('display','left middle','Pol wedge(D)'),('deletion','left middle','d’un'),('text','left middle','carte duale'),('text','left lower','pôle D; disque Delta(D)'),('deletion','left lower','le bord'),('text','right upper','intéresse peut être considérée'),('deletion','right upper middle','ce'),('insertion','right upper middle','pour chaque Delta(D)'),('text','right middle','arêtes libres'),('insertion','right middle','marquées en vert et bleu ici'),('text','right middle lower','et en les repliant'),('insertion','right lower','Delta prime(D)'),('insertion','right lower','repliées; autant de'),('text','right bottom','Si on garde le tracé'),('deletion','right bottom','le'),('drawing','lower middle','disk with coloured arrangement and 1–12'),('drawing','lower right middle','folded boundary circle with coloured stubs and 1–12')]
d=[('first paragraph','deux pol.; définis; est au point; de lui-même','Compressed and overwritten clause; first-pass lexical readings particularly tentative','low'),('24.12 opening notation','Pol wedge(D) / Pol star(D)','The raised angled mark may be a hat written to the right rather than star','low'),('left middle to lower','le passage; d’un; un nouveau dessin !','Fast short phrases, cancellation and parenthetic exclamation','low'),('right paragraph','m’expliquer; ce; on dénoue','Short correction and terminal verb are uncertain','medium'),('large/small figures','1, 2, 11, 12','Some pencil numerals are faint against the printed show-through; approximation preserves their locations','low')]
obs='Explicit pending examination: specialization to supersingular Delta. Dated 24.12 entry identifies dual polygon/cartography as more intuitive. Construction by complementary disks and folding free boundary edges is presented, with two numbered coloured drawings; next page continues. First paragraph and several local readings require especially careful second audit.'
save_page(26,tex,e,d,obs,sheet_kind='reused_typed')

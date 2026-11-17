from workflow import save_page
tex=r'''\scanpage{40}
\margin{39}
\uline{1 \deleted{type}\inserted{côté de} spécialisation} (les arcs \deleted{qui}\inserted{de transition} sont de spécialisation)

\uline{1 \deleted{type}\inserted{côté de type} générisation} (les arcs de transition sont de gén.)

1 \uline{côté de type} mixte.

Quand on contourne les coins en partant du côté spécialisation, on trouve dans l'ordre :
\diagram{\begin{array}{rcl}
1)\ \text{spécialisation}&\longrightarrow&\text{spécialisation}\\
2)\ \text{générisation}&\longrightarrow&\text{spécialisation}\\
3)\ \text{générisation}&\text{---}&\text{générisation}\\
4)\ \text{spécialisation}&\longrightarrow&\text{générisation}
\end{array}}
(\unsure{Qu'on tourne} dans un sens, ou dans l'autre)

Ainsi il y a \deleted{deux côtés}\inserted{un côté} de type spéc., un autre de type générisation, et deux de type mixte. Les faces correspondent biunivoquement aux \deleted{points}\inserted{couples} $(L,a)$, où $L$ est une position relative, et $a$ un arc \deleted{de spéc. \unsure{ou}} d'inertie de type spécialisation (ou de type générisation, au choix, il y a corr. 1-1 entre les deux types de couples). Le deuxième type est peut-être plus \unsure{joli} comme description, car il s'agit de trouver

a) les paires de sommets \inserted{$(s,t)$} non alignés de $\overline\Sigma$ \inserted{et les p.r. \inserted{(critiques forcément)} qui y passent};

b) pour une telle donnée $(s,t,L)$,

s'il y a un arc de neutralité ayant \deleted{\unsure{ses}} ses extrémités au dessus de $(s,t)$ (a priori, il est possible quatre arcs à \unsure{construire}\ldots) et les classer. C'est surtout une description agréable dans les cas \inserted{(très)} particuliers où par deux sommets non alignés passe une unique position relative.

\figure{\begin{tikzpicture}[x=.75cm,y=.75cm,line cap=round]
\draw[yellow!70!green,line width=2pt](0,0)ellipse(1.6 and1.65);
\draw[orange!70!red,line width=1.7pt](-.1,1.65)..controls(-.6,.3)and(-.65,-.6)..(-.4,-1.6);
\draw[orange!70!red,line width=1.7pt](.15,1.64)..controls(.3,.4)and(.05,-.9)..(-.1,-1.65);
\draw[orange!70!red,line width=1.7pt](.4,1.6)..controls(.7,.3)and(.3,-.9)..(.15,-1.64);
\draw[orange!70!red,line width=1.7pt](-1.25,-1)..controls(-.5,.1)and(.55,.9)..(1.35,.9);
\draw[orange!70!red,line width=1.7pt](-1.25,-1)..controls(.1,-.6)and(1,.5)..(1.35,.9);
\draw[->](-1.7,1)..controls(-1.4,1.7)and(-.8,1.85)..(-.2,1.85);
\draw[->](-1.75,.6)..controls(-1.8,-.2)and(-1.6,-.6)..(-1.4,-1);
\node at(-1.8,.8){4};
\draw[->](.95,1.65)..controls(.7,1.8)and(.55,1.85)..(.4,1.85);
\draw[->](1.1,1.6)--(1.25,1.25);\node at(1.1,1.85){1};
\draw[->](1.7,-.7)..controls(1.9,.1)and(1.8,.7)..(1.5,1);
\draw[->](1.65,-1)..controls(1.2,-1.6)and(.7,-1.85)..(.3,-1.85);\node at(1.8,-.85){2};
\draw[->](-.75,-1.75)--(-.45,-1.8);\draw[->](-.9,-1.6)--(-1.3,-1.25);\node at(-.95,-1.85){3};
\end{tikzpicture}}

La construction de la surface cellulaire n'est pas complète, car on a laissé de côté, dans le processus de recollement, les positions relatives supercritiques, et les arcs de spécialisation et de générisation qui vont aux uns \unsure{partant} de ces dernières. Donc \deleted{\unsure{ça}} il manque encore des disques polygonaux qu'il faut recoller sur les arêtes qui restent libres pour les recollements : on pourrait néanmoins
'''
e=[('margin note','bottom left','39'),('text','left top first classification','1 type spécialisation'),('deletion','left top','type'),('insertion','left top','côté de'),('deletion','left top parenthesis','qui'),('insertion','left top parenthesis','de transition'),('text','left top second classification','1 type générisation'),('deletion','left second classification','type'),('insertion','left second classification','côté de type'),('text','left third classification','1 côté de type mixte'),('text','left upper middle','Quand on contourne'),('diagram','left middle','four transition types'),('text','left middle parenthesis','Qu’on tourne'),('text','left middle','Ainsi il y a'),('deletion','left middle','deux côtés'),('insertion','left middle','un côté'),('deletion','left middle','points'),('insertion','left middle','couples'),('deletion','left lower','de spéc. ou'),('text','left lower','Le deuxième type'),('text','left lower a','les paires de sommets'),('insertion','left lower a','(s,t)'),('insertion','left lower a','et les p.r. qui y passent'),('insertion','left lower a','(critiques forcément)'),('text','left bottom b to right top','pour une telle donnée'),('deletion','right top','ses'),('insertion','right middle','(très)'),('drawing','right upper middle','disk with four numbered pairs of boundary arrows'),('text','right lower','La construction de la surface'),('deletion','right lower','ça')]
d=[('left classification','1 côté de type mixte','Visible numeral is 1 although later paragraph says deux; retained.','high'),('third displayed transition','plain dash','No arrowhead visible, unlike other three lines.','high'),('left lower','joli','Short adjective before comme description.','medium'),('right upper parenthesis','quatre arcs à construire…','Compressed word after à uncertain; dots are present in manuscript.','low'),('right lower','vont aux uns partant','Contracted linking words before de ces dernières; uncertain reading preserved.','low')]
save_page(40,tex,e,d,'''Three corner types, four cyclic transitions, and a bijection of faces with pairs (L,a) of inertia arcs. Suggests classifying via nonaligned vertex pairs and relative positions through them, particularly when unique. Explicitly says surface construction is incomplete because supercritical relative positions and their incoming/outgoing arcs were omitted; missing disks must be glued to remaining free edges. This is a standing self-flagged incompleteness item. Initial count 1 mixed side conflicts with later two; transcription retains the numeral, note should flag reading/stated discrepancy.''',sheet_kind='reused_typed')

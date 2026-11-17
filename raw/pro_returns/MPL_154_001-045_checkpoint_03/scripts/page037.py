from workflow import save_page
tex=r'''\scanpage{37}
\margin{36}
Il peut arriver que $L$ admette \uline{deux} arcs de spécialisation exceptionnels, ce qui est le cas ssi $L$ est \uline{\unsure{position}} ``bissectrice'' d'un couloir de $C$.

\figure{\begin{tikzpicture}[x=.6cm,y=.6cm,line cap=round]
\draw[yellow!70!green,line width=2pt] (0,0) ellipse(2.2 and 2.1);
\draw[green!25!black,line width=3pt] (.1,2.1) arc(87:267:2.2 and 2.1);
\draw[green!25!black,line width=3pt] (.35,2.07) arc(81:-88:2.2 and 2.1);
\draw[blue!50!green,line width=3pt] (.1,2.1)--(.35,2.07);
\draw[blue!50!green,line width=3pt] (-.12,-2.1)--(.25,-2.1);
\draw[orange!70!red,line width=1.5pt] (.1,2.1)..controls(-.7,.6)and(-.75,-1.2)..(-.12,-2.1);
\draw[orange!70!red,line width=1.5pt] (.3,2.07)--(.05,-2.1);
\draw[orange!70!red,line width=1.5pt] (.55,2.02)..controls(.75,.6)and(.4,-1.3)..(.25,-2.1);
\draw[orange!70!red,line width=1.5pt] (-1.75,1.3)--(2.15,.1);
\draw[orange!70!red,line width=1.5pt] (-2.15,.6)..controls(-1,.1)and(.8,-.6)..(1.9,-.65);
\draw[orange!70!red,line width=1.5pt] (-2.2,-.35)..controls(-.5,-.35)and(.9,.8)..(1.8,1.2);
\draw[orange!70!red,line width=1.5pt] (-1.5,-1.55)..controls(.15,-1.25)and(-1.2,1)..(1.4,1.6);
\draw[orange!70!red,line width=1.5pt] (-.65,.1)..controls(.7,-1.3)and(1.5,.1)..(2.15,.6);
\draw[black] (1.3,-.6)--(1.43,-.54)--(1.53,-.6)--(1.7,-.56);
\end{tikzpicture}} % crop-candidate: scan 37
Dans ce cas, il n'existe pas d'autre arc de spécialisation, et exactement deux arcs de générisation, et l'ensemble de ces quatre arcs est l'ensemble des \deleted{arcs}\inserted{côtés} d'une structure de polygone topologique sur $\widetilde D$.

Dans tous les cas, les deux \uline{arcs de transition} (i.e. de spécialisation ou de générisation) \inserted{distincts} ne se rencontrent que si l'un d'eux est un arc de spécialisation exceptionnel, l'autre un arc de générisation, et alors ils sont adjacents.

On appelle \uline{arcs d'inertie} \inserted{(ordinaires)} les \deleted{arcs de} adhérences des composantes connexes du complémentaire de la réunion de l'ensemble des arcs de transition, en leur ajoutant combinatoirement les deux sommets sur $L$. Mieux,

\deleted{Ainsi le} on appelle \uline{sommets de transition} les sommets sur $\widetilde L$ qui sont extrémités d'arcs de transition. Ces sommets partagent $\widetilde L$ en des arcs, qui sont de trois types :

$\left\{\vphantom{\begin{matrix}a\\b\\c\\d\\e\\f\end{matrix}}\right.$
a) les arcs de générisation

b) les arcs de spécialisation (ordinaire et exceptionnelle)

c) les \deleted{arcs de} arcs qui ne sont ni de type a), ni de type b), et qu'on appelle \uline{arcs d'inertie}. (ils sont ``inertes'' dans le processus de transition d'une pos. rel. à une autre)

\margin{\uline{arcs caractéristiques} qui sont les côtés du \uline{polygone caractéristique}}

Dans les cas où il n'y a pas d'arc de spécialisation exceptionnel, sur deux arcs \inserted{caractéristiques} adjacents, \deleted{\unsure{il}} un et un seul est un arc d'inertie, l'autre étant de générisation, ou de spécialisation. Deux arcs d'inertie ne sont jamais adjacents. Si deux arcs caractéristiques sont adjacents, \deleted{l'un de} et si aucun n'est un arc d'inertie, \inserted{alors} l'un \deleted{d'eux est un triangle} de spécialisation exceptionnel, l'autre est un arc de générisation. Parfois, le \deleted{arc} \unsure{ponctuel} (réduit au sommet qui
'''
e=[('margin note','bottom left','36'),('text','left opening','Il peut arriver'),('drawing','left upper middle','disk with two blue and two green boundary arcs'),('text','left upper middle','Dans ce cas'),('deletion','left middle','arcs'),('insertion','left middle','côtés'),('text','left middle','Dans tous les cas'),('insertion','left middle','distincts'),('text','left lower','On appelle arcs d’inertie'),('insertion','left lower','(ordinaires)'),('deletion','left lower','arcs de'),('text','right top','on appelle sommets de transition'),('deletion','right top','Ainsi le'),('text','right a','les arcs de générisation'),('text','right b','les arcs de spécialisation'),('text','right c','les arcs qui ne sont'),('deletion','right c','arcs de'),('margin note','center diagonal','arcs caractéristiques qui sont les côtés'),('text','right lower','Dans les cas où il n’y a pas'),('insertion','right lower','caractéristiques'),('deletion','right lower','il'),('deletion','right lower','l’un de'),('insertion','right lower','alors'),('deletion','right lower','d’eux est un triangle'),('deletion','right bottom','arc')]
d=[('left opening','position','Underlined, abbreviated-looking word before bissectrice; ending uncertain.','medium'),('right last line','ponctuel (réduit au sommet qui','The noun/adjective before opening parenthesis is difficult; continuation awaits next scan but not supplied from it.','low'),('right lower cancellation','d’eux est un triangle','Struck phrase partly obscured.','medium'),('left colored disk','chords and black small strokes','Curve positions approximated; small black marks on lower-right chord reproduced as strokes.','medium')]
save_page(37,tex,e,d,'''If there are two exceptional specialization arcs, L is characterized as a corridor bisector; exactly two generalization arcs then complete a four-sided polygon. General transition arcs only meet in exceptional-specialization/generalization adjacency. Defines ordinary inertia arcs, then improves definition through transition vertices and characteristic polygon. Without exceptional arcs, characteristic arcs alternate inertia/transition; two inertia arcs are never adjacent. Adjacent non-inertia arcs must be exceptional-specialization/generalization. All assertions to be inventoried as research notes.''',sheet_kind='reused_typed')

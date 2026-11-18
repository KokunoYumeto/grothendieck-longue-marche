from save_page import save
text=r'''\scanpage{21}
\mspage{2 bis}
% archive foliation: 20

\uline{Thm} Soit
\diagram{\begin{tikzcd}
Y\arrow[r,"i"]\arrow[d,"g"']&X\arrow[d,"f"]\\
Y'\arrow[r,"i'"']&X'
\end{tikzcd}}
un diagramme cartésien, avec $i',f$ des cofibrations,
\inserted{(donc $i,g$ \unsure{aussi})}, \deleted{\unsure{et}} Supposons
que $\forall x'\in X'$, $f^{-1}(x')$ \uline{ou} $i'^{-1}(x')$ soit isom.
à la catégorie ponctuelle, et considérons le foncteur canonique
\diagram{\begin{tikzcd}
\displaystyle\int\left(\begin{tikzcd}[ampersand replacement=\&,cramped]
Y\arrow[r]\arrow[d]\&X\\Y'\&\deleted{\unsure{X'}}
\end{tikzcd}\right)\arrow[r]&X'.
\end{tikzcd}}
\margin{\unsure{propre aux} \uline{fibrations}}
\margin{au lieu de ponctuelle, il suffit qu'elle soit $\underline W$-asphérique}

Ce foncteur est une cofibration, à fibres les
\diagram{$\displaystyle\int\begin{tikzcd}
Y_{x'}=Y'_{x'}\times X_{x'}\arrow[r,"\mathrm{pr}_2"]\arrow[d,"\mathrm{pr}_1"]&X_{x'}\\
\deleted{\unsure{Y'_{f'}}}\,Y'_{x'}&
\end{tikzcd}$}, qui sont \inserted{isom. à des cat.} de la forme
\diagram{$\displaystyle\int\begin{tikzcd}
A\arrow[r,"{\deleted{\unsure{f}}\,\mathrm{id}_A}"]\arrow[d]&A\\e&
\end{tikzcd}$}
(ou
\diagram{$\displaystyle\int\begin{tikzcd}
A\arrow[r]\arrow[d,"\mathrm{id}_A"']&e\\A&
\end{tikzcd}$}), donc asphériques.

\margin{La catégorie est $C(A)\amalg_A(A\times\Delta^1)$.
\deleted{Il y a un \unsure{rétracte} \unsure{hom.}}
$C(A)$ en est un \unsure{rétracte} par déformation, on gagne !}

\deleted{Il suffit de voir que
\diagram{$\displaystyle\int\begin{tikzcd}A\arrow[r]&A\end{tikzcd}$}
et
\diagram{$\displaystyle\int\begin{tikzcd}A\arrow[r]&e\end{tikzcd}$}
sont $\underline W$-asphériques (par propriétés des recollements), pour le deuxième
c'est clair car il y a élément final, pour le premier \unsure{disons}.}

\margin{\uline{Lemme} Si dans
\diagram{$\displaystyle\int\left(\begin{tikzcd}[ampersand replacement=\&]
Y\arrow[r,"i"]\arrow[d,"g"']\&X\\Y'\&
\end{tikzcd}\right)$}
on a $\unsure{i}\in\underline W$, $\unsure{g}\in\underline W$
$(\unsure{i'\!\in\underline W})$.}

\uline{Corollaire}
\[
i\in\underline W\ \Longrightarrow\ i'\in\underline W
\qquad
 g\in\underline W\ \Longrightarrow\ f\in\underline W.
\]
'''
e=[('text','top','Thm Soit un diagramme cartésien'),('diagram','top','Y X Y prime X prime; i g f i prime'),('insertion','top right','donc i g aussi'),('deletion','top right','et'),('text','upper','Supposons que pour tout x prime'),('display','upper','f inverse x prime ou i prime inverse x prime'),('diagram','upper middle','integral Y to X Y prime to X prime'),('deletion','inside upper integral','X prime'),('margin note','upper left diagonal','propre aux fibrations'),('margin note','left diagonal','au lieu de ponctuelle il suffit'),('text','middle','Ce foncteur est une cofibration'),('diagram','middle','Y x prime Y prime x prime times X x prime; pr1 pr2'),('deletion','middle integral lower object','Y prime f prime'),('insertion','middle','isom. à des cat.'),('diagram','middle lower','integral A id A to A and A to e'),('deletion','middle lower arrow label','f'),('diagram','lower middle','integral A to e and id A to A'),('text','lower middle','donc asphériques'),('margin note','lower left','La catégorie est C A amalg A times Delta1'),('display','lower left','C A amalg over A A times Delta1'),('deletion','lower left','Il y a un rétracte hom.'),('margin note','lower left','C A en est un rétracte par déformation'),('deletion','lower large cancelled block','Il suffit de voir que'),('diagram','inside cancelled block upper','integral A to A'),('diagram','inside cancelled block lower','integral A to e'),('margin note','bottom diagonal','Lemme Si dans'),('diagram','bottom diagonal','integral Y to i X g to Y prime'),('display','bottom diagonal','i in W g in W i prime in W'),('text','bottom right','Corollaire'),('display','bottom right','i in W implies i prime in W; g in W implies f in W')]
save(21,text,'text',e,'Theorem 2 bis: cartesian square of cofibred maps, one of two point fibers at each target point is a point; margin weakens point to W-aspherical. Live fiber computation and cancelled proof paragraph; diagonal bottom lemma is difficult and partly unfinished. Corollary preserves W under the indicated pushout. All mathematical status awaits post-freeze work; margin wording and final formula remain doubtful.')

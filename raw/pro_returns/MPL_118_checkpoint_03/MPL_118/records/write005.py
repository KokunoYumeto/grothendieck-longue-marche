from save_page import save
save(5,r'''\scanpage{5}
% archive foliation: 4
\[
\boxed{\mathrm{Sm}\cap\mathrm{Pr}\subset S}
\]
\[
\boxed{\begin{gathered}WSC\cap\mathrm{Pr}\subset S\\ WSF\cap\mathrm{Sm}\subset S\end{gathered}}
\quad
\begin{gathered}
(\text{hence }WSC\cap\mathrm{Pr}=\inserted{\unsure{WSB\cap\deleted{\unsure{\mathrm{Pr}}}=}}(S\cap\mathrm{Pr}))\\
(\text{--- }WSF\cap\mathrm{Sm}=\unsure{S\cap\mathrm{Sm}})\\
\inserted{(WSB\cap\mathrm{Sm})}
\end{gathered}
\]
\margin{\diagram{\begin{tikzcd}[column sep=small]
S, \arrow[d,dash] & \mathrm{Pr}, \arrow[d,dash] & \mathrm{Sm} \arrow[d,dash] \\
\begin{gathered}\text{Serre map}\\\text{i.e. Hot-}\\\text{fibration}\end{gathered} & \text{proper} & \text{Smooth}
\end{tikzcd}}
$T=$ ``\unsure{univers.ly} in $W$''}

\margin{\deleted{$WSB\cap\mathrm{Sm}\unsure{\not\subset} \unsure{F}\ ?$}
\deleted{$(WSB\cap\mathrm{Pr}\unsure{\not\subset} C)$}

$WSB\neq WSF\cap WSC$ !

$WSC,WSB$ not stable under $S\cap C$ base ch.!
(And dually!) even if both are ``trivial''? $*$}

\margin{$C,\unsure{F|E}\not\subset WSF,WSC$ !
\deleted{$\unsure{C,F}$}
$\left[\begin{gathered}C\not\subset WSF\\F\not\subset WSC\end{gathered}\right]$

$C\cap WSF\not\subset S$ ?

$F\cap WSC\unsure{\not\subset}S$ ?}

\diagram{\begin{tikzcd}[column sep=small,row sep=large,
execute at end picture={\draw[dashed] (cutleft) -- (cuttop) -- (cutright);\draw[dashed] (cutlefttwo) -- (cuttoptwo) -- (cutrighttwo);}]
&&& \begin{gathered}\mathrm{def}\\B=F\cap C\end{gathered}\arrow[dl]\arrow[dr] &&& \\
&& F\cap\mathrm{Pr}\arrow[dl]\arrow[dr] & |[alias=cuttop]| {} & \mathrm{Sm}\cap C\arrow[dl]\arrow[dr] && \\
& F\cap S\arrow[ddll]\arrow[dr]\arrow[dl,no head] && \mathrm{Sm}\cap\mathrm{Pr}\arrow[dl]\arrow[dr] && S\cap C\arrow[dl]\arrow[ddr]\arrow[dr,no head] & \\
\underset{F\cap WSC}{\bullet}\arrow[d]\arrow[ddrr,gray] && \mathrm{Sm}\cap S\arrow[dl,no head]\arrow[ddr]\arrow[dddd,dotted,very thick] && S\cap\mathrm{Pr}\arrow[ddl]\arrow[dr,no head]\arrow[dddd,dotted,very thick] && \underset{WSF\cap C}{\bullet}\arrow[d]\arrow[ddll,gray] \\
|[draw,circle]| F\arrow[dr] & \underset{\mathrm{Sm}\cap WSC}{\bullet}\arrow[d] && |[alias=cuttoptwo]| {} && \underset{WSF\cap\mathrm{Pr}}{\bullet}\arrow[d] & |[draw,circle]| C\arrow[dl] \\
|[alias=cutleft]| {} & |[draw,circle]| \mathrm{Sm} && |[draw,circle]| S\arrow[d,"\unsure{\neq}"'] && |[draw,circle]| \mathrm{Pr} & |[alias=cutright]| {} \\
&&& |[draw,ellipse,dashed]| WSB\arrow[d] &&& \\
&& |[draw,ellipse,dashed]| \begin{gathered}\deleted{\unsure{\mathrm{Spr}F}}\\\inserted{WSF}\end{gathered}\arrow[ddr] & \begin{gathered}\deleted{\unsure{\mathrm{Spr}B}}\\WSF\cap WSC\end{gathered}\arrow[l]\arrow[r] & |[draw,ellipse,dashed]| \begin{gathered}\deleted{\unsure{\mathrm{Spr}C}}\\\inserted{WSC}\end{gathered}\arrow[ddl] && \\
& |[alias=cutlefttwo]| {} & \begin{gathered}(\deleted{\unsure{pre}}\text{ Serre pre-}\\\text{fibrations})\\\text{stable by}\\\text{proper b.ch.}\end{gathered} && \begin{gathered}(\deleted{\unsure{pre}}\text{ Serre}\\\text{precofibrations})\\\text{stable by}\\\text{smooth b.ch.}\end{gathered} & |[alias=cutrighttwo]| {} & \\
&&& \mathrm{Fl}(\mathrm{Cat}) &&&
\end{tikzcd}}
\margin{\unsure{str}}
\margin{stable under any base change

Squares cartesian}
\margin{\unsure{mon ch.|non ch.}

\unsure{tested by} $\Delta_1$ base ch.}

\margin{A Serre map is in $W$ iff \unsure{its} fibers are aspheric, i.e.
$S\cap W=S\cap T$
\inserted{and also iff it is univ. in $W$}}

\margin{Even if fibers are aspheric, the Serre condition cannot be tested by only taking base-changes $\Delta_1\to\unsure{Y}$ ?}

\margin{stable by intersection
\uline{except} $WSF\cap C$ and $\unsure{WCF}\cap\mathrm{Pr}$
and dually $F\cap WSC$, $\mathrm{Sm}\cap WSC$
and $WSF\cap WSC$}

\margin{$*$ i.e. find $f:X\to Y$, $g:Y'\to Y$
with $f\in W\cap WSB$ (i.e. $f$ tot. asph)
\deleted{$W$} and $g\in T\cap C$ (cofibration with trivial fibers) s.th.
$f':X'\longrightarrow Y'$ is not in $WSE$
(say $Y'$ with final element $e$ and $y'\in\mathrm{Ob}\,Y'$ s.th.
$X'_{/y'}\to X'_{/e}$ not a Weak equiv. ?}

\diagram{\begin{tikzcd}[column sep=small,row sep=large,
execute at end picture={\draw[dashed] (lowcutleft) -- (lowcuttop) -- (lowcutright);\draw[dashed] (lowcutlefttwo) -- (lowcuttoptwo) -- (lowcutrighttwo);}]
&& \unsure{\overline{W}}\cap F\cap C\arrow[dl,"\mathrm{str}"']\arrow[dr] && \\
& \unsure{\overline{W}}\cap F\cap\mathrm{Pr}\arrow[dl,"\mathrm{str}"']\arrow[dr] & |[alias=lowcuttop]| {} & W\cap\mathrm{Sm}\cap C\arrow[dl]\arrow[dr] & \\
\begin{gathered}W\cap F\cap S\\\deleted{\unsure{W}}=T\cap F\end{gathered}\arrow[dr] && W\cap\mathrm{Sm}\cap\mathrm{Pr}\arrow[dl]\arrow[dr] && \begin{gathered}W\cap S\cap C\\=T\cap C\end{gathered}\arrow[dl] \\
|[alias=lowcutleft]| {} & \begin{gathered}W\cap\mathrm{Sm}\cap S\\=T\cap\mathrm{Sm}\end{gathered}\arrow[dr] & |[alias=lowcuttoptwo]| {} & \begin{gathered}W\cap S\cap\mathrm{Pr}\\=T\cap\mathrm{Pr}\end{gathered}\arrow[dl] & |[alias=lowcutright]| {} \\
&& |[draw,ellipse,double]| \begin{gathered}W\cap S\\=T\cap S=\unsure{uW}\end{gathered}\arrow[d,"\mathrm{str}"] && \\
|[alias=lowcutlefttwo]| {} && |[draw,ellipse,dashed]| \begin{gathered}\mathrm{Tot\ As}\\=W\cap WSB\end{gathered}\arrow[dl,"\mathrm{str}"']\arrow[dr] && |[alias=lowcutrighttwo]| {} \\
& |[draw,ellipse,double]| \begin{gathered}\mathrm{As}^{\circ}\\\deleted{\unsure{\mathrm{As}}}\\=W\cap WSF\end{gathered}\arrow[dr,"\mathrm{str}"'] && |[draw,ellipse,double]| \begin{gathered}\mathrm{As}\deleted{\unsure{^{\circ}}}\\=W\cap WSC\end{gathered}\arrow[dl] & \\
& \begin{gathered}(\text{stable by}\\\text{proper b.ch.})\end{gathered} & W & \begin{gathered}(\text{stable by}\\\text{smooth b.ch.})\end{gathered} & \\
&& \begin{gathered}(\text{stable by}\\S\text{ base ch.})\end{gathered} &&
\end{tikzcd}}
\margin{Stable under any base change

Squares cartesian}
\margin{this square $\longrightarrow$
non cartesian?}
\margin{stable by intersection except $\mathrm{As}\cap\mathrm{As}^{\circ}$}
''','text',[
('display','upper left box','Sm∩Pr⊂S'),
('display','upper left second box','WSC∩Pr⊂S; WSF∩Sm⊂S'),
('text','beside second box','hence WSC∩Pr = S∩Pr; WSF∩Sm = S∩Sm'),
('insertion','above hence equation, connected by curved line','WSB∩ deleted Pr ='),
('insertion','below second hence equation','(WSB∩Sm)'),
('margin note','top right','S, Pr, Sm; Serre map i.e. Hot-fibration; proper; Smooth; T='),
('deletion','upper left, beneath boxes','WSB∩Sm; WSB∩Pr'),
('margin note','left upper middle','WSB≠WSF∩WSC! WSC,WSB not stable under S∩C base ch.!'),
('margin note','left of upper diagram','C,F⊄WSF,WSC! C⊄WSF; F⊄WSC; C∩WSF⊄S? F∩WSC⊄S?'),
('deletion','left of upper diagram, before bracketed pair','C,F'),
('diagram','upper and central main lattice','def B=F∩C; F∩Pr; Sm∩C; F∩S; Sm∩Pr; S∩C; WSB; WSF∩WSC; WSF; WSC; Fl(Cat)'),
('deletion','upper lattice, below WSB and at lower two vertices','SprB; SprF; SprC; pre; pre'),
('insertion','upper lattice, beside two revised vertices','WSF; WSC'),
('margin note','beside F∩S to F arrow','str'),
('margin note','right brace of upper diagram','stable under any base change; Squares cartesian'),
('margin note','right, two oblique strokes','mon ch.; tested by Δ1 base ch.'),
('margin note','left centre boxed note','A Serre map is in W iff its fibers are aspheric'),
('insertion','bottom of boxed Serre-map note','and also iff it is univ. in W'),
('margin note','left centre second boxed note','Even if fibers are aspheric, the Serre condition cannot be tested'),
('margin note','right below upper lattice','stable by intersection except WSF∩C and WCF∩Pr; and dually; and WSF∩WSC'),
('margin note','large lower-left starred note','i.e. find f:X→Y, g:Y′→Y with f∈W∩WSB'),
('deletion','starred note, before and g','W'),
('diagram','lower central lattice','W∩F∩C; W∩F∩Pr; W∩Sm∩C; W∩S; Tot As; As°; As; W'),
('deletion','lower lattice, equality at left and two As vertices','W; As; °'),
('margin note','right brace of lower lattice','Stable under any base change; Squares cartesian'),
('margin note','lower left oval','this square → non cartesian?'),
('margin note','lower right','stable by intersection except As∩As°')
], 'Dense working diagram with extensive overwritten class names. The partly obliterated old labels are assigned tentative Spr-readings inside deleted+unsure; these are low confidence, not secure readings. The pencil right-hand exception WCF∩Pr is retained as read, not harmonized to WSF. Two W shapes in the lower diagram carry apparent upper bars but could be corrections; marked unsure. Self-questioned points: stability even for two trivial maps; test of the Serre condition by Δ1 base change; starred search for a counterexample; non-cartesian last square. The upper/lower heavy dashed chevrons and circled vertices are reproduced as diagram decorations. The author appears to distinguish WSB from WSF∩WSC, but no mathematical conclusion is drawn during transcription.')

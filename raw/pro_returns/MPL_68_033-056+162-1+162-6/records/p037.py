import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(37,r'''
\scanpage{37}
% archive foliation: 36
II) Groupes à un paramètre formel

$K$ $\mathbf Q$-algèbre comm. unifère.

$\overline G_{aK}$ droite formelle sur $K$ $(\overline G_{aK}\subset G_{aK})$ :
\[
\overline G_a(K')=N(K')\subset K'\qquad\text{( }K'\ K\text{-alg. comm.}
\]
$1^\circ$ Soit $U$ $K$-algèbre, $\operatorname{Un}(U)$ le foncteur-groupes
\[
K'\longmapsto(U_{K'})^*\qquad\operatorname{Alg}_{/K}\longrightarrow\operatorname{Gr}
\]
On va définir les homomorphismes de groupes
\diagram{\begin{tikzcd}
\overline G_{aK}\arrow[r]\arrow[d,phantom,"\cap" description]&\operatorname{Un}(U)\\
G_{aK}\arrow[r]&\operatorname{Un}(U)
\end{tikzcd}}
Soit $x\in U$, on lui associe
\[
\bar e_x:\overline G_{aK}\longrightarrow\operatorname{Un}(U)
\]
par
\[
\bar e_x(\lambda)=\exp(\lambda x)
\]
i.e. si $\lambda\in\overline G_{aK}(K')=N(K')$, $\unsure{\bar e_x|e_x}(\lambda)=\exp(\lambda x_{K'})$ (cf. Ex. 1)

On a bien $\bar e_x(\lambda+\lambda')=\bar e_x(\lambda).\bar e_x(\lambda')$ (Th. 1, $2^\circ$)

Donc
\[
\bar e_x\in\operatorname{Hom}_{\mathrm{gr}}(\overline G_{a\unsure{K'|K}},\operatorname{Un}(U))
\]
D'où une application
\[
(*)\qquad x\longmapsto\bar e_x:\quad U\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(\overline G_{aK},\operatorname{Un}(U))
\]
Si $x\in N(U)$, alors on définit de \unsure{même}
\[
\left\{\begin{aligned}
e_x:&\quad G_{aK}\longrightarrow\operatorname{Un}(U)\\
&e_x(\lambda\deleted{\unsure{x}})=\exp(\lambda x)
\end{aligned}\right.
\]
et on a encore
\[
e_x\in\operatorname{Hom}_{\mathrm{gr}}(G_{aK},\operatorname{Un}(U))
\]
d'où
\[
(**)\qquad x\longmapsto e_x:\quad N(U)\longrightarrow\operatorname{Hom}_{\mathrm{gr}}(G_{aK},\operatorname{Un}(U))
\]
\uline{NB} a) $\bar e_x$ est la restriction de $e_x$ à $\overline G_{aK}$. b) Si $x,y$ commutent, alors $\bar e_x,\bar e_y$ (resp $e_x,e_y$) commutent, et $\bar e_{x+y}=\bar e_x.\bar e_y$ (resp. $e_{x+y}=e_x.e_y$)

\uline{Th. 2} $(*)$ et $(**)$ sont \uline{bijectives}. [NB si $U$ est comm., alors ce sont des isom. de groupes]
''',[
('text','top','II) Groupes à un paramètre formel'),
('text','upper','K Q-algèbre comm. unifère; bar G droite formelle'),
('display','upper','bar G_a(K prime)=N(K prime) subset K prime'),
('text','upper','1° Soit U K-algèbre'),
('display','upper','K prime maps to (U_Kprime)^star; Alg_/K to Gr'),
('text','upper middle','On va définir les homomorphismes de groupes'),
('diagram','upper middle','bar G_aK to Un(U), cap, G_aK to Un(U)'),
('text','middle','Soit x in U on lui associe'),
('display','middle','bar e_x: bar G_aK to Un(U)'),
('text','middle left','par'),
('display','middle','bar e_x(lambda)=exp(lambda x)'),
('text','middle','i.e. si lambda in bar G_aK(K prime)'),
('text','fold','On a bien bar e_x(lambda+lambda prime)'),
('text','below fold','Donc'),
('display','below fold','bar e_x in Hom_gr'),
('text','lower middle','Dou une application'),
('display','lower middle','(*) x maps to bar e_x'),
('text','lower middle','Si x in N(U), alors on définit de même'),
('display','lower middle','brace e_x: G_aK to Un(U); e_x(lambda)=exp'),
('deletion','argument of e_x','x (overwritten small symbol)'),
('text','lower','et on a encore'),
('display','lower','e_x in Hom_gr(G_aK,Un(U))'),
('text','lower','dou'),
('display','lower','(**) N(U) to Hom_gr'),
('text','bottom','NB a) restriction; b) commutation identities'),
('text','bottom','Th. 2 (*) et (**) sont bijectives')
],[
('additive-group symbols throughout','G, bar G','reinforced G could denote bold G; retained ordinary G with explicit bars','medium'),
('top parenthetical K prime K-alg. comm.','no closing parenthesis supplied','right edge has no securely visible closure','medium'),
('i.e. formula','bar e_x','e_x; initial symbol retraced','medium'),
('Donc Hom subscript on G','K prime','K; small stroke after K','medium'),
('de même','même','word is reduced to two horizontal strokes','low'),
('argument of e_x','deleted x after lambda','small black overwritten symbol','low')])

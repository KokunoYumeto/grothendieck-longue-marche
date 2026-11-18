from save_page import save
text=r'''\scanpage{26}
\mspage{7}
% archive foliation: 25
\margin{\deleted{\uline{\unsure{Foutaise}}}}

Dans cet argument, il a fallu \inserted{\unsure{visiblement}} utiliser un intervalle
$I$ \uline{séparant} (cf condition (iii)). Donc dans le cas $M=\widehat A$, il faut
disposer d'un intervalle $I$ \uline{séparant} dans $\widehat A$
\deleted{dans $A$} qui de plus définisse une \deleted{\unsure{théorie}}\inserted{structure}
homotopique sur $\widehat A$ \deleted{\unsure{pour}}\inserted{compatible} avec $W$
--- et pour ceci, il faut supposer que
$I\longrightarrow e$ est $\underline W_A$-asphérique
[ou du moins que \deleted{les deux extrémités}\inserted{$\delta_0$ et $\delta_1:e\longrightarrow I$}
\deleted{\unsure{aient}} \uuline{$\mathrm{univ}^{t}$}
$\Rightarrow$ image dans $W$ $\ldots$] --- donc, finalement, que
\deleted{\unsure{donc}} $A$ soit une catégorie-test \uline{locale}.
\margin{\uline{NB} \unsure{c'est inutile}, \unsure{cf ci. $h$}
\unsure{Si on regarde la catégorie $A$} \deleted{\unsure{puisque}}}
\margin{\deleted{\unsure{doit être} \unsure{une catégorie} \unsure{test}}}

On a utilisé aussi la propriété (pour \unsure{cas} $J=2$) que pour une famille de
flèches $(f_j)_{j\in J}$ dans $\widehat A$, $f_j\in\underline W_A$ pour
$\forall j\in J\ \Longrightarrow\ \coprod_j f_j\in\underline W_A$.
On est ramené à voir la $=$ chose dans $(\mathrm{Cat})$, pour $\underline W$.
Cela résulte alors de loc. 3 (condition de \unsure{localis.tion}) appliqué à
\diagram{\begin{tikzcd}
X\arrow[r]\arrow[dr]&Y\arrow[d]\\&J
\end{tikzcd}}.

\deleted{Coroll.}
'''
e=[('margin note','top right','Foutaise'),('deletion','top right','Foutaise'),('text','upper','Dans cet argument il a fallu utiliser'),('insertion','top','visiblement'),('text','upper','intervalle I séparant cf condition iii'),('text','upper middle','Donc dans le cas M A hat'),('display','upper middle','M equals A hat'),('deletion','upper middle','dans A'),('deletion','upper right','théorie'),('insertion','upper right','structure'),('text','middle','homotopique sur A hat'),('deletion','middle right','pour'),('insertion','middle right','compatible'),('text','middle','et pour ceci il faut supposer'),('display','middle','I to e W A asphérique'),('text','middle bracket','ou du moins que'),('deletion','middle','les deux extrémités'),('insertion','middle','delta0 et delta1 e to I'),('deletion','middle right','aient'),('display','middle','univ t double underlined implies image dans W dots'),('deletion','middle left','donc'),('text','middle lower','A soit une catégorie test locale'),('margin note','left vertical','NB c est inutile cf ci h'),('deletion','left vertical','puisque'),('margin note','left lower','doit être une catégorie test'),('deletion','left lower','doit être une catégorie test'),('text','lower','On a utilisé aussi la propriété'),('display','lower','family f j j in J; each in W A implies coproduct in W A'),('text','lower','On est ramené à voir la même chose dans Cat'),('text','bottom','Cela résulte alors de loc.3'),('diagram','bottom','X Y J triangle'),('deletion','bottom','Coroll.')]
save(26,text,'text',e,'Re-examines the separating-interval and local test category requirement, with top cancelled Foutaise-like word and left margin questioning necessity. Coproduct stability is then reduced to loc.3 via a triangle to discrete J. Densely slanted margin and overwritten words are among the least secure readings; no mathematical check has yet been done.')

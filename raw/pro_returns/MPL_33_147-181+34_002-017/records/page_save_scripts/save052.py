import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{52}
\mspage{16}
Dans Hot, par contre on a ceci :
Tout carré cocartésien est cartésien. Pour qu'un carré cartésien $\diagram{\begin{tikzcd}&\xi_0\arrow[dl,no head]\arrow[dr]&\\\xi_a\arrow[dr,no head]&&\xi_b\arrow[dl,no head]\\&\xi_1&\end{tikzcd}}$ soit aussi cocartésien, il f. et s. que l'on ait
\[\pi_0(\xi_1)=\mathrm{Im}\pi_0(\xi_a)\cup\mathrm{Im}\pi_0(\xi_b)\]
\margin{Complètement faux. Si p.ex. $\xi_1=e$, le diagramme \unsure{n'est-il pas} homotopiquement cartésien et cocartésien que si $\xi_a\simeq e$ \uline{ou} $\xi_b\simeq e$.}
\figure{\begin{tikzpicture}\draw (0,0)--(3,.1);\end{tikzpicture}}
Der 6 ou Der 6' entraîne donc W7. Quant à W8, il semble relever d'un principe général

``\uline{Der 8}'' \inserted{(``lemme des cinq'')} Soit un hom. de deux carrés \deleted{\unsure{co}}cartésiens de même nature, dans $\mathcal A(\Delta^1\times\Delta^1)$. Considérons les conditions
\[\diagram{\begin{tikzcd}[row sep=small,column sep=small]
&\xi_a\arrow[dr,no head]\arrow[dddd,"f_a",near start]&\\
\xi_0\arrow[ur]\arrow[dr,no head]\arrow[dddd,"f_0"']\arrow[dddd,no head,shift left=2pt]&&\xi_1\arrow[dddd,"f_1"]\\
&\xi_b\arrow[ur]\arrow[dddd,"f_b",near start]&\\
&&\\
&\eta_a\arrow[dr,no head]&\\
\eta_0\arrow[ur]\arrow[dr]&&\eta_1\\
&\eta_b\arrow[ur]&
\end{tikzcd}}\qquad\begin{array}{ll}a)&f_0\text{ est iso}\\b)&f_1\text{ est iso}\\c)&f_a\text{ et }f_b\text{ sont iso.}\end{array}\]
\deleted{Alors} Si les carrés sont hom. cartésiens, \uline{Alors} \deleted{\unsure{deux de ces trois}} $b+c\Rightarrow a$. S'ils sont hom. cocartésiens, $a+c\Rightarrow b)$. S'ils sont bicartésiens, \deleted{\unsure{cartésiens, ces propriétés}} \deleted{\unsure{le diagramme est}} donc de plus $a+b\Rightarrow c$ (``?'' \unsure{étendre le cas d'un morphisme qui apparaît} \unsure{d'une catégorie}).
\margin{Il suffit d'exiger que $a)+b)\Rightarrow c$, i.e. si $f_0,f_1$ iso, alors $f_a$ et $f_b$ iso, les autres cas \unsure{en découlent}.}
\deleted{\uline{NB} Les deux cas $a+c\Rightarrow b$, $b+c\Rightarrow a$, il suffit cartésien \unsure{dans} et \unsure{l'autre} ci-dessus. Le cas non immédiat est le cas $a+b\Rightarrow c$.}
\mspage{51}

\mspage{17}
\margin{Forme renforcée de W7 p. 9}
\uline{W7 bis} Soit $\diagram{\begin{tikzcd}&X_a\\X_0\arrow[ur,no head]\arrow[dr]&\\&X_b\end{tikzcd}}$ diagramme dans Cat, soit $\underline\Phi=\diagram{\begin{tikzcd}&a\arrow[dl]\\0&\\&b\arrow[ul]\end{tikzcd}}$ et $\mathcal X$ la catégorie fibrée sur $\underline\Phi$ définie par le diagramme. On a un diagramme commutatif dans $\mathrm{Hot}_W$ :
\[\diagram{\begin{tikzcd}&X_0\arrow[dl,"i_a"']\arrow[dr,"i_b"]&\\X_a\arrow[dr,"i'_b"']&&X_b\arrow[dl,"i'_a"]\\&\mathcal X&\end{tikzcd}}\]
\margin{\uline{NB} Autre présentation $\mathcal X$, fibré sur $\diagram{\begin{tikzcd}&a\\0\arrow[ur]\arrow[dr]&\\&b\end{tikzcd}}$. On \uline{part} sur}
(NB Dans Cat, \deleted{je présume que} les deux flèches composées sont homotopes, par un chemin de longueur 2 : elles sont homotopes tous deux, par une homotopie de long. 1, à ``l'inclusion'' $X_0\hookrightarrow\mathcal X$.)
Alors \deleted{\unsure{les}}
\[i_a\in W\Longleftrightarrow i'_a\in W\]
\[i_b\in W\Longleftrightarrow i'_b\in W\]
\margin{(traits pleins)}
\uline{W8 bis} Soit un diagramme comm. dans Cat
\[\diagram{\begin{tikzcd}[row sep=small,column sep=small]
&X_a\arrow[dr,dashed]\arrow[dddd,"f_a",near start]&\\
X_0\arrow[ur,no head]\arrow[dr,no head]\arrow[dddd,"f_0"']&&\mathcal X\arrow[dddd,"f"]\\
&X_b\arrow[ur,dashed]\arrow[dddd,"f_b",near start]&\\
&&\\
&X'_a\arrow[dr,dashed]&\\
X'_0\arrow[ur,no head]\arrow[dr,no head]&&\mathcal X'\\
&X'_b\arrow[ur,dashed]&
\end{tikzcd}}\]
\margin{Équivalent : l'énoncé dans $\mathcal X,\mathcal X'$ cofibrées sur $\underline\Psi$, avec hom \uuline{cartésien} $\mathcal X\longrightarrow\mathcal X'$.}
\margin{Cet axiome, \unsure{c'est donc} W7 bis, à l'hyp. $f$ cartésien (\unsure{W8 bis}) \unsure{est déjà}\illegible{2}\unsure{équivalent}.}
se complète par un diagramme commutatif dans $\mathrm{Hot}_W$ (déf. construction de $\mathcal X,\mathcal X'$ comme $\mathcal X=\int(\diagram{\begin{tikzcd}&X_a\\X_0\arrow[ur,no head]\arrow[dr]&\\&X_b\end{tikzcd}})$). Considérons les cond.
\[\begin{cases}a)\quad\unsure{f|f_a}\in W\\b)\quad f_0\in W\\c)\quad f_a\text{ et }f_b\in W\end{cases}\]
Alors deux de ces conditions entraînent la troisième.
'''
e=[('text','left top','16'),('text','left top','Dans Hot'),('text','left upper','Tout carré'),('diagram','left upper','xi0 xia xib xi1'),('display','left upper middle','pi0 xi1 images union'),('margin note','left upper','Complètement faux'),('drawing','left middle','divider'),('text','left middle','Der6 ouDer6prime'),('text','left lower middle','Der8'),('insertion','left lower middle','lemme des cinq'),('deletion','left lower middle','co'),('diagram','left lower','morphism of xi eta squares'),('display','left lower right','a f0 b f1 c fa fb'),('deletion','left lower right','Alors'),('text','left lower','Si les carrés'),('deletion','left lower','deux de ces trois'),('display','left lower','b+c implies a'),('display','left lower','a+c implies b'),('deletion','left lower','cartésiens ces propriétés'),('deletion','left lower','le diagramme est'),('display','left lower','a+b implies c'),('text','left lower','étendre le cas'),('margin note','left lower','Il suffit'),('deletion','left bottom','NB Les deux cas'),('text','left bottom','51'),('text','right top','17'),('margin note','right top gutter','Forme renforcée de W7 p9'),('text','right top','W7bis'),('diagram','right top','X0 Xa Xb'),('text','right upper','diagramme dansCat'),('diagram','right upper','Phi a b to0'),('text','right upper','et Xcal'),('diagram','right upper middle','i_a i_b i primes'),('margin note','right upper','NB Autre présentation'),('diagram','right upper margin','0 to a b'),('text','right middle','NB DansCat'),('deletion','right middle','je présume que'),('deletion','right middle','les'),('display','right middle','ia inW iff'),('display','right middle','ib inW iff'),('text','right lower middle','W8bis'),('margin note','right middle','traits pleins'),('diagram','right lower','morphism cube X and Xprime'),('margin note','gutter lower','Équivalent'),('margin note','right lower edge','Cet axiome'),('text','right lower','se complète'),('diagram','right lower','integral X0 Xa Xb'),('display','right bottom','three conditions'),('text','right bottom','Alors deux')]
record_page(52,s,e,notes='Dense landscape16–17. Explicit marginal rejection Complètement faux of square claim; lower Der8 discussion heavily revised and crossed. W7bis headed Forme renforcée de W7 p9. Two conditions in W8bis glyph f/f_a ambiguous. Several physically damaged edge words illegible after rotated magnification.')
build_doubts()

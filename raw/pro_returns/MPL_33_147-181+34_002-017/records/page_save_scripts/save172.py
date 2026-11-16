import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,172,r'''\scanpage{172}
\margin{\uline{à vérifier !}}
\margin{\unsure{Généraliser} aux faisceaux d'anneaux \unsure{plus généraux}.}
\uline{Théorème} Soit $X$ de type \inserted{loc} fini sur le corps $k$, $\dim X\leq n$, $A=\mathbb{Z}/N\mathbb{Z}$, $N$ premier à car. $k$, \deleted{\unsure{Alors}} \inserted{$F$} et $C$ deux $A$-\deleted{\unsure{ét.}}Modules. Supposons que $F$ soit plat $=$ $C$ : fibres injectives ($=$ plates, dans le cas particulier envisagé !). Alors

(i) Si $F$ constructible, alors $\operatorname{Ext}^i(F,C)=0$ pour $i>2n$.

(ii) Si $k$ est séparablement clos, alors \deleted{\unsure{pour tout}}
\[
\begin{aligned}
\unsure{\mathcal{E}xt^i|\operatorname{Ext}^i}(\deleted{\unsure{A}}\inserted{F},C)&=0&\text{pour }i&>2n\\
\operatorname{Ext}^i(F,C)&=0&\text{pour }i&>2n.
\end{aligned}
\]

\uline{Dém.} (i) se ramène par passage à la limite à (ii). Dans (ii), on peut supposer $k$ sép. clos, et \deleted{un argument général} il suffit de prouver le \uline{premier} alinéa. \inserted{supposer d'abord $C$ : fibres injectives.} Un argument général nous ramène à \deleted{\unsure{le}} vérifier \inserted{la formule} lorsque $F$ est \unsure{quotient} d'un \unsure{produit} de la forme $i_!(A_{X'})$, où $X'$ affine et $X'\unsure{-|\longrightarrow}X$ étale, \unsure{au} dessus d'un ouvert affine \inserted{$U$} de $X$. Car on se ramène au cas où $X=U$ est aussi affine [car on peut remplacer $X$ par $U$, $C$ par $C|U$]
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[gray] (0,0)--(0.05,1.2);\draw[gray] (0.01,1.45)--(0.08,2.5);\end{tikzpicture}}}
\margin{171}
''',[
('margin note','top','à vérifier !'),('margin note','upper left diagonal','Généraliser aux faisceaux d’anneaux plus généraux'),('text','upper','Théorème Soit X de type fini'),('insertion','above type fini','loc'),('deletion','before F et C','Alors'),('insertion','above deleted Alors','F'),('deletion','before Modules','ét.'),('text','middle','(i) Si F constructible'),('text','middle','(ii) Si k est séparablement clos'),('deletion','after alors','pour tout'),('display','middle','two Ext vanishings for i>2n'),('deletion','first Ext argument','A'),('insertion','first Ext argument','F'),('text','lower','Dém. (i) se ramène'),('deletion','proof','un argument général'),('insertion','proof between first alinéa and Un argument général','supposer d’abord C : fibres injectives'),('deletion','before vérifier','le'),('insertion','above lorsque','la formule'),('insertion','after ouvert affine','U'),('drawing','left of proof','two vertical pencil strokes'),('margin note','bottom left','171')],remarks='Whole, both halves, enlarged upper text, enlarged Ext formulas and lower proof, and rotated diagonal margin read. This is a very faint and rapidly written sheet; the connective prose and the phrase provisionally read quotient d’un produit are low confidence, not mathematical emendations. The apparent equality mark after plat is retained. The first Ext is overwritten and the alphabet is doubtful; the second is plain Ext. The arrow before X is a plain dash in the visible ink and is marked accordingly. The theorem itself is explicitly marked à vérifier !. A supplemental instruction says to suppose C has injective fibres; the relation of that insertion to the initial hypotheses deserves a research reading question.')

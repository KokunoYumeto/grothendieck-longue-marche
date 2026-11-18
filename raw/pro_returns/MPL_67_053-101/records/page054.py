import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{54}
\mspage{1}
% archive foliation: 56
\uline{\unsure{16.1.84|11.1.84}}

\uline{Chirurgie conforme}

\textcircled{A)} Surface conforme à bord. On \deleted{\unsure{peut donc}} le définit par des
cartes locales qui, \uline{au} voisinage d'un point du
bord, sont \unsure{modelées} sur \inserted{$\overline H=$} $(\Im z\geq0)\subset\mathbb C$.
Dans le cas $X$ orienté i.e. structure holomorphe, la
structure peut \deleted{se} définir par un faisceau
de $\mathbb C$-algèbres, qui sur le modèle
$\overline H$ précédent, aux points $x$ de $\delta\overline H=\mathbb R$, est \unsure{formé}
de germes de fonctions qui se \uline{prolongent} en
fonctions hol. \deleted{aux}\inserted{au} \uline{voisinage} de $x$ \uline{dans} $\mathbb C$.
À ne pas confondre avec le sous faisceau
plus grand du faisceau des fonctions
complexes continues, savoir \deleted{\unsure{celui des}}\inserted{les} fonctions
continues qui sont hol dans $\operatorname{Int}(X)$.

\uline{Théorème 1} La structure conforme de $X$ (surface
conforme à bord) est connue quand on
la connaît dans $\operatorname{Int}(X)$, (ce qui suffit à
déterminer le faisceau des fonctions \inserted{complexes} continues
qui sont conformes dans $\operatorname{Int}(X)$).

Il suffit de voir que cela permet de
reconstituer les \uline{cartes} conformes des voisinages
des points du bord. Je dis que ces cartes
"""
save(54,tex,[('text','top left','16.1.84'),('text','heading','Chirurgie conforme'),('text','upper body','A) Surface conforme à bord'),('deletion','line 1','peut donc'),('insertion','line 3','H-bar ='),('deletion','line 5','se'),('deletion','line 9','aux'),('insertion','line 9','au'),('text','middle','À ne pas confondre'),('deletion','line 12','celui des'),('insertion','line 12','les'),('text','lower half','Théorème 1 La structure conforme'),('insertion','theorem line 4','complexes'),('text','bottom','Il suffit de voir')],
 doubts=[('date','16.1.84','11.1.84; day has two angular strokes','medium'),('line 1 deletion','peut donc','crossing obscures the second word','low'),('lines 3, 7','modelées; formé','endings compressed','medium')],
 notations=[('Boundary sign',r'\delta\overline H','Scan 54, same delta form as scan 53'),('Closed upper half-plane',r'\overline H','Scan 54, bar present'),('Imaginary part',r'\Im z','Scan 54'),('Circled section letter',r'\textcircled{A)}','Scan 54')],
 abbreviations=[('hol.','holomorphe(s)'),('Int','intérieur')],
 leads=['Theorem 1: bordered conformal structure is determined by the interior conformal structure on the fixed topological bordered surface; proof continues on scan 55.','Title Chirurgie conforme, own page 1, dated 16.1.84 (day uncertain), scan 54.','Distinction between germs extending holomorphically across the boundary and continuous functions holomorphic only in the interior.'])

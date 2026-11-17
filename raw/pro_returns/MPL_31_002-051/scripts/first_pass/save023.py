import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{23}
\uline{Corollaire} $A$ anneau local \deleted{hensélien} noethérien
intègre, corps des fractions $K$, corps résiduel $k$.
Alors pour tt premier $r$, on a
\[
\mathrm{cd}_r(K)\geq\mathrm{cd}_r(k)+\dim A
\]
\deleted{[avec \uline{égalité} dans le cas $A$ hensélien \unsure{?}]}
\deleted{\inserted{\figure{\begin{tikzpicture}[baseline=(n.base)]\node[draw,ellipse,align=left,inner sep=3pt] (n) {et $A$ \unsure{Univ.} japonais\\\unsure{univ. caténaire}};\end{tikzpicture}}}}
\margin{\deleted{\unsure{à le}}}

sauf exception possible dans les cas suivants:

a) $r$ est la caractéristique de $K$\inserted{(égale caractéristique $>0$)}

b) $r=2$, \deleted{$A$ un anneau de \unsure{dim $1$}, $r=2$, Il existe}
\deleted{$A$ ``d'inégales caractéristiques'', \unsure{que} la caractéristique
résiduelle est $2$, \unsure{$r=$} un idéal premier $\mathfrak p\subset A$, \unsure{non nul}, avec $A/\mathfrak p$ de dim $1$.}
$\exists\ x\in\operatorname{Spec}(A)$ tel que $\kappa(x)$
soit ordonnable, et $\mathrm{cd}_2\kappa(x)(\sqrt{-1})$ soit fini
(corps réel \unsure{coulant|courant}).
\margin{\uline{Ex} $A=\mathbb R[x,y]/(x^2+y^2)$ \uline{\unsure{localisé}}}

\uline{NB.} Si $A$ est \uline{caténaire} et \uline{univ. japonais},
(ce que garantit le fait que les \unsure{lieux normaux}
des sous-schémas de $A$ sont ouverts), alors
\deleted{il suffit} on peut préciser\inserted{dans le cas b)}, \deleted{\unsure{à quel}} l'exception
possible par: $k$ lui-même ``corps réel \unsure{coulant|courant}''.
Enfin, lorsque $A$ est \uline{régulier},
cette exception elle-même est inoffensive, i.e.
on a l'inégalité annoncée, (pourvu qu'on ne
soit dans le cas a)].
\margin{cette restriction est-elle \unsure{inutile} ???}
\margin{22}
'''
e=[('text','top','Corollaire A anneau local'),('deletion','top line 1','hensélien'),('text','top lines 2–3','intègre corps des fractions K'),('display','upper','cd_r(K) ≥ cd_r(k)+dim A'),('deletion','upper below display','avec égalité dans le cas A hensélien'),('insertion','upper right circled','et A Univ. japonais univ. caténaire'),('drawing','upper right','ellipse around cancelled insertion'),('deletion','upper right','et A Univ. japonais univ. caténaire'),('margin note','below upper-right ellipse','à le'),('text','upper middle','sauf exception possible'),('text','middle a','r est la caractéristique de K'),('insertion','above a line end','égale caractéristique >0'),('text','middle b','r=2'),('deletion','middle above b','A un anneau de dim 1 r=2 Il existe'),('deletion','middle large cancelled block','A d’inégales caractéristiques'),('text','middle after cancellation','∃ x∈Spec(A) tel que κ(x)'),('margin note','left slant','Ex A=R[x,y]/(x²+y²) localisé'),('text','lower','NB. Si A est caténaire et univ. japonais'),('text','lower parenthesis','ce que garantit le fait que les lieux normaux'),('deletion','lower','il suffit'),('insertion','lower right','dans le cas b)'),('deletion','lower after préciser','à quel'),('text','lower','on peut préciser l’exception possible'),('margin note','left lower slant','cette restriction est-elle inutile ???'),('text','bottom','Enfin lorsque A est régulier'),('margin note','bottom left','22')]
save(23,s,e,observations='Whole page and both supplied halves viewed; cancellation, NB, and oblique marginal example/question enlarged repeatedly. The deleted mixed-characteristic formulation has heavily overwritten words, retained with doubts. The repeated adjective after corps réel is read coulant, alternative courant; no mathematical replacement used. Tiny strokes beneath the upper ellipse are tentatively retained as à le. The marginal restriction question is preserved independently of the claim.')

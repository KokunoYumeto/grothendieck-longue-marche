import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,167,r'''\scanpage{167}
Validité des théorèmes de dualité

1) \uline{Dualité globale}
\[
\operatorname{Hom}(F_\bullet,\mathrm{R}^{!}f(G^{\bullet}))\xleftarrow{\sim}\operatorname{Hom}(\mathrm{R}_{!}f(F_\bullet),G^{\bullet})
\]
$f:(X,A_X)\unsure{\text{---}|\longrightarrow}(Y,A_Y)$ morphisme \uline{compactifiable} et \uline{\unsure{lissifiable}} de préschémas, annelés par $A_X$ et $A_Y$, \deleted{\unsure{des}} faisceaux d'anneaux \deleted{de \uline{torsion}} tels que pour tt pt géom. $\bar{y}$ de $Y$, $\exists n_{\bar{y}}\geq1$ \unsure{que} $n_{\bar{y}}A_{Y,\bar{y}}=\deleted{\text{est un anneau}}0$ $n_{\bar{y}}$ premier à $\operatorname{car}k(\bar{y})$.

2) \uline{Dualité locale}
\[
F_\bullet\simeq\underline{D}_X\underline{D}_X(F_\bullet)\quad\text{isom,}\quad\underline{D}_X(F_\bullet)\text{ à ch. constructible,}
\]
$X$ préschéma \deleted{\unsure{loc.}} noeth. \uline{régulier} annelé par $A_X$ faisceau d'anneaux loc. ct à fibres \deleted{\unsure{noethériennes}} \unsure{qui sont} des anneaux de torsion noethériens, premiers aux car. résiduelles

$R_X^{\bullet}$ un \inserted{complexe de} faisceaux de $A_X$-Modules loc. const., et dualisant \inserted{sur les} fibres \deleted{géométriques}
\[
\underline{D}_X(F_\bullet)=\mathrm{R}\mathcal{H}om(F_\bullet,\unsure{R_X|A_X})
\]
\[
F_\bullet\in\operatorname{Ob}D^b(X)
\]
\margin{+ résolution et pureté sur $X$ -------}
\margin{166}
''',[
('text','heading','Validité des théorèmes de dualité'),('text','upper heading','1) Dualité globale'),('display','upper','Hom(F,R!f G) left isomorphism Hom(R_!f F,G)'),('text','upper middle','f:(X,A_X) to (Y,A_Y)'),('deletion','upper middle','des'),('deletion','upper middle','de torsion'),('deletion','middle','est un anneau'),('text','lower heading','2) Dualité locale'),('display','lower middle','F isomorphic D_X D_X(F)'),('text','lower','X préschéma noeth. régulier'),('deletion','lower','loc.'),('deletion','lower','noethériennes'),('text','lower','R_X a complex of sheaves'),('insertion','lower','complexe de'),('insertion','lower','sur les'),('deletion','lower','géométriques'),('display','bottom','D_X(F)=RHom(F,R_X)'),('display','bottom','F in Ob D^b(X)'),('margin note','bottom right framed','+ résolution et pureté sur X'),('margin note','bottom left','166')],remarks='Whole, halves and enlarged hypotheses/bottom examined. The global functors are written R^! f and R_! f, not modernized to Rf^! etc. The hypothesis following compactifiable appears lissifiable and remains uncertain. The local duality coefficient in the definition is overwritten and retained as an explicit R_X/A_X alternative. The margin adds resolution and purity on X. Blue underlying text is show-through from the reverse and not an additional live block.')

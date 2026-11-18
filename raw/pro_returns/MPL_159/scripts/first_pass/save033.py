import sys
sys.path.insert(0,'MPL_159/scripts')
from record_page import commit
commit(33,r'''\scanpage{33}
$X/S$ schéma relatif

$\mathcal P$: $\mathcal O_X$-Algèbre augmentée, sép. complète pour la top. $J$-adique ($J$ idéal d'augmentation)
\inserted{$J/J^2=\Omega$ inv.}
\[
C:\mathcal P\longrightarrow\mathcal P\widehat\otimes\Omega^1_{X/S}
\]
connexion \inserted{d'Algèbre} (ne \unsure{respectant} pas néc. l'augmentation)
\[
\begin{cases}
C(fg)=fC(g)+gC(f)& f,g\text{ sections de }\mathcal P\\
C(\lambda.1)=1\otimes d\lambda&\lambda\text{ section de }\mathcal O_X.
\end{cases}
\]
\deleted{\unsure{Comment peut-on connaître $C$}}

\uline{N.B.} Localt (sur des ouverts affines) \deleted{On a}
\deleted{\unsure{pour}} iso $\mathcal P\simeq\widehat{\operatorname{Sym}}(\Omega)$ (\unsure{compatibles aux augm.}) et $C$ connu quand on connaît
$C|\Omega$, qui est un hom. \uline{additif}
\[
\Omega\longrightarrow\widehat{\operatorname{Sym}}(\Omega)\widehat\otimes\Omega^1_{X/S}
=\prod_{i\geq0}\underbrace{\operatorname{Sym}^i(\Omega)}_{\Omega^{\otimes i}}\otimes\Omega^1_{X/S}
\qquad C_\Omega=(\unsure{\varpi_i|\bar\omega_i})
\]
où les $\unsure{\varpi_i|\bar\omega_i}$ pour $i\neq1$ sont \uline{linéaires}, et
$\unsure{\varpi_1|\bar\omega_1}$ est une connexion de modules --- les $\unsure{\varpi_i|\bar\omega_i}$ par ailleurs quelc. On interprète
\[
\begin{cases}
\unsure{\varpi_i|\bar\omega_i}\in\deleted{\unsure{\Gamma\operatorname{Sym}^i}}\Gamma\,\Omega^{\otimes(i-1)}\otimes\Omega^1_{X/S}&(i\neq1)\\
\unsure{\varpi_1|\bar\omega_1}\text{ une connexion sur }\Omega.
\end{cases}
\]
On voit sur ceci que $C$ \unsure{satisfait tjrs à}
\[C(J^i)\subset J^{i-1}\widehat\otimes\Omega^1_{X/S}\]
donc $C$ induit un hom. $(i\geq1)$
\[
\operatorname{gr}^i(\mathcal P)=J^i/J^{i+1}\simeq\Omega^i
\xrightarrow{\deleted{\unsure{C}}\inserted{\widetilde C}}
\unsure{\operatorname{gr}^{i-1}}(\mathcal P\widehat\otimes\Omega^1_{X/S})
\quad\begin{matrix}\simeq\\\Omega^{i-1}\otimes\Omega^1_{X/S}\end{matrix}
\]
qui est tjrs \inserted{$\mathcal O_S$-}\uline{linéaire}, et \unsure{est}
$\operatorname{Sym}(\Omega)$-linéaire, donné par
\[\widetilde C(\omega_i)=\omega_i\otimes\unsure{\varpi_0|\bar\omega_0}.\]
% archive foliation: 32
''',[
 ('text','top','X/S schéma relatif'),('text','top','P O_X-algèbre augmentée sép complète'),('insertion','under topology','J/J^2=Omega inv'),
 ('display','upper third','C:P to P completed tensor Omega^1'),('text','right of map','connexion ne respectant pas néc augmentation'),('insertion','above connexion','d Algèbre'),
 ('display','upper middle','Leibniz identity and C(lambda.1)'),('deletion','middle','Comment peut-on connaître C'),('text','middle','N.B. Localt sur des ouverts affines'),
 ('deletion','middle line end','On a'),('deletion','middle next line start','pour'),('text','middle','iso P=completed Sym Omega and C restricted to Omega'),
 ('display','middle lower','Omega to completed Sym tensor differentials product'),('display','under product','C_Omega=(varpi_i)'),('text','lower middle','varpi_i for i not 1 linear; varpi_1 connexion'),
 ('display','lower middle','coefficient sections and connection'),('deletion','coefficient display','Gamma Sym^i'),('text','lower quarter','On voit sur ceci'),('display','lower quarter','C(J^i) subset J^{i-1} tensor Omega^1'),
 ('text','lower quarter','donc C induit un hom'),('display','bottom','gr^i P to gr^{i-1} completed tensor'),('deletion','arrow label','C'),('insertion','arrow label','tilde C'),
 ('text','bottom','qui est tjrs linéaire et Sym(Omega)-linéaire'),('insertion','above linéaire','O_S'),('display','last line','tilde C(omega_i)=omega_i tensor varpi_0')
],observations='Connection on a complete augmented rank-one algebra, coefficient decomposition, associated graded construction. The last formula and claimed Sym(Omega)-linearity have been transcribed as written, including missing-looking factors; they have not been corrected by mathematical expectation. Coefficient glyph remains a marked reading question.')

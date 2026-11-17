import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{69}
% archive foliation: 68
hom compatibles aux op. $\tfrac12$-\unsure{cos.} (pour $i,j$ fixés) et les op. diff (pour $i,j$ variables)

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
(C^i\otimes_B C^j)\otimes\unsure{C_{ij}^{*\bullet}|C_{ij}^*} \arrow[d] & (C^i\otimes_B C^j)\otimes\unsure{C_{i+1,j}^{*}} \arrow[l,"{\unsure{d^{1,0}_{i+1,j}|d^{i,0}_{i+1,j}}}"'] \arrow[d,"{d^i\otimes-\otimes-}"]\\
\begin{gathered}\deleted{\unsure{(C^i\otimes_B C^j)\otimes C_{ij}^*}}\\\inserted{C^*}\end{gathered}
& \begin{gathered}\deleted{\unsure{(C^{i+1}\otimes_B C^j)\otimes C_{i+1,j}^*}}\\(C^{i+1}\otimes_B C^j)\otimes\unsure{C_{i+1,j}^{*}}\end{gathered} \arrow[l,"{\unsure{u|d}}"]
\end{tikzcd}}

Plus des données de compatibilité aux unités, assoc, comm. (\unsure{Ce dernier|La dernière} s'explicite de façon particulièrement directe).

\uuline{Remarque} $K$ n'a pas d'unité pour $*$! donc \deleted{\unsure{il}} on ne peut exprimer directement, en restant dans $K$, une compatibilité avec les unités! Comment s'en tirer? Si on passe à $P_0$ ou $Q=P_1$, \deleted{\unsure{on pourrait imposer le $\Sigma$ de suites exactes}} on trouve que les foncteurs $k$-additifs de $Q$ (resp. $P_0$) dans $B$ qui sont $\Sigma$-exacts à gauche (i.e. transforment des \inserted{$\Sigma$-}suites exactes courtes
\[
\unsure{0}{-}A'{-}A{-}A''{-}0
\]
en suites exactes
\[
\unsure{0}{-}F(A'){-}F(A){-}F(A'')
\]
) \deleted{avec $F(A')\unsure{\longrightarrow|{-}}F(A)$ un $\Sigma$-mono}, correspondent par $F\longmapsto F(C^\bullet)$ aux complexes de coch dans $B$ tels que $\forall i$ \unsure{l'hom}'''
e=[('text','top','hom compatibles aux op. 1/2-cos.'),('diagram','upper third','differential compatibility for Ci⊗B Cj⊗Cij*'),('deletion','diagram lower left','(Ci⊗B Cj)⊗Cij*'),('insertion','diagram lower left','C*'),('deletion','diagram lower right','(Ci+1⊗B Cj)⊗Ci+1,j*'),('text','middle','Plus des données de compatibilité'),('text','middle/lower','Remarque K n’a pas d’unité pour *!'),('deletion','lower middle','il'),('text','lower','Comment s’en tirer?'),('deletion','lower','on pourrait imposer le Σ de suites exactes'),('text','lower','on trouve que les foncteurs k-additifs'),('insertion','lower','Σ-suites'),('display','bottom','0–A′–A–A″–0'),('display','bottom','0–F(A′)–F(A)–F(A″)'),('deletion','bottom','avec F(A′)→F(A) un Σ-mono'),('text','bottom','correspondent par F↦F(Cbullet)')]
save(69,text,e)

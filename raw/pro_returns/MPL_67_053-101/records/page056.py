import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{56}
\mspage{2}
% archive foliation: 58
ment en série qui commence par
\[
a_nz^n\qquad n>0,\ a_n\ne0\qquad(\text{OPS }x=0)
\]
on voit tout de suite que l'on doit avoir
$n=1$ ---

\margin{Notes : \uline{indétermination} \uline{\unsure{finie}} d'une carte loc.
au bord : modulo chgt. de coordonnées par un \unsure{germe}
de fct. analytique \uuline{\unsure{réelle|nulle}}.}

\noindent$\bigl[$\uline{Thm 2} Équiv. de la cat. des surfaces conformes
à bord \inserted{compactes}, avec celle des courbes alg. propres
lisses sur $\mathbb R$. $\bigr]$

\margin{\uline{NB} À partir d'ici $H$ désigne le demi-plan \uline{fermé}
$\{\deleted{\unsure{\mathbb R}}z\in\mathbb C\mid\Im z\geq0\}$.}

\textcircled{B)} Découpe d'une surface conforme à bord,
suivant un 1-complexe top. $K\subset X$,
satisfaisant des hypothèses de régularité
convenables (rectifiabilité suffit ?).

\uline{Théorème 3} La découpe $\widetilde X$, muni de \deleted{la}
\deleted{structure}\inserted{faisceau} des fonctions \inserted{complexes} continues conformes
dans $\operatorname{Int}(\widetilde X)$ $(\simeq X\setminus K)$, ``est'' une surface
conforme à bord.

\margin{C'est un th. du type ``uniformisation \uline{à bord}''.}

Cela revient à vérifier \deleted{donc} que \inserted{pour} tout
point $\unsure{\widetilde x|\overline x}$ de $\delta\widetilde X$, il existe un voisinage \inserted{ouvert} $U$ de $x$,
et un \deleted{\unsure{isom}}\inserted{homéo} de $U$ avec $H\cap\mathring D$ (où
$D=\{z\in\mathbb C\mid |z|\leq1\}$ est le disque
unité de $\mathbb C$). Cela revient

\margin{\unsure{renv. mt}\ \unsure{dans a)} Cor. au théor.}

\figure{\begin{tikzpicture}[scale=.7]
\draw (-1.7,0) .. controls (-1.6,1.15) and (-.6,1.65) .. (.35,1.4)
.. controls (1.05,1.2) and (1.4,.65) .. (1.5,0);
\draw (-1.75,0)--(1.5,0);
\fill (-.15,0) circle (2.3pt);
\fill (1.5,0) circle (1.8pt);
\end{tikzpicture}}

à deux choses, suivant que $x$ correspond :
"""
save(56,tex,[('text','top','ment en série qui commence par'),('display','top','a_n z^n; n>0; a_n≠0; OPS x=0'),('text','upper','on voit tout de suite; n=1'),('margin note','upper left diagonal','Notes: indétermination finie'),('text','upper middle bracket','Thm 2 Équiv. de la cat.'),('insertion','Thm 2','compactes'),('margin note','middle left','NB À partir d’ici H désigne'),('deletion','within marginal set','R'),('text','middle','B) Découpe d’une surface conforme'),('text','lower middle','Théorème 3 La découpe'),('deletion','Théorème 3','la; structure'),('insertion','Théorème 3','faisceau; complexes'),('margin note','left beside theorem','th. du type uniformisation à bord'),('text','lower','Cela revient à vérifier'),('deletion','lower first line','donc'),('insertion','lower first line','pour'),('insertion','lower second line','ouvert'),('deletion','lower third line','isom'),('insertion','lower third line','homéo'),('margin note','lower left','renv. mt dans a) Cor. au théor.'),('drawing','bottom left','semidisc; centre dot; right endpoint'),('text','bottom line','à deux choses, suivant que x correspond')],
 doubts=[('top diagonal note','indétermination finie; germe; réelle','small oblique handwriting, final word possibly nulle','low'),('theorem 3','muni de [la deleted] faisceau','grammar preserved; revision may be incomplete','medium'),('lower margin','renv. mt dans a)','abbreviations uncertain','low')],
 notations=[('H after NB',r'H=\{z\in\mathbb C\mid\Im z\geq0\}','Scan 56 explicitly changes H to closed half-plane'),('Cut surface',r'\widetilde X','Scan 56'),('Open disc',r'\mathring D','Scan 56; small ring above D')],
 abbreviations=[('OPS','on peut supposer'),('Thm','théorème'),('Équiv.','équivalence'),('cat.','catégorie'),('alg.','algébriques'),('top.','topologique'),('loc.','locale'),('chgt.','changement'),('fct.','fonction'),('homéo','homéomorphisme'),('Cor.','corollaire')],
 leads=['Thm 2 asserts, in brackets and without proof here, an equivalence between compact bordered conformal surfaces and smooth proper real algebraic curves. Need precise objects, boundaryless cases, and morphisms.','Self-flagged: rectifiabilité suffit ? for cutting along a topological 1-complex.','Théorème 3: conformal structure on the cut surface; marginal identification as uniformisation à bord.','NB explicitly changes H from the earlier open-half-plane convention to the closed half-plane; do not normalize this away.'])

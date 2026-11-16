import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(34,3,r'''\cotefile{34}
\scanpage{3}
\mspage{1}
\uline{Exposé I}\qquad\deleted{\uline{Action du groupe de monodromie :}}
\uline{Généralités, \inserted{le} th. de monodromie par voie arithmétique.}

0. \uline{Introduction}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,1)..controls(1.2,1.1) and(1.1,0)..(2.2,0)--(12,0.15);\end{tikzpicture}}

0.1. \unsure{Notations}. $S=\operatorname{Spec}V$ un trait, $s$ pt fermé, $\eta$ point générique
\[
\mathfrak m=\pi V\inserted{\text{ ``}V\text{''}},\quad k=k(s)\inserted{\text{ ``}V/\mathfrak m\text{''}},\quad K=k(\eta);\qquad p=\text{exp. car. de }k(s).
\]
Le plus souvent, on supposera $V$ hensélien, et \unsure{$S$|même} strictement \unsure{locale|local} i.e. $k$ sép. clos;

\deleted{\unsure{$K$}} $\bar K$ une clôture séparable de $K$, $\bar\eta=\operatorname{Spec}\bar K$;
\[
\pi=\operatorname{Gal}(\bar K/K).
\]
$\ell$ nombre premier. \deleted{Sauf mention du contraire} \deleted{Dans la plus grande partie \unsure{voir}} \inserted{\unsure{Pour toute la première partie du séminaire}, on supposera}
\deleted{L'hyp. de}
\[
\ell\neq\operatorname{car}k
\]

0.2. L'objet du séminaire est l'étude de certaines représentations $\ell$-adiques de $\pi$, provenant de diverses situations géométriques. Une repr. $\ell$-adique de $\pi$ est un \deleted{\unsure{module}} hom. continu
\[
(*)\qquad\pi\longrightarrow\operatorname{Aut}_{\mathbb Z_\ell}(E),
\]
où $E$ est un module de t.f. sur $\mathbb Z_\ell$. On pourra aussi regarder
\[
\pi\longrightarrow\operatorname{Aut}_{\mathbb Q_\ell}(E)
\]
$E$ module de d.f. sur $\mathbb Q_\ell$.

\uline{Exemple} 0.3. $X_K$ schéma algébrique sur $K$, \inserted{$i$ entier.} On suppose que $H^i(X_{\bar K},\mathbb Z/\ell\mathbb Z)$ est un groupe fini, de sorte que
\[
E=H^i(X_{\bar K},\mathbb Z_\ell)\overset{\mathrm{dfn}}=\underset{\nu}{\uline{\lim}}H^i(X_{\bar K},\mathbb Z/\ell^\nu\mathbb Z)
\]
est un module de t.f. sur $\mathbb Z_\ell$; \deleted{Cette hyp. est} \deleted{\unsure{est}} vérifiée dans les trois cas suivants :

a) On dispose de résolution des sing. \inserted{sous forme de Hironaka (\quad)} des schémas alg. de dim $\leq\dim X$ sur $\bar K$, -- p.ex. $K$ de car. nulle

b) $X$ propre sur $K$.

c) $X$ lisse sur $K$.
\margin{2}
''',[
('text','top','Exposé I'),('text','top right','1'),('deletion','heading','Action du groupe de monodromie'),('text','heading revised','Généralités, th. de monodromie par voie arithmétique'),('insertion','heading','le'),('text','upper left','0. Introduction'),('drawing','under heading','curved horizontal divider'),('text','upper','0.1. Notations S=Spec V'),('display','upper','m=pi V, k=k(s), K=k(eta), p exp car'),('insertion','below m and k definitions','V and V/m in quotation marks'),('text','upper','Le plus souvent, on supposera'),('deletion','before bar K','K'),('text','upper middle','bar K une clôture séparable'),('display','upper middle','pi=Gal(bar K/K)'),('text','middle','ell nombre premier'),('deletion','middle','Sauf mention du contraire'),('deletion','middle','Dans la plus grande partie voir'),('insertion','middle','Pour toute la première partie du séminaire, on supposera'),('deletion','left middle','L’hyp. de'),('display','middle','ell not equal car k'),('text','middle','0.2. L’objet du séminaire'),('deletion','before hom. continu','module'),('display','middle lower','(*) pi to Aut_Zell(E)'),('text','middle lower','où E est un module de t.f.'),('display','middle lower','pi to Aut_Qell(E)'),('text','middle lower','E module de d.f.'),('text','lower','Exemple 0.3 X_K'),('insertion','after sur K','i entier'),('display','lower','E=H^i and inverse limit expression'),('text','lower','est un module de t.f.; vérifiée'),('deletion','lower','Cette hyp. est'),('deletion','start of vérifiée line','est'),('text','bottom','a) On dispose de résolution des sing.'),('insertion','after sing.','sous forme de Hironaka ( )'),('text','bottom','b) X propre'),('text','bottom','c) X lisse'),('margin note','bottom left','2')],remarks='Whole, both halves and enlarged heading, notation/cancellations and final examples read. First supplied cote34 image is scan003, own p1, archival2. The exposition title is revised in the manuscript. The long replacement preceding ell≠car k is low confidence and must not be treated as established prose. A quotient annotation V/m and a quoted V are interlinear; their exact attachment is somewhat uncertain. The limit has an underlined lim with no unmistakable arrowhead; retained as underlined lim, not silently normalized. The proof-level hypotheses distinguishing resolution, properness and smoothness are visible; no reference has been filled into the empty Hironaka parentheses.')

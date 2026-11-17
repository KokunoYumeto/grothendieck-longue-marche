from save_page import save_page
save_page(90,r'''\scanpage{90}
\mspage{18}
% archive foliation: 89
\uuline{Dictionnaire}\qquad Fonctions $L$ --- \unsure{Cohomologie} à
\hfill action galoisienne.

Soit $k$ un \deleted{corps} anneau

\deleted{$\unsure{\mathcal A|\mathbf N}$ la catégorie}
\deleted{$\operatorname{Mod}(\mathbf Z)$ la catégorie}
$C$ la catégorie des modules de longueur
finie sur $k[t]=$ \deleted{vectoriels}\inserted{modules} $V$ \inserted{proj.}
de \deleted{dim}\inserted{rang} finie sur
$k$ munis d'un endomorphisme $f=$
$k[\unsure{\mathbf N|\mathbf Z}]$-modules, de \deleted{\unsure{rang}}\inserted{projectifs} finie sur $\unsure{\forall k|k}$.

Cette catégorie donne lieu à un faux-anneau,
noté $R^\bullet(\unsure{\mathbf N|\mathbf Z};k)$, qui est aussi, \inserted{si $k$ est un corps,}
le \deleted{\unsure{faux-anneau}} \inserted{groupe}
libre engendré par les classes des $k[\unsure{\mathbf N|\mathbf Z}]$-
modules simples, \inserted{finis sur $k$} or on connaît les $k[t]$-modules
simples, ce sont les polynômes \inserted{unitaires} irréductibles
$P\in k[t]$, en associant à $P$ le module
$k[t]/Pk[t]$. À tout tel $P$, \inserted{est} associé \unsure{à}
un $(V,f)$, dont le polynôme car. est
précisément $P$,
\margin{$k$ un corps ou non}
\[
P(t)=\det(t\,\mathrm{id}-f)
\]
[vrai pour tt $P$, irréd. ou non !]. Il nous sera
plus commode de remplacer $P(t)$ par
\[
Q(t)=t^dP\left(\frac1t\right)=\det(1-tf)
\]
qui est un polynôme quelconque à coeff. cst égal $1$.
''',[
('top-left','text','Circled author page number 18'),
('top','title','Dictionnaire; Fonctions L — Cohomologie à action galoisienne'),
('upper','text','Soit k un corps [deleted] anneau'),
('upper','deletion','la catégorie; Mod(Z) la catégorie'),
('upper-middle','text','C la catégorie des modules de longueur finie sur k[t]'),
('upper-middle','text','modules V proj. de rang fini munis d’un endomorphisme f'),
('middle','text','Cette catégorie donne lieu à un faux-anneau'),
('middle','formula','R bullet (N/Z;k)'),
('middle','text','groupe libre engendré par les classes des k[N/Z]-modules simples'),
('lower-middle','text','polynômes unitaires irréductibles P dans k[t]'),
('lower-middle','formula','k[t]/Pk[t]; (V,f)'),
('lower-left margin','margin note','k un corps ou non'),
('lower','formula','P(t)=det(t id-f)'),
('lower','text','vrai pour tt P, irréd. ou non !'),
('bottom','formula','Q(t)=t^d P(1/t)=det(1-tf)'),
('bottom','text','polynôme quelconque à coeff. cst égal 1')
],remarks='Whole and halves plus title, rewritten definition, ring notation and marginal qualification enlarged. Heavily overwritten N/Z ring argument remains uncertain pending recurrence check. Faux-anneau retained as written.')

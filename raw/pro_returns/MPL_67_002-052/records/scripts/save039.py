import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(39,r'''\mspage{13}
% archive foliation: 41
[NB \deleted{\unsure{On}} pense notamment au cas où $X$ est associé à une \uline{carte}, et $H$ est le groupe des autom. de cette carte, qui est fini --- la condition $X^H=\varnothing$ signifie aussi qu'il n'y a pas de facette de la carte fixe par $H$.]

Dans tous les cas où $Q_X$ est définie, $Q_X$ est hyperbolique (i.e. : courbure $<0$) ssi $X$ est hyperbolique, et alors $Q_X$ est de courbure \inserted{constante} égale à $-1$. D'autre part $Q_X$ est \uline{plate} \deleted{dans les cas} (ou encore, de courbure nulle) ssi $\widetilde X\simeq\mathbb C$ [y inclus le cas a) ci-dessus, où on a encore une $Q_X$ mod cte]. Le cas restant est celui du plan projectif réel, conforme, \deleted{qui est} \deleted{dans} lequel $Q_X$ est une métrique homogène, de courbure cte \deleted{égale à} et $>0$.

Donc chaque fois que $Q_X$ est définie, ou définie mod cte, il est à courbure constante, \deleted{et c'est} Il en est encore de $=$ des $Q_{X,H}$ quand $X\simeq\mathbb P^1_{\mathbb C}$ et $H\subset\mathrm{Aut}_{\mathrm{conf}}X$ est cpt et tq que $X^H=\varnothing$, \unsure{métriques} \unsure{automatiquement} sph. euclidiennes, donc de courbure constante $>0$.

\margin{\uline{NB} Pour tte $X$ 0-connexe conforme on \deleted{\unsure{a}} a dans l'ensemble \deleted{des \unsure{métriques}} $\mathrm{Riem}(X)$ des métr. riemanniennes comp. avec la str. conforme une orbite canonique sous $\mathrm{Aut}_{\mathrm{conf}}(X)$, qui est réduite à 1 pt dans tous les cas, sauf les cas a) et b) de la p. 12, où dans le cas a), on trouve une demi-droite dans $\mathrm{Riem}(X)$, et dans le cas b), une variété de dim 3 (\deleted{\unsure{qui}} telles \deleted{\unsure{que}} que $Q,Q'\in R(X)$, $Q\ne Q'$ implique $Q'$ et $Q$ \uline{non} prop). Notion des métriques riemanniennes distinguées (a un sens aussi dans le cas \unsure{disconnexe}).}
''',[
('text','top bracket','NB ... X ... carte; H ... autom.; X^H=∅'),
('deletion','top bracket','On'),
('text','middle','Dans tous les cas où Q_X est définie'),
('insertion','middle','constante'),
('deletion','middle','dans les cas'),
('deletion','lower middle','qui est; dans; égale à'),
('text','lower','Donc chaque fois ... Q_{X,H}'),
('deletion','lower','et c’est'),
('margin note','right diagonal','NB Pour tte X 0-connexe conforme ... Riem(X)'),
('deletion','right margin','a; des métriques; qui; que')],leads='The opening bracket relates X^H=empty to the absence of an H-fixed face of a carte; check the exact geometric realization and fixed-cell statement. Curvature recap and a canonical orbit of distinguished metrics Riem(X); marginal dimensions 1 (ray) and 3, and nonproportionality. Search context cartes, facettes, Riem, métriques distinguées after freeze. Final line says X^H=empty for Q_X,H; it repeats the uniqueness assertion of scans037–038, not a proof.')

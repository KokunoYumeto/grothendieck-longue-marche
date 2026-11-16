import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,165,r'''\scanpage{165}
\margin{$\operatorname{cdim\,inj}F\leq 2\dim\unsure{\operatorname{Supp}F|X_{\operatorname{Supp}F}}+\sup_{x\in X}\dim\operatorname{inj}F_{\bar{x}}$}
\begin{center}
INSTITUT\\
DES HAUTES ÉTUDES SCIENTIFIQUES
\end{center}
\uline{Applications}\quad\uline{possibles}

\textcircled{1} Majoration de la cdim. inj. via la dim inj. des fibres

Dim. ch. \unsure{stricte|stricts} d'un préschéma (en particulier d'un pr. Alg.)

(Consulter notes de Verdier)
\margin{$\operatorname{c-dim\,inj}(F)\leq\displaystyle\sup_{x\in X,\,F_{\bar{x}}\ne0}\left[2\dim O_{X,\bar{x}}+\dim\operatorname{inj}F_{\bar{x}}\right]$}

\textcircled{2} Cas d'un Anneau $A$ de torsion \uline{loc.} \uline{ct} premier aux car. résiduelles, et $R_X$ complexe de faisceaux de $A_X$-modules \unsure{\{}loc. cts, dualisant fibre par fibre (sur $X$ régulier ---)

\uline{NB} On peut globaliser, et considérer des schémas relatifs sur $(X_{\mathrm{ét}},(\mathbf{Z}/n\mathbf{Z})_X)$ ----.

\textcircled{3} \deleted{Applications aux ths. de Lefschetz cohomologiques locaux et globaux [\unsure{Pourrais|Pouvoir} donner un article séparé ....]}
\margin{164}
''',[
('margin note','upper right pencil','cdim inj F bound'),('text','printed heading','INSTITUT DES HAUTES ÉTUDES SCIENTIFIQUES'),('text','heading','Applications possibles'),('text','upper','1 Majoration de la cdim. inj.'),('text','upper','Dim. ch. stricte'),('text','upper middle','Consulter notes de Verdier'),('margin note','upper middle pencil','c-dim inj(F) supremum bound'),('text','middle','2 Cas d’un Anneau A de torsion'),('text','lower','NB On peut globaliser'),('text','bottom','circled 3'),('deletion','bottom','Applications aux ths. de Lefschetz'),('margin note','bottom left','164')],remarks='Whole, both halves, enlarged pencil formula, first item and cancelled third item examined. The third agenda item is cancelled by diagonal strokes, including the bracketed publication thought. The pencil upper bound has an overwritten support term. The brace before loc. cts is uncertain; it may instead be an insertion stroke. Research agenda: injective dimension, locally constant torsion coefficient rings, fibrewise dualizing complexes and relative globalization.')

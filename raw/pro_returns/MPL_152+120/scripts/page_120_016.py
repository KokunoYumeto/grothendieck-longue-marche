from record_page import save_page
save_page(120,16,r'''
Soit $\unsure{\mathcal X|E}$ un espace ind-modéré. Une partie \deleted{$\unsure{\mathcal Y|Y}$} de $\mathcal X$ est dite loc. modérée si $\forall A\in\mathcal M_{\mathcal X}$, on a $A\cap\mathcal Y\in\mathcal M_{\mathcal X}$. C'est stable par intersections finies (y compris pour famille vide, i.e. $\mathcal X\in\unsure{\underrightarrow{\widetilde{\mathcal M}}|\overrightarrow{\mathcal M}}_{\mathcal X}$), par image inverse par morphismes \deleted{loc.} d'espaces ind-modérés.

La notion d'application modérée d'un espace modéré $X$ dans un $R^I$, est un cas particulier de la précédente, quand $M8$ est satisfait donc $X$ et $R^I$ sont tous deux des espaces ind-modérés.

Moyennant $M6,M7$, il existe \deleted{pour} dans $\underrightarrow{\operatorname{Esp}}_{\mathcal M_*}$ le quotient $\mathcal X/\mathcal Y$ au sens (et commute à $X\mapsto|X|$), si $\mathcal Y$ est partie $\mathrm{loc}^{\mathrm t}$ modérée, etc de $=$
\[
 \mathcal X_1\amalg_{\mathcal Z}\mathcal X_2
\]
pour $\mathcal Z\hookrightarrow\mathcal X_1$ et $\mathcal Z\hookrightarrow\mathcal X_2$ des ``\unsure{immersions} modérées'' i.e. correspondant à des parties \inserted{loc} modérées.
\mspage{15}
''',[
('text','upper','Soit X un espace ind-modéré'),('deletion','top right','Y'),('text','upper middle','C’est stable par intersections'),('deletion','before d’espaces','loc.'),('text','middle','La notion d’application modérée'),('text','lower','Moyennant M6 M7'),('deletion','before dans','pour'),('display','lower','X1 amalg Z X2'),('text','bottom','pour Z into X1'),('insertion','bottom above modérées','loc'),('text','bottom left','15')], observations='Locally moderate parts are introduced by intersection with moderate parts. Claims ind-space quotients and amalgams under M6–M7. Some overwritten calligraphic variables and the decoration on M must be checked together with subsequent pages.')

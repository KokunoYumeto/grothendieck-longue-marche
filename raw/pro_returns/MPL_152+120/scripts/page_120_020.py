from record_page import save_page
save_page(120,20,r'''
\uline{Espaces loc. modérés} Esp. \deleted{loc. cpts} \inserted{ind-modérés} dont la top. est \deleted{loc. cpt} séparée, et $\forall$ point admet un \uline{voisinage} qui est \deleted{\unsure{esp.}} modéré (donc l'espace est loc. cpt), et $\forall$ pt admet un syst. fond. de voisinages modérés, et les parties compactes sont les parties contenues dans une partie modérée --- qui forment donc un antifiltre cofinal à celui des parties compactes.

Par exemple, par $(M10)$ $R$ est un espace $\mathrm{loc}^{\mathrm t}$ modéré, donc les $R^I$ aussi.

Les espaces loc. modérés \deleted{$\unsure{f}\ \operatorname{Esp}_{\mathrm{loc},\mathcal M_*}$} forment une sous-catégorie pleine $\operatorname{Esp}_{\mathrm{loc},\mathcal M_*}$ de $\underrightarrow{\operatorname{Esp}}_{\mathcal M_*}$, stable par $\varprojlim$ finies.

\margin{Dire qu'une partie compacte et \deleted{\unsure{fermée}} d'un espace modéré est modérée.}
\margin{\unsure{loc.}}
\figure{\begin{tikzpicture}\draw (0,0)--(3.4,-.02);\draw (1.1,-.12)--(2.5,-.2)--(1.5,-.23)--(2.4,-.36);\end{tikzpicture}}
\mspage{19}
''',[
('text','top heading','Espaces loc. modérés'),('deletion','top right','loc. cpts'),('insertion','above cancellation','ind-modérés'),('deletion','second line','loc. cpt'),('deletion','third line after qui est','esp.'),('text','upper middle','dont la top. est séparée'),('text','middle','Par exemple par M10'),('text','lower','Les espaces loc. modérés'),('deletion','after loc. modérés','f Esp loc'),('margin note','bottom left oblique','Dire qu’une partie compacte'),('deletion','inside bottom margin','fermée'),('margin note','bottom left below note','loc.'),('drawing','bottom middle','divider strokes'),('text','bottom right','19')], observations='Defines locally moderate spaces and states finite inverse-limit stability. Main text says compact parts are parts contained in a moderate part; retained without inserting a closedness condition. The small bottom margin includes a cancelled adjective, uncertain.')

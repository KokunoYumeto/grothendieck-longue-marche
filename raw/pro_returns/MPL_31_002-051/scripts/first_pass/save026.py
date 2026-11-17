import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
s=r'''\scanpage{26}
\mspage{\unsure{35|55}}
tel que $A$ soit séparé et complet pour la topologie $J$-adique. Sous ces conditions:

(i) Le foncteur $F\rightsquigarrow\widehat F$ de la catégorie des Modules localement libres
sur $U'$ dans la catégorie des Modules localement libres sur $\widehat U'$ est
pleinement fidèle.

(ii) Pour tout Module localement libre $\underline F$ sur $\widehat U'$, il existe un Module
cohérent $F$ sur $\unsure{U'|V'}$ (pas nécessairement localement libre, hélas), et un
isomorphisme $\widehat F\simeq\underline F$.

Il reste seulement à prouver (ii), grâce à 5.9. Or d'après \unsure{ceytte|cette}
remarque, et exposé IX 2.1. il s'ensuit que $\underline F$ est induit par un Module
cohérent $\underline G$ sur $\widehat X'$. D'après le théorème \deleted{de comparaison et} d'existence\inserted{EGA $\overline{\underline{\mathrm{III}}}$}
5.1.4., $\underline G$ est de la forme $\widehat F$, où $F$ est cohérent sur $X$, d'où la conclusion.

\uline{Remarques} 5.1\unsure{0|1}.\inserted{$1^{\mathrm o})$} Utilisant 5.10.\inserted{, 4.7.}
\deleted{et des hypothèses convenables de}
une hypothèse convenable, disant que certains anneaux locaux des fibres
géométriques de $X'\quad S'$ sont ``purs'' resp. \unsure{parafactoriels|Parafactoriels}, on doit pouvoir
obtenir des énoncés disant \deleted{\unsure{que}} que le foncteur $Z'\rightsquigarrow\widehat Z'$ de la catégorie
des revêtements étales de $X'$ dans la catégorie des revêtements étales de
$\widehat X'$ \deleted{est} (ou ce qui revient au même, de $X'_0$) est \deleted{pleinement fidèle} une
équivalence de catégories, resp. que le foncteur $\underline L\rightsquigarrow\widehat{\underline L}$ de la catégorie
des Modules inversibles sur $X'$ dans la catégorie des Modules inversibles
sur $\widehat X'$ est une équivalence. Utilisant des résultats récents de MURRE,
il est probable que l'on doit pouvoir en déduire des théorèmes d'existence
\deleted{pour} des schémas de Picard pour \deleted{des}\inserted{certains} schémas algébriques \deleted{propres} \uline{non}
\uline{propres}. \deleted{\unsure{voir}} De façon générale, l'élimination d'hypothèses de propreté
dans divers théorèmes d'existence, notamment de représentabilité de
foncteurs comme les foncteurs de Hilbert, ou de Picard etc, à l'aide
\margin{25}
'''
e=[('margin note','top right in reading orientation','35'),('text','top continuation','tel que A soit séparé et complet'),('text','condition i','Le foncteur F↝hat F'),('text','condition ii','Pour tout Module localement libre F'),('text','upper middle proof','Il reste seulement à prouver (ii)'),('deletion','proof line 3','de comparaison et'),('insertion','proof right margin','EGA III'),('text','proof end','5.1.4. G est de la forme hat F'),('text','lower heading','Remarques 5.10'),('insertion','after heading','1o)'),('insertion','after Utilisant 5.10','4.7.'),('deletion','lower first line','et des hypothèses convenables de'),('text','lower','une hypothèse convenable disant que certains anneaux locaux'),('deletion','lower after disant','que'),('text','lower','que le foncteur Z′↝hat Z′'),('deletion','lower after hat X′','est'),('deletion','lower before une équivalence','pleinement fidèle'),('text','lower','équivalence de catégories resp. que le foncteur L↝hat L'),('text','lower','Utilisant des résultats récents de MURRE'),('deletion','near bottom before des schémas','pour'),('deletion','near bottom after pour','des'),('insertion','near bottom above des','certains'),('deletion','near bottom before non','propres'),('deletion','bottom before De façon générale','voir'),('text','bottom','De façon générale l’élimination d’hypothèses de propreté'),('margin note','bottom left in supplied orientation','25')]
save(26,s,e,sheet_kind='reused_typed',observations='Whole supplied sheet inspected, then rotated whole and both rotated supplied halves read in typed orientation. Overtyped heading digit, ce(y)tte and corrected U/V retained as doubts. The gap between X′ and S′ in the fibres sentence has no securely drawn arrow and remains a gap. Handwritten wavy functor arrows, hats, underlined module letters, EGA III insertion, and cancellations recorded. Reused sheet includes explicit expectations; they will be indexed separately after the freeze.')

import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,161,r'''\scanpage{161}
\mspage{3.}
\margin{160}
Les sites annelés $\mathrm{Ouv}(X)$ et $\mathrm{Ouv}(Y)$ sont donc isomorphes. Ils ont donc la m\inserted{ê}me cohomologie et, de plus, leurs faisceaux (quasi-) cohérents, localement libres etc. se correspondent, d'où la relation avec la théorie classique. Pour plus de détails voir [EGA IV ; § 10] déjà cité.

Nous rencontrons déjà ici un fait qui va \inserted{ê}tre illustré plus abondamment dans ce qui suit : ``dans la pratique'' un site n'est pas donné d'une façon intrinsèque. Ici les sites $\mathrm{Ouv}(X)$ et $\mathrm{Ouv}(Y)$ sont cependant équivalentes (et m\inserted{ê}me isomorphes ). On verra que la catégorie des faisceaux associée à un site (i.e. le topos associé ) est beaucoup plus intrinsèque. Choisir un site particulier admettant un topos donné comme topos associé est une opération du m\inserted{ê}me genre que de choisir un système de générateurs d'un espace vectoriel, et il est naturel de chercher un tel site qui est aussi ``petit'' que possible.

On peut cependant introduire à l'aide des sites $\mathrm{Ouv}(Z)$ ($Z/X\in(\mathrm{Sch})_{/X}$) une topologie bien déterminée sur $(\mathrm{Sch})_{/X}$ de la manière suivante:

L'application qui a chaque ouvert de Zariski d'un préschéma $Z$ associe le préschéma induit sur cet ouvert définit un foncteur
\[
\mathrm{Ouv}(Z)\xrightarrow{i_Z}(\mathrm{Sch})_{/Z}
\]
d'où un foncteur sur les catégories des préfaisceaux
\[
\widehat{\mathrm{Ouv}(Z)}\xleftarrow{i_{Z\unsure{\bullet|*}}}\widehat{(\mathrm{Sch})_{/Z}}
\]

\uline{Proposition et définition 1.}--\uline{La sous-catégorie} (strictement) \uline{pleine de} $\widehat{(\mathrm{Sch})_{/X}}$ \uline{formée des préfaisceaux} $F$ \uline{tels que} $i_{Z\unsure{\bullet|*}}(F)\in\widetilde{\mathrm{Ouv}(Z)}$ \uline{pour tout} $Z/X\in(\mathrm{Sch})_{/X}$ \uline{est une catégorie de} $\underline{U}$-\uline{faisceaux sur} $(\mathrm{Sch})_{/X}$. \deleted{\illegible{5}} \uline{La topologie correspondante sur} $(\mathrm{Sch})_{/X}$ \uline{peut \inserted{ê}tre engendrée par la prétopologie où une famille} $\{Z_\alpha\xrightarrow{j_\alpha}Z\}_{\alpha\in I}$ \uline{de morphismes de} $(\mathrm{Sch})_{/X}$ \uline{est une famille couvrante si et seulement si}
''',[
('text','upper right','3.'),('margin note','archival edge','160'),('text','top','Les sites annelés Ouv(X) et Ouv(Y)'),('insertion','top paragraph','circumflex on même'),('text','upper middle','Nous rencontrons déjà ici un fait'),('insertion','second paragraph','circumflex on être'),('insertion','second paragraph','circumflex on même isomorphes'),('insertion','second paragraph','circumflex on même genre'),('text','middle','On peut cependant introduire'),('text','middle','L’application qui a chaque ouvert'),('display','lower middle','Ouv(Z) to (Sch)/Z'),('text','lower middle','d’où un foncteur'),('display','lower middle','hat Ouv(Z) from hat (Sch)/Z'),('text','lower','Proposition et définition 1'),('deletion','lower','solid black cancellation, estimated five words'),('insertion','lower','circumflex on être engendrée')],sheet_kind='reused_typed',remarks='Original whole, upright whole, both halves, and 4x crop of solid black cancellation examined. The cancellation is physically opaque, approximately five words, and is the first illegible macro in this package. Typed équivalentes and qui a chaque ouvert retained. Hand-added circumflexes marked as insertions in accented letters. The i_Z subscript is printed as a round dot; alternatives retained pending notation audit.')

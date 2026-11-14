from record_page import save_page
save_page(120,15,r'''
\mspage{14}\mspage{7}
\margin{on suppose $M5$ mais pas $M6$ \unsure{et} $M7$}
\figure{\begin{tikzpicture}\node[draw,ellipse] {IV};\end{tikzpicture}}
Ind-structures modérées strictes \inserted{\uline{indespaces modérés}} \inserted{(ou ind-espaces modérés)} : consiste : la donnée d'un ens. $E$, et un ens de parties $\mathcal M_E$ de $E$ (les parties modérées), stable par réunions finies, \inserted{de réunion $E$}, avec une structure modérée sur chacun, ces structures s'induisant mutuellement, et
\[
 A\in\mathcal M,\quad B\in\mathcal M_A\Longrightarrow B\in\mathcal M.
\]
Il revient au $=$ de se donner la notion d'application modérée d'un $X$ modéré dans $E$, avec \deleted{\unsure{une identité}} quelques conditions \unsure{supplém.}. Si on suppose
\[
 (M8)\quad R\text{ est réunion \inserted{(filtrante par $M5$)} de ses parties modérées},
\]
on trouve une structure ind-modérée canonique sur $R$, et de $=$ sur les $R^I$.

\uline{Proposition} La catégorie des \inserted{$\overrightarrow{\operatorname{Esp}}_{\mathcal M_*}$} \deleted{Ind} Ind-espaces modérés stricts admet des $\varprojlim$ finies, le foncteur oubli y commute.
\margin{\unsure{des ensembles modérés}}
\margin{$M1:M5$}
\margin{$\overrightarrow{\operatorname{Esp}}_{\mathcal M_*}$ \unsure{est obtenue} par $\uline{\varinjlim}$ filtrantes \unsure{des injections} \deleted{strictes} \unsure{dans les ensembles} \unsure{modérés} \unsure{quelconques}.}

Si $R_0\ne\varnothing$ (i.e. dans $\operatorname{Esp}_{\mathcal M_*}$ il y a sommes disjointes finies) il y a des sommes disjointes \deleted{finies} \inserted{(infinies !)} dans $\overrightarrow{\operatorname{Esp}}_{\mathcal M_*}$, et $X\longrightarrow |X|$ y commute.
''',[
('text','top left','14'),('text','top right','7'),('margin note','top left','on suppose M5'),('drawing','top','circled IV'),('text','top heading','Ind-structures modérées strictes'),('insertion','above heading','indespaces modérés'),('insertion','top right','ou ind-espaces modérés'),('text','upper','consiste la donnée'),('insertion','above avec','de réunion E'),('display','middle upper','A in M B in MA'),('text','middle','Il revient au ='),('deletion','after avec','une identité'),('display','middle lower','M8 R est réunion'),('insertion','above de ses parties','filtrante par M5'),('text','middle lower','on trouve une structure'),('text','lower','Proposition La catégorie'),('insertion','above des','Esp with arrow'),('deletion','before Ind-espaces','Ind'),('margin note','above proposition oblique','des ensembles modérés'),('margin note','left of proposition','M1:M5'),('margin note','lower left oblique','Esp est obtenue'),('deletion','lower left margin','strictes'),('text','bottom','Si R0 nonempty'),('deletion','bottom','finies'),('insertion','above cancelled finies','infinies !')], observations='Section IV, ind-structures/indespaces modérés stricts. Axiom M8: R is the union of its moderate parts. Proposition about finite inverse limits and sums. Bottom-left marginal category description remains highly uncertain; do not treat its tentative words as established.')

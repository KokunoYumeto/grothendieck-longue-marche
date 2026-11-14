from record_page import save_page
save_page(120,8,r'''
Alors $R$ est muni d'une structure modérée canonique (en tant que modèle $\subset R^1=R$), i.e.
\[
 R\in\operatorname{Ob}\mathcal E\qquad(\mathcal E=\operatorname{Esp}_{\mathcal M_*})
\]
et $\forall$ objet de $\mathcal E$ est isomorphe à un sous-objet d'un $R^n$ \inserted{(produit dans $\mathcal E$)}. On récupère $\mathcal M_n$ comme l'ens des sous-objets \inserted{\unsure{sous-ens.} de $R^n$ \unsure{correspondants dans Ens}} (dans $\mathcal E$) de l'objet $R^n$. On trouve que la donnée d'un $\mathcal M_*$ est équivalente à la donnée d'un système (à isom. près)
\[
 (\mathcal E,R,X\longmapsto |X|)
\]
de a) la catégorie $\mathcal E$ avec $\varprojlim$ finies

b) le foncteur $X\mapsto |X|$ $\mathcal E\longrightarrow(\mathrm{Ens})$ exact à gauche

c) l'objet $R\in\operatorname{Ob}\mathcal E$ tel que $\forall$ objet de $\unsure{R|\mathcal E}$ se plonge dans un $R^n$.

\margin{Parler aussi des applications modérées d'ens. modérés dans des $R^I$.}

\margin{Introduire les parties modérées d'un espace modéré \unsure{correspondant} aux sous-objets dans $\operatorname{Esp}_{\mathcal M_*}$, les propriétés de stabilité $f(A)$, $f^{-1}(B)$, produits cartésiens.}

\figure{\begin{tikzpicture}\node[draw,ellipse] {III};\end{tikzpicture}}
\uline{Limites inductives finies d'\unsure{espaces} modérés}

S'intéresser à la question des réunions finies des parties modérées, et des $\varinjlim$ finies dans $(\operatorname{Esp}_{\mathcal M_*})$.

\margin{A partir d'ici, \unsure{je n'utilise} $\unsure{M5|M4}$ \unsure{de} \unsure{réunion} \unsure{seulement} \unsure{possible}. \unsure{Je verrai} $(M0)$ pour les \unsure{suites} \unsure{par un axiome}.}
\mspage{7}
''',[
('text','top','Alors R est muni'),('display','upper','R in Ob E'),('text','upper','et tout objet'),('insertion','above R^n','produit dans E'),('insertion','above sous-objets','sous-ens. de R^n'),('text','upper middle','On récupère M_n'),('display','middle','(E,R,X maps to |X|)'),('text','middle','a) la catégorie E'),('text','middle lower','b) le foncteur'),('text','lower','c) l’objet R'),('margin note','above III','Parler aussi des applications'),('margin note','oblique lower left','Introduire les parties'),('drawing','lower','circled III'),('text','lower heading','Limites inductives'),('text','bottom','S’intéresser à la question'),('margin note','oblique lower right','A partir d’ici'),('text','bottom right','7')], observations='Categorical presentation using E, R, the underlying-set functor; finite colimits heading. The two oblique margins and the insertion over sous-objets need special reinspection; the lower right margin is particularly uncertain. No mathematical reconstruction used to complete it.')

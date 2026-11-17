from record_page import record
tex=r'''\scanpage{31}
% archive foliation: 30
(Si $A$ est réduite à un objet, \inserted{$A$ \unsure{seul}}, l'anneau
des endom. $k$ de celui-ci, on
trouve une équivalence avec la
cat. des $k$-modules à droite
\uline{libres de type fini}, par $X\longmapsto\operatorname{Hom}(A,X)$)
\par\bigskip\hrule\bigskip
Transformant par dualité les énoncés.
Si $\forall$ objet de $C$ est $\varprojlim$
d'objets de $A$, alors le foncteur
canonique
\[
\rho:C^\circ\longrightarrow\widehat{A^\circ}
\quad(\text{resp. }\widehat{A^\circ}_{ab})
\]
\margin{$\underline{\operatorname{Hom}}(A,\mathrm{Ens})$
(resp. $\underline{\operatorname{Hom}}(A,\mathrm{Ab})$)}
vers les foncteurs
\uline{covariants} sur $A$ à valeurs dans
$\mathrm{Ens}$ (resp. $\mathrm{Ab}$) est pl. fidèle. Si
de plus, $\forall$ objet de $C$ est
$\varinjlim$ de certains types d'objets
de $C$, alors l'image essentielle est
contenue dans la sous-cat. pleine
de $\widehat{A^\circ}$ (resp. $\widehat{A^\circ}_{ab}$) formée des
foncteurs $A\longrightarrow\mathrm{Ens}$ (resp. $A\longrightarrow\mathrm{Ab}$)
qui sont $\varprojlim$ de ces types de
foncteurs représentables --- et
l'image essentielle est $\simeq$ égale à
cette dernière catégorie si
'''
record(31,tex,[('text','top parenthesis','Si A réduite à un objet; anneau endom k; modules à droite libres de type fini'),('insertion','top above objet','A seul'),('display','top inline functor','X↦Hom(A,X)'),('text','after separator','Transformant par dualité les énoncés'),('text','upper-middle','Si tout objet de C lim inverse objets A; foncteur canonique'),('display','middle','ρ:C°→widehat(A°) (resp ab)'),('margin note','under right display','Hom(A,Ens), Hom(A,Ab)'),('text','middle-lower','vers les foncteurs covariants; pl fidèle'),('text','lower','tout objet de C lim directe; image essentielle sous-cat pleine'),('display','lower inline','A→Ens (resp A→Ab)'),('text','bottom','qui sont lim inverse; image essentielle égale à catégorie si')],doubts=[('top insertion','A seul','A soit le? very cramped above line; only A secure','low'),('top endomorphism-ring phrase','l’anneau des endom. k de celui-ci','word order as seen; ring label k may syntactically follow endom.','medium'),('canonical functor letter','ρ','r possible; same convention as preceding scan','medium'),('lower source category','objets de C','A mathematically plausible but visible letter rounded C','medium'),('last comparison','= up to ≃: est ≃ égale à','equivalence sign may instead be cancelled word; no mathematical normalization','low')])

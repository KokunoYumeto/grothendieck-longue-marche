from save_page import save_page
save_page(91,r'''\scanpage{91}
% archive foliation: 90
Ainsi, on obtient via le pol. car. modifié un
hom
\[
(V,f)\longmapsto\frac1{\det(\mathrm{id}_V-ft)}=L(V,f)
\]
\[
R(\unsure{\mathbf N|\mathbf Z};k)\longrightarrow 1+k[[t]]^+
\]
\inserted{\unsure{Composé|Conjugué} avec l'\deleted{\unsure{isomorphisme|homomorphisme}}\inserted{aut° ``additif''}
$\varphi(t)\longmapsto\dfrac1{\varphi(t)}$ dans $1+k[[t]]^+$}
qui est un hom de $\lambda$-anneaux,
\margin{en fait, à valeurs dans les \uline{fractions rationnelles}
de valeur $1$ en $0$}

Lorsque $k$ est un corps, l'hom
précédent est injectif. En effet, si
\deleted{$k$ est \unsure{alg. clos},} la connaissance de la
série formelle permet de reconstituer \inserted{la fonction rationnelle}
[$k[t]$
étant factoriel] l'élément
$\displaystyle\sum_{\substack{P\ \unsure{irr.|pol.}\\\mathrm{unitaires}}}c_P(V_P,f_P)$
\deleted{dont} par
\[
L=\prod_Q Q^{c_P}
\]
[$Q$ et $P$ associés de
la façon précisée plus haut].

Notons qu'on a un homomorphisme
naturel \deleted{\unsure{$k$ séparé alg.}}
\[
1+k[[t]]^+\longrightarrow k[[t]]
\]
\[
\varphi(t)\longmapsto\frac{\varphi'(t)}{\varphi(t)}\deleted{\unsure{t}}
\]
qui correspond à
\[
\Lambda(V,f)(t)=\frac{L(V,f)'(t)}{L(V,f)(t)}
=[\log L(V,f)]'=\frac1t\sum_1^\infty(\operatorname{Tr}f^n)t^n.
\]
\deleted{En car. $0$, on peut}
Si $k$ de car. $0$, \inserted{i.e. $k\supset\mathbf Q$} on peut inverser cet
homomorphisme par $\exp\left(\int_0^{\unsure{t}}\Lambda(V,f)(t)\right)$.
Donc \inserted{si $k$ est \margin{un corps de car. $0$,}}
$\Lambda:R(\mathbf N,k)\longrightarrow k[[t]]$ est aussi injectif \deleted{($k$ corps}
''',[
('top','text','Ainsi, on obtient via le pol. car. modifié un hom'),
('upper','formula','(V,f) maps to 1/det(id_V-ft)=L(V,f)'),
('upper','formula','R(N/Z;k) -> 1+k[[t]]^+'),
('upper interline','insertion','Composé/Conjugué avec l’aut° additif phi -> 1/phi'),
('upper','text','qui est un hom de lambda-anneaux'),
('upper-left margin','margin note','en fait, à valeurs dans les fractions rationnelles de valeur 1 en 0'),
('middle','text','Lorsque k est un corps, l’hom précédent est injectif'),
('middle','text','connaissance de la série formelle; fonction rationnelle; k[t] factoriel'),
('middle','formula','sum c_P(V_P,f_P)'),
('lower-middle','formula','L=product_Q Q^{c_P}'),
('lower-middle','text','Q et P associés de la façon précisée plus haut'),
('lower','text','Notons qu’on a un homomorphisme naturel'),
('lower','formula','1+k[[t]]^+ -> k[[t]]; phi -> phi prime/phi'),
('lower','formula','Lambda(V,f)(t)=L prime/L=[log L] prime=1/t sum Tr(f^n)t^n'),
('bottom','text','Si k de car. 0, i.e. k contains Q; inverse exp integral Lambda'),
('bottom','formula','Lambda:R(N,k) -> k[[t]] est aussi injectif'),
('bottom-left margin','margin note','un corps de car. 0')
],remarks='Whole, both halves, inserted automorphism line, boxed left margin, reconstruction clause and dense footer enlarged. Product exponent c_P and absent differential retained from ink; overwritten ring N/Z remains uncertain in top line while bottom N is clear.')

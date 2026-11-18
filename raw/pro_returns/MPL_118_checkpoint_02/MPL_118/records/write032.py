from save_page import save
text=r'''
\scanpage{32}
% archive foliation: 31
\uline{Corollaire 2} \uline{Dans} $\mathrm{Hot}(\underline W)$, les produits finis existent, et les foncteurs canoniques $(\mathrm{Cat})\longrightarrow\mathrm{Hot}(\underline W)$, $\widehat A\longrightarrow\mathrm{Hot}(\underline W)$ ($A$ catégorie test stricte) y commutent.

\margin{il suffit $=$ que $A$ soit tot. $\underline W$-asph.}

On est ramené à prouver que
\[
\widehat A\longrightarrow[\mathrm{Hot}(\underline W)\simeq]\underline W_A^{-1}\widehat A
\]
commute aux produits finis, i.e. que
\[
(*)\quad\operatorname{Hom}_{\underline W_A^{-1}\widehat A}(X,\unsure{Y_j|Y})\longrightarrow\prod_J\operatorname{Hom}_{\underline W_A^{-1}\widehat A}(X,Y_j)
\]
est bijectif, pour \unsure{tte} famille finie $(Y_j)_{j\in J}$ d'objets de $\widehat A$, et $X$ de $\widehat A$.

\margin{\deleted{\unsure{on voit}} Mais le cas de $(\mathrm{Cat})$ se traite directement.}

\uline{Surjectivité} Un élément du $2^{\mathrm o}$ \unsure{mb} provient d'une famille
\diagram{\begin{tikzcd}
f_j:X\arrow[r]&Y'_j
\end{tikzcd}}
où $Y_j\longrightarrow Y'_j$ équiv. faible.

\deleted{\uline{\unsure{Dém}}}\inserted{Considérons} alors
\[
f=(f_j):X\longrightarrow\prod Y'_j=Y'
\]
il définit $X\longrightarrow Y$ qui convient, \uline{si on sait que} $\prod Y_j\longrightarrow\prod Y'_j$ est $\in\underline W$.
'''
elements=[
('text','top','Corollaire 2 Dans Hot(W), les produits finis'),
('display','upper','(Cat) → Hot(W); Ahat → Hot(W)'),
('text','upper middle','A catégorie test stricte'),
('margin note','right below stricte','il suffit = que A soit tot. W-asph.'),
('text','middle','On est ramené à prouver que'),
('display','middle','Ahat → [Hot(W) ≃] W_A^-1 Ahat'),
('text','middle','commute aux produits finis'),
('display','middle lower','(*) Hom(X,Y_j) → product Hom(X,Y_j)'),
('text','lower middle','est bijectif, pour tte famille finie'),
('margin note','left slanting','Mais le cas de (Cat) se traite directement'),
('deletion','beginning of margin','on voit'),
('text','lower','Surjectivité Un élément du 2o mb'),
('diagram','lower','f_j:X → Y prime_j'),
('display','right of f_j','Y_j → Y prime_j équiv. faible'),
('deletion','near foot','Dém'),
('insertion','above Dém','Considérons'),
('display','near foot','f=(f_j):X → product Y prime_j = Y prime'),
('text','foot','il définit X → Y qui convient, si on sait que'),
('display','foot','product Y_j → product Y prime_j in W'),
]
save(32,text,'text',elements,'Products corollary; a marginal note replaces strict test with total W-asphericity as sufficient, and another notes a direct Cat treatment. The first Hom target seems to carry j despite the expected product; this remains an explicit reading doubt. The final appeal to product stability is underlined by the author. No mathematical checking done here.')

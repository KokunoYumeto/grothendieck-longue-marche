from save_page import save_page
save_page(59,r'''\scanpage{59}
% archive foliation: 58
Si $M$ est un motif sur $K$, $\frac12$ simple pour simplifier, alors on a
\diagram{\begin{tikzcd}
\unsure{\mathfrak{g}_\ell|g_\ell}(\overline{K}^{\unsure{\ell|s}}/K) \arrow[r] & \mathrm{End}(M_\ell)\simeq\check{M}_\ell\otimes M_\ell
\end{tikzcd}}

On pense que l'image provient d'un motif $\unsure{\mathfrak{g}|g}\deleted{(M)}\inserted{_{M}}\inserted{\subset\check{M}\otimes M}$ indépendant de $\ell$, [qui est un motif en Algèbres de Lie].
Pour $M$ de plus en plus grand, on trouve un \uline{promotif} \inserted{(en alg de Lie)} canonique, appelé \uline{promotif} \uline{fondamental}, qui peut aussi se construire de façon canonique en termes de la catégorie des motifs, munie de ses structures tensorielles ---

Quelle est la partie ``Algébrique'' de ce promotif ? [Sur un corps fini, c'est tout --- le promotif n'étant lui-même autre que $\mathbf{Z}(0)$ ! ; \deleted{dans}\inserted{en} tout \deleted{\unsure{autre}}\inserted{autre} cas, \unsure{on} \inserted{je pense qu'il est \deleted{\unsure{purement}} \unsure{réduit}} \deleted{\unsure{lui-même}} \deleted{\unsure{centre}} \deleted{\unsure{dans le}} \deleted{\uline{centre} du dit promotif fondamental}, et \deleted{je pense que c'est} \inserted{réduit à $\mathbf{Z}(0)$} [\unsure{h. scalaires}]]
''',[
('top','text','Si M est un motif sur K; 1/2 simple pour simplifier'),
('upper','diagram','g_l(Kbar/K) -> End(M_l) ~= check M_l tensor M_l'),
('middle','text',"On pense que l'image provient d'un motif g_M"),
('middle-lower','text','Pour M de plus en plus grand; promotif fondamental; structures tensorielles'),
('lower','text','Quelle est la partie Algébrique de ce promotif ?'),
('bottom; overwritten ending','text','Sur un corps fini; Z(0); en tout autre cas; réduit à Z(0)')],remarks='Whole page and halves checked, with enlargements of the first g symbol and crossed footer. Footer revision layers remain low confidence; the bracketed final abbreviation is not expanded.')

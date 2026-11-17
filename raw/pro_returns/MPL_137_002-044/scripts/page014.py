from record_page import record
tex=r'''\scanpage{14}
% archive foliation: 13
$k$ anneau (com. unit.)

\uline{Déf 1} Un $k$-module $\frac12$ simplicial $L_\bullet$ est dit
$\partial$-pseudo-cohérent (resp. strictement $\partial$-pseudocohérent,
resp. $\partial$-parfait, resp strictement $\partial$-parfait)
si $L^!_\bullet$ (le complexe de chaînes associé
par Dold-Puppe) est pseudo-cohérent
(resp. str. ps. cohérent, resp parfait, resp.
strict.t parfait).
\margin{\unsure{Donc on a par déf a) ci-dessous}}

\uline{Prop 1} a) $L_\bullet$ est str. $\partial$-pseudocohérent
(resp. str. $\partial$-parfait) si et seulement si les
$(L^!_n)$ sont projectifs de t.f. (resp. et
nuls sauf un nb fini); \deleted{\illegible{3}}

b) $L_\bullet$ est str. $\partial$-ps. coh. ssi les $L_n$
sont projectifs de t.f.

c) $L_\bullet$ est str. $\partial$-parfait ssi $L_\bullet$ est
extension successive \inserted{finie} de Modules de
la forme $\Lambda^i\Psi_\bullet\otimes_{\mathbf Z}M_i$
\inserted{$(i\geq0)$}, où les
$M_i$ sont $k$-modules pr. de t.f.
(l'ordre des facteurs des \unsure{une} filtration
croissante \unsure{précédente} pourra d'ailleurs
être choisi par ordre des $i$
croissant), ou encore \deleted{\unsure{ssi}}
(\unsure{\illegible{2} le complexe à spécifier comme une résolution}).
\margin{ssi les $L_n$ sont proj. de t.f. et
$f_{L_\bullet}(n)=\operatorname{rg}_kL_n$ \unsure{une fonction
polynomiale pour $n$ grand} \unsure{(on}\illegible{3}\unsure{telles fonctions)}}

d) Si $k$ est noeth., $L_\bullet$ est $\partial$-
pseudo-cohérent (ssi les $L^!_n$ sont
de type fini sur $k$, \unsure{ou encore}) ssi
les $L^{\unsure{\natural|\sharp}}_n$ le sont.

e) Si $k$ est noeth. régulier, $L_\bullet$ est
$\partial$-parfait ssi les $L_n$ sont de t.f.
et \deleted{\unsure{$L_\bullet\otimes K$}} $\forall$ $K$ corps résiduel, la fonction
'''
record(14,tex,[('text','top','k anneau (com. unit.)'),('text','definition','Déf1 Un k-module ½ simplicial L est dit ∂-pseudo-cohérent'),('text','definition continuation','si L! le complexe de chaînes associé par Dold–Puppe'),('margin note','right beside end of definition','Donc on a par déf a) ci-dessous'),('text','proposition a','L est str. ∂-pseudocohérent'),('deletion','right end of a','three struck words'),('text','proposition b','L est str. ∂-ps. coh. ssi les L_n sont projectifs'),('text','proposition c','L est str. ∂-parfait ssi extension successive'),('insertion','above successive','finie'),('text','c elementary objects','Λ^iΨ⊗Z M_i'),('insertion','above M_i','i≥0'),('text','c parenthesis','l’ordre des facteurs; filtration croissante'),('deletion','after ou encore','ssi'),('text','end c overwritten parenthesis','complexe à spécifier comme une résolution'),('margin note','left lower, linked to c','ssi les L_n sont proj. de t.f.; f_L(n)=rg_k L_n'),('text','proposition d','Si k est noeth.; pseudo-cohérent'),('text','proposition e, bottom','Si k est noeth. régulier; ∀K corps résiduel'),('deletion','last line before ∀','L⊗K')],doubts=[('definition note at right','Donc on a par déf a) ci-dessous','compressed note; words not all certain','low'),('end a deletion','three illegible words','nearly completely inked over','low'),('c parenthesis','des une filtration; précédente','rapid faded script and grammatical irregularity preserved','low'),('end c inserted/revised parenthesis','complexe à spécifier comme une résolution','several words physically unclear; anchoring uncertain','low'),('lower left margin','rank function polynomial for n grand; telles fonctions','oblique writing; final words and connector unclear','low'),('d superscript on final L','natural / sharp','not read as ! without a visible dot; comparison needed','low'),('last-line deletion','L⊗K','thick overwrite','low')],notation=[('differential perfection prefix',r'$\partial$-','scan 14 definition; curled partial sign, not ordinary d'),('strict finiteness abbreviation','t.f.','scan 14; distinct letters t.f. here'),('alternate normalization superscript',r'$L^{\unsure{\natural|\sharp}}_n$','scan 14 d; unclear symbol, not silently harmonized to !')])

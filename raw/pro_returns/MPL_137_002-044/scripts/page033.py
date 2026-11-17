from record_page import record
tex=r'''\scanpage{33}
% archive foliation: 32
En fait, on trouve un diagramme
can. commutatif
\diagram{\begin{tikzcd}[column sep=small,row sep=huge]
&&A\arrow[r,hook]\arrow[dll,"\operatorname{id}"']\arrow[drr,"\operatorname{id}"]&
C\arrow[dll,"\rho","\sim"']\arrow[drr,"\rho'","\sim"']\\
A\arrow[r,hook]&\widehat A_\tau\arrow[r,hook]&\widehat A&&
A\arrow[r]& (\widehat{A^\circ}_{\tau'})^\circ\arrow[r,hook]&
(\widehat{A^\circ})^\circ
\end{tikzcd}}
(resp. sur $\widehat A_{ab}$ et $\widehat{A^\circ}_{ab}$)
On trouve en particulier une
équivalence remarquable
\[
\widehat A_\tau\simeq(\widehat{A^\circ}_{\tau'})^\circ
\]
qui peut se définir intrinsèque-
ment \inserted{en termes de $A,\tau,\tau'$}, chaque fois qu'on a une
sous-cat. $D$ de $\widehat A$ (resp. une sous-cat.
additive de $\widehat A_{ab}$), stable \inserted{dans $\widehat A$} par
$\varprojlim$ de type $\tau$, et \inserted{où existent les} $\varinjlim$ de type $\unsure{\tau|\tau'}$
(pas néc. les mêmes que dans $\widehat A$!)
et dont chaque objet est à la fois
$\varprojlim$ \inserted{de type $\tau$} dans $\unsure{C|D}$ de foncteurs repr.,
et $\varinjlim$ \inserted{de type $\tau'$} dans $\unsure{C|D}$ de tels foncteurs.

Si $A$ est réduite à un seul objet \inserted{$A$} et
dans le cas resp. ($C$ additive)
$\tau=\tau'=$ \deleted{\unsure{ens.}} catégories discrètes finies,
on trouve une antiéquivalence
entre modules libres de t.f. à g. et
'''
record(33,tex,[('text','top','En fait diagramme can commutatif'),('diagram','top','A⊂C; id maps; ρ,ρ′ equivalences to Â_τ and opposite presheaf subcat'),('text','under diagram','resp sur Â_ab et widehat(A°)_ab'),('text','middle','On trouve une équivalence remarquable'),('display','middle','Â_τ≃(widehat(A°)_τ′)°'),('text','middle-lower','qui peut se définir intrinsèquement; sous-cat D'),('insertion','above chaque fois','en termes de A,τ,τ′'),('insertion','after stable','dans Â'),('text','lower','limits τ; colimits τ; pas néc les mêmes; each object'),('insertion','above second limits','où existent les'),('insertion','before dans C first','de type τ'),('insertion','before dans C second','de type τ′'),('text','bottom','Si A réduite un seul objet; C additive; τ=τ′ discrètes finies'),('insertion','after seul objet','A'),('deletion','after τ=τ′=','ens.'),('text','bottom continued','antiéquivalence entre modules libres de t.f. à g. et')],doubts=[('diagram equivalence functors','ρ,ρ′','cursive r with loop; consistent tentative convention','medium'),('middle subcategory','D','could be a calligraphic D; distinguish from subsequent rounded C','medium'),('colimit type following où existent','τ','τ′ possible; small prime may merge with right boundary','low'),('two ambient categories near bottom of argument','C','D possible; manuscript had named D; no mathematical correction','low'),('cancelled abbreviation before catégories','ens.','small overwritten start may be aux','low')],notation=[('presheaf subcategories by shape classes',r"$\widehat A_\tau,(\widehat{A^\circ}_{\tau'})^\circ$",'scan 33; outer opposite sign retained separately from inner A°')])

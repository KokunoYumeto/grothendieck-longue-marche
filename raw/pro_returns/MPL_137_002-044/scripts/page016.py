from record_page import record
tex=r'''\scanpage{16}
% archive foliation: 15
\unsure{si on dispose d'une théorie analogue}
pour les complexes de chaînes de $k$-modules
ps. coh., ce qui \unsure{est guère le cas que}
si on suppose $k$ principal, (\unsure{Dedekind}
à la rigueur). Supposons donc
$k$ \deleted{\unsure{anneau}} \unsure{principal}
\deleted{\uline{principal}},
\inserted{(le cas $k$ \unsure{non commutatif} est déjà pratiquement le
\unsure{cas des $L_\bullet$} \illegible{3})}
et soit $\operatorname{Max}(k)$ l'ens.
des idéaux \deleted{premiers} \inserted{maximaux} de $k$,
$\unsure{\mathfrak P}=\mathbf N^{(\operatorname{Max}k)}-\{0\}$.
\margin{\unsure{la classe d'un projectif de t.f. est son rang}}

\uline{Th.} Tout $L_\bullet$ \inserted{str.} $\partial$-ps. coh. est isomorphe
à un produit de modules de la
forme suivante
\[
\begin{array}{lll}
a)&\deleted{\unsure{M_i\otimes_k}}(\Lambda^i\Phi_\bullet)^{\mu_i}
 &(i\geq1)\quad\deleted{M_i\ k\text{-module libre}}\ \inserted{\mu_i\in\mathbf N}\\
&&\deleted{\text{libre de t.f.}}\\
b)&\deleted{\unsure{N_j\otimes_k}}(\Lambda^j\Psi_*)^{\nu_j}
 &(j\geq0)\quad\deleted{N_j}\ (\nu_j\in\mathbf N)\\
c)&\deleted{\unsure{P_{i,\ell}\otimes_k}}\Phi(i,\ell)_*^{\beta_{i,\ell}}
 &(i\geq1)\quad\deleted{\unsure{P_{i,\ell}}}\ \beta_{i,\ell}\in\mathbf N,
\end{array}
\]
\deleted{où $\Phi(i,\ell)$}
$\ell$ un \deleted{idéal} diviseur de $k$ (cf plus bas
la définition de $\Phi(i,\ell)_*$), de façon
précise
\[
\begin{split}
L_\bullet&\simeq\prod_{i\geq1}M_i\otimes_k\Lambda^i\Phi_\bullet
\times\prod_{j\geq0}N_j\otimes_k\Lambda^j\Psi_*\\
&\qquad\times\prod_{\substack{i\geq1\\\ell\in\unsure{\mathfrak P}}}
\Phi_{i,\ell}^{\beta_{i,\ell}}
\end{split}
\]
où pour tout
$i\geq1$, l'ensemble des $\ell$ où les $\beta_{i\ell}$ sont non
nuls est fini. (NB de tels
produits sont bien str. $\partial$-ps coh.)
On peut supposer de plus que pour tout
$i$ donné, \unsure{l'ens.} des $\ell\in\unsure{\mathfrak P}$ \deleted{\unsure{les}} tels
que $\beta_{i\ell}\neq0$ est tot. ordonné, moyennant
'''
record(16,tex,[('text','faint top continuation','si on dispose d’une théorie analogue'),('text','upper paragraph','complexes de chaînes; k principal'),('deletion','after k','anneau; principal'),('insertion','above assumption','le cas k non commutatif ...'),('text','upper definition of index set','Max(k); P=N^(Maxk)−{0}'),('deletion','before de k','premiers'),('insertion','above premiers','maximaux'),('margin note','left circled','la classe d’un projectif de t.f. est son rang'),('text','theorem heading','Th. Tout L ∂-ps.coh. est isomorphe'),('insertion','above ∂','str.'),('display','a','deleted M_i⊗; (Λ^iΦ)^μ_i; i≥1'),('deletion','right of a','M_i k-module libre; libre de t.f.'),('insertion','right above a','μ_i∈N'),('display','b','deleted N_j⊗; (Λ^jΨ)^ν_j; j≥0'),('deletion','right b','N_j'),('display','c','deleted P_iℓ⊗; Φ(i,ℓ)^β_iℓ; i≥1'),('deletion','right c','P_iℓ'),('deletion','below display','où Φ(i,ℓ)'),('text','middle','ℓ un diviseur de k; cf plus bas'),('deletion','after ℓ un','idéal'),('display','lower product decomposition','L≃Π M_i⊗Λ^iΦ ×Π N_j⊗Λ^jΨ ×Π Φ_iℓ^β_iℓ'),('text','lower finiteness','où pour tout i≥1; ensemble des ℓ fini'),('text','lower NB','de tels produits sont bien str. ∂-ps coh.'),('text','bottom','On peut supposer ... totalement ordonné'),('deletion','after ℓ∈P','les')],doubts=[('first paragraph','si on dispose; est guère le cas que; Dedekind','very faint words over staff; negatives particularly uncertain','low'),('assumption on k','principal; deleted anneau/principal','blue hatching and superseding word ambiguous','low'),('interlinear parenthesis','le cas k non commutatif ...','small faint handwriting with several unreadable words','low'),('upper circled note','la classe d’un projectif de t.f. est son rang','left extremity and final noun faint','low'),('index-set letter','mathfrak P','may be another script capital; no forced Greek identification','low'),('a–c deleted coefficients','M_i,N_j,P_iℓ with tensors','heavy hatching; last capital particularly uncertain','low'),('new multiplicity letters','μ_i,ν_j,β_iℓ','β formed with loop and stem; local alternatives possible','medium'),('lower product display','M_i,N_j retained alongside multiplicity powers in previous display','visible unreconciled revision; not harmonized mathematically','high'),('bottom abbreviation','l’ens.; tot.','faint strokes','medium')],notation=[('torsion elementary module',r'$\Phi(i,\ell)_*$','scan 16; rounded Φ rather than forked Ψ'),('multiplicity of torsion elementary module',r'$\beta_{i,\ell}$','scan 16'),('divisor indexing monoid',r'$\unsure{\mathfrak P}$','scan 16; script capital unresolved')])

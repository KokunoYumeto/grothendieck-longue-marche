from record_page import record
tex=r'''\scanpage{20}
% archive foliation: 19
2) Pour que $L_\bullet$ soit \deleted{projectif}, \inserted{flasque (projectif)},
il f. et s.
qu'il n'y ait que des facteurs
$(\Lambda^i\Phi_*)^{\mu_i}$
\inserted{(resp. et $(\Lambda^0\Psi_*)^{\nu_0}=k^{\nu_0}$)}.
Pour que $L_\bullet\otimes_k K$ (comme
$K$-module $\frac12$ simplicial, où $K$ est le
corps des fractions) soit flasque
il f. et suffit qu'il n'y ait que des
$(\Lambda^i\Phi_*)^{\mu_i}$, $\Phi_*(i,n)^{\beta_{i\ell}}$
\inserted{$(i\geq1)$}, à l'exclusion
des $(\Lambda^j\Psi_*)^{\nu_j}$ $(j\geq0)$.

\deleted{Pour}
3) Pour déterminer d'ailleurs toute la
catégorie additive des $k$-modules
$\frac12$ simpliciaux str. $\partial$-ps coh. (resp.
str. $\partial$-parfaits), il suffit en principe
de déterminer les hom. modules
entre les objets indécomposables
\[
\Lambda^i\Phi,\quad\uline{\Phi(i,n)},\quad\Lambda^j\Psi_*
\qquad(i\geq1,j\geq0)
\]
\inserted{\unsure{un pour chaque idéal}\ \unsure{chaque diviseur}}
qu'on peut réduire à deux types si
on admet aussi le cas $n=1$
\[
\Phi(i,n)\qquad\Lambda^j\Psi_*
\qquad(i\geq1,j\geq0)
\]
On trouve, en repassant aux
complexes de chaînes associés
'''
record(20,tex,[('text','remark 2','Pour que L soit projectif'),('deletion','first line','projectif'),('insertion','above projectif','flasque (projectif)'),('text','upper','il f.et s.; facteurs (Λ^iΦ)^μ_i'),('insertion','above factor sentence','resp. et (Λ^0Ψ)^ν0=k^ν0'),('text','upper-middle','L⊗kK; K corps des fractions'),('text','middle allowed factors','(Λ^iΦ)^μ_i; Φ(i,n)^β_iℓ'),('insertion','above factors','i≥1'),('text','middle excluded factors','à l’exclusion des (Λ^jΨ)^ν_j, j≥0'),('deletion','before remark 3','Pour'),('text','remark 3','Pour déterminer d’ailleurs toute la catégorie additive'),('text','remark 3 continuation','hom. modules; objets indécomposables'),('display','lower-middle','Λ^iΦ, Φ(i,n), Λ^jΨ; i≥1,j≥0'),('insertion','below Φ(i,n)','un pour chaque idéal; chaque diviseur'),('text','lower','réduire à deux types; cas n=1'),('display','lower','Φ(i,n), Λ^jΨ; i≥1,j≥0'),('text','bottom','On trouve, en repassant aux complexes de chaînes associés')],doubts=[('first line revision','flasque (projectif)','parenthetical projectif at top slightly clipped','medium'),('top inserted factor','resp. et (Λ^0Ψ)^ν0=k^ν0','tiny superscripts over staff; ν0 particularly faint','low'),('remark 3 opening','d’ailleurs toute la','faded joins between words','medium'),('note below Φ(i,n)','un pour chaque idéal; chaque diviseur','possibly second phrase replaces first, deletion not clearly visible','low'),('two index conditions','i≥1,j≥0','horizontal staff crosses inequality bars','medium')],notation=[('projectivity versus acyclicity revision','projectif → flasque (projectif)','scan 20; cancellation retained'),('scalar n=1 as an elementary case',r'$\Phi(i,n),\ n=1$','scan 20')])

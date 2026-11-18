import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(43,r'''\mspage{17}
% archive foliation: 45
En fait, les anti-involutions de $\mathbb C$ ont toutes des pts fixes, et ce sont les symétries orth. p.r. à des droites réelles (pas néc. passant par l'origine) dans $\mathbb C$. La surface à bord conforme correspondante est isom. à un \uuline{demi-plan} (avec bord). On note que tte métrique \inserted{sur $\mathcal X$,} quasi-invariante par autom. conformes, est invariante par autom. d'ordre fini, en particulier par $\sigma$. Donc il y a sur $X$ une classe \inserted{can.} de métriques riemanniennes, mod. cte.

\uline{NB} \deleted{\unsure{Le}} Le modèle de $X$ envisagé est le demi-plan supérieur \deleted{$\unsure{\mathbb C}$}
\[
\overline{\mathbb H}=\{z\in\mathbb C\mid\mathrm{Im}\,z\geq0\}.
\]
Le groupe des autom. de $\overline H$, isom. au groupe des autom. de la droite affine $\mathbb C$ qui commutent à $\sigma:z\longmapsto\overline z$, est \uline{le groupe affine réel}
''',[
('text','top','En fait, les anti-involutions de C ont toutes des pts fixes'),
('text','middle','La surface à bord conforme ... demi-plan'),
('insertion','middle left','sur 𝒳'),
('insertion','middle lower','can.'),
('text','lower','NB Le modèle de X envisagé'),
('deletion','lower','Le; C'),
('display','lower','Hbar={z∈C | Im z≥0}'),
('text','bottom','Le groupe des autom. ... le groupe affine réel')],leads='Explicit claim that every plane anti-involution has fixed points and is an orthogonal reflection in a real affine line; quasi-invariance forces invariance for finite-order automorphisms. Closed half-plane and real affine automorphism group. Check relation to distinction between interior and doubled hyperbolicity without silently identifying metric families.')

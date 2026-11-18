import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(41,r'''\mspage{15}
% archive foliation: 43
Si $X$ est une surface conforme hyperbolique, alors la métrique canonique hyperbolique sur $X^{or}$ se descend en une métrique hyperbolique sur $X$, pour laquelle le bord est géodésique.

Plus généralement, chaque fois que $X^{or}$ est muni d'une métrique canonique, invariante par autom. conformes [ou seulement par anti-involutions, ce qui est le cas aussi si $X^{or}\simeq\mathbb C$] alors celle-ci se descend à $X$, avec bord géodésique.

Quand $X$ est sans bord, \deleted{\unsure{alors si elle}} alors \deleted{\unsure{si}} la métrique obtenue sur $X$ est celle déjà envisagée --- \deleted{\unsure{elle}} \inserted{il y en a} dans tous les cas, sauf $X\simeq\mathbb P^1_{\mathbb C}$. On fera attention cependant que lorsque $X$ est le plan projectif réel, la deuxième prescription sans plus ne fournit \uline{pas} de métrique --- elle le fait si on exige que la métrique sur $X^{or}$ soit en $R(X^{or})$, \uline{et} stable par $\sigma$ (ce qui la détermine sans ambiguïté). \deleted{De $=$} \inserted{\deleted{Dans le} En sens inverse}, dans le cas $X\simeq\mathbb C$, $X^{or}\simeq\mathbb C\amalg\mathbb C$, le procédé direct donne une classe des métriques (mod cte), la deuxième
''',[
('text','top','Si X est une surface conforme hyperbolique'),
('text','middle','Plus généralement ... anti-involutions'),
('text','middle to bottom','Quand X est sans bord ... la deuxième'),
('deletion','middle','alors si elle; si; elle'),
('insertion','middle','il y en a'),
('deletion','lower','De =; Dans le'),
('insertion','lower','En sens inverse')],leads='Descent of a canonical metric from the conformal double gives geodesic boundary. Explicit qualification for the real projective plane: require membership in R(Xor) and sigma invariance. The plane case continues on042; do not infer an omitted metric. Need context matching doubling/canonical metrics/geodesic boundary.')

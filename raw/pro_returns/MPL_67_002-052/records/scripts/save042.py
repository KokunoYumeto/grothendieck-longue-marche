import sys
sys.path.insert(0,'MPL_67_002-052/records')
from save_page import save
save(42,r'''\mspage{16}
% archive foliation: 44
ne donne quelque chose que si on la complète par la prescription que l'on prend une métrique ``distinguée'' sur $X^{or}$ qui soit stable par $\sigma$.

Considérons maintenant les seuls cas nouveaux --- ceux où $X$ est 0-connexe et $\partial X\ne\varnothing$, correspondant à un $X^{or}=\mathcal X$ connexe, munie d'une anti-involution $\sigma$ telle que $\mathcal X^\sigma\ne\varnothing$. Les seuls cas problématiques pour l'existence d'une métrique canonique sur $X$, sont les suivants :

a') $\mathcal X\simeq\mathbb C$. \deleted{Les} \inserted{OPS} $\mathcal X=\mathbb C$. Les anti-aut. de $\mathbb C$ sont
\[
z\longmapsto a\overline z+b\qquad(a\in\mathbb C^*,\ b\in\mathbb C).
\]
Si on prend une anti-involution à pts fixes, OPS que 0 est pt fixe, donc $b=0$; donc \deleted{l'application est $z\longmapsto a\overline z$}
\[
\sigma z=a\overline z\qquad\text{avec }a\overline a=1\quad\text{i.e }|a|=1\quad\text{i.e }a\in\mathbb U
\]
(pour avoir $\sigma^2=\mathrm{id}$) soit
\deleted{l'ens des pts fixes est}
\[
\sigma z=\alpha^2\overline z=\frac\alpha{\overline\alpha}\overline z\qquad\text{si }a=\alpha^2,\quad\alpha\in\mathbb U,
\]
et l'ens des pts fixes est
\[
\mathbb C^\sigma=\alpha.\mathbb R.
\]
\margin{symétrie p.r. à la droite $\alpha.\mathbb R$}
''',[
('text','top','ne donne quelque chose ... métrique distinguée'),
('text','middle','Considérons ... X^{or}=𝒳; 𝒳^σ≠∅'),
('text','lower middle','a′) 𝒳≃C ... anti-aut.'),
('deletion','lower middle','Les'),
('insertion','lower middle','OPS'),
('display','lower middle','z↦a zbar+b; a∈C*,b∈C'),
('text','lower','Si on prend une anti-involution à pts fixes'),
('deletion','lower','l’application est z↦a zbar'),
('display','lower','σz=a zbar; a abar=1; |a|=1; a∈U'),
('text','lower','pour avoir σ²=id; soit'),
('deletion','lower','l’ens des pts fixes est'),
('display','bottom','σz=α² zbar=α/αbar zbar; a=α²,α∈U'),
('text','bottom','et l’ens des pts fixes est'),
('display','bottom','C^σ=α.R'),
('margin note','bottom right','symétrie p.r. à la droite α.R')],leads='Plane anti-involutions explicitly written z↦a zbar+b, after choosing a fixed origin a abar=1 and C^sigma=alpha R for a=alpha²; potentially checks earlier scan036 formula without changing that reading. New script X denotes the connected double. No proof check yet; literal coordinate calculation only transcribed.')

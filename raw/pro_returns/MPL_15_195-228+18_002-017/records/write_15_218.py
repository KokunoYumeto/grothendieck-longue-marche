from record_page import save
save(15,218,'reused_typed',r'''
\mspage{217}
1 -- 47 -- \hfill n° 413

16. \uline{Mesure de Haar d'une variété de groupe}.

Conservons les notations de la fin du n° précédent. L'espace $\Omega_e^n(G)$ est alors
de dimension 1 et il en résulte que \uline{l'espace des formes différentielles invariantes
à gauche et de degré} $n=\dim G$ \uline{est de dimension} 1. On en obtient une \uline{base} en
prenant une base $\omega_1,\ldots,\omega_n$ de $\Omega_e^1(G)$ et en prenant le produit extérieur des
formes $I_{\omega_k}^g$. Avec les notations de (30), on obtient en prenant $\omega_k=dx_k$, l'expression
d'une forme invariante à gauche $I_\omega^g$ de degré maximum au voisinage de $e$ :
\[
\tag{31} I_\omega^g(x)=(\text{dét }\partial m_k/\partial y_j(x^{-1};x))\,dx_1\ldots dx_n.
\]
D'autre part, il est clair que l'espace des formes différentielles invariantes
à gauche est invariant par translations à droite. Il existe donc une fonction de
classe $C^{r-1}$ sur $G$, soit $\delta$, telle que :
\[
\tag{32} I_\omega^g(xy)=\delta(y)I_\omega^g\qquad(x,y\in G,\ \omega\in\Omega_e^n(G)).
\]
Mais on a $\delta(y)I_\omega^g=I_\omega^g(xy)=I_\omega^g(y^{-1}xy)=I_{\omega'}^g$ avec $\omega'=(\operatorname{ad}y^{-1})_*(\omega)$. D'où :
\[
\tag{33} \delta(y)=(\text{dét }\operatorname{ad}y)^{-1}.
\]
Supposons maintenant que $K$ soit \uline{localement compact} et soit $\omega\in\Omega_e^n(G)$.
Il est clair que la mesure $\mu=|I_\omega^g|$ est une \uline{mesure de Haar à gauche} sur le groupe
localement compact $G$. Avec les notations de (30) et (31), on a donc pour $x$ voisin
de $e$ :
\[
\tag{34} d\mu(x)=\operatorname{mod}(\text{dét }\partial m_k/\partial y_j(x^{-1};x)))\,dx_1\ldots dx_n
\]
où mod est le \uline{module} du corps localement compact $K$ (Int. VII, § 1, n° 10 et F. R. V.).
D'autre part, (32) et (33) montrent que le \uline{module} du groupe localement compact $G$
(Int. VII, § 1, n° 3, déf. 3) n'est autre que
\[
\tag{35} \Delta(y)=\operatorname{mod}(\delta(y))=\operatorname{mod}(\text{dét }\operatorname{ad}y)^{-1}.
\]
''',[
('text','typed header','1 - 47 -; n° 413'),
('text','typed upper','16. Mesure de Haar d’une variété de groupe'),
('text','typed upper','Conservons les notations de la fin du n° précédent'),
('display','typed upper-middle','(31) I_omega^g(x), determinant and coordinate differentials'),
('text','typed middle','D’autre part, il est clair que l’espace'),
('display','typed middle','(32) I_omega^g(xy)=delta(y) I_omega^g'),
('text','typed middle','Mais on a delta(y) I_omega^g'),
('display','typed middle-lower','(33) delta(y)=(det ad y)^-1'),
('text','typed lower','Supposons maintenant que K soit localement compact'),
('display','typed lower','(34) dmu(x)=mod(det partial m/partial y) dx_1 ... dx_n'),
('text','typed bottom','où mod est le module; D’autre part (32) et (33)'),
('display','typed bottom','(35) Delta(y)=mod(delta(y))=mod(det ad y)^-1'),
('text','manuscript bottom left','217')], 'Apparent extra closing parenthesis in printed (34) retained; source ellipses in products retained.')

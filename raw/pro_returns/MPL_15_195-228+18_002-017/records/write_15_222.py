from record_page import save
save(15,222,'reused_typed',r'''
\mspage{221}
-- 9 -- \hfill n° 370

$\mu(f')\ne0$, on a $\mu((D_f-D_{f'})g)=0$ quelle que soit $g\in\mathcal K$ ; remplaçant $g$ par
$(D_f-D_{f'})g$, on obtient $\mu((D_f-D_{f'})^2g)=0$ quelle que soit $g\in\mathcal K^+$, donc
$D_f=D_{f'}$ puisque le support de $\mu$ est $G$. Posons donc $D_f=D$. La formule (14)
donne
\[
\tag{17} \mu(f)D(e)=\check\nu(f).
\]
La formule (17) s'étend par linéarité aux $f\in\mathcal K$ telles que $\mu(f)=0$. On a
$D(e)\ne0$ puisque $\check\nu\ne0$. Ceci établit bien la proportionnalité de $\mu$ et $\check\nu$.

COROLLAIRE.-- \uline{Toute mesure complexe invariante à gauche} (resp. \uline{à droite}) \uline{sur} $G$
\uline{est proportionnelle à une mesure de Haar à gauche} (resp. \uline{à droite}).

\uline{Exemple} 1.-- Sur le groupe additif $\mathbb R$, la mesure de Lebesgue $dx$ est une mesure
de Haar (Chap. III, § 2, n° 2, exemple).

\uline{Exemple} 2.-- Pour toute fonction $f\in\mathcal K(\mathbb R_+^*)$, on a (Fonct. var. réelles, chap.
II, § 1, formule (13))
\[
\int_0^{+\infty}\frac{f(x)}x\,dx
=\int_0^{+\infty}\frac{f(tx)}{tx}\,t\,dx
=\int_0^{+\infty}\frac{f(tx)}x\,dx
\]
quel que soit $t>0$ ; la mesure $x^{-1}dx$ est donc une mesure de Haar sur le groupe
multiplicatif $\mathbb R_+^*$.

\uline{Exemple} 3.-- Prenons pour $G$ le tore $\mathbb T=\mathbb R/\mathbb Z$. Soit $\varphi$ l'application canonique
de $\mathbb R$ sur $\mathbb T$. Pour $f\in\mathcal K(\mathbb T)$, la fonction $f\circ\varphi$ est continue et périodique de
période 1 sur $\mathbb R$, et l'intégrale $I(f)=\int_a^{a+1}f(\varphi(x))dx$ est indépendante du
choix de $a\in\mathbb R$ ; il est immédiat qu'elle est invariante par translation ; elle
définit donc une mesure de Haar sur $\mathbb T$. Par transport de structure, on en
déduit que $I(f)=\int_a^{a+1}f(e^{2\pi it})dt$ est une mesure de Haar sur le groupe multiplicatif
$\mathbb U$ des nombres complexes de valeur absolue 1 (Top. géné., chap. VIII,
§ 2, n° 1).

PROPOSITION 1.-- \uline{Soient} $G$ \uline{un groupe localement compact}, $\mu$ \uline{une mesure de Haar à
gauche ou à droite sur} $G$. \uline{Pour que} $G$ \uline{soit discret}, \uline{il faut et il suffit que}
''',[
('text','typed header','- 9 -; n° 370'),
('text','typed upper','mu(f prime) nonzero; D_f = D_f prime'),
('display','typed upper','(17) mu(f)D(e)=check nu(f)'),
('text','typed upper-middle','La formule (17) s’étend'),
('text','typed middle','COROLLAIRE; toute mesure complexe invariante'),
('text','typed middle','Exemple 1. Groupe additif R'),
('text','typed middle','Exemple 2. f in K(R_+^*)'),
('display','typed middle','three integrals over positive reals'),
('text','typed middle-lower','quel que soit t>0; multiplicatif R_+^*'),
('text','typed lower','Exemple 3. Tore T=R/Z; integral formulas'),
('text','typed bottom','PROPOSITION 1, unfinished sentence'),
('text','manuscript bottom left','221')])

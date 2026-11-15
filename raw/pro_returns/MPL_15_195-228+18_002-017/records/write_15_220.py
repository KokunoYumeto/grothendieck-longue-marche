from record_page import save
save(15,220,'reused_typed',r'''
\mspage{219}
-- 12 -- \hfill n° 370

4) Supposons $G$ unimodulaire. Soit $\mu$ une mesure de Haar sur $G$. On a
\[
\tag{26} \gamma(s)\mu=\delta(s)\mu=\check\mu=\mu.
\]
Si $f$ est $\mu$-intégrable sur $G$, les translatées à gauche et à droite de $f$ sont
$\mu$-intégrables ainsi que $\check f$, et on a
\[
\tag{27} \int f(sx)d\mu(x)=\int f(xs)d\mu(x)=\int f(x^{-1})d\mu(x)=\int f(x)d\mu(x).
\]
Si $A$ est une partie $\mu$-intégrable de $G$, $sA$, $As$ et $A^{-1}$ sont $\mu$-intégrables, et
\[
\tag{28} \mu(sA)=\mu(As)=\mu(A^{-1})=\mu(A).
\]
On a des propriétés analogues pour l'intégrale essentielle.

PROPOSITION 2.-- \uline{S'il existe dans} $G$ \uline{un voisinage compact} $V$ \uline{de} $e$ \uline{invariant par
automorphismes intérieurs}, \uline{alors} $G$ \uline{est unimodulaire}.

En effet, soit $\mu$ une mesure de Haar à gauche sur $G$. On a, pour tout $s\in G$,
$\mu(V)=\mu(s^{-1}Vs)=\Delta_G(s)\mu(V)$, d'où $\Delta_G(s)=1$ puisque $0<\mu(V)<+\infty$.

On en déduit aussitôt :

COROLLAIRE.-- \uline{Si} $G$ \uline{est discret}, \uline{ou compact}, \uline{ou commutatif}, $G$ \uline{est unimodulaire}.

Ceci est d'ailleurs trivial lorsque $G$ est \uline{commutatif}. Notons aussi que, si
$G$ est \uline{discret}, la mesure sur $G$ pour laquelle chaque point est de masse 1 est
évidemment une mesure de Haar à gauche et à droite sur $G$, qu'on appelle mesure
de Haar \uline{normalisée} sur $G$. Si $G$ est \uline{compact}, il existe une mesure de Haar $\mu$ et
une seule sur $G$ telle que $\mu(G)=1$ ; on l'appelle la mesure de Haar \uline{normalisée}
de $G$. Les deux conventions précédentes ne concordent pas lorsque $G$ est à la
fois discret et compact, c'est-à-dire fini ; quand on sera dans ce cas, on
précisera toujours explicitement ce qu'on entend par mesure de Haar normalisée.

Un sous-groupe, un groupe quotient d'un groupe unimodulaire ne sont pas
toujours unimodulaires (§ 2, exerc. 5). Cf., toutefois, le § 2, prop. 10.

$^{*}$Nous verrons plus tard que les groupes de Lie connexes semi-simples ou
nilpotents sont unimodulaires.$^{*}$
''',[
('text','typed header','- 12 -; n° 370'),
('text','typed upper','4) Supposons G unimodulaire'),
('display','typed upper','(26) gamma(s)mu=delta(s)mu=check mu=mu'),
('text','typed upper-middle','Si f est mu-intégrable'),
('display','typed upper-middle','(27) equality of four integrals'),
('text','typed upper-middle','Si A est une partie mu-intégrable'),
('display','typed middle','(28) mu(sA)=mu(As)=mu(A^-1)=mu(A)'),
('text','typed middle','PROPOSITION 2; proof; On en déduit aussitôt'),
('text','typed lower','COROLLAIRE; normalized Haar measure'),
('text','typed bottom','Un sous-groupe, un groupe quotient'),
('text','typed final starred paragraph','Nous verrons plus tard'),
('text','manuscript bottom left','219')])

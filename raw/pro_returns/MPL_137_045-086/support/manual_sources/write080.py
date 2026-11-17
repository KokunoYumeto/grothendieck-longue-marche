import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{80}
% archive foliation: 79
on veut faire abstraction des questions de représentabilité sauf pour les $\Gamma^{\nu_i}(X_i)$)
\[\Gamma^{\nu_1}(X_1)\otimes\cdots\otimes\Gamma^{\nu_r}(X_r)\longleftarrow\Gamma^\nu(X_1,\ldots,X_r)\]
on aura un hom \unsure{fonctoriel en} $M$ dans $P_1$
\[P_\nu(X_1,\ldots,X_r;M)\longleftarrow P_{1,\ldots,1}(\Gamma^{\nu_1}X_1,\ldots,\Gamma^{\nu_r}X_r;M)\]
par composition avec les applications canoniques de $P$
\diagram{\begin{tikzcd}
X_1\arrow[r,"\unsure{\gamma_1}"]&\Gamma^{\nu_1}X_1&\cdots&X_r\arrow[r,"\unsure{\gamma_r}"]&\Gamma^{\nu_r}(X_r)
\end{tikzcd}}
et on suppose que c'est un \inserted{iso}. Moyennant ceci, on a
\[\Gamma^n(X_1\times\cdots\times X_r)\simeq\sum_{\substack{\nu=(\nu_i)\in\mathbb N^r\\\sum\nu_i=n}}\underbrace{\Gamma^{\nu_1}(X_1)\otimes\cdots\otimes\Gamma^{\nu_r}(X_r)}_{=\Gamma^{\nu_1,\ldots,\nu_r}(X_1,\ldots,X_r)}\]
[NB Il suffirait de \unsure{libeller} ces hypothèses relatives $r=\unsure{n|2}$ --- pour $r=2$ d'abord, et les déduire ensuite pour $r$ quelc.

En particulier on trouve, pour $n=1$, en considérant le produit $X\times0$, pour $1=\Gamma^0(0)$
\[\deleted{\Gamma^1(X\times1)\simeq}\]
\[X\otimes1\simeq\Gamma^1(X)\otimes\Gamma^0(0)\simeq\underbrace{\Gamma^{1,0}(X,0)\simeq X}_{\text{car }P_{1,0}(X,0;M)\simeq P_1(X,M)}\]
et donc $1\otimes X\simeq X$. \deleted{\unsure{N.B. on a aussi}} \deleted{$\unsure{X\otimes1}$}

On suppose qu'il y a des produits tensoriels stricts dans les \unsure{$P_1$ en jeux}, et que les $\Gamma^nX$ satisfont à \unsure{la condition} plus haut.
\margin{\unsure{formant une} \unsure{catégorie} \unsure{rigide}}
'''
e=[('text','top','on veut faire abstraction'),('display','upper','Gamma^nu1(X1) tensor ... leftarrow Gamma^nu'),('text','upper','on aura un hom'),('display','upper','P_nu ... leftarrow P_1,...,1'),('text','upper-middle','par composition'),('diagram','middle','X1 -> Gamma^nu1 X1 ... Xr -> Gamma^nur Xr'),('text','middle','et on suppose'),('insertion','above middle line','iso'),('display','middle','Gamma^n(X1 times ... times Xr) = sum'),('text','below middle','NB Il suffirait'),('text','lower','En particulier'),('deletion','lower above display','Gamma^1(X times 1) iso'),('display','lower','X tensor 1 iso Gamma^1(X) tensor Gamma^0(0)'),('text','lower','et donc 1 tensor X iso X'),('deletion','lower right','N.B.'),('deletion','lower center','X tensor 1'),('text','bottom','On suppose qu’il y a'),('margin note','left bottom oblique','formant une catégorie rigide')]
save(80,text,e)

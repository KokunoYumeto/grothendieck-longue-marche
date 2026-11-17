from save_page import save_page
save_page(93,r'''\scanpage{93}
% archive foliation: 92
\deleted{\unsure{somme|sommes}} en groupant suivant les valeurs absolues
des zéros et pôles\ldots. Lorsque $X$ est
complet et lisse, \inserted{et $F$ \unsure{localement tordu|constant tordu}, de poids $\rho$,}
on a $\uline{h}^i(F)=H^{i-\rho}_!(\bar X,\bar F)$
comme $\mathbf N$-modules, donc on a la
connaissance de $L(X,F)$ équivaut à celle des
$H^{\unsure{i-\rho|i}}(\bar X,\bar F)$ et l'opération du Frobénius dedans.

\deleted{
\diagram{\begin{tikzcd}
X \arrow[r,dash] \arrow[d] & X_{(\unsure{\eta})}\arrow[d,dash]\\
Y \arrow[r,dash] & K
\end{tikzcd}}
$K=$ corps des fonctions de $Y$

Soit $f:X\mathbin{-}Y$ morphisme
[non propre] avec $X,Y$ algé-
briques de type fini sur $\mathbf F_p$.
Considérons les ouverts
denses $U$ de $Y$, et
les $L(f^{-1}(U),F)$. Pour $U$ variable, les
fonctions rationnelles
}

Considérons, d'autre part \inserted{[pour $X$ de dim $n$]}
les ouverts \deleted{denses} $U$ de $X$, \inserted{tels que $X-U$ de dim $<n$,} et les
$L(U,F\vert U)$, qui ne diffèrent \deleted{que} (pour $F$ pur
de poids $\rho$) que par des fonctions rationnelles
de poids $\le2n-2+\rho$. Donc, à priori la
\margin{les poids ici sont pour la bonne filtration \deleted{\unsure{voir}} N°12}
connaissance de l'invariant birationnel
$L(X,F)$ mod. fonct. rat. de poids $\le2n-2+\rho$,
''',[
('top','text','en groupant suivant les valeurs absolues des zéros et pôles'),
('upper','text','Lorsque X est complet et lisse; F localement/constant tordu de poids rho'),
('upper','formula','h^i(F)=H^{i-rho}_!(Xbar,Fbar)'),
('upper-middle','text','comme N-modules; connaissance de L équivaut aux H et à l’opération du Frobénius'),
('middle-left','diagram','Cancelled square X—X_eta over Y—K, downward left arrow, other plain edges'),
('middle-left','text','Cancelled K=corps des fonctions de Y'),
('middle-right','text','Cancelled Soit f:X-Y morphisme [non propre], X,Y algébriques de type fini'),
('middle','text','Cancelled ouverts denses U de Y, L(f^-1(U),F), fonctions rationnelles'),
('lower','text','Considérons d’autre part les ouverts U de X'),
('lower','formula','L(U,F|U); fonctions rationnelles de poids <=2n-2+rho'),
('lower-left margin','margin note','les poids ici sont pour la bonne filtration; N°12'),
('bottom','text','connaissance de l’invariant birationnel L(X,F) mod. fonct. rat. de poids <=2n-2+rho')
],remarks='Whole and both halves read; cancelled right-hand text and diagram inspected, top inserted condition and lower-left note enlarged/rotated. All of the large cancelled block retained. First corrected h exponent retains i-rho as ink.')

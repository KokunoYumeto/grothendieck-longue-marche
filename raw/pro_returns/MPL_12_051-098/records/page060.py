from save_page import save_page
save_page(60,r'''\scanpage{60}
\mspage{15}
% archive foliation: 59
\uline{Cohomologie absolue}

En plus des foncteurs cohomologiques de motifs $\mathbf{R}^{*}f_*$ [$f$ morphisme de type fini] il y a lieu de considérer également les foncteurs ``absolus''
\[
H^*(X,M)=(H^i(X,M))_i.
\]
$M$ motif variable sur $X$, qui doivent provenir d'un foncteur de catégories triangulées
\diagram{\begin{tikzcd}
\mathbf{R}\Gamma_X:\ D^b(\unsure{M^*}(X)) \arrow[r] & D^b(\mathrm{Ab})
\end{tikzcd}}
On veut que les $H^*(X,M)$ et $\mathbf{R}\Gamma(M_\cdot)$ aient les propriétés suivantes

1°) Commutation aux $\varprojlim$ essentiellement affines de préschémas \unsure{qu. cpt} \unsure{qu. sép.}
Cela nous ramène pratiquement aux cas $X$ de type fini sur $\mathbf{Z}$..

2°) Transitivité : Si $f:X\unsure{-|\longrightarrow}Y$ un
''',[
('top','text','15) Cohomologie absolue'),
('upper','text','En plus des foncteurs cohomologiques de motifs'),
('middle','display','H^*(X,M)=(H^i(X,M))_i'),
('middle','text','M motif variable; foncteur de catégories triangulées'),
('lower-middle','diagram','R Gamma_X : D^b(M^*(X)) -> D^b(Ab)'),
('lower-middle','text','On veut que les H^*(X,M) et R Gamma(M_.)'),
('lower','text','1°) Commutation aux lim; préschémas'),
('bottom','text','2°) Transitivité : Si f:X-Y un')],remarks='Whole page and supplied halves inspected against the fragment. The arrow in the unfinished bottom sentence has no clear head; retained with explicit dash/arrow doubt.')

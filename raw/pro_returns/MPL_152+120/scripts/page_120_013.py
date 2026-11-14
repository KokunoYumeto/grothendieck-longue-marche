from record_page import save_page
save_page(120,13,r'''
\mspage{6}
On va introduire
\[
(M6)\quad \deleted{\unsure{\exists f}}\quad
\forall Z,X\in\mathcal M_n,\quad Z\subset X,\quad\exists(f_\alpha)_{\alpha\in A}
\]
famille finie de fonctions modérées $X\longrightarrow R$ et des $(e_\alpha)_{\alpha\in A}$, $e_\alpha\in R_0$, telle que
\[
 Z=\bigcap f_\alpha^{-1}(e_\alpha).
\]
De plus, \unsure{on s.} que les $f_\alpha$ séparent les points de $X\smallsetminus Z$.

\margin{\uline{Prop} $(M6)$, $(M7)$ impliquent l'existence de la somme amalg. \unsure{avec une} \unsure{rétraction} \unsure{libre}.}
\margin{\diagram{\begin{tikzcd}[column sep=small]
X_1&Z\arrow[l,hook']\arrow[r]&X_2
\end{tikzcd}}}

\deleted{Cela implique que l'on peut faire un diagramme \inserted{cart}}
\diagram{\begin{tikzcd}
\deleted{X}\arrow[r,hook]&\deleted{R^n\times R^A}\\
\deleted{Z}\arrow[u,hook]\arrow[r,hook]&\deleted{R^n\times\{e\}}\arrow[u,hook]
\end{tikzcd}}
\deleted{$e=(e_\alpha)_{\alpha\in A}$}

\deleted{Appliquons ceci : $Z_1\unsure{\hookrightarrow|\longleftrightarrow}X_1$ et $Z_2\hookrightarrow X_2$}

\unsure{ce qui est} \uline{équivalent} au fait que le quotient $X/Z$ (contraction de $Z$ en un point) existe dans $\mathcal E$ au sens strict (i.e. $X\mapsto|X|$ y commute). De plus, on suppose
\margin{\unsure{Voir important}}
\[
(M7)\quad\forall Z,X\in\mathcal M_n,\quad Z\subset X,\quad\text{et }\forall
\]
\[
f:Z\longrightarrow R\text{ modérée},\qquad\exists g:X\longrightarrow R\text{ modérée}
\]
qui prolonge

\uline{Proposition} Moyennant $M5,M6,M7$, les sommes amalgamées $X_1\amalg_Z X_2$ ($Z\hookrightarrow X_1$, $Z\hookrightarrow X_2$) existent dans $\operatorname{Esp}_{\mathcal M_*}$, et commutent au foncteur oubli.
\margin{cf généralisation \unsure{aux ensembles} ci-dessous.}
\mspage{12}
''',[
('text','top right','6'),('text','top','On va introduire'),('display','upper','M6 forall Z X'),('deletion','left of M6 condition','exists f'),('text','upper','famille finie de fonctions'),('display','upper','Z intersection inverse images'),('text','upper middle','De plus'),('margin note','upper left oblique','Prop M6 M7 impliquent'),('diagram','left margin','X1 Z X2'),('deletion','middle','Cela implique'),('insertion','right above diagram','cart'),('diagram','middle cancelled','X Rn times RA Z Rn times {e}'),('deletion','right of diagram','e=(e_alpha)'),('deletion','under diagram','Appliquons ceci'),('text','middle lower','ce qui est équivalent'),('margin note','left middle lower','Voir important'),('display','lower','M7 forall Z X'),('display','lower','f Z to R exists g'),('text','lower','qui prolonge'),('text','bottom','Proposition Moyennant M5 M6 M7'),('margin note','bottom left oblique','cf généralisation'),('text','bottom left','12')], observations='Introduces (M6), finite moderate functions constant on Z and separating its complement, and (M7), extension of moderate scalar functions. States existence of amalgamated sums along inclusions under M5–M7. Margin and some connecting words require audit. The cancelled Cartesian diagram is fully retained.')

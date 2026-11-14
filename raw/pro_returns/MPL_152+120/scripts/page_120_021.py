from record_page import save_page
save_page(120,21,r'''
\mspage{20}\mspage{10}
\figure{\begin{tikzpicture}\node[draw,ellipse] {VI};\end{tikzpicture}}
\margin{\uline{Relation avec structure de corps}}
Oublions les structures topologiques, supposons par contre que $R$ ait une \uline{structure de corps}. On supposera alors, \deleted{\unsure{Alrt}} en plus de $(M1)_{\unsure{0}}$ et $(M4)$ (minimum pour construire $\operatorname{Esp}_{\mathcal M_*}$ avec ses $\varprojlim$ finies) l'axiome

\deleted{$(M11)$ \deleted{a) Pour $\forall$} partie modérée $A$ de $R$, l'application $a\mapsto-a$ de $A$ dans $R$ est modérée (i.e. l'ens $\{(a,-a)\in R^2\mid a\in A\}$ est \unsure{modéré})}

\figure{\begin{tikzpicture}\node[draw,rounded corners] {$M11$};\end{tikzpicture}}
a) $0$ et $1$ sont $\in R_0$ i.e. $\{0\},\{1\}\in\mathcal M_1$

b) $\forall A\in\mathcal M_2$, les fonctions
\[
 (x,y)\longmapsto x-y\qquad
 (x,y)\longmapsto xy
\]
\deleted{c) $\forall A\subset R^*$, $A\in\mathcal M_1$, $\exists B\in\mathcal M_1$ tel que $A^{-1}\subset B$}
\margin{\deleted{(\unsure{NB}\ \unsure{OB}\ $B\supset A^{-1}$)}}
sur $A$ sont modérées, \deleted{\unsure{car}} i.e. les deux parties de $R^3$
\[
 \{(x,y,x-y)\mid(x,y)\in A\},\qquad\text{et }\{(\unsure{x|a},y,xy)\mid(x,y)\in A\}
\]
sont modérées.

c) $\forall A\subset R^*$, $A\in\mathcal M_1$, $\exists B\in\mathcal M_1$ avec $A^{-1}\subset B$ \unsure{(NB $B=A^{-1}$)}.

\deleted{\unsure{Et axiome}} \deleted{\unsure{les parties a) b)}} \inserted{les parties a) b)} équivalent à la validité de la

\margin{\uline{NB} Si $R\in\mathcal M_1$, il suffit de prendre $(M11)$ pour $A=R^2$}

\uline{Proposition} Pour un espace modéré $X$, les fonctions modérées $X\longrightarrow R$ \deleted{\unsure{est = un sous $R_0$}} forment un \uline{sous-anneau} de l'anneau des fonctions scalaires sur $X$. En particulier, $R_0$ est un sous-corps de $R$, et les anneaux
\margin{de fonctions mod. \unsure{sont} des $R_0$-algèbres}
''',[
('text','top left','20'),('text','top right','10'),('drawing','top left','circled VI'),('margin note','upper left','Relation avec structure de corps'),('text','upper','Oublions les structures'),('deletion','after alors','Alrt'),('text','upper middle','l’axiome'),('deletion','middle large block','M11 a) Pour toute partie'),('deletion','inside cancelled block','a) Pour tout'),('drawing','middle lower','boxed M11'),('text','a','0 et 1 sont in R0'),('text','b','pour tout A in M2'),('display','b','(x,y) to x-y and xy'),('deletion','between b lines','c) forall A subset R*'),('margin note','right of deleted c','NB OB B contains inverse A'),('text','b continued','sur A sont modérées'),('deletion','b after modérées','car'),('display','b graphs','two subsets of R3'),('text','c','forall A subset R*'),('deletion','after c','Et axiome'),('deletion','after c','les parties a) b)'),('insertion','above proposition','les parties a) b)'),('text','above proposition','équivalent à la validité'),('margin note','left oblique','NB Si R in M1'),('text','lower','Proposition Pour un espace modéré'),('deletion','under functions','est = un sous R0'),('margin note','bottom left vertical','de fonctions mod. sont des R0-algèbres')], observations='Section VI forgets topology and introduces a field structure on R. M11 is revised in place: constants 0 and 1, difference and product, and an inverse-image boundedness/existence clause c. Several cancelled lines around c are heavily overwritten; keep low confidence. Claims ring of scalar moderate functions and R0 a subfield.')

from record_page import save_page
save_page(120,12,r'''
En effet, si $Y$ est un espace modéré, une \deleted{\unsure{flèche}} flèche du syst. inductif $(X_i)$ (dans $\mathcal E$) dans $Y$, \inserted{$(f_i:X_i\longrightarrow Y)_{i\in I}$}, équivaut à la donnée d'une application $f:X\longrightarrow Y$, telle que les $f\circ g_i$ soient modérées. Il nous reste à prouver que cela implique que $f$ est modérée, i.e. que son graphe $\Gamma_f\subset X\times Y$ est une partie modérée. Or $X$ étant la réunion des images des $X_i$, il en est que $\Gamma_f$ est la réunion des images des $\Gamma_{f_i}\subset X_i\times Y$ par
\[
 X_i\times Y\xrightarrow{g_i\times\operatorname{id}_Y}X\times Y.
\]
Mais ces images sont modérées, et \deleted{donc} leur réunion aussi.

\uline{Cor} Soit $f:X\longrightarrow Y$ application modérée, $\mathcal R_f$ la relation d'équivalence définie par $f$ (qui est donc une partie modérée de $X\times X$, et est une $\mathcal E$-relation d'équivalence). Alors $X/\mathcal R_f$ existe dans $\mathcal E=\operatorname{Esp}_{\mathcal M_*}$, et est \inserted{can} isomorphe à $f(X)$ (avec structure induite)

\deleted{\uline{Cor. 2} Considérons}
\diagram{\begin{tikzcd}[column sep=small]
&\deleted{Z}\arrow[dl,"\deleted{i_1}"']\arrow[dr,"\deleted{i_2}"]&\\
\deleted{X_1}&&\deleted{X_2}
\end{tikzcd}}
\deleted{dans $\mathcal E$.}
\mspage{11}
''',[
('text','upper','En effet si Y'),('deletion','second line','flèche'),('insertion','above équivaut','(fi:Xi to Y)'),('text','middle','Il nous reste à prouver'),('display','middle lower','Xi times Y to X times Y'),('text','middle lower','Mais ces images'),('deletion','after et','donc'),('text','lower','Cor Soit f'),('insertion','above isomorphe','can'),('deletion','bottom','Cor. 2 Considérons'),('diagram','bottom cancelled','Z i1 i2 X1 X2'),('deletion','bottom right','dans E'),('text','bottom left','11')], observations='Proof by expressing the graph as a finite union of images of the component graphs; quotient corollary for the equivalence relation defined by a moderate map. Cancelled Cor. 2 diagram at bottom retained.')

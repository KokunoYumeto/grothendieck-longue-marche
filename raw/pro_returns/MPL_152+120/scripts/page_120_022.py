from record_page import save_page
save_page(120,22,r'''
De $=$ pour $X$ un espace ind-modéré, p.ex. (si $R$ est réunion de ses parties modérées $(M8)$ i.e. \inserted{les $R^I$} sont des espaces ind-modérés) pour les fonctions ind-modérées sur les $R^I$, qui contiennent en tous cas les \deleted{ensembles} anneaux de polynômes $R_0[(X_i)_{i\in I}]$ en les fonctions coordonnées.

\margin{Donc les applications $R_0$-polynomiales \deleted{\unsure{entre}} \deleted{\unsure{transfont}} $R^I$ sont modérées, et transfont des parties modérées en \unsure{itou}.}

\uline{Corollaire} Soit $f$ une fonction modérée sur l'espace modéré $X$. Alors $f$ est inv. \unsure{(dans|dans} l'anneau des fonctions modérées ssi $f$ ne s'annule pas dans $X$.

En considérant $f(X)\subset R^*$, cela revient au

\uline{Corollaire} Soit $A\subset R^*$, $A\in\mathcal M_1$, alors la restriction de $x\mapsto x^{-1}$ à $A$ est modérée, i.e. l'ens des $(x,x^{-1})\in R^2$, $x\in A$, est $\in\mathcal M_1$.
\mspage{21}
''',[
('text','upper','De = pour X'),('insertion','above sont','les R^I'),('deletion','before anneaux','ensembles'),('margin note','right middle','Donc les applications R0-polynomiales'),('deletion','inside margin','entre'),('deletion','inside margin','transfont'),('text','middle lower','Corollaire Soit f'),('text','lower','En considérant f(X)'),('text','lower','Corollaire Soit A subset R*'),('text','bottom left','21')], observations='Moderate scalar functions on ind-spaces; contains polynomial coordinate rings. Unit criterion for moderate functions, reduced to inversion on a moderate A subset R*. Last graph-membership index visibly reads M1, retained rather than changed to M2.')

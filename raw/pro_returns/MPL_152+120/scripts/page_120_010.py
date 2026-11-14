from record_page import save_page
save_page(120,10,r'''
Axiome supplémentaire
\[
 (M5)\quad \forall n,\quad \mathcal M_n\text{ stable par réunions finies}
\]
\[
 (\Longleftrightarrow\ \varnothing\in\mathcal M_n,\ \deleted{\unsure{\delta}}\text{ et }A,B\in\mathcal M_n\Longrightarrow A\cup B\in\mathcal M_n)
\]
\uline{Proposition} Parties modérées d'un esp. mod. stable par réunions finies.

\uline{Proposition} Sur $\varnothing$ il $\exists$ une structure modérée unique, qui en fait objet initial de $\operatorname{Esp}_{\mathcal M_*}$.

\uline{Proposition} Soit $X$ un espace modéré, $(X_i)_{i\in I}$ une famille finie de parties modérées de $X$. Alors $\bigcup X_i$ est une partie modérée de $X$. Si $X=\bigcup_iX_i$, alors $X$ est somme amalgamée des $X_i$ suivant les $X_i\cap X_j$ --- une application $f:X\longrightarrow Y$ \inserted{entre espaces modérés} est modérée ssi ses restrictions aux $X_i$ le sont.

\uline{Question} Donnons-nous
\diagram{\begin{tikzcd}[column sep=small]
&\unsure{Y|Z}\arrow[dl]\arrow[dr]&\\
X_1&&X_2
\end{tikzcd}}
dans $\operatorname{Esp}_{\mathcal M_*}$, existe-t-il une somme amalgamée ? Si $Y=\varnothing$, c'est la question de l'existence des sommes finies dans $(\operatorname{Esp}_{\mathcal M_*})$.
\mspage{9}
''',[
('text','top','Axiome supplémentaire'),('display','upper','M5 finite unions'),('display','upper','equivalence emptyset and unions'),('deletion','inside second display','delta'),('text','upper middle','Proposition Parties modérées'),('text','upper middle','Proposition Sur emptyset'),('text','middle','Proposition Soit X'),('insertion','above f is moderate','entre espaces modérés'),('text','lower','Question Donnons-nous'),('diagram','lower','Y to X1 and X2'),('text','bottom','dans Esp existe-t-il'),('text','bottom left','9')], observations='Introduces additional axiom (M5), finite unions. A question asks for amalgamated sums, with the empty-source case identified with finite sums. No external identification made here.')

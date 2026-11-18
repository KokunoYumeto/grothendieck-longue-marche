from save_page import save
save(20,r'''\scanpage{20}
\mspage{2}

\margin{$\Vert$}
On voudrait que sous ces conditions
\diagram{\begin{tikzcd}[column sep=large]
\displaystyle\int\!\begin{gathered}Y\longrightarrow X\\\downarrow\hspace{1.4cm}\\Y'\hspace{1.4cm}\end{gathered}\arrow[r]&X'=\varinjlim\left(\begin{gathered}Y\mathbin{\text{---}}X\\\downarrow\hspace{1.4cm}\\Y'\hspace{1.4cm}\end{gathered}\right)=X\amalg_Y Y'
\end{tikzcd}}
soit $\in\underline W$, et \unsure{$\equiv$|même} qu'il soit coasphérique.

Les conditions sont \deleted{elles} stables par \uline{tout} chgt de base sur $X'$.

\diagram{\deleted{\begin{tikzcd}[column sep=small,row sep=small]
&Y\arrow[rr,hook,"i"]\arrow[dd,"g"]&&X\arrow[dd]\\
\unsure{Y_1}\arrow[ur]\arrow[rr]\arrow[dd]&&\unsure{X_1}\arrow[ur]\arrow[dd]&\\
&Y'\arrow[rr,hook]&&X'\\
Y'_1\arrow[ur]\arrow[rr,hook]&&X'_1\arrow[ur]&
\end{tikzcd}}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\int(i,g)\arrow[r,dash]&X'\\
\int(i_1,g_1)\arrow[u]\arrow[r]&X'_1\arrow[u]
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&Y\arrow[rr,hook,"i"]\arrow[dd,"g"]&&X\arrow[dd,"f"]\\
Y_1\arrow[ur]\arrow[rr,"i_1"']\arrow[dd,"g_1"']&&X_1\arrow[ur]\arrow[dd,"f_1"]&\\
&Y'\arrow[rr,hook,"i'"']&&X'\\
Y'_1\arrow[ur]\arrow[rr,dash,"i'_1"']&&X'_1\arrow[ur]&
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&&Y\arrow[r,dash,"i"]\arrow[dd,"g"]&X\arrow[dd]\arrow[dll,dash]\\
Y_1\arrow[urr,dash]\arrow[r,"i_1"']\arrow[dd,"g_1"']&X_1\arrow[dd]&&\\
&&Y'\arrow[r,dash,"i'"']&X'\arrow[dll,dash]\\
Y'_1\arrow[urr]\arrow[r,dash,"i'_1"']&X'_1&&
\end{tikzcd}}

Ce diagramme est-il cartésien ? À vérifier ! Si oui, cela signifierait que $\int(i,g)\longrightarrow X'$ est \uline{universellement} dans $\underline W$.

\margin{$\Vert\,|$}
Mais on vérifie directement que
\[
\int(i,g)\longrightarrow X'\quad\text{est \uline{cofibré} à fibres $\underline W$-asphériques}
\]

en fait, fibres sont
\[
\begin{aligned}
&\simeq e_{u'}\quad\text{pour }\unsure{x=u'}\in U'\\
&\simeq\underbrace{C(Y_{y'})}_{\substack{\text{\unsure{ajouter} élément}\\\text{final : }Y_{y'}\,!}}\quad\text{pour }x=y'\in Y'
\end{aligned}
\]
% archive foliation: 19
''','text',[
('text','top author number','2 circled'),('margin note','left upper double rule','double vertical emphasis'),('text','top','On voudrait que sous ces conditions'),('diagram','upper display','integral span→X prime=colimit span=pushout'),('text','under upper diagram','soit in W et equivalence/même qu il soit coasphérique'),('text','upper middle','Les conditions sont stables par tout chgt de base'),('deletion','upper middle','elles'),('diagram','middle left cancelled cube','Y X Y prime X prime Y1 X1 Y1 prime X1 prime'),('deletion','middle left','whole preliminary cube'),('diagram','middle central square','integral(i,g) dash X prime; integral(i1,g1)→X1 prime'),('diagram','middle right upper cube','i g f; i1 g1 f1; base-change cube'),('diagram','middle right lower cube','alternative perspective on base-change cube'),('text','lower middle','Ce diagramme est-il cartésien ? À vérifier !'),('text','lower middle continuation','Si oui cela signifierait universellement dans W'),('margin note','lower left triple rule','triple vertical emphasis'),('text','bottom','Mais on vérifie directement que'),('display','bottom','integral(i,g)→X prime est cofibré à fibres W-asphériques'),('text','bottom explanation','en fait fibres sont'),('display','bottom fiber cases','e_u prime for x=u prime; C(Y_y prime) for x=y prime'),('insertion','underbrace under C(Y_y prime)','ajouter élément final : Y_y prime !')],
'Explicit self-check: “Ce diagramme est-il cartésien ? À vérifier !”. The following direct argument asserts the comparison is cofibered with W-aspheric fibers and identifies the fibers. The two surviving cubes are separately transcribed, as is the crossed preliminary cube; directions of the light perspective edges are least secure. An integral sign denotes the span construction and is not silently replaced by a homotopy-colimit notation.')

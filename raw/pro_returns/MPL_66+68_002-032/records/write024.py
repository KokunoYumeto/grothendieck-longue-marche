from record_page import record
record(24,r'''\scanpage{24}
\uline{Jeux de position}

a) $C$ ensemble des ``\uline{configurations}'' ou ``\uline{positions}''

b) $R\subset C\times C$, interprété comme $x\longmapsto R(x)$
\margin{$C\longrightarrow\mathcal P(C)$}
\[
\text{d'où}\qquad C_0=\{x\in C\mid R(x)=\varnothing\}\subset C
\]
\margin{(conf. \uline{terminales})}

c) $J$ ensemble des ``\uline{joueurs}''

d) $C\setminus C_0\xrightarrow{\alpha}J$ On dit que (si $x\in C\setminus C_0$) $j=\alpha(x)$ est le joueur qui a \uline{l'initiative} dans la position $x$.
\inserted{\[
C(j)=\{x\in C\setminus C_0\mid\alpha(x)=j\}\qquad
\bar C(j)=(C\setminus C_0)\setminus C(j)
\]}

e) $J\longrightarrow\mathcal P(C_0)\qquad j\longmapsto G_0(j)$ (ens. des \uline{positions terminales gagnantes pour $j$})

\uline{Partie}\quad $(x_0,x_1,\ldots,x_n,\ldots)$ suite finie ou infinie de positions, telle que pour deux termes consécutifs $x_i,x_{i+1}$, on ait
\[
x_{i+1}\in R(x_i)
\]
\margin{ne dépend que de $C,R$}

\uline{Prolongement} des parties --- parties non prolongeables ou ``\uline{terminées}'' : ce sont les parties qui sont soit infinies, soit finies, avec \deleted{\unsure{une}} \inserted{la} position finale $x_n\in C_0$.
\margin{Composition des parties (Associativité --- on a une ``catégorie des positions''\ldots)}

\uline{Partie gagnée pour $j$} : partie finie (non prolongeable) dont la position finale $x_n$ est $\in G_0(j)$.
\margin{ne dépend que de $C,R$ et $G_0(j)\subset C_0$}
\margin{\uline{NB} \deleted{Si} $XY$ est gagnée pour $j$, \deleted{\unsure{donc}} $\Longleftrightarrow Y$ est gagnée pour $j$.}

\uline{Stratégie $\Sigma$/pour $j$} (ou $j$-Stratégie) : Application
\[
\Sigma:C(j)\longrightarrow\mathcal P(C)
\]
telle que $\forall x\in C(j)$, on ait
% archive foliation: 23
''',[
('text','heading','Jeux de position'),
('text','upper','a) C ensemble des configurations ou positions'),
('text','upper','b) R⊂C×C interprété comme x↦R(x)'),
('margin note','upper right','C→P(C)'),
('display','upper','C_0={x∈C | R(x)=∅}⊂C'),
('margin note','upper right','conf. terminales'),
('text','upper middle','c) J ensemble des joueurs'),
('text','middle','d) C\C_0→αJ ... initiative'),
('insertion','middle left','C(j)={x∈C\C_0|α(x)=j}; bar C(j)=(C\C_0)\C(j)'),
('text','middle','e) J→P(C_0), j↦G_0(j), ens. des positions terminales gagnantes pour j'),
('text','middle lower','Partie (x_0,x_1,...), suite finie ou infinie ...'),
('display','middle lower','x_{i+1}∈R(x_i)'),
('margin note','left middle lower','ne dépend que de C,R'),
('text','lower','Prolongement des parties ... terminées ...'),
('deletion','lower','une'),
('insertion','lower','la'),
('margin note','lower right','Composition des parties ... catégorie des positions'),
('text','lower','Partie gagnée pour j ...'),
('margin note','left lower','ne dépend que de C,R et G_0(j)⊂C_0'),
('margin note','bottom right','NB XY est gagnée ... iff Y ...'),
('deletion','within NB','Si; donc'),
('text','bottom','Stratégie Σ/pour j (ou j-Stratégie): Application'),
('display','bottom','Σ:C(j)→P(C)'),
('text','bottom edge','telle que ∀x∈C(j), on ait')
],'''A new “Jeux de position” exposition after the omitted blank scan 23. The initiative map is now alpha on C minus C_0, with C(j) and bar C(j) explicitly excluding terminals; this is not silently unified with the earlier i-based convention. A marginal “catégorie des positions” remark proposes associative composition of plays, and another notes concatenation preserves whether the final play is won. These observations are terse and need a finite-play/endpoint formulation in any research discussion. Title is visible but no authorial page count accompanies it.''')

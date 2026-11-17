from record_page import record
record(10,r'''
\scanpage{10}
% archive foliation: 9
\deleted{\uline{Prop} Soient \unsure{x}\ \unsure{qui}}

On dit que $\uline{x}\in C\deleted{\unsure{(j)}}$ est \uline{acceptable} contre $j'\in J$ si \deleted{$\exists$} (posons $J'=J-\{j'\}$) \deleted{et pour $J'=J-\{j'\}$} $\exists$ $J'$-stratégie $\Sigma$ telle que $\Sigma$ soit acceptable pour $x\in C$ contre $j'$.
\margin{si $x\in C_0$ signifie donc que $x\notin G(j')$.}

Cela implique que $x\notin G(j')$. Car si on avait $x\in G(j')$, \deleted{alors} et si $\Sigma'$ était une $j'$-stratégie $x$-gagnante, alors prenons une partie maximale (à priori finie ou infinie) commençant par $x$ et compatible avec $\Sigma$ et avec $\Sigma'$, cette partie serait finie (car $\Sigma$ est gagnante pour $x$ et $j$), et on aurait (si $x_N$ est l'aboutissement) à la fois $x_N\in G(j')$ et $x_N\notin G(j')$, absurde. Mieux

\uline{Théorème 2} Soient $j'\in J$, $J'=J\setminus\{j'\}$, $x\in C$.

Pour qu'on ait $x\in\overline G(j')$ (i.e. $x\notin G(j')$), il \uline{faut} et il suffit que $x$ soit acceptable contre $j'$.
''',[
('deletion','top','Prop Soient x qui'),('text','upper','On dit que x in C est acceptable contre j prime'),('deletion','upper','(j); exists; et pour J prime=J-{j prime}'),('display','upper inline','J prime=J-{j prime}; exists J prime-stratégie Sigma'),('margin note','upper-left','si x in C_0 signifie donc que x notin G(j prime)'),('text','middle','Cela implique que x notin G(j prime)'),('deletion','middle','alors'),('text','middle-lower','alors prenons une partie maximale ... compatible avec Sigma et Sigma prime'),('text','lower parenthesis','car Sigma est gagnante pour x et j'),('display','lower inline','x_N in G(j prime) et x_N notin G(j prime)'),('text','lower','absurde. Mieux'),('text','bottom heading','Théorème 2 Soient j prime in J ...'),('display','bottom inline','J prime=J\\{j prime}; x in C; x in Gbar(j prime)'),('text','bottom statement','Pour qu’on ait ... il faut et il suffit ... acceptable contre j prime')
],'''Theorem 2 identifies nonwinning positions for j′ with positions acceptable against j′ for the complementary coalition. One direction is proved by a maximal play compatible with both strategies; the winning strategy forces that play to terminate and yields contradictory terminal status. In the parenthetical justification the unprimed Sigma and j are written although Sigma′ and j′ were introduced; preserved without correction. The converse follows later.''')

from record_page import record
record(9,r'''
\scanpage{9}
% archive foliation: 8
pour $j$ \inserted{$\Gamma$-}gagnantes, \deleted{pour tt} $\Sigma$ est la plus grande, i.e. $\Sigma\supset\Sigma'$, i.e. $\forall z\in C(j)$, on a $\Sigma(z)\supset\Sigma'(z)$. Bien évident (puisque $\Sigma'(z)\subset R(z)$) \deleted{\unsure{si $\Sigma$}} dans le cas où $\Sigma(z)=R(z)$, donc quand \deleted{\unsure{on n'a pas simultanément}}\inserted{$z\notin\Gamma$} \deleted{$\exists x\in\Gamma$, avec $z\unsure{\succ|\geq}x$, et $z\in G(j)$.} On peut supposer \deleted{\unsure{ces conditions satisfaites}}\inserted{$z\in\Gamma$}, donc $\Sigma(z)=R(z)\cap G(j)$. Il suffit donc de prouver que $\Sigma'(z)\subset G(j)$, \deleted{\unsure{ce}} ce qui résulte du \uuline{lemme} après la prop.

\deleted{Stratégie}

$4^\circ)$ \uline{Stratégie acceptable}, \uline{positions acceptables}.

$J'$-Stratégie (si $J'\subset J$) \deleted{\unsure{Se}} \unsure{Posons}
\[
C(J')=\bigcup_{j\in J'}C(j),
\]
se définit comme une $j$-stratégie, en y remplaçant $C(j)$ par $C(J')$.
Donc les $j$-stratégies deviennent les $\{j\}$-stratégies.
\margin{\unsure{pour celle}}

Une \deleted{\unsure{telle}} $J'$-stratégie \inserted{$\Sigma'$} est dite \uline{acceptable} (\deleted{pour}\inserted{\uline{contre}} un $j_0\in J$ \inserted{et $x\in C$}) si pour $\forall$ partie \inserted{$(x_0,\ldots,x_N)$} comp. avec $\Sigma$, \deleted{\unsure{avec}}\inserted{partant de $x$}\deleted{\unsure{terminant par}}, et terminée, on a $x_N\notin G(j_0)$
\inserted{i.e. $x_N\notin G_0(j_0)$.}
''',[
('text','top','pour j Gamma-gagnantes; Sigma est la plus grande'),('insertion','top','Gamma-'),('deletion','top','pour tt'),('display','top inline','Sigma superset Sigma prime; forall z in C(j)'),('text','upper','Bien évident (puisque Sigma prime(z) subset R(z))'),('deletion','upper','si Sigma'),('display','upper inline','Sigma(z)=R(z)'),('deletion','upper-middle','on n’a pas simultanément; exists x in Gamma ...'),('insertion','upper-middle','z notin Gamma'),('text','middle','On peut supposer ... donc Sigma(z)=R(z) cap G(j)'),('deletion','middle','ces conditions satisfaites'),('insertion','middle','z in Gamma'),('text','middle','Il suffit donc de prouver ... lemme après la prop.'),('display','middle inline','Sigma prime(z) subset G(j)'),('deletion','middle','ce; Stratégie'),('text','lower heading','4 degrees Stratégie acceptable, positions acceptables'),('text','lower','J prime-Stratégie (si J prime subset J) Posons'),('deletion','lower','Se'),('display','lower','C(J prime)=union_(j in J prime) C(j)'),('text','lower','se définit comme une j-stratégie ...'),('text','lower','Donc les j-stratégies deviennent les {j}-stratégies'),('margin note','lower-right','pour celle'),('text','bottom','Une J prime-stratégie est dite acceptable ...'),('deletion','bottom','telle; pour; avec; terminant par'),('insertion','bottom','Sigma prime; contre; et x in C; tuple; partant de x'),('display','bottom','x_N notin G(j_0); i.e. x_N notin G_0(j_0)')
],'''The greatest-strategy proof uses the successor lemma to bound any other winning strategy inside G(j). Section 4 introduces coalition strategies for J′⊂J and acceptable strategies against j_0, demanding avoidance of j_0-winning terminal outcomes rather than termination. This change is a potentially significant distinction; follow continuation. The definition names Sigma′ but later says Sigma in the compatibility clause; retained as ink.''')

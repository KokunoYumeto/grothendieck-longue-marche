from workflow import save_page
save_page(71,r'''
\scanpage{71}
% archive foliation: 70
Paradigme des courbes algébriques

I\quad Point de vue topologique.

On considère des surfaces topologiques (sans bord) orientables paracompactes \inserted{$X$} -- on se donne aussi un ensemble $\omega$ de cardinal $2$, et on pose
\[
T=\mathbb Z\wedge_{\mathbb Z/2}\omega,
\]
et on suppose donné pour $X$ une $\omega$-orien-\\
tation, i.e. une \inserted{$\mathbb Z/2$-}application \deleted{\unsure{compatible}}\deleted{de $\omega$ dans} l'ens des orientations de $X$, en $\omega$ qui revient au $=$, un isomorphisme du faisceau des entiers tordus sur $X$ avec le faisceau constant $T_X$. On suppose que les composantes connexes $X_i$ de $X$ \deleted{sont}\inserted{est} homéomorphes à un $\widehat X_i\setminus S_i$, où $\widehat X_i$ est une surface compacte, et $S_i$ une partie finie de $\widehat X_i$. On sait que $(\widehat X_i,S_i)$ est détermi-\\
né à isom unique près par $\unsure{X|X_i}$.

(comme le \unsure{décomp.} des compactifiés de Čech
''',[
('text','top','Paradigme des courbes algébriques'),
('text','upper third','I Point de vue topologique'),
('text','upper half','On considère des surfaces topologiques ... un ensemble omega'),
('insertion','above paracompactes','X'),
('display','upper middle','T=Z wedge_{Z/2} omega'),
('text','middle to lower','et on suppose donné pour X une omega-orientation ...'),
('insertion','above application','Z/2-'),
('deletion','following application','compatible; de omega dans'),
('text','lower half','On suppose que les composantes connexes X_i ...'),
('deletion','after de X','sont'),
('insertion','above sont','est'),
('text','lower half','homéomorphes à un Xhat_i minus S_i; On sait ...'),
('text','last line','(comme le décomp. des compactifiés de Čech')])

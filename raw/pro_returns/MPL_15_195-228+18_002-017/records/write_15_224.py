from record_page import save
save(15,224,'reused_typed',r'''
\mspage{223}
\begin{center}-- 7 --\end{center}\hfill n\textsuperscript{o}370

si $f\leq\sum_{i=1}^n c_i\gamma(s_i)g$ avec des $c_i\geq0$, on a $\sup f\leq\sum_{i=1}^n c_i g(s_i^{-1}s)$ pour un $s\in G$, donc $\sup f\leq(\sum_{i=1}^n c_i)\sup g$, d'où (iv). Prouvons (v) ; soient $f\in\mathcal K$, $g,h\in\mathcal K^*_+$ ; si $f\leq\sum_{i=1}^n c_i\gamma(s_i)g$ et $g\leq\sum_{j=1}^p d_j\gamma(t_j)h$ ($c_i,d_j\geq0$, $s_i,t_j\in G$), $f\leq\sum_{i,j}c_i d_j\gamma(s_it_j)h$, donc $(f:h)\leq\sum_{i,j}c_i d_j=(\sum_i c_i)(\sum_j d_j)$ ; donc $(f:h)\leq(f:g)(g:h)$. Si on applique (v) à $f_0,f,g$ d'une part et à $f,f_0,g$ d'autre part, on obtient (vi). Enfin, soient $f,f',h\in\mathcal K_+$ avec $h(s)\geq1$ sur le support de $f+f'$, et soit $\varepsilon>0$. Posons $F=f+f'+\frac12\varepsilon h$ ; les fonctions $\varphi,\varphi'$, qui coïncident respectivement avec $f/F$ et $f'/F$ sur le support de $f+f'$ et qui sont nulles en dehors de celui-ci, appartiennent à $\mathcal K_+$ ; pour tout $\eta>0$, il existe un voisinage compact $V$ de $e$ tel que $|\varphi(s)-\varphi(t)|\leq\eta$ et $|\varphi'(s)-\varphi'(t)|\leq\eta$ pour $s^{-1}t\in V$. Soit alors $g\in\mathcal K^*_+(V)$ ; pour tout $s\in G$, on a $\varphi\mathbin{.}\gamma(s)g\leq(\varphi(s)+\eta).\gamma(s)g$ (en effet, c'est évident aux points où $\gamma(s)g$ s'annule, donc hors de $sV$ ; et, dans $sV$, $\varphi\leq\varphi(s+\eta)$ ; de même, $\varphi'\mathbin{.}\gamma(s)g\leq(\varphi'(s)+\eta).\gamma(s)g$. Ceci posé, soient $c_1,\ldots,c_n$ des nombres $\geq0$ et $s_1,\ldots,s_n$ des éléments de $G$ tels que $F\leq\sum_{i=1}^n c_i\gamma(s_i)g$ ; on a
\[
f=\varphi F\leq\sum_{i=1}^n c_i\varphi\mathbin{.}\gamma(s_i)g\leq\sum_{i=1}^n c_i(\varphi(s_i)+\eta).\gamma(s_i)g
\]
et de même pour $f'$ ; par suite
\[
(f:g)+(f':g)\leq\sum_{i=1}^n c_i(\varphi(s_i)+\varphi'(s_i)+2\eta)\leq(1+2\eta)\sum_{i=1}^n c_i
\]
puisque $\varphi+\varphi'\leq1$. En appliquant la définition de $F$, puis (ii), (iii), et (v), on en conclut
\[
\begin{aligned}
(f:g)+(f':g)&\leq(1+2\eta)(F:g)\leq(1+2\eta)\left[(f+f':g)+\frac12\varepsilon(h:g)\right]\leq\\
&\leq(f+f':g)+\frac12\varepsilon(h:g)+2\eta(f+f':h)(h:g)+\varepsilon\eta(h:g)
\end{aligned}
\]
et, si on a choisi $\eta$ tel que $\eta[2(f+f':h)+\varepsilon]\leq\frac12\varepsilon$, on obtient (vii).

Quand $V$ parcourt l'ensemble des voisinages compacts de $e$, les $\mathcal K^*_+(V)$ forment une base de filtre $\mathfrak B$ sur $\mathcal K^*_+$. Soit $\mathfrak F$ un ultrafiltre sur $\mathcal K^*_+$ plus fin que $\mathfrak B$.
''',[
('text','sheet edge','223'),('text','typed header','– 7 –; n°370'),
('text','upper to middle','si f ≤ sum c_i γ(s_i)g; Prouvons (v)'),
('display','middle','f=φF ≤ sum c_i φ.γ(s_i)g'),
('text','middle','et de même pour f′; par suite'),
('display','middle lower','(f:g)+(f′:g) ≤ sum'),
('text','lower','puisque φ+φ′ ≤ 1'),
('display','lower','(f:g)+(f′:g) ≤ (1+2η)(F:g)'),
('text','lower','et, si on a choisi η'),
('text','bottom','Quand V parcourt ... base de filtre B')
], 'Upside-down reused typescript read after 180-degree rotation, whole and both supplied halves. Printed φ≤φ(s+η) and unclosed prose parenthesis retained.')

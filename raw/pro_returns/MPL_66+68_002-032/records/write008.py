from record_page import record
record(8,r'''
\scanpage{8}
% archive foliation: 7
\unsure{donnée} par la condition, (pour $\forall z\in C(j)$)
\[
\Sigma(z)=\begin{cases}
\text{a)}\ R(z)\text{ si }\deleted{\unsure{\nexists}\text{ partie }(x_0,x_1,\ldots,x_n)\text{ avec }x_0\in\Gamma,\ x_n=z}\ \deleted{\unsure{\nexists}x\in\Gamma,\ \unsure{\text{avec}}\ z\unsure{\succ|\geq}x,\ \text{ou si }z\notin G(j)}\ \inserted{z\notin\Gamma}\\
\text{b)}\ R(z)\cap G(j)\text{ si }\deleted{\exists x\in\Gamma\text{ avec }z\unsure{\succ|\geq}x,\text{ et }z\in G(j)}\ \inserted{z\in\Gamma}
\end{cases}
\]
\deleted{\unsure{bien} (donc $z\in G(j)$)}

\uline{Dém} Prouvons que $\Sigma(z)$ est une stratégie gagnante pour $\forall x\in\Gamma$. C'est une stratégie i.e. $R(z)\ne\varnothing\Longrightarrow\Sigma(z)\ne\varnothing$. Il suffit de regarder le cas \deleted{b) $\exists x\in\Gamma$, avec $z\unsure{\succ|\geq}x$, et $z\in G(j)$}\inserted{$z\in\Gamma$} (sinon $\Sigma(z)=R(z)\ne\varnothing$), alors $\Sigma(z)=R(z)\cap G(j)$, et par le $1^\circ)$ de la prop. on a (puisque $z\notin C_0$ donc $z\notin G_0(j)$) $R(z)\cap G(j)\ne\varnothing$ OK

Prouvons que $\Sigma(z)$ est gagnante pour $\forall x\in\Gamma$. Soit donc une partie \inserted{$(x_0=x,x_1,\ldots,x_{\unsure{N|n}})$} compatible avec $\Sigma$ et maximale, \deleted{terminant en}\inserted{partant de} $x$, et \unsure{d'aboutissement} : $x_{\unsure{N|n}}$, prouvons $x_{\unsure{N|n}}\in G(j)$ (Alors on aura, $x_{\unsure{N|n}}\in G_0(j)$). Par hyp $x_0\in G(j)$, on va prouver par rec.
\[
x_i\in G(j)\Longrightarrow x_{i+1}\in G(j).\qquad(0\leq i\leq N-1)
\]
\uline{Si} $x_i\in\overline C(j)$, cela résulte de Prop., $2^\circ$. Si $x_i\in C(j)$, cela résulte de la définition de $\Sigma$, qui implique que $\Sigma(x_i)=R(z)\cap G(j)$, donc \inserted{comme} $x_{i+1}\in\Sigma(x_i)$ \deleted{\unsure{et z}} $x_{i+1}\in G(j)$. O.K.

Prouvons enfin que parmi les stratégies $\Sigma$
''',[
('text','top','donnée par la condition (pour forall z in C(j))'),('display','top cases','Sigma(z)=R(z) or R(z) cap G(j)'),('deletion','top first case','no partie tuple; no x in Gamma ... ou si z notin G(j)'),('deletion','top second case','exists x in Gamma avec z succeeds x et z in G(j)'),('insertion','top cases','z notin Gamma; z in Gamma'),('deletion','between cases','bien (donc z in G(j))'),('text','upper-middle','Dém Prouvons que Sigma(z) est une stratégie gagnante'),('display','upper-middle inline','R(z) nonempty implies Sigma(z) nonempty'),('text','middle','Il suffit de regarder le cas ...'),('deletion','middle','b) exists x in Gamma ... et z in G(j)'),('insertion','middle','z in Gamma'),('display','middle inline','Sigma(z)=R(z) cap G(j); z notin C_0; R(z) cap G(j) nonempty'),('text','lower','Prouvons que Sigma(z) est gagnante pour forall x in Gamma'),('insertion','lower','(x_0=x,x_1,...,x_N); partant de'),('deletion','lower','terminant en'),('text','lower','et d’aboutissement x_N ... Par hyp x_0 in G(j)'),('display','lower','x_i in G(j) implies x_(i+1) in G(j); 0<=i<=N-1'),('text','bottom','Si x_i in Cbar(j) ... Si x_i in C(j)'),('display','bottom inline','Sigma(x_i)=R(z) cap G(j)'),('insertion','bottom','comme'),('deletion','bottom','et z'),('text','bottom edge','Prouvons enfin que parmi les stratégies Sigma')
],'''Continues the greatest-strategy corollary from scan 006 after cancelled scan 007. The policy is unrestricted off Gamma and chooses G(j)-successors on Gamma. The proof carries a terminal winning condition through play. The displayed R(z) in Sigma(x_i)=R(z)∩G(j) is retained as written; any correction to R(x_i) belongs in notes only. Top case conditions show replaced reachability formulations.''')

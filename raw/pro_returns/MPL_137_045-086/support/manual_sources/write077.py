import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{77}
% archive foliation: 76
\deleted{donc
\[
(\lambda^n-\lambda^{n'})g_{n'}=0\qquad\forall\lambda\in\mathbf Z^r,
\]
et il suffit de voir que les $\lambda^n-\lambda^{n'}$ engendrent l'idéal $1$, ou encore}

Si on exigeait qu'on a, pour tt $\mathbf Z$-algèbre $k$, des compositions entre les $P_k(X,Y)=P(X,Y)\otimes_{\mathbf Z}k$, et on exigeait la décomposition plus haut valable pour tt $P_k(\prod X_i,Y)$, pour $\lambda\in(k^\times)^r$. Or on va mettre comme \uline{structure supplémentaire} la \uline{donnée} de la décomposition $(*)$ avec

e) Condition des degrés pour les compositions
\diagram{\begin{tikzcd}
X_1 \arrow[r,phantom,"\times\cdots\times"] & X_r \arrow[r,"{(n_1,\ldots,n_r)}"] & Y \\
Z_1^1\times\cdots\times Z_{s_1}^1 \arrow[u,"{m_1^1,\ldots,m_{s_1}^1}"] & Z_1^r,\ldots,Z_{s_r}^r \arrow[u,"{m_1^r,\ldots,m_{s_r}^r}"']
\end{tikzcd}}
la composée est de degré $(n_i m_1^i,n_i m_2^i,\ldots,n_i m_{s_i}^i)$ en $Z_1^i,\ldots,Z_{s_i}^i$; de même
\margin{Oubli: \unsure{les catégories} \unsure{Ce qu'on veut est} \unsure{la structure} \unsure{de degré $1$} $\unsure{P_1(X,Y)=P_1(X,Y)}$.}
\margin{\deleted{\unsure{Pour tt $i$, $f_i=0$ aussi}} $\unsure{(n_i)_{i=1,\ldots,r}}$ \unsure{ou $n_i=0$}; \unsure{si $m_i=0$, $n_i\ne0$} \unsure{(\text{homogène})} \unsure{$P_{(n_i)}$}.}

f) conditions \inserted{\unsure{symétrie}} pour la permutation des facteurs

g) $\forall X\in\operatorname{Ob}P$, l'application canonique déduite de $X\longrightarrow0$
\[
P_0(0,Y)\longrightarrow P_0(X,Y)
\]
est bijective (les ``applications constantes'' \inserted{de $X$ en $Y$} ``ne dépendent pas de $X$'')

Si $k$ est un anneau comm. et si $P_1$ est munie d'une structure $k$-linéaire par
\diagram{\begin{tikzcd}
k \arrow[r,no head] & \operatorname{End}(P_1) & \operatorname{End}(P) \arrow[l,no head]
\end{tikzcd}}
\deleted{on dit que} telle que les formules haut soient vraies pour $\lambda\in k^r$ (non seulmt $\lambda\in\mathbf Z^r$), on dit que $P$ est $k$-polynomiale.'''
e=[('deletion','top','donc (λn−λn′)gn′=0 et il suffit de voir'),('display','cancelled top','(λn−λn′)gn′=0 ∀λ∈Zr'),('text','upper','Si on exigeait qu’on a pour tt Z-algèbre k'),('text','upper middle','Or on va mettre comme structure supplémentaire'),('text','middle','e) Condition des degrés pour les compositions'),('diagram','middle','X1×…×Xr→Y with maps from products of Z'),('text','middle','la composée est de degré (ni mi1,…)'),('margin note','middle right diagonal','Oubli les catégories'),('margin note','middle left diagonal','Pour tt i fi=0 aussi'),('deletion','left margin','Pour tt i fi=0 aussi'),('insertion','above f)','symétrie'),('text','middle lower','f) conditions symétrie pour la permutation des facteurs'),('text','lower','g) ∀X∈ObP l’application canonique déduite de X→0'),('display','lower','P0(0,Y)→P0(X,Y)'),('text','lower','est bijective les applications constantes'),('insertion','lower right','de X en Y'),('text','bottom','Si k est un anneau comm et si P1 est munie'),('diagram','bottom','k–End(P1)–End(P)'),('deletion','bottom','on dit que'),('text','bottom','telle que les formules haut soient vraies pour λ∈kr')]
save(77,text,e)

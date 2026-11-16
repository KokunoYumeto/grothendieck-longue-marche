from record import draft
draft(114,r'''
\scanpage{114}
\uline{NB} La condition sur $N_2$ implique celle sur $T_2$, en passant aux formes bil. ass., i.e. en l'appliquant pour $a$ \uline{et} pour $1+a$ $(a\in A_1)$.

\textcircled{3°} On veut la condition
\[
 \boxed{\sigma_1\sigma_2\sigma_3=1}
\]
\margin{Cette condition est automatiquement vérifiée sur \unsure{la sous-algèbre} de $A$ engendrée par les $A_i$, car elle est vraie sur chaque $A_i$ (lequel est stable par les $\sigma_i$).}
qui implique que les involutions $\sigma_i$ commutent entre elles (car le produit de 2 d'entre elles est une involution
\[
 \boxed{\begin{aligned}
 \sigma_1\sigma_2&=\sigma_3\\
 \sigma_2\sigma_3&=\sigma_1\\
 \sigma_3\sigma_1&=\sigma_2
 \end{aligned}}
\]
(car pour deux invo. $\sigma$ et $\tau$,
\[
 \sigma\tau=\tau\sigma\quad\Longleftrightarrow\quad(\sigma\tau)^2=\unsure{1}\quad\text{i.e.}\quad\sigma\tau\sigma\tau=1
\]
)

En utilisant $1^\circ)$, \deleted{ceci} \inserted{la condition $\sigma_1\sigma_2\sigma_3=1$} s'explicite par la formule
\[
 2x=T_1(x)+T_2(x)+T_3(x)-\uline{t_2T_2(x)},
\]
non symétrique, mais elle est équivalente à
\[
 \sigma_2\sigma_3\sigma_1=1,\quad\text{ou}\quad\sigma_3\sigma_1\sigma_2=1,
\]
donc
\[
 \begin{aligned}
 2x&=T_1(x)+T_2(x)+T_3(x)-t_3T_3(x)\\
 2x&=\mathbin{-}\ \mathbin{-}\ \mathbin{-}\ \mathbin{\text{---}}-t_1T_1(x),
 \end{aligned}
\]
donc elles impliquent\unsure{*} la condition
\[
 \boxed{t_1\operatorname{Tr}_1(x)=t_2\operatorname{Tr}_2(x)=t_3\operatorname{Tr}_3(x)}
\]
\margin{du moins si $k\mathbin{-}A$ injectif --- mais on la suppose \unsure{vérifiée} en tous cas.}
(qui ressemble à $6^\circ$ ci-dessus). Si on désigne par $T_{A/k}(x)$ la valeur commune aux trois mbs, on trouve donc la condition
\[
 \boxed{2x=T_1(x)+T_2(x)+T_3(x)-T_{A/k}(x).}
\]
\mspage{113}
''')

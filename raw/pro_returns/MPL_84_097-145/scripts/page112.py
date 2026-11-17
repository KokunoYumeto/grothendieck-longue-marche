from record import draft
draft(112,r'''
\scanpage{112}
Considérons un des 6 diagrammes comm.
\diagram{\begin{tikzcd}
A_1 \arrow[r,no head,"\alpha_1"] \arrow[d,no head] & A \arrow[d,no head,"\alpha_2"] \\
k \arrow[r,no head] & A_2
\end{tikzcd}}
on veut que la situation soit, au pt de vue \unsure{raisonnablement bien}, comme si $A_1$ était quadratique sur $k$, et que $A$ en \unsure{soit déduit} par le changement de base $k\mathbin{-}A_2$.
\margin{Mais \unsure{on ne suppose ni les $A_i$ ni $A/A_i$} quadratiques, ni que $A_1,A_2$ \unsure{engendrent $A$}.}
\textcircled{1°}
\[
\boxed{T_2\bigl(\alpha_1(x_1)\deleted{\alpha_2(x_2)}\bigr)=t_1(x_1)\deleted{\alpha_2(x_2)}}
\]
\margin{Ce qui détermine $T_2$ sur $k[A_1,A_2]\subset A$ en termes de $t_1$.}
i.e. on \unsure{exige} un diagramme comm.
\diagram{\begin{tikzcd}
A_1\otimes_k A_2 \arrow[r] \arrow[d,"t_1\otimes\mathrm{id}_{A_2}"'] & A \arrow[d,"\unsure{T_1|T_2}"] \\
A_2 \arrow[r,equal] & A_2
\end{tikzcd}}
\margin{NB. $A_1\otimes A_2\mathbin{-}A$ n'est pas supposé injectif, mais que $t_1\otimes\mathrm{id}_{A_2}$ s'annule au moins sur le noyau.}
Ceci implique que
\[
\boxed{\sigma_2\bigl(\unsure{\alpha_1(x)}\bigr)=\alpha_1(\bar x)}
\]
i.e. $\sigma_2$ (et aussi $\sigma_3$) ``induit'' sur $A_1$ l'involution donnée $x_1\mathbin{-}\bar x_1$ de $A_1$

On veut une condition similaire pour les normes
\textcircled{2°}
\[
\boxed{\boxed{N_2\bigl(\alpha_1(a_1)\deleted{\unsure{\alpha_2(a_2)}}\bigr)=n_1(a_1)\deleted{\unsure{\alpha_2(a_2)^2}}}}
\]
\mspage{111}
''')

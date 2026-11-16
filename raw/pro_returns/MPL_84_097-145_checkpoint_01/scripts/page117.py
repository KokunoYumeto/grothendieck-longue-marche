from record import draft
draft(117,r'''
\scanpage{117}
et \deleted{\unsure{là}} on a une \deleted{bonne} op. de $\unsure{\gamma|\Gamma}$ sur $A$, telle que
\[
 \bigotimes A_i\mathbin{-}A
\]
soit compatible aux deux opérations de $\unsure{\gamma|\Gamma}$, savoir celle qui fait opérer
\[
 \tau_i\quad\text{par}\quad\sigma_{A/A_i}.
\]
\figure{\begin{tikzpicture}\draw[->] (0,.1)--(.12,0)--(.35,.04);\end{tikzpicture}}
\deleted{Considér}
Supposons maintenant que les $A_i$ correspondent \deleted{\unsure{à}} des rev. quadratiques $X_i$ de $X$, donc on a un rev. quadratique
\[
 X_1\wedge X_2\wedge X_3,\qquad\text{d'algèbre }B=A_1\unsure{\wedge|*}A_2\wedge A_3,
\]
et on a
\diagram{\begin{tikzcd}[column sep=large]
X_1\times X_2\times X_3\arrow[r]&X_1\wedge X_2\wedge X_3\\
(x_1,x_2,x_3)\arrow[r,no head]&x_1*x_2*x_3
\end{tikzcd}}
i.e.
\diagram{\begin{tikzcd}B\arrow[r]&A_1\otimes A_2\otimes A_3\end{tikzcd}},
et de façon plus précise, on a
\diagram{\begin{tikzcd}B\arrow[r,no head]&(A_1\otimes A_2\otimes A_3)^{\unsure{\gamma|\Gamma}}\end{tikzcd}}
\margin{invariants sous $\unsure{\gamma|\Gamma}$}
Et même, si on exclut les $x\in X=\operatorname{Spec}(k)$ de \uline{car. 2} tels que deux au moins des $A_i$ soient non étales en ce point, alors l'hom précédent est un \uline{iso}.

On va regarder le composé
\diagram{\begin{tikzcd}B\arrow[r,no head]&A_1\otimes A_2\otimes A_3\arrow[r,no head]&A\end{tikzcd}}, \deleted{\unsure{i.e.}}
\mspage{116}
''')

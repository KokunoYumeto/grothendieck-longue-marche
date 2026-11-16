from record import draft

draft(102,r'''
\scanpage{102}
\[
\xi^{\unsure{\natural|\flat}}=\xi+\bar\xi\deleted{^{\unsure{\natural}}}
\qquad\text{pour }\xi\in\mathcal A_1\otimes\mathcal A_2,
\]
en \unsure{supprimant|supposant} maintenant $\unsure{\chi}=2$ i.e. qu'on a
\[
\begin{aligned}
x_1&\mapsto\bar x_1=\deleted{\unsure{\overline T_1}\psi_1(x_1)}\inserted{\operatorname{Tr}_1(x_1)}-x_1,\\
x_2&\mapsto\bar x_2=\deleted{\unsure{\overline T_2}\psi_2(x_2)}\inserted{\operatorname{Tr}_2(x_2)e_2}-x_2
\end{aligned}
\]
sur $\mathcal A_1,\mathcal A_2$, donc
\[
\xi\mapsto\bar\xi,\quad x_1\otimes x_2\mapsto\overline{x_1\otimes x_2}\overset{\mathrm{def}}=\bar x_1\otimes\bar x_2
\]
sur $\mathcal A_1\otimes\mathcal A_2$. On aura donc, si $\xi\in\mathcal A_1$ i.e. $\xi=x_1\otimes e_2$
\[
\xi^{\unsure{\natural}}=(x_1\otimes1)^{\unsure{\natural}}=(x_1+\bar x_1)\deleted{\unsure{^{\natural}}}\otimes e_2=\operatorname{Tr}_1(x_1)e_1\otimes e_2
\]
c'est OK.

\uline{NB} Si \deleted{\unsure{la structure}} sur $X_0=V(2.1_X)\subset X$ (lieu de car. $2$), en tt pt de $X_0$ l'une des deux structures $E_1,E_2$ est étale, alors $\mathcal A\hookrightarrow\mathcal A_1\otimes\mathcal A_2$ est univ injectif, et a pour image
\[
(\mathcal A_1\otimes\mathcal A_2)^{\unsure{\natural}}=(\mathcal A_1\otimes\mathcal A_2)^{\sigma_1\otimes\sigma_2}.
\]
Ceci posé, on peut \inserted{donc} identifier l'application
\[
(x_1,x_2)\mapsto x_1*x_2:\mathcal A_1\times\mathcal A_2\longrightarrow\mathcal A
\]
ou
\[
x_1\otimes x_2\mapsto x_1*x_2\qquad \mathcal A_1\otimes\mathcal A_2\longrightarrow\mathcal A
\]
à des applications à valeurs dans $(\mathcal A_1\otimes\mathcal A_2)^{\unsure{\natural}}$.
\unsure{En tant que telle} elle est simplement \unsure{définie} comme \uline{l'application trace} pour $\sigma_1\otimes\sigma_2$.

Quand $\mathcal A_1,\mathcal A_2$ sont des alg. de \unsure{rev. qu. ét.}, il s'agit bien de trace au sens habituel.
Mais cette trace, sans cond. de car. $\ne2$ \unsure{etc.},
\mspage{101}
''')

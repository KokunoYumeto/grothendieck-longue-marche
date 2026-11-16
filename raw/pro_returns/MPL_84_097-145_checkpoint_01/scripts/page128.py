from record import draft
draft(128,r'''\scanpage{128}
\[
 \begin{aligned}
 \widetilde b_i&=\unsure{\varpi_i}-\chi q_i\quad;\qquad b_i+\widetilde b_i=\chi\operatorname{id}-\chi\operatorname{id}=0\\
 &=-\uuline{b_i}
 \end{aligned}
\]
$\widetilde U_i$ tel que
\[
 q'_i=\underbrace{q_i}_{\operatorname{id}-p_i}-\widetilde U_i
 =\deleted{\unsure{\chi}}\operatorname{id}-\underbrace{(p_i+\widetilde U_i)}_{p'_i}=.
\]
\[
 \widetilde U_i=-U_i
\]
\[
 \begin{aligned}
 \widetilde U&=\widetilde b_1\otimes\widetilde U_2+\widetilde U_1\otimes\widetilde b_2+\chi\widetilde U_1\otimes\widetilde U_2\\
 &=b_1\otimes U_2+U_1\otimes b_2+\chi U_1\otimes U_2=U
 \end{aligned}
\]
\margin{Mais attention,
$\widetilde T_{\widetilde U}=\deleted{\unsure{-}}T_{-\widetilde U}=-T_{-U}=T_U^{-1}$}
\figure{\begin{tikzpicture}\draw[->] (0,1.6) .. controls (.15,1) and (.1,.2) .. (0,0);\end{tikzpicture}}
\[
 \widetilde b=\widetilde b_1\widetilde b_2=b_1b_2
\]
\diagram{\begin{tikzcd}[row sep=huge]
\mathcal E_{(p_1,q_1)(p_2,q_2)}\deleted{\unsure{\simeq}}=M_1\otimes M_2\oplus L_1\otimes L_2\arrow[d,leftrightarrow,"\sim"',"T_{v_{(p_1,q_1)(p_2,q_2)}}"]\\
\mathcal E_{(\widetilde p_1,\widetilde q_1)(\widetilde p_2,\widetilde q_2)}=M_1\otimes M_2\oplus L_1\otimes L_2
\end{tikzcd}}
\margin{$\chi$-scindage défini (comme $q$) par
\diagram{\begin{tikzcd}[column sep=large]
M_1\otimes M_2\arrow[r,no head,"b=b_1b_2"]&L_1\otimes L_2
\end{tikzcd}}}
\margin{$\chi$ sc. défini (comme $\unsure{p.}$) par $-b$}
\inserted{$(=(\eta,\zeta)\longmapsto\eta,\zeta\unsure{+|-}v(\eta))$}
$T_v$ \deleted{\unsure{tr}}ansforme le $\chi$-scindage défini par $b$ en le $\unsure{\varphi|\chi}$-scindage défini par $b+\chi v$.
\deleted{\unsure{Si}} L'on veut que
\[
 b+\chi v=\underset{-b}{\underset{\Vert}{\widetilde b}}\deleted{\unsure{=}}\quad\text{i.e.}\quad v\overset{!}{=}-\frac{2}{\chi}b
\]
Supposons que $\exists\unsure{\gamma}\in k$, tq. $\gamma\chi=2$, \unsure{on peut} prendre \deleted{$\unsure{v}$}
\[
 \boxed{v=-\gamma b}
\]
\mspage{127}''')

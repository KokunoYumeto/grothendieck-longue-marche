from record import draft
draft(130,r'''\scanpage{130}
\diagram{\begin{tikzcd}[column sep=small]
0\arrow[r,no head]&L_i\arrow[r,no head]&E_i\arrow[r,no head]&M_i\arrow[r,no head]&0
\end{tikzcd}}
, et
\diagram{\begin{tikzcd}[column sep=small]
\pi_i:E_i\arrow[r,no head]&L_i
\end{tikzcd}}
$\chi$-scindage \unsure{donné}
\[
 p=(p_1,p_2)
\]
\diagram{\begin{tikzcd}[column sep=small]
p_i:E_i\arrow[r,no head]&L_i
\end{tikzcd}}
scindage
\[
 \Theta_{p_i}:E_i\simeq M_i\oplus L_i
\]
\diagram{\begin{tikzcd}[column sep=small]
b_i:\pi_i-\chi p_i:M_i\arrow[r]&L_i
\end{tikzcd}}
\diagram{\begin{tikzcd}[column sep=large]
b=b_1\otimes b_2:M_1\otimes M_2\arrow[r,no head]&L_1\otimes L_2
\end{tikzcd}}
d'où $\chi$-trivialisation \unsure{comp.} avec $\pi_{(p_1,p_2)}$,
\diagram{\begin{tikzcd}[column sep=huge]
\mathcal E_{(p_1,p_2)}\deleted{\unsure{\simeq 0}}=(M_1\otimes M_2)\oplus(L_1\otimes L_2)\arrow[r,"\deleted{\unsure{T_{-U}}}","{\Theta_{p,p'}\ \deleted{\unsure{\Theta_{p,p'}}}=T_{-U}}"']&\mathcal E_{p'_1,p'_2}
\end{tikzcd}}
\[
 \pi_{(p_1,p_2)}-\chi\unsure{p|\rho}=b_1\otimes b_2
\]
\[
 \pi_{p_1,p_2}:(\eta,\zeta)\mathbin{\text{---}}\deleted{\unsure{\eta}}\chi\zeta+b_1\otimes b_2(\eta))
\]
\figure{\begin{tikzpicture}\draw (0,0)--(0,4.8);\end{tikzpicture}}
\[
 p'_i=p_i-U_i,\quad U_i:M_i\longrightarrow L_i
\]
\[
 p'=(p'_1,p'_2)
\]
d'où $b'_1,b'_2$, avec
\[
 \unsure{b'_1}=\unsure{b_1}+\chi U_1,\quad b'_2=b_2+\chi U_2
\]
\[
 U=b_1\otimes U_2+U_1\otimes b_2+\chi U_1\otimes U_2
\]
\[
 (\eta,\zeta)\longmapsto(\eta,\zeta\unsure{+|-}U\eta)
\]
\uline{NB} $\Theta_{p,p'}$ transforme $\pi_{(p_1,p_2)}$
\[
 \begin{aligned}
 \pi_{p'_1,p'_2}:\ (\eta,\zeta)&\longmapsto\deleted{\unsure{\eta}}\chi\zeta+(b'_1\otimes b'_2)(\eta)\\
 &=\pi_{(p_1,p_2)}(\eta,\zeta)+U(\eta)
 \end{aligned}
\]
\mspage{129}''')

from record import draft
draft(134,r"""
\scanpage{134}\mspage{133}
\diagram{\begin{tikzcd}[column sep=huge,row sep=large]
& E_1\unsure{\wedge|\vee}E_2\arrow[dl,very thick,"\Theta_{p_1*p_2}"']\arrow[dr,"\Theta_{p'_1*p'_2}=\Theta_{p_1*p_2}\unsure{-|+}U"] &\\
(M_1\otimes M_2)\oplus(L_1\otimes L_2)\arrow[rr] && (M_1\otimes M_2)\oplus(L_1\otimes L_2)\\
b_1,b_2&&b'_1,b'_2
\end{tikzcd}}
\[
T_U:(\unsure{\eta|\zeta},\unsure{\zeta|\xi})\longmapsto(\eta,\zeta+U(\eta))
\]
\[
U=b_1(p_1)\otimes U_2+U_1\otimes b_2(p_2)+\chi U_1\otimes U_2
\]
\[
b'_1=b_1-\chi U_1,\qquad b'_2=b_2-\chi U_2
\]
\[
p'_1=p_1\unsure{+|-}U_1\psi_1,\quad
\unsure{p'_i|p'_2}=p_2\unsure{+|-}U_2\psi_2
\]
\diagram{\begin{tikzcd}[row sep=small]
U_1:M_1\arrow[r]&L_1\\
U_2:M_2\arrow[r,no head]&\unsure{L_2|L_1}
\end{tikzcd}}
\[
p'_1*p'_2=p_1*p_2\unsure{+|-}
\left[\underbrace{(\pi_1-\chi p_1)}_{b_1(p_1)}\otimes U_2
+U_1\otimes\underbrace{(\pi_2-\chi p_2)}_{b_2(p_2)}\right]
\deleted{\unsure{+}}-\chi U_1\otimes U_2
\]
\deleted{\(\unsure{b_2|b_1}\)}
\margin{\figure{\begin{tikzpicture}\draw[->](0,0)--(.25,.45);\end{tikzpicture}}
signe étrange\\
\unsure{qui où le|qui doit} \unsure{produit être}\\
\deleted{\unsure{étrange}}}
\[
U_1*U_2=-\chi U_1\otimes U_2
\]
Ces signes sont \unsure{dûs} au signe \(\underset{\mathcal E}{-\mathrm{id}}\) dans le diag. \unsure{comm.}
\unsure{commutatif}. (pour une extension de \(\underline O\) par \(\mathcal H\)
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
0\arrow[r,no head]&\mathcal H\arrow[r,no head,"\alpha"]\arrow[d,"-\mathrm{id}"']&\mathcal E\arrow[r,no head,"\psi"]\arrow[d,"\Phi"',"R"]&\underline O\arrow[r]\arrow[d,equal]&0\\
0\arrow[r,no head]&\mathcal H\arrow[r]\arrow[d,equal]&\operatorname{Hom}'(E,\mathcal H)\arrow[r]&O\arrow[r,no head]&0\\
&\operatorname{Hom}(\underline O,\mathcal H)&&&
\end{tikzcd}}
\[
\varphi(x,y)=-x\psi(y)+y\psi(x)
\]
\figure{\begin{tikzpicture}\draw[->](.3,.3)--(0,0);\draw(.15,.03)--(.35,.03);\end{tikzpicture}}
\[
\deleted{=\unsure{\lambda\operatorname{Hom}|\lambda}\ \mathcal E\longrightarrow\mathcal H}
\qquad f\longmapsto\lambda
\]
\deleted{\unsure{qui a le}| \(\unsure{a}.\exists\lambda;\)}
\[
=\left\{f:\mathcal E\longrightarrow\mathcal H\ \middle|\ 
f\circ\alpha=\unsure{\alpha|a}(\lambda\,\mathrm{id}_{\mathcal H}\right\}
\]
\margin{\diagram{\begin{tikzcd}[column sep=small,row sep=small]
&\arrow[r,mapsto]&\deleted{\unsure{\eta}}\\
\zeta_1,\eta_1\arrow[rr]&&\chi\eta_1+b_1(\zeta_1)\\
M_1\otimes M_2\arrow[u]&L_1\otimes L_2\arrow[ul]&
\end{tikzcd}}}
Si on pose
\[
p'_1=p_1-U'_1,\quad p'_2=p_2-U'_2,\quad
p'_1*p'_2=p_1*p_2-U'
\]
\[
\text{d'où }\left\{\begin{aligned}
U'_1&=-U_1\\
U'_2&=-U_2\\
\unsure{U'|U'_0}&=-U
\end{aligned}\right.
\quad\unsure{\sim}\quad
U'=-b_1\otimes U_2-U_1\otimes b_2+\chi U_1\otimes U_2
\]
\[
\boxed{U'=b_1\otimes U'_2+U'_1\otimes b_2+\chi U'_1\otimes U'_2}
\]
\margin{\unsure{soit|c'est} la formule \unsure{trouvée}....}
""")

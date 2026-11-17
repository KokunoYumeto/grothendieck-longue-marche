from record import draft
draft(144,r"""
\scanpage{144}
\[
 E_1\otimes E_2^{\deleted{\unsure{*}}}
\]
\figure{\begin{tikzpicture}
\node at (0,0) {$E_1\unsure{\wedge|\vee}E_2=$};
\node at (3.7,0) {$E_1\otimes E_2\quad\oplus L_1\otimes L_2$};
\node at (4.9,-.7) {$(E_1\otimes_0 E_2)$};
\draw (3.8,-.55)--(4.4,-.22)--(4.7,-.35)--(5.8,-.4)--(6,-.55);
\end{tikzpicture}}

$f_i$ endom de $E_i$ t.q. $f_i(L_i)\subset L_i$
\[
 \unsure{u_i|f_i}\big|_{L_i}=\unsure{u'_i|f'_i}:L_i\longrightarrow L_i
\]
\deleted{$u_2$ endom de $E_2$}
\[
 \begin{array}{lll}
 f_1\otimes f_2&\text{sur}&E_1\otimes E_2\\
 f'_1\otimes f'_2&\text{---}&L_1\otimes L_2
 \end{array}
\]
\[
 \deleted{u_1\otimes u_2}\qquad
 \begin{aligned}
 f(x_1*x_2)&=f_1(x_1)*f_2(x_2)\\
 f(u_1\otimes u_2)&=f'_1(u_1)\otimes f'_2(u_2)
 \end{aligned}
\]
\diagram{\begin{tikzcd}
 E_1\otimes L_2\arrow[d]&\unsure{E_1\otimes E_2}&\\
 x_1\otimes u_2\arrow[ur,mapsto]\arrow[dr,mapsto]&
 x_1\otimes u_2\arrow[r,mapsto]&f_1(x_1)*f_2(u_2)\\
 &\pi_1(x_1)\otimes u_2\arrow[r,mapsto]&f'_1(\pi_1(x_1))\otimes f'_2(u_2)
\end{tikzcd}}
\[
 f_1(x_1)*v_2=f'_1(\pi_1(x_1))\otimes v_2
\]
\[
 \deleted{\unsure{f(x_1}}\qquad\uline{\text{Ex}}\qquad f=
\]
\[
 f_1(x_1)=f_1(\pi\qquad \deleted{\unsure{f_2}}
\]
\diagram{\begin{tikzcd}
 E_1\otimes E_2\arrow[r]&\uline{\unsure{L_1|B_1}}\otimes L_2\\
 \alpha&\chi f_1\otimes f_2
\end{tikzcd}}
\[
 x_1-\pi_1(x_1)
\]
\diagram{\begin{tikzcd}
 E_1\arrow[d,"f_1"']&E_2\arrow[d,"f_2"]\\
 L_1&L_2\\
 \lambda_1&\lambda_2
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw (0,0)--(0,2.5);\end{tikzpicture}}
\diagram{\begin{tikzcd}
 &E_1\otimes E_2\arrow[r]&L_1\otimes\unsure{L_2}\\
 E_1\otimes L_2\arrow[ur]\arrow[dr]& &\\
 &L_1\otimes L_2\arrow[uur,"{\deleted{\unsure{\chi f_1\otimes f_2}}\ \unsure{f'_1f'_2|f'_1\otimes f'_2}}"']&
\end{tikzcd}}
\[
 \begin{array}{cc}
 f_1&f_2\\[.5em]
 \lambda_1&\lambda_2
 \end{array}
\]
\[
 \deleted{\unsure{f_1(}}\qquad x_1\otimes u_2\qquad
 \chi(\pi_1(x_1)\otimes u_2)
\]
\[
 \deleted{\lambda_1\lambda_2(\pi_1(x_1)\otimes u_2)}
\]
\[
 \deleted{f_1\otimes f_2}\qquad f'_1(\pi_1(\unsure{x'_1|x_1}))\otimes f_2(u_2)
\]
\[
 \frac{\unsure{\lambda_1}}{\unsure{\lambda_2}}f\qquad
 \chi f_1(x_1)\otimes\overbrace{f_2(u_2)}^{\deleted{\unsure{\lambda_2}}\lambda_2u_2}
\]
\[
 \deleted{\unsure{f_1(f'_1(x_1)\otimes u_2}\ \unsure{\longrightarrow}}
\]
\[
 \lambda_1\deleted{\unsure{\lambda_2}}\pi_1(x_1)\otimes\unsure{\lambda_2u_2}
\]
\[
 \deleted{\lambda_2f_1(x_1)=\lambda}
\]
\[
 \lambda_1\pi_1(x_1)=f_1(x_1)\chi
\]
\mspage{143}
""")

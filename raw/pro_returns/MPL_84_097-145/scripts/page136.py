from record import draft
draft(136,r"""
\scanpage{136}\mspage{135}
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
0\arrow[r]&L\arrow[r,no head]\arrow[d,"-\mathrm{id}_L"']&E\arrow[r,"\psi"]\arrow[d,"\sim"]&\underline O\arrow[r]\arrow[d,equal]&0\\
\arrow[r,no head]&L\arrow[r]&\operatorname{Hom}^{!}(E,L)\arrow[r,no head]&\underline O\arrow[r,no head]&0
\end{tikzcd}}
\[
\unsure{x}\longmapsto
\left[y\longmapsto(\unsure{x|-x}\psi(y)+y\psi(x))\right]
\]
\diagram{\begin{tikzcd}E\arrow[r,"\psi(x)"']&L\end{tikzcd}}
\[
{}_{\lambda_1}E_1*{}_{\lambda_2}E_2\simeq
\]
\figure{\begin{tikzpicture}\draw(0,0)..controls(5,.2)and(11,.5)..(16,.25);\end{tikzpicture}}
\[
\left|\begin{aligned}
(f_1*f_2)(x_1*x_2)&=\unsure{\Psi_1(f_1)|\Psi(f_1)}
\left[\pi_1(x_1)\otimes f_2(x_2)+f_1(x_1)\otimes
\unsure{\Psi_2 f_2|\Psi_2(f_2)}\pi_2(x_2)-\chi f_1(x_1)\otimes f_2(x_2)\right]\\
(f_1*f_2)(u_1\otimes u_2)&=\lambda_1\lambda_2\,u_1\otimes u_2
\end{aligned}\right.
\]
\figure{\begin{tikzpicture}\draw(0,0)..controls(6,.5)and(11,.7)..(16,.5);\end{tikzpicture}}
\[
(f_1*U_2)(x_1*x_2)=\Psi_1(f_1)\pi_1(x_1)\otimes
\underbrace{\unsure{U_2|f_2}(x_2)}_{U_2(\psi_2(x_2))}
-\chi f_1(x_1)\otimes\unsure{U_2|f_2}(x_2)
\]
\deleted{\((U_1*f_2)(x_1*x_2)\)}
i.e.
\[
(f_1*U_2)(x_1*x_2)=
\underbrace{\bigl(\Psi_1(f_1)\pi_1-\overset{\Psi_1(\pi_1)}{\overset{\Vert}{\chi}}f_1\bigr)}_{\text{nul sur }L_1}
\otimes U_2\,(x_1\otimes x_2)
\]
\[
\bigl(\unsure{[\pi'_1,f'_1]'|[\pi_1^!,f_1^!]^!}\otimes U_2\bigr)(x_1\otimes x_2).
\]
de \(=\)
\[
\left\{\begin{aligned}
U_1*f_2\,(x_1*x_2)&=
\bigl(U_1\otimes\unsure{[\pi'_2,f'_2]'|[\pi_2^!,f_2^!]^!}\bigr)(x_1\otimes x_2)\\
(U_1*U_2)(x_1*x_2)&=-\chi\cdot U_1(x_1)\otimes U_2(x_2)=
\end{aligned}\right.
\]
\margin{\figure{\begin{tikzpicture}\draw[->](0,0)--(.15,.5);\end{tikzpicture}}
signe étrange!}
\figure{\begin{tikzpicture}\draw(0,0)..controls(1,-.15)and(3,0)..(4,.1);\end{tikzpicture}}
\[
(\unsure{x_1|u_1}+u_1)*(\unsure{x_2|u_2}+u_2)
=x_1*x_2+\underbrace{x_1*u_2}_{\underbrace{\pi_1(x_1)}_{b_1}\otimes u_2}
+\underbrace{u_1*x_2}_{u_1\otimes\underbrace{\pi_2(x_2)}_{b_2}}
+\underbrace{u_1*u_2}_{\Vert\ \chi u_1\otimes u_2}
\]
""")

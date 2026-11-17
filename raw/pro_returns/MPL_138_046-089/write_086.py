from workflow import save_page
save_page(86,r'''\scanpage{86}
% archive foliation: 85
Soit $\unsure{\mathcal T|\Gamma}_\nu^!$ le ss-groupe de $\mathcal T_\nu$
formé des éléments qui satisfont
aux relations précédentes. Donc on a
\[
1-\mathcal T_\nu^{!0}-\mathcal T_\nu^!\longrightarrow\widehat{\mathbf Z}^{*}\longrightarrow1
\]
avec
\[
\begin{gathered}
\mathcal T_\nu^{!0}\subset\mathcal T_\nu^0\\
\text{''}\\
\{\gamma\in\mathcal T_\nu^0\mid\gamma\text{ commute aux }\rho_\nu(i)
\text{ et à }t_\nu\}
\end{gathered}
\]
\figure{\begin{tikzpicture}\draw (0,0)..controls (.5,-.04) and (1.6,.04)..(2.6,0);\end{tikzpicture}}

Si $\nu=2$ il y a un autre choix
intéressant de $I_{\unsure{0}}\subset\mathbf P^1(\overline{\mathbf Q})$, savoir
\[
I=\{0,1,\infty\}\qquad(\text{plutôt que }I=\mu_3(\overline{\mathbf Q}))
\]
qui donne lieu à action de
$\unsure{\mathfrak S}_3$ sur $(X_0/I_0/k)$ --- on trouve
action de $\Gamma\times\mathfrak S_3$ sur $\unsure{F_2|\Gamma_2}^{\mathrm{ext}}$, i.e.
\[
\Gamma\times\mathfrak S_3\longrightarrow\widetilde{\mathcal T}_2
\]
''',[
('text','upper','Soit T_ν^! le ss-groupe'),
('display','upper-middle','1−T_ν^{!0}−T_ν^!→Zhat*→1'),
('text','middle','avec'),
('display','middle','T_ν^{!0}⊂T_ν⁰; centralizer description'),
('drawing','middle divider','horizontal wavy stroke'),
('text','lower-middle','Si ν=2 il y a un autre choix'),
('display','lower-middle','I={0,1,∞} (plutôt que I=μ₃(Qbar))'),
('text','lower','qui donne lieu à action de S₃'),
('display','bottom','Γ×S₃→Ttilde₂')])

from save_page import save_page
save_page(78,r'''\scanpage{78}
% archive foliation: 77
\figure{\begin{tikzpicture}[x=1mm,y=1mm]\draw (0,0) ellipse(.7mm and .45mm);\draw (0,0)--(5,8);\end{tikzpicture}}
$H^2(S,A)\deleted{\unsure{\otimes\mathbf{Q}_\ell}}$ (dont le $T_\ell$ est $H^2(S,T_\ell(A))$) n'est pas néc nul, \deleted{\unsure{si}} \inserted{comme on voit} si $S$ est une courbe lisse projective géom. connexe sur $\mathbf{F}_p$ et $A=J\times S$, où $J$ est la jacobienne de $S$.
On a en tous cas
\[
\begin{aligned}
H^2(S,T_\ell(A))&\simeq H^1(\overline{S},T_\ell(\overline{A}))_\pi\\
&=\deleted{T_\ell J(\overline{\mathbf{F}}_p)\otimes}\inserted{[T_\ell(\unsure{\check{J}|\overline{J}})\otimes T_\ell(\overline{J})]_\pi}\\
&\simeq\mathrm{End}(J)\otimes_{\unsure{\mathbf{Z}|\mathbf{Q}}}\mathbf{Q}_\ell\quad\deleted{\unsure{par}}\ (\simeq(\unsure{\text{bihom}|\text{classes}}\text{ de corr. }\inserted{\text{divisorielles}}\text{ sur }C\,C)\otimes_{\mathbf{Z}}\mathbf{Q}_\ell
\end{aligned}
\]
qui est non nul .....
''',[
('top left','drawing','small loop with rising oblique stroke'),
('upper','text','H^2(S,A) dont le T_l est H^2(S,T_l(A))'),
('upper middle','text','On a en tous cas'),
('middle','display','H^2(S,T_l(A)) ≃ H^1(Sbar,T_l(Abar))_π'),
('middle right','display','[T_l(check J) tensor T_l(Jbar)]_π'),
('middle lower','display','End(J) tensor Q_l and correspondences expression'),
('below display','text','qui est non nul')
],remarks='Whole then both halves; lower half blank apart from archive foliation. Formula enlarged. Parenthetical interpretation to right of End(J), first J accent, and cancelled coefficient on first line are low-confidence; no missing closing parenthesis supplied.')

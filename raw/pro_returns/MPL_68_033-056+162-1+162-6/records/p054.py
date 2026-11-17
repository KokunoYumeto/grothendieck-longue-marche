import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(54,r'''
\scanpage{54}
% archive foliation: 53
\[
U\underset{\omega'}{\underbrace{\subset}}W\underset{\omega}{\underbrace{\subset}}V
\qquad\Omega(V/W)\wedge\Omega(V)\longrightarrow\Omega(W)
\]
\[
\mathrm{St}_{\omega}:\Omega(V)\unsure{\longrightarrow|\text{---}}\Omega(W)
\]
\[
\mathrm{St}_{\omega'}:\Omega(W)\text{---}\Omega(U)
\]
\[
\mathrm{St}_{\omega'}\mathrm{St}_{\omega}:\Omega(V)\longrightarrow\Omega(U)
\]
\[
I(\omega,\omega')\in\Omega
\]
\margin{$(\omega,\omega')\longmapsto\omega\times\omega'$}
\[
\Omega(V)\wedge\Omega(V')\longrightarrow\Omega(V\unsure{\wedge|\times}V')
\]
\[
\omega'\times\omega=(-1)^{\dim V.\dim V'}\deleted{\unsure{\Omega}}\omega\times\omega'
\]
\[
\deleted{\mathrm{St}(\omega)=\mathrm{St}(\omega')}
\]
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\mathbf R\arrow[d,phantom,"\rotatebox{90}{$\supset$}"]\arrow[r,phantom,"\subset"] &
\mathbf R^2\arrow[d,phantom,"\rotatebox{90}{$\supset$}"]\arrow[r,phantom,"\subset"] &
\mathbf R^3\arrow[d,phantom,"\rotatebox{90}{$\supset$}"]\arrow[r,dash] &
\mathbf R^{n-1}\arrow[d,phantom,"\rotatebox{90}{$\supset$}"]\arrow[r,phantom,"\subset"] &
\mathbf R^n\arrow[d,phantom,"\rotatebox{90}{$\supset$}"]\\
\mathbf R^+\arrow[r,phantom,"\subset"] &
\mathbf R\times\mathbf R^+\arrow[r,phantom,"\subset"] &
\mathbf R^2\times\mathbf R^+\arrow[r,phantom,"\subset"] &
\mathbf R^{\unsure{n-2}}\times\mathbf R^+\arrow[r,phantom,"\subset"] &
\mathbf R^{n-1}\times\mathbf R^+
\end{tikzcd}}
\[
\unsure{\ell_1\wedge\text{---}\ell_{n-1}\wedge\ell_n|e_1\wedge\text{---}e_{n-1}\wedge e_n}
\qquad e_1\wedge\text{---}\wedge e_{n-1}\wedge e_n
\]
\[
\omega\times\omega'\qquad I(\omega,\omega')\qquad I(\omega',\omega)
\]
\[
\left\{\begin{array}{l}
\mathrm{St}(\omega\times\omega')=\inserted{\unsure{(-1)^{?}|(-1)^p}}\mathrm{St}(\omega)\times\omega'\\
\mathrm{St}(\omega\times\omega')=\deleted{\unsure{(-1)^p}}\omega\times\mathrm{St}\omega'
\end{array}\right.
\]
\[
\underbrace{e_1\text{---}e_p}\quad f_1\text{---}f_q
\]
\[
\mathrm{St}(e_1\text{---}e_{p-1}e_p f_1\text{---}f_q)
=(-1)^{\unsure{q}}e_1\text{---}e_{p-1}\widehat e_p f_1\unsure{\text{---}f_q}
\]
\[
e_1\ e_2\text{---}e_n
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=.8pt,->] (0,0)--(0,1.15)--(1.2,1.12);
\draw[line width=.8pt,->] (1.2,1.12)--(1.2,0);
\draw[line width=1.2pt,->] (1.2,0)--(0,0);
\draw[line width=1pt,->] (3.8,1.15)--(3.8,3.2);
\draw[line width=.8pt,->] (3.83,3.05)--(3.8,1.15);
\draw[line width=.8pt,->] (3.8,1.15)--(6,1.1);
\draw[line width=.35pt] (3.9,1.35)--(4.5,2.2);
\draw[line width=.35pt] (3.83,2.2)--(4.4,2.85);
\draw[line width=.35pt] (4.3,1.42)--(4.9,2.15);
\draw[line width=.35pt] (4.85,1.4)--(5.55,2.1);
\draw[line width=.8pt,->] (5.45,-.25) .. controls (5.7,.05) and (5.55,.35) .. (5.4,.4);
\end{tikzpicture}}
''',[
('display','top left','U subset W subset V; inclusion braces omega prime,omega'),
('display','top right','Omega(V/W) wedge Omega(V) to Omega(W)'),
('display','upper','St_omega:Omega(V) to Omega(W)'),
('display','upper','St_omega prime:Omega(W) dash Omega(U)'),
('display','upper-middle','St_omega prime St_omega:Omega(V) to Omega(U)'),
('display','upper-middle','I(omega,omega prime) in Omega'),
('margin note','left of product formula','(omega,omega prime) maps to omega x omega prime'),
('display','middle','Omega(V) wedge Omega(V prime) to Omega(V wedge V prime)'),
('display','middle','omega prime x omega sign formula'),
('deletion','in sign formula','Omega'),
('deletion','left above chain','St(omega)=St(omega prime)'),
('diagram','middle','R subset R2 subset R3 dash R^(n-1) subset Rn with halfspace row'),
('display','middle-lower','ell_1 wedge dash ell_(n-1) wedge ell_n; e_1 wedge dash wedge e_(n-1) wedge e_n'),
('display','above fold','omega x omega prime; I(omega,omega prime); I(omega prime,omega)'),
('display','at fold','braced pair St product formulas'),
('insertion','above first St product formula','(-1)^?'),
('deletion','second St product formula','(-1)^p'),
('display','right of fold','e_1 dash e_p underbrace; f_1 dash f_q'),
('display','right below fold','St(e_1...e_p f_1...f_q) sign and hatted e_p'),
('display','lower left','e_1 e_2 dash e_n'),
('drawing','lower left','oriented square'),
('drawing','lower centre','hatched quadrant, vertical arrows up and down, horizontal arrow right, curved arrow below')
],[
('first St_omega map','right arrow','plain dash with slightly thickened endpoint','medium'),
('product target','Omega(V wedge V prime)','Omega(V x V prime); sign resembles a wedge','medium'),
('cancelled term in commutation formula','Omega','heavy angular cancellation leaves a round initial shape','low'),
('halfspace chain penultimate exponent','n-2','last figure faint; n-1 possible','medium'),
('dark sequence below chain','ell_1 wedge dash ell_(n-1) wedge ell_n','e letters; strongly reinforced ascenders','low'),
('inserted sign over first St formula','(-1)^?','(-1)^p; raised mark has a dot-like lower ending','low'),
('deleted sign in second St formula','(-1)^p','entire sign crossed out; exponent uncertain','low'),
('right-hand St basis formula','exponent q and terminal dash f_q','right end touches scan edge; hatted e_p retained','medium'),
('square direction marks','clockwise arrows','several corner strokes could be reinforced corners rather than arrowheads','medium')])

import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(36,r"""\scanpage{36}
\[
g=\exp f\qquad f'=\varphi=\unsure{\psi|\Psi}^{1/2}
\]
\[
g'=(\exp f)f'\deleted{=\unsure{(\exp f)\varphi}}
\]
\[
g''=(\exp f)f'^2+(\exp f)f''=(\exp f)(f'^2+f'')
\]
\[
\begin{aligned}
g'''&=(\exp f)f'(f'^2+f'')+(\exp f)(2f'f''+f''')\\
&=(\exp f)(f'^3+3f'f''+f''')
\end{aligned}
\]
\[
\frac{g'''}{g'}=f'^2+3f''+\frac{f'''}{f'}
\]
\[
\frac{g''}{g'}=f'+\frac{f''}{f'}\qquad
\left(\frac{g''}{g'}\right)^2=f'^2+\left(\frac{f''}{f'}\right)^2+2f''
\]
\[
\begin{aligned}
-2\frac{g'''}{g'}+3\left(\frac{g''}{g'}\right)^2
&=\uline{-2f'^2}-\deleted{6f''}-2\frac{f'''}{f'}\\
&\quad+\uline{3f'^2}+3\left(\frac{f''}{f'}\right)^2+\deleted{6f''}\\
&=-2\frac{f'''}{f'}+3\left(\frac{f''}{f'}\right)^2+\deleted{\unsure{3}}f'^2
\end{aligned}
\]
\[
G(t,\exp f)=G(t,f)+3(df)^2
\]
\[
\begin{array}{c}
\Vert\\
-c_t+c_{\exp f}=-c_t+c_f+3(df)^2
\end{array}
\]
\[
\boxed{c_{\exp f}=c_f+\deleted{\unsure{3}}df^2}
\]
\[
c_{\exp f}=c_f+\deleted{\unsure{3}}df^2=c_f+\omega^{\unsure{\otimes2|2}}.
\]
\[
\begin{array}{l}
\varphi=\exp t\\
\varphi'=\exp t\\
\varphi''=\exp t\\
\varphi^{\unsure{'''}}=\exp t
\end{array}
\qquad
\left(-2\frac{\varphi'''}{\varphi'}+3\left(\frac{\varphi''}{\varphi'}\right)^2\right)dt^2=dt^2
\]
\[
c_f+\unsure{\omega^2|\infty}
\]

\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node (formula) at (0,1.2) {$\deleted{\unsure{C}}G(z,f)\deleted{\unsure{d}}=\left(-\unsure{2}\frac{f'''}{f'}+3\left(\frac{f''}{f'}\right)^2\right)dz^2$};
\node (note) at (-2,-.2) {\shortstack{\unsure{invariant} \unsure{pour} $\pi$\\\deleted{\unsure{automorphismes|homomorphismes}}\\\unsure{hyperboliques}}};
\draw (-4,.45) .. controls (-4.6,-.25) and (-3.8,-.9) .. (-2.1,-.85) .. controls (-.2,-.9) and (.3,.35) .. (-1,.45) -- cycle;
\draw[->] (-3.6,.45) .. controls (-3.2,.6) and (-3.1,.8) .. (-3.1,1);
\draw (-.8,.8) .. controls (-.4,.55) and (2,.65) .. (2.6,.75);
\node at (2,-.1) {$\dfrac{df}{dz}$};
\node[right] at (2.7,-.1) {\shortstack{forme inv. par\\$\pi$}};
\end{tikzpicture}}}

\margin{$G(f,z)\deleted{\unsure{df^2}}=0$}
\margin{\figure{\begin{tikzpicture}
\node at (0,0) {$\dfrac{d^3z}{df^3}$};
\draw (.4,.05) .. controls (.65,.12) and (1.4,.1) .. (1.7,.05);
\end{tikzpicture}}}
\margin{$G(f,z)=0$}
\margin{$G(z,f)=$}
\margin{$\begin{array}{c}
\unsure{\gamma}.G(z,f)\\
\Vert\\
G(\unsure{\gamma}.z,\unsure{\gamma}.f)\\
\Vert\\
G(\unsure{\gamma}z,f)\\
\Vert\\
G(z,f)
\end{array}$}
\figure{\begin{tikzpicture}\draw (0,0)--(0,1.4);\draw (.17,.05)--(.17,1.3);\end{tikzpicture}}
\margin{35}
""",'text',[
('display','top line','g = exp f; f prime = varphi'),('display','second line','g prime'),('deletion','second line','=(exp f)varphi'),('display','third line','g double prime'),('display','fourth and fifth lines','g triple prime'),('display','upper middle','g triple prime over g prime'),('display','middle','g double prime over g prime and square'),('display','middle long expansion','minus 2 ratio plus 3 square'),('deletion','middle expansion','6 f double prime, twice'),('deletion','end expansion','coefficient 3'),('display','below fold','G(t, exp f)'),('display','below G formula','vertical equality; minus c_t'),('display','boxed','c_exp f = c_f plus df squared'),('deletion','boxed coefficient','3'),('display','below box','c_exp f = c_f plus omega tensor square'),('deletion','repeated coefficient','3'),('display','lower left','varphi and three derivatives'),('display','lower middle','Schwarzian expression equals dt squared'),('display','near bottom','c_f plus omega square'),('display','inverted bottom edge','G(z,f) and derivatives'),('deletion','inverted formula','leading C and d-like symbol'),('drawing','inverted bottom','outlined callout and arrow to f; underbrace'),('margin note','inverted callout','invariant pour pi; hyperboliques'),('deletion','inverted callout','automorphismes or homomorphismes'),('margin note','inverted bottom beside derivative','forme inv. par pi'),('display','inverted right margin first','G(f,z) df squared = 0'),('deletion','inverted right margin','df squared'),('drawing','beside d cubed z','short curved stroke'),('display','inverted right margin','d cubed z / df cubed'),('display','inverted right margin','G(f,z)=0; G(z,f)='),('display','right margin chain','gamma.G(z,f) vertical equalities'),('drawing','bottom left edge','two vertical strokes'),('margin note','bottom left','35')
],[
('top, last letter','psi','Psi','medium','Three-pronged letter; case is not decisive from the hand.'),('second line cancellation','=(exp f)varphi','','low','Overwritten ink obscures the exp letters and opening parenthesis.'),('three cancelled coefficients','3','','medium','Zigzag cancellation leaves a 3-like grey base; no separate replacement digit is clear.'),('c_exp f, last exponent','tensor 2','2','medium','A small loop/cross precedes the superscript 2.'),('lower left, last derivative','varphi triple prime','','medium','The three derivative strokes merge into a hooked stroke.'),('bottom upright unfinished expression','c_f + omega squared','c_f + infinity','low','Small curled final symbol appears partly within the inverted callout contour.'),('inverted formula, leading cancelled marks','C; d','','low','Blue retracing prevents identification of original marks; retained as doubtful deleted symbols.'),('inverted formula, coefficient of f triple prime','2','','medium','Staining crosses the coefficient; a lower curved trace remains.'),('inverted callout, first line','invariant pour pi','','low','Letters are compressed and close to the outline; read after rotation and enlarged inspection.'),('inverted callout, cancelled middle line','automorphismes','homomorphismes','low','Strike-through destroys several letter junctions; these are tentative readings, not a supplied mathematical completion.'),('inverted callout, final word','hyperboliques','','medium','The opening and ending are readable; middle loops are compressed.'),('inverted right margin, cancelled differential','df squared','','low','Diagonal blue strokes obscure the superscript.'),('inverted right margin chain','gamma','','medium','The first hooked Greek letter could have another cursive form; all four occurrences share the same treatment.')
])

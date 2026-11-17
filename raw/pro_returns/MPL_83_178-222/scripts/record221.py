import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(221,r'''\scanpage{221}
\[
\begin{aligned}
 A&=a+a'=\lambda\\
 B&=b+b'=\mu\\
 C&=c+c'=\nu
\end{aligned}
\qquad
\boxed{\lambda,\mu,\nu}\quad\text{correspondent aux trois directions d'arêtes}
\]
\[
\deleted{\unsure{\beta}}\qquad
\begin{aligned}
 A'&=a'\unsure{+|-}a\\
 B'&=b'-b\\
 C'&=c'\unsure{+|-}c
\end{aligned}
\qquad\uline{\lambda\ \mu\ \nu}
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (-1.5,.8)--(-1.4,-.25);
\fill (-1.54,.22) circle(.025);
\draw (.2,2)--(.2,1.05);
\draw (.23,1.8)--(.37,1.5)--(.46,1.5)--(.7,.35);
\draw (.7,-.05)--(.82,-1.2);
\fill (.68,-.55) circle(.025);
\draw (1.65,1.05)--(1.72,-.3);
\fill (1.7,.48) circle(.025);
\end{tikzpicture}}
\[
\begin{aligned}
 a\unsure{+|-}a'&=\lambda\\
 b\unsure{+|-}b'&=\mu\\
 c\unsure{+|-}c'&=\nu
\end{aligned}
\qquad
\varphi_a+\varphi_{a'}=2(b+b'\unsure{-|+}c+c')=2(\mu+\nu)
\]
\margin{220}
''',[('display','upper left','A=a+a′=λ; B=b+b′=μ; C=c+c′=ν'),('display','upper centre','boxed λ,μ,ν'),('text','upper right','correspondent aux trois directions d’arêtes'),('deletion','left below C','β'),('display','left middle','A′=a′+a; B′=b′−b; C′=c′+c'),('display','upper centre below box','underlined λ μ ν'),('drawing','centre','four vertical strokes and points'),('display','lower left','a+a′=λ; b+b′=μ; c+c′=ν'),('display','lower middle','φa+φa′=2(b+b′−c+c′)=2(μ+ν)'),('margin note','bottom left','220')],[('left A′,C′ equations','+','The small joining strokes look like plus signs; a minus is also possible.','low'),('lower-left sums','+','Very cursive horizontal strokes, each retained with minus alternative.','medium'),('last display, before c','−','The visible stroke is horizontal; + is the mathematical expectation but not imposed.','low'),('cancelled sign below first group','β','Retraced, blacked sign; reading only conjectural.','low')],['The plus/minus differences in A′,C′ and the last face-sum formula require a reading note, not algebraic correction.','λ,μ,ν explicitly correspond to three edge directions.'],notation=[('three edge-direction parameters',r'\lambda,\mu,\nu','As in upper explanatory label; no new script alphabet.')])

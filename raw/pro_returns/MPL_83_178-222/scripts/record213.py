import sys
sys.path.insert(0,'MPL_83_178-222/scripts')
from record_page import record
record(213,r'''\scanpage{213}
\figure{\begin{tikzpicture}[scale=1.05]
\draw (0,0.3)--(0,3.1)--(3.4,3.25);
\draw[->] (0,2.2)--(0,.9);
\draw (0,3.1)--(1.3,4.25)--(4.5,4.45)--(4.45,1.6);
\draw (1.3,4.3)--(4.35,4.5);
\draw (3.55,3.4)--(4.5,4.45) (3.4,3.05)--(3.35,.25) (3.7,.2)--(4.45,1.6);
\draw[<-] (0,0)--(3.45,.1);
\draw[dashed] (1.3,1.5)--(4.45,1.6) (1.3,1.5)--(1.3,3.9);
\draw (.15,.15)--(.3,.3);
\fill (0,3.1) circle(.1);\fill (4.45,1.6) circle(.08);
\draw[->] (.6,2.55)..controls (1.1,2.8) and (1.1,3.2)..(.8,3.5);
\node[above] at (1.3,4.3) {$A$};\node[above right] at (4.5,4.45) {$B'$};
\node[right] at (3.55,3.25) {$C$};\node[left] at (1.3,1.5) {$C'$};
\node[below] at (0,0) {$B$};\node[below] at (3.45,.1) {$A'$};
\node[above left] at (.6,3.7) {$a$};\node[left] at (0,1.5) {$b$};
\node[above] at (2.3,3.2) {$c$};\node[right] at (4.45,3) {$b'$};
\node[right] at (4.1,.8) {$a'$};\node[above] at (2.8,1.6) {$c'$};
\node[right] at (1.3,2.5) {$\alpha'$};\node[right] at (.55,.65) {$\alpha$};
\node[above] at (2.9,4.4) {$\beta$};\node[above left] at (4,3.9) {$\beta'$};
\node[right] at (3.4,1.95) {$\gamma$};\node[above] at (1.8,0) {$\gamma'$};
\end{tikzpicture}}
\[\gamma'-c=a'-\beta'=c'-\beta=\alpha-a\ \big|\ =\delta'\]
\[\left\{\begin{aligned}
\gamma'&=\delta'+c\\
\beta'&=-\delta'+a'\\
\beta&=-\delta'+c'\\
\alpha&=\delta'+a
\end{aligned}\right.\]
\unsure{reste pour expr.} $\uline\gamma,\uline{\alpha'}$
\[\uline{b-\gamma}=\uline{\alpha-a'}=\uline{\alpha'-b'}=a-\beta'\ \big|\ =\delta''\]
\[\left\{\begin{aligned}
\gamma&=\deleted{\unsure{b}}+\delta''+b\\
\alpha'&=-\delta''+b'
\end{aligned}\right.\]
\[\begin{aligned}
\alpha&=-\delta^{\unsure{''|4}}+a'\\
\beta'&=\unsure{|}+\delta^{\unsure{''|4}}+a
\end{aligned}\]
\[\boxed{-\delta''+a'=\delta'+a}\]
\figure{\begin{tikzpicture}\node[draw,ellipse] {$\delta'+\delta^{\unsure{''|4}}=a'-a$};\end{tikzpicture}}
\[\boxed{+\delta^{\unsure{''|4}}+a=-\delta'+a'}\]
\margin{212}
''',[
('drawing','upper left','cube A,B prime,C,C prime,B,A prime with edges a,b,c,alpha,beta,gamma'),('display','upper right','gamma prime-c=a prime-beta prime'),('display','middle right','four equations delta prime'),('text','right of system','reste pour expr. gamma,alpha prime'),('display','lower middle','b-gamma=alpha-a prime'),('display','lower middle','gamma=...;alpha prime=-delta doubleprime+b prime'),('deletion','gamma equation','b'),('display','bottom middle','alpha=-delta doubleprime+a prime;beta prime'),('display','bottom right','boxed -delta doubleprime+a prime=delta prime+a'),('drawing','bottom right','circled delta prime+delta doubleprime=a prime-a'),('display','bottom right','boxed +delta doubleprime+a=-delta prime+a prime'),('margin note','lower left','212')],
[('middle text','reste pour expr.','last abbreviated word reduced to long strokes','low'),('gamma solution','+delta doubleprime+b','plus is visible despite preceding relation b-gamma=delta doubleprime','high'),('bottom superscripts on delta','double prime or4','two upper strokes merge to4/u shape; retained uncertainty','medium'),('beta prime solution prefix','vertical stroke','possible cancelled unfinished sign before plus','low')],
['Second cube parametrization by opposite edge pairs; delta prime+delta doubleprime=a prime-a circled. Several sign inconsistencies in solutions are visible and preserved.'],sheet_kind='reused_typed',notation=[('delta superscript two joined strokes',r'\delta^{\unsure{\prime\prime|4}}','double prime versus digit4 uncertain in lower equations')])

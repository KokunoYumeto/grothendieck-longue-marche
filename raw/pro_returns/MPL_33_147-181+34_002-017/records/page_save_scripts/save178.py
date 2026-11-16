import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,178,r'''\scanpage{178}
\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=1.2pt] (0,0.8)--(1.1,0.8)--(1.05,0)--(0.2,0.03)..controls (0.4,0.4)..(0,0.8);
\draw[line width=0.8pt] (0,0.8)--(1.05,0)--(0.25,0.5)--(1.1,0.8)--(0.2,0.03)--(0.9,0.4)--(0.1,0.7)--(1.1,0.8)--(0.45,0.1)--(0.15,0.6)--(0.95,0.1)--(1.1,0.8)--(0.3,0.25)--(0,0.8);
\end{tikzpicture}}}
\[
\operatorname{Ext}^i(F,G)
\]
\[
\deleted{\unsure{F}}\qquad DG
\]
\[
\begin{aligned}
\mathrm{R}\mathcal{H}om(F,G)&\simeq\mathrm{R}\mathcal{H}om(F,DDG)\\
&\simeq\mathrm{R}\mathcal{H}om(F\overset{\mathrm L}{\otimes}DG,R_X^{\bullet})
\end{aligned}
\]
\[
F_{\unsure{\bullet|q}}\otimes DG
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[left] at (0,0) {$-2d$};\node[right] at (1.1,0) {$0$};\draw[line width=2pt] (0,0)--(1.05,0.02);\draw ( -0.55,-0.22)..controls(-0.65,-0.45) and (0.7,-0.43)..(1.3,-0.2);
\node[left] at (3.5,0.05) {$-2d$};\draw (3.55,0.02)--(4.0,0.02);\node[right] at (4.1,0.05) {$0$};
\end{tikzpicture}}
\[
\deleted{\operatorname{Ext}^i}\qquad\mathcal{H}_i(F\otimes DG)\text{ de dim }\leq i
\]
\[
D(F\overset{\mathrm L}{\otimes}DG
\]
\[
\operatorname{Ext}^i(F,G)
\]
\[
\boxed{\operatorname{Ext}^*(F,\unsure{C|G})\Leftarrow E_{\unsure{1|2}}^{pq}=\operatorname{Ext}^{p\deleted{\unsure{+q}}}(F\otimes\operatorname{Ext}^{-q}(G,A_X),A_X)}
\]
\[
\deleted{\unsure{q^4-q\leq q}}\qquad F\otimes\operatorname{Ext}^{2d}(\unsure{C|G},A)
\]
\[
\deleted{\operatorname{Ext}^p(}
\]
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (-0.8,0)--(2.55,0);\draw (0,1.7)--(0,-2.65);
\node[above] at (0,1.8) {$q$};\node[left] at (0,0.08) {$0$};\node[right] at (2.55,0) {$p$};\node[above] at (2.3,0.1) {$2d$};\node[left] at (0,-2.25) {$2d$};
\draw (0,-2.25)..controls(0.9,-2.33) and (1.6,-2.22)..(2.4,-2.25)--(2.3,0);
\draw[line width=1.8pt] (0,0)--(2.4,-2.25);\draw[line width=0.8pt] (0.03,-0.02)..controls(1.1,-0.9) and (2.0,-1.9)..(2.4,-2.25);
\draw (0,-2.25)--(0.65,-2.8);\draw (-0.2,-2.02)--(0.1,-2.3);
\draw (-0.08,-0.65)--(0.05,-0.55);\draw (-0.06,-1.2)--(0.03,-1.1);\draw (-0.08,-1.8)--(0.03,-1.6);
\fill (0,0) circle(0.04);\fill (2.4,-2.25) circle(0.055);\draw[line width=1.2pt] (2.15,0.15)--(2.48,-0.15);
\end{tikzpicture}}
\margin{$\operatorname{Supp}\operatorname{Ext}^{-q}(\unsure{C|G},A_X)$ de \unsure{codim} $\geq-q$\par
\deleted{de dim $\leq$}\par
donc $\operatorname{Ext}^p(\ ,A_X)$ $=0$ si $p<-q$\par
i.e. $p+q<0$}
\[
\deleted{\operatorname{Ext}^{\unsure{*}}?}\qquad\operatorname{Ext}^{2d}(F,\unsure{C|G})\simeq\operatorname{Ext}^{2d}(F\otimes\mathcal{H}om(\unsure{C|G},A_X),A_X)
\]
\margin{177}
''',[
('drawing','upper right','crosshatched quadrilateral'),('display','top left','Ext^i(F,G)'),('deletion','upper','F'),('display','upper','DG'),('display','upper middle','RHom(F,G) bidual and tensor chain'),('display','middle','F_bullet tensor DG'),('drawing','middle','two intervals -2d to0, first bracketed'),('deletion','middle','Ext^i'),('display','middle','H_i(F tensor DG) de dim≤i'),('display','middle lower','D(F derived tensor DG unfinished'),('display','middle left','Ext^i(F,G)'),('display','lower boxed','Ext star left E_1^pq and Ext expression'),('deletion','boxed exponent','+q'),('deletion','below box','q^4-q≤q'),('display','right below box','F tensor Ext^2d(C,A)'),('deletion','right below box','Ext^p('),('drawing','lower center','p q axes, rectangle and descending diagonal'),('margin note','lower right','Supp Ext^-q codimension bound and vanishing'),('deletion','lower right','de dim≤'),('display','bottom','Ext^2d(F,C) isomorphism'),('deletion','bottom before formula','Ext star?'),('margin note','bottom left','177')],remarks='Whole, halves and enlarged boxed formula/lower right read. D(F derived tensor DG has no closing parenthesis in the source. The graph lower vertical-axis label appears 2d without a visible minus; no minus supplied. The E-page index looks 1, with alternative2 marked, and the cancelled addition to exponent p is unresolved. Several pencilled G/C forms are marked. Right-hand argument says support codimension at least -q, followed by Ext vanishing for p<-q and p+q<0; no hypotheses or proof supplied here. Top-right crosshatched doodle and interval annotations reproduced in TikZ.')

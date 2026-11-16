from page_work import save_page
text=r'''\scanpage{123}
\diagram{\fbox{$\begin{array}{ll}
H^i_Y(X,M)&\operatorname{Ext}^i(X,M,A)\\[1ex]
H^i(X,M)&\operatorname{Ext}^i_Y(X,M,A)\\[1ex]
H^i(U,M)&\operatorname{Ext}^i(U,M,A)
\end{array}$}}
\[
\operatorname{Ext}_{\unsure{m}}(M,A)\overset{?}{=}D(M)\qquad A
\]
\[
0\mathrel{-}M'\mathrel{-}M\mathrel{-}M''\mathrel{-}0
\]
\[
\unsure{\operatorname{Hom}}_{\unsure{m}}(M,A).
\]
\figure{\begin{tikzpicture}\draw(0,0)--(1.2,4.2);\draw(.08,0)--(1.29,4.25);\end{tikzpicture}}
\diagram{\begin{tikzcd}[row sep=small,column sep=large]
\operatorname{Ext}^i_Y(X;M,N)\arrow[d]&\bullet&\operatorname{Ext}^{1-i}(X;N,M)\\
\operatorname{Ext}^i(X;M,N)\arrow[d]&&\operatorname{Ext}^{1-i}_Y(X;N,M)\arrow[u,dash]\\
\operatorname{Ext}^i(U;M,N)&&\operatorname{Ext}^{-i}(U;N,M)\arrow[u,dash]
\end{tikzcd}}
\figure{\begin{tikzpicture}\draw(0,0)ellipse(.4cm and .6cm);\fill(.04,.07)circle(1.5pt);\end{tikzpicture}}
\[
\operatorname{Ext}^i_Y(X;F,G)\longrightarrow\operatorname{Ext}^i_Z(X;F,G)\longrightarrow\operatorname{Ext}^i_{Z-Y}(X;F,G)
\]
\diagram{\begin{tikzcd}[column sep=small,row sep=tiny]
\operatorname{Ext}^{\unsure{r-i}}(X_{/Y}-Y,G_{/\unsure{Y|Z}},F_{/\unsure{Y|Z}})&
\operatorname{Ext}^{r-i}_a(\unsure{\widehat X|X}_{/Y},\widehat G_{/Y},\widehat F_{/Y})\arrow[l,"?"']&
\operatorname{Ext}^{r-i}_a(X_{/Z};G_{/Z},F_{/Z})\arrow[l]&
\operatorname{Ext}^{r-i-1}(X_{/Z}-Y,G_{/Z},F_{/Z})\arrow[l,"?"']\\
&\unsure{U}\ ?&&
\end{tikzcd}}
\[
Y\subset Z
\]
\diagram{\begin{tikzcd}[row sep=tiny,column sep=large]
X_{/Y}\arrow[r]&X_{/Z}\\
&\cup\\[-1ex]
&Y\\[-1ex]
&\cup\\[-1ex]
&\{a\}
\end{tikzcd}}
\margin{$\unsure{1}$}
\[
\mathrel{-}\operatorname{Hom}_a(X_{/Z};G_{/Z},F_{/Z})
\]
\figure{\begin{tikzpicture}\draw(0,0)--(0,.17);\draw(.08,-.01)--(.08,.13);\end{tikzpicture}}
\mspage{122}
'''
save_page(123,text,[('diagram','top boxed three by two table','HiY(X,M),Exti(X,M,A);Hi(X,M),ExtiY(X,M,A);Hi(U,M),Exti(U,M,A)'),('display','middle left queried equality','Extm(M,A)?=D(M)'),('display','middle isolated right','A'),('display','middle left sequence','0-Mprime-M-Msecond-0'),('display','middle left unfinished Hom','Homm(M,A)'),('drawing','middle divider','two slanting parallel lines'),('diagram','middle right paired columns','ExtiY→Exti→Exti(U); Ext1-i, Ext1-iY, Ext-i(U); dot'),('drawing','lower left','oval containing a dot'),('display','lower first row','ExtiY(X;F,G)→ExtiZ(X;F,G)→ExtiZ-Y(X;F,G)'),('diagram','lower long leftward sequence','Extr-i(X/Y-Y,..)←? Extr-i a(hatX/Y,hatG/Y,hatF/Y)←Extr-i a(X/Z;G/Z,F/Z)←?Extr-i-1(X/Z-Y,..)'),('display','lower under second sequence object','U ?'),('display','lower left inclusion','Y subset Z'),('diagram','lower center','X/Y→X/Z contains Y contains {a}'),('margin note','lower center right','1'),('display','bottom unfinished Hom','-Homa(X/Z;G/Z,F/Z)'),('drawing','bottom below Hom','two short parallel vertical strokes'),('text','bottom left page number','122')],observations='Whole and both halves read, with enlarged lower long row and left-hand formulas. Blue typescript is mirrored show-through, not surface writing. Source right-hand upward connectors in the paired columns have no secure arrowheads and are retained as plain lines. The source has 1-i in its first two right objects but -i in its last. Question marks above two lower arrows are literal. Hats and the faint formal-neighbourhood subscripts carry doubt where their strokes do not decide.')

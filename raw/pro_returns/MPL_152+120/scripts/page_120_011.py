from record_page import save_page
save_page(120,11,r'''
\mspage{5}
Pour que la somme amalgamée existe dans \deleted{\unsure{$\operatorname{Esp}$}} $\mathcal E$ et que $X\mapsto|X|$ y commute, il \unsure{f. et s.} qu'il existe une famille finie de \inserted{paires de} fonctions
\[
\begin{array}{l}
f_\alpha:\deleted{\unsure{g}}\ X_1\longrightarrow R\\
g_\alpha:X_2\longrightarrow R
\end{array}
\]
telles que l'on ait
\[
\text{a)}\quad f_\alpha(\unsure{i_1|z_1}(z))=g_\alpha(i_2(z))\qquad\forall\alpha\in\unsure{I|A},\ z\in Z
\]
b) \deleted{Si $\unsure{x},y$ les $f_\alpha$ \unsure{x}} les $f_\alpha$ ($g_\alpha$) séparent \deleted{$(f_\alpha)$} les pts de $X_1$ ($X_2$) i.e.
\[
 X_1\longrightarrow R^I\qquad(X_2\longrightarrow R^I)
\]
sont injectifs
\[
\begin{array}{ll}
\text{c)}&\text{Si }x_1\deleted{\unsure{\alpha}}\in X_1\smallsetminus i_1(Z)\\
&x_2\in X_2\smallsetminus i_2(Z)\\
&\exists\alpha\text{ avec }f_\alpha(x_1)\ne g_\alpha(x_2)
\end{array}
\]

\uline{NB} On peut généraliser, sous les conditions de la proposition, il existe la structure modérée qu'on veut sur $X$, ssi $\exists$ une famille finie $(F_\alpha)$ \deleted{\unsure{de}} de systèmes inductifs
\[
 (f_\alpha:i\in I\qquad f_{\alpha i}:X_i\underset{\text{modérée}}{\longrightarrow}R),
\]
déterminant des
\[
 f_\alpha:X\longrightarrow R
\]
telles que les $f_\alpha$ séparent les pts de $X$, i.e.
\[
 f=(f_\alpha):X\hookrightarrow R^A
\]
\mspage{10}
''',[
('text','top right','5'),('text','upper','Pour que la somme amalgamée'),('deletion','second line','Esp'),('insertion','above fonctions','paires de'),('display','upper','f_alpha and g_alpha'),('deletion','first function','g'),('text','above a','telles que l’on ait'),('display','a','f_alpha(i1(z))'),('text','b','les f_alpha séparent'),('deletion','b first line','Si x,y les f_alpha'),('deletion','b second line','(f_alpha)'),('display','b','X1 to R^I'),('text','b after display','sont injectifs'),('display','c','x1 and x2 outside images'),('deletion','c after x1','alpha'),('text','lower','NB On peut généraliser'),('deletion','lower after F_alpha','de'),('display','lower','f_alpha i in I'),('text','lower','déterminant des'),('display','lower','f_alpha X to R'),('text','bottom','telles que les f_alpha'),('display','bottom','f=(f_alpha) X into R^A'),('text','bottom left','10')], observations='Point-separating finite families of compatible functions give the stated criterion for amalgamated sums; NB extends to finite diagrams. Index alphabet in first display uncertain; must compare I/A across sheet during audit.')

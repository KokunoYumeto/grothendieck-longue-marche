import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{\textcircled{b}}
we may assume $Y$ is a $(\underline W)$-Kan object of $\widehat A$, in which case $\operatorname{Hom}_{\mathrm{Hot}}(X,Y)\simeq\overline{\operatorname{Hom}}(X,Y)$ (homotopy classes of maps). Moreover, because of the assumption on $Y$, \inserted{the} homotopy relation \deleted{of}\inserted{among} maps $X\longrightarrow Y$ is \deleted{equivalent}\inserted{the same} \unsure{as} elementary homotopy.

Surjectivity of $(*)$? We get maps $g_0,g_1\cdots$
\diagram{\begin{tikzcd}
X_0\arrow[r,hook]\arrow[dr,"g_0"']&X_1\arrow[r,hook]\arrow[d,"g_1"]&X_2\arrow[r,hook]\arrow[dl,"g_2"]&{}\\
&Y&&
\end{tikzcd}}
\diagram{\begin{tikzcd}&X_n\arrow[r,no head,"f_n"]\arrow[dl,"g_n"']&X_{n+1}\arrow[dl,"g_{n+1}"]\\{}&{}&\end{tikzcd}}
such that $g_{n+1}f_n\sim g_n$ for any $n$, the question is to find \deleted{a representative} for each $n$ a $g'_n\sim g_n$ such that \uline{equality} $g'_{n+1}f_n=g'_n$ holds. This brings us to the slightly more general situation (where $i:X\longrightarrow X'$ is $f_n:X_n\longrightarrow X_{n+1}$, and $p:Y\longrightarrow Y'$ is the can. $Y\longrightarrow e$, and $g=g_n$, $\varphi=g_{n+1}$)
\diagram{\begin{tikzcd}
X\arrow[r,"g"]\arrow[d,"i"']&Y\arrow[d,"p"]\\
X'\arrow[r,"g'"']\arrow[ur,dashed,"\deleted{\unsure{g}}\varphi"]&Y'
\end{tikzcd}}
where $i$ is a cofibration, $p$ \unsure{is} a fibration, and the two triangles commutative up to homotopy
\[\varphi i\overset h\sim g\qquad p\varphi\overset h\sim g'\]
(we assume $X,X'$ cofibrant, $Y,Y'$ fibrant, so that $\overset l\sim$ and $\overset r\sim$ are the same, --- we \unsure{treat} the situation in any model category)

May we find a $\overline\varphi:X'\longrightarrow Y$ \inserted{homotopic to $\varphi$,} s.th. the two triangles commute:
\[\varphi i=g,\quad p\varphi=g'\qquad?\]
\margin{$\overline\varphi\sim\varphi$,}
\figure{\begin{tikzpicture}\draw(0,1)--(0,-.7)--(.35,-1.1);\draw(0,0)--(-.25,-.7);\end{tikzpicture}}
Now this is about

\deleted{Let $\overline{X'}$ be a cylinder object over $X'$}

exactly the content of Quillen's version of ``covering homotopy extension theorem'' for simplicial closed model categories (prop. 4 of Ch. \unsure{II|I}, pg \unsure{2.9|2.4}) --- although it was a little hard to make a sense of it, the way he states it

\margin{\deleted{\unsure{iff}} There is such a possibility, iff we can find $k$ and $h$ s.th. the two resulting homotopies $p\circ k$ and $h\circ(i\otimes\unsure{J|I})^{\unsure{o}}:\ p\varphi i\longrightarrow pg=g'i$ are homotopic! This is \unsure{possibly} not always satisfied!}
\figure{\begin{tikzpicture}[scale=.5]
\draw[->](0,0)--(0,4)--(1,4);\draw(.2,2.8)--(-.2,2.8) (.2,2.65)--(-.2,2.65) (.2,2.5)--(-.2,2.5) (.2,2.35)--(-.2,2.35);
\draw(1.3,0)..controls(1.1,.1)and(1.1,.3)..(1.3,.4)--(1.3,1.1)..controls(1.4,1.3)and(1.45,1.3)..(1.3,1.5)--(1.3,2.3);
\draw(3.6,0)..controls(3.8,.2)and(3.8,.4)..(3.6,.6)--(3.6,1.2)..controls(3.5,1.35)and(3.5,1.5)..(3.6,1.65)--(3.6,2.3);
\draw[->](1.5,2.5)..controls(2,2.8)and(2.4,2.8)..(2.8,2.5);
\end{tikzpicture}}
\mspage{20}
"""
elements=[('text','top circled','b'),('text','upper paragraph','we may assume Y is a (W)-Kan object'),('display','within top paragraph','Hom_Hot(X,Y) ~= overline Hom(X,Y)'),('text','upper question','Surjectivity of (*)?'),('diagram','upper middle left','X0 -> X1 -> X2; gi to Y'),('diagram','upper middle right','Xn f_n Xn+1; gn gn+1 to blank'),('text','middle','such that gn+1 fn ~ gn'),('diagram','centre','X,Y,Xprime,Yprime; dashed phi'),('text','below centre','where i is a cofibration'),('display','below centre','phi i ~h g; p phi ~h gprime'),('text','parenthesis','we assume X,Xprime cofibrant'),('text','lower question','May we find a bar phi'),('display','lower','phi i=g, p phi=gprime ?'),('margin note','lower left','bar phi ~ phi'),('drawing','question end','branched reference stroke'),('text','lower paragraph','Now this is about'),('deletion','lower crossed line','Let bar Xprime be a cylinder'),('text','bottom','exactly the content of Quillen version'),('margin note','left rotated','There is such a possibility iff'),('drawing','left margin','reference arrow and braces'),('text','foot left','20')]
if __name__=='__main__':save(107,21,tex,elements,notes='Surjectivity of (*) via straightening a compatible-up-to-homotopy sequence. General square with cofibration i, fibration p and diagonal phi: asks for homotopic strict diagonal. Body invokes Quillen covering homotopy extension theorem and explicitly says wording was hard to make sense of. Margin qualifies strictification by compatibility of p k and h(i tensor J)^o, and doubts whether always satisfied. These must be separate research items. Both relations ~^l, ~^r differ from primes/exclamations. The page writes unbarred phi in strict equalities despite asking for bar phi. Exact chapter/page reading and margin cylinder parameter uncertain.')

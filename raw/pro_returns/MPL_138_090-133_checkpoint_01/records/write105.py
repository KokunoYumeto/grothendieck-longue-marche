from records.record_page import save
save(105,r"""\scanpage{105}
% archive foliation: 104
\uline{NB} La figure barycentrique complète est la réunion de la droite $y(=\operatorname{Im}z)=0$, et de la courbe $2x(x^2+y^2)+(-3x^2+y^2)=0$
\figure{\begin{tikzpicture}[x=.8cm,y=.65cm]
\draw(-2.7,0)--(2.15,0);\draw(-2.05,5.1)..controls(-2.2,3.2)and(-1.4,1.5)..(0,0)..controls(.75,-1.3)and(2.1,-1.7)..(2.15,0)..controls(2.2,2.0)and(.8,1.8)..(0,0)..controls(-1.1,-1.7)and(-1.9,-3.5)..(-2,-5.2);
\draw[line width=1.15pt](0,0)..controls(.7,1.7)and(2.15,2)..(2.15,0)..controls(2.1,-1.6)and(.7,-1.4)..(0,0);
\fill(0,0)circle(.085);\node at(-2.7,0){$\times$};\node at(2.15,0){$\times$};\draw(1.4,0)circle(.085);
\foreach\x in {.15,.25,.35,.47,.59,.72,.84,.98,1.13,1.22,1.62,1.75,1.9}{\draw(\x,-.08)--(\x+.04,.08);}
\node at(-2.55,-.42){$-3$};\node at(0,-.4){$0$};\node at(1.46,-.35){$1$};\node[right]at(2.15,0){$\frac32$};
\end{tikzpicture}}

$\unsure{3''|3'''}$) (dual du précédent)
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw(0,0)--(2.2,0);\fill(0,0)circle(.06);\node at(.6,0){$\times$};\fill(1.15,0)circle(.06);\node at(2.2,0){$\times$};
\node at(0,-.35){$0$};\node at(.6,.4){$\frac13$};\node at(1.2,-.35){$1$};\node at(2.3,.4){$\frac43$};\draw(4.7,0)circle(.045);\node at(4.7,-.25){$\infty$};
\end{tikzpicture}}
\[f(z)=\frac{27}{4}z(z-1)^2\]
$\deleted{\unsure{\gamma\simeq}}G=\mathfrak S_3,\quad\gamma=\{1\}$
\[\operatorname{Card}C^{\alpha}_{\mathcal C_0}=1\]
""",[
('text','top','NB La figure barycentrique complète'),('drawing','upper-left to middle','real line and nodal loop curve; -3,0,1,3/2'),('text','middle','3-double-prime) (dual du précédent)'),('drawing','middle-right','segment 0,1/3,1,4/3; infinity'),('display','middle','f(z)=27/4 z(z-1)²'),('deletion','middle-right before G','gamma ≃'),('display','middle-right','G=S3; gamma={1}'),('display','middle-lower','Card C=1')
],doubts=[('4','3-double-prime','3-triple-prime','medium'),('5','gamma ≃','cancelled before G','low')],leads='Barycentric locus for preceding cubic, explicitly union of real axis and curve 2x(x²+y²)+(-3x²+y²)=0, with nodal loop and two unbounded branches. Dual example polynomial (27/4)z(z-1)², S3, trivial gamma, one pinned map. Mathematical formula/locus candidates for actual check after freeze.')

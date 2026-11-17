from records.record_page import save
tex=r'''\scanpage{114}
% archive foliation: 113
\figure{\begin{tikzpicture}[scale=.7,line cap=round,line join=round]
\begin{scope}[shift={(1,8)}]
\draw (0,0)..controls(-1,1)and(1.3,2.5)..(2,1.8)..controls(2.7,1.2)and(1.2,-.2)..(0,0);
\draw[very thick](0,0)--(1.4,.2)--(1.2,1.2)--(2,1.8);\draw(1.2,1.2)..controls(1.8,1.2)..(2,1.8);
\foreach \p in {(0,0),(1.4,.2),(1.2,1.2),(2,1.8)}\fill\p circle(2pt);\end{scope}
\begin{scope}[shift={(5,8)}]
\draw(0,-.2)..controls(-.4,1)and(1,1.7)..(2,1.7)..controls(2.8,1.3)and(2.2,-1)..(1.5,-.4)..controls(.6,-.8)..(0,-.2);
\draw(2,1.7)--(1.25,.85)--(1.5,-.4);
\foreach \p in {(0,-.2),(2,1.7),(1.65,1.3),(1.25,.85),(1.5,-.4)}\fill\p circle(2pt);
\node at(.7,.7){$5$};\node at(1.9,.65){$4$};\end{scope}\node at(9,8.7){$3$};
\draw(-.8,5.2)..controls(-.8,6.1)and(.4,6.4)..(.4,5.8);
\begin{scope}[shift={(3,5.6)}]
\draw[thick](0,0)..controls(-.6,1.2)and(1.7,1.8)..(1.5,.35)..controls(1,-.7)..(0,0);
\draw(0,0)..controls(1.5,.2)and(.8,1.1)..(0,0);\draw(1.5,.35)--(2.3,.3);
\foreach\p in{(0,0),(.35,1.05),(1.5,.35)}\fill\p circle(2pt);
\node at(.55,.35){$1$};\node at(1, .9){$3$};\node at(1.9,-.15){$\unsure{4|5}$};
\draw(-.6,1.5)..controls(-1.8,-2)and(4,-2)..(2.5,.9)..controls(1.7,2.4)..(-.6,1.5);\node at(1.4,-1.2){$8$};\end{scope}
\begin{scope}[shift={(.5,3.7)}]
\draw(0,0)..controls(-.6,.9)and(.2,2)..(1,1.3)..controls(2,.3)and(1,-.8)..(0,0);
\draw(-.6,-.6)--(0,0)--(.9,.9);\draw(1.5,.55)--(2.3,.55);
\foreach\p in{(0,0),(-.05,.7),(.55,1.4),(1.5,.55)}\fill\p circle(2pt);
\draw(.2,.25)--(.4,.6)--(.6,.6)--(.7,.8)--(.9,.9)--(.85,.65);
\node at(.8,.3){$3$};\node at(2,.05){$\unsure{5|4}$};\end{scope}
\begin{scope}[shift={(6.3,6.2)}]
\draw[very thick](-.7,0)--(2.1,0);\draw(0,0)--(0,1.2);
\foreach\p in{(0,0),(0,.65),(0,1.2),(.65,0),(1.3,0),(2,0)}\fill\p circle(2pt);
\draw(-.7,-.2)--(-.95,-.25)--(-.7,-.3);\draw(1.9,0)--(2.1,.13)--(2.25,-.07);
\end{scope}
\begin{scope}[shift={(6.3,4.3)}]
\draw(-.7,0)--(1.7,0);\draw(0,0)--(0,1.1);
\foreach\p in{(0,0),(0,.6),(.5,0),(1.05,0)}\fill\p circle(2pt);
\draw(-1,1.1)..controls(-2,-1.5)and(.2,-2.4)..(2.7,-1.1)..controls(4,1.8)and(-.1,2.2)..(-1,1.1);
\node at(.5,-.7){$\deleted{\unsure{9}}$};\node at(1.6,-1.9){$9$};\end{scope}
\begin{scope}[shift={(10.3,6.8)}]
\draw(-.7,0)--(1.2,0);\draw(0,-.5)--(0,.55);\foreach\p in{(-.7,0),(0,0),(.65,0),(1.2,0)}\fill\p circle(1.5pt);\draw(0,.5)--(.1,.65)--(-.05,.6);
\end{scope}
\begin{scope}[shift={(10.3,5)}]\draw(-.45,.3)--(.35,-.25);\draw(-.35,-.4)--(0,0)--(0,.5);\end{scope}
\begin{scope}[shift={(10.3,1.8)}]
\draw[thick](-.9,0)--(.7,0);\draw(0,0)--(0,.5);\foreach\p in{(-.5,0),(0,0),(.7,0)}\fill\p circle(2pt);
\draw(0,-.3)ellipse(1.7 and1);\node at(0,-.7){$6$};\node at(0,.95){$\deleted{\unsure{4}}$};\end{scope}
\draw(6.5,0)--(7.1,0);\fill(7.1,0)circle(1.5pt);
\end{tikzpicture}}
\figure{\begin{tikzpicture}\fill(0,0)circle(2pt);\draw(0,0)--(1,0);\node[right]at(2,0){degré $1$};\end{tikzpicture}}
\deleted{\figure{\begin{tikzpicture}\draw(0,0)--(1,0);\draw(.5,0)--(.6,1);\foreach\p in{(.5,0),(.55,.5),(.6,1)}\fill\p circle(2pt);\draw(0,.1)--(.8,.3)--(.1,.2)--(.8,.6)--(.1,.4)--(.9,.9);\end{tikzpicture}}}
\[
n=\sum_s q_s=\sum_f p_f
\]
\uline{degré $1$}\qquad $\unsure{\varphi(1)|\varphi(n)}=2$
\figure{\begin{tikzpicture}\fill(0,0)circle(2pt);\draw(.15,0)--(1,0);\end{tikzpicture}}
\uline{degré $2$}\quad a) $1$ seul sommet d'ordre $2$
\figure{\begin{tikzpicture}\draw(-1,0)--(1,0);\fill(0,0)circle(2pt);\node at(0,.45){\deleted{\unsure{2 arêtes}}};
\begin{scope}[shift={(3,0)}]\draw(0,0)..controls(-1,1.5)and(1.5,1.5)..(0,0);\fill(0,0)circle(2pt);\end{scope}
\draw(4.5,.2)--(5.2,.1)--(4.5,.25)--(5.3,.05);\end{tikzpicture}}
b) $2$ sommets d'ordre $1$
\figure{\begin{tikzpicture}\draw(0,0)--(1,0);\fill(0,0)circle(2pt);\fill(1,0)circle(2pt);\end{tikzpicture}}
\uline{degré $3$}\quad a) $1$ sommet d'ordre $3$
\figure{\begin{tikzpicture}\draw(-1,0)--(0,0)--(.5,.6);\draw(0,0)--(.4,-.6);\fill(0,0)circle(2pt);
\draw(2,-.2)--(2.6,.1)..controls(2.6,1.6)and(4.1,.3)..(2.6,.1);\fill(2.6,.1)circle(2pt);\end{tikzpicture}}
b) $2$ sommets, d'ordre $1$ et $2$
\figure{\begin{tikzpicture}\draw(0,0)ellipse(.6 and.35);\draw(-.5,.3)--(.3,.25)--(-.4,.1)--(.6,.1)--(-.4,-.15)--(.2,-.25);
\draw(1.3,0)--(3.4,0);\fill(1.3,0)circle(2pt);\fill(2.3,0)circle(2pt);\end{tikzpicture}}
\uline{degré $4$}\quad a) $1$ sommet d'ordre $4$
\figure{\begin{tikzpicture}
\draw(-.7,-.45)--(.7,.25);\draw(-.6,.45)--(.4,-.45);\fill(0,0)circle(2pt);
\begin{scope}[shift={(2.5,0)}]\draw(-.7,0)--(0,0)--(0,.65);\draw(0,0)..controls(1.9,.7)and(.6,-2.1)..(0,0);\fill(0,0)circle(2pt);\end{scope}
\begin{scope}[shift={(.7,-1.5)}]\draw(0,0)..controls(-2,0)and(.7,1.3)..(0,0)..controls(1.8,1)and(1.5,-1.6)..(0,0);\fill(0,0)circle(2pt);\end{scope}
\begin{scope}[shift={(3.5,-1.5)}]\draw(0,.6)--(-.2,0)--(.2,-.3);\draw(-.2,0)..controls(-1,-1.5)and(1.4,-1.1)..(-.2,0);\fill(-.2,0)circle(2pt);\end{scope}
\draw(-2,-1)..controls(-.5,-.6)and(-1,-2.5)..(3.8,-2.2);
\end{tikzpicture}}
b) $1$ sommet d'ordre $3$, $1$ d'ordre $1$
\figure{\begin{tikzpicture}\draw(0,0)--(1,0)--(1.7,.4);\draw(1,0)--(1.6,-.4);\fill(0,0)circle(2pt);\draw[fill=white](1,0)circle(2pt);\end{tikzpicture}}
\deleted{\figure{\begin{tikzpicture}
\draw(0,0)--(1,0)--(1.8,.4);\draw(1,0)--(1.8,-.3);\fill(0,0)circle(2pt);\fill(1,0)circle(2pt);
\draw(0,-1.3)--(1,-1.3)--(1.5,-.5);\draw(1,-1.3)..controls(2.5,-1.3)and(1,-2.3)..(1,-1.3);\fill(0,-1.3)circle(2pt);\fill(1,-1.3)circle(2pt);
\foreach\x in{0,.2,...,1.7}\draw(\x,-1.7)--(\x+.5,-.6);
\draw(0,.3)--(-.3,-.7)--(.8,.4)--(.4,-.8)--(1.5,-.2)--(1.7,-.6)--(2.5,-.5);
\node at(2.6,-1.4){\unsure{rigide}};\draw(1.9,-1.8)--(3.3,-1.9)--(3.4,-1.7);
\end{tikzpicture}}}'''
e=[('figure','upper left','oval with doubled internal edge'),('figure','upper centre','oval marked 5 and 4'),('number','upper right','3'),('figure','left','isolated arc'),('figure','upper middle','nested loop 1,3,4/5; circled 8'),('figure','middle left','loop 3; exterior 5'),('figure','middle centre','five-point branched line'),('figure','middle right','cross graph'),('figure','right','four rays'),('figure','middle lower','branched line circled 9'),('figure','lower right','three-point graph circled 6'),('cancelled_number','above circled6','4'),('figure','above crease','short segment'),('figure','below crease left','degree1 segment'),('cancelled_figure','below crease right','branched graph'),('formula','middle lower','n=sum q_s=sum p_f'),('text','lower','degree1'),('formula','degree1','phi(1)=2'),('figure','degree1','single endpoint'),('text','lower','degree2 a)'),('figure','degree2','segment and loop'),('deleted_text','degree2','2 arêtes'),('cancelled_figure','degree2 right','small horizontal strokes'),('text','lower','degree2 b)'),('figure','degree2b','two endpoints'),('text','lower','degree3 a)'),('figure','degree3a','Y and loop with tail'),('text','lower','degree3 b)'),('cancelled_figure','degree3b','scribbled oval'),('figure','degree3b','line with2vertices'),('text','lower','degree4 a)'),('figure','degree4a','four rays'),('figure','degree4a','loop with two outside tails'),('figure','degree4a','double loop'),('figure','degree4a','loop with inner and outer tail'),('figure','lower separator','curved separator'),('text','bottom','degree4 b)'),('figure','bottom left','Y with endpoint'),('cancelled_figure','bottom right','Y and loop-tail diagrams'),('deleted_text','bottom right','rigide')]
save(114,tex,e,doubts=[('upper figures','overwritten labels 4/5 and 5/4','both layers retained as alternatives','low'),('degree1','phi(1)=2','phi(n)=2; glyph heavily overwritten','low'),('degree2 margin','2 arêtes','cancelled cursive','low'),('bottom','rigide','cancelled cursive partly covered','medium')],leads='Enumeration sketches of maps in degrees1–4; branching/face counts, n=sum_s q_s=sum_f p_f. Many rejected drawings retained. No proof of completeness on this sheet.')

from save_page import save_page
save_page(92,r'''\scanpage{92}
% archive foliation: 91
Si $k$ n'est pas de car. $0$, on ne peut en
général aller en sens inverse, et
$R(\mathbf N,k)\xrightarrow{\Lambda}k[[t]]$ n'est \deleted{en général} pas injectif,
[$k$ corps de car. $>0$]

\figure{\begin{tikzpicture}\draw (0,0)--(1.1,-.04)--(2.3,-.04);\end{tikzpicture}}

On voit \deleted{que} par la formule de
Lefschetz-Weil-Grothendieck que la connaissance
de la fonction $L$ de $\unsure{(X,F)|X}$ algébrique
sur $\mathbf F_p$, \inserted{à coeff dans $F$,} \uline{équivaut} à celle de l'élément
\[
\uline{\chi}(F)=\sum(-1)^i\,\mathrm{cl}\,H^i_!(\bar X,\bar F)
\quad\text{de }R(\mathbf N,\mathbf Q_\ell)
\]
[car essentiellement cette fonction $L$ est l'image
de $\uline{\chi}(F)$ dans $1+\mathbf Q_\ell[[t]]^+$]. Lorsque
on admet les conjectures de Weil, et $F$
\inserted{est un motif,}
$\uline{\chi}(F)$ se décompose suivant les poids en
\[
\sum(-1)^i\,\deleted{\unsure{\mathrm{cl}}}\uline{h}^i_!(F),
\qquad\uline{h}^i(F)\in R(\mathbf N,\mathbf Q_\ell),
\]
et la \deleted{\unsure{connaiss.}} connaissance de $L(X,F)(t)$
\uline{équivaut} à celle des $\uline{h}^i(F)$ : les $\uline{h}^i(F)$
correspondent à la décomposition de $L(X,F)$
''',[
('top','text','Si k n’est pas de car. 0, on ne peut en général aller en sens inverse'),
('upper','formula','R(N,k) -> k[[t]] via Lambda; pas injectif'),
('upper','text','k corps de car. >0'),
('upper-middle','drawing','Short horizontal separator'),
('middle','text','On voit par la formule de Lefschetz-Weil-Grothendieck'),
('middle','text','connaissance de la fonction L de (X,F)/X algébrique sur F_p'),
('middle','formula','underlined chi(F)=sum (-1)^i cl H^i_!(Xbar,Fbar) in R(N,Q_l)'),
('lower-middle','text','fonction L image de chi(F) dans 1+Q_l[[t]]^+'),
('lower','text','conjectures de Weil, F est un motif; décomposition suivant les poids'),
('lower','formula','sum (-1)^i underlined h^i_!(F); h^i(F) in R(N,Q_l)'),
('bottom','text','connaissance de L(X,F)(t) équivaut à celle des h^i(F)'),
('bottom','text','les h^i(F) correspondent à la décomposition de L(X,F)')
],remarks='Whole and halves read; X/F phrase and cancelled cl in the sum enlarged. Subscript ! visible in the first h expression but not silently supplied to following h expressions. Divider reproduced.')

from save_page import save_page
save_page(95,r'''\scanpage{95}
% archive foliation: 94
savoir les ``invariants birationnels fondamentaux''
\inserted{relativement à $\mathbf F_p$,}
\deleted{de} envisagés dans les notes sur les \uline{Motifs}.

Il semblerait opportun d'étudier \deleted{\unsure{si}}
\inserted{le cas des coefficients $F$ généraux et de voir si,}
pour un morphisme $f:X\longrightarrow Y$
disons lisse \deleted{projectif}\inserted{propre}, \inserted{$F$ \unsure{lct|ct} tordu sur $X$,} la connaissance de
\deleted{$\unsure{H|\zeta}$}
$L(X,F)$ modulo $L(f^{-1}(Y'),F)$,
pour $Y'$ propre dans $Y$, permet de récupérer
les invariants birationnels fondamentaux
de $(X_K,\unsure{F\vert_{X_K}|F\vert_K})/K$
[$K$ corps des fonctions de
$Y$]. \uline{Dans quelle mesure faut-il}
\uline{faire les hypothèses $f$ lisse propre}, et $F$
\uline{ct tordu} pour obtenir des énoncés
de cette nature ??
\figure{\begin{tikzpicture}[scale=.45]
\draw (0,0)--(-.04,2.3)--(-.08,4.6) (.16,0)--(.11,2.3)--(.09,4.6);
\end{tikzpicture}}
''',[
('top','text','invariants birationnels fondamentaux relativement à F_p'),
('upper','text','envisagés dans les notes sur les Motifs'),
('upper-middle','text','Il semblerait opportun d’étudier le cas des coefficients F généraux'),
('middle','formula','f:X -> Y'),
('middle','text','disons lisse projectif/propre; F lct/ct tordu sur X'),
('middle','formula','L(X,F) modulo L(f^-1(Y’),F)'),
('middle','text','Y’ propre dans Y; récupérer les invariants birationnels fondamentaux'),
('lower-middle','formula','(X_K,F|X_K)/K'),
('lower-middle','text','K corps des fonctions de Y'),
('lower','text','Dans quelle mesure faut-il faire les hypothèses f lisse propre, F ct tordu ??'),
('left margin beside central paragraph','drawing','Two vertical emphasis strokes')
],remarks='Whole and both halves inspected; overwritten projectif/propre and generic-fibre coefficient expression enlarged. Lower region otherwise blank. Final question marks and emphasis retained.')

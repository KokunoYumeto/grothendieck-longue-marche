from audit_tools import *
old=r'''% The large left parenthesis spans this and the following A-W line.
(\quad et \uline{shuffles} est (anti)-commutative

A-W - est seulement comm à homotopie près'''
new=r'''\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0] (aw) at (0,0) {\begin{tabular}{l}
et \uline{shuffles} est (anti)-commutative\\[10pt]
A-W - est seulement comm à homotopie près
\end{tabular}};
\draw ([xshift=-6pt,yshift=-1pt]aw.north west)
 .. controls ([xshift=-19pt,yshift=-15pt]aw.north west) and ([xshift=-19pt,yshift=-3pt]aw.south west)
 .. ([xshift=-2pt,yshift=-5pt]aw.south west);
\end{tikzpicture}}'''
finish(360,replacements=[(old,new)],note='Second reading confirms the two-line scope of the left parenthesis; its first-pass rendering was only a baseline character plus a comment, so it is now drawn as the full curved stroke already recorded in the opening-parenthesis change row and inventory. Rechecked the singular objet, N subscript doubt, headless integral descent, two separator strokes, three primes, cancelled trial factor count, wave above crossed arrow, tildes on Z, struck arrow after pt, German spelling/case, two missing outer Hom closes, right brace and insertion pour X variable. No new reading beyond the already documented parenthesis scope.')

import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{89}
% archive foliation: 91
\figure{\begin{tikzpicture}\draw (0,0)--(.08,-2.8)--(.17,-5.5)--(.3,-7.2);\end{tikzpicture}}
\uline{Théorème} Soit $k$ un corps alg. clos de car. $\ne2$,
\deleted{Soit $I$ un ens de card $4$, d'où $J$ de card. $3$ et $V=V(J)$. Considérons}

Considérons le groupoïde des $(X,I\hookrightarrow X)$, où $X$ est
une droite projective sur $k$, \deleted{\unsure{tel}}\inserted{$I$ de card $4$}.
Ce groupoïde est équivalent à celui des couples $(I,\zeta\in Z(J(I))^*)$,
en associant à ce couple
\[
X=X(I)\wedge_{\underbrace{V(J(I))}_{\text{ou }V(I)}}t(\zeta,I).
\]
\margin{où $t(\zeta,I)$ est le $V(I)$-torseur $I\wedge X(I)_\zeta^{-1}$}
$I\hookrightarrow X$ est la fibre \inserted{$X_\zeta$} de $X$ en $\zeta$, compte tenu que
\[
\begin{gathered}
X/V(I)\simeq X(I)/V(I)\simeq\unsure{Z|X}(J)\\
X_\zeta\simeq X(I)_\zeta\wedge t(\zeta,I).
\end{gathered}
\]

(\deleted{\unsure{Si}} si $I$ est muni d'un pt $i_0$, on a une description
de $X$ comme $X(I)\wedge_{V(I)}X(I)_\zeta^{-1}$ ; c'est isom. à $X(I)$ une
fois choisi un \unsure{sommet|élément} de $X(I)$ au dessus de $\zeta$.

De façon plus générale, \deleted{\unsure{donc}} la donnée d'un
isom. ``admissible'' $X\simeq X(I)$ équivaut à celle d'un
$V$-isom $I\simeq\deleted{\unsure{Y}}X(I)_\zeta$.
"""
save(89,tex,[('drawing','left of theorem','vertical delimiting line'),('text','top theorem','Théorème Soit k un corps alg. clos'),('deletion','top two lines','Soit I un ens de card 4'),('text','upper','Considérons le groupoïde'),('deletion','after sur k','tel'),('insertion','above deletion','I de card 4'),('display','middle','X=X(I) wedge V(J(I)) t(zeta,I)'),('margin note','right of display','où t(zeta,I) est le V(I)-torseur'),('text','middle','I into X est la fibre'),('insertion','above fibre','X zeta'),('display','middle lower','X/V(I) isomorphic X(I)/V(I) isomorphic Z(J)'),('text','below theorem','si I est muni d’un pt i0'),('deletion','before si','Si'),('text','lower','De façon plus générale'),('deletion','before la donnée','donc'),('deletion','last formula before X(I)','Y')],doubts=[('after sur k','tel','Crossed short word beneath insertion I de card 4.','low'),('quotient curve','Z(J)','X heavily overdrawn with horizontal bars, as preceding page.','medium'),('choice above zeta','sommet','élément; initial and medial strokes do not resolve the word, retained without mathematical correction.','low'),('before la donnée','donc','Crossed word could be on.','low'),('last formula','Y','Overwritten capital preceding X(I), may simply be a cancelled X.','low')],abbreviations=[('alg.','algébriquement'),('car.','caractéristique'),('ens','ensemble'),('card','cardinal'),('pt','point'),('isom.','isomorphisme')],leads=['Theorem states equivalence of the groupoid of four-point projective lines with pairs (I,zeta in Z(J(I)) star); compare retained automorphism groups and implicit torsor data.','Choice of a point of I trivializes the I torsor, but choosing a point above zeta remains noncanonical; the last paragraph spells out admissible isomorphisms.'])

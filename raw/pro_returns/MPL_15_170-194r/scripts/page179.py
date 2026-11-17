from record_page import record

record(179, r'''\scanpage{179}

\deleted{On peut supposer $X$ irréductible de pt générique $\eta$.
L'inclusion $\unsure{\eta-X|\eta\to X}$ définit une suite spectrale
(pour la cohomologie étale)
\[
H^*(\eta,G_m)\Leftarrow E_2^{pq}=H^p(X,R^qi_*(G_m))
\]
Or \deleted{\unsure{comme les}} comme les $H^q(\eta,G_m)$ et les fibres de $R^qi_*(G_m)$, qui s'explicitent par de la cohomologie galoisienne, sont des groupes de torsion pour $q>0$,
\unsure{je trouve que} \deleted{\unsure{il en va de même des groupes}}
\[
(*)\qquad H^p(X,R_X^*)\quad
\deleted{,\quad R_X^*=R\unsure{i_*}(G_m)}
\]
\inserted{est un groupe de torsion pour $p>0$,}
où $R_X^*=\deleted{\unsure{Ri_*}}i_*(G_m)$ est le faisceau (étale) des fonctions rationnelles \inserted{non nulles} sur $X$. \deleted{(\unsure{ceci étant}}}

D'autre part, on a \inserted{si $X$ est \inserted{noethérien} ``sans idéaux premiers immergés'',} la suite exacte
\diagram{\[
\text{(1.1.)}\qquad
\begin{tikzcd}[column sep=large]
0 \arrow[r] & G_{mX} \arrow[r] & R_X^* \arrow[r] & \underline{\operatorname{Div}}_X \arrow[r] & 0
\end{tikzcd}
\]}
où $\underline{\operatorname{Div}}_X$ est le faisceau (\inserted{pour la top.} étale) des diviseurs (de Cartier) sur $X$, ce qui \deleted{\unsure{veut dire que}} \inserted{implique} compte tenu de ce que
\diagram{\[
\begin{tikzcd}[column sep=large]
H^{\unsure{i}}(X,\underline{\operatorname{Div}}_X) \arrow[r,"\partial"] & H^{i+1}(X,G_{mX})
\end{tikzcd}
\]}
\margin{\uline{\unsure{donne le|donner le}} \uline{corollaire} \unsure{3.4.}}
est bijectif modulo torsion \deleted{pour} si $i\geq 1$. \uline{Ainsi}
\deleted{\unsure{pour en montrer l'utilité}} L'hypothèse de factorialité d'autre part implique \deleted{l'isomorphisme} qu'on a un isomorphisme de faisceaux étales :

\margin{178}
''', [
('deletion','large crossed block upper half','On peut supposer X irréductible'),
('text','cancelled block opening','On peut supposer X irréductible'),
('text','cancelled block second paragraph','L’inclusion η-X'),
('display','cancelled block first display','H*(η,Gm) ⇐ E2pq'),
('deletion','cancelled block line Or','comme les'),
('text','cancelled block central paragraph','Or comme les Hq'),
('deletion','cancelled block before (*)','il en va de même des groupes'),
('display','cancelled block (*)','Hp(X,RX*)'),
('deletion','cancelled block right of (*)','RX* = Ri*(Gm)'),
('insertion','above right of (*)','est un groupe de torsion pour p>0'),
('text','cancelled block definition','où RX* = i*(Gm)'),
('deletion','before i*(Gm)','Ri*'),
('insertion','above fonctions rationnelles','non nulles'),
('deletion','end of cancelled block','ceci étant'),
('text','start of live paragraph','D’autre part, on a'),
('insertion','above la suite exacte','si X est sans idéaux premiers immergés'),
('insertion','above si X est','noethérien'),
('diagram','display (1.1.)','0 → GmX → RX* → DivX → 0'),
('text','after (1.1.)','où DivX est le faisceau'),
('insertion','above étale','pour la top.'),
('deletion','after ce qui','veut dire que'),
('insertion','above deleted phrase','implique'),
('diagram','connecting map','Hi(X,DivX) → Hi+1(X,GmX)'),
('margin note','left of connecting map and following text','donne le corollaire 3.4.'),
('text','below connecting map','est bijectif modulo torsion'),
('deletion','after torsion','pour'),
('deletion','before L’hypothèse','pour en montrer l’utilité'),
('text','last paragraph','L’hypothèse de factorialité'),
('deletion','last paragraph','l’isomorphisme'),
('margin note','bottom left pencil','178')
], sheet_kind='cancelled_draft', observations='''The upper passage is cancelled as a single block by a perimeter and diagonal strokes; its internal deletions and insertions are separately preserved. Lower half remains live. Sheet classified cancelled_draft because of the cancelled draft occupying its upper half; this is not a claim that the lower text is cancelled. Whole page and supplied halves read, with enlarged crops of cancelled lines, the noethérien insertion, the margin, and the bottom paragraph. In the upper inclusion the stroke has no certain arrowhead, hence dash first. The insertion noethérien belongs after est in the lower hypothesis, not to fonctions rationnelles. The last cancelled phrase before L’hypothèse is particularly difficult and remains low-confidence. The final line is at the physical bottom edge but is readable as isomorphisme de faisceaux étales. No context read.''')

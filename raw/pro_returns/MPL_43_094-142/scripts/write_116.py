from page_work import save_page
text=r'''\scanpage{116}
\[
H^*(\Delta^2T(A))\Longleftarrow(H^p\Delta^2)(H^q(K,A))
\]
\[
E_2^{pq}=\deleted{\unsure{H^p(\Delta^2H^qA)}}
\left\{\begin{array}{l}0\text{ si }q\neq0,\ p\unsure{\neq|=}q\\\phantom{0}\end{array}\right.
\]
\figure{\begin{tikzpicture}
\draw[line width=1pt] (-1.7,0)--(1.5,.03);\node[right] at(1.7,0){$p$};
\draw (0,-1.4)--(-.08,1.7);\node[above] at(-.2,1.7){$q$};
\draw[line width=1pt] (-.8,0)--(-.85,.8)--(-.05,.85);
\draw (-1.4,1.1)--(0,0);\draw (-.85,.8)--(0,0);
\draw (-.85,.72)--(-.05,.78);\draw (-.8,.07)--(0,.02);
\fill (-.8,0) circle (.07);\fill(0,0) circle(.08);\fill(-.05,.85) circle(.08);\fill(-.85,.8) circle(.035);
\end{tikzpicture}}
\[
\left\{\begin{array}{l}
(H^{-1}\Delta^2)(H^0(K,A))\subset\pi_1(A)\\[1em]
(H^0\Delta^2)(H^0(K,A))\\[1em]
(H^0\Delta^2)(H^1(k,A))=H^1(k,A)
\end{array}\right.
\]
\margin{\uline{compact}}
\margin{\deleted{\unsure{qui est}}\inserted{\uline{est le \unsure{plus gr}}}
\uline{\unsure{complété}} de \uline{fini}}

$\Delta T(\mathcal P_\bullet)$ et $T(\mathcal P'_\bullet)$ \uuline{sont $=\unsure{0|\Delta}$.}
\[
\boxed{\underline{\underline{\operatorname{Ext}}}^{0}(\unsure{\mathcal P},\mathbb Q/\mathbb Z)=0}
\]
\[
\operatorname{Ext}(H
\]
\diagram{\begin{tikzcd}
T(\mathcal P')&\Delta T(\mathcal P_\bullet)\arrow[l,Leftarrow]
\end{tikzcd}}
\margin{\figure{\begin{tikzpicture}\draw (0,1.2)--(.06,.1)--(0,0);\end{tikzpicture}}}

\deleted{\uline{Remarque} 2.7. J'ignore si les conditions
d'équidimensionnalité de 1.1. ii) sont
essentielles; de $=$ dans 2.6.

\uline{Prop.} 2.8. Continuité des Cohen-Macaulay.}
\mspage{115}
'''
save_page(116,text,[('display','top spectral sequence','Hstar(Delta2T(A)) ⇐ (HpDelta2)(Hq(K,A))'),('display','upper E2 partial cases','E2pq=0 si q non0,p nonq'),('deletion','upper E2 attempted expression','Hp(Delta2HqA)'),('drawing','middle left p q graph','four vertices on square, two axes and diagonal'),('display','middle brace three terms','H-1Delta2 H0; H0Delta2 H0; H0Delta2 H1'),('margin note','right first expression','compact'),('margin note','right second expression','est le plus gr complété de fini'),('deletion','right second expression old text','qui est'),('insertion','right second expression above','est le plus gr'),('text','middle lower','DeltaT(P bullet) et T(Pprime bullet) sont =0'),('display','lower boxed','double-underlined Ext0(P,Q/Z)=0'),('display','lower unfinished','Ext(H'),('diagram','lower left-pointing map','T(Pprime) ← DeltaT(Pbullet)'),('drawing','beside lower map','one-sided vertical bracket'),('deletion','bottom opposite orientation cancelled block','Remarque2.7 J’ignore si les conditions ... Prop2.8'),('text','bottom opposite orientation first paragraph','Remarque2.7 J’ignore si les conditions d’équidimensionnalité'),('text','bottom opposite orientation second heading','Prop2.8 Continuité des Cohen-Macaulay'),('text','bottom left page number','115')],observations='Whole and both halves read, with rotation of the opposite-facing bottom note and enlarged right margin. The bottom remark and proposition heading are struck as a block. The ditto sign after de is retained literally as an equals sign. The thin-versus-thick strokes in the p,q graph are drawn, including the diagonal and all four visible junctions. The right-hand marginal wording is low confidence and has not been supplied from mathematical expectation.')

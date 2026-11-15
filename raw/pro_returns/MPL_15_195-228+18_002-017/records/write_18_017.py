from record_page import save
save(18,17,'text',r'''
\margin{\unsure{faire le raisonnement}}
\figure{\begin{tikzpicture}\draw (0,0)--(0,1.3);\draw (.08,0)--(.08,1.3);\end{tikzpicture}}
Alors on voit que $P_{an}(1_Y)$ est la classe de \unsure{Ch.|Coh.} sur $X-a$ représentée par la forme diff. $\dfrac{dz}{z}$, et par suite \deleted{\unsure{on a}} si $P_{an}(1_Y)=\lambda P_{top}(1_Y)$, on a
\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\lambda={} & \displaystyle\int_C P_{an}(1_Y) & {}={} & \displaystyle\int_C\frac{dz}{z} & {}=2i\pi\\
&&\text{cercle unité \deleted{\unsure{ord.}} orienté.}\arrow[ul,bend left=15]\arrow[ur,bend right=15]&&
\end{tikzcd}}
Donc
\[
\boxed{P_{an}\left(\frac{1}{2i\pi}1_Y\right)=P_{top}(1_Y).}
\]
\[
\boxed{\left\{\begin{aligned}
P_{top}(1_Y)&=\frac{1}{2i\pi}P_{an}(1_Y)\\
P_{an}(1_Y)&=2i\pi P_{top}(1_Y).
\end{aligned}\right.}
\]
\figure{\begin{tikzpicture}\draw[->] (0,.10)..controls(2,.07)and(4,.17)..(7,.1);\draw(0,0)..controls(2,-.05)and(4,.05)..(7,0);\end{tikzpicture}}
\uline{\unsure{Cor.|Gén.}} Considérons le diagramme
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
H_{\unsure{a|Z}}^{i+p}(X,\mathbf Z)\arrow[r] & H_{\unsure{Z|a}}^{\unsure{i}+p}(X,\mathbf C)\arrow[r,"\text{De Rham}","\sim"'] & H^{\unsure{i}+p}(X,\Omega_X)\\
H_{\unsure{Z}}^i(Y,\mathbf Z)\arrow[u,"P_{top}"]\arrow[r] & H_{\unsure{Z}}^{\unsure{i|*}}(\unsure{Y|X},\mathbf C)\arrow[u,"P_{top}"]\arrow[r,"\substack{\deleted{\unsure{DR}}\\\sim}","\frac{1}{(2i\pi)^p}\,\text{can.}"'] & \underline{\underline H}_{\unsure{Z}}^{\unsure{i|*}}(\unsure{Y|X},\Omega^\bullet_{\unsure{Y|X}})\arrow[u,"P_{an}"]
\end{tikzcd}}
\uline{Il est commutatif}, i.e. la formule ci-dessus est valable \uline{globalement}, et en remplaçant $1_Y$ par une classe de Coh. quelc. \unsure{Provient} de la comm. de
\mspage{16}
''',[
('drawing','upper left margin','double vertical rule'),
('text','top','Alors on voit que'),
('diagram','upper middle','lambda = integrals; cercle unité'),
('text','middle','Donc'),
('display','middle','boxed P_an(1/(2i pi) 1_Y)'),
('display','middle','boxed brace P_top; P_an'),
('drawing','middle','two horizontal strokes; upper arrowhead'),
('text','lower middle','Cor. Considérons le diagramme'),
('diagram','lower middle','H^{i+p}; H^i; P_top; P_an'),
('text','bottom','Il est commutatif'),
('text','bottom left','16')
], 'Whole page and both supplied halves inspected; upper, diagram and bottom crops enlarged manually. No OCR.')

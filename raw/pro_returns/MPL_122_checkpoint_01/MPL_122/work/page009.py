from record import save
save(9,r'''
\scanpage{9}
Ecrivons aussi les 2 suites exactes relatives à l'inclusion $P\subset W$. On a
\diagram{\begin{tikzcd}[column sep=small]
\cdots\arrow[r]&H^i_P(W,F)\arrow[r]\arrow[d,"{\deleted{\simeq}}"]&H^i(W,F)\arrow[r,dash]&H^i(W-P,F)\arrow[r,dash]\arrow[d,phantom,"="{rotate=90}]&\cdots\\
&\deleted{H^i_{\unsure{!}}(\mathring P)}&&H^i(\mathring Q,F)\\
&&&H^i(Q,F)\arrow[u,"\simeq"]
\end{tikzcd}}
\margin{\deleted{\unsure{si} \unsure{compact}}}

Or, si $\widetilde P$ est un petit épaississement de $P$ dans $W$, alors l'inclusion $P\longrightarrow\widetilde P$ induit, on le sait
\figure{\begin{tikzpicture}[scale=.8]
\begin{scope}[rotate=-30]
\draw (0,0) ellipse (1.2 and 1.6);\draw (0,.05) ellipse (.9 and 1.3);
\draw (-.35,1.52)--(-.31,1.27) (.05,1.6)--(.05,1.35) (.45,1.47)--(.37,1.23) (.8,1.17)--(.64,1.04) (1.05,.77)--(.82,.6) (1.18,.22)--(.91,.15) (1.18,-.32)--(.88,-.3) (.98,-.9)--(.75,-.65) (.62,-1.37)--(.48,-1.07) (.15,-1.58)--(.1,-1.23) (-.35,-1.52)--(-.3,-1.18) (-.8,-1.17)--(-.64,-.91) (-1.12,-.57)--(-.86,-.42) (-1.18,.27)--(-.9,.25) (-1,.9)--(-.75,.78);
\end{scope}
\node at (0,.1) {$P$};
\draw (1.38,1.65) .. controls (1.7,1.65) and (1.15,.25) .. (1.28,-.1) .. controls (.9,-.25) and (.35,-1.85) .. (-.2,-1.9);
\node at (1.65,.35) {$\widetilde P$};
\end{tikzpicture}}
\diagram{\begin{tikzcd}[column sep=large]
H^i_P(\widetilde P,F)\arrow[r,"\simeq"]\arrow[d,phantom,"\simeq"{rotate=90},"\text{excision}"']&H^i(\widetilde P\mathbin{\mathrm{mod}}\partial\widetilde P,F)\arrow[d,phantom,"\simeq"{rotate=90}]\\
H^i_P(W,F)&H_!^i(\mathring P,F)
\end{tikzcd}}
Donc la suite exacte pour l'inclusion $P\subset W$ peut s'écrire
\diagram{\begin{tikzcd}[column sep=small]
\cdots\arrow[r,dash]&H_!^i(\mathring P,F)\arrow[r,dash]\arrow[d,phantom,"\simeq"{rotate=90}]&H^i(W,F)\arrow[r,dash]&H^i(Q,F)\arrow[r,dash]&\cdots\\
&H^{n-i}(P,F^\vee\otimes\unsure{\mathcal T|\tau}_W)^\vee
\end{tikzcd}}
\mspage{8}
''',[
('text','top','Ecrivons aussi les 2 suites exactes'),('diagram','upper','H^i_P(W,F) to H^i(W,F) to H^i(W-P,F)'),('deletion','upper diagram lower left','H^i_!(interior P) and isomorphism'),('margin note','left upper','cancelled si compact'),('deletion','left upper','si compact'),('text','middle','Or si P tilde est un petit épaississement'),('drawing','left middle','P and enlarged P tilde with hatching and brace'),('diagram','middle','excision and relative/compact-support cohomology'),('text','lower middle','Donc la suite exacte pour l’inclusion'),('diagram','lower','H_!^i(interior P,F) - H^i(W,F) - H^i(Q,F)'),('text','bottom left','8')],
[('cancelled upper-left margin','si compact','Two very small words heavily crossed out; alternative reading not secure.','low'),('cancelled cohomology support','!','Subscript overwritten by dense strokes.','low'),('final sequence','dash connections','Arrowheads not visible on these horizontal strokes.','medium'),('final duality orientation sign','calligraphic T','tau, as in scan 007.','medium')],
['Excision for a thickening and identification of supported cohomology with compact-support cohomology are asserted with on le sait.','The first of the two promised inclusion sequences is rewritten using the dual of H^(n-i)(P,Fvee tensor orientation).'])

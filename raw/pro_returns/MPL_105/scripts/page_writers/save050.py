import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{50}
\mspage{14}
\margin{\deleted{\unsure{formulation fausse}\illegible{1}}}
``\uline{Der 6'}'' \inserted{(provisoire)} Si $\mathcal X$ est fibré sur
\[\underline\Psi^{\mathrm{op}}=\underline\Phi=\left(\diagram{\begin{tikzcd}&a\arrow[dl]\\1&\\&b\arrow[ul]\end{tikzcd}}\right)\]
(donc donné par, à $\underline Q$-équiv. près, par un diagramme $\diagram{\begin{tikzcd}&X_0\\\unsure{X_a|X_1}\arrow[ur,no head]\arrow[dr]&\\&X_b\end{tikzcd}}$ dans Cat) alors pour $\xi\in\underline D(\mathcal X)$ constant (voire l.c.)
\[\deleted{\unsure{H\xi}}\quad\psi_!(\sigma)\in\underline D(\underline Q)\]
est non seulement cocartésien (sans mérites), mais aussi cartésien.
\margin{\uline{Axiome des fibrations}}
\[\underline\Phi\subset\underline Q^{\mathrm{op}}=\figure{\begin{tikzpicture}[baseline=0]\node (a) at (0,1){$a$};\node (b) at (0,-1){$b$};\node (one) at (-1,0){$1$};\node (zero) at (1,0){$0$};\draw[->] (a)--(one);\draw[->] (b)--(one);\draw[->] (zero)--(a);\draw[->] (zero)--(b);\draw (-.45,0) ellipse (.95 and 1.35);\end{tikzpicture}}\]
\uline{NB} Der 6' pour $D$ \deleted{\unsure{implique}} n'est autre que Der 6 pour $D^{\mathrm o}$. Je ne vois pas comment l'un impliquerait l'autre, en dehors du cas exceptionnel où il y aurait \deleted{\unsure{comme}\ (\unsure{\forall\xi})} un foncteur dualisant dans $\mathcal A=D(e)$, et une corresp. donnée par dualité entre cohomologie et homologie.

Finalement, il semblerait que le bon axiome, qui englobe Der 6 et Der 6 bis, soit le suivant :
\margin{\uuline{La définition} \deleted{\unsure{abstraite}}}
\margin{``\uuline{l'axiome géométrique}''}
\uline{Der 6} \deleted{\unsure{bis}\illegible{1}} Si $\sigma\in\underline D(\Delta^1\times\Delta^1)$, $\sigma$ est cartésien ssi il est cocartésien.
\inserted{\uline{De plus} (\uline{à moins} que ça n'ait \unsure{rien d'absurde}) :}
Le diagramme squelettique associé est
\mspage{49}
'''
e=[('text','top','14'),('margin note','left top','cancelled formulation'),('deletion','left top','formulation fausse'),('text','top','Der6prime'),('insertion','top','provisoire'),('display','upper','Psi op Phi'),('diagram','upper','a b to1'),('text','upper middle','donc donné'),('diagram','middle left','Xa X0 Xb'),('text','middle right','alors pour xi'),('deletion','middle right','H xi'),('display','middle right','psi shriek sigma'),('text','middle right','est non seulement'),('margin note','left upper','Axiome des fibrations'),('drawing','middle left','Phi subset Qop diamond circled three objects'),('text','lower','NB Der6prime'),('deletion','lower','implique'),('deletion','lower','comme forall xi'),('text','bottom','Finalement'),('margin note','bottom left','La définition'),('deletion','bottom left','abstraite'),('margin note','bottom left',"l'axiome géométrique"),('text','bottom','Der6 Si sigma'),('deletion','bottom','bis word'),('insertion','bottom right','De plus à moins'),('text','bottom','Le diagramme'),('text','bottom','49')]
record_page(50,s,e,notes='Der6prime dual and speculative stronger axiom; exclamation direct-image exponent read !, not prime. Heavy cancelled margin words partly unreadable. Final insertion wording particularly uncertain.')
build_doubts()

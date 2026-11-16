import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{49}
\mspage{12}
$\xi\in\underline D(\mathcal X)$,
considérons (si $\varphi:\mathcal X-\underline\Psi$ \unsure{est} la projection)
\[\sigma_0\overset{\mathrm{déf}}=\varphi_*(\xi)\in\underline D(\underline\Psi)\qquad\deleted{\unsure{H}}\]
\[\sigma=\underline k_*(\sigma_0)\in\underline D(\underline Q),\]
donc
\[\begin{aligned}\sigma(0,0)&\simeq\deleted{\unsure{X_0}}H^\bullet_{\underline D}(X_0,\xi)\\\sigma(0,1)&\simeq H^\bullet_{\underline D}(X_a,\xi)\\\sigma(1,0)&\simeq H^\bullet_{\underline D}(X_b,\xi)\\\sigma(1,1)&\simeq H^\bullet_{\underline D}(\mathcal X,\xi)\end{aligned}\]
et \deleted{diagramme} le carré squelettique associé est
\[(*)\quad\diagram{\begin{tikzcd}&H^\bullet_{\underline D}(\mathcal X,\xi)\arrow[dl]\arrow[dr]&\\H^\bullet_{\underline D}(X_a,\xi)\arrow[dr]&&H^\bullet_{\underline D}(X_b,\xi)\arrow[dl]\\&H^\bullet_{\underline D}(X_0,\xi)&\end{tikzcd}}.\]
(NB $\diagram{\begin{tikzcd}&X_a\arrow[dr]&\\X_0\arrow[ur]\arrow[dr]&&\mathcal X\\&X_b\arrow[ur]&\end{tikzcd}}$ n'a rien de carré, dans $\mathcal X$\ldots $X_a\cap X_b=\varnothing$. Mais $\diagram{\begin{tikzcd}&X_{/a}\arrow[dr,no head]&\\X_{/0}\arrow[ur,no head]\arrow[dr,no head]&&\mathcal X\\&X_{/b}\arrow[ur,no head]&\end{tikzcd}}$ est carré, et le carré (*) est aussi déduit de
\mspage{48}

\mspage{13}
celui-là par $H^\bullet_{\underline D}(-,\xi)$.
L'élément $\sigma\in\underline D(\underline Q)$ est cartésien par construction, donc le ``carré'' (*) aussi. Ça serait le cas pour \uline{toute} cat. $\mathcal X$ \inserted{propre} au-dessus de $\underline\Psi$, sans avoir à le supposer cofibré. Mais le fait que $\mathcal X$ soit cofibré doit donner à ce carré la vertu suppl. qu'il est aussi \uline{cocartésien}. J'ai l'impression que ça ne peut absolument pas découler de l'un des axiomes Der 1 -- Der 5,5' vus jusqu'à présent. Je vais le mettre comme

``\uuline{Der 6}'' \inserted{(provisoire)} \deleted{\unsure{Soit}} \inserted{Si} $\mathcal X$ sur $\underline\Psi$ est cofibré, $\xi$ \deleted{\unsure{constant}}\inserted{quelconque} \deleted{\unsure{considéré, les}} de $\underline D(\mathcal X)$, \deleted{\unsure{le}} l'élément
\[\psi_*(\xi)\in\underline D(\underline Q),\]
\margin{où $\psi=(\mathcal X\xrightarrow{\varphi}\underline\Psi\overset{\underline k}{\hookrightarrow}\underline Q)$\\ $\underline Q=\Delta^1\times\Delta^1$}
est non seulement cartésien, mais aussi cocartésien.
\margin{\unsure{à vérifier que ça devient faux} si $\xi$ quelconque (non loc. const.) \unsure{pas} \deleted{\unsure{constant}} \unsure{découle déjà} \unsure{des axiomes antérieurs}.}
\margin{\uline{Axiome des cofibrations}\\\unsure{Sans doute : ceci devrait être expliqué en termes de carrés cartésiens, à l'aide des axiomes} \unsure{antérieurs} \unsure{Der. 6 de la page qui suit}.}
'''
e=[('text','top left','12'),('text','left top','xi in D'),('text','left top','considérons'),('display','left upper','sigma0 phi star'),('deletion','left upper','H'),('display','left upper','sigma k star'),('text','left middle','donc'),('display','left middle','four sigma values'),('deletion','left middle first value','X0'),('deletion','left middle','diagramme'),('text','left middle','et le carré'),('diagram','left lower middle','(*) H D'),('text','left lower','NB'),('diagram','left lower','X0 Xa Xb Xcal'),('text','left lower',"n'a rien de carré"),('display','left lower','Xa intersection Xb empty'),('text','left bottom','Mais'),('diagram','left bottom','X/0 X/a X/b Xcal'),('text','left bottom','est carré et le carré'),('text','left bottom','48'),('text','right top','13'),('text','right top','celui-là'),('text','right main',"L'élément sigma"),('insertion','right upper','propre'),('text','right lower','Der6'),('insertion','right lower','provisoire'),('deletion','right lower','Soit'),('insertion','right lower','Si'),('deletion','right lower','constant'),('insertion','right lower','quelconque'),('deletion','right lower','considéré les'),('deletion','right lower','le'),('display','right lower','psi star xi'),('margin note','right lower','où psi'),('text','right bottom','est non seulement'),('margin note','gutter lower','à vérifier'),('deletion','gutter lower','constant'),('margin note','bottom right','Axiome des cofibrations')]
record_page(49,s,e,notes='Landscape double12–13; Der6 explicitly provisoire. Lower gutter/bottom marginal handwriting especially poor: several phrase readings tentative, require re-examination. Direct-image operator star; square sigma maintained as previous pages. No expected correction of contradictory tentative axiom.')
build_doubts()

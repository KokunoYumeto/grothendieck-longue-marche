import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{51}
\mspage{15}
\[\diagram{\begin{tikzcd}&\sigma(0,1)\arrow[dl,"j_0"']&\\\sigma(0,0)&&\sigma(1,1)\arrow[ul,"i_1"']\arrow[dl,"j_1"]\\&\sigma(1,0)\arrow[ul,"i_0"]&\end{tikzcd}}\]
\unsure{donc} $\begin{cases}i_1\text{ iso}\Longleftrightarrow i_0\text{ iso},\\j_1\text{ iso}\Longleftrightarrow j_0\text{ iso}.\end{cases}$
\margin{De plus, on doit imposer ceci pour les dérivateurs induits $\underline D_I$ ($I\in\mathrm{Dirg}$), donc dans $\underline D(I\times\Delta^1\times\Delta^1)$.}

Cette dernière assertion résulte de la précédente (car cart. implique $\Rightarrow$, cocartésien implique $\Leftarrow$), \unsure{prouvons pour ceci} :

``\uline{Lemme}'' \deleted{(associé à Der 6)} : si $\xi=\left(\diagram{\begin{tikzcd}&\xi_a\arrow[dl,"j_0"']\\\xi_0&\\&\xi_b\arrow[ul,"i_0"]\end{tikzcd}}\right)$ est un diagramme abstrait tel que $i_0$ soit un iso, alors il est isom. à l'image inverse d'un $\eta\in\underline D(\underline U)$ \deleted{\unsure{\xi}} (où $\underline U=(\unsure{0}\longrightarrow a)$ \inserted{$\simeq\Delta^1$} est l'ouvert canonique gauche de $\underline\Psi$) par la \unsure{rétraction} $\rho$ de $\underline\Psi$ sur $\underline U$.

Il suffit de prouver que
\[\deleted{\unsure{\xi}}\quad\rho^*\rho_*(\xi)-\xi\qquad\text{l'adj.}\]
est iso. Comme $\rho$ est \unsure{bien sûr} lisse, comme induit par $\mathrm{pr}_1:\Delta^1\times\Delta^1-\Delta^1$ sur un ouvert) mais aussi \unsure{propre}, $\rho_*(\xi)$ se calcule fibre par fibre. On utilise que \deleted{\unsure{sur}}
\[\mathcal A\simeq\underline D(e)\longrightarrow\underline D^{\mathrm{lc}}(\Delta^1)\]
est une équiv. de cat. (\uline{forme de Der 3})$^*$
\margin{\deleted{\unsure{Il faut raisonner}\illegible{2}\unsure{ici}}}
\mspage{50}
'''
e=[('text','top','15'),('diagram','top','sigma square'),('display','upper','i1 iso iff i0'),('margin note','right upper','De plus'),('text','middle','Cette dernière assertion'),('text','middle','Lemme'),('deletion','middle','associé à Der6'),('diagram','middle right','xi0 xia xib'),('text','middle lower','est un diagramme abstrait'),('deletion','right lower','xi'),('insertion','lower middle','simeq Delta1'),('text','lower','Il suffit de prouver'),('display','lower','rho star rho star xi'),('deletion','lower display','xi'),('text','lower','est iso Comme rho'),('deletion','bottom','sur'),('display','bottom','A D(e) DlcDelta1'),('text','bottom','est une équiv'),('margin note','left lower cancelled','Il faut raisonner'),('text','bottom','50')]
record_page(51,s,e,notes='Arrowless counit and pr1 stroke retained. Cancelled vertical left note is physically obscured by multiple strokes. Diagram xi definition nearby heavy pointer treated as pointer, not extra morphism.')
build_doubts()

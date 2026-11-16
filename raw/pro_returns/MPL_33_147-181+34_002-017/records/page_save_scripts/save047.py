import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{47}
\mspage{10}
\deleted{(Donc pour le Dérivateur \deleted{\unsure{fort}}\inserted{``complet''}, avec des coeff. \uline{loc.} constants $\xi$ au lieu de constants, il faut supposer que l'application de pr. $X\longrightarrow\overline X$ est $D$-équiv. $2$-complète.}

Pour avoir l'implication inverse
\[i\in W_{\underline D}\Longrightarrow i_0\in W_{\underline D},\]
il faudrait savoir que le diagramme (**), plus \deleted{\unsure{part}} précisément le \deleted{\unsure{i\longrightarrow}} \deleted{diagramme}\inserted{carré} abstrait $\sigma$ qui lui donne naissance, est non seulement cartésien, mais aussi \uline{cocartésien}. ``Moralement'', qu'il soit cartésien me semble être la traduction cohomologique du fait que le \deleted{diagramme}\inserted{carré}
\[\diagram{\begin{tikzcd}&U\arrow[dl]&\\U\cap U'&&X\arrow[ul,no head]\arrow[dl]\\&U'\arrow[ul]&\end{tikzcd}}\quad\text{dans Cat}\]
est \uline{cocartésien} dans un sens suffisamment fort. Mais il est également cartésien, de façon triviale, et on peut s'attendre (sous certaines conditions) que les diagrammes ``transfigurés'' par $H^\bullet_{\underline D}(-,\xi)$ sont cocartésiens\ldots

J'ai envie de regarder d'emblée $X$ comme sur $\underline Q=\Delta^1\times\Delta^1$, plutôt que sur \unsure{l'ouvert} $\underline\Psi=\underline Q-\{e\}$ de $\underline Q$, alors
\[\underline\Psi_{\underline Q}(X)|\underline\Psi\simeq\Psi_{\underline\Psi}(X)\quad\text{déjà considéré.}\]
\mspage{46}
'''
e=[('text','top','10'),('deletion','top block','Donc pour le Dérivateur'),('deletion','top first line','fort'),('insertion','top first line','complet'),('text','upper','Pour avoir'),('display','upper','i in W implies i0'),('text','middle','il faudrait savoir'),('deletion','middle','part'),('deletion','middle','i arrow'),('deletion','middle','diagramme'),('insertion','middle','carré'),('deletion','middle lower','diagramme'),('insertion','middle lower','carré'),('diagram','middle lower','U X Uprime Uintersection'),('text','lower','est cocartésien'),('text','bottom',"J'ai envie"),('display','bottom','Psi Q X'),('text','bottom','46')]
record_page(47,s,e,notes='Expected cocartesian property explicitly unproved. Cancelled opening with local coefficients; several overwritten/cancelled words uncertain. Diagram arrowheads follow ink even where surprising.')
build_doubts()

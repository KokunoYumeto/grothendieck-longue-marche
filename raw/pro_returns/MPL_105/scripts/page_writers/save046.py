import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{46}
\mspage{8}
Donc le diagramme squelettique
\[(*)\quad\diagram{\begin{tikzcd}H^\bullet_{\underline D}(U,\xi)\arrow[dr]&&H_{\underline D}(U',\xi)\arrow[dl,no head]\\&H^\bullet_{\underline D}(U\cap U',\xi)&\end{tikzcd}},\]
\inserted{du type $\underline\Psi^{\mathrm{op}}$,} provient-il d'un diagramme \unsure{concret|ouvert}
\[\sigma_0\deleted{\unsure{\xi_0}}\overset{\mathrm{déf}}=\overline\varphi_*(\unsure{a}_{\overline X})\in\underline D(\underline\Psi).\]
Considérons l'inclusion
\[\underline\Psi\overset{\underline k}{\subset}\deleted{\unsure{*}}\Delta^1\times\Delta^1=\diagram{\begin{tikzcd}&(0,1)\arrow[dr,no head]&\\(0,0)\arrow[ur,no head]\arrow[dr]&&(1,1)\\&(1,0)\arrow[ur]&\end{tikzcd}}\]
déduite de $\Psi$ en lui rajoutant l'élément final manquant $(1,1)$. Soit $\underline k$ l'inclusion, et considérons le ``carré cartésien''
\[\sigma=\underline k_*(\sigma_0)\in\underline D(\Delta^1\times\Delta^1)\]
\deleted{Donc les fibres de $\sigma$ en les points de}
On a
\[\underline k^*(\sigma)\simeq\sigma_0,\]
donc le \deleted{\unsure{fibré diagramme}} squell. induit par $\sigma$ sur $\Psi$ n'est autre que (*), ci-dessus. Mais je dis que le diagramme squelettique sur $\Delta^1\times\Delta^1$ ainsi \inserted{s'identifie :}
\figure{\begin{tikzpicture}\draw (0,0)--(0,.7);\draw (.07,0)--(.07,.7);\draw (.14,0)--(.14,.7);\end{tikzpicture}}
\mspage{45}

\mspage{9}
\[(**)\quad\diagram{\begin{tikzcd}&H^\bullet_{\underline D}(\inserted{\unsure{\overline X|X}},\xi)\arrow[dl,"i^*"']\arrow[dr,"i'^*"]&\\H^\bullet_{\underline D}(U,\xi)\arrow[dr,"i_0'^*"']&&H^\bullet_{\underline D}(U',\xi)\arrow[dl,"i_0^*"]\\&H^\bullet_{\underline D}(U\cap U',\xi)&\end{tikzcd}};\]
\margin{\uline{NB} On a ce carré cartésien, pour $\uline{\forall}\ \xi\in\underline D(\unsure{\overline X|X})$, pas seulement $\xi$ constant\ldots}
Notons pour ceci que si
\[\psi=\underline k\circ\varphi:\overline X\longrightarrow\Delta^1\times\Delta^1=\underline Q\]
\[\sigma=\underline k_*(\sigma_0)=\underline k_*(\varphi_*(\xi_{\overline X}))=\psi_*(\xi_{\overline X}),\]
d'où
\[H^\bullet_{\underline D}(\Delta^1\times\Delta^1,\sigma)\simeq H^\bullet_{\underline D}(\overline X,\xi)\xrightarrow{\sim}H^\bullet_{\underline D}(X,\xi)\]
\inserted{car $\alpha:X\longrightarrow\overline X$ est $\in W$}
D'autre part, comme $e=(1,1)$ élément final de $\Delta^1\times\Delta^1=\underline Q$ donc $e\longrightarrow\underline Q$ asph.,
\[\deleted{\unsure{\theta}}\qquad\underbrace{H^\bullet_{\underline D}(Q,\sigma)}_{H^\bullet_{\underline D}(\inserted{\unsure{\overline X|X}},\xi)}\simeq\sigma(e)=\sigma(1,1)\deleted{\unsure{\leftarrow\cdots}},\]
d'où l'assertion.
Ça doit faire partie, d'autre part, des propriétés générales des carrés cartésiens \inserted{``dans $\mathcal A$''} (comme (**)), que
\[i_0'^*\text{ iso}\Longleftrightarrow i'^*\text{ iso},\]
\margin{\uuline{à vérifier} (ou à \unsure{mettre en axiome} sur les dérivateurs.)}
\deleted{\unsure{Et}} comme \inserted{ceci} est vrai pour $\uline{\forall}\ \xi\in\mathcal A=\underline De$, cela donne
\[i'_0\in W_{\underline D}\Longrightarrow i'\in W_{\underline D}.\]
'''
e=[('text','top left','8'),('text','left top','Donc le diagramme squelettique'),('diagram','left top','(*) H D'),('insertion','left upper','du type Ψ op'),('text','left upper','provient-il'),('display','left upper','sigma0'),('deletion','left upper display','xi0'),('text','left middle',"Considérons l'inclusion"),('display','left middle','Ψ subset Delta'),('deletion','left middle','star under inclusion'),('diagram','left middle','(0,0) (0,1) (1,0) (1,1)'),('text','left middle','déduite de Ψ'),('display','left lower middle','sigma=k star'),('deletion','left lower middle','Donc les fibres'),('text','left lower','On a'),('display','left lower','k star sigma'),('deletion','left lower','fibré diagramme'),('text','left lower','donc le squell.'),('insertion','left bottom',"s'identifie"),('drawing','left bottom','three vertical strokes'),('text','bottom left','45'),('text','right top','9'),('diagram','right top','(**) H D'),('insertion','right top diagram','Xbar'),('margin note','right top','NB On a ce carré'),('text','right upper','Notons pour ceci'),('display','right upper','psi=k circ phi'),('display','right middle','sigma=k star sigma0'),('text','right middle',"d'où"),('display','right middle','H D Delta'),('insertion','right middle','car alpha'),('text','right middle',"D'autre part"),('display','right lower middle','H D Q sigma'),('deletion','right lower middle','theta'),('insertion','right lower middle underbrace','Xbar'),('deletion','right lower middle','left arrow'),('text','right lower',"d'où l'assertion"),('text','right lower','Ça doit faire partie'),('insertion','right lower','dans A'),('display','right lower','i0 prime star iso iff'),('margin note','gutter lower','à vérifier'),('deletion','right bottom','Et'),('insertion','right bottom','ceci'),('text','right bottom','comme est vrai'),('display','right bottom','i0 prime in W implies i prime in W')]
record_page(46,s,e,notes='Landscape double page8–9, folio45. Squelettique/squell. preserved. Diagram-carré argument self-flagged à vérifier with alternative of axiom; first concrete diagram adjective uncertain. Greek sigma and overwritten xi need audit.')
build_doubts()

import sys
sys.path.insert(0,'/workspace/scratch/3b3cef4e0bd3/MPL_105_work/scripts')
from record_page import record_page,build_doubts
s=r'''\scanpage{48}
\mspage{11}
mais la quatrième fibre est
\[\overline X_{(1,1)}=X_{/(1,1)}\simeq X\]
donc le diagramme \inserted{dans Cat} de type $\underline Q$ donnant naissance à $\Psi_{\underline Q}(X)$ n'est autre que
\[\diagram{\begin{tikzcd}&U\arrow[dr,no head]&\\U\cap U'\arrow[ur]\arrow[dr]&&X\\&U'\arrow[ur,no head]&\end{tikzcd}}\]
Mais ce diagramme \inserted{comme ds Cat} n'est bien sûr pas quelconque, sa propriété essentielle, pour les propriétés que nous avons en vue, me semble la suivante :
\[\left(\underbrace{\int\diagram{\begin{tikzcd}&U\\\unsure{V|U\cap U'}\arrow[ur]\arrow[dr,no head]&\\&U'\end{tikzcd}}}_{\substack{\text{déf.}\\\Psi_{\underline\Psi}(X)\text{ en tant}\\\text{qu'objet de Cat sans plus}}}\right)\longrightarrow X\]
\margin{flèche définie pour $\forall$ diagr. comme $\diagram{\begin{tikzcd}&U\arrow[dr,no head]&\\V\arrow[ur]\arrow[dr,no head]&&X\\&U'\arrow[ur]&\end{tikzcd}}$ dans Cat}
est dans $W$. Et le fait général que je \unsure{subodore} est le suivant

``\uline{Principe}'' \unsure{(1)} Soit $\diagram{\begin{tikzcd}&X_a\\X_0\arrow[ur,no head]\arrow[dr,no head]&\\&X_b\end{tikzcd}}$ un diagramme dans Cat du type $\underline\Psi$, soit $\mathcal X$ la cat. cofibrée sur $\underline\Psi$ qu'il définit. Pour tout $\xi$
\margin{\textsf{MédiGraf Montpellier 21999}}
\mspage{47}
'''
e=[('text','top','11'),('text','top','mais la quatrième fibre'),('display','top','Xbar11'),('text','upper','donc le diagramme'),('insertion','upper','dans Cat'),('diagram','upper middle','Ucap Uprime U X'),('text','middle','Mais ce diagramme'),('insertion','middle','comme ds Cat'),('diagram','lower middle','integral V U Uprime to X'),('text','underbrace','déf Psi en tant'),('margin note','right middle','flèche définie'),('diagram','right middle','V U Uprime X'),('text','lower','est dans W'),('text','lower','Principe'),('diagram','lower','X0 Xa Xb'),('text','bottom','un diagramme'),('margin note','printed right edge','MédiGraf Montpellier 21999'),('text','bottom','47')]
record_page(48,s,e,notes='Grey paper ruling and reverse-side show-through not live content. Printed maker text included. Heavily overwritten central diagram object V/Uintersection uncertain. General principle number uncertain.')
build_doubts()

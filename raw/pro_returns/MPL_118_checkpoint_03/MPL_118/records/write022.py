from save_page import save
text=r'''\scanpage{22}
\mspage{3}
% archive foliation: 21

Soit maintenant
\diagram{\begin{tikzcd}
Y\arrow[r,hook,dash]\arrow[d]&X\arrow[d,dash]\\
Y'\arrow[r,hook,dash]&X'
\end{tikzcd}}
diagramme cocartésien dans un $\widehat A$, avec $Y\hookrightarrow X$ mono donc
$Y'\longrightarrow X'$ mono. \inserted{\uline{Il est aussi cartésien}.}
Considérons le diagramme \deleted{cartésien} correspondant dans $\mathrm{Cat}$
\diagram{\begin{tikzcd}
A_{/Y}\arrow[r,hook]\arrow[d]&A_{/X}\arrow[d,dash]\\
A_{/Y'}\arrow[r,hook]&A_{/X'}
\end{tikzcd}}
il est cocartésien (car $i_A:\widehat A\longrightarrow(\mathrm{Cat})$ commute aux
$\varinjlim$) et cartésien (car $i_A$ commute aux produits fibrés) et dont les flèches
sont \unsure{fibrantes}, de plus $A_{/Y}\longrightarrow A_{/X}$ et
$A_{/Y'}\longrightarrow A_{/X'}$ \deleted{sont} des mono fibrants donc des imm. ouvertes.
On est donc dans la situation \unsure{du th. ci-dessus énoncé}, donc
$\deleted{\unsure{\int}}\,A_{/X'}$ \unsure{réalise}
\diagram{$\displaystyle\int\left(\begin{tikzcd}[ampersand replacement=\&]
A_{/Y}\arrow[r]\arrow[d]\&A_{/X}\\A_{/Y'}\&
\end{tikzcd}\right)$},
\margin{\uuline{Thm}}
\uline{Corollaire} Si $(Y\longrightarrow X)\in\underline W$
(resp. $Y\longrightarrow Y'\ \deleted{\unsure{est}}\ \in\underline W$)
alors $(Y'\longrightarrow X')\in\underline W$
(resp. $X\longrightarrow X'\in\underline W$).
'''
e=[('text','top','Soit maintenant'),('diagram','top','Y X Y prime X prime'),('text','upper middle','diagramme cocartésien dans un A hat'),('display','upper middle','Y hook X mono donc Y prime to X prime mono'),('insertion','upper right','Il est aussi cartésien'),('text','middle','Considérons le diagramme correspondant'),('deletion','middle','cartésien'),('diagram','middle','A over Y A over X A over Y prime A over X prime'),('text','lower middle','il est cocartésien car i A commute'),('display','lower middle','i A A hat to Cat; direct limit'),('text','lower middle','et cartésien car i A commute aux produits fibrés'),('display','lower middle','A over Y to A over X and primes'),('deletion','lower middle left','sont'),('text','lower','des mono fibrants donc des imm. ouvertes'),('deletion','lower','integral before A over X prime'),('diagram','lower','integral A over Y to A over X down A over Y prime'),('margin note','bottom left','Thm double underlined'),('text','bottom','Corollaire Si'),('display','bottom','Y to X in W resp Y to Y prime in W'),('deletion','bottom','est'),('display','bottom','Y prime to X prime in W resp X to X prime in W')]
save(22,text,'text',e,'Presheaf pushout with a monomorphism; categories of elements square asserted cocartesian and cartesian using i_A preserving colimits and fiber products, fibers and open immersions. Concluding corollary of W stability. The line between the square discussion and the span integral has a deleted integral-like mark and doubtful reading realise; preserve without repair.')

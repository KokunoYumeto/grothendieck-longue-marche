from record_page import record
record(11,r'''
\scanpage{11}
% archive foliation: 10
Il reste à prouver que si $x\in\overline G(j)$, \deleted{\unsure{alors}} $x$ est acceptable contre $j'$. On va construire une stratégie $\Sigma'$ pour $J'$ qui sera acceptable \deleted{contre} contre $j'$ pour \uline{tous} les $x\in\overline G(j)$.

On pose pour $z\in C(J')$
\[
\Sigma'(z)=\begin{cases}R(z)\text{ si }z\in G(j')\\R(z)\cap\overline G(j')\text{ sinon i.e. }z\in\overline G(j')\end{cases}
\]
C'est \uline{une} $\unsure{J'|J}$ \uline{stratégie} i.e. $R(z)\ne\varnothing\Longrightarrow\Sigma'(z)\ne\varnothing$. Il suffit de le voir pour $z\in\overline G(j')$, donc $z\in\overline C(j')\cap\overline G(\unsure{z'|j'})$, mais on a par la prop. $2^\circ$
\[
\overline C(j')\cap\overline G(\unsure{z'|j'})=\{z\in\overline C(j')\mid\exists y\in R(z)\text{ avec }y\in\overline G(j')\text{ ou }(R(z)=\varnothing\text{ et }z\in\overline G_0(j'))\}
\]
donc, lorsque $R(z)\ne\varnothing$, on voit que $R(z)\cap\overline G(j')\ne\varnothing$, OK.

Prouvons que $\Sigma'$ est acceptable contre $j'$ pour $\forall x\in\overline G(j')$. Soit donc
\[
(x_0=x,x_1,\ldots,x_{\unsure{N|n}})\ \deleted{\text{une}}
\]
\inserted{$x_0\in\overline G(j')$}
''',[
('text','top','Il reste à prouver que si x in Gbar(j)'),('deletion','top','alors; contre'),('text','upper','On va construire une stratégie Sigma prime ... tous les x'),('text','upper-middle','On pose pour z in C(J prime)'),('display','upper-middle cases','Sigma prime(z)=R(z) or R(z) cap Gbar(j prime)'),('text','middle','C’est une J prime stratégie ...'),('display','middle inline','R(z) nonempty implies Sigma prime(z) nonempty'),('text','middle','Il suffit de le voir pour z in Gbar(j prime) ... prop 2 degrees'),('display','lower','Cbar(j prime) cap Gbar(z prime) = set with exists y ... or terminal clause'),('text','lower','donc lorsque R(z) nonempty ... OK'),('display','lower inline','R(z) cap Gbar(j prime) nonempty'),('text','bottom','Prouvons que Sigma prime est acceptable contre j prime'),('display','bottom','(x_0=x,x_1,...,x_N)'),('deletion','bottom-right of tuple','une'),('insertion','below tuple','x_0 in Gbar(j prime)')
],'''The converse uses a coalition policy that stays in the complement of G(j′). The nonemptiness check invokes the second part of the earlier proposition and explicitly carries the terminal exception. Two occurrences of G with an argument resembling z′ rather than j′ are marked as reading doubts. Initial prose appears to omit the prime on j; transcription retains that difference.''')

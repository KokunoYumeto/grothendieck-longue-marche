import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(34,r'''
\scanpage{34}
% archive foliation: 33
\uline{Proposition} \unsure{Soit} $(C,R,J,\hat\alpha,G_0:J\longrightarrow\unsure{\mathcal P|P}(C_0))$ un jeu de position à deux joueurs jouant alternativement, $G\subset C$ et $P\subset C$, l'ens des positions gagnantes resp. perdantes. Soient $\widetilde G,\widetilde P$ deux parties de $C$ ayant les propriétés suivantes
\[
\begin{aligned}
1)\quad&\forall x\in\widetilde G,\quad\exists y\in R(x)\quad\text{tel que }y\in\widetilde P\\
2)\quad&\forall x\in\widetilde P,\quad\deleted{\unsure{\exists}}\unsure{\forall}\,y\in R(x),\quad\text{on a }y\in\widetilde G\\
3)\quad&\forall x\in\widetilde G\cap C_0,\quad\text{on a }x\in G_0(\hat\alpha(x))\\
4)\quad&\forall x\in\widetilde P\cap C_0,\quad\text{on a }x\in G_0(\overline{\hat\alpha}(x))
\end{aligned}
\]
Alors, si dans $C$ il n'existe pas de \deleted{\unsure{jeu}} \inserted{partie} infinie, on a
\[
\widetilde G\subset G,\qquad\widetilde P\subset P
\]
Si de plus on suppose \deleted{\unsure{la réunion disjointe des} deux parties $G_0(j)$ $(j\in J)$, alors on a} \inserted{que $\widetilde G$ et $\widetilde P$ sont complémentaires} l'une de l'\deleted{\unsure{a}}autre, \deleted{\unsure{alors}} et $G_0(j)\cap G_0(\bar j)=\varnothing$ (donc $G\cap P=\varnothing$) alors on a $\widetilde G=G$, $\widetilde P=P$

(et par suite $G\cup P=C$ donc $G_0(j)\cup G_0(\unsure{j'|\bar j})=C_0$)

\uline{Cor} Soit $(C;$ un jeu alterné tel que \deleted{\unsure{G(j)\subset}}

a) Pas de partie infinie \quad b) $C_0$ réunion disjointe des $G_0(j)$ et $G_0(\bar j)$. Soient $\widetilde G,\widetilde P$ deux parties de $C$.

Pour que l'on ait $\widetilde G=G$, $\widetilde P=P$, il f et s. que $\widetilde G$ et $\widetilde P$ soient complémentaires l'une de l'autre, et satisfassent les conditions 1) à 4) ci-dessus.
''',[
('text','top','Proposition Soit (C,R,J,hat alpha,G_0)'),
('display','upper-middle numbered 1','forall x in tilde G exists y in R(x)'),
('display','upper-middle numbered 2','forall x in tilde P forall y in R(x)'),
('deletion','condition 2 before y','exists (overwritten quantifier)'),
('display','middle numbered 3','forall x in tilde G cap C_0'),
('display','middle numbered 4','forall x in tilde P cap C_0'),
('text','middle below conditions','Alors, si dans C il nexiste pas'),
('deletion','before infinie','jeu'),
('insertion','above deleted jeu','partie'),
('display','fold','tilde G subset G, tilde P subset P'),
('text','below fold','Si de plus on suppose'),
('deletion','two lines after suppose','la réunion disjointe des deux parties'),
('insertion','above deleted phrase','que tilde G et tilde P sont complémentaires'),
('deletion','above autre','a'),
('deletion','after lautre','alors'),
('text','lower middle','et G_0(j) cap G_0(bar j) = emptyset'),
('text','parenthesis below','et par suite G cup P = C'),
('text','lower','Cor Soit (C; un jeu alterné tel que'),
('deletion','right of corollary opening','G(j) subset'),
('text','bottom two paragraphs','a) Pas de partie infinie; Pour que lon ait')
],[
('proposition opening','Soit','final letters overwritten','medium'),
('power-set target','mathcal P(C_0)','ordinary P(C_0)','medium'),
('condition 2 quantifier','deleted exists; forall','quantifier altered in place; underlying and replacement uncertain','low'),
('before infinie','deleted jeu','short word heavily crossed out','medium'),
('deleted clause after suppose','la réunion disjointe des','opening is heavily cancelled','low'),
('autre / following deleted word','a; alors','overwritten cancellation fragments','low'),
('last G_0 union','j prime','bar j','medium'),
('corollary opening deletion','G(j) subset','formula fragment heavily cancelled','low')])

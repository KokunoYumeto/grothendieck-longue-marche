import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(46,r'''
\scanpage{46}
% archive foliation: 45
\uline{Cor} \deleted{$A$} Supposons $NA$ nilpotent (p. ex. $A$ noeth). Alors les conditions précédentes sur $u$ équivalent à :

(v) $u$ induit l'identité sur $A_{\mathrm{red}}$

Dans ces conditions, \deleted{\unsure{\exists}} si \deleted{\unsure{t}} $N(A)^{N+1}=0$, les conditions de la prop sont satisfaites pour $(u,N)$, i.e. $\forall$ \unsure{autom.|opérateur} diff de $A$ est d'ordre $\leq N$.

\uline{Cor.} Supposons $A$ une $K$-alg ($K$ une $\mathbf Q$-alg). Si $u=\exp\Theta$ ($\Theta$ dérivation nilpotente) alors $u$ est un $K$-autom ssi $\Theta$ est une $K$-dérivation.

\uline{Cor} Soit $I$ un idéal nilpotent de \deleted{$A$}, $K$-alg. comm. $A$ ($K$ $\mathbf Q$-alg. \unsure{commutative et unifère}\ldots), \inserted{$I^{N+1}=0$,} soit $L_K(A,I)$ l'ens des $K$-dérivations $\Theta$ \deleted{$A$} de $A$ qui induisent $0$ dans $A/I$ (i.e. $\Theta(A)\subset I$), $G_K(A,I)$ le grpe des $K$-autom. de $A$ \deleted{tels} qui induisent l'identité sur \deleted{\unsure{O}} $A/I$ (i.e. $(u-\operatorname{id})(A)\subset I$ i.e. $u(x)-x\in I$ $\forall x\in A$).

Alors a) $\forall\Theta\in L_K(A,I)$, on a $\Theta^{N+1}=0$

(plus généralement, $\forall\deleted{\unsure{k}}i\in\mathbf N$, $\Theta^i A\subset I^i$)

b) $\Theta\longmapsto\exp\Theta:\quad L_K(A,I)\xrightarrow{\sim}G_K(A,I)$
''',[
('text','top','Cor Supposons NA nilpotent'),
('deletion','after first Cor','A'),
('text','upper','(v) u induit lidentité sur A_red'),
('text','upper-middle','Dans ces conditions, si N(A)^(N+1)=0'),
('deletion','before si','exists'),
('deletion','after si','t'),
('text','middle','Cor. Supposons A une K-alg'),
('text','below fold','Cor Soit I un idéal nilpotent'),
('deletion','after de before K-alg.','A'),
('insertion','above soit L_K','I^(N+1)=0'),
('deletion','after K-dérivations Theta','A'),
('deletion','after K-autom. de A','tels'),
('deletion','before A/I','O'),
('text','lower','Alors a) forall Theta in L_K(A,I)'),
('text','bottom parenthesis','plus généralement forall i in N Theta^i A subset I^i'),
('deletion','after forall before i','k'),
('display','bottom','b) Theta maps to exp Theta: L_K(A,I) isomorphism G_K(A,I)')
],[
('Dans ces conditions cancelled marks','exists; t','small overwritten signs','low'),
('after i.e. forall','autom.','opérateur; faint letters, first reading fits visible short word','medium'),
('base algebra parenthesis','commutative et unifère','line break and faint connective difficult','medium'),
('before A/I','deleted O','overwritten round letter','low'),
('general formula quantified index','deleted k then i','index altered in place','medium')])

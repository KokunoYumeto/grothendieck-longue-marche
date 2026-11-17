import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(45,r'''
\scanpage{45}
% archive foliation: 44
\uline{Prop}

$A$ $\mathbf Q$-alg. comm. unif.

$u$ un autom de $\mathbf Q$-alg., $n\in\mathbf N$,

$J$ l'idéal engendré par les $u(x)-x$ $(x\in A)$
\margin{\uline{NB} $u$ induit l'identité sur $\operatorname{gr}_J(A)$}

1) Conditions équivalentes

(i) $u$ op. diff d'ordre $\leq n$

\margin{\deleted{(ii') $u$ \unsure{induit} l'identité}}
(ii) $J^{n+1}=0$

\margin{\deleted{(iii') $\exists\unsure{I\subset A}$ que $I^{n+1}=0$, et que $u$ \unsure{induise} l'identité sur $\operatorname{gr}_I(A)$ \unsure{(0)}}}
(iii) $\exists I$ idéal \inserted{de $A$} tel que $I^{n+1}=0$, et que $u$ induit l'identité dans $A/I$, i.e.
\[
\uline{$ux-x$}\in I\qquad\forall x\in A\qquad[\text{i.e. }I\supset J]
\]
\deleted{(iv)} \inserted{Pour ceci, il \uline{suffit} que $(u-\operatorname{id})^{n+1}=0$, ou (ce qui revient au \unsure{même})}
$\exists$ dérivation $\Theta:A\longrightarrow A$ avec
\[
\Theta^{n+1}=0,\qquad u=\exp\Theta
\]
\margin{est-ce nécessaire ?}

\deleted{\uline{NB} Si $N(A)$ est nilpotent, \unsure{ces condts sont équivalentes}}

2) L'application
\[
\Theta\longmapsto\exp\Theta
\]
est une bijection de l'ens des dérivations $\Theta$ de $A$ telles que $\Theta^{n+1}=0$, dans l'ens des autom $u$ de $A$ \inserted{\unsure{tels|telles} que $(u-\operatorname{id})^{n+1}=0$ (\unsure{donc}} satisfaisant les conditions équivalentes plus haut).

\uline{Cor} Conditions équivalentes sur autom $u$

(i) $u$ op. diff

(ii) $J$ idéal nilp.

(iii) $\exists I$ nilpotent tel que $u$ induise $\operatorname{id}_{A/I}$

(iv) $\exists\Theta$ dérivation, nilpotente, telle que $u=\exp\Theta$

De plus, $\Theta\longmapsto\exp\Theta$ est une bij de l'ens des dérivations nilpotentes de $A$, et l'ens des autom \inserted{de $A$} qui sont des op. diff.
''',[
('text','top heading','Prop; A Q-alg. comm. unif.'),
('text','upper','u un autom de Q-alg. n in N'),
('text','upper','J lidéal engendré par les u(x)-x'),
('margin note','top right','NB u induit lidentité sur gr_J(A)'),
('text','upper','1) Conditions équivalentes'),
('text','upper condition i','u op. diff dordre <=n'),
('deletion','left upper margin','(ii prime) u induit lidentité'),
('display','upper condition ii','J^(n+1)=0'),
('deletion','left middle margin','(iii prime) exists I ... gr_I(A)'),
('text','middle condition iii','exists I idéal tel que I^(n+1)=0'),
('insertion','above idéal tel','de A'),
('display','middle','ux-x in I forall x in A; I superset J'),
('deletion','middle old condition label','(iv)'),
('insertion','above derivation clause','Pour ceci il suffit que (u-id)^(n+1)=0 ou'),
('text','middle','exists dérivation Theta: A to A avec'),
('display','middle','Theta^(n+1)=0, u=exp Theta'),
('margin note','right middle','est-ce nécessaire ?'),
('deletion','above fold full line','NB Si N(A) est nilpotent ces condts sont équivalentes'),
('text','above fold','2) Lapplication'),
('display','fold','Theta maps to exp Theta'),
('text','below fold','est une bijection de lens des dérivations'),
('insertion','above satisfaisant','tels que (u-id)^(n+1)=0 (donc'),
('text','lower','Cor Conditions équivalentes sur autom u'),
('text','lower condition i','u op. diff'),
('text','lower condition ii','J idéal nilp.'),
('text','lower condition iii','exists I nilpotent tel que u induise id_A/I'),
('text','lower condition iv','exists Theta dérivation nilpotente'),
('text','bottom','De plus Theta maps to exp Theta est une bij'),
('insertion','bottom under autom','de A')
],[
('cancelled upper-left note','u induit lidentité','letters under diagonal strike','medium'),
('cancelled middle-left alternative','exists I subset A; induise; (0)','substantial cancellations; terminal parenthesis/zero especially uncertain','low'),
('insertion ending au ...','même','written with two horizontal strokes','medium'),
('deleted NB line','ces condts sont équivalentes','faint beneath long deletion; abbreviation / verb uncertain','low'),
('insertion in bijection paragraph','tels que; donc','telles que; last parenthetical word unclear','low')])

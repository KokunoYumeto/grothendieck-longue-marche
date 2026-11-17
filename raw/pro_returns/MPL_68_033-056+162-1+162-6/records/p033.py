import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(33,r'''
\cotefile{68}
\scanpage{33}
% archive foliation: 32
\[
\left\{\begin{aligned}
G\cap(C\setminus C_0)&=\unsure{G^*|G^\times}\\
P\cap(C\setminus C_0)&=\unsure{P^*|P^\times}\\
C\setminus(G\cup P)&=N
\end{aligned}\right.
\qquad\text{(positions nulles, i.e. gagnantes pour aucun des deux joueurs)}
\]
Une position $x$ sera encore dite \uline{gagnante} (resp. \uline{perdante}) si $x\in G$ (resp. $x\in P$) --- cette terminologie coïncide avec la précédente si $x\notin C_0$. On aura, posant
\[
\deleted{\unsure{G(j)=\text{face}}}
\]
\[
\hat C(j)=\{x\in C\mid\unsure{\hat\alpha}(x)=j\}
\]
(de sorte que $C$ \unsure{apparait|apparaît} comme réunion disjointe des deux ens. $\hat C(j)$, $j\in J$),
\[
\left\{\begin{aligned}
G(j)\cap\hat C(j)&=\deleted{\unsure{\hat\alpha}}\ \hat C(j)\cap G\\
G(j)\cap\hat C(\bar j)&=\hat C(\bar j)\cap P
\end{aligned}\right.
\]
donc \inserted{les} $G(j)$ $(j\in J)$ se \unsure{reconstituent} à partir de $\unsure{\hat\alpha}$ et des ensembles $G,P$.

On aura, pour $x\in C\setminus C_0$
\[
\begin{aligned}
x\in G&\Longleftrightarrow\exists y\in R(x)\ \inserted{\text{tel que}}\ y\in P
&&\text{i.e. }R(x)\cap P\ne\varnothing\\
x\in P&\Longleftrightarrow\forall y\in R(x),\ \text{on a }y\in G
&&\text{i.e. }R(x)\unsure{\subset|\in}G
\end{aligned}
\]
i.e.
\[
\begin{aligned}
G\cap(C\setminus C_0)\deleted{\unsure{G}}&=\{x\in C\setminus C_0\mid R(x)\cap P\ne\varnothing\}\\
P\cap(C\setminus C_0)&=\{x\in C\setminus C_0\mid R(x)\subset G\}
\end{aligned}
\]
''',[
('display','top','G cap (C minus C_0) = G star; P star; N'),
('text','top right','positions nulles, i.e. gagnantes'),
('text','upper middle','Une position x sera encore dite gagnante'),
('deletion','above hatted-C definition','G(j)=face (doubtful)'),
('display','middle','hat C(j) = {x in C | hat alpha(x)=j}'),
('text','middle','de sorte que C apparait'),
('display','below fold','G(j) cap hat C(j); G(j) cap hat C(bar j)'),
('deletion','first equality after equals','hat alpha (doubtful)'),
('text','lower middle','donc les G(j)'),
('insertion','lower middle after donc','les'),
('text','lower','On aura, pour x in C minus C_0'),
('display','lower','x in G iff; x in P iff'),
('insertion','existential line between R(x) and y in P','tel que'),
('text','bottom left','i.e.'),
('display','bottom','G cap (C minus C_0); P cap (C minus C_0)'),
('deletion','bottom first equality before equals','G (doubtful)')
],[
('top display','G^*, P^*','G^times, P^times','medium'),
('deleted line above definition','G(j)=face','cancellation incompletely deciphered; every discernible stroke represented by tentative reading','low'),
('definition / reconstruction','hat alpha','hatted a-like player map; Greek alpha not entirely certain','medium'),
('parenthesis','apparait','apparaît','medium'),
('first intersection equality, deletion','hat alpha','overwritten formula fragment','low'),
('paragraph after intersections','reconstituent','verb ending and central strokes faint','medium'),
('right-hand universal reformulation','subset','in','medium'),
('bottom first equality, deletion','G','cancelled symbol compressed against preceding parenthesis','low')])

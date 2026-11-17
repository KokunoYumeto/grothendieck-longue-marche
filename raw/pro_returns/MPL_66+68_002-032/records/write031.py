from record_page import record
record(31,r'''\scanpage{31}
\deleted{Supposons}
\uline{NB}\quad $G(j),G(j')$ et $N(j)$ sont connus quand on connaît (en plus des \inserted{parties} $G_0(j)$ et $G_0(j')$ de $C_0$) les ensembles
\[
\left\{\begin{aligned}
G^*&=\{x\in C\setminus C_0\mid x\in G(\alpha(x))\}\\
P^*&=\{x\in C\setminus C_0\mid x\in G(\bar\alpha(x))\}
\end{aligned}\right.
\]
où $\bar\alpha(x)$ désigne l'unique $j'\in J$ tel que $j'\ne j=\alpha(x)$.

On dit qu'une position $x\in C\setminus C_0$ qui est $\in G^*\inserted{\text{ (resp. }\in P^*\text{)}}$, i.e. \deleted{telle} \inserted{gagnante} \unsure{pour} le joueur qui a l'\unsure{initiation|initiative} (resp. pour le joueur qui n'a pas l'initiative) est \uline{gagnante} (resp. \uline{perdante}); on dit que c'est une \uline{position nulle} \deleted{autrement} si elle n'est ni gagnante, ni perdante, on pose
\[
N^*=(C\setminus C_0)\setminus(G^*\cup P^*)=N\cap(C\setminus C_0)
\]
(où $N$ est défini dans le corollaire ci-dessus).

On aura
\[
\left\{\begin{aligned}
G(j)\cap C(j)&=G^*\cap C(j)\\
G(j)\cap\bar C(j)&=G(j)\cap C(j')=P^*\cap C(j')\\
G(j)\cap C_0&=G_0(j)
\end{aligned}\right.
\]
ce qui montre que \inserted{les} $G(j)$ $(j\in\unsure{G|J})$ se reconstituent par la connaissance de $G^*,P^*$ et des $G_0(j)$ $(j\in J)$.

Supposons qu'on ait une application
\[
\hat\alpha:C\longrightarrow J
\]
prolongeant $\alpha$, et qu'on ait, pour $\forall x\in C$ et $y\in R(x)$
\[
\hat\alpha(y)\ne\hat\alpha(x)
\]
% archive foliation: 30
''',[
('deletion','top','Supposons'),
('text','top','NB G(j),G(j′) et N(j) sont connus ...'),
('insertion','upper','parties'),
('display','upper','G*={x∈C minus C_0|x∈G(α(x))}; P*={...G(bar α(x))}'),
('text','upper middle','où bar α(x) désigne l’unique j′∈J ...'),
('text','middle','On dit qu’une position ... gagnante, perdante, nulle ...'),
('insertion','middle right','resp. ∈P*'),
('deletion','middle right','telle'),
('insertion','middle left','gagnante'),
('deletion','middle lower','autrement'),
('display','middle lower','N*=(C minus C_0) minus (G* union P*)=N∩(C minus C_0)'),
('text','lower','où N est défini ... On aura'),
('display','lower','three reconstruction equalities for G(j)'),
('text','lower','ce qui montre que les G(j) ... se reconstituent ...'),
('insertion','lower','les'),
('text','bottom','Supposons qu’on ait une application'),
('display','bottom','hat α:C→J'),
('text','bottom','prolongeant α ... pour ∀x∈C et y∈R(x)'),
('display','bottom edge','hat α(y)≠hat α(x)')
],'''Defines relative-to-mover winning/losing/neutral sets G*, P*, N* and gives reconstruction of each player’s absolute winning set, with terminal winning data supplied separately. N(j) in the initial NB is the actual notation despite the preceding N. The final paragraph adds an extension hat α to terminals with alternating colors on every move; this is an extra hypothesis, not implicit in the general game definition. One occurrence of initiative may read initiation and is marked, as is the apparent index set G instead of J after the reconstruction equations.''')
